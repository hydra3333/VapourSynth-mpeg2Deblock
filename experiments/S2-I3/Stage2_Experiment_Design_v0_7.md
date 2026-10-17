# Stage 2 Experimental Deblocking Design

**Filename:** `Stage2_Experiment_Design_v0_7.md`
**Version:** 0.7 - RATIFIED 2026-10-17
**Date:** 2026-10-17
**Prepared by:** ChatGPT, from the ratified Stage 2 v0.6 source and Claude's reviews of S2-I3 designs v0.1/v0.2
**Status:** RATIFIED 2026-10-17 by the project owner following independent Claude clearance. Supersedes ratified Stage 2 v0.6 at the documentation-only installation. S2-I1 and S2-I2 are closed; S2-I3 experimental design v0.3 is ratified, but no S2-I3 implementation, filtering or quality runs are authorised.
**Stage 1 prerequisite:** `Stage1_Evidence_and_Gate_Report_v0_3.md` ratified.
**Repository authority:** `05_DECISIONS_v1_2.md` ratified; `06_DEBLOCK_CONCEPT.md` v1.2 ratified; `02_INDEX_FORMAT_SPEC.md` v0.4 current ratified constraints (not final frozen packing).
**Scope:** Stage 2 Python/scalar experiment design, sample assignments and evidence protocol. The inherited MPEG-2, index, frame, chroma and Restricted Media rules remain unchanged.
**Base:** `Stage2_Experiment_Design_v0_6.md` as carried at repository commit `6e7b5c53df1c65775524936fc945c449cc9fa100`. Source bytes hashed in review manifest.

---

## 0. Purpose

Stage 1 established a credible, output-frame-correspondent metadata source for the tested MPEG-2
frame-picture material.

Stage 2 now addresses the ratified project question:

> **Given authoritative indexed MPEG-2 geometry and QP, what filtering rule produces useful luma
> and chroma deblocking without unacceptable damage, and which indexed metadata are actually needed
> by the final production filter?**

The production architecture is already decided to be **index-driven** (D-24).

Therefore Stage 2 does **not**:

- build a pixel seam-position detector;
- build Family B as a pixel-only architecture control;
- compare index-driven versus pixel-only production architectures;
- require the custom index to justify its existence by beating a pixel-only alternative;
- use an existing external filter as a planned yardstick.

Those older v0.1 experiments are superseded by the ratified repository direction.

Stage 2 may still conclude that:

- the chosen filtering kernel is ineffective;
- useful artifact reduction requires unacceptable detail loss;
- off-grid / prediction-propagated blocking bounds the achievable benefit too severely;
- chroma filtering causes unacceptable colour damage or field mixing;
- more filtering research is needed before production implementation;
- or the project should stop.

That is the feasibility gate that remains.

---

## 1. Authority and inherited constraints

This design is subordinate to:

- `05_DECISIONS_v1_2.md`;
- `06_DEBLOCK_CONCEPT.md` v1.2;
- `02_INDEX_FORMAT_SPEC.md` v0.4 constraints;
- `Stage1_Evidence_and_Gate_Report_v0_3.md`.

The project proposal remains historical/workflow context only where later authority has not
superseded it.

### 1.1 Frame-owned processing

**DECIDED (D-09).**

The processing object is the decoded VapourSynth frame.

Do not split an interlaced frame into two independently deblocked field images.

Use field-parity-aware sample access where filtering across a seam would otherwise mix temporally
different fields.

### 1.2 Indexed geometry is authoritative

**DECIDED (D-24).**

For the supported luma frame-picture path, seam geometry / eligibility comes from MPEG-2 coding
structure and the index.

Pixels do not decide whether a macroblock is FRAME or FIELD.

Pixels remain essential for:

- blocking-versus-real-edge classification;
- local activity / flatness assessment;
- correction limiting;
- no-harm protection.

The production model is therefore:

```text
index metadata
    -> seam geometry / eligibility

decoded pixels
    -> block-like versus real-detail judgement
    -> local activity / edge protection

indexed QP + global strength
    -> threshold / correction scale
```

### 1.3 Transform-state semantics

The index states:

```text
FRAME
FIELD
NONE
```

`NONE` means:

> no current coded residual transform geometry is asserted for that macroblock.

It does **not** mean:

> no visible blocking can exist there.

Prediction may propagate prior blocking into skipped or no-residual areas.

### 1.4 Luma geometry in frame pictures

For a 16x16 luma macroblock in a frame picture:

```text
FRAME:
    fixed macroblock-edge locations
    +
    internal vertical transform seam at x = 8
    +
    internal horizontal transform seam between frame lines 7 | 8

FIELD:
    fixed macroblock-edge locations
    +
    internal vertical transform seam at x = 8
    no FRAME-style mid-height horizontal transform seam

NONE:
    fixed macroblock-edge locations only
    no internal vertical transform seam
    no internal horizontal transform seam
```

The internal x = 8 seam exists for both FRAME and FIELD coded macroblocks because their coded
8x8 blocks are arranged left/right in both organisations. A NONE macroblock has no coded residual
blocks, so it has no internal transform seam in either orientation. Its outer macroblock edges may
still be examined because prediction can propagate blocking or discontinuities there.

For interlaced frame material, D-09 requires field-parity-aware access where ordinary adjacent-line
filtering would mix fields.

For the FRAME internal horizontal seam this gives, relative to the 16-line macroblock:

```text
top-field pair around the seam:       6 | 8
bottom-field pair around the seam:    7 | 9
```

### 1.5 4:2:0 chroma

**DECIDED in scope (D-25); mechanics accepted as K-04, K-10 and K-11.**

For the inspected MPEG-2 4:2:0 frame-picture path:

- one 8x8 Cb block and one 8x8 Cr block correspond to each 16x16 luma macroblock;
- chroma transform placement does not follow luma `dct_type`;
- chroma uses the macroblock's same effective `quantizer_scale`;
- the inspected reference decoder selects the luma quantisation-matrix path for 4:2:0;
- in field prediction, chroma-line parity alternates top/bottom by line.

The first chroma experiment therefore uses:

```text
native Cb / Cr planes
+
fixed 8x8 chroma transform grid
+
indexed effective per-MB QP
```

Do not import luma FRAME/FIELD/NONE transform geometry into chroma placement.

Whether interlaced horizontal chroma filtering should use same-field-polarity access remains a
Stage 2 design question (O-06/O-14), with V4 providing a verified parity premise.

### 1.6 Support constraint

For the initial short-support candidate:

> **Support for one known transform seam must not cross another known transform seam.**

This is a filter-design constraint, not an MPEG-2 normative rule.

### 1.7 Initial metadata scope

The first Stage 2 filtering work uses:

- authoritative luma FRAME/FIELD/NONE state;
- effective per-macroblock QP;
- per-picture `progressive_frame`;
- picture type for I/P/B reporting and leading-B quality exclusion;
- frame/dimension correspondence needed for index validation.

Do not initially consume:

- coded-block pattern as a filtering input;
- coefficient activity;
- prediction mode as a filtering input;
- motion vectors;
- quantisation-matrix coefficient values.

Availability in the Stage 1 temporary index does not imply production retention.

---

## 2. Stage 2 questions

### Q2-01 - Does the candidate index-directed filtering family help?

Can a short-support, edge-preserving filter reduce visible MPEG-2 blocking on real LG material
without unacceptable detail damage?

### Q2-02 - Does the real per-MB QP map help?

Use two explicitly separate comparisons on the real original recordings: (a) with one fully frozen
kernel and all other parameters identical, swap only clip-median QP for the real effective per-MB QP
(identifies the effect of the QP input for that kernel); and (b) fit fixed-QP and indexed-QP branches
with equal search effort inside identical content-group cross-validation folds (compares performance
under equally tuned regimes). Do not conflate these estimands. All `_blocky` source QPs are constant
62, so they cannot independently identify the value of a spatial QP map.

### Q2-03 - What kernel / thresholds / strength are useful?

What bounded, no-harm-protected, index-directed luma correction generalises across different
actual recording content groups when finally fitted using all designated development recordings?
Use the entire eligible development population; evaluate generalisation by leaving an entire
source-content group out rather than reserving half of one clip.

### Q2-04 - How should `NONE` be treated?

