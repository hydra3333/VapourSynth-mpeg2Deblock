# S2-I3 - Full-Data, Multi-Content-Group Luma Experiment Design

**Filename:** `S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md`
**Version:** 0.3; dated 2026-10-17
**Author:** ChatGPT; independently reviewed by Claude; ratified by project owner
**Status:** RATIFIED 2026-10-17 / DESIGN ONLY. No S2-I3 code, filtering or S2-I4 run authorised.
**Baseline:** Git commit `6e7b5c53df1c65775524936fc945c449cc9fa100`; ratified `Stage2_Experiment_Design_v0_7.md` supersedes v0.6 with this documentation-only installation.

---

## 0. Decision summary and why v0.1 changes

The owner's engineering preference is complete original recording data, rather than arbitrary
partitions masquerading as the real problem. Claude found that v0.1's LP, LP+LP_blocky and
LP_blocky optimisation paths were *one content group*, because the latter was a software
re-encode of the same footage. This v0.3 makes four materially different content groups
(XP, SP, LP, TEST 3A) the common development pool. Every group includes its original
and software `_blocky` counterpart. Development uses every eligible frame; no forced
720x576 geometry and no selecting favourable scenes. Entire-group cross-validation
provides the quality-assurance complement rather than replacing full-data engineering.

**Preferred protocol:** complete read-only source characterization -> source registration
and pairing gates -> same-budget grouped procedure comparisons -> predeclared choice ->
fit joint K0 on ALL EIGHT development recordings -> freeze K0 -> record source- and
native-GOP-specific in-sample behaviour. Further original-only and blocky-only fits
are separately frozen comparators. Hold-outs stay completely unopened for filtering
until S2-I8. The governing authority changes are in ratified Stage 2 v0.7, not an appendix.

## 1. Authority, invariants and boundary

This ratified S2-I3 design is subordinate to ratified Stage 2 v0.7; it does not
independently amend that authority. Stage 2 v0.7 supersedes the previous v0.6
sections 3/6/8.4/9/10/13.3/19, consistent with D-26's placement of source roles
in the Stage 2 design. No change to D-13 or D-24 is needed under B0.

Unchanged: frame-owned D-09; decoder frame + matching index; authoritative indexed
FRAME/FIELD/NONE residual geometry; coded NONE has no internal residual seam; frame-
and field-parity-appropriate pixel access; no support spanning another known transform
seam; no pixel-derived seam positions; indexed QP and one manual strength; conservative
bounded edge/detail protection; OFF bit-exact; no colour/chroma work until S2-I7;
no Stage 1 accepted index regeneration; no Family B architecture benchmark; optional
Family C non-blocking; `NOTICE.md` Restricted Media controls all actual and derived
visual media (ordinary numerical-text evidence excepted).

All quality evidence excludes leading B pictures before the first I (structural checks
still include them). Source geometry/metadata always comes from the corresponding
validated index. The currently finished S2-I2 report and implementation are frozen.

## 2. Development population and source roles

| Group | Original | Re-encode | Frame geometry | Q_fixed: original / blocky | Role |
|---|---|---|---|---|---|
| XP | `LG_576i_1_XP` | `LG_576i_1_XP_blocky` | 720x576 interlaced | 14 / 62 | Development |
| SP | `LG_576i_2_SP` | `LG_576i_2_SP_blocky` | 720x576 interlaced | 16 / 62 | Development, admission pending |
| LP | `LG_576i_3_LP` | `LG_576i_3_LP_blocky` | 720x576 interlaced | 18 / 62 | Development, S2-I2 verified |
| 3A | `TEST_3A_A002` | `TEST_3A_A002_blocky` | **704x576** interlaced | 14 / 62 | Development, original admission pending |

Each source is distinct as an encoding; each original/blocky pair is related picture
content. No re-encode is a new independent scene-content replicate. Q_fixed is the
**full-index all-MB median**, including NONE and leading-B entries where present;
quality evidence excludes those leading B frames. Never replace LP 18 with its
coded-only median 16. Re-evaluate hash, width, height, picture properties, all-MB
median and quality-eligible frame count from the owner's Windows indexes before runs.

**Explicitly reserved:** EP, 2A and 4A originals AND their `_blocky` counterparts are
locked together until S2-I8. The `_blocky` variant contains hold-out content despite
being a different encode. These six have no S2-I3 use, including diagnostics revealing
filter efficacy. Do not even use them for informal parameter selection.

**Controls:** MLS original and MLS_blocky are evaluated separately after final
freeze. Original MLS is a 352x288 progressive control. Claude found MLS_blocky is
352x288, has progressive_frame=0 and only 230 FIELD MBs over 420 frames; it is
not a meaningful 3x3 FRAME/FIELD contrast test. Treat syntax as observed, do not
artificially label it progressive or interlaced to make a test pass.

