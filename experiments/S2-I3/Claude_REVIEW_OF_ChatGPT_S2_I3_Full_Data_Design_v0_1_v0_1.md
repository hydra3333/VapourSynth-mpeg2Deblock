# Claude review of ChatGPT S2-I3 full-data multi-source design v0.1 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: `S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_1_FOR_CLAUDE_REVIEW.md`
Baseline: repository commit `6e7b5c53df1c65775524936fc945c449cc9fa100`; Stage 2 Experiment Design v0.6; Decisions v1.2.

## 1. Verdict

The direction is right, but the draft is **NOT READY TO RATIFY**. There are four MUST findings.

The draft moves from "tune on half of one clip" to "use complete real recordings", which is what the owner asked for. Its development data, however, is still **one piece of content**: LP plus LP_blocky, a software re-encode of the same pictures. The owner's stated requirement is development and testing across a *range* of real inputs, not one input or one type of input. The draft does not yet meet that.

The evidence in section 2 shows that a properly multi-source design is feasible with the samples already in the repository. Section 4 proposes the structure: grouped cross-validation by content.

## 2. Preflight evidence (read-only; requested as review item M3)

**What Claude ran.** Under the owner's development-media authorisation, Claude ran the same read-only checks as S2-I1 and S2-I2 on seven non-hold-out recordings:

- stream properties;
- a scratch index from the frozen inspector source, built via a regular `.m2v` file (no pipe);
- the reader's structural summary;
- picture-type correspondence;
- the S2-I2 registration gate, run through the unchanged S2-I2 engine on FFmpeg-decoded frames.

**What Claude did not do:**

- no filtering;
- no look at descriptive detectability statistics;
- no contact with EP, 2A or 4A originals or their `_blocky` copies.

The indexes are non-baseline scratch files. The decoded media were deleted afterwards.

| Source | Size | Frames | Leading B | FRAME / FIELD / NONE (MBs) | QP median (all MBs) | Picture-type match | S2-I2 gate |
|---|---|---|---|---|---|---|---|
| LG_576i_1_XP | 720x576, interlaced | 228 | 0,1 | 44725 / 261966 / 62669 | 14 (2-72) | PASS | PASS |
| LG_576i_1_XP_blocky | 720x576, interlaced | 228 | none | 50279 / 46997 / 272084 | 62 const | PASS | PASS |
| LG_576i_2_SP | 720x576, interlaced | 192 | 0,1 | 18246 / 228258 / 64536 | 16 (1-72) | PASS | BLOCKED (3x3 INCONCLUSIVE) |
| LG_576i_2_SP_blocky | 720x576, interlaced | 192 | none | 37273 / 63506 / 210261 | 62 const | PASS | BLOCKED (3x3 INCONCLUSIVE) |
| TEST_3A_A002 | **704x576**, interlaced | 300 | none | 322593 / 36022 / 116585 | 14 (1-56) | PASS | BLOCKED (row INCONCLUSIVE) |
| TEST_3A_A002_blocky | **704x576**, interlaced | 300 | none | 79897 / 109602 / 285701 | 62 const | PASS | PASS |
| LG_576i_5_MLS_blocky | **352x288**; progressive_frame=0 | 420 | none | 35819 / 230 / 130271 | 62 const | PASS | BLOCKED (3x3 FAIL) |

All seven sources:

- consist of frame pictures only, in 4:2:0;
- have indexes of exactly the expected size;
- give inspector exit code 0;
- catch all 7 known-bad offsets.

Registration detail:

| Source | 3x3: C00 / best other / frame fraction | Column margin | Row margin / frame fraction |
|---|---|---|---|
| XP | 6.53 / 4.95 / 0.83 | 36.5% | 12.5% / 0.84 |
| XP_blocky | 1.22 / 0.11 / 0.73 | 47.7% | 29.9% / 0.91 |
| SP | 7.09 / 5.98 / **0.59** | 45.8% | 18.2% / 0.86 |
| SP_blocky | **-0.32 / -0.66** / 0.51 | 58.3% | 37.0% / 0.97 |
| 3A | 6.98 / 5.71 / 0.73 | 28.4% | **5.2% / 0.61** |
| 3A_blocky | 2.48 / 0.96 / 0.84 | 48.4% | 21.6% / 0.95 |
| MLS_blocky | **0.20 / 0.43** / 0.17 | 30.2% | 28.9% / 0.66 |