What conservative index-consistent policy best handles visible blocking in macroblocks with no
current coded residual transform geometry?

### Q2-05 - What is the practical limit from I/P/B prediction?

Does useful benefit differ materially among I, P and B pictures, consistent with the known
off-grid / propagated-blocking limitation?

### Q2-06 - How should chroma be filtered safely?

For native MPEG-2 4:2:0 chroma:

- what thresholds and strength are useful?
- does real per-MB QP improve behaviour?
- what horizontal/vertical treatment is appropriate?
- what interlaced sample-access rule is safe?
- can colour smearing and field mixing be avoided?

### Q2-07 - Which indexed metadata survive into the final production design?

Stage 2 does not freeze the final `.idx2`.

It should identify which currently available metadata the eventual production filter actually
consumes.

---

## 3. Experimental material and evidence hierarchy

### 3.0 Recorder quality order versus experimental role

The LG recorder quality order remains `XP -> SP -> LP -> EP -> MLS`; this is not an assignment
of experimental role. The four S2-I3 development content groups, in each case using native,
unaltered decoded frames and native macroblock indexes, are:

| Group | Original recording | Software re-encode | Original Q_fixed | Blocky Q_fixed |
|---|---|---|---:|---:|
| XP | `LG_576i_1_XP` | `LG_576i_1_XP_blocky` | 14 | 62 |
| SP | `LG_576i_2_SP` | `LG_576i_2_SP_blocky` | 16 | 62 |
| LP | `LG_576i_3_LP` | `LG_576i_3_LP_blocky` | 18 | 62 |
| 3A | `TEST_3A_A002` | `TEST_3A_A002_blocky` | 14 | 62 |

Every group is distinct source content; the original and `_blocky` of a group share picture
content, despite being different encodes. These assignments are ratified in v0.7
(2026-10-17). All quality-eligible frames of each accepted source
are used in full-data development. Leading B pictures remain subject to section 4.

Geometry is source-specific, not forced to LP: XP/SP/LP are 720x576; 3A is 704x576. The
prototype must derive coded MB columns/rows, pixel dimensions and valid picture structure from
the validated source index; NEVER hard-code 720 width or 45 macroblock columns.

The sources reassigned from the historical unassigned/spare category
are XP, SP and 3A (both versions), and LP_blocky. There are no new *unassigned* blocky variants of these four groups. The remaining
protected/control samples are explicitly assigned below, rather than being silently treated
as tunable material.

### 3.1 Primary product and development evidence

**D-26 remains controlling: real recorder material is primary.** S2-I3 develops using the four
originals above, together with their four software re-encodes as paired stress/comparison material;
it does not treat the re-encodes as four independent recordings. The primary final joint K0
procedure is fitted on **all eight** designated sources, after full leave-one-content-group-out
procedure assessment, using a source/content-group-balanced objective defined in section 8.4.

Original-only, blocky-only, LP-only and LP-pair routes may be retained as controlled comparison
arms, but not substituted for the declared final full eight-source fit without an explicit
owner decision. Failed or registration-blocked sources are NOT quietly dropped; they suspend
final full-data development until the common admission procedure in section 6.3 resolves them.

Product evidence consists chiefly of the owner's visual assessment, seam-local diagnostics,
collateral/no-harm diagnostics and consistency across materially different content groups.
Do not let sample counts or the greater number of NONE MBs in re-encodes dominate that judgement.

### 3.2 LP heritage and unchanged technical rationale

LP remains a particularly informative development source: 720x576, original 204 frames,
45x36 MBs, rich FRAME/FIELD/NONE coverage, and all-MB median QP 18. Its Stage 1 reference
histogram and code baselines are unchanged. Stage 2 v0.6's justification of LP as the first
real LG tuning clip remains historical motivation, but is not a restriction that excludes XP,
SP or 3A from v0.7 development.

### 3.3 Locked hold-out content

Until S2-I8 (after final kernel and thresholds are frozen), no development, screening,
visualisation, tuning, filtered-output viewing or procedure selection may use:

- `LG_576i_4_EP` and `LG_576i_4_EP_blocky`;
- `TEST_2A_A001` and `TEST_2A_A001_blocky`;
- `TEST_4A_A003` and `TEST_4A_A003_blocky`.

The original clips are the ratified locked interlaced hold-outs. Their `_blocky` copies share
the same picture content and therefore inherit the protection, despite their earlier
paired-reference/secondary label. If a hold-out exposes a flaw, record it; any retuning makes
that material no longer pristine for a subsequent independence claim. Do not automatically
alter S2-I3 in response to S2-I8 results.

### 3.4 MLS control pair

`LG_576i_5_MLS` remains the 352x288 progressive control (original: progressive_frame=1;
FIELD=0); `LG_576i_5_MLS_blocky` is a separate 352x288 control whose syntax reports
progressive_frame=0 and only 230 FIELD MBs in 420 frames. A picture flag is not license to
pretend that FRAME/FIELD contrast has adequate population. Neither MLS clip is development
or held-out interlaced quality evidence. Evaluate both after freeze for no-harm,
frame-domain handling and format robustness, with separate applicability of field-specific
registration diagnostics. The unexpected metadata combination is a reported condition, not
normalised away.

### 3.5 Paired-reference status and applicability

XP, SP, LP and 3A each have an original/blocky development pair; after proving temporal frame
correspondence, the original may serve as a **higher-quality decoded reference** for the blocky
member's relative MAE/MSE/PSNR and seam/non-seam comparisons. The original is NOT pristine
ground truth. Pair metrics are admissible in development and per-group cross-validation only
where pairing is independently proven, with both members of a content group kept within the
same fold. EP/2A/4A pairs remain entirely locked until S2-I8; MLS pair remains control.

### 3.6 Accepted Stage 1 index baselines and derived-media discipline

The six tracked accepted Stage 1 `.idx` files are immutable regression baselines for Stage 2 reader
validation:

```text
LG_576i_3_LP.idx
LG_576i_4_EP.idx
LG_576i_5_MLS.idx
TEST_2A_A001.idx
TEST_2A_A001_blocky.idx
TEST_4A_A003.idx
```

Do **not** regenerate or replace these files merely to make a reader or test pass. A genuine format or
accepted-baseline change requires its own explicit change control and verification.

**Distinct, owner-approved Stage 2 non-baseline index set:** the seven
additional development indexes, not members of the six frozen baselines, are:

```text
VHSC_samples/LG_576i_1_XP.idx
VHSC_samples/LG_576i_1_XP_blocky.idx
VHSC_samples/LG_576i_2_SP.idx
VHSC_samples/LG_576i_2_SP_blocky.idx
VHSC_samples/LG_576i_3_LP_blocky.idx
VHSC_samples/TEST_3A_A002.idx
VHSC_samples/TEST_3A_A002_blocky.idx
```

The owner approved Git tracking of these seven **only as Stage 2 development
inputs**, not Stage 1 accepted baselines. Six are newly generated scratch
indexes; the LP_blocky index was previously generated for S2-I2 and remains
non-baseline. Before any installation, the authoritative Windows inspector
and Stage 1 structural reader must verify them against their source media;
record Windows SHA-256, size, index version, source identity and Linux
cross-check hashes in a separate manifest. Retain the reviewed bytes in Git,
with explicit named staging and after-push verification. If the LP_blocky
Windows index differs from the earlier scratch hash, investigate; do not
silently replace it. Indexes containing ordinary nonvisual coding metadata
are not Restricted Media under the existing section 3.6/NOTICE distinction;
verify no embedded media or owner-identifying material before committing.
Tracking approval is not an instruction to generate or stage them now.

Stage 2 may create Restricted Media and non-media diagnostic artefacts as bounded evidence. The
governing definitions are in `NOTICE.md`; this section summarizes the Stage 2 consequences.

Source Recordings are the recordings expressly included for project testing, presently the video
recordings under `VHSC_samples/`. Derived Media includes:

- filtered clips, matched crops, still frames, difference images and audio extracts that reproduce or
  transform Source Recording picture and/or sound; and
- media visualisations derived directly or indirectly from Source Recording metadata, measurements
  or analysis, including QP heat maps, seam-statistics plots, charts, maps, masks and similar
  visualisations.

The second category is intentionally Restricted Media even when it contains no recognisable source
frame. This is the project owner's selected option (a).