No source is resized/cropped to a common width. MB columns = index-declared coded
width / 16 (720 => 45, 704 => 44); all picture dimensions and valid coverage
must agree with the decoded frames. Each file keeps its native GOP structure.

## 3. Claude read-only preflight and admission gate

Claude used a scratch-index plus unchanged S2-I2-engine preflight on seven non-hold-out
sources. No filtering, no viewing detectability results, no protected content, and
decoded copies removed afterwards. Inspector exited 0; structures, 4:2:0 frame
pictures, picture types and known-bad mutation detection passed on all seven.

| Source | S2-I2 LP-specific numerical result | Interpretation for this design |
|---|---|---|
| XP | PASS | Re-run unchanged gate on owner's index |
| XP_blocky | PASS | Same |
| SP | BLOCKED: 3x3 frame-fraction 0.59; FRAME ~7% of coded MB | 3x3 underpowered; not proof of pixel shift |
| SP_blocky | BLOCKED: negative FRAME-FIELD contrast at all shifts | 3x3 discriminant premise unsupported; zero is nonetheless best |
| 3A original | BLOCKED: row 5.2% margin, frame fraction 0.61 | Marginal row evidence; not proof of shifted label map |
| 3A_blocky | PASS | Re-run unchanged gate on owner's index |
| MLS_blocky | 3x3 FAIL with only 230 FIELD MBs / 420 frames | 3x3 inapplicable as a contrast test; control only |

Important: these PASS and BLOCKED labels are outcomes of the **old LP-oriented
quantitative thresholds**. They are not preapproved source-admission decisions.
The same mechanism-grounded policy MUST apply to every new source, even prior PASSes.
The earlier S2-I2 and reviewer preflight views were unfiltered registration
or structural diagnostics, not filtered quality comparisons, and cannot
be used retrospectively to select a kernel.

### 3.1 Mandatory orthogonal admission (before quality or filtering)

The owner's **actual Windows BestSource + authoritative index** pipeline must
apply Stage 2 v0.7 section 6.3 to **all eight development sources**, including
those with old S2-I2 diagnostic PASS labels. It provides two HARD conditions:

1. Full index/decoder structural and temporal correspondence, including
   detected corruption/ordinal failures and 7/7 known-bad offsets.
2. **Exact MPEG-2 P-picture skipped-macroblock identity**: every qualifying
   decoded 16x16 luma block at its indexed coordinates must equal the
   co-located block of the prior I/P forward reference, pixel for pixel.
   A single wrong pixel is REGISTRATION FAIL; no percentage tolerance.

Declare spatial negative controls (+/-1, +/-2, +/-4, +/-8, +/-16 pixels,
horizontally and vertically, plus diagonals) and wrong temporal references
(older anchor, next/previous picture in display order when not the correct
anchor).
Each attempted control with valid blocks must show **less than 100%** exact
identity; no valid control evidence, or a control reaching 100%, means
INCONCLUSIVE - QUALITY BLOCKED, not REGISTRATION FAIL. Require at
least **200 qualifying P-skip macroblocks in >=10 distinct P pictures**,
otherwise INCONCLUSIVE. All source outputs include exact match counts,
per-frame minima, reference mapping and negative-control populations.

The unchanged S2-I2 shifted 3x3 FRAME/FIELD, column-phase and row-phase
measurements remain **mandatory reported diagnostics**, using their original
S2-I2 thresholds; they no longer determine admission for the new sources.
None of the old INCONCLUSIVE/FAIL diagnostic results is rewritten. Sparse
FRAME/FIELD populations and weak phase modulation do not weaken the hard
P-skip criterion. Report the residual limit: a consistent field swap in
both current and reference pictures is not independently exposed by this
P-skip test. Cross-pair frame correspondence has its own gate (section 5).

#### Independent reviewer rehearsal (not Windows acceptance)

Claude's FFmpeg/Linux, no-filter rehearsal on the same eight inputs found
100% exact P-skip identity at the true indexed position on every source,
with every exercised shifted and wrong-reference control below 100%.
Counts of matched P-skip macroblocks were XP 1619, XP_blocky 25635,
SP 1764, SP_blocky 19010, LP 1533, LP_blocky 20300,
3A 8812, 3A_blocky 18190. The maximum misregistered-control identity
was 96.7% on static 3A, confirming why no arbitrary sub-100% margin is
permissible. Source: `Claude_REVIEW_OF_ChatGPT_S2_I3_v0_2_and_Stage2_v0_7_v0_1.md`
section 2. This rehearsal does not admit Windows sources; redo the hard
gates in BestSource on the owner's verified index bytes before quality runs.

