# Claude review of ChatGPT S2-I3 design v0.2 and Stage 2 v0.7 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude

Subject:

- `S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_2_FOR_CLAUDE_REVIEW.md`
- `Stage2_Experiment_Design_v0_7_FOR_CLAUDE_REVIEW.md`
- the accompanying v0.6-to-v0.7 patch

Baseline: `6e7b5c53df1c65775524936fc945c449cc9fa100`.

## 1. Verdict

**Not yet ratifiable.** There are two MUST findings, both small to fix. Everything else is sound and close to final.

- **Package integrity:**
  - the manifest hashes match;
  - all files are US-ASCII CRLF;
  - the v0.6 base hash `6178a4f1...0b77` (LF) matches the repository file.
- **Patch coverage:** it covers sections 0-3, 6.3, 8.4, 9.1, 10, 13.3, 18, 19, 22 and 23 as stated.
- **The content groups, fold logic, protection of hold-out content and the QP treatment are correct.**

**The main finding is positive.** Review item 1 asked for an independent, mechanistic proof of alignment for the weak sources. That proof now exists (section 2). It is exact by the MPEG-2 standard, has no tunable threshold, and passed on all eight development sources, including the four the S2-I2 thresholds could not settle. It also closes the S2-I2 temporal-slip limitation.

## 2. Registration admission: an orthogonal, exact proof (answers review item 1)

### 2.1 Mechanism

In an MPEG-2 **P picture**, a **skipped macroblock** has:

- motion vector zero;
- frame prediction (for frame pictures);
- no residual.

MPEG-2 has no in-loop filter. Its decoded 16x16 luma block must therefore be **bit-identical** to the co-located block of the forward reference picture, which is the preceding I or P picture in display order.

So for every P-skip macroblock the index identifies, and only if index and pixels are registered spatially **and** temporally:

```
Y[n][16*my : 16*my+16, 16*mx : 16*mx+16] == Y[ref(n)][same window]   (exactly)
```

This test has the following properties:

- It uses coding-mode semantics plus decoder exactness. It uses no blockiness, no FRAME/FIELD contrast and no QP-dependent signal, so it is orthogonal to every S2-I2 test.
- It needs no tunable threshold. The requirement is **100% exact identity at the indexed position**, which the standard guarantees whenever registration is correct.
- Any spatial shift moves the window onto pixels outside the guarantee. Any temporal slip compares against the wrong picture. Either way, exact identity can then survive only by coincidence of perfectly static content, which the controls in section 2.2 measure.
- It is equally valid at 720 and 704 width, at QP 14 or QP 62, and with any FRAME/FIELD mix.

### 2.2 Review rehearsal on all eight development sources

Claude decoded each source with FFmpeg and paired it with its index. The LP pair used the accepted LP index and the S2-I2 LP_blocky index (`b3f1d714...`); the other six used the scratch indexes from the previous review. No filtering was done and no hold-out content was used. The media were deleted afterwards.

The table uses these terms:

- **Exact @ true position:** P-skip blocks bit-identical to the true reference at the indexed position.
- **Shifted:** the same windows offset by +/-1, 2, 4, 8 or 16 px horizontally or vertically, or diagonally.
- **Wrong-reference controls:** the same windows compared against an older anchor, the next frame, or the previous frame (where that frame is not the reference).

| Source | P-skip MBs | Exact @ true position | Minimum per-P-frame | Best shifted window | Wrong-reference controls (older anchor / next / previous) |
|---|---:|---:|---:|---:|---|
| XP | 1619 | **100.000%** | 100% | 48.9% | 15.1% / 77.9% / 83.9% |
| XP_blocky | 25635 | **100.000%** | 100% | 73.2% | 37.6% / 14.8% / 22.3% |
| SP | 1764 | **100.000%** | 100% | 45.2% | 14.8% / 69.9% / 77.7% |
| SP_blocky | 19010 | **100.000%** | 100% | 73.4% | 33.8% / 17.7% / 29.6% |
| LP | 1533 | **100.000%** | 100% | 40.3% | 18.1% / 82.8% / 94.8% |
| LP_blocky | 20300 | **100.000%** | 100% | 69.2% | 36.3% / 15.1% / 24.3% |
| 3A (704x576) | 8812 | **100.000%** | 100% | 93.1% | 83.0% / 86.1% / 96.7% |
| 3A_blocky (704x576) | 18190 | **100.000%** | 100% | 78.6% | 47.1% / 36.4% / 47.2% |