The accepted Stage 1 `.idx` files, hashes, logs, metadata, source code and purely numerical or textual
diagnostics are not Restricted Media merely because they derive from or analyse Source Recordings,
provided they do not themselves contain or embed Restricted Media.

Ordinary CSV/tabular/text files containing numerical or textual metadata, measurements or diagnostics
remain non-media under that rule. A character/text grid deliberately arranged to visually reproduce
or represent spatial Source Recording-derived content is treated by its content/function, not its
file extension, and falls under the Derived Media visualisation rule.

Under the coordinated `NOTICE.md` / `README.md` / Stage 2 media policy proposed by this v0.6
reconciliation:

- Source Recordings and Derived Media may remain in this repository during active development only
  while reasonably necessary for project testing, validation, diagnosis, bounded evidence or review;
- Restricted Media is not permanent project authority;
- until **Development Closure**, Restricted Media supplied by the project maintainer for this
  project's own development conversations may be received/accessed/used by ChatGPT and Claude AI
  only as reasonably necessary for this project's permitted development purposes; this exception is
  limited to those two AI services and does not authorise unrelated reuse, publication, broader
  redistribution, model training/fine-tuning/adaptation or post-closure retention;
- apart from active-development repository use and that narrow AI exception, Restricted Media must
  not be separately shared, uploaded or transmitted to another person or service;
- copies outside the permitted active-development repository/AI use must be deleted or destroyed as
  soon as practicable after their permitted project purpose is complete;
- **Development Closure** is the point at which the project owner expressly declares active development finished;
  at that point all Restricted Media is removed from the current repository tree and project-
  controlled release/assets storage, and the ChatGPT/Claude AI development exception ends;
- the separately planned Development Closure Git-history purge is intended to remove historical
  repository copies as well; after cleanup the project/repository may continue as an ongoing
  maintenance project, but Restricted Media stays out of the Git tree/history unless a separately
  reviewed and ratified decision says otherwise;
- Restricted Media is not used as content for additional/reusable media datasets, corpora,
  collections or training sets, and is not used to train, fine-tune, adapt or otherwise alter
  machine-learning or artificial-intelligence model parameters;
- `NOTICE.md` is the governing text if this summary and `NOTICE.md` ever differ; any later change to
  the governing media policy must be carried into this section in the same coordinated,
  owner-ratified change.

A report or document that embeds Restricted Media is itself treated as Restricted Media while the
embedded content remains. A media-free/redacted final version may be retained under the ordinary
project terms. This allows temporary Stage 2 gate evidence while ensuring the final repository can be
media-free.

### 3.7 No existing-filter yardstick

Per the project owner's explicit 2026-10-08 ruling:

> No existing external deblocker is part of the planned Stage 2 comparison.

Revisit only if later evidence creates a specific need.

---

## 4. Excluded leading B pictures

Some extracted real LG clips begin with B pictures whose normal prediction context extends before
the clip.

For quality evidence, use the observable index rule:

> **Exclude B pictures output before the first I picture of the clip.**

Exclude those pictures from:

- parameter tuning;
- quality metric aggregates;
- visual A/B selections;
- feasibility conclusions.

Still process and validate them for:

- record/frame correspondence;
- parser / index robustness;
- bounds safety;
- diagnostic completeness.

Record the number of excluded leading B pictures for each clip.

---

## 5. Prototype architecture

Stage 2 is a research prototype, not the production VapourSynth plugin.

### 5.1 Language and execution model

Preferred first implementation:

- Python 3;
- VapourSynth / BestSource for decoded frames;
- NumPy for scalar/reference operations where convenient;
- Stage 1 temporary-index reader;
- deterministic per-frame processing;
- serial runs acceptable;
- 64-bit Python and 64-bit native/helper bindings throughout the prototype environment, consistent
  with the accepted x64 VapourSynth/build environment; do not introduce a mixed-bitness or 32-bit
  helper path.

No C++, API4 production plugin or AVX2 optimisation belongs in Stage 2.

### 5.2 Inputs

For each clip:

```text
BestSource decoded frame
+
matching validated index (accepted Stage 1 baseline or section 6.3-admitted non-baseline index)
```

Reject:

- wrong magic/version;
- incomplete index;
- dimension mismatch;
- frame-count mismatch;
- record ordinal mismatch;
- unsupported field-picture structure for this experiment.

Do not weaken Stage 1 validity checks because Stage 2 is experimental.

### 5.3 Outputs

The prototype should be able to produce:

- filtered lossless comparison output;
- difference frames / maps;
- seam / eligibility maps;
- per-seam diagnostic records;
- CSV or other machine-readable metrics;
- per-frame summaries;
- I/P/B aggregate summaries;
- QP-band aggregate summaries.

### 5.4 Reproducibility

Every run must record:

- input filename;
- index filename;
- frame range;
- variant ID;
- parameter set;
- fixed-QP rule/value where applicable;
- global strength;
- code/script version;
- excluded leading-B count;
- aggregate results.

No result should depend on an unrecorded interactive setting.

---

## 6. Mandatory pre-filter validation

### 6.1 Temporal / structural validation

Stage 1 already established the intended output-record correspondence model.

Stage 2 repeats cheap checks:

```text
index records == BestSource frames
dimensions match
record ordinals match
picture structure supported
```

The new Stage 2 index reader must also reproduce the already-verified analyzer v0.2 summary totals
for each formal clip, including at least:

```text
record count
FRAME / FIELD / NONE totals
effective-QP histogram / totals
```

A mismatch is a reader/interpretation failure and must be resolved before filtering experiments.

`TEST_4A_A003_blocky` was part of the formal Stage 1 original-versus-blocky evidence, but its `.idx`
is not one of the six tracked immutable regression baselines. During S2-I1, if that index remains
untracked/absent, generate it with the frozen accepted inspector, validate the resulting
record/state/QP statistics against `Stage1_Evidence_and_Gate_Report_v0_3.md` section 8.1 and the
accepted correspondence evidence, and present the result to the project owner. Generation/validation does **not**
make it a seventh immutable baseline; tracking/baseline status requires a separate the project owner decision.
The generated `TEST_4A_A003_blocky.idx` and `.log` remain uncommitted unless the project owner explicitly decides to track them; check `git status --short` before any snapshot commit.

### 6.2 Spatial index-to-pixel registration

**MUST complete before filtering-quality conclusions.**

The following is the S2-I2 diagnostic originally validated on LP. Its numerical
benchmarks remain unchanged; it does not imply that an intrinsically
low-information population is misregistered. For *new-source admission* the
uniform PASS / INCONCLUSIVE / FAIL interpretation in section 6.3 additionally
controls. In particular, the original section's generic "failure requiring
investigation" does not automatically become a demonstrated coordinate error
when the signed contrast or phase signal is non-discriminating.

Stage 1 proved temporal correspondence but did not independently prove that macroblock `(x,y)` in
the index is spatially registered to decoded pixels at the intended 16x16 luma location.

On LP, produce a detector-free two-dimensional registration diagnostic.

#### 6.2.1 FRAME-versus-FIELD contrast

At the indexed mid-height position, measure the same-field-polarity luma step separately for
indexed FRAME and FIELD macroblocks and define a declared contrast statistic, for example:

```text
C = mean_step(FRAME) - mean_step(FIELD)
```

Compute the same statistic after shifting the **index labels**, not the pixels, by one macroblock:

```text
x shift: -1, 0, +1 macroblock
y shift: -1, 0, +1 macroblock
```

The primary registration expectation is:

```text
C at zero shift
    >
C at each one-macroblock shifted control
```

or, more generally, the FRAME-versus-FIELD contrast should **peak at zero shift**.

This gives a relative control rather than relying on an arbitrary absolute definition of
"strongly enough".

#### 6.2.2 Horizontal/grid-phase check

Independently measure mean luma step across vertical sample boundaries by 8-pixel column phase:

```text
x mod 8 = 0
versus
x mod 8 = 1..7
```

The coding-grid step should peak at phase 0.

This specifically tests horizontal registration that the mid-height FRAME/FIELD contrast alone
could miss.

#### 6.2.3 Interpretation

Also report the fixed macroblock-edge step for FRAME and FIELD populations as a diagnostic.

These tests are **registration validation**, not production seam detectors:

- they do not infer FRAME/FIELD/NONE from pixels;
- they do not move the production seam map;
- they only test whether the authoritative index and decoded pixels are spatially aligned.

For the historical LP-specific S2-I2 gate, missing an expected zero-shift peak
required investigation before accepting the S2-I2 spatial registration result.
That historical outcome is not rewritten. Under the eight-source S2-I3
scheme, non-peaking or weak contrasts remain mandatory **reported diagnostics**:
inspect seam coordinates, crop, shifts and parity, but decide source admission
**only** by section 6.3's structural and exact P-skip hard checks. A diagnostic
score by itself is not a reason to block an otherwise REGISTERED source.

An 8-pixel horizontal offset may preserve the 8-pixel column phase and make a
single grid-phase measure look plausible. Preserve this known limitation and
report its numeric observations without converting it to a new gate.

Do not automatically reinterpret pixels to override indexed geometry.

### 6.3 Per-source pre-filter admission gate (v0.7)

**Scope and rationale.** Apply the same registration admission to all eight development
sources, even where the original S2-I2 numerical test passed. The S2-I2 3x3 and
column/row-phase tests measure content-dependent contrast; they are not, by themselves,
an exact registration proof for all coding-state populations. Admission instead uses
index/decoder structural agreement plus the exact P-picture skipped-macroblock identity
in section 6.3.2. These are hard gates, not recalibrated LP-specific thresholds.

#### 6.3.1 HARD structure and correspondence

Validate the source's accepted Stage 1 baseline index or newly generated, explicitly
non-baseline index against the **same** decoded recording: reader version/magic and
completeness, file and picture structure (MPEG-2 frame pictures, 4:2:0), dimensions,
macroblock geometry, frame counts/ordinals, picture-type correspondence, expected
leading-B exclusion and structural summaries, no damage or unsupported frame/picture
format. All seven known-bad S2-I2 offset mutations must be detected. Any mismatch is
a **HARD FAIL**, not an inconclusive statistical result. The six accepted Stage 1
indexes must never be modified or regenerated to obtain a PASS.

#### 6.3.2 HARD P-skip identity in the actual Windows BestSource path

For an MPEG-2 frame P picture, a skipped macroblock with zero motion, frame
prediction and no coded residual must reconstruct as an exact co-located 16x16
luma copy from the forward reference picture (the immediately preceding I
or P picture in display order, which is also the most recently decoded
anchor). MPEG-2 has no in-loop filter. Using the *actual source index's*
P-skip flags and reference-picture mapping, compare every eligible such block
with the co-located decoded reference block, all pixel values exactly:

A qualifying block is a macroblock whose index coding state is SKIPPED
(skipped by macroblock_address_increment) inside a P frame picture. NONE
macroblocks of any other coding state (for example INTER with CBP 0, which
may carry a non-zero motion vector) do not qualify.

```
Y[P][16*mb_y : 16*mb_y+16, 16*mb_x : 16*mb_x+16]
    == Y[prior_I_or_P_reference][same 16x16 region]
```

The identity rate **must equal 100.000%**, including per-P-picture rates on
pictures containing qualifying P-skip blocks; **any single wrong pixel in any
true-position qualifying block is REGISTRATION FAIL**, regardless of aggregate
rate. A test may not round a near-perfect result up to 100%.

**Negative controls:** rerun the same eligible comparison with shifted sampled
windows at +/-1, +/-2, +/-4, +/-8 and +/-16 pixels in horizontal and vertical
directions, and with declared diagonal offsets; preserve the seven known-bad
S2-I2 offsets as structural mutations. The same offset is applied to the
current and reference windows; only windows lying wholly inside the picture
are counted. Also use wrong temporal references:
older I/P anchor (when available), next picture in display order, and
immediately previous picture in display order whenever that is not the
correct reference. For
**each** declared spatial and temporal negative-control case having valid
comparisons, the exact-block identity rate **must be strictly below 100%**.
Log the attempted, in-bounds, excluded and compared block counts per control;
a missing, zero-denominator, or unexecuted control is **INCONCLUSIVE**, never
silently counted as a PASS. Freeze the explicit finite shift/diagonal and
reference-selection list in the separately reviewed implementation plan before
running admission. The true-coordinate rule is dictated by MPEG-2 syntax, not
tuned to previous outcome scores. Static pictures may give high but sub-100%
control rates; no arbitrary margin is imposed.

**Applicability floor:** at least **200 qualifying P-skip macroblocks** from at
least **10 distinct quality-eligible P pictures**. Below either count the
source is **INCONCLUSIVE - QUALITY BLOCKED** even if every observed block
matches. These robustness floors are declared in advance, not fitted from
registration scores.

**Disposition:** structural FAIL or any true-position mismatch is
**REGISTRATION FAIL - HARD STOP**. Insufficient qualifying blocks or P pictures,
a missing valid negative control, or any executed negative control also
reaching 100% (non-discriminating content) is
**INCONCLUSIVE - QUALITY BLOCKED**. All conditions met is **REGISTERED**.
The exact P-skip proof is orthogonal to the S2-I2 seam/FRAME-FIELD proxies
and additionally tests temporal index/decoder alignment; it does **not**
prove an independent field-swap guarantee when the same swap affects both
pictures. Do not silently drop an INCONCLUSIVE source from the eight-source fit.

#### 6.3.3 Required diagnostic reporting (not an admission gate)

Run the **unchanged** S2-I2 3x3 shifted-offset, column-phase and row-phase
measurements, including the original thresholds, frame fractions, signed
contrasts, population sizes and 7/7 mutation outcomes, on every structurally
valid development source (including P-skip-INCONCLUSIVE ones where safe). Report PASS/FAIL/INCONCLUSIVE under the *original* S2-I2 criteria as
**diagnostic**, separately from the section 6.3.2 admission disposition.
Never relabel a historical S2-I2 result or loosen its threshold to admit a
source. Sparse FRAME/FIELD populations, zero or negative contrast and weak
row-phase modulation explain why those diagnostics may be inconclusive even
when exact P-skip registration succeeds.

#### 6.3.4 Evidence and first authorised implementation preflight

Claude's **FFmpeg/Linux rehearsal**, prior to Windows authorisation, gave
100% true-position P-skip identity on all eight sources and less than 100%
for every tested shifted/wrong-reference control. This is strong,
**non-authoritative rehearsal evidence**; its method was proposed after the
reviewer had seen the old S2-I2 outcomes, but its exactness criterion comes
from MPEG-2 reconstruction semantics, not an outcome-fitted threshold.

On the owner's **first separately authorised S2-I3 implementation preflight**,
Windows generates/verifies the seven non-baseline development indexes as
needed and records hashes; the owner's accepted LP index remains untouched.
The actual **BestSource** pipeline must perform all section 6.3.1/6.3.2 hard
checks on **all eight** prior to any filtering/quality run. Run 6.3.3 for
reporting, plus the four development-pair temporal correspondence checks
(section 15). Stop on any FAIL. Inconclusive admission blocks quality runs
pending review. No Linux-only result substitutes for the Windows result.

Seven additional indexes (six new source indexes plus the existing
LP_blocky scratch index) are approved for Git tracking as **non-baseline
Stage 2 development inputs**, conditional on authoritative Windows validation,
complete SHA-256 manifest, absence of embedded Restricted Media or identity
material, and named-file staging/review. Preserve their exact file bytes;
track neither intermediate elementary streams nor decoded media. A separately
ratified installation procedure is required; approval to track indexes does
not itself authorise generating, committing or executing S2-I3 code.

---

## 7. Initial luma boundary abstraction

A boundary operation receives conceptually:

```text
samples on side P
samples on side Q
boundary orientation
sample stride / parity-aware stride
boundary class
effective QP or fixed clip QP
global strength
pixel activity / edge state
```

For a vertical boundary:

```text
... p2 p1 p0 | q0 q1 q2 ...
```

uses neighbouring horizontal samples.

For horizontal boundaries in interlaced material, use parity-aware row access where ordinary
adjacent-line access would mix fields.

The implementation must make the access rule explicit.

---

## 8. Initial candidate luma kernel

The production kernel is not yet decided.

Stage 2 begins with a deliberately parameterised, short-support candidate.

### 8.1 Required properties

The candidate must:

- operate only at index-eligible / fixed coding-grid seams;
- reject strong genuine edges;
- use short support;
- clamp correction magnitude;
- allow thresholds / limits to scale monotonically with QP and strength;
- avoid crossing another known transform seam;
- be suitable for later integer scalar and AVX2 implementation.

### 8.2 Candidate pixel tests

The first candidate may combine:

1. boundary step magnitude;
2. same-side local activity;
3. bounded local range / flatness;
4. QP-scaled thresholds.

Conceptual quantities:

```text
D  = abs(q0 - p0)
LP = local activity on P side
LQ = local activity on Q side
R  = local max - local min
Q  = selected boundary quantiser
S  = global experimental strength
```

The candidate should prefer corrections where the boundary step looks block-like relative to local
same-side activity and reject obviously strong natural edges.

No MPEG-4/H.264 threshold table is adopted blindly.

### 8.3 Candidate correction

Start with a bounded local correction primarily modifying `p0` and `q0`, optionally with smaller
`p1` / `q1` participation in sufficiently flat regions.

Requirements:

- clipping to valid sample range;
- bounded correction magnitude;
- near-zero-sum local correction where practical;
- no support across another known transform seam.

### 8.4 Full-data procedure assessment, candidate development and freeze (v0.7)

The old rule (even LP GOPs tune K0, odd LP GOPs test QP) is replaced. Preserve
even/odd native GOP reports as **in-sample stability diagnostics**, not independent evaluation.
Never move a frame into another recording's GOP structure.

**Eight-source assessment:** four independent content groups (XP, SP, LP, 3A), each an original
and its blocky re-encode. For each group in turn, leave **the whole group** out; on the other
three complete groups, screen M/F/R/T/P/K options, choose a small declared shortlist and
tune within fixed, reproducible budgets; evaluate the untouched fourth group. Refit the
procedure from scratch per fold. No fold's held-out metrics may influence its fit.

Comparison arms share candidate families, budget and fold partition:

- originals-only fitting on the three training originals;
- blocky-only fitting on the three training re-encodes;
- joint fitting on all six training recordings (PRIMARY procedure);
- optional LP-original-only and LP-pair historical arms, evaluable on held-out XP, SP and
  3A groups only; the held-out LP fold has no LP training observations and is **N/A**,
  not secretly trained from held-out content.

For **any numerical comparison involving historical L or LB**, restrict **every
arm in that comparison** to the identical held-out XP, SP and 3A groups and
the same predeclared weighting. Do not compare an all-four-fold J/O/X score
against a three-fold L/LB score. J/O/X's separate full-four-fold analysis
remains available but is not the L/LB comparison.

**Predeclared balancing:** each content group contributes the same total weight. In the joint
arm, each group's original contributes 2/3 and `_blocky` 1/3 within that group. Raw source
statistics remain visible. The same evaluation weights apply in each held-out group;
per-seam counts are not pooled directly across groups to select a winner. The choice of 2:1
is an engineering prior favouring real recorder content, not a fitted numerical result.
If significant trade-offs arise, disclose the Pareto frontier and let the owner arbitrate
instead of retroactively changing weights.

**Selection sequence:** predeclare quality/no-harm rubric and budgets, make the four-fold
candidate-procedure comparison (including per-group failures), select procedure/options
without seeing protected EP/2A/4A material, then fit the final **joint K0 on all eight**
quality-eligible source populations using the selected procedure, exactly as the owner
requested. Freeze code hash, metadata, options, thresholds, manual strength and run inputs.
Originals-only and blocky-only final fits on their full four-source populations are frozen
comparison kernels, not silently substituted for joint K0. If the joint result is
unacceptable while a comparator succeeds, report that as a design decision requiring
explicit owner approval; do not force an unsatisfactory K0.

**Uncertainty:** four content groups mean only four truly independent content-group
held-out results. Report all four, plus within-group frame/GOP dispersion; no inferential
p-values, no claim of independent frame-level observations. Paired-content leakage is
prevented by keeping both encodes in one fold. Full-data final fits are in-sample on all
eight; the fold's held-out evaluations are out-of-training-*content* for the procedure
run within that fold, not for the final eight-source K0. Selecting the winning procedure using these
cross-validation results makes its reported CV score subject to selection
optimism; these runs **rank procedures**, not provide an unbiased estimate of
the selected final K0. S2-I8, after the final candidate freeze, supplies the
first independent protected-content estimate. EP/2A/4A remain locked until
S2-I8.

**S2-I3 scope boundary:** all screening, candidate fitting and comparison
filtering in S2-I3 use **fixed per-clip QP only**, determined as each source's
all-MB median; no actual per-MB-QP branch or ablation is run until separately
authorised S2-I4. The existing all-MB medians are not re-fitted on folds.

**S2-I4 linkage:** K0 is frozen for a direct fixed-QP vs real indexed-QP input swap;
the complementary symmetric optimisation comparison is separately labelled and never
misrepresented as a frozen-parameter QP swap. Section 19 defines their authorisation
and ordering. B0 remains the sole initial metadata policy; B1 requires a new owner decision.

---

## 9. QP handling

### 9.1 Fixed-QP control

For the fixed-versus-real QP comparison:

```text
Q_fixed(clip) = median of all effective per-MB QP entries in that clip's full index
```

The population includes FRAME, FIELD and NONE macroblocks (including leading-B frames for
this descriptive fixed control), with the clip-wide median locked before any filtering
results are seen. Leading B pictures are still excluded from quality evidence per section 4;
the full-index fixed-QP definition is not silently recalculated on quality-eligible frames,
per-GOP folds, coded-only states or after seeing outcomes.

Known verified examples:

```text
XP original = 14      SP original = 16
LP original = 18      3A original = 14
all eight-pool `_blocky` recordings = 62
EP original = 14 (HOLD-OUT METADATA ONLY)      MLS original = 10 (CONTROL METADATA ONLY)
```

Use that one scalar for every MB in the clip. All-MB and coded-only medians differ for
LP (18 vs 16); coded-only 16 MUST NOT replace Q_fixed. New source distributions are
reverified from the owner's authoritative index before trials, and any disagreement
requires resolution rather than silently re-estimating from chosen subsets.

### 9.2 Real-QP variant

Use the effective per-macroblock QP from the validated Stage 1 index.

For a `NONE` macroblock, interpret that value carefully:

> the indexed QP is the quantiser scale in force at that point in the slice, but the NONE
> macroblock has no coded residual, so that QP did not quantise any residual samples in that
> macroblock.

The decoded pixels in a NONE macroblock come from prediction and therefore reflect whatever
quantisation history exists in the reference pictures rather than a residual quantised by the
current macroblock's indexed QP.

Consequences for Stage 2:

- a shared boundary touching NONE may include a QP value that does not directly describe the
  pixels on that side;
- the fixed-QP versus real-QP comparison must report boundaries touching NONE separately;
- whether a different boundary-QP rule is useful for NONE is an evidence question under Step 5,
  not a pre-emptive design change.

### 9.3 Shared macroblock boundaries

For a boundary shared by two macroblocks, the first implementation hypothesis is:

```text
Q_boundary = rounded mean(Q_left, Q_right)
```

An internal seam uses the containing macroblock's QP.

For a boundary touching a NONE macroblock, this rounded mean is still used initially for the
controlled experiment, but the result must be reported separately because the NONE-side QP did
not quantise a residual in that macroblock.

This is a Stage 2 hypothesis, not repository knowledge.

Large cross-boundary QP disparities must be reported separately. LP includes cases such as:

```text
Q_left = 112
Q_right = 14
rounded mean = 63
```

Report the population and behaviour of such high-disparity shared boundaries so an apparently
moderate mean QP does not hide a severely quantised neighbour.

If results show sensitivity to this choice, compare a small bounded set such as min / mean / max
rather than silently changing the rule.

### 9.4 QP saturation reporting

LP and EP contain macroblocks at effective QP 112.

Report QP-112 behaviour separately where practical so saturation does not disappear inside whole-
clip averages.

---

## 10. Revised Stage 2 experiment ladder

### Step 1 - unfiltered baseline

No filtering.

Purpose:

- mandatory visual baseline;
- diagnostic baseline;
- paired-reference baseline where a practical reference exists.

### Step 2 - indexed geometry + fixed clip-wide QP