### Scratch index SHA-256 (frozen-inspector source, gcc build; non-baseline)

```
4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127  LG_576i_1_XP.idx
8d0326b5975b19b36742717a80be9eaf11bc21f379f2855eb22651e94dd16b20  LG_576i_1_XP_blocky.idx
40a97ce1a9920cd63e45da13371e0b41ff1619fed688d6145899a300463cc5d9  LG_576i_2_SP.idx
7e19ca6078075e7bf7a3a34bcda0816267e4d38ad02a56e01b6b0ed726ace746  LG_576i_2_SP_blocky.idx
9a60a8d24a7e4a45cbe82b4f41d232ede0e5c00624e82a8f8099f61351957f33  TEST_3A_A002.idx
e6f556dd4aaed0f4709b7c011fcf045193dccbb8abd2a01c646dddf0da893c83  TEST_3A_A002_blocky.idx
915bee8ce95ea9fa58d283b38ba445427a7ab7402ee15e71e6c9dd38ab46d1da  LG_576i_5_MLS_blocky.idx
```

The S2-I2 precedent (LP_blocky `b3f1d714...`) showed the gcc build reproduces the Windows inspector byte-for-byte. The owner's own Windows generation should nevertheless be the authoritative step.

## 3. Findings

### MUST

**M1. The development data must span different content, not one clip and its re-encode.**

- Paths A, B and C all develop on LP content only. LP_blocky is the same pictures re-encoded by software at QP 62. The draft itself notes this "related-source" dependence.
- **This contradicts two things:**
  - the owner's explicit requirement;
  - Stage 2 v0.6 section 3.1's own criterion, "consistency across materially different recorder modes".
- **Available instead:** the repository already holds four non-hold-out content groups, each with a real original and a `_blocky` re-encode:
  - LG XP;
  - LG SP;
  - LG LP;
  - TEST 3A.
- **Fix:** adopt the structure in section 4.

**M2. Remove the "same dimensions as LP" requirement. Its premise is wrong.**

- `TEST_3A_A002_blocky`, which the draft nominates, is **704x576**. It would be rejected under the draft's own rule, and so would the whole TEST series, including the 2A and 4A hold-outs.
- The method is index-driven. Geometry comes from each source's own index, so frame width does not matter, provided the source is MB-aligned, uses frame pictures and is 4:2:0. The S2-I2 engine already handles any such size.
- **Requirement instead:** the prototype must never assume 720 or 45 MB columns.
- `MLS_blocky` (352x288) is a different case; see S6.

**M3. Per-source registration acceptance needs a ratified rule before any new source is used.**

- Four of the seven sources did not PASS the S2-I2 thresholds, which were calibrated on LP. In every case both phase tests behaved, and all seven known-bad offsets were caught.
- The causes are the tests' preconditions, not misregistration:
  - **SP:** zero shift is the strict best, with a 15.7% margin. However, FRAME is only 7% of SP's coded MBs, so the per-frame FRAME-minus-FIELD contrast is noisy and the frame fraction is 0.59.
  - **SP_blocky:** FRAME-minus-FIELD contrast is negative at every shift, so the D-map premise does not hold for this encode. Zero shift is still the best.
  - **3A:** lightly quantised (median QP 14), so its row-phase signal is weak. Margin 5.2%, frame fraction 0.61.
  - **MLS_blocky:** only 230 FIELD MBs in 420 frames, so the 3x3 FRAME-vs-FIELD test is inapplicable.
- **Required rule:** the owner should ratify a source-independent acceptance rule grounded in each test's preconditions. For example:
  - column and row phase tests mandatory;
  - all known-bad offsets caught;
  - the 3x3 test required only where both FRAME and FIELD populations exceed a declared minimum per frame.
