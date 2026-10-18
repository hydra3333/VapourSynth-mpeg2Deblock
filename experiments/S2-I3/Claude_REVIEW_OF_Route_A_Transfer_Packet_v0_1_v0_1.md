# Claude review of the Route A transfer packet v0.1

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude, independent review role
Date: 2026-10-18
Packet reviewed: `Route_A_S2_I3_P0_CLAUDE_REVIEW_PACKET_v0_1.zip`, five files
Repository baseline verified: `8ffaa7d6d2500f842d5f841402a7b025ea4eda90` (fresh GitHub clone, 2026-10-18)

## 1. Verdict

**(A) `S2_I3_P0_Evidence_and_Gate_Report_v0_1_DRAFT.md`: CLEARED SUBJECT TO ONE MUST.**
One factual error in section 5.1, three SHOULDs, one OPTIONAL. Everything else Claude could check
independently is correct, including every gate figure, every index hash, both control tables and all
transferred annex measurements.

**(B) `06_DEBLOCK_CONCEPT` v1.3 candidate: NO OBJECTION on substance.** The K-03/K-07/K-08
evidence-level qualifiers are correctly narrow, the figures are right, and the three things most at risk
of overstatement are each explicitly bounded. One MUST applies to both documents jointly: the
install-time wording.

**(C) Transfer completeness: SUBSTANTIVELY COMPLETE for every knowledge class, with two gaps worth one
sentence each.** Claude agrees the bridge is **not** yet retirable, for the reason the packet itself
gives: the operational annex still needs deliberate landing in the role handovers.

**No contradiction with accepted repository authority was found.** No MUST arises against the evidence,
the recomputations, the ratified gate, or any ratified design document.

## 2. The explicit confirmations the packet asked for

Each of these was requested in `Route_A_Transfer_Matrix_and_Claude_Review_Request_v0_1.md` and each was
checked independently rather than taken on trust.

| Requested confirmation | Result |
|---|---|
| Baseline v1.2 in the packet matches actual HEAD `8ffaa7d6` byte-wise after LF normalisation | **CONFIRMED.** Both 531 lines, LF-normalised SHA-256 prefix `869abc833456c762`. No rebase needed |
| HEAD is `8ffaa7d6` and the cleanup/index commits exist as stated | **CONFIRMED.** `7f8e445` Commit A, `b83ab3e` Commit B, `35923a5` seven indexes, `8ffaa7d6` Commit C. 214 tracked files, **zero** `.zip` anywhere |
| Gate numbers and eight full index hashes against v0.5 and status v0.4 | **CONFIRMED.** All eight hashes, frame counts, geometries, exact P-skip counts and qualifying P-picture counts match. Section 5.1's sixteen control percentages match Claude's own computation to four decimal places |
| 137-file acceptance chain remains the controlling proof | **CONFIRMED.** The evidence archive Claude received has SHA-256 `898763a3e43d1a80f4c31713b4ccb9a498cd86c27c846eb15ddfabf498146af4`, exactly as the report states, and 158 entries = 21 directory + **137 file** entries. The report's wording on this is precise and correct |
| `known_bad_offsets.csv` `caught` statement against `stage2_registration_stats_v0_1.py` | **CONFIRMED AGAINST SOURCE.** At `8ffaa7d6` line 500-501 the code is `'caught': r['cx'] == r['ry'] == 0 or any(r[k] != 'PASS' for k in ('shift','column','row'))`. The report's rendering is exactly equivalent. `OFFSETS` at line 27 is `[(0,0),(4,0),(8,0),(16,0),(0,1),(0,2),(0,8),(0,16)]` - eight rows, the first the aligned reference and the other **seven** the known-bad offsets. The report's wording, including "True by definition" for the zero-offset row, is correct |
| K-03/K-07/K-08 qualifiers do not misrepresent exploratory work or P0 scope | **CONFIRMED.** See section 4 |
| M1/M2/M3/M4 corrections survive | **CONFIRMED.** See section 5 |
| 90.2% and 93.08% remain separate | **CONFIRMED** in both documents, and correctly argued |
| v0.5 SHOULD S1-S4, scope correction, appearance-vs-population, `q_scale_type`, `auc_proxy`, post-preflight floors | **CONFIRMED.** See section 6 |
| Annexes preserve the bridge's section 9 inventory; identify any missing class | See section 7. Two gaps, both minor |
| No Stage2 v0.7 / S2-I3 v0.3 / `05` / `02` change, no hold-out use, no P1 authorisation, no new K item or filter policy | **CONFIRMED.** Nothing in either candidate touches those, and both state the restriction explicitly |
| D-23 handling and install shapes | **CONFIRMED CORRECT**, and the packet is appropriately outside the tree. One MUST on wording - section 3 |
| Identity text | **CLEAN.** All five packet files scanned, zero occurrences |