Use validated indexed geometry, fixed clip-wide QP as section 9.1, and the selected
short-support, edge-protected candidate K0. S2-I3 selects the final joint K0 via full
multi-source development with grouped procedure assessment (section 8.4). Record complete
per-source original and blocky outcomes, with source-balanced diagnostics.

### Step 3 - indexed geometry + real per-MB QP

S2-I4 addresses two separate estimands on the real originals:

- **Frozen switch:** with K0, geometry, pixels, strength, thresholds and every non-QP
  parameter unchanged, replace the clip median by each actual indexed effective MB QP.
  Paired same-frame/same-seam differences isolate the QP-map input's effect for K0.
- **Symmetric tuned comparison:** develop a fixed-QP branch and a real-QP branch with
  equal search budgets in the same content-group folds and compare their held-out-group
  metrics. Distinct fitted parameter sets are declared openly; this answers which
  approach achieves better quality with fair calibration, NOT the same frozen-kernel
  question. No protected hold-out content participates.

Real-QP information comes from originals, not QP-62 constant re-encodes. Report NONE-touching
edges and QP saturation populations separately. Do not interpret either comparison as a
pristine independent population estimate from the final all-eight K0.

### Step 4 - luma kernel / threshold / strength development

S2-I5 continues only **after** S2-I4 has reported both QP comparisons. It may refine
edge/activity rejection, correction magnitude, bounded strength sweep and no-harm treatment
using the full eight-source development population and real indexed QP. New versions and
new fitting rounds must be identified separately; never retroactively redefine S2-I3 K0
or S2-I4 results. Preserve OFF bit-exact and no-cross-seam support invariants.

No S2-I5 change may touch EP/2A/4A hold-out content before S2-I8.

### Step 5 - `NONE` policy

Start with:

**N0 - conservative**

```text
NONE has no internal transform seam in either orientation:
    no internal vertical x = 8 seam
    no internal horizontal mid-height seam
```

Only the NONE macroblock's **outer macroblock-edge locations** remain eligible coding-grid
locations and may still be tested by the pixel-domain blocking/detail logic.

Only if N0 leaves a demonstrated problem should a bounded alternative be designed.

Any alternative must remain index-consistent and must not recreate a general FRAME/FIELD pixel
detector by another name.

### Step 6 - bounded chroma experiment

Use native Cb/Cr planes and fixed 8x8 chroma geometry.

Initial QP comparison:

```text
C0  unfiltered chroma
C1  chroma candidate + fixed clip-wide median QP
C2  same candidate + real indexed per-MB QP
```

For interlaced material, explicitly investigate the horizontal sample-access rule required by
O-06/O-14.

Leading candidate:

```text
same-field-polarity horizontal access
```

because V4 verifies the chroma parity premise and D-09 requires avoiding field mixing where
applicable.

However, same-field chroma filtering remains an experimental design choice until Stage 2 evidence
is reviewed.

For progressive MLS:

```text
progressive_frame = 1
    -> normal frame-domain access
```

Do not use luma FRAME/FIELD/NONE state to place chroma seams.

### Step 7 - locked generalisation / no-harm

Only after the full final luma/chroma candidate is frozen, perform S2-I8 first-contact
filter assessment on EP, 2A, 4A originals **and their `_blocky` re-encodes**, with
no prior tuning on any member of those content groups. MLS and MLS_blocky are
separate frame/format/no-harm controls. Report the owner-requested complete
16-recording census with roles clearly labelled. Record all failures; no hidden
revisions after seeing a hold-out, and no call to those clips in S2-I3/S2-I4/S2-I5.

---

## 11. Progressive versus interlaced access

Take `progressive_frame` per picture from the index.

### `progressive_frame = 1`

Use ordinary frame-domain sample access.

### `progressive_frame = 0`

Use parity-aware sample access where filtering across the selected seam would otherwise mix fields.

Do not infer progressive/interlaced handling from:

- filename;
- vertical resolution;
- container metadata alone.

Field pictures remain outside the current Stage 2 filtering path.

---

## 12. Strength handling

The intended eventual user interface exposes one global strength.

Stage 2 uses a small declared sweep such as:

```text
OFF
LOW
NOMINAL
HIGH
```

or equivalent numeric values.

Requirements:

- OFF is bit-exact input;
- stronger settings must monotonically permit more correction / looser thresholds;
- compared variants use the same strength definition;
- do not independently retune strength merely to make one variant win.

The exact production scale remains open.

---

## 13. Measurements and evidence

No single metric decides the project.

### 13.1 Source-separated seam diagnostics

At known eligible seams, report before/after quantities such as:

```text
boundary step magnitude
same-side local activity
step / activity relationship
applied correction magnitude
percentage of eligible seams changed
```

Break down where useful by:

```text
seam class
FRAME / FIELD / NONE
boundary touches NONE: yes / no
I / P / B
QP band
strength
```

The `boundary touches NONE` split is mandatory for the Step 2 versus Step 3 QP-map comparison.

These are diagnostics, not absolute perceptual-quality scores.

### 13.2 No-harm / collateral-change measures

Report:

```text
mean absolute output-input change
percentage of changed pixels
change energy away from eligible seam neighbourhoods
changes around strong natural edges
```

A filter that improves seam statistics by broadly blurring non-seam content should fail.

### 13.3 Paired-reference metrics

For each of the four development original/re-encode pairs (XP, SP, LP, 3A), once
cross-file frame correspondence is proven under section 15:

- luma MAE, MSE, PSNR;
- seam-local reference error;
- non-seam reference error;
- separate FRAME/FIELD/NONE and I/P/B breakdown where the statistic is meaningful.

Interpretation is **movement toward/away from the decoded higher-quality original**,
not restoration truth or proof of perceived quality. Record failures of pairing proof
and disable paired metrics for that source without fabricating alignment. Both paired
encodes stay in the same grouped cross-validation fold to prevent content leakage.

Software `_blocky` encodes have QP 62 in every MB: the fixed and real QP inputs are
therefore identical there, so they cannot establish spatial QP-map benefit. Only
originals (XP/SP/LP/3A) provide a meaningful QP-variation experiment. EP/2A/4A pairs
remain locked until S2-I8. MLS pair is a separate control.

### 13.4 I/P/B reporting

Report practical results separately for:

- I pictures;
- P pictures;
- B pictures;
- all included pictures.

This tests the practical limit from prediction-propagated / off-grid blocking.

### 13.5 QP-band reporting

Use declared QP bands sufficient to reveal whether behaviour changes materially with quantisation.

At minimum identify the QP-112 saturation population separately where present.

### 13.6 Visual evidence

Produce matched crops or lossless clips for the project owner.

Include:

- flat/blocky regions;
- strong genuine edges;
- texture/detail;
- FRAME-heavy regions;
- FIELD-heavy regions;
- NONE-heavy regions;
- I/P/B examples;
- representative low/mid/high QP regions;
- chroma-rich areas for chroma testing.

Blind or shuffled A/B presentation is preferred where practical.

---

## 14. Frame / region selection

Do not rely only on favourable hand-picked examples.

### 14.1 Full included-frame reporting

Run aggregate diagnostics across all quality-eligible frames after applying the leading-B exclusion.

### 14.2 Deterministic diagnostic subset

Before viewing filtered results where practical, select a reproducible subset based on metadata,
for example:

- highest mean-QP frames;
- lower-QP comparison frames;
- highest FRAME proportion;
- highest FIELD proportion;
- highest NONE proportion;
- representative I/P/B frames.

### 14.3 Manual additions

The project owner may add visually troublesome frames.

Label them as manually selected rather than statistical samples.

---

## 15. Cross-pair temporal correspondence for secondary reference metrics

Stage 1 proves index-record correspondence inside each file.

Before using an original/blocky pair for paired-reference metrics, also verify that decoded frame
`N` in one corresponds to decoded frame `N` in the other.

For each frame, compare against a small temporal window, e.g.:

```text
N-2 .. N+2
```

using luma MAE or MSE.

Expected:

```text
best match at N
```

for all or effectively all non-ambiguous frames.

Very static ties may be reported rather than treated as failures.

This check applies only to software-transcode pairs, including all four development original/blocky pairs.

---

## 16. Quantisation matrices