- **Disclosure:** Claude has seen these outcomes. The rule must therefore be justified by mechanism (population size, signal strength) and applied identically to every source, including those that already PASS.
- **Do not lower thresholds** until the four listed sources pass.

**M4. Authority: replace Stage 2 v0.6 with a versioned v0.7. Do not use an appendix.**

- The changes alter sample roles, the development and evaluation sequence, and the S2-I3, S2-I4 and S2-I5 definitions. Under D-23 a revision is a new versioned file.
- Sections affected in v0.6:
  - **section 3:** the unassigned list, 3.1 (LP as the only development clip), 3.3 ("after a candidate parameter set is fixed on LP"), 3.4 (MLS) and 3.5 (2A/4A blocky);
  - **section 8.4:** the even/odd K0 split;
  - **section 13.3:** where QP-ablation evidence comes from;
  - **section 19:** the S2-I3, S2-I4 and S2-I5 definitions, plus the S2-I8 all-16 census, still pending.
- Section 9.1 (Q_fixed per clip, "apply the same median rule to other clips") already covers the new sources.
- **No decision-file changes are needed:**
  - D-26 states that development/hold-out assignment and fixed-QP selection are "Stage 2 design details, not repository decisions";
  - D-13 is unaffected while B0 is used;
  - D-24 is unaffected.

### SHOULD

**S1. Redesign the QP ablation (S2-I4) symmetrically.**

- The draft compares a K0 tuned at fixed QP against the same K0 run at real QP. As the draft itself concedes, that favours fixed QP.
- **Instead:** tune both QP modes with the same procedure and budget, inside the same cross-validation folds (section 4). Compare their held-out-group results, paired by group.
- **Where the evidence comes from:**
  - only the **originals** carry QP information: XP median 14, SP 16, LP 18 and 3A 14, each with a real spread;
  - every `_blocky` has QP 62 everywhere, so the two modes are identical there (v0.6 section 13.3).
- This answers the S2-I4 question without reserving any frames, and replaces the even/odd split.

**S2. Even/odd becomes in-sample stability reporting only.**

- GOPs within one recording share scenes and lighting, so even/odd folds are strongly correlated and give optimistic "held-out" figures.
- Keep the even/odd breakdown as a within-source stability report: the owner's item (c), clearly labelled as in-sample.
- Make the D/E/F/G split-training tracks optional, or drop them. Grouped cross-validation answers their question better.

**S3. Predeclare source balancing.**

- The `_blocky` encodes are software transcodes at constant QP 62, with 73-85% NONE. Counted seam by seam, they would outvote the real recorder material.
- **Proposed rule:** equal weight per content group, and within each group the real original weighted at least equally with its `_blocky` (D-26: real recorder material is primary).
- Report every source separately as well.

**S4. Use the paired-reference metric inside development.**

- Each development `_blocky` has a higher-quality original, so the section 13.3 metric ("movement toward the decoded original") becomes available during development, not only on 2A/4A.
- **Frame correspondence must be proven first.** The two members of each pair have the same frame counts, but different picture types, and the originals have leading B frames.

**S5. Keep hold-out content out of S2-I3 entirely.**

- `LG_576i_4_EP_blocky`, `TEST_2A_A001_blocky` and `TEST_4A_A003_blocky` contain the same pictures as the locked EP, 2A and 4A originals.
- Using them now would contaminate those hold-outs: every `_blocky` is a different encode, but each shares its original's content.
- They belong with their originals at S2-I8.

**S6. MLS and MLS_blocky stay control material.**

- **Format:** both are 352x288. MLS is progressive; MLS_blocky is flagged interlaced but is 99.9% FRAME/NONE.
- **Recommended use:** run them as a separate no-harm / format-robustness check on the frozen candidates, not as a development group, unless the owner chooses otherwise.

### OPTIONAL

**O1. Uncertainty.** Four content groups give only four genuinely independent held-out estimates. Report them per group, with frame and GOP intervals inside each, and no p-values.