## 3. (A) Findings against the Evidence and Gate Report

### MUST M1 - section 5.1, the mismatch count is wrong

Section 5.1, the paragraph beginning "On Windows, 3A's built-in **horizontal (-1,0) per-block offset
control**", states that control "reproduced **93.08%** of its 8,812 qualifying blocks (289 blocks
differed)".

**289 is the wrong figure for that control. The correct value is 610.** From the evidence:

| 3A hypothesis | compared | identical | differed | rate |
|---|---:|---:|---:|---:|
| true position | 8812 | 8812 | **0** | 100% |
| spatial control `-1,0` | 8812 | 8202 | **610** | 93.0776% |
| temporal control `previous_display` | 8812 | 8523 | **289** | 96.7204% |

289 is `previous_display`'s mismatch count, not `-1,0`'s. The arithmetic is also self-checking: 6.92% of
8,812 is about 610, and cannot be 289.

**This error originated in Claude's own wording and Claude owns it.** Review v0.5 section 3 says "the
true position has **0** non-matching blocks out of 8812, while the best competing hypothesis has
**289**". Read strictly that is correct, because the best competing hypothesis by match rate *is*
`previous_display` at 96.72%. But it sits immediately after a paragraph dominated by the 93.08% figure,
and the natural reading welds the two together - which is exactly what happened. The ambiguity was
Claude's; the report resolved it the only way the surrounding text suggested.

**Proposed correction** for section 5.1, naming both controls so the ambiguity cannot recur:

> On Windows, 3A's built-in **horizontal (-1,0) per-block offset control** reproduced **93.08%** of its
> 8,812 qualifying blocks, with **610** blocks differing, whereas the true aligned hypothesis reproduced
> all 8,812 with **zero** mismatches. The strongest control of any kind on 3A was the wrong
> `previous_display` temporal hypothesis at **96.72%**, differing in only **289** of 8,812 blocks.

Claude will correct the same ambiguity in its own handover, and notes for the record that review v0.5
is already committed and carries it; under the owner's 2026-10-18 decision not to re-version committed
documents for single sentences, the correction belongs in this report and in the next handover revision
rather than in a v0.6 of the review.

### MUST M2 (joint with the concept candidate) - install-time wording

Both candidates assert their own unratified, uninstalled status in flat terms. Every such sentence
becomes **false at the commit that installs it**. This is the project's most frequently recurring defect
class; by Claude's count this is its eighth occurrence, and the installing commit is exactly where it
bites. The lines are:

**Evidence Report** - 3 lines:

```
  4: **Version:** 0.1 - DRAFT FOR CLAUDE INDEPENDENT REVIEW; NOT INSTALLED OR RATIFIED AS A DOCUMENT
536: **Evidence Report** (this file): draft only, proposed current-tree addition after Claude review and owner ratification, **1 A / 0 M / 0 D** if installed alone
555: ### v0.1 - 2026-10-18 (DRAFT, NOT RATIFIED AS REPORT)
```