Current evidence shows custom non-intra matrices in four of the five real LG recordings examined.

The first Stage 2 filter does **not** consume matrix coefficients.

Record matrix-presence provenance with results.

Reopen Stage 1 for matrix values only if there is a concrete unresolved pattern such as:

```text
QP-normalised threshold behaviour differs consistently
between custom-matrix and no-custom-matrix LG material
```

and simpler explanations have been excluded.

Do not unfreeze Stage 1 pre-emptively.

---

## 17. FFmpeg / BestSource QP side data

FFmpeg per-macroblock QP side data remains an optional implementation cross-check, not an
architecture decision.

Core Stage 2 filtering uses the validated Stage 1 index.

If the BestSource/VapourSynth path later exposes FFmpeg QP side data cleanly, it may be compared
against Stage 1 QP as a cross-check.

This must not block Stage 2.

---

## 18. Feasibility gate

Stage 2 ends with an explicit gate report.

### 18.1 Primary evidence

Primary product evidence includes real-original visual quality and detail protection,
real-source seam-local behaviour, source-balanced no-harm/collateral-change
measurements, the four development content groups' cross-validated transfer,
and finally consistency across the independently locked EP/2A/4A content groups.
The additional full-data fits' own measurements are engineering **in-sample**
diagnostics, not independent generalisation estimates.

### 18.2 Secondary evidence

Secondary evidence includes verified original/re-encode paired-reference movement,
frame/GOP-type and QP-band diagnostics, and the separate MLS controls.
All `_blocky` clips are software transcodes with QP 62 everywhere; their
fixed-QP and indexed-QP inputs are identical. Claims about value of a spatial
real-QP map require the original XP/SP/LP/3A recordings with QP variation,
then independent protected material when S2-I8 becomes authorised.

### 18.3 Pass / fail interpretation

Do not invent one arbitrary PSNR or seam-step threshold in advance.

A positive result requires:

- visible blocking reduction on target material;
- corrections localised appropriately;
- acceptable preservation of real edges and texture;
- acceptable chroma behaviour;
- no unacceptable field mixing or colour smearing;
- reasonable consistency across hold-outs.

The project may fail the gate even if some numerical seam measures improve.

### 18.4 Final metadata-retention output

The gate report should explicitly list:

```text
metadata definitely consumed by the successful filter
metadata used only for diagnostics
metadata shown unnecessary
metadata still unresolved
```

That evidence feeds Stage 3 and the final index specification.

---

## 19. Implementation increments

**Ratified v0.7 order (2026-10-17), NOT implementation authorisation.** Stage 1 remains FROZEN.
S2-I1 and S2-I2 are COMPLETE / accepted / pushed; v0.7 supersedes Stage 2 v0.6.
S2-I3 has design-only authority; independent authorisation
is required for code and filtered runs and for every later increment.

```text
S2-I1 [COMPLETE]
    read-only Stage 1 index reader and validation, leading-B accounting

S2-I2 [COMPLETE]
    spatial registration diagnostics, LP and LP_blocky, gate report installed

S2-I3 [DESIGN ONLY NOW]
    Windows BestSource structural + exact P-skip admission (section 6.3)
      on all eight; failed/inconclusive sources BLOCK quality runs
    characterise all eight using all quality-eligible frames
    compare procedures by leave-one-CONTENT-group-out CV over XP/SP/LP/3A pairs
    originals-only vs blocky-only vs balanced joint fitting, same search budget
    choose procedure using predeclared rubric; fit final joint K0 on ALL EIGHT;
      freeze one exact kernel/parameters, preserve comparator identities
    native even/odd GOPs for descriptive IN-SAMPLE stability only
    FIXED QP ONLY: no real-QP fitting, comparison runs or conclusions
    no viewing EP/2A/4A content or their blocky versions

S2-I4 [NOT AUTHORISED]
    two expressly different fixed-vs-real QP evaluations on originals:
      frozen-K0 QP-only input switch; symmetric retrained/calibrated comparison
      with matched content-folds and budgets
    NONE-touching boundaries separate; QP-112 saturation reported

S2-I5 [NOT AUTHORISED]
    further full-development-pool real-QP luma kernel/threshold/strength refinement
    new kernel revisions tracked separately from frozen S2-I3/S2-I4 results

S2-I6 [NOT AUTHORISED]
    NONE N0 policy and only evidence-driven alternatives

S2-I7 [NOT AUTHORISED]
    bounded native 4:2:0 chroma experiment; progressive/interlaced access

S2-I8 [NOT AUTHORISED]
    LOCKED external-content generalisation/no-harm, frozen final candidate only:
      EP, 2A, 4A originals plus their paired `_blocky` re-encodes;
      MLS + MLS_blocky as separate controls
    owner's requested ALL-16-RECORDING census with source-by-source metrics,
      with developer/hold-out/control labels and no silent refitting

S2-I9 [NOT AUTHORISED]
    final additional paired-reference/secondary analyses (including protected pairs
      after S2-I8's first-contact gate), no tuning on hold-out data

S2-I10 [NOT AUTHORISED]
    feasibility, limits and metadata-retention gate report
```

Keep every recorded historical negative/control measurement; a bad result is not license
to change sample roles after viewing it. S2-I8's first-contact hold-out evaluation
follows the final S2-I5/S2-I7 candidate freeze; it must not occur prematurely simply
because the S2-I3 K0 was frozen. Only the project owner may ratify Stage 2 v0.7 and
separately authorise implementation or future stages.

---

## 20. Explicit non-goals

Stage 2 does not:

- freeze final `.idx2` packing;
- optimise index size;
- build the final production indexer;
- build the production C++ VapourSynth API4 plugin;
- implement AVX2;
- solve field-picture filtering;
- solve damaged-stream production support;
- add motion vectors;
- add CBP or coefficient activity unless evidence later demands them;
- capture quantisation-matrix coefficient values without evidence;
- build a pixel seam-position detector;
- build Family B;
- run an existing-filter yardstick as part of the planned experiment;
- reopen the production architecture question decided by D-24.

Family C remains optional later research under D-12, but is not part of the core Stage 2 experiment and
must not delay the feasibility gate.

---

## 21. Historical v0.4 review scope (superseded by v0.7 section 3)

**HISTORICAL ONLY - NOT OPERATIVE SOURCE ASSIGNMENTS.** The following
paragraph and numbered points describe the v0.4 review snapshot. The sample
roles in ratified v0.7 section 3 replace those historical assignments.

The prior v0.3 design questions were reviewed by Claude, which gave NO OBJECTION, and the project owner ratified
v0.3 on 2026-10-08. They are no longer open review questions.

Claude's cold review of this v0.4 candidate should be limited to whether the post-ratification
knowledge has been incorporated faithfully without changing the algorithmic design:

1. v0.3's ratified status and the continuing no-code / separate-restart guard are stated correctly;
2. the LG quality ladder is distinguished from Stage 2 experimental roles;
3. LP, EP, 4A, 2A and MLS roles remain exactly as ratified;
4. XP, SP, 3A and their `_blocky` copies remain unassigned/spare and no properties are inferred;
5. the 64-bit Python/native-helper constraint is consistent with the accepted x64 environment;
6. the six accepted `.idx` files are correctly identified as immutable regression baselines;
7. derived-media handling correctly defers to the repository `NOTICE.md` / `README.md` policy;
8. no text in v0.4 accidentally authorises S2-I1 or any other technical development.

---

## 22. Current post-reconciliation disposition

The history recorded in v0.6 remains binding history; its earlier time-specific
technical-restart statement is no longer the current operating status. At the
`6e7b5c53...` baseline Stage 1 is frozen, S2-I1 is complete, and S2-I2 is fully
closed, with nine code files and the S2-I2 gate report/evidence installed. Ratified v0.7 responds to the owner's explicit **S2-I3 design-only** instruction
and Claude's subsequent independent review. It supersedes v0.6 at installation;
ratification of this design does NOT grant S2-I3 implementation or filtering authority.

---

## 23. Change log

### v0.7 - 2026-10-17 (RATIFIED)

- Replaces LP-only even/odd kernel selection with full eight-source development,
  four whole-content-group leave-one-out comparisons and exact source balancing.
- Assigns XP/SP/LP/3A pairs to development, while reserving EP/2A/4A and their
  blocky encodes for locked S2-I8; MLS pair is a separate control.
