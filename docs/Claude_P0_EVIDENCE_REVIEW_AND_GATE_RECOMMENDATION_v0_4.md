# Claude comprehensive S2-I3 P0 evidence review and gate recommendation v0.4

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude, independent review role
Date: 2026-10-18
Revision: v0.3 supersedes v0.2 and v0.1 on installation (D-23 v1.2, 1 A / 1 D against the tree, since
neither predecessor was ever committed). Both predecessors were issued to the owner only. v0.1 carried
a reasoning error about the `_blocky` re-encodes which the owner challenged; v0.2 corrected it but
over-generalised, dismissing the blocky/original PAIR as an instrument along with the artefact
statistics; the owner challenged that too, and v0.3 rewrote section 5 accordingly. **v0.4 corrects two
further errors found when the owner asked whether this review affected three ratified
`docs/REPOSITORY/` documents: v0.3 section 5.3 wrongly attributed a scope conflation to the committed
`interim_` document, which is in fact correct and precise; and v0.3's SHOULD S1 wrongly described the
93.08% control figure as superseding the interim's 90.2% figure, when the two measure different
things.** See sections 3.1 and 5.3. **The gate verdict is unchanged throughout: every error has been
confined to interpretation and commentary and none has touched the gate.**
Evidence reviewed: `S2_I3_P0_RESULTS_FOR_CLAUDE.zip` - the complete P0 `results\` tree, 137 files
Reference folders reviewed: `handover_respository.zip` - `docs/HANDOVER/` (8 files) and `docs/REPOSITORY/` (9 files)
Repository HEAD at last verification: `4636c33ebd7fd053149bebac8bc2dbe2d754d090`

## 1. Verdict

**P0 EVIDENCE ACCEPTED. Claude recommends the P0 registration gate be recorded as PASSED.**

Every gate-bearing field in the evidence tree is a pass value, and every quantity Claude can check
independently agrees with the references it published **before** the Windows runs existed. Claude did
not merely read the reported verdicts: it **recomputed** the two decisive results from the raw
per-item data the evidence carries, and both reproduce exactly.

No MUST against the evidence. Three SHOULDs, all additive records for the eventual Evidence and Gate
Report rather than defects. Two OPTIONALs. One MUST against **Claude's own v0.1 of this document**,
owned and corrected in section 5.

What this verdict does **not** cover, unchanged from the predeclared scope: `READY_FOR_P1=true` is a
numerical disposition only. It is not authorisation for P1, for filtering, for touching protected
hold-out media, or for expanding the source pool. Those remain separate owner decisions.

## 2. What was checked, and how

The evidence tree is complete and uniform: 8 sources x 16 files, 4 pair directories x 2 files, and one
global summary = 137 files, with no gaps and no truncation.

| # | Check | Method | Result |
|---|---|---|---|
| 1 | 8 admissions REGISTERED | read `pskip_identity.json` status and reason | **8/8** |
| 2 | Exact P-skip identity | `true_position.identical == compared ==` Claude reference | **8/8 exact** |
| 3 | Identity **recomputed** | summed `p_skips` and `exact` over `per_P_picture`, compared to totals | **8/8 reproduce** |
| 4 | Anchor causality | every `per_P_picture` entry has `anchor < picture` in display order | **8/8 hold** |
| 5 | Per-picture consistency | every entry has `exact == p_skips` | **8/8 hold** |
| 6 | Qualifying P-picture counts | vs Claude's unpublished rehearsal values | **8/8 match** |
| 7 | Index SHA-256 | vs the eight-value allow-list | **8/8 match** |
| 8 | Frame count and geometry | `record_count`, `index_validation.json`, and the `vspipe --info` block in each log | **8/8 match** |
| 9 | Negative controls present | 24 spatial + 3 temporal per source | **8/8 complete** |
| 10 | No control reaches identity | strongest competitor per source | **none at 100%** |
| 11 | 4 pair tests PASS | `pair_correspondence.json` status | **4/4** |
| 12 | Decisive counts | vs Claude's rehearsal 140/175/81/268 | **4/4 match** |
| 13 | Decisive rule **recomputed** | re-evaluated `min_original_neighbour_mae >= 2 * mae_at_0` over all 908 frame records | **4/4 reproduce** |
| 14 | Per-frame flag consistency | recomputed `decisive` and `violation` vs stored flags | **0 inconsistencies** |
| 15 | Zero decisive violations | reported and recomputed | **0 and 0** |
| 16 | Strict k=0 argmin | `strict_zero_argmin` plus the five clip means | **4/4 strict** |
| 17 | Both sample-size floors | >=20 decisive AND >=10% decisive | **4/4 met with margin** |
| 18 | Frame-count correspondence | original vs blocky frame counts per pair | **4/4 equal** |
| 19 | Runtime provenance | all 7 runtime fields across all 8 admissions | **identical x8** |
| 20 | BestSource DLL continuity | vs accepted S2-I2 `run_manifest.json` | **identical** |
| 21 | Media hash chain | admission `source_sha256` vs pair `original_sha256`/`blocky_sha256` | **8/8 tie** |
| 22 | No duplicate samples | distinctness of all 8 media hashes | **8/8 distinct** |
| 23 | Hold-out protection | regex sweep of all 137 files for protected and non-allow-list media | **zero hits** |
| 24 | Summary cross-check | `P0_summary.json` vs the 12 underlying evidence files | **consistent** |
| 25 | Adversarial sweep | every FAIL/ERROR/WARN/INCONCLUSIVE/BLOCKED/NaN occurrence located | **all descriptive only** |

### 2.1 The two recomputations, because they are the substance of this review

**Admission.** `pskip_identity.json` carries `per_P_picture`, a list with one entry per qualifying P
picture giving `picture`, `anchor`, `p_skips` and `exact`. Claude summed those lists. For every source
the sum of `p_skips` equals the sum of `exact` equals the reference skip count, and the list length
equals the reference P-picture count. So the headline identity claim is not taken on trust from a
summary field; it is reconstructed from the per-picture breakdown and agrees.

**Pair correspondence.** `pair_correspondence.json` carries `frame_evidence`, one record per common
interior frame with `mae_at_0`, `min_original_neighbour_mae`, `decisive` and `violation`. Claude
re-evaluated the predeclared rule over all 908 records across the four groups and obtained 140, 175,
81 and 268 decisive frames with zero violations - identical to the reported values, with no frame
whose stored flags disagree with the recomputation.

### 2.2 Admission results

| Label | Status | Exact identity | Qualifying P pictures | Frames | Geometry | Index SHA-256 |
|---|---|---|---:|---:|---|---|
| XP | REGISTERED | 1619/1619 | 54 | 228 | 720x576 | `4f3821b5...f127` |
| XP_blocky | REGISTERED | 25635/25635 | 55 | 228 | 720x576 | `8d0326b5...6b20` |
| SP | REGISTERED | 1764/1764 | 46 | 192 | 720x576 | `40a97ce1...cc5d9` |
| SP_blocky | REGISTERED | 19010/19010 | 46 | 192 | 720x576 | `7e19ca60...e746` |
| LP | REGISTERED | 1533/1533 | 46 | 204 | 720x576 | `849b6a9c...0011` |
| LP_blocky | REGISTERED | 20300/20300 | 50 | 204 | 720x576 | `b3f1d714...5238` |
| 3A | REGISTERED | 8812/8812 | 133 | 300 | 704x576 | `9a60a8d2...7f33` |
| 3A_blocky | REGISTERED | 18190/18190 | 73 | 300 | 704x576 | `e6f556dd...83c8` |

Every source additionally reports `P_pictures_without_anchor_excluded = 0`, an empty `first_mismatches`
list, `expected_skip_count_info == actual_index_skip_count_info`, `control_count = 24` and three
temporal controls. `index_validation.json` reports `status = PASS` with
`picture_types_validated_all_frames = true` for all eight.

### 2.3 Pair correspondence results

| Group | Status | Decisive | Violations | Mean MAE k=0 | Best competing mean | Ratio | Decisive fraction |
|---|---|---:|---:|---:|---:|---:|---:|
| XP | PASS | 140/224 | 0 | 3.5250 | 9.8761 | 2.80x | 61.4% |
| SP | PASS | 175/188 | 0 | 3.2322 | 13.9828 | 4.33x | 91.1% |
| LP | PASS | 81/200 | 0 | 4.3876 | 9.9337 | 2.26x | 39.7% |
| 3A | PASS | 268/296 | 0 | 5.5276 | 19.9471 | 3.61x | 89.3% |

The common-interior frame counts (224, 188, 200, 296) are each four fewer than the clip length, which
is the correct consequence of a k = -2..+2 window needing two frames of margin at each end. Frame
numbering runs 2..N-3 as expected.

## 3. The strongest result in this evidence set: the threshold-free choice is vindicated

This is the single most important thing the owner's real Windows run has established, and it is
stronger than Claude's rehearsal indicated.

The test demands **exact** equality across every qualifying block. The question that always hung over
that choice was whether it was unnecessarily strict. The negative controls answer it:

| Label | Strongest spatial control | Rate | Strongest temporal control | Rate |
|---|---|---:|---|---:|
| XP | `-1,0` | 48.86% | previous_display | 83.88% |
| XP_blocky | `1,0` | 73.22% | older_anchor | 37.56% |
| SP | `1,0` | 45.24% | previous_display | 77.72% |
| SP_blocky | `0,1` | 73.35% | older_anchor | 33.75% |
| LP | `0,-1` | 40.29% | previous_display | **94.85%** |
| LP_blocky | `1,0` | 69.16% | older_anchor | 36.34% |
| 3A | `-1,0` | **93.08%** | previous_display | **96.72%** |
| 3A_blocky | `-1,0` | 78.61% | previous_display | 47.18% |

**A one-pixel horizontal shift of 3A still reproduces 93.08% of its skipped-macroblock blocks exactly.**
Any registration test using a tolerance threshold below roughly 93% would have **passed a
misregistered 3A**. The previous-display temporal control reaches 96.72% on 3A and 94.85% on LP.

So the margin that makes this test decisive is not a comfortable rate gap - it is the difference
between 100% and "not 100%". In absolute terms on 3A: the true position has **0** non-matching blocks
out of 8812, while the best competing hypothesis has **289**. That is decisive, but only because the
rule is exact. Claude's earlier rehearsal note recorded 90.2% for a 3A one-line shift; the owner's run
shows 93.08%, so the real data makes the case more forcefully than the rehearsal did.

### 3.1 How this relates to the figure already committed in the `interim_` document - corrected

v0.3 of this review said the 93.08% figure "supersedes the 90.2% rehearsal figure". **That was wrong
and is withdrawn. The two measure different things and neither supersedes the other.**

| | Committed `interim_` section 15 | This P0 evidence |
|---|---|---|
| Figure | **90.2%** | **93.08%** |
| Fault | TEST 3A shifted **1 line vertically** | offset `-1,0`, one pixel **horizontally** |
| Mechanism | whole-clip injected fault, re-running the admission | the test's own built-in per-block spatial control probe |
| Platform | Claude's Linux rehearsal | the owner's Windows run |

Today's *vertical* one-line controls for 3A are `0,-1` at 77.22% and `0,1` at 28.86%, nowhere near
90.2%, because an injected whole-clip shift and a per-block spatial probe are different operations with
different qualifying populations. So the two figures are **complementary evidence for the same
conclusion**, not competing versions of one measurement.

The `interim_` document already states that conclusion, and states it well: *"A threshold-based gate set
anywhere below 90% would have passed the 3A one-line shift. That is the argument for exact identity
over a tuned threshold."* Claude's contribution here is an additional data point at a different offset,
on the owner's own platform, which **raises the floor a tolerance-based test would have to clear from
90% to 93%** and extends the argument from one injected fault to the full 24-offset control set.

**SHOULD S1 (revised): in the Evidence and Gate Report, carry BOTH figures with their mechanisms
named**, and state the floor as at least 93%. Do not present either as a correction of the other, and
do not merge them into a single number.

## 4. Independent re-derivations that confirm ratified design parameters

These were not required by the gate. Claude did them because the diagnostic CSVs make them possible,
and a ratified parameter that reproduces from an independent data path is worth more than one that does
not.

**Q_fixed reproduces exactly for all eight sources.** Claude recomputed the quantisation median from
the `right_or_lower_qp` / `left_or_upper_qp` strata in `outer_mb_edge_diagnostics.csv`, weighted by the
`n` column:

| Label | Derived median QP | Ratified `Q_fixed` | Observed QP range |
|---|---:|---:|---|
| XP | 14 | 14 | 2..72, 25 distinct |
| SP | 16 | 16 | 1..72, 26 distinct |
| LP | 18 | 18 | 1..112, 31 distinct |
| 3A | 14 | 14 | 1..56, 24 distinct |
| XP_blocky, SP_blocky, LP_blocky, 3A_blocky | 62 | 62 | **62..62, 1 distinct** |

All four originals land exactly on their ratified value, and all four blockys are **single-valued at
62**. That independently confirms both the `Q_fixed` table and the constant-QP62 claim from the owner's
own Windows diagnostics. Caveat for the record: this is a boundary-pair-side weighting, not a strict
all-macroblock census, so exact agreement on all eight is a stronger result than the method guarantees
(**OPTIONAL O2**).

**Transform mix confirms the two opposite regimes.** Derived from the same strata, as
FIELD/FRAME/NONE percentages, against the committed interim figures:

| Group | Derived | Committed |
|---|---|---|
| XP | 71.0 / 12.1 / 16.9 | 70.9 / 12.1 / 17.0 |
| SP | 73.5 / 5.8 / 20.7 | 73.4 / 5.9 / 20.8 |
| LP | 51.9 / 23.3 / 24.8 | 52.7 / 23.0 / 24.3 |
| 3A | **7.7 / 68.3 / 24.0** | **7.6 / 67.9 / 24.5** |

Agreement is within 0.1 to 0.8 percentage points, the residual being the weighting difference noted
above. The qualitative finding stands confirmed on owner-run data: **3A sits in the opposite transform
regime to XP, SP and LP**, which is exactly why the owner's insistence on multiple content groups
mattered. A method developed on XP, SP and LP alone would have been developed almost entirely on
FIELD-coded material and would have met a 68%-FRAME clip for the first time in production.

## 5. The original/`_blocky` pair: what it is good for, and what it is not

Two Claude errors were corrected here by owner challenge, in sequence. Both are recorded because the
second is a more instructive failure than the first.

**Error 1, in v0.1 - a technical term used as a provenance claim.** v0.1 stated that "the severe
blocking in the Q62 re-encodes is predominantly inherited or off-grid rather than coded-seam content".
The owner's challenge: the originals are far less blocky than the deliberately bitrate-starved
re-encodes, so the seam blockiness must have been introduced by the transcode and cannot have been
inherited from the original. That reasoning is correct and **the claim is withdrawn.**

In K-08 "inherited" means *carried forward from an earlier picture of the same stream by motion
compensation*. It does not mean "inherited from the original recording". Claude's wording invited the
second reading, in which it is false. The actual mechanism: damage **originates** in the transcode's
coarsely quantised coded macroblocks, overwhelmingly the 100%-INTRA I pictures at `quantiser_scale`
62, and is then **propagated** by prediction into macroblocks carrying no coded transform of their
own. Every link in that chain is transcode-caused. Nothing in this evidence suggests blocking carried
over from the original recordings.

v0.1 also drew a backwards conclusion, that the blockys "exercise mainly the paths that geometry does
not mark". A propagated macroblock's blocking is not off-grid merely because that macroblock carries no
coded transform. For SKIPPED macroblocks in P pictures the motion vector is exactly zero and the block
is exactly co-located - the very property the P-skip admission test verified in section 2 - so that
blocking is **perfectly grid-aligned**. For INTER with CBP=0, and for skips in B pictures which can
inherit non-zero vectors, displacement is **unknown**, because Stage 1 indexes carry no motion-vector
components. The defensible word is "may be displaced", never "is".

**Error 2, in v0.2 - over-generalising from the artefact to the instrument.** Having established that
the blockys' internal quantiser statistics say nothing useful about production material, v0.2 went on
to dismiss "the whole blocky-vs-original comparison framing". The owner challenged that, and is right.
Those are two different things:

- the blockys' **internal statistics** - how coarse they are, which quantiser table they use, their
  coding-state mix - are properties of a synthetic artefact and do not describe production input;
- the original/`_blocky` **pair**, used as a controlled observation, provides something available from
  no other source in the pool and is genuinely valuable.

### 5.1 What the pair uniquely provides

**Known frame correspondence, now demonstrated rather than assumed.** The P0 pair test established it
on real Windows runs: strict clip-mean minimum at k=0, zero decisive violations across 908 decisive
frame records, equal frame counts. So a pixel difference between the two members is attributable to
the damage and not to misalignment. Before P0 this was a working assumption; it is now evidence, which
makes the pair **more** usable than it was before this gate, not less.

**A clean reference at every seam location.** For any candidate seam in the blocky member, the same
position in the original shows what was actually there - flat area, texture, or a genuine edge. That is
the only way to separate "this seam is damage" from "this seam is real detail", which is the central
difficulty of the entire filter design and the thing every false-alarm and detail-protection criterion
depends on. A real poor capture presents the damage with no clean twin and can never answer it.

**Real quantisation damage on real captured content at grid positions the index names.** Not a
synthetic blocking model constructed from theory. The alternative to the pair is either no information
about seam appearance, or inferred information unrelated to real material - which is worse than none,
because it has the shape of data.

**A basis for no-harm and OFF bit-exactness testing**, by running the filter against the clean member
and requiring no change where no damage exists.

This is consistent with D-26, which already frames the original member as the higher-quality decoded
reference rather than ground truth or an uncompressed source.

### 5.2 Where the pair's evidence stops: appearance instrument, not population sample

The useful distinction, and the one that prevents later misuse:

> The pair is a **controlled appearance and mechanism instrument** - what blocky seams look like, where
> they sit relative to the coded grid, and what the undamaged content was at that location. It is
> **not a population sample** of real-world blocking - how often damage occurs, how severe it is, and
> which macroblocks carry it in genuine captures.

The census below bounds the second use. It is a scope limit on the instrument, not a finding about the
world. Joint coding x transform state, n-weighted over the whole clip:

| Label | INTRA coded | INTER coded | INTER CBP=0 | SKIPPED | transform NONE | **coded transform present** |
|---|---:|---:|---:|---:|---:|---:|
| XP | 8.4 | 74.7 | 10.0 | 6.9 | 16.9 | **83.1** |
| XP_blocky | 14.3 | 11.9 | 46.8 | 27.0 | 73.7 | **26.3** |
| SP | 8.5 | 70.8 | 12.7 | 7.9 | 20.7 | **79.3** |
| SP_blocky | 17.6 | 14.8 | 42.8 | 24.8 | 67.6 | **32.4** |
| LP | 8.9 | 66.3 | 17.0 | 7.8 | 24.8 | **75.2** |
| LP_blocky | 12.4 | 14.0 | 50.2 | 23.4 | 73.7 | **26.3** |
| 3A | 24.1 | 51.9 | 19.2 | 4.9 | 24.0 | **76.0** |
| 3A_blocky | 14.5 | 25.6 | 40.9 | 19.0 | 59.9 | **40.1** |

In the blockys the index marks **26 to 40%** of macroblocks as carrying a coded transform, against
**75 to 83%** in the originals. Together with constant `quantiser_scale` 62, which is not real
rate-control behaviour, that means: **do not tune frequency thresholds, prevalence estimates or
severity distributions on blocky statistics.** Neither limit touches the appearance question the pair
exists to answer.

Also recorded: the transcode demonstrably creates fresh coded-seam blocking, which v0.1 failed to
weigh. Every blocky I picture is 100% INTRA at scale 62. Blocky P pictures carry a far higher INTRA
share than their originals - XP 0.1% to 19.4%, SP 0.1% to 32.3%, LP 2.0% to 12.5%, with 3A the
exception at 25.4% down to 21.1% - because prediction fails at that bitrate and the encoder falls back
to intra coding. All blocky INTRA sits at scale 62 against an original INTRA median of 14 to 18.

### 5.3 Withdrawn: the alleged scope conflation in the committed `interim_` document

**v0.3 of this review stated that the committed `interim_` document conflated scopes, contrasting its
"1.9 to 9.4% of NONE" against this census's "20 to 41% of NONE". That claim is wrong and is withdrawn.
The `interim_` document is correct, precise, and needs no change.**

Its table in section 7 is explicitly headed "Percentages are of NONE macroblocks only per source, not
of all macroblocks", and it decomposes NONE into four named columns: *Skipped in P*, *Skipped in B*,
*INTER CBP=0* and *Other*. The 1.9 to 9.4% range is the **Skipped in P** column alone, correctly
identified in the surrounding text as "the guaranteed zero-motion co-located portion". Total SKIPPED is
the sum of the first two columns, and it **agrees with this census**:

| Source | `interim_` Skipped in P + Skipped in B | This census, total SKIPPED of NONE |
|---|---:|---:|
| XP_blocky | 9.4 + 26.9 = 36.3% | 36.6% |
| SP_blocky | 9.0 + 27.2 = 36.2% | 36.7% |
| LP | 1.9 + 29.6 = 31.5% | 31.6% |
| LP_blocky | 8.4 + 23.2 = 31.6% | 31.8% |

Residuals are rounding and the boundary-pair weighting difference. **Claude compared its total-SKIPPED
figure against the interim's Skipped-in-P column alone and wrote the difference up as a defect in the
committed document.** The defect was in the reading, not the document. Recorded here because a review
that casts unwarranted doubt on a correct committed document is a worse failure than one that merely
gets a number wrong, and because this is the third correction in this area in one session.

**SHOULD S3 (revised): record in the Evidence and Gate Report the appearance-instrument versus
population-sample distinction from 5.2, and the census as its scope bound. Record also that the v0.1
provenance claim and the v0.3 criticism of the `interim_` document were both withdrawn.** The practical
effect on the 2:1 original:blocky weighting is a reason to keep the weighting favouring originals, not
a new reason to change it. **No change is required to the `interim_` document on account of this
review.**

## 5A. Forward note for S2-I4 scoping: indexed quantiser values

Not a P0 finding, and irrelevant to P1, which is fixed-QP. Recorded here only because it emerged while
checking the above and would otherwise have to be rediscovered when S2-I4 is scoped.

MPEG-2 maps a 5-bit `quantiser_scale_code` of 1..31 to `quantiser_scale` through one of two tables
selected by `q_scale_type`: linear, where `scale = 2 * code` and the maximum is 62, or non-linear,
where the maximum is 112. All four **originals** - real captures - use the non-linear table.

**Indexed QP saturates on starved real material.** LP, the long-play and most bitrate-starved real
recording in the pool, has **4.23%** of its macroblock-edge weight above scale 62, and it is not a
smooth tail but a clamp spike: **49,113 occurrences at exactly 112** against 1,518 at 104. XP and SP
reach 72 at 0.11% and 0.20%; 3A never exceeds 56. A spike at the table ceiling is rate-control
saturation, so above it `quantiser_scale` stops discriminating severity - content that "wanted" coarser
quantisation than the ceiling all reads 112. Any strength mapping monotone in indexed QP will treat all
clamped content identically, precisely where damage is worst. This is a property of real captures, not
of the transcodes.

**SHOULD S4 (new): before S2-I4, confirm whether `q_scale_type` is recoverable from the current
index.** `02_INDEX_FORMAT_SPEC` records `q` and `q_update` in the 8-byte record, but Claude has not
confirmed the table selector is stored. Real captures from different recorders and encoders may use
either table, and a 62 from the linear table is not the same step size as a 62 from the non-linear
table, so without the selector indexed values cannot be compared across sources. That is a D-13
extra-metadata question to settle before S2-I4 rather than during it.

## 6. Descriptive S2-I2 diagnostics: correctly scoped, and correctly reported as not a gate

All eight `S2_I3_diagnostic_disposition.json` files carry `not_a_P0_admission_gate: true`. The legacy
S2-I2 gate outcomes they report are:

| Label | Legacy S2-I2 gate, reported only |
|---|---|
| XP, XP_blocky, LP, LP_blocky, 3A_blocky | PASS |
| **SP, SP_blocky, 3A** | **BLOCKED** |

ChatGPT's status v0.3 and handover v0.9 both state that the BLOCKED outcomes affect SP, SP_blocky and
3A and arise from those tests' preconditions rather than from index misregistration. **The evidence
confirms exactly those three labels**, and the P-skip admission for all three is REGISTERED with exact
identity. The two results are not in conflict: one is a threshold-based detectability test with
preconditions, the other is a threshold-free registration test, and only the latter is the P0 gate.

The adversarial sweep found 406 `FAIL`, 315 `INCONCLUSIVE`, 12 `BLOCKED` and 1481 `NaN` occurrences
across the tree. **Every one is inside a descriptive S2-I2 artefact; none is in a gate-bearing field.**
In `known_bad_offsets.csv` a `FAIL` is the *desired* outcome, since the file exercises deliberately
wrong offsets, and all eight rows report `caught = True` for all eight sources - the legacy diagnostic
catches every known-bad offset it is given.

**SHOULD S2: define the `caught` column.** `known_bad_offsets.csv` has 8 rows: the 7 known-bad offsets
plus the aligned `(0,0)` reference. At that aligned row, 3A reports `row = INCONCLUSIVE` together with
`caught = True`, which a later reader could easily misread as "the correctly aligned case was flagged
as misregistered". It is not - but the column's semantics are nowhere stated. One sentence in the
Evidence and Gate Report defining `caught`, and noting that the `(0,0)` row is a reference rather than
a known-bad case, removes a real misreading risk from an evidence file that will outlive this
conversation.

**OPTIONAL O1:** `auc_proxy` is `NaN` throughout `boundary_detectability.csv` for every source. Harmless
for P0, which does not read it, but if that column is meant to carry a value it is not being computed.
Worth resolving before anything in S2-I4 relies on it.

## 7. Integrity properties worth recording

**The media hash chain is closed.** For each group, the `source_sha256` recorded at admission equals
the `original_sha256` / `blocky_sha256` recorded by the pair test. The pair tests therefore
demonstrably ran on the same bytes that were admitted, not on a re-fetch that merely shared a
filename. All eight media hashes are distinct.

That last point deserves a note. The duplicate-sample incident earlier in this project - where
renamed copies of existing recordings briefly entered the pool and nearly cost the EP hold-out - is
exactly the failure this check would catch. On this run it is clean.

**The runtime is internally consistent.** All seven runtime fields are byte-identical across all eight
admissions: VapourSynth R81, BestSource `PluginVersion(major=22, minor=0)`, plugin SHA-256
`fa5b9016...f69c`, adapter SHA-256 `154c9046...aa41`, Python 3.14.8 MSC v.1944 x64, NumPy 2.5.4. So the
eight admissions are one coherent experiment, not eight runs under drifting conditions. The BestSource
plugin SHA-256 equals the value in the accepted S2-I2 `run_manifest.json`, so the decoder is
bit-identically the one that produced the accepted S2-I2 evidence. NumPy differs from S2-I2 and from
Claude's rehearsal at 2.5.3 against 2.5.4 here; immaterial to exact `uint8` equality and
integer-promoted absolute differences, and correctly recorded rather than smoothed over.

**Hold-out protection held.** A regex sweep of all 137 files for `LG_576i_4_EP`, `TEST_2A`, `TEST_4A`,
`TEST_6A`, `TEST_7A`, `TEST_1A`, `TEST_8A`, `TEST_9A`, `TEST_10A` and `MLS` returned **zero hits**. The
only media stems referenced anywhere are the four allow-list originals and their `_blocky` partners.
The protected content was not read, decoded or named.

**The summary is correctly scoped.** `P0_summary.json` reports `READY_FOR_P1: true` alongside
`ready_is_numerical_only: true`, `requires_owner_and_claude_gate_review: true`, `problems: []`, and
marks all eight diagnostics `REPORTED_NOT_GATE`. The vocabulary discipline the project has maintained
throughout is intact in the machine-readable evidence, not just in the prose.

## 8. What the P-skip test still does not prove

Unchanged, and must travel with any statement of this result:

- **A field swap is undetectable.** A uniformly field-swapped clip would present identical co-located
  16x16 luma for skipped macroblocks and would register.
- **An IPPP stream would be INCONCLUSIVE**, because the previous-display control would always equal the
  anchor. Checked on this evidence: no source has `previous_display` at 100%, the maximum being 96.72%
  on 3A, so the control is informative for all eight and this limitation is not engaged here.
- **The two pair-rule sample-size floors, >=20 decisive frames and >=10% decisive, were chosen after
  seeing preflight data.** All four groups clear them with margin - the tightest being LP at 81 frames
  and 39.7% - but the disclosure must accompany the rule wherever it is published. The evidence files
  carry it themselves in `floor_note`, which is good practice.
- **Luma only.** No chroma registration is established by any of this.
- **Determinism is observed for these samples**, not proven for every MPEG-2 stream.

## 9. Repository state: what the attached folders need

Claude re-verified the two installed checkpoint documents: `ChatGPT_...v0_9.md` and
`S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_3.md` in `docs/HANDOVER/` are **byte-identical
(LF-normalised) to the corrected files Claude returned**. The corrections were installed as cleared.
No identity text appears in any of the 17 files in either folder.

### 9.1 Commit B has grown from two paths to four

This is the one item in the attached folders that needs action, and it is larger than previously
stated. `docs/HANDOVER/` now holds **three** ChatGPT handover versions, **two** Claude handover
versions and **two** status versions:

```
ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md   <- delete, D-23 predecessor
ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md   <- delete, D-23 predecessor
ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_9.md      KEEP, current
Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md                         <- delete, D-23 predecessor
Claude_HANDOVER_TO_Future_Claude_Chat_v0_10.md                           KEEP, current
ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT_FOR_BOTH_ROLES.md                  KEEP, not versioned
S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_2.md                       <- delete, D-23 predecessor
S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_3.md                          KEEP, current
```

**Revised Commit B, expected staged shape `0 A / 0 M / 4 D`:**

```
docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md
docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md
docs/HANDOVER/Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md
docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_2.md
```

Three superseded handover versions coexisting is the specific harm D-23 exists to prevent: a successor
chat that reads v0.7 or v0.8 gets an obsolete next action. v0.8 in particular still says S4 awaits
review, which is now two gates out of date.

### 9.2 Unchanged from the previous audit

**Commit A stays at exactly four paths** - the identity carriers under `experiments/S2-I3/`, all four
re-confirmed present at HEAD. Do this one first; it is the only time-sensitive item.

**Commit C stays at 52 candidate paths** pending owner agreement, as enumerated in status v0.3
section 8. Never by wildcard, because `experiments/stage2/` holds accepted code.

### 9.4 Does this review require changes to any ratified `docs/REPOSITORY/` document?

Checked directly against the committed text of all three documents the owner asked about. **No change
is required to any of them.**

| Document | Effect of this review |
|---|---|
| `interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md` | **None.** Its NONE decomposition and its 90.2% negative-rehearsal figure are both correct; see sections 3.1 and 5.3 for the two withdrawn criticisms. Still load-bearing until Route A completes |
| `S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md` | **None required.** Its `Q_fixed` claims, 14/16/18/14 for originals and constant 62 for blockys, are **independently confirmed** by this evidence from a different data path. Cosmetic only: the Role column still reads "admission pending" for SP and "original admission pending" for 3A, which the eight completed admissions overtake. Claude does **not** recommend revising a ratified design document for a stale operational annotation; let the Gate Report record the admissions and fold the wording into a future revision made for a substantive reason |
| `S2_I2_Evidence_and_Gate_Report_v0_1.md` | **None, and today strengthens it.** It records its own runtime correctly, NumPy 2.5.3 with BestSource DLL `fa5b9016...f69c`. The P0 run used the **identical DLL**, so this is a continuity confirmation rather than a conflict; the NumPy 2.5.3 to 2.5.4 difference is recorded in the P0 status document, which is its correct home. It makes no BLOCKED claims and S2-I2 was LP-centric, so the descriptive BLOCKED outcomes for SP, SP_blocky and 3A are new territory with nothing to reconcile |

**Route A transfers have not happened.** Claude confirmed `06_DEBLOCK_CONCEPT.md` contains none of the
corrected measurement figures, and the only reference to an S2-I3 Evidence and Gate Report anywhere in
`docs/REPOSITORY/` is inside the interim bridge itself. So the interim document is still load-bearing
and must not be retired. The four SHOULDs in this review are additions to the eventual Evidence and
Gate Report, which does not yet exist.

### 9.3 Now unblocked

The **seven-index tracking commit** was gated on P0 evidence acceptance. With this review, the
numerical and integrity preconditions are met, so it needs only the owner's acceptance. Expected shape
`7 A / 0 M / 0 D`, exact SHA-verified admitted bytes only, `git ls-files --eol` reporting `-text` for
every staged `.idx`, and the six frozen Stage 1 indexes untouched. **LP original is not in this
commit** - it is the pre-existing frozen baseline, which is why the count is seven and not eight.

## 10. When Claude's own handover needs updating

The owner asked directly. The answer is **now**, and here is the reasoning rather than just the
recommendation.

`Claude_HANDOVER_TO_Future_Claude_Chat_v0_10.md` states its as-at point as `35cd543`. Since then:
three commits have landed, the P0 campaign has run end to end, the isolated-Python incident happened
and was fixed, the interim knowledge bridge was installed, two status versions and a ChatGPT handover
version were installed, and this review has produced findings that exist **nowhere but in this
conversation**. v0.10's stated next action is obsolete in the same way v0.8's is.

The project convention is to refresh at every substantial milestone. **P0 gate closure is that
milestone.**

Two sequencing options, and Claude recommends the first:

1. **Write v0.11 now, revise it after the commits.** The findings in sections 3, 4 and 5 of this review
   exist only here. If this conversation ends before they are written down, they are lost and would
   have to be re-derived from the CSVs by someone who does not know they are there. The cost of this
   option is one small revision after the seven-index and hygiene commits land.
2. **Wait until after the seven-index commit and Commits A/B/C.** Produces one clean document with no
   revision, but leaves the new findings unrecorded for as long as that takes.

Option 1 is the safer order given the owner's stated concern about losing knowledge to abrupt chat
failure, and given that the new findings are the least recoverable thing in play. The commits that
would re-stale it are mechanical and their shapes are already written down in section 9, so a successor
could reconcile that delta easily.

Claude can produce v0.11 on request. It should carry, at minimum: this review's verdict and the four
SHOULDs; the control-margin numbers from section 3; the Q_fixed and transform-mix re-derivations from
section 4; the appearance-instrument versus population-sample distinction and both withdrawn claims from section 5; the S2-I4 forward note from section 5A; the revised four-path Commit B; the
unblocked seven-index commit and its exact expected shape; and the verified HEAD.

## 11. Unchanged constraints

No filtering has been run and none is authorised. `READY_FOR_P1` remains numerical. P1 requires
separate explicit owner authorisation after acceptance of this review. EP, TEST 2A and TEST 4A with
every `_blocky` copy stay locked until S2-I8 under any filename or alias. TEST 6A and 7A remain
committed but role-unassigned and outside the P0 allow-list. The six frozen Stage 1 indexes must never
be rewritten and `VHSC_samples\LG_576i_3_LP.idx` must remain byte-unchanged. The interim knowledge
bridge stays in place until the Route A transfers are complete and independently reviewed. Review
material must not enter the repository.