**`06` v1.3 candidate** - 5 lines:

```
  4: **Version:** 1.3 (DRAFT - FOR CLAUDE INDEPENDENT REVIEW; NOT RATIFIED)
  7: **Status:** v1.3 is a REVIEW DRAFT ONLY; the project owner has NOT ratified this revision. Version 1.2 ... remains the current Stage 0 concept authority until separately approved.
134: ### 3.1 S2-I3 empirical cross-checks on K-03, K-07 and K-08 (v1.3 DRAFT; evidence only)
504: ### v1.3 - 2026-10-18 (DRAFT FOR CLAUDE REVIEW; NOT RATIFIED)
514: - This proposed revision requires Claude's independent review and the owner's ratification; v1.2 remains authoritative until then.
```

**Proposed treatment.** Keep the review-candidate files exactly as they are - they are true now, and
truthful self-labelling in a review candidate is correct. Produce **separate install copies** whose
sentences are true at their installing commit: version lines without "DRAFT/NOT RATIFIED", status lines
reading RATIFIED with the owner's date, section 3.1's heading without "(v1.3 DRAFT; ...)", and change-log
entries reading as installed revisions. Line 536 should state the shape as a fact of the installing
commit rather than a conditional. Claude will diff-check the install copies against the cleared
candidates before installation, as for every previous install package.

Note what is **not** in this finding: lines 8, 32 and 551 of the report are durable statements that stay
true after installation - that ChatGPT did not execute P0 or read the 137 files, that v0.5 supersedes
v0.1-v0.4, and the record of the owner's ratification. Leave them.

### SHOULD S1 - flag the bridge's stale operational snapshot

Section 12 "Bridge retention" correctly keeps the bridge. But the bridge's own **section 10** contains a
now-false operational line: *"S2-I3 P0A and P0B completed on Windows; P0C XP alone REGISTERED at last
observed state; remaining admissions, diagnostics, pairs, summary and independent review are
outstanding."* That was true on 2026-10-17 and is overtaken.

The harm is small, because bridge section 10 itself points operational state at the status document
rather than owning it. But the bridge stays in the tree until retirement, and a successor could read
that line as current. **Add one sentence to section 12**: that the bridge's section 10 operational
snapshot is historical and superseded by this report and by status v0.4, and that only the bridge's
empirical and methodological sections remain live pending transfer.

### SHOULD S2 - carry the "do not quote v0.2's figures" instruction

Bridge **section 2** holds a durable instruction that the annexes do not restate: that
`Claude_ANALYSIS_OF_Paired_Reference_Metric_and_Sample_Pool_Extension_v0_2.md`'s boundary and interior
figures **must not be quoted**, because its seam placement was the M3 error.

Two things reduce the severity, and Claude checked both. First, section 13 item 5 already carries the
companion point, that no v0.3 of that analysis exists and none should be sought. Second, **that analysis
document is not committed** - Claude confirmed it is absent from the tree at `8ffaa7d6` - so a successor
working from the repository cannot quote it. Third, section 9 does preserve v0.2's figures *with
invalidity labels*, and handles them well: it correctly notes that the 'H' axis across the x=8 vertical
seam is unaffected by the vertical-pitch error because x=8 is transform-type independent. That is a
genuine nuance, correctly stated.

**Proposed correction:** extend section 13 item 5 to read that neither a v0.3 should be sought **nor
v0.2's boundary and interior figures quoted**, the corrected values being those in section 9.

### SHOULD S3 - make the coverage claim self-evidencing

Section 2 lists bridge coverage as "sections 3-8, 12 and 14-17 ... sections 11 and 13". The bridge has
**eighteen** sections. A reader cannot tell from the report whether 1, 2, 9, 10 and 18 were considered
and deliberately not reproduced, or simply missed. They were considered - Claude read all five - and four
of them are meta material that retires with the bridge: section 1 is the Route A rationale, section 9 is
the transfer checklist itself, section 10 is the no-change guardrail, section 18 is the consolidation
record. Only section 2 carries durable content, per S2.