- Replaces dimension-equality assumption with authoritative per-index geometry;
  admits development sources through hard structural and standard-exact P-skip
  identity (Windows BestSource), retaining unmodified S2-I2 metrics as diagnostics;
  adds symmetric S2-I4 QP tuning alongside frozen-K0 QP-only switch.
- Updates 3, 6.3, 8.4, 9.1, 10, 13.3, 19 and status. Carries the
  owner-requested all-16-source S2-I8 census, explicitly still unexecuted.
- Preserves immutable Stage 1 indexes and all existing technical/media rules;
  records owner approval to track seven separately-labelled non-baseline
  development indexes; requires Windows verification and separate installation.
- Clarifies the historical-only section 21, full-vs-three-fold comparisons,
  CV selection optimism, S2-I3 fixed-QP-only scope and MLS/hold-out metadata.
  This ratified design revision grants no S2-I3 code authorisation.

### v0.6 - 2026-10-13 (RATIFIED)

- Synchronizes Stage 2 with the project owner's later narrow ChatGPT/Claude AI Restricted Media authorisation and
  defines Development Closure as the project owner's declaration that active development is finished.
- Records that Restricted Media cleanup/history purge occurs at Development Closure and that the
  project/repository may continue afterward as an ongoing maintenance project.
- Replaces the absolute "same reviewed change" media-sync wording with "same coordinated,
  owner-ratified change", preserving the project owner's authority to waive further review explicitly.
- Lists `LG_576i_3_LP_blocky`, `LG_576i_4_EP_blocky` and `LG_576i_5_MLS_blocky` as
  unassigned/spare exactly as the project owner ruled; the originals keep their existing roles.
- Clarifies ordinary CSV/tabular numerical/text diagnostics versus picture-like text grids according
  to content/function rather than extension.
- Plans generation/validation of the currently untracked/absent `TEST_4A_A003_blocky.idx` inside
  S2-I1 without promoting it to a seventh immutable baseline.
- Tidies authority/version wording under the project owner's "named version or later" rule and updates the
  post-reconciliation disposition.
- Changes no deblocking algorithm, no existing assigned material role, no six-baseline identity and
  no S2-I1-through-S2-I10 increment order. Technical restart remains NOT AUTHORISED.

### v0.5 - 2026-10-12 (RATIFIED)

- Ratified directly by the project owner after he elected to close further review and apply the coordinated
  Restricted Media policy.
- Aligns section 3.6 with the coordinated `NOTICE.md` / `README.md` policy without changing any
  Stage 2 algorithm, sample role, immutable-index rule, implementation sequence or
  technical-restart status.
- Anchors the policy to expressly designated Source Recordings rather than generic media file type.
- Keeps the project owner's option (a): visualisations derived from Source Recording metadata/measurements remain
  Derived Media / Restricted Media.
- Distinguishes non-media `.idx`/hash/log/metadata/numerical-text diagnostics from visual/audible
  Derived Media.
- Allows bounded active-development repository evidence/review but removes any separate private
  reviewer/service transmission exception.
- Requires prompt deletion of other copies after use and project-finalisation removal of all
  Restricted Media from the current tree, followed by the separately planned history purge so the
  repository becomes and remains media-free afterward.
- Treats documents that embed Restricted Media as Restricted Media until a media-free/redacted
  version is produced.

### v0.4 - 2026-10-11 (RATIFIED)

- Claude delta recheck: NO OBJECTION; the project owner ratified v0.4 on 2026-10-11.
- Revised after Claude's 2026-10-11 authority/status review: restates the full derived-media
  discipline in section 3.6, with `NOTICE.md` governing on conflict and the pre-widening
  prohibition retained.

- Corrects the document status: v0.3 was ratified by the project owner on 2026-10-08 after Claude's no-objection
  review; no Stage 2 code has started.
- Records the LG recorder quality order `XP -> SP -> LP -> EP -> MLS` while explicitly separating
  recorder quality from experimental role.
- Preserves LP as primary development/tuning material, EP/4A/2A as locked interlaced hold-outs, and
  MLS as progressive/control material.
- Records XP, SP, 3A and their `_blocky` copies as present but unassigned/spare; no technical
  properties or future role may be inferred without explicit analysis and assignment.
- Adds the 64-bit Python/native-helper binding constraint for the Stage 2 prototype environment.
- Identifies the six tracked accepted Stage 1 `.idx` files as immutable regression baselines.
- Records derived-media handling as subordinate to the repository `NOTICE.md` / `README.md` policy.
- Replaces stale pre-ratification review/disposition language with the current post-migration
  knowledge-update review and separate technical-restart guard.
- Makes no change to the S2-I1 through S2-I10 implementation sequence or algorithmic experiment design.

### v0.3 - 2026-10-08

- Revised after `Claude_REVIEW_OF_ChatGPT_Stage2_Experiment_Design_v0_2_Revised_v0_1.md`, which
  gave NO OBJECTION to ratification and confirmed all prior MUST/SHOULD corrections.
- Defined a Stage 2 GOP operationally as the display-order run from one I picture up to but not
  including the next I picture, numbered from 0 at the first I picture.
- Made the LP K0 split explicit: even-numbered usable GOPs tune K0; odd-numbered usable GOPs perform
  the fixed-QP versus real-QP comparison.
- Clarified indexed QP semantics for NONE macroblocks: the QP is the quantiser in force but did not
  quantise any residual in that macroblock.
- Required Step 2 versus Step 3 reporting to split boundaries that touch NONE from boundaries that
  do not.
- Kept rounded-mean shared-boundary QP as the initial controlled hypothesis while flagging NONE-side
  interpretation as an evidence question for Step 5.
- Added awareness that an 8-pixel horizontal misregistration can preserve the grid-phase signal;
  absence of a clear zero-shift contrast maximum remains a stop condition.
- Version bumped to v0.3 so the earlier and revised v0.2 texts can be archived distinctly.
- No Stage 2 code is authorised by this draft.

### v0.2 - 2026-10-08

- Revised after `Claude_REVIEW_OF_ChatGPT_Stage2_Experiment_Design_v0_2.md`.
- Corrected NONE geometry: NONE has no internal vertical or horizontal transform seam; only outer
  macroblock-edge locations remain eligible.
- Strengthened spatial registration validation with shifted-index-label controls in x/y and an
  8-pixel column grid-phase test.
- Split LP deterministically by GOP parity so K0 is tuned on one subset and the fixed-QP versus
  real-QP comparison is performed on the other.
- Required the Stage 2 index reader to reproduce analyzer v0.2 record/state/QP summary totals.
- Stated explicitly that QP-62-everywhere `_blocky` transcodes cannot test the value of the spatial
  QP map.
- Required separate reporting of high-disparity shared-boundary QP cases such as 112 next to 14.

- Supersedes the experimental premise of v0.1 after ratified D-24.
- Removes Family B, pixel seam-position detection, Step 2b, transform-state-value architecture
  comparisons and custom-index justification testing.
- Incorporates D-25: chroma deblocking is in scope on mechanism; Stage 2 tests how to do it safely,
  not whether chroma is eligible for scope.
- Incorporates D-26: real LG recorder material is primary evidence; software-transcode pairs are
  secondary paired-reference evidence.
- Uses LP for development; EP, 4A original and 2A original as locked interlaced hold-outs; MLS as
  progressive/control material.
- Uses per-clip median effective QP as the fixed-QP control.
- Adds mandatory detector-free spatial index-to-pixel registration validation.
- Adds leading-B quality-evidence exclusion before the first I picture.
- Uses `progressive_frame` per picture to select progressive frame-domain versus interlaced
  parity-aware access.
- Carries Claude V1-V4 evidence distinctions into luma/chroma geometry and access design.
- Keeps same-field chroma filtering experimental rather than promoting it to VERIFIED.
- Defers quantisation-matrix coefficient capture unless Stage 2 evidence requires it.
- Explicitly excludes an existing-filter yardstick from the planned experiment.
- Defines S2-I1 through S2-I10 incremental implementation order.
- No Stage 2 code is authorised by this draft.

### v0.1 - 2026-10-07

- Original pre-D-24 Stage 2 draft.
- Retained here only as superseded design history after v0.2 is ratified.