**O2. Visual review.** The owner reviews the final candidates on every development source, plus spot checks of each fold's held-out group, blinded where practicable. All such excerpts are Restricted Media.

**O3. Comparison arms (the owner's item d).** Run three arms through the same folds:

- the old single-source arm (LP only);
- LP plus LP_blocky;
- all groups.

Evaluate all three on the same held-out groups. This directly measures what single-source development costs, which is the owner's point, demonstrated with data.

## 4. Recommended structure: grouped cross-validation by content

**Development pool.** Eight recordings in four content groups:

- XP, XP_blocky;
- SP, SP_blocky;
- LP, LP_blocky;
- 3A, 3A_blocky.

**The sequence:**

1. **Characterise all eight.** Read-only, with all eligible frames.
2. **Run the candidate procedures with leave-one-group-out cross-validation.**
   - For each of the four groups in turn: develop (screen, shortlist, tune) on the other three groups, using all their eligible frames, then evaluate untouched on the left-out group.
   - The averaged held-out results measure how well each *procedure* generalises to content it has never seen.
3. **Choose the procedure** using the predeclared rubric applied to the cross-validation results, plus owner visual review.
4. **Fit the final K0 on all eight sources**, which is "develop on all", and freeze it.
5. **S2-I8:** the frozen K0 goes to the locked hold-outs (EP, 2A and 4A originals, and their `_blocky` copies) and to the MLS controls. This is the first contact with that content.

This gives the owner exactly the property he asked for: the final method is developed on all available real data, and every development source is also tested once as unseen data.

Fixed QP per clip remains the all-MB median (v0.6 section 9.1):

| Source | Fixed QP |
|---|---|
| LP | 18 |
| XP | 14 |
| SP | 16 |
| 3A | 14 |
| every `_blocky` | 62 |

Medians were computed over all frames, as in Stage 1. The design should state whether leading-B frames are included and must not re-derive the values afterwards.

## 5. Owner decisions needed before any S2-I3 implementation

1. Adopt the development pool: XP, SP, LP and 3A, each original plus `_blocky`. This is a role change from "unassigned/spare".
2. Exclude EP, 2A and 4A `_blocky` from S2-I3; they move to S2-I8 with their originals.
3. Set the MLS pair's role (S6).
4. Replace the even/odd split with leave-one-group-out cross-validation and a symmetric QP ablation (S1, S2).
5. Approve the per-source registration acceptance rule (M3) and the source-balancing rule (S3).
6. Revise Stage 2 to v0.7, covering roles, sequence, S2-I3 to S2-I5, and the S2-I8 census.
7. Have the owner generate the scratch indexes on Windows (the S2-I2 procedure, run per source) as the authoritative step. Claude's Linux hashes above are the cross-check.

Then ChatGPT drafts Stage 2 v0.7 and S2-I3 design v0.2 for Claude's review. **No S2-I3 code** until both are ratified. S2-I3 remains NOT AUTHORISED for implementation.

## 6. Answers to the draft's questions (brief)

- **M1 (authority):** see M4. Use a new versioned Stage 2 file.
- **M2 (independence):**
  - Viewing LP and LP_blocky before the external sources is weak separation, because the external sources stay single-use.
  - D/E folds are temporally dependent and optimistic.
  - Cross-validation by content group replaces both.
- **M3 (preflight):** answered in section 2.
  - 3A_blocky is 704x576.
  - MLS_blocky is 352x288.
  - XP_blocky is a clean PASS.
  - SP_blocky is BLOCKED by a test whose premise fails for it.
- **M4 (QP):** the per-clip all-MB medians are confirmed above. No Stage 2 change is needed beyond naming the population.
- **M5 (options):** the disposition rules are sound: B0 is the default, B1 needs explicit authorisation, and M4a is correctly a proposal.
- **M6 (QA):** see S2, S3, S5 and O1.
- **M7 (stage boundaries):** preserved. S2-I8 stays the locked generalisation stage, now also receiving the hold-out-content `_blocky` copies and the planned all-16 census.