Every source passes, including SP, SP_blocky and 3A, which the S2-I2 thresholds could not settle. Every shifted window and every wrong-reference control falls below 100%.

3A shows why the requirement must be exact identity rather than a margin: its static content keeps some shifted and temporal controls high (up to 96.7%), yet none reaches 100%.

**Disclosure.** Claude ran this test after seeing the S2-I2 outcomes. It is not fitted to them: its pass condition is fixed by the decoding standard, not chosen, and it was applied identically to all eight sources. It is written into the design before any filtering run.

### 2.3 Proposed admission rule (replaces v0.7 section 6.3 items 3-5 and S2-I3 v0.2 section 3.1's provisional thresholds)

1. **HARD structural checks** (unchanged from v0.7 6.3 item 1).
2. **HARD exact P-skip identity in the actual BestSource pipeline**, using the owner's authoritative Windows index:
   - every P-skip macroblock in every quality-eligible P picture is bit-identical to its forward reference at the indexed position;
   - for every one of the declared shifted windows (the seven S2-I2 known-bad offsets plus +/-1 and +/-2 px horizontal and vertical, and one diagonal), the shifted-window identity rate is below 100%;
   - each wrong-reference control (older anchor, adjacent frames) is below 100%.
3. **Applicability minimum:** at least 200 P-skip macroblocks across at least 10 P pictures. This is a robustness floor, not a fitted cutoff; the smallest development source has 1533. Below it, the source is INCONCLUSIVE.
4. **Outcomes:**
   - **any** non-identical block at the true position is **REGISTRATION FAIL**, a hard stop (no tolerance);
   - all conditions met is **REGISTERED**;
   - too few skips is **INCONCLUSIVE - QUALITY BLOCKED**.
5. **S2-I2 tests (3x3, column, row):** they still run on every source with their **original thresholds unchanged**. They are reported as diagnostics, with their known applicability limits stated. They are not admission gates for new sources, and their historical LP and LP_blocky results are unaffected.
6. **Drop the proposed applicability thresholds:** the >=64-MB, >=10% and 2/3-frame figures are no longer needed, and should not be ratified as invented numbers.

Two further notes:

- **Temporal slip:** this test also detects the one-frame slip that S2-I2 could not catch. That limit is now covered for every source.
- **Field swap:** a field swap applied consistently to both pictures would still go undetected. Keep that stated as a limit.

## 3. Findings

### MUST

**M1. Identity.**

- S2-I3 v0.2 line 4 appends a place name to the date. That place is the owner's location, which D-23 (owner-identity amendment) prohibits in any committable file.
- Remove it; use the date only.
- Claude missed the same place name in v0.1's header during the previous review, and owns that miss.
- Stage 2 v0.7 is clean.

**M2. Registration admission.**

- Replace v0.7 section 6.3 items 3-5 and S2-I3 v0.2 section 3.1's provisional 3x3 applicability thresholds with the rule in section 2.3.
- Make the P-skip identity test a mandatory Phase 0 preflight on every source, run in the owner's BestSource pipeline before any quality run.
- Delete the "orthogonal proof still to be designed" blocking item (S2-I3 section 8; v0.7 sections 6.3 and 19). It is now designed.
- Record Claude's rehearsal table as non-authoritative evidence. The owner's Windows run is the authoritative admission.

### SHOULD

**S1. Stale operative text in v0.7.**

- **Section 21** ("v0.4 review scope") still says, in the present tense: "LP, EP, 4A, 2A and MLS roles remain exactly as ratified" and "XP, SP, 3A and their `_blocky` copies remain unassigned/spare".
  - That contradicts section 3.
  - Retitle it "Historical: v0.4 review scope (superseded by section 3 of v0.7)", or delete it with a change-log note.
- **Section 5.2** requires a "matching Stage 1 index record". Development sources now use validated non-baseline scratch indexes.
  - Reword it to "matching validated index (accepted Stage 1 baseline or section 6.3-admitted scratch index)".
  - Keep every rejection rule.
- **Section 15:** "This check applies only to the software-transcode pairs" is correct. Add "including the four development pairs".

**S2. Comparator arms must be compared on identical folds.**

- The L and LB arms (LP-only and LP-pair) are N/A on the LP fold.
- Any comparison of J, O or X against L or LB must therefore use only the XP, SP and 3A folds for **all** arms, never J over four folds against L over three.
- State this in v0.7 section 8.4 and S2-I3 section 4.2.