**Proposed correction:** one sentence in section 2 naming sections 1, 9, 10 and 18 as deliberately not
reproduced because they are process material that expires with the bridge, and section 2 as carried into
section 13 item 5. The completeness audit at retirement time then needs no reconstruction.

### OPTIONAL O1 - label consistency

Section 4 and the section 9 annexes write "TEST 3A" while sections 5.1 and 6 write "3A". Harmless but
worth one pass for a document that will be cited by source label.

### NO OBJECTION, verified correct

The gate boundary statement in section 1 and its repeated insistence that a PASSED P0 is neither filter
feasibility nor P1 authorisation. The six-class evidence table in section 2, which is the structural
device that keeps exploratory work from contaminating gate claims. The 200-block and 10-picture floors
with 190 and 9 named as below-floor, matching Claude's exact boundary verification. The 24 spatial and 3
temporal control structure, including the exclusion of a previous-display control that equals the actual
anchor. FAIL taking precedence over INCONCLUSIVE, and any control reaching 100% being INCONCLUSIVE. Both
blind spots, field swap and IPPP, stated without overclaiming. The pair rule with its triangle-inequality
justification and the explicit post-preflight disclosure of the two floors. The 908-versus-664 wording,
which incorporates ChatGPT's own correction of Claude's v0.4 and is now right. The closed media hash
chain and all-distinct media hashes. The runtime paragraph, including the refusal to claim identical
environments and the correct note that Linux research ran CPython 3.13 / NumPy 2.5.3. The S2-I2 legacy
dispositions: five PASS and exactly SP, SP_blocky and 3A BLOCKED on preconditions.

**One item Claude independently confirmed because the report raised it.** Section 6 observes that a fully
static all-ties case is presently classified FAIL where INCONCLUSIVE would be more semantically accurate.
**That is correct.** Tracing the predeclared rule on a frame where every MAE is zero: `min_other >= 2 *
mae_0` becomes `0 >= 0`, so the frame is counted decisive; the violation test `mae_0 < min_other` becomes
`0 < 0`, which is false, so the decisive frame is also a violation; and any decisive violation is a hard
FAIL. Claude also searched all 908 frame records across the four pairs: **zero** have `mae_at_0 == 0`, so
the edge case does not arise in this evidence. The report's statement that no present source engages it
is correct. Worth carrying into S2-I4 design if the pair rule is reused on static material.

## 4. (B) Findings against the `06` v1.3 concept candidate

**NO OBJECTION on substance. No MUST beyond M2's shared wording finding.**

The three evidence-level qualifiers are the heart of this delta and all three are correctly bounded:

- **K-03** adds "additional exploratory decoded-luma corroboration on development original/blocky pairs
  (not a P0 filter gate)". It does not redefine the seam and does not claim tested filter performance.
  The normative geometry stays RESEARCHED from H.262 with the implementation separately VERIFIED.
- **K-07** adds "owner-run P0 empirically verifies the qualifying skipped-P subset only (not all NONE
  cases)". Section 3.1 reinforces it: the test keys on `coding=SKIPPED` and picture type P, **not** on
  `transform=NONE` as a substitute. That distinction is the one most likely to be lost later, and stating
  it twice is right.
- **K-08** keeps HYPOTHESIS for off-grid propagation while recording P0's verified on-grid co-location
  for the zero-motion skipped-P subset, "without verifying off-grid prevalence". It correctly leaves
  O-04 and O-09 open.

Every figure in section 3.1 checks out against Claude's records: FRAME row-band excess 12.8%-19.5% (XP
+19.5, SP +16.2, LP +17.3, 3A +12.8), the FIELD control at 2.3%-3.3% (+3.2/+3.3/+2.7/+2.3), and the x=8
vertical within-state span 16.5%-25.5%. The attribution "using the **blocky** index's own transform
states" is correct - the bridge's section 5 says the per-pixel differences were "assigned by the **blocky
encode's own** per-macroblock transform state". The supersession of the geometry-blind 7%-10%
interpretation is stated plainly. O-04 and O-09 were read at lines 462 and 467 of the candidate and say
what the delta claims they say.