#### Index tracking authorised (but not installed)

The owner approves tracking seven development `.idx` files as explicit
**non-baseline Stage 2 inputs**: six new XP/SP/3A original/blocky indexes,
plus the existing LP_blocky scratch index. The original LP index remains
one of the six immutable Stage 1 baselines. No file is added by this design
package. Generate/validate on Windows under separate implementation authority,
record index file sizes and SHA-256 and Claude's earlier Linux reference
hashes, check repository `NOTICE.md` and identity restrictions, then stage
only the seven reviewed byte-exact files by name. Do not track elementary
stream/decoded media as index evidence. See Stage 2 v0.7 sections 3.6/6.3.

---

## 4. Full-data experiments and grouped quality assurance

### 4.1 Source preparation and descriptive characterisation

For all eight development files: capture exact media/index hashes, decoded format,
actual width/height, coding states, MB counts, all-MB QP histogram/median, GOP
ordinals, eligible/excluded frames, I/P/B, index eligibility and phase statistics.
No frames or scenes are manually dropped because their output looks poor. For
paired-reference numerical metrics, verify actual cross-file temporal correspondence
using a small window (e.g., N-2...N+2) after within-file index/frame validation.
Do not assume pair identity merely from matching frame counts and picture types.

### 4.2 Full-content-group leave-one-out procedure comparison

Run four folds: leave out XP group, SP group, LP group and 3A group in turn.
For each fold, train the algorithm-selection **procedure**, feature shortlist and
parameters afresh using every eligible frame of the other three groups; evaluate
on both members of the untouched group. No fold-held-out output is used to
change its own fitting or metric weighting. Candidate space, search/evaluation
budget, random seeds (if any), pixel/field-access convention and summary metrics
are held constant across arms. This is content-group cross-validation, not GOP
cross-validation. There are four independent content groups, not thousands of
independent MBs, so report per-group dispersion rather than p-values.

**Comparative arms:**

| Arm | Training material (of the 3 groups available per fold) | Primary question |
|---|---|---|
| O | all 3 originals | Does unmodified recorder-only development suffice? |
| X | all 3 blocky re-encodes | How well does severe-block-only tuning generalise? |
| J | all 6, balanced 2:1 original:blocky within each group | Joint development with/without re-encodes |
| L (optional historical) | LP original only | Historical single-source cost, XP/SP/3A evaluation folds ONLY |
| LB (optional historical) | LP original + LP_blocky | LP content-pair cost, XP/SP/3A evaluation folds ONLY |

L/LB are mathematically undefined for the LP-held-out fold: they get **N/A** there,
not permission to look at LP. For EVERY comparison involving L or LB,
compare all arms on identical held-out **XP, SP, 3A folds only**. Do not
compare a four-fold J/O/X score against a three-fold L/LB score; publish
separate four-fold J/O/X results.

**A priori weighting for J**: 25% per content group in full-data reporting;
within each group, 2/3 original and 1/3 blocky. During CV the three training
groups have equal weights; held-out groups have equal weight in aggregation.
This protects real recorder footage and prevents much larger raw seam counts in
constant-QP blocky data from determining the result. Report full unweighted
per-source results as well. Never retroactively adjust weights after results.

### 4.3 Two kinds of evaluation, not conflated

1. **Cross-validated, out-of-training-content**: each candidate fitting procedure
   is tested on a content group it did not see. Both pair members stay in the
   same fold, and the fold is locked during fitting. This gives per-group
   cross-source evidence, not a pristine independent external population.
   Because the cross-validation results choose among procedures, the
   **selected procedure's CV estimate is subject to selection optimism**;
   CV ranks procedures, while untouched S2-I8 content supplies the first
   external-content estimate for the final frozen candidate.
2. **Final full-data fits and reporting**: after CV procedure selection, run the
   preferred JOINT procedure on **all 8 recordings** and freeze an exact K0-J.
   Also fit O on all 4 originals (K0-O) and X on all 4 blockys (K0-X),
   freeze separately and cross-evaluate all three on all eight. That matrix
   measures real engineering in-sample behaviour; it is not cross-validation.
   Native even/odd GOP breakouts are optional descriptive stability tables
   (not separate training/independent testing). Do not align GOP parity across
   encodes.