**S3. Selection bias in the cross-validation is acknowledged, not removed.**

- Choosing among arms or procedures using the cross-validation results makes the chosen procedure's cross-validation score optimistic.
- Add one sentence: the cross-validation figures rank procedures; the unbiased estimate comes only at S2-I8.

**S4. Admission indexes for reproducibility.**

- The admission evidence must record the hashes of the six new development scratch indexes and of LP_blocky's.
- Whether to **track** them in Git as non-baseline development indexes is the owner's decision. Recommend tracking, because eight-source runs cannot be reproduced without them.
- Either way, they are never Stage 1 baselines.

**S5. S2-I4 scope boundary.**

- The symmetric tuned comparison reuses S2-I3's fold machinery. State explicitly that S2-I3 runs **fixed-QP only**: no real-QP branch is fitted and no QP comparison is reported in S2-I3.
- With that sentence, v0.7 Step 3 and section 19 are consistent and nothing from S2-I4 leaks into S2-I3.

### OPTIONAL

**O1.** Note in the cross-validation section that S2-I2's descriptive statistics on LP and LP_blocky, and Claude's preflights, were seen earlier. They are unfiltered structural or registration data, so they do not bias kernel selection.

**O2.** In section 9.1's verified examples, mark EP 14 as "hold-out metadata (known from Stage 1; no filtering)" to avoid any implication of use.

## 4. Checks that passed (review items 2-7)

**Item 2 - grouped cross-validation.**

- **Fold structure:**
  - whole-group folds, with both encodes of a group always in the same fold, so there is no paired-content leakage;
  - screening, shortlisting and tuning are rerun per fold, and held-out results never feed back into their own fold;
  - L and LB are correctly N/A on the LP fold.
- **Weighting:** 2:1 original-to-blocky within each group, with groups equal. That is consistent with D-26 and is declared before results.
- **Final fit:** the joint K0 is fitted on all eight, with O and X kept as frozen comparators that are never silently substituted.

**Item 3 - S2-I4.** The two estimands are correctly separated and labelled: the frozen-K0 QP-only switch, which is in-sample, and the symmetric tuned comparison inside the cross-validation folds. Only the originals carry QP information. S2-I4 is not run in S2-I3; S5 makes that explicit.

**Item 4 - authority.** Sections 2, 3, 8.4, 9.1, 10, 13.3, 18, 19, 22 and 23 are consistent. No LP-only or even/odd rule remains operative. The even/odd split survives only as in-sample stability reporting. The exceptions are the stale section 21 and the section 5.2 wording (S1).

**Item 5 - per-source facts.**

- Geometry comes from each index: 3A is 44x36 MBs, 704x576, and nothing is hard-coded.
- The native pairings are correct.
- Leading-B handling is correct: excluded from quality evidence, and included in the descriptive Q_fixed population, consistent with LP's Stage 1 value of 18.
- Q_fixed values are verified: XP 14, SP 16, LP 18, 3A 14, every blocky 62. The coded-only 16 is barred.
- Hard FAIL is kept separate from INCONCLUSIVE.
- The six frozen indexes are untouched.

**Item 6 - protection and controls.**

- EP, 2A and 4A are locked together with their `_blocky` copies until S2-I8.
- MLS and MLS_blocky are post-freeze controls, with the MLS_blocky metadata condition reported rather than normalised away.
- The all-16 census sits at S2-I8, after the final freeze (S2-I5/S2-I7), not merely after the S2-I3 K0.
- NOTICE and Restricted Media rules are intact.

**Item 7 - options.**

- All register entries are preserved, including M4a, labelled as distinct from the ratified M4.
- B0 is the only initial setting; B1 needs a separate owner decision.
- G1/G2 are read-only aggregates.
- No-harm measures include off-support change, clamping, and edge/texture change.

## 5. Design fixes versus implementation preflight

**Design fixes** (ChatGPT revises, Claude reviews, the owner ratifies v0.7 and S2-I3 v0.3): M1, M2, S1-S5, and O1-O2 as accepted.

**Implementation preflight** (the first authorised S2-I3 run, before any quality run):

- generate the Windows scratch indexes for the six new sources and record their hashes;
- run the hard structural checks and the exact P-skip identity admission in the BestSource pipeline on all eight sources;
- run the S2-I2 diagnostics as reports;
- run the cross-file frame-correspondence proof for the four pairs (section 15).

Any FAIL stops the campaign. None of these is a filtering run.