Two sentences deserve singling out as the most valuable things in the delta, because they close
misreadings that already happened once:

> In this context "inherited" means propagated from earlier pictures **of the same encoded stream**, not
> from the higher-quality original recording.

> Co-located zero-motion P-skips demonstrate that carried-forward damage can remain **on the current
> grid**; propagation does not automatically imply off-grid displacement.

Those are precisely the two errors Claude made and the owner caught on 2026-10-18. Having them in the
concept authority, rather than only in a review document, is the right permanent home.

The closing guard is also correct: the cross-checks alter neither D-09 same-field-polarity safety, chroma
scope, Stage 2's evidence hierarchy, nor the open filtering decisions, and the P0 report establishes
admission and correspondence, **not** filter benefit.

## 5. M1-M4 survival check

| Correction | Status in the packet |
|---|---|
| **M1** side-by-side macroblocks share a VERTICAL boundary, stacked share a HORIZONTAL one | **SURVIVES.** Annex line 169 states explicitly that "the originally relayed 15.7 / 8.5 / 24.0 / 10.0 values are **HORIZONTAL** boundaries, not vertical", and the transition table carries both axes separately: XP 15.5/11.3 vertical and 15.7/11.4 horizontal, LP 23.6/15.0 and 24.0/15.3 - matching Claude's values exactly |
| **M2** coded-pair versus all-pairs denominators must be stated | **SURVIVES.** Both denominators appear in the table with the raw counts (XP 40777/263190), so the ratio is reconstructable rather than asserted |
| **M3** the geometry-blind row-8 mask was wrong for most FIELD macroblocks; the "paired MAE is intrinsically weak" conclusion is withdrawn | **SURVIVES, well handled.** Labelled "**SUPERSEDED CONCLUSION**" with the surviving narrower claim stated, the dilution mechanism explained, and the FIELD proportion (53%-73%) given as the reason |
| **M4** prior K items already contained much of the mechanism, so measurements upgrade evidence rather than invent K items | **SURVIVES.** No new K item is proposed anywhere, and the delta is confined to evidence-level annotation |
| Transform regime mix | **EXACT.** XP 70.9/12.1/17.0, SP 73.4/5.9/20.8, LP 52.7/23.0/24.3, 3A 7.6/67.9/24.5, with the both-states-present column 99.1/99.5/97.1/92.3 |
| NONE composition and the P-skip subset scope | **EXACT**, including the four-column decomposition and the correctly scoped "1.9% to 9.4% of NONE is the guaranteed zero-motion co-located portion" |

## 6. v0.5 SHOULD S1-S4 disposition

| SHOULD | Disposition | Claude's assessment |
|---|---|---|
| **S1** carry both control figures with mechanisms named | Section 5.1 | **Satisfied in structure**, but carries MUST M1's wrong mismatch count. Satisfied once M1 is applied |
| **S2** define the `caught` column and the `(0,0)` aligned reference | Sections 6 and 10 | **Satisfied and verified against source.** The report correctly declines to redefine CSV logic and asks for reviewer verification; Claude has now done that and confirms the rendering is exact |
| **S3** appearance instrument versus population sample | Section 10 | **Satisfied.** The 26.3/32.4/26.3/40.1 against 83.1/79.3/75.2/76.0 census is reproduced correctly, the withdrawn claims are recorded, and it correctly notes the owner did not approve a change to the 2:1 weighting |
| **S4** confirm `q_scale_type` recoverability before S2-I4 | Section 10 | **Satisfied, and improved on Claude's wording.** All quantiser figures correct: 4.23% above 62, the 49,113-at-112 spike against 1,518 at 104, XP and SP at 72 for 0.11% and 0.20%, 3A reaching 56. The report adds "do not presume it absent solely from a partial byte-layout inspection", which is a fair correction to Claude's own framing - Claude inferred likely absence from the 8-byte record layout without reading the writer. **Claude accepts that qualifier**; the question stays open pending a source read, under D-13 |
| `auc_proxy` NaN | Section 10, OPTIONAL | **Correctly scoped** as a descriptive follow-up with no gate impact |
| post-preflight floors | Sections 5 and 6 | **Disclosed in both**, in the required terms |