Choose from the CV procedure comparison using a **predeclared selection rubric**:
minimum acceptable detail/no-harm, realistic seam improvement, no catastrophic
failure on any original, transparency on blocky stress gains, and owner's
blinded visual judgement (D-26). The owner remains final evaluator. Report
Pareto-incomparable choices rather than manufacture a scalar winner. K0-J is
the presumptive engineering deliverable because it is the all-eight fit the
owner requested; if it fails an agreed gate, propose a change openly rather
than quietly substituting K0-O or K0-X.

A failed admissibility check prevents final joint fitting; do not redefine
"all eight" to mean whichever clips happened to pass. If data are unavailable
for a substantive reason, return to design review.

## 5. Candidate option inventory and staged search

Preserve all options from Claude's non-authoritative v0.2 table: M1..M5;
M4a (adjacent-slope numerator with the M4 denominator) as a proposed additional
variant, not a rewrite of S2-I2 M4; F1..F3; R1..R4; T1/T2; P0..P2;
K1..K4; D0/D1; B0/B1; G1/G2. The owner required that choices be made
openly and no option silently discarded.

First measure diagnostic discrimination and edge/no-harm sensitivity on the
three training groups inside each fold; shortlist two or three practical
M/F/R/T/P/K combinations with reasons. Filtering on the held-out group must
NOT lead to changing that fold's shortlist. Apply the same shortlist-selection
procedure and comparable effort across O, X and J. G1/G2 are aggregate
read-only diagnostics; K4 is optional Family C and does not delay Family A;
D1 is optional and should be justified by demonstrated noise-limited failure.

**B0 ONLY** is available for the initial implementation: index geometry,
transform state and QP, with no extra coding-context boundary-strength
feature. B1 uses additional coding/CBP metadata and requires a separately
identified owner decision; mentioning it in the catalogue is not permission
to use it. No existing third-party deblocker is an authorised benchmark.

The numeric scoring must not treat indexed seams as proven visible artefacts.
Use declared off-seam controls and false-alarm rates, local edge protection,
full-frame no-harm metrics and I/P/B/state/QP breakdown. Keep a short-support
bounded kernel with off bit-exact. Capture every rejected option's reason.

## 6. S2-I4 QP comparison redesign: two complementary questions

All four ORIGINALS have real QP variation and Q_fixed 14/16/18/14;
all `_blocky` QPs are constant 62, so their fixed and indexed modes
are identical and do not establish spatial QP benefit.

**Q1 - fixed-parameter causal input switch:** on the same originals/frames,
apply K0-J unchanged except for QP input (all-MB clip-median versus actual
per-MB map). This is a paired input ablation answering how useful the QP
*information* is for an already selected filter; calibration favours the
regime used during K0 fitting, and the data were also part of final fitting.
Label these limitations. Report NONE-contact and QP saturation separately.

**Q2 - symmetric fit/calibration:** in the four grouped CV folds, fit a
fixed-QP branch and indexed-QP branch independently **with identical
algorithms, budgets, development groups, evaluation groups and no-harm rubric**.
Choose/tune within the three training groups; evaluate both unchanged on
identical left-out original frames and compare the paired per-group
statistics. Record both fitted parameter sets. This answers which regime
achieves better quality *after equally fair calibration*, not the one-variable
input-change question.

S2-I3 is **FIXED-QP ONLY** for fitting, filtering and candidate comparisons.
No real-indexed-QP branch is fitted or tested and no fixed-versus-real QP
comparison is produced in S2-I3. S2-I3 defines procedures and freezes K0-J;
actual QP ablation runs are **S2-I4 only**, subject to separate authorisation. A symmetric tuned
branch is never mislabelled as the original frozen K0. S2-I5 may then
revisit real-QP tuning, preserving all S2-I4 result identities. This
explicitly changes Stage 2 v0.6 section 8.4 and the section 19 ladder;
Stage 2 v0.7 is therefore required, not an appendix.

## 7. QA evidence, negative outcomes, and controls

**Metrics:** indexed seam difference before/after, seam-versus-off-seam
proxy discrimination (at declared false-positive rates), correction
frequency and amplitudes, edge/texture and off-support change, clamped
pixels, OFF bit-exactness, I/P/B and FRAME/FIELD/NONE breakdown,
real-QP bands and QP-112 saturation, per-GOP/frame uncertainty,
paired-reference movement toward the original where alignment is proven.
Do not infer perceptual success from proxy metrics alone.

**Visual:** owner inspects anonymised/shuffled comparisons, preferably
blinded as to arms; compare flat blocking, genuine edges, detailed texture,
noise, motion, field parity and representative MB classes. The owner's
visual judgement is final. Keep derived stills, heatmaps, plots and clips
within permitted Restricted Media boundaries; numerical/tabular evidence
is ordinary text unless visually laid out to reproduce spatial media.

