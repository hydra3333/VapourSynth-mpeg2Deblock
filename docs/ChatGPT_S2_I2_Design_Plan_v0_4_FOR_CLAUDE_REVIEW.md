# S2-I2 - Spatial Index-to-Pixel Registration and Seam-Map Diagnostics

**Filename:** `ChatGPT_S2_I2_Design_Plan_v0_4_FOR_CLAUDE_REVIEW.md`  
**Version:** 0.4  
**Date:** 2026-10-15  
**Author/role:** ChatGPT, implementation drafter  
**Status:** DRAFT FOR CLAUDE INDEPENDENT REVIEW; NOT RATIFIED; NO CODE AUTHORISED BY THIS DRAFT  
**Scope:** S2-I2 design only. This does not authorise S2-I3.  
**Repository context:** Claude verified S2-I1 content at commit `4221f7f9f3c015da4ca70b4f8c0249536cd7e3b5`; the ratified Project Status v0.5 installation was subsequently committed and pushed at `2286341` (as reported in Claude's v0.3 review). These are **historical commit identities**, not an assertion of live current HEAD.

---

## 0. Intent, provenance and authority

The project owner said "ok lets go with then next please" after being told that the next step would be an S2-I2 **design plan**. Following delivery of v0.1, the owner explicitly approved **amending that plan to run S2-I2 diagnostics on BOTH `LG_576i_3_LP` and `LG_576i_3_LP_blocky`**, with the `_blocky` recording serving a separately qualified secondary diagnostic/control role. Version 0.2 made that amendment. Version 0.3 incorporated Claude's v0.2 review M1/S1-S4 and the owner's descriptive-pixel-report additions. This **v0.4** corrects Claude's v0.3-review M1 row-phase gate and addresses its S1-S3 implementation clarifications and O1 provenance/sign convention. It is not a command to execute scripts and not ratified technical authority.

**Authority/delta note:** Stage 2 v0.6 section 3.0 expressly lists `LP_blocky` as UNASSIGNED/SPARE and prohibits silently assigning it without analysis and owner disposition. The owner's new conversational decision is the narrow **S2-I2 diagnostic-role assignment** below, with an explicit identity and preflight gate; it does **not** revise the ratified original-LP primacy, hold-outs, software-pair roles or any filtering policy. Until propagated into a later ratified Stage 2 authority revision, preserve this distinction. Claude reviewed v0.2 and found no authority revision necessary before implementation: record the S2-I2-only assignment now and synchronize at the next real Stage 2/status revision. The new same-field row-phase test similarly serves the existing two-dimensional registration objective and is to be recorded at the next Stage 2 revision. Do not quietly rewrite v0.6.

Controlling authorities (named versions or later under D-23):

- `docs/REPOSITORY/Stage2_Experiment_Design_v0_6.md`, specifically sections 1.1-1.4, 3, 4, 5, 6.2, 11, 14 and 19;
- `docs/REPOSITORY/05_DECISIONS_v1_2.md`, particularly D-09, D-23, D-24 and D-26;
- `docs/REPOSITORY/06_DEBLOCK_CONCEPT.md` v1.2, particularly K-03, K-07 and frame-owned geometry;
- `docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md` v0.4, constraints C-1 to C-3 (final binary packing remains unfrozen);
- `docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md` (frozen Stage 1); and
- `NOTICE.md` (governing Restricted Media policy).

The ratified `00_PROJECT_STATUS_v0_5.md`, installed at `2286341`, supersedes the historical state in the archived handovers where relevant. The authority documents above, not this proposal or a handover, govern algorithm and methodology. This proposal adds implementation-specific measurement conventions explicitly identified as **proposed** below; it does not silently amend the v0.6 requirements.

### 0.1 Scope and provenance of this revision

Inputs newly incorporated, all supplied by the project owner:

- `Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_2_v0_1.md`, Claude's review: **M1 MUST** (same-field row-phase test), **S1-S4 SHOULD** (fixed gate thresholds, normalised D, deliberately known-bad controls and `LP_blocky` identity, correct Python/NumPy preflight), plus O1/O2 optional observations;
- `Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_3_v0_1.md`, Claude's review: **M1 MUST** (lower row-phase tie-guard margin to 5% with fixed 16-pixel interior and per-frame consistency), **S1-S3 SHOULD** (exact horizontal comparator pairs; `vspipe`-executed Python/NumPy preflight; VapourSynth-independent NumPy statistics engine and bounded-memory processing), and O1 (status commit and offset sign);
- the owner's clean additions to S2-I2: **descriptive** boundary-strength and seam-versus-control detectability statistics, LP and `LP_blocky`, optional additional diagnostic clips only on subsequent confirmation, all 16 recordings at S2-I8 after freeze, and future pixel-test principles for S2-I3..S2-I5;
- `Claude_REVIEW_OF_ChatGPT_Copilot_Grok_Block_Detection_Assessment_v0_1.md`, including the precise informal proxy definitions and limitations;
- `Claude_S2_Seam_Pixel_Test_Options_Table_v0_2.md`, retained **unchanged** as the future S2-I3/S2-I5 research-options inventory.

S2-I2 **may report pixel strength and detectability** but cannot select a detector, optimize thresholds, choose a filtering kernel, filter pixels, or promote surrogate seam/control classes to ground-truth visible-artifact labels. This v0.4 is **design only**; Claude reviews and the owner ratifies the approach before implementation. S2-I3 remains unauthorised.

### 0.2 Starting gate - already met

Owner-reported/Claude-verified S2-I1 Windows acceptance: six frozen-index regressions PASS, six BestSource/index correspondences PASS, 4A-blocky candidate generated and validated against all applicable Stage 1 report 8.1 rows, expected candidate SHA-256 `57f3b60d1ea2108f29f222c7c658cb1ddc9eb26c14071cb056112a2f3b296e73`; candidate remains non-baseline/uncommitted in `%TEMP%`. The five v0.2 files with the corrected logging BAT were committed as part of `4221f7f`. Stage 1 and the six accepted `.idx` baselines remain immutable.

S2-I2 must import/reuse the accepted independent reader `experiments/stage2/stage2_index_reader_v0_2.py` and its validation contract, not clone or weaken it. Its public interface includes `read_index(path)`, `Stage1Index.records`, `Stage1Index.quality_excluded(ordinal)`, `PictureRecord.macroblock(x,y)`, `PictureRecord.progressive_frame`, `PictureRecord.picture_type`, `PictureRecord.mb_width`, `PictureRecord.mb_height`, and `validate_clip_metadata(...)`.

## 1. Precisely bounded purpose

**Primary question:** With full-frame MPEG-2 decoded by BestSource, are the Stage 1 index macroblock transform labels and coded seam locations spatially aligned with the decoded *luma* pixels, including field parity?

Deliverables (numbers/CSV, no filtering):

1. Deterministic seam geometry: outside MB edges, FRAME/FIELD coded internal seam locations and explicit NONE absence, read only from the accepted index reader.
2. Original LP mandatory 3x3 FRAME-versus-FIELD shifted-label contrasts, **8-pixel column-phase**, and independent **same-field 8-row-phase** tests. Each has predeclared gates, frame consistency and deliberately misregistered known-bad controls.
3. Identical supported tests on the separately indexed/validated `LP_blocky` as **supplementary diagnostic/control**; a success cannot rescue an original LP FAIL or INCONCLUSIVE.
4. A separate **descriptive boundary-strength / pixel-detectability report for each clip**, in **both seam orientations**, comparing index-known coded seams with deliberately chosen non-seam controls. Use the two owner-specified metrics (plain and noise-robust), hit rate at a fixed 5% proxy false-alarm rate and AUC, with seam class/QP/picture-type strata, frame/GOP-level uncertainty and explicit denominator/limitation reporting. No data-dependent threshold or kernel tuning.
5. Separate numeric CSVs, manifests, explicit coverage/limitations, and per-clip dispositions. No required PNG or other media depiction.

Not in S2-I2: pixel-only seam localisation, deblocking, filter/kernel/threshold selection, denoising, QP ablation, chroma filtering, AVX2/plugin work, extra Stage 1 parsing or index changes, a comparison against an external deblocker, or use of locked hold-outs. The future options catalogue belongs to **S2-I3/S2-I5**, not to the present implementation.

### 1.1 Material and verified identities

**Mandatory primary:** `VHSC_samples/LG_576i_3_LP.mpg` with frozen tracked `.idx` SHA-256 `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011`. Expect 720x576, MB 45x36, 204 decoded/indexed output frames, leading B ordinals `[0,1]` structurally retained but **202** eligible for quality/registration/pixel statistics, subject to live preflight confirmation.

**Owner-approved secondary S2-I2-only:** `VHSC_samples/LG_576i_3_LP_blocky.mpg`, with its *own* scratch, non-baseline index. Claude's independently generated and characterised expected index is:

```text
SHA-256: b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238
frames / records: 204; 720x576; MB grid: 45x36; frame pictures: 204
progressive_frame: 0 on all 204
I/P/B: 19 / 50 / 135; first is I; leading B exclusions: 0
FRAME / FIELD / NONE: 54292 / 33853 / 242335
QP: 62 throughout, 330480 macroblocks
```

These are **expected preflight assertions**, not a seventh accepted `.idx` baseline. A Windows candidate differs? STOP that clip and investigate identity, demux, tool version and index bytes; do **not** overwrite an accepted baseline, normalize an unexpected result or change the expected hash to make a run pass. Revalidate with the frozen analyzer, independent reader and every-frame BestSource correspondence. The informal FFmpeg probe aligned correctly at zero; it does **not** substitute for formal BestSource validation or an owner-run gate.

**Other sample roles:** MLS, `TEST_2A_A001_blocky` and `TEST_4A_A003_blocky` are *optional only if the owner subsequently confirms*, with fresh source-specific preflight and role constraints. Do not add them to the v0.4 mandatory runner silently. Original EP, 2A, 4A hold-outs are **excluded until S2-I8**, as are hold-out-driven decisions. The owner wants one clean **all-16-recording census at S2-I8**, each with its own matching verified index, **after kernel and thresholds are frozen**. Record that *future* instruction, not a current S2-I2 run permission.

### 1.2 Distinct roles and gate disposition

| Topic | Original LP | LP_blocky |
| --- | --- | --- |
| Authority | **Mandatory primary** spatial-registration gate | **Supplementary** S2-I2-only diagnostic/control |
| Matching index | Frozen SHA-verified tracked LP index | Preflight-generated expected-hash-verified scratch index; untracked/non-baseline |
| 3x3 FRAME/FIELD | Mandatory | Mandatory when preflight and populations are adequate; current verified populations support it |
| Column + row phase | Mandatory independent tests | Run and report identically; secondary evidence only |
| Descriptive detectability | Mandatory proxy-labelled output | Mandatory proxy-labelled output; *not* image-quality ground truth |
| Outcome | FAIL/INCONCLUSIVE blocks S2-I2 primary gate | Cannot rescue LP; own failure/inconclusive reported, investigated separately |

Separate per-clip reports and separate denominator/threshold calibration. **No pooling across sources.** If LP passes and secondary fails, LP primary is still a pass but the secondary discrepancy must be explained and reported. If LP fails and secondary passes, the gate remains blocked. Unsupported/missing data is NOT APPLICABLE or INCONCLUSIVE, never fabricated as PASS.

## 2. Geometry contract - no filtering yet

Use decoded frame coordinates `(x,y)` with upper-left origin `(0,0)`; `x` increases right and `y` down. Macroblock `(mx,my)` covers nominal luma columns `16*mx .. 16*mx+15` and rows `16*my .. 16*my+15` for currently supported full-frame material. Index record N addresses decoded output frame N.

The **candidate locations** are determined by index coding geometry. A candidate is not a decision to actually filter and is not proof that a visible block artifact exists.

| Luma boundary type | FRAME | FIELD | NONE |
| --- | --- | --- | --- |
| Outer vertical MB edge at x multiple of 16 (inside frame) | Candidate | Candidate | Candidate |
| Internal vertical at local x=8 | Candidate | Candidate | **Absent** |
| Outer horizontal MB edge at y multiple of 16 (inside frame) | Candidate | Candidate | Candidate |
| Internal horizontal at local y=8 | Candidate, parity-aware for interlaced frame | **Absent** | **Absent** |

For outer boundaries touching two MBs, record **both neighbouring states**. These boundaries exist once per coordinate/span; they must not be generated twice. The production policy for filtering boundaries touching NONE remains OPEN (O-04) and is not being chosen here. Do not infer internal seams from the mere presence of a `dct_type` bit. No internal transform geometry exists for NONE.

**Interlaced FRAME horizontal seam measurement** (frame-owned, never merge fields): for macroblock row start `b=16*my`, evaluate absolute differences between `Y[b+6,x]` and `Y[b+8,x]` (even/top parity) and independently between `Y[b+7,x]` and `Y[b+9,x]` (odd/bottom parity). These are the v0.6 specified same-field samples around the nominal local seam 7|8. No filtering or sample mutation is involved. The FIELD-labelled population is measured at **the same pixel positions** as the FRAME population for the registration contrast; this is a control observation, not a claim of a FIELD mid-height transform seam.

For diagnostics on outer horizontal MB boundaries, any cross-boundary pixel measurement in interlaced frames also uses same-field neighbours, e.g. at boundary row `b`, rows `(b-2,b)` and `(b-1,b+1)` where in bounds. Actual seam objects can carry the nominal line coordinate and parity without representing individual sample pairs as extra seams. Vertical boundaries measure across adjacent columns within the same row; no field crossing occurs.

**Bounds:** skip frame-exterior edges. Validate every coordinate and source sample access. The original LP nominal dimensions divide by 16; apply the same full-frame geometry contract to `LP_blocky` **only after** its actual coded dimensions, macroblock grid and frame-picture support have been checked. Do not extrapolate to an unsupported partial-MB, field-picture or cropped/resized case. Refuse anything outside the reader and BestSource contract. Do not automatically crop, resize, shift or change pixel format to make an alignment test pass.

### 2.1 Proposed internal representation (not a production index change)

Each diagnostic seam is keyed unambiguously by frame ordinal, orientation, nominal boundary coordinate/span, seam class (`MB_OUTER`, `MB_INTERNAL`), applicable transform state(s) and optional field-parity measurement selector. Include `(mx,my)` ownership and exact source sample coordinates for audit. There should be no duplicate geometric keys. Only native luma plane Y is included in S2-I2; native 4:2:0 chroma filtering belongs to S2-I7. Numeric seam classes must retain source orientation, MB owners/states and parity, including both states at outer edges.

This is a Python diagnostic data model **only**, not a proposal to freeze `.idx2` binary packing or add fields to Stage 1.

## 3. Mandatory registration and descriptive pixel measurements

All registration tests use identical unmodified BestSource-decoded Y samples within each clip, validated ordinal alignment, supported full-frame pictures, explicit widened/signed subtraction and **frame-owned, parity-safe** sample access. Exclude leading-B quality ordinals but retain them for structural validation. Predeclare thresholds *before* reviewing formal Windows results; Claude already saw informal probe values, disclosed in the v0.2 review. Those values are feasibility information, not acceptance evidence.

### 3.1 Raw D and supporting content-normalised D_norm

For frame N and target MB `(mx,my)`, with `b=16*my` and each of its 16 luma columns x:

```text
S_even(x) = abs(Y[N,b+8,x] - Y[N,b+6,x])  # even field, 6|8
S_odd(x)  = abs(Y[N,b+9,x] - Y[N,b+7,x])  # odd field,  7|9
D_raw(N,mx,my) = mean of all 32 S_even and S_odd terms
```

Also compute the **descriptive content-normalised version**, with 16 columns and both parity samples:

```text
B_in(N,mx,my) = mean(abs differences on same-field pairs
                      2|4, 3|5, 10|12, 11|13)
D_norm = D_raw - B_in
```

Report raw `D_raw`, `B_in`, `D_norm`, field-specific component means and counts. **Gate on `D_raw`** to retain the original v0.2/v0.6 interpretation; `D_norm` is a corroborating and confounding diagnostic, not a newly tuned second pass gate. Avoid unsigned wrap. For FIELD/NONE-labelled target MBs the same midpoint sample rows provide an observational contrast, not a claim they have a coded FRAME mid-height seam.

### 3.2 Two-dimensional shifted-label contrast

Fix the common lattice `1 <= mx < mb_width-1`, `1 <= my < mb_height-1`; every shift sees the identical target D samples. Define for `(dx,dy)` in `{-1,0,+1} x {-1,0,+1}`:

```text
label_at_target(N,mx,my,dx,dy) = index_state[N,mx-dx,my-dy]
C(dx,dy) = mean(D_raw | shifted label FRAME) - mean(D_raw | shifted label FIELD)
```

Report all 9 results, label counts, even/odd component means, `C(0,0)-C(dx,dy)`, raw and normalised contrasts, frame-level shift winners and per-frame class-population eligibility. NONE-labelled targets are not artificially allocated to either contrast class.

**Predeclared formal gate, addressing Claude S1:**

- **PASS:** `C(0,0)` is positive and is the **strict maximum** across nine shifts; for each competing shift `C(0,0)-C(dx,dy) >= 0.10*C(0,0)`; and `(0,0)` wins in **at least two thirds** of frames in which both populations are present (report eligible-frame denominator and all ties). The 10% and 2/3 thresholds are proposals from Claude's review, disclosed as chosen after its informal probe; owner approval must precede the formal run.
- **FAIL:** a nonzero shift has a **strictly greater** aggregate C than `(0,0)`; include winner displacement and counts.
- **INCONCLUSIVE:** zero shift is the maximum but its margin, positivity, consistency or support is inadequate, or there is a tie. An INCONCLUSIVE primary test **blocks advancement** just as a FAIL does.
- **NOT APPLICABLE:** only for a genuinely unsupported secondary coding population, with reason/counts; never apply to valid original-LP input just to avoid a failure.

For `D_norm`, report corresponding 3x3 table for explanation without independently promoting it to a gate. A shifted test is a relative contrast, **not** a guarantee that every possible 4/8/16-pixel or parity offset will be caught.

### 3.3 Independent 8-pixel *column*-phase check

For vertical sample boundaries, take `E(N,x,y) = abs(Y[N,y,x]-Y[N,y,x-1])`, with x denoting the **right-side** column. Partition by `p=x mod 8`, phases 0..7, using the **fixed frame interior excluding a 16-pixel border on all sides** (the same declared coordinate convention as the row-phase test and known-bad controls), identical inclusion rules and explicit sample counts for every phase. Per-clip and per-frame results: means, counts, phase ranking, `(E_0-max(E_1..E_7))/E_0`, and frame-wise success fraction.

**Gate:** phase 0 is the unique largest aggregate mean and exceeds each other phase by **at least 10% of phase-0 mean**. Wrong unique peak = FAIL; tie, deficient support or smaller margin = INCONCLUSIVE. Known blind spot: an exactly 8/16-column shift preserves the phase; shifted labels must detect those controls. This test must not shift or reinterpret production seam positions.

### 3.4 Independent same-field 8-*row*-phase check (Claude v0.2 M1, corrected by v0.3 M1)

For each included frame N, sample on the **fixed interior region**: exclude a 16-pixel border at left, right, top and bottom of the decoded frame (coordinates `16 <= x < width-16`, `16 <= y < height-16`), as declared in the run manifest. Require both `(y,x)` and `(y+2,x)` to be valid, including for deliberate pixel offsets. The region is **fixed before the formal run**, identical between zero-offset and deliberately shifted tests, and not selected anew to improve either clip's outcome.

```text
F(N,x,y) = abs(Y[N,y+2,x] - Y[N,y,x])   # same-field only
q = y mod 8; q in 0..7
```

Count/average by q over the **complete eligible-frame set**, and separately per eligible frame. Under correct registration, **q=6 and q=7 are jointly the two highest aggregate phases** (same-field boundary pairs 6|8 and 7|9, including periodic repeats such as 14|16 and 15|17). Never substitute adjacent-field 7|8.

```text
R_expected_low = min(mean_F[q=6], mean_F[q=7])
R_other_high   = max(mean_F[q in {0,1,2,3,4,5}])
row_margin     = (R_expected_low - R_other_high) / R_expected_low
```

**Gate J (Claude v0.3 M1 correction):**

- **PASS** iff both q6 and q7 are the aggregate top two (order immaterial), `row_margin >= 0.05`, and q6/q7 are also the two highest in **at least two thirds of eligible frames**. Both the aggregate and eligible-frame denominators, phase counts/means and ties are reported. A frame counts toward the consistency numerator only if its top-two membership is unambiguous (a tie with an outside phase is not a win).
- **FAIL** if any phase other than q6/q7 ranks among the top two aggregate phases. This includes an outside phase tying for an aggregate top-two rank; report the tie explicitly.
- **INCONCLUSIVE** otherwise, including q6/q7 aggregate top-two with insufficient `row_margin`, inadequate frame consistency or insufficient/nonpositive support.

The row-phase margin is **5%**, not 10%: Claude independently observed an aligned original-LP margin of 11.5% on the 16-pixel interior, but 9.7% on a different central-half region; the margin is a tie/noise guard whereas ranks detect +1/+2 row offsets. Claude disclosed seeing these informal FFmpeg results before formal acceptance. The **3x3 and column-phase margins remain 10%** (and the unchanged 3x3 two-thirds rule). This adds a parity-sensitive test to fulfil ratified two-dimensional registration intent without altering Stage 2 v0.6 authority prematurely.

### 3.5 Mandatory deliberately known-bad registration controls (Claude S3)

After the aligned measurement, rerun **all three registration tests** on the *same frame set* with pixels displaced in memory relative to fixed index labels by:

```text
columns: +4, +8, +16
rows:    +1, +2, +8, +16
```

For all controls and the aligned run use a **common, predetermined 16-pixel frame-interior domain**, with only additional invariant sample-pair bounds where unavoidable; verify identical eligible frames, phase counts and comparable sample support. **Offset convention (must be written into the run manifest): pixels moved right/down by k, index unchanged.** Operationally, a positive displacement `(cx,ry)` evaluates source luma at `Y_original[N,y-ry,x-cx]` for each target `(x,y)`, and does not wrap or pad. Test the same target coordinates on every displacement; refuse any requested sample outside the original frame instead of fabricating borders or silently changing the sample populations. For **each** deliberate offset at least **one** independently evaluated test must return non-PASS (**FAIL or INCONCLUSIVE**). An offset that passes *all* tests is a defective registration test harness, and the formal run stops. Report a matrix with shift, 3x3 verdict, column-phase verdict, row-phase verdict, detecting test(s) and known individual blind spots; do not require every individual test to detect every displacement. Also run synthetic parity swaps, seam shifts, ties and unsupported input cases before the real evidence.

### 3.6 NEW descriptive boundary strength / pixel detectability (owner instruction)

**Diagnostic, not a registration gate or detector contest.** For *each* clip separately, sample known index-coded seam locations and declared non-seam controls on unmodified Y pixels. This asks whether **coded seams as a proxy class** separate from non-seam positions, **not** whether individual edges have been proved to be visible block artefacts.

**Both orientations:**

- **Vertical seam segments:** indexed outer MB vertical edges; internal x=16mx+8 for FRAME/FIELD (code-residual internal); do not invent an internal seam for NONE. For the standard non-seam control class use local `x mod 16 = 4,12`. Separately enumerate local internal x=8 inside NONE MBs as a *distinct* **no-coded-seam / possible propagated-blocking** class; never merge it into the standard controls or label it ground-truth unblocked.
- **Horizontal seam segments:** indexed outer MB horizontal edges and FRAME internal midpoint horizontal boundaries with **same-field** differences only. FIELD and NONE have **no** internal horizontal seam in the current coded geometry; report their mid-height positions separately as no-coded-seam classes if sampled. Use the exact same-field cross/comparator pairs in the table below, relative to MB top `b=16*my`, for all applicable seam and control classes. Never use adjacent-row 7|8 or mix fields.

**Fixed horizontal pair definitions (Claude v0.3 S1):** The first of each pair is the *upper* sample. Every pair must be in bounds and within one field parity; all comparator pairs must lie within one block and must **not cross the tested boundary**.

| Boundary class (nominal position) | Cross-boundary sample pairs | Same-field in-block comparators |
| --- | --- | --- |
| FRAME internal midpoint (7\|8) | `(b+6,b+8)`, `(b+7,b+9)` | above `(b+4,b+6)`, `(b+5,b+7)`; below `(b+8,b+10)`, `(b+9,b+11)` |
| Outer MB boundary (`b-1\|b`) | `(b-2,b)`, `(b-1,b+1)` | above `(b-4,b-2)`, `(b-3,b-1)`; below `(b,b+2)`, `(b+1,b+3)` |
| Standard control (3\|4) | `(b+2,b+4)`, `(b+3,b+5)` | above `(b+0,b+2)`, `(b+1,b+3)`; below `(b+4,b+6)`, `(b+5,b+7)` |
| Standard control (11\|12) | `(b+10,b+12)`, `(b+11,b+13)` | above `(b+8,b+10)`, `(b+9,b+11)`; below `(b+12,b+14)`, `(b+13,b+15)` |
| FIELD / NONE internal midpoint (7\|8), **no coded horizontal seam** | Same pairs as FRAME midpoint | Same comparators as FRAME midpoint; separate descriptive class only |

The (7|8) textual label denotes a nominal **boundary** in full-frame coordinates, not an instruction to subtract adjacent lines; even- and odd-parity differences use 6|8 and 7|9. At the outer boundary, use the `b` of the MB immediately *below* the edge. Exclude cases lacking the preceding MB or all required comparator pixels. For a horizontal segment, split its 16 columns into **two 8-column chunks**. Compute the robust statistic separately for **each parity in each chunk** and use an **equal-weight mean across the two parities x two chunks**, not a sample-count-weighted or cross-field signed average.

**Vertical transpose:** at each vertical seam or local control with its right-side column `x`, the cross pair for each sampled row is `(x-1,x)` (signed `right-left`). In-block comparators are `(x-3,x-2)` and `(x+1,x+2)` on the same sampled row. Compute per-field over the appropriate **8-row parity population** of its owning 16-row MB segment; average the two resulting parity scores equally. The vertical convention applies to MB outer, coded internal, x=4/12 controls and NONE x=8 separately, respecting the bounds on both sides.
- Record outer-edge neighbours' states, picture type, QP and coding-seam class; do not silently assign the class to one MB when two touch the seam. For a seam touching two differently coded MBs, report the class and paired metadata explicitly; determine any stratification convention *before* measurement. The descriptive report never changes which positions are the index-defined candidates.

**Two predeclared measures for every applicable segment, field-safe and in widened signed arithmetic:**

- **Plain (M2-like):** `mean(abs(signed cross steps)) - mean(abs(signed in-block comparator steps))`, evaluated using the fixed pairs above and matched segment populations. Use `lower-upper` for horizontal and `right-left` for vertical signed steps. Aggregate all applicable cross-pair observations and their above/below or left/right comparator observations within each segment; preserve negative scores rather than clipping.
- **Noise-robust (M4-like):** for each declared segment subpopulation (one field parity x one 8-column chunk for horizontal; one 8-row field population for vertical), compute `abs(mean(signed cross) - mean(signed comparators)) / (mean(abs(signed comparators)) + 1)`. Horizontal final score is the **equal-weight mean of four** subpopulation results (two parities x two chunks). Vertical final score is the **equal-weight mean of two** separate field-population results. Compute absolute value **after** subtracting signed means *within* each subpopulation, but **before** averaging subpopulation results; never average signed steps across fields first. Record exact sample counts and fail/skip according to explicit support rules rather than changing weights after seeing results.

**Proxy scoring and reporting:**

1. Threshold each metric at the **95th percentile of standard non-seam control scores** for a target **5% proxy false-alarm level**. Calibrate **once per clip, orientation and metric** on that clip's eligible control population, then hold that threshold fixed across the seam-class, picture-type and QP-stratum breakdowns. Define percentile/tie handling and comparison direction in the tool; report achieved false-alarm fraction, control counts and threshold. Do not choose a threshold separately after viewing a favourable stratum.
2. For each clip/orientation/metric, report the **seam hit rate** at that predeclared threshold and tie-aware rank-based **AUC** (area under receiver operating characteristic curve) using coded-seam and standard control populations. Include exact positive/negative denominators, missing/unsupported strata, and separate NONE internal positions as their own descriptive distribution, *not* interchangeable with standard negative controls. Break out by seam class (outer vs coded internal, FRAME/FIELD context, NONE-control), QP band (including QP=62 only where appropriate), and I/P/B. These are **proxy separability statistics**, not verified visible-artefact recognition accuracy.
3. **Uncertainty:** report frame-level metric populations and variation (e.g., median and quartiles of per-frame hit rate, AUC where estimable, and frame hit/phase winner rates), number of eligible frames, and **GOP-level** summaries using Stage 2 v0.6's display-order I-to-before-next-I convention when complete runs can be formed. Respect within-frame and between-frame correlation; do **not** compute false precision from hundreds of thousands of segment-level observations as if independent. If confidence intervals are added, they must use a documented deterministic cluster/GOP resampling procedure, record its seed/method and explicitly flag insufficient independent clusters. No uncertainty estimate is an extra acceptance threshold at S2-I2.
4. Provide a human-readable numeric table **per clip**, per orientation. Do **not pool** LP and LP_blocky results; strong blocky separability cannot compensate for weak or failed original-LP registration. Preliminary FFmpeg-only values (~20% vs ~47% LP, ~50% blocky at 5% proxy FA, vertical internal seams only) remain **informal and non-binding**; the formal code covers both orientations and provides reproducible samples/denominators.

**Interpretation caution:** seam-coded and non-seam positions are *not ground-truth classifications of visual compression damage*. Some coded seams carry negligible step; some controls contain real edges or propagated blocking; VHS noise, prediction and texture affect the overlap. No step is permitted to alter filter strength, select a kernel or denoise. Keep these diagnostics separate from the **registration gate** and from later S2-I3 screening of alternatives M1-M5.

## 4. Validation, sample discipline and robustness

1. **Before numeric work:** use `read_index` from S2-I1, run its established BestSource metadata validation for every frame, verify Y-plane dimensions and compatible native luma sample type/bit depth. Never ignore exceptions. `picture_structure` must remain supported frame pictures; a field picture is a hard unsupported-input error.
2. **No implicit picture conversions:** do not use chroma/luma range scaling, deinterlacing, interpolation, resizing or color conversion. Treat decoded stride/pitch correctly; data read-only.
3. **Leading B:** structurally process LP ordinals `[0,1]` and exclude them from LP registration/quality interpretation. On `LP_blocky`, calculate actual leading-B excluded ordinals from its own validated reader output and **assert 204 frames and zero leading B** against section 1.1; never inherit LP's `[0,1]`. For each clip separately output processed, excluded and eligible counts.
4. **Population counts and determinism:** every aggregate includes denominator and sampling rule. No random sampling. If memory limits arise, stream data per frame rather than silently reduce the population.
5. **External MB seams:** report luma outer-boundary step for FRAME and FIELD populations as a diagnostic only. Do not interpret outer edges as coded residual seams on both sides or decide whether they should be filtered.
6. **One source for indexed geometry:** new scripts use `stage2_index_reader_v0_2.py` as is. Stage 1 inspector, frozen analyzer and all six accepted baseline `.idx` remain unchanged/read-only. Original LP uses its tracked `.idx`; `LP_blocky` requires a **new, scratch-only, non-baseline** index created from its own video before secondary analysis.
7. **Negative checks:** wrong/missing source or index, mismatched dimensions/frames/picture type, unsupported field picture, invalid seam bounds, missing FRAME/FIELD class and synthetic shifted patterns should produce an explicit diagnostic failure/inconclusive/NOT APPLICABLE outcome, not a PASS. Unsupported secondary structure stops **its** analysis; it does not alter the original-LP gate.
8. **No tuning on hold-outs:** do not run the registration tool across the locked EP/2A/4A filtering hold-outs to rationalise a failed LP result without a separate owner decision. `LP_blocky` is not a filtering-quality hold-out or a replacement primary sample.

### 4.1 Required `LP_blocky` preflight / scratch-index procedure (new in v0.2)

This is a **procedure specification for a later Claude-reviewed tool**, not a command for the owner to execute now.

1. **Inputs/identities:** pin the actual `VHSC_samples/LG_576i_3_LP_blocky.mpg` path and SHA-256 in a per-run manifest; record FFmpeg/ffprobe, inspector, analyzer, Python reader and BestSource versions/identity. Detect missing source/tools before generating anything.
2. **Scratch ownership:** write only under `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky\` (or an explicitly approved equally isolated scratch directory). Never use `VHSC_samples` as the output location; never overwrite `LG_576i_3_LP.idx` or any of the six frozen `.idx` files. Any scratch `.m2v` derived from the recording is **Restricted Media** (NOTICE.md); handle and eventually delete it accordingly. The scratch `.idx` is non-baseline and uncommitted.
3. **Safe generation:** follow the accepted S2-I1 v0.2 file-based design: FFmpeg `-c:v copy -an -f mpeg2video` demuxes to a **regular scratch `.m2v` file**; only after FFmpeg has closed it, run frozen `Mpeg2BlockInspector.exe -b <scratch.m2v> -m <scratch.idx>`. **Do not pipe FFmpeg into the frozen inspector**: a short `read()` may end index acquisition prematurely yet exit 0. Do not have both processes append to the same CMD log simultaneously. Exit codes, missing/empty outputs and errors are distinct stop conditions. BAT logging must avoid CMD's digit-adjacent-to-redirection handle trap (e.g., use `>>"%log%" echo Inspector exit code: %inspector_rc%`).
4. **Independent validation before use:** run the frozen `tools/Stage1_Inspector_Analyzer_v0_2.py` on the candidate, independently parse it with `stage2_index_reader_v0_2.py`, check COMPLETE/format/record/MB invariants and compare all available analyzer totals (FRAME/FIELD/NONE, coding, effective-QP histogram, picture types, progressive-frame and structural flags). Cross-check indexed record count, dimensions/MB grid, and **every frame's picture type** with BestSource/decoded metadata using the established S2-I1 contract. A nominal inspector exit 0 or merely plausible frame count is **not** sufficient.
5. **Characterize before selecting applicable diagnostics:** record actual decoded frame count, width/height, macroblock grid, supported picture structure, chroma format, progressive-frame distribution, FRAME/FIELD/NONE populations, coding/picture types, effective-QP distribution and leading-B quality exclusions. Only if spatial format and native luma conditions satisfy the common reader/registration contract may diagnostics proceed. Although the verified index contains both FRAME and FIELD, re-check sufficient nonempty class populations for every 3x3 shifted-label contrast; if unexpectedly absent/too sparse, report an explicit failure of the expected preflight or INCONCLUSIVE/NOT APPLICABLE supported tests as appropriate, never artificial values. Never synthesize FIELD labels or silently substitute a new test.
6. **Identity/reproducibility:** compute the new scratch `.idx` SHA-256 and list its byte size, index record count and the source identity. **Assert the independently verified expected candidate SHA-256 and complete 204-frame/45x36/I-P-B/FRAME-FIELD-NONE/QP=62/no-leading-B identity in section 1.1.** Re-validate analyzer, reader and BestSource results on every run; a mismatch STOPs the secondary and is investigated, never silently relabelled as success or promoted to a baseline.
7. **Stop/cleanup:** stop secondary execution on malformed/index-decode mismatch, unsupported pictures/chroma/sampling format, or missing inputs; preserve the numerical error report and necessary scratch evidence for owner review. Supply an explicit reviewed cleanup procedure for Restricted scratch `.m2v` after verification; do not delete a still-needed evidence file automatically without making the lifecycle clear. Do not copy scratch media into review ZIPs or commit it.

**S2-I1 regression gate remains mandatory** and must still prove the six immutable reference hashes/summaries unchanged. The new `LP_blocky` candidate is a seventh *test-specific scratch index*, **not** a seventh immutable accepted baseline or part of the six-index regression suite.

## 5. Proposed software/file decomposition (conceptual names; no code yet)

Keep the already accepted `stage2_index_reader_v0_2.py` **unchanged**. Prefer one shared statistics module for both clips; no copy/paste clip-specific calculations. Design components (names not yet ratified):

- `stage2_seam_geometry_v0_1.py`: immutable-index seam enumeration and 2D candidate geometry, with FRAME/FIELD/NONE rules, outer-edge neighbours, coordinates and parity.
- `stage2_registration_stats_v0_1.py`: **VapourSynth-independent** shared numerical engine. Its public measurement entry points accept ordinary NumPy luma arrays (`Y` of one decoded frame at a time) plus accepted S2-I1 reader records/metadata, without importing `vapoursynth` or BestSource. It computes `D_raw`, `D_norm`, 3x3 shifted-label C, column and **row** phases, deliberately shifted-pixel controls, both-orientation M2/M4, proxy AUC/hit rates and frame/GOP summaries. Identical numerical logic must run under Claude's FFmpeg-decoded-frame rehearsal and the owner's BestSource path. Stream per frame/limited batches, retaining accumulators and bounded diagnostics instead of all decoded frames or seven displaced full clips simultaneously; **target <= approximately 1 GB working memory**. A small independent report/helper module is acceptable with Claude review.
- `stage2_registration_tests_v0_1.py`: deterministic synthetic positive/negative/error tests including parity, row +1/+2, column +4/+8, shifts +8/+16 and both-orientation proxy maths; no media.
- `stage2_registration_clip_v0_1.vpy`: a thin BestSource/VapourSynth **frame-provider adapter**. It performs S2-I1 structural validation and explicit source-index identity binding, extracts or views one frame's NumPy luma array at a time, and passes arrays plus reader records to the shared pure statistics engine; **no duplicated math or VapourSynth imports inside the statistics engine**, no silent conversion or filtering.
- `S2_I2_run_registration_v0_1.bat`: explicit `LP` / `LP_blocky` selection, separate temp folders/logs, a **tiny vspipe-executed `.vpy` preflight** (see below), all numeric report outputs and gate exit status; no implicit all-source mode.
- `S2_I2_prepare_LP_blocky_index_v0_1.bat`: sequential FFmpeg -> **regular scratch `.m2v`** -> frozen inspector -> analyzer and reader/BestSource preflight, including the exact independent expected hash and totals; safe independent log handles and restricted scratch cleanup instructions.

**S4 preflight, refined per Claude v0.3 S2:** supply `stage2_vspipe_env_preflight_v0_1.vpy` (or equivalently a tiny dedicated `.vpy`) and run it with the **same `vspipe --info` binary, environment and invocation method as the actual BestSource run**. It must import `numpy` and `vapoursynth` in the process used by `vspipe` itself and write to **stderr**: `sys.executable`, `sys.version`, `numpy.__version__`, VapourSynth version and BestSource version (or an explicit inability-to-query error, resolved before proceeding). It must exit nonzero/abort on import, plug-in-access or version-query failure; the BAT verifies the vspipe return code and captured diagnostic values **before** any clip decoding/measurement. No hardcoded Python path, and the separate shell `python` running S2-I1 scripts is not accepted as evidence that NumPy exists in the vspipe interpreter. Claude audits the CMD invocation and redirections. The module/file list grows by this tiny preflight adapter.

The `LP_blocky` index generation must **never pipe into the inspector**, nor allow two concurrent processes to append to the same Windows CMD log; redirections must avoid digits adjacent to `>>`. Reuse the approved sequential S2-I1 strategy; reject missing/empty outputs even with exit code 0. Claude independently executes/rehearses Python and data-dependent tests and audits every BAT line, including redirection, quoting, errorlevels, paths and `%TEMP%` lifecycle, **before** the owner runs it.

### 5.1 Numeric outputs, identity and Restricted Media discipline

Save **separate** scratch run folders, e.g. `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP\` and `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky\` (or equivalent reviewed isolated paths). Required files (CSV/report text/JSON only):

| Output | Minimum contents |
| --- | --- |
| `run_manifest.json` | source/index/script SHA-256, versions, BestSource/Python/NumPy, frame count/structure, exclusions; **fixed 16-pixel frame interior for row phase and control runs**, pair/chunk/parity definitions, exact **"pixels moved right/down by k; index unchanged"** offset sign and `Y_shift(x,y)=Y_original(x-cx,y-ry)` convention, all preapproved registration thresholds and tie handling |
| `seam_counts.csv`, optionally `seam_coordinates.csv` | exact index-directed geometry by orientation/class/frame; no character-art maps or hidden Restricted Media |
| `shifted_label_contrast.csv` | 9 shifts: counts, raw D, D_norm, margin, per-frame consistency and labelled disposition |
| `column_phase.csv` / `row_phase.csv` | 8 phase means/counts and per-frame ranks; column phase **10% margin**, row phase **5% margin and >=2/3 eligible-frame top-two consistency**; separate PASS/FAIL/INCONCLUSIVE and exact sample region/denominators |
| `known_bad_offsets.csv` | seven deliberate pixel displacements, all three verdicts, detecting test(s) and blind-spot coverage |
| `boundary_detectability.csv` | per clip, **both orientations**, seam/control class, plain and robust scores, 5% proxy-FA threshold, achieved FA, hits/AUC, picture type, QP band and all sample counts |
| `frame_gop_uncertainty.csv` | frame/GOP-level dispersion or explicitly unsupported/insufficient class, not segment-level pseudo-confidence |
| `outer_mb_edge_diagnostics.csv` | outer edge pair states and own step statistics, no silently chosen filter eligibility |
| `S2_I2_<clip>_result.txt` / `.log` | structural/preflight vs registration vs *non-gating* detectability dispositions and exceptions; stop/next step advice |
| secondary `index_preflight.txt` plus logs | scratch index full SHA-256, all exact expected counts/flags/QP histogram, analyzer/reader/BestSource correspondence and identity |

A cross-source numerical comparison may be generated only after independently validated clip reports exist; report denominators/context and *never pool* either thresholds or evidence. The descriptive detectability report is **not** a fourth registration gate.

No pictures/maps/stills required for S2-I2. An optional explicitly selected deterministic PNG overlay would be **Restricted Media** even without recognisable pixels, and cannot enter the review/commit ZIP without separately authorised compliant handling. Scratch source `.m2v` is Restricted Media and requires explicit reviewed deletion/retention instructions. Source videos are not bundled with tool packages. Ordinary numerical CSVs stay non-media unless embedding visual media content; no ASCII picture-like grids. Adhere to `NOTICE.md` and D-23 naming/identity conventions.

## 6. Proposed implementation tests and acceptance gates

| ID | Test / required evidence | Disposition |
| --- | --- | --- |
| A | S2-I1 six-index regression unchanged; original LP tracked hash correct | Any mismatch STOP |
| B | Synthetic FRAME/FIELD/NONE seam geometry, de-duplication and bounds | Must PASS |
| C | Explicit signed arithmetic and same-field 6|8, 7|9 sampling; no 7|8 or interfield mixing | Must PASS |
| D | Synthetic 3x3 shifted-label indexing on common lattice, diagonal and tie cases | Must PASS |
| E | Synthetic column 8-phase peak/shift and row q6/q7 paired peak; deliberately +1/+2-row errors recognized | Must PASS |
| F | BestSource/reader every-picture count/type/dims/chroma/format correspondence for LP (all 204, excluded 2) | Must PASS |
| G | LP_blocky regular-file demux, frozen inspector, analyzer and reader/BestSource checks; **expected b3f1d714...5238** and exact section 1.1 summary including **204/no-leading-B** | Must PASS for secondary reports; no index tracked |
| H | Original-LP 3x3 raw C unique zero maximum, **>=10% margin**, **>=2/3 frame support**, positive signal; report D_norm separately | PASS needed; otherwise primary blocked |
| I | Original-LP column phase 0 strictly top with **>=10% margin**, counts/frames | PASS needed; otherwise primary blocked |
| J | Original-LP row phases **q6 and q7 aggregate top two**, `row_margin >=0.05` with fixed 16-pixel interior, **>=2/3 eligible frames** also top two; any outside aggregate top-two phase => FAIL; otherwise insufficient margin/support => INCONCLUSIVE | PASS needed; otherwise primary blocked |
| K | All seven known-bad offsets caught by >=1 of the above tests; coverage/blind-spot matrix | Must PASS on each clip for which registration is claimed |
| L | Separate secondary 3x3/column/row outcomes, no eligibility fabricated and no rescue of original LP | Must report and investigate distinct secondary discrepancy |
| M | Descriptive **both-orientation** M2/M4, 5%-proxy-FA hit rates and AUC, seam classes, NONE/nonseam separation, QP, I/P/B and frame/GOP uncertainty | Required **report completeness**, not a tuned performance/pass target |
| N | Plain/robust synthetic known numerical values, percentile/tie/AUC semantics, control-sample integrity and frame/GOP grouping | Must PASS tests before formal data |
| O | **Same-`vspipe --info` tiny `.vpy`** confirms runtime Python/NumPy/VapourSynth/BestSource (sys.executable/version printed to stderr); source-index bindings, CMD redirections and scratch/Restricted Media lifecycle independently verified | Must PASS preflight/audit |
| P | Separate source reports with source/index hashes, exact eligible frames, manifests, no pictures, no mutable tracked baseline side effects | Must PASS |
| Q | Claude independent execution/rehearsal and line-by-line CMD audit; owner runs only cleared package and ratifies results | Required workflow gate |

**Formal primary registration PASS requires H, I and J PASS simultaneously, with all earlier structural/testing prerequisites and K satisfied.** A FAIL or INCONCLUSIVE on any primary registration diagnostic blocks later filtering-quality work. A secondary failure does not upgrade or cancel the independent original-LP primary verdict; it is always documented and assessed. Descriptive metric weakness, including low seam-proxy hit rate, **is not** S2-I2 registration FAIL.

**Disclosure of informal evidence (not formal results):** Claude's v0.2-review FFmpeg feasibility probe used LP/LP_blocky, found aligned shifts and phases, and deliberately tested offsets. Example aligned raw C peak margin approximately +28% LP / +38% LP_blocky; +1/+2 rows were blind to earlier tests, motivating row phase. The LP_blocky scratch index expectation is separately independently supported. These preview numbers are not acceptance measurements, do not permit threshold changes after the owner sees results and do not substitute for the formal Windows BestSource run.

## 7. Bounded handback and authority sequence

1. **Now:** Claude cold-reviews this **v0.4 design only** against the v0.3 review M1/S1-S3/O1, previous v0.2 review M1/S1-S4, Stage 2 v0.6, geometry/decisions/NOTICE and the pristine S2-I1 reader; particularly check the revised 5% row-phase gate, exact both-orientation comparator maths, vspipe preflight and VapourSynth-independent statistics interface. Owner explicitly ratifies approach and thresholds *before* formal execution.
2. **Implementation (separately approved):** ChatGPT produces bounded source/scripts, deterministic synthetic tests, manifest/source SHA-256 and review package. Do not change frozen Stage 1, index format or production DLL.
3. **Claude pre-owner:** run **the exact shared NumPy statistics engine** with independently FFmpeg-decoded original LP and scratch LP_blocky luma arrays, plus the accepted S2-I1 index records, exercising real raw/normalised D, 3x3/phase diagnostics, both-orientation M2/M4, known-bad controls and output schemas. Independently verify scratch-index identity. Perform synthetic tests and a line-by-line Windows BAT/CMD audit including the **vspipe-run `.vpy` preflight**, return codes, redirections and Restricted Media scratch lifecycle. Clearly distinguish Linux FFmpeg rehearsal from still-untested Windows BestSource and `vspipe` operation. Owner runs only after Claude clears the package.
4. **Owner Windows run:** LP then LP_blocky, per-source preflight, all three registration gates and descriptive reports, offset controls and sample identities. Owner returns numeric CSVs/logs/manifests for independent assessment; unexpected output => STOP and issue a versioned fix for re-review.
5. **Assessment:** distinguish LP mandatory PASS/FAIL/INCONCLUSIVE, secondary outcomes, descriptive hit/AUC uncertainty, known-bad coverage and unresolved confounding; no tuning to improve S2-I2 proxy results. Owner decides the S2-I2 gate.
6. **Install if approved:** named staging, verify `git diff --cached --check`, `git diff --cached --name-status --no-renames`, ensure no media/PNG, scratch `.m2v` or `.idx`, no obsolete versions or changed accepted indexes. Record LP_blocky assignment and row-phase addition in next genuine ratified Stage 2/status update; handover refresh after this milestone.
7. **Future scope only:** options-table v0.2 IDs **M1-M5 / F1-F3 / R1-R4 / B0-B1 / T1-T2 / P0-P2 / K1-K4 / G1-G2 / D0-D1** remain intact for an independently authorised S2-I3/S2-I5 design. **Nothing may be dropped without a written reason.** B1 (coding state/CBP beyond D-13) is an owner decision at that time; G1/G2 are optional aggregate before/after diagnostics, not S2-I2 per-seam decision controls. H.264-inspired step-limit/side-flatness/noise averaging/optional real-edge protection and no pre-denoising are *future* candidate principles, not current filter code.
8. **Future clean census:** only at S2-I8, **after kernel/thresholds freeze**, all 16 recordings each matched to its own validated index, no pooled per-clip evidence, locked hold-outs exposed only then. This is a future owner-directed scope item needing scheduling in that increment, not authorisation to run them in S2-I2.
9. **STOP:** no S2-I3 kernel implementation, threshold tuning or additional sample exposure before separate owner authorisation.

## 8. Precise v0.4 review questions for Claude

1. **M1 MUST (v0.3 review):** Confirm 16-pixel fixed interior, aggregate **q6/q7 top-two** membership, `row_margin >=0.05`, **>=2/3 eligible-frame** agreement, and classification of an outside aggregate top-two phase as FAIL. Confirm row displacement +1/+2 still fails and column/3x3 gates are unchanged (10% and 2/3 as applicable).
2. **S1 SHOULD:** Verify every horizontal same-field cross and comparator pair in section 3.6 against the v0.3 review, including MB-outer, controls 3|4 and 11|12, and FIELD/NONE mid-height non-coded classes. Confirm exact robust per-parity/per-8-column-chunk statistic and vertical transpose with two 8-row field populations. Are signs, bounds, denominators and equal weighting unambiguous for implementation?
3. **S2 SHOULD:** Verify the tiny `.vpy` preflight is executed by **the same `vspipe --info`** as the real workload, reports the interpreter/NumPy/VS/BestSource versions to stderr, fails closed, and does not guess a Python path.
4. **S3 SHOULD:** Verify the pure NumPy statistics engine consumes luma arrays plus accepted reader records **without VapourSynth import**; the BestSource `.vpy` is only a frame-provider adapter. Can you rehearse the **actual** statistic code against FFmpeg-decoded LP/LP_blocky clips, stream per frame within the approximately 1 GB bound, and then audit BAT separately?
5. **O1 OPTIONAL:** Confirm status v0.5 installation at historical commit `2286341` and positive offset convention **pixels right/down, index unchanged**; all seven bad offsets still use fixed equivalent target coordinates, same eligible-frame populations and no array wrapping.
6. **Carry-forward:** The original v0.2 findings and owner's descriptors remain incorporated: raw D gate and supporting D_norm, scratch LP_blocky index identity, seam map CSV, both-orientation M2/M4, 5% proxy false alarm/AUC and frame/GOP uncertainty. Confirm no threshold tuning, kernel selection, pre-denoising, hold-out exposure or pixel-only seam finding was introduced.
7. **Disposition:** Classify any remaining issues MUST/SHOULD/OPTIONAL, and state whether this **design-only v0.4** is suitable for owner ratification, after which a **separate S2-I2 implementation package** may be authorised. S2-I3 remains out of scope.

These are review requests, not executable instructions or final project-owner ratification.

## 9. Explicit non-decisions

- Stage 2 v0.6 remains the ratified methodology unless the owner later approves an actual revision; this S2-I2 design plus owner conversation clarifies implementation only. No new production algorithm is made authoritative.
- No Stage 1/source, analyzer, accepted six `.idx`, index-packing, native plugin or build-system modifications.
- No filtering, strength tuning, threshold fitting, de-noising for measurement, selecting M5, B1, G1/G2 or any M/F/R/T/P/K/D option at S2-I2.
- No pixel-only seam finder; the index defines geometry and coded-state semantics including the absence of internal seams for NONE.
- No claim that coded-seam proxy AUC/hits prove detector truth accuracy or indicate how often visible blocking occurs; no fake statistical precision from correlated segments.
- No automatic broad census now; optional additional pre-hold-out sources require owner confirmation; hold-outs stay sealed until S2-I8 and its later authorisation.
- No accepted seventh index baseline: LP_blocky scratch identity is now known but remains untracked/non-baseline; failing identity is STOP not an opportunity to regenerate an immutable reference.
- No claim that an unreviewed ZIP is installable, that formal Windows runs occurred or that `4221f7f`/`2286341` is current HEAD.
- No approval of S2-I3 or later from this draft.

## 10. Draft change log

### v0.4 - 2026-10-15 (FOR CLAUDE REVIEW; NOT RATIFIED)

- **Claude v0.3 M1 MUST:** row-phase Gate J uses **fixed 16-pixel frame interior, q6/q7 aggregate top-two, >=5% rank-separation margin and >=2/3 eligible-frame consistency**; wrong aggregate top-two phase FAIL. Column and 3x3 thresholds unchanged. Included Claude's disclosure of preliminary LP/LP_blocky observations.
- **Claude v0.3 S1 SHOULD:** full same-field horizontal cross/comparator pairs, vertical transpose, plain and per-parity/per-chunk robust M2/M4 formula with fixed signs and equal weights.
- **Claude v0.3 S2 SHOULD:** runtime NumPy/Python/VS/BestSource preflight via the **same vspipe --info** executing a tiny `.vpy`, no guessed Python path.
- **Claude v0.3 S3 SHOULD:** statistics module independent of VapourSynth, frame-by-frame FFmpeg/BestSource-compatible luma arrays and reader records, bounded ~1 GB; requires Claude to rehearse real numerical code.
- **Claude v0.3 O1 OPTIONAL:** historical status v0.5 commit `2286341`; manifest convention pixels shifted right/down by k while index stays fixed.
- Preserved all preceding v0.3 S2-I2 and owner additions (registration plus descriptive CSV only), future options-table v0.2 and S2-I8 all-16 intention. No S2-I3 implementation or filtering authorised.

### v0.3 - 2026-10-15 (FOR CLAUDE REVIEW)

- **M1 MUST:** added independent same-field 8-row-phase q6/q7 test with >=10% margin and 1-/2-row misregistration coverage.
- **S1 SHOULD:** fixed 10% zero-shift/phase thresholds, 2/3 per-frame consistency and PASS/INCONCLUSIVE/FAIL handling; noted informal values were seen beforehand.
- **S2 SHOULD:** introduced raw D versus D_norm (in-block slope controls) with raw D retaining gate ownership.
- **S3 SHOULD:** added 7 deliberately bad pixel-shift controls; pinned independently established LP_blocky exact hash, 204-frame identity, coded-state and QP totals.
- **S4 SHOULD:** added preflight NumPy import/version check in the *VapourSynth-used* Python interpreter.
- Included both optional coverage matrix and default numeric-CSV (no required PNG) clarifications.
- Owner-approved descriptive **both-orientation** M2/M4 seam/control strength, 5%-proxy-FA hit/AUC, per seam/QP/picture strata and frame/GOP uncertainty, with no new gate/tuning.
- Recorded LP_blocky verified characterization and pending formal scratch preflight; optional MLS/2A_blocky/4A_blocky owner confirmation; future all-16 S2-I8 census after freeze.
- Preserved **all** Claude pixel-test options-table v0.2 identifiers for later S2-I3/S2-I5, with no silent exclusions; deferred B1 owner decision.

### v0.2 - 2026-10-14 (PREDECESSOR REVIEW CANDIDATE)

- Added the narrow owner-approved LP_blocky secondary role and separate-index, separate-report, non-rescue safeguards to original v0.1.

### v0.1 - 2026-10-14 (SUPERSEDED REVIEW CANDIDATE)

- Initial original-LP S2-I2 registration and seam-map plan.