## 7. (C) Transfer completeness

**Every knowledge class in the bridge's section 9 inventory has a destination in the draft, and the
measurements transferred faithfully.** Claude's view on retirement matches the packet's: **not yet**.

The transfer matrix's own "still required" column is honest, and the two rows that say more than
"ratify and install" are the right two:

- **Bridge section 15, operational lessons** - isolated Python, filename imports, Git line endings, CMD
  traps, review-artefact hygiene. Annex J and section 12 place these correctly, but their real
  destination is the **role handovers**, and a report annex is not a substitute. Claude's handover v0.12
  already carries the isolated-Python incident, the staging lessons and the `.gitignore` remedy; the
  ChatGPT handover needs the equivalent pass. **Until both handovers carry them, the bridge is
  load-bearing.** The packet says exactly this.
- **Bridge section 16, correction history** - same treatment, same conclusion. v0.12 carries all of it
  plus the five 2026-10-18 corrections; the ChatGPT side needs its own pass.

Gaps found: **two**, both one sentence, both in section 3's SHOULD S2 and S3 above. Nothing else is
missing, and no knowledge class is unaccounted for.

**Retirement test Claude proposes**, so the decision is mechanical when it comes: the bridge may be
retired when (a) this report is installed and ratified, (b) the `06` v1.3 revision is installed and
ratified, (c) both role handovers have been revised to carry bridge sections 15 and 16 deliberately, and
(d) the transfer matrix is updated with the actual install commit IDs. Not before all four.

## 8. Installation shapes

Claude agrees with the packet's proposed control, with the M2 wording pass applied first.

| Step | Action | Expected staged shape |
|---|---|---|
| 1 | Install the Evidence Report at `docs/REPOSITORY/S2_I3_P0_Evidence_and_Gate_Report_v0_1.md`, from an install copy with M1 and M2 applied | **`1 A / 0 M / 0 D`** |
| 2 | Separately install `06_DEBLOCK_CONCEPT.md` v1.3 in place, from an install copy with M2 applied | **`0 A / 1 M / 0 D`** |
| 3 | Update the transfer matrix with both commit IDs | separate, when they exist |

Keep steps 1 and 2 as distinct commits: one adds a report, the other modifies a ratified authority, and
they want separate audit boundaries. **Nothing else from this packet enters the repository** - not the
baseline copy, not the review-only patch, not the candidate files, not the ZIP. The seven indexes are
already installed at `35923a5` and must not be staged again; Claude verified all seven against the
admitted bytes and all six frozen Stage 1 indexes as byte-unchanged.

Run `git diff --cached --name-status --no-renames` before each commit and confirm the shape exactly.
Three commits on 2026-10-18 swept unintended files, and that check is what stopped the fourth.

## 9. Unchanged

P0 is ratified PASSED; **P1 remains unauthorised and needs a separate explicit owner decision**. No
filtering has been run or evaluated. EP, TEST 2A and TEST 4A with every `_blocky` copy stay locked until
S2-I8 under any filename or alias. TEST 6A and 7A remain outside the allow-list with no assigned role.
The six frozen Stage 1 indexes are never rewritten and `VHSC_samples/LG_576i_3_LP.idx` stays
byte-unchanged. Git history has not been scrubbed and that remains a Development Closure obligation.
Review correspondence, candidate patches and evidence archives do not enter the repository.