**Controls:** MLS pair only after candidate freeze for progressive/format
no-harm. EP, 2A and 4A pairs remain unopened for filtering assessment until
S2-I8. At that point the owner-requested all-16-source census includes
8 development, 6 protected paired hold-outs, and 2 MLS controls. No
S2-I8 content influences prior kernel selection; failures are archived,
not used to quietly retune and call the same evidence pristine.

No p-values are justified by only four independent held-out content groups.
Store per-group outcomes and within-group frame/GOP intervals; don't count
one thousand adjacent seams as one thousand independent experiments.

## 8. Execution and authorisation gates

This ratified v0.3 remains a design, not a runnable instruction. The owner
has ratified Stage 2 v0.7 and this design after independent Claude review.
S2-I3 implementation and filtering still require a separate explicit owner
authorisation, reviewed code and a successful admission preflight. No real-QP
branch or S2-I4 comparison is authorised under S2-I3 design ratification.

When implementation is later authorised, use serial deterministic Windows
runs and bounded staging. Windows scratch indexes are regenerated only for
previously untracked/non-baseline recordings; no six frozen Stage 1 indexes
are modified. Store data, code, index hashes, source list, tool versions,
frame admission/exclusions and fold identities; preserve original and
blocky results side-by-side rather than merging source identities away.

**Implementation admission preflight (design CLOSED; Windows test PENDING):**
the exact P-skip proof is specified in section 3.1 and Stage 2 v0.7 section
6.3. On the first separately authorised Windows run, generate/verify the
seven development indexes, test all eight in BestSource using hard structure
and exact P-skip identity, retain unchanged S2-I2 diagnostic reporting,
and establish temporal frame correspondence for all four pairs before
paired-reference metrics. Any hard FAIL stops; INCONCLUSIVE blocks filtering.
The successful FFmpeg/Linux rehearsal is not Windows acceptance.

## 9. Disposition of Claude's findings

| Finding | v0.2 / v0.7 action |
|---|---|
| MUST M1 | Four content groups with original+blocky; not LP-only |
| MUST M2 | Per-index geometry; 3A 704x576 retained |
| MUST M3 | Uniform prefilter source gate; weak/inapplicable signal is explicitly INCONCLUSIVE; exact P-skip identity admission (v0.3) closes the alternate-proof gate |
| MUST M4 | Complete Stage 2 v0.7 (ratified), preserves original v0.6 versioned history |
| SHOULD S1 | Symmetric QP-fit comparison plus frozen input switch, not conflated |
| SHOULD S2 | Even/odd reporting descriptive only; D/E/F/G dropped from required campaigns |
| SHOULD S3 | 2:1 original:blocky per group; equal content groups |
| SHOULD S4 | Development paired-reference metric after verified cross-file frame correspondence |
| SHOULD S5 | EP/2A/4A blockys locked with their originals until S2-I8 |
| SHOULD S6 | MLS original+blocky controls, not development |
| OPTIONAL O1 | Four group-level outcomes; no p-values |
| OPTIONAL O2 | Blinded/shuffled owner visual review when practical |
| OPTIONAL O3 | O/X/J same-fold comparisons, LP-only and LP-pair optional where feasible |

## 10. Change log

### v0.3 - 2026-10-17 (RATIFIED)

- Removes owner-identifying location from the header and the unfounded
  applicability percentage/count thresholds for S2-I2 FRAME/FIELD signals.
- Requires hard structural and exact MPEG-2 P-skip/forward-reference identity
  on every source in the owner's Windows BestSource path before quality runs;
  unmodified LP-specific S2-I2 gate scores remain diagnostic.
- Requires identical fold sets for every LP-only/LP-pair comparison, records
  CV procedure-selection optimism, and confines S2-I3 strictly to fixed QP.
- Records owner's approval for Git tracking of seven *non-baseline* Stage 2
  development indexes, after separate Windows identity/validation/review.
- Applies Claude's review v0.1 M1/M2, S1-S5 and accepted optional
  clarifications, without changing the four content-group/hold-out policy.

### v0.2 - 2026-10-17 (DRAFT; superseded review draft)

- Replaces three LP-content-only development paths with four complete real-content
  original/blocky groups and whole-content-group cross-validation.
- Preserves full-data joint engineering as primary; original-only and blocky-only
  fits are retained for meaningful with/without comparisons.
- Discards false same-size requirement; provides proposed registration
  applicability/admission policy and honest INCONCLUSIVE classifications.
- Specifies frozen switch plus symmetric tuned QP ablation; protects all six
  EP/2A/4A encodes until S2-I8 and separates MLS control pair.
- No implementation or new authority granted.
