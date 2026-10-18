# S2-I3 P0 - Evidence and Gate Report

**Repository path:** `docs/REPOSITORY/S2_I3_P0_Evidence_and_Gate_Report_v0_1.md`  
**Version:** 0.1 - RATIFIED by the project owner on 2026-10-18  
**Date:** 2026-10-18  
**Underlying gate disposition:** **P0 PASS, owner-ratified on 2026-10-18**, following Claude's independent acceptance of the complete evidence tree. This is a report of an already-ratified gate, not a new gate decision.  
**Repository drafting baseline:** Git `main` commit `8ffaa7d6d2500f842d5f841402a7b025ea4eda90` (post-cleanup, verified owner-provided HEAD and clean working tree).  
**Authors/review boundary:** Prepared by ChatGPT from the accepted owner Windows results, Claude's v0.5 independent report, the ratified interim bridge and the ratified S2-I3 / Stage 2 designs. ChatGPT did **not** independently execute P0 or examine the 137 raw evidence files. The independent raw-data recomputation and acceptance belong to Claude, not to this draft.  
**Authority:** `docs/REPOSITORY/05_DECISIONS_v1_2.md` (D-05/D-09/D-13/D-23/D-24/D-25/D-26); `docs/REPOSITORY/Stage2_Experiment_Design_v0_7.md`; `docs/REPOSITORY/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md`; `docs/REPOSITORY/06_DEBLOCK_CONCEPT.md` v1.2 at the report drafting baseline; subsequent v1.3 is a separately reviewed and ratified update when installed.

## 1. Gate result, precise boundary and decision provenance

**S2-I3 P0 REGISTRATION/ADMISSION GATE: PASSED.** P0A preflight PASS; P0B eight index identities match independent reference (six newly generated, one checked copy and one already frozen); P0C eight of eight sources REGISTERED at 100% exact qualifying P-skip identity; P0D eight descriptive diagnostic runs complete, all four paired-reference correspondence checks PASS; the global numerical summary says `READY_FOR_P1=true`, `ready_is_numerical_only=true`, `problems=[]`. Claude independently reviewed all **137** evidence files and recommends acceptance, with **no MUST** and four documentation SHOULDs; the owner subsequently **ratified P0 PASS on 2026-10-18**.

This gate proves a bounded, checked correspondence of Stage 1 index metadata to BestSource display frames and of four original/blocky pairs. **No deblocking filter was run or evaluated. No kernel, strength, threshold, chroma policy, NONE-edge policy or P1 selection has been authorised, tested or approved.** A PASSED P0 gate is neither Stage 2 filter feasibility PASS nor authorisation for P1. Protected S2-I8 hold-outs remain locked. Unadmitted 6A/7A media are outside P0.

Record as contemporaneous follow-through, not as evidence of filter quality: on 2026-10-18 the owner committed the seven new SHA-checked development indexes (`35923a540a9e1dbe5893552dec784a5a7b414cee`, exactly 7 A / 0 M / 0 D), and completed separately bounded current-tree review-artefact cleanup Commit A (`7f8e445`), Commit B (`b83ab3e`) and Commit C (`8ffaa7d6`). Git history has **not** been scrubbed; that remains a Development Closure obligation. The six Stage 1 frozen baseline indexes were not changed.

## 2. Evidence classes and immutable source references

The distinction between sources is mandatory, because a test of index/pixel identity is not itself a filter-performance observation.

| Evidence class | What it establishes | What it does NOT establish |
|---|---|---|
| RATIFIED MECHANISM (`06` K-02/K-03/K-07/K-08; D-09) | Meaning of residual transform geometry and candidate seams | That a proposed filter is safe or effective |
| OWNER-RUN WINDOWS P0 | Exact identity/temporal controls for eight admitted development sources; paired correspondence; tested runtime | Improvement in subjective or objective decoded video quality |
| CLAUDE INDEPENDENT EVIDENCE AUDIT | Recalculated P-skip and pair-rule decisions from raw evidence; checked hashes, controls, consistency | Independent execution on owner's Windows machine |
| CLAUDE INDEX-ONLY RECOMPUTATION | Transform-state regimes, NONE composition and neighbour transition rates | Pixel appearance, filtering performance or real-population prevalence |
| CLAUDE EXPLORATORY LUMA RESEARCH | Original/blocky local difference signals and crude blur-probe harms on a Linux/BestSource development population | P0 owner-run pixel metric; adopted optimisation target or quality gate |
| INTERPRETATION / HYPOTHESIS | Bounded predictions for future S2-I4+ design | A ratified metadata, threshold or filter-policy change |

**Permanent reference documents:** `docs/Claude_P0_EVIDENCE_REVIEW_AND_GATE_RECOMMENDATION_v0_5.md` (the definitive final v0.5 review, *not* preliminary v0.1-v0.4); `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_4.md` (observational status, predating formal owner ratification and cleanup); and the independently reviewed `docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md` (temporary evidence bridge; sections 3-8, 12 and 14-17 are reproduced in section 9 of this report; methodological sections 11 and 13 are captured in sections 5 and 6). Retain the bridge until every transfer row has been reviewed and owner-ratified; do not retire it merely because this report exists. Bridge sections 1 (Route A rationale), 9 (transfer checklist), 10 (dated operational guardrail) and 18 (consolidation record) are deliberately not copied: they are process material that expires at bridge retirement. Bridge section 2's durable prohibition on quoting invalid v0.2 boundary/interior measurements is carried in section 13 item 5.

**Raw evidence (outside the report installation commit):** the accepted P0 scratch `results/` tree, `%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1\results`, comprising eight source subtrees x 16 files, four pair subtrees x 2 files and `P0_summary.json`: **137 files**. The full tree was furnished to Claude for independent evaluation. The owner retains P0 scratch; no rerun, regeneration or duplication of restricted pixels/media is directed by this report. The evidence-only archive recorded for owner transfer has SHA-256 `898763a3e43d1a80f4c31713b4ccb9a498cd86c27c846eb15ddfabf498146af4` and 158 ZIP entries including directory entries, not 158 evidence files.

## 3. P0A preflight, failure recovery and safety checks

The initial P0A run failed at an isolated Python import (`ModuleNotFoundError` of sibling P-skip core); it did **not** establish a failed registration gate. The corrected, Claude-cleared invocation explicitly prepended the script directory via `sys.path` when using embedded/isolated VapourSynth Python. The owner reran P0A successfully with unchanged five Python modules and three VPY files.

Accepted Windows P0A checks: six frozen Stage 1 index regressions passed; four negative index tests passed; **9/9 P-skip** and **5/5 pair** unit tests passed; VapourSynth R81/BestSource preflight passed. The expected absence of a protected `TEST_4A_A003_blocky.idx` is not a failing regression nor permission to create it. The corrected P0A returned exit code zero. Detailed isolated-Python fail-closed lesson is preserved in Annex J for the next role handovers.

## 4. P0B cross-platform index identity and P0C source admission

The table combines the **eight independently anticipated Linux** index identities with the actual **Windows MSVC generation/check/copy results** and qualifying P-skip equality. Six new indexes were generated with the frozen Windows inspector; `LP_blocky` was byte-copied from accepted S2-I2 scratch; original `LP` was reused from the frozen Stage 1 baseline. All eight values match Claude's Linux `gcc -O2` reference **for these sample streams only**.

| Label | Frames | Native geometry | P-skip identical/total | Qualifying P pictures | Full SHA-256 of index | P0C |
|---|---:|---|---:|---:|---|---|
| XP | 228 | 720x576 | 1,619/1,619 | 54 | `4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127` | REGISTERED |
| XP_blocky | 228 | 720x576 | 25,635/25,635 | 55 | `8d0326b5975b19b36742717a80be9eaf11bc21f379f2855eb22651e94dd16b20` | REGISTERED |
| SP | 192 | 720x576 | 1,764/1,764 | 46 | `40a97ce1a9920cd63e45da13371e0b41ff1619fed688d6145899a300463cc5d9` | REGISTERED |
| SP_blocky | 192 | 720x576 | 19,010/19,010 | 46 | `7e19ca6078075e7bf7a3a34bcda0816267e4d38ad02a56e01b6b0ed726ace746` | REGISTERED |
| LP | 204 | 720x576 | 1,533/1,533 | 46 | `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011` | REGISTERED (FROZEN) |
| LP_blocky | 204 | 720x576 | 20,300/20,300 | 50 | `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238` | REGISTERED (COPIED) |
| TEST 3A | 300 | 704x576 | 8,812/8,812 | 133 | `9a60a8d24a7e4a45cbe82b4f41d232ede0e5c00624e82a8f8099f61351957f33` | REGISTERED |
| 3A_blocky | 300 | 704x576 | 18,190/18,190 | 73 | `e6f556dd4aaed0f4709b7c011fcf045193dccbb8abd2a01c646dddf0da893c83` | REGISTERED |

The labels `3A` and `TEST 3A` refer to the same admitted TEST_3A_A002 source throughout this report. Both display frame geometry and metadata frame counts agree; all eight are native YUV420P8. Every admission returned zero and a complete index-verifier PASS. Claude's independent audit reconstructed all totals from `per_P_picture` and confirmed anchor order, per-picture exactness, frame picture structure, hash identity, and qualifying picture counts. **P0 is a luma registration gate only:** it cannot certify chroma registration or field identity.

## 5. Why the P-skip identity rule is a gate, and its known blind spots

An MPEG-2 **frame P-picture SKIPPED macroblock** has zero forward-motion prediction and no coded residual; its reconstructed 16x16 luma samples must match the co-located block in the immediately preceding I/P **anchor in display order**. There is no adjustable error tolerance: **any true-position inequality fails**. An indexed `NONE` state alone **never qualifies** a macroblock as P-skip: NONE includes INTER/CBP=0 cases that may have motion vectors, and skipped B-picture blocks do not share this forced-zero model.

Before comparison, check output ordinals, frame picture structure (`picture_structure==3`), chroma 4:2:0, frame counts and coded macroblock grid, pixel format YUV420P8 without conversion, and picture-type agreement with BestSource `_PictType`. The true anchor is found by scanning previous display-order I/P pictures, **not** assumed to be `n-1`. A qualifying unit is one skipped macroblock of one P frame picture. Use at least **200 such blocks** and **10 qualifying P pictures**; 200 and 10 are passing boundaries, 190 and 9 are below floor.

Negative controls: **24 spatial** hypotheses (ten x, ten y, four diagonals, including the seven earlier known-bad offsets) applied to both windows while they remain in bounds, and **three temporal** hypotheses (earlier anchor, next display picture, previous display picture), excluding a previous-display control wherever it equals the actual anchor. Structural failure or any true-position mismatch is **FAIL**, taking precedence over sampling weakness. Missing counts/control, or any executed control itself reaching 100%, is **INCONCLUSIVE**. Exact identity and every informative control below 100% led to REGISTERED for all eight sources.

**Independent limits:** A consistent top/bottom field swap is not detected by this identity test. For an IPPP stream, `previous_display` equals the true anchor and the test is INCONCLUSIVE. Neither blind spot occurred as a triggered control failure in the eight admitted B-containing development sources, but neither can be described as universally solved. No blanket claim about cross-decoder equality or all MPEG-2 streams is made.

### 5.1 Highest negative-control matches and the decisive threshold-free lesson

| Source | Highest spatial control | Matching blocks | Highest temporal control | Matching blocks |
|---|---|---:|---|---:|
| XP | (-1,0) | 48.86% | previous_display | 83.88% |
| XP_blocky | (+1,0) | 73.22% | older_anchor | 37.56% |
| SP | (+1,0) | 45.24% | previous_display | 77.72% |
| SP_blocky | (0,+1) | 73.35% | older_anchor | 33.75% |
| LP | (0,-1) | 40.29% | previous_display | 94.85% |
| LP_blocky | (+1,0) | 69.16% | older_anchor | 36.34% |
| 3A | (-1,0) | **93.08%** | previous_display | **96.72%** |
| 3A_blocky | (-1,0) | 78.61% | previous_display | 47.18% |

On Windows, 3A's built-in **horizontal (-1,0) per-block offset control** reproduced **93.08%** of its 8,812 qualifying blocks, with **610** blocks differing, whereas the true aligned hypothesis reproduced all 8,812 with **zero mismatches**. The strongest control of any kind on 3A was the wrong `previous_display` temporal hypothesis at **96.72%**, differing in only **289** of 8,812 blocks. On Linux, a distinct **whole-clip vertically shifted one-line negative rehearsal** reproduced **90.2%** of qualifying blocks. **Neither number supersedes the other:** they involve different directions, perturbation implementations, populations and platforms. Both show why a tolerance below roughly 93% cannot replace strict identity. LP's wrong previous-display control also reproduced 94.85%; 3A's reached 96.72%. These high wrong-control matches are evidence *for exactness*, not gate violations.

Other Linux fault rehearsals correctly FAILED: XP frames with XP_blocky index (8.7% match), reverse swap (34.0%), LP +1 display-frame slip (80.4%), 3A -1 display slip (84.8%), SP_blocky x+2 (71.1%) and 3A one-line vertically shifted (90.2%). These are **Linux injected-fault rehearsals**, not owner-run P0 Windows fault cases.

## 6. P0D original/blocky correspondence and diagnostic disposition

For pair `b_N` and original `o_N`, candidate temporal offsets `k=-2..+2` are tested on common-interior frames. A frame is **decisive** if `min_{k != 0} MAE(o_N,o_{N+k}) >= 2 * MAE(b_N,o_N)`. By the triangle inequality, in a decisive frame no competing shifted original can be closer to `b_N` than the aligned original. A PASS requires equal frame counts, strict **clip-mean** minimum at zero offset, **zero** decisive-frame violations, and **at least 20 decisive frames and 10% of eligible frames decisive**. A floor miss blocks paired metrics as INCONCLUSIVE; any decisive violation is FAIL. The last two floors were **selected after observing the preflight values** and are reported here as such, not represented as preregistered independently of the rehearsal.

| Pair | Result | Decisive / common-interior evaluated | Decisive violations | MAE at k=0 | Best competing mean | Decisive / all clip frames |
|---|---|---:|---:|---:|---:|---:|
| XP | PASS | 140/224 | 0 | 3.5250 | 9.8761 | 61.4% |
| SP | PASS | 175/188 | 0 | 3.2322 | 13.9828 | 91.1% |
| LP | PASS | 81/200 | 0 | 4.3876 | 9.9337 | 39.7% |
| 3A | PASS | 268/296 | 0 | 5.5276 | 19.9471 | 89.3% |

The denominators 224/188/200/296 are four fewer than clip frame counts because the window needs a margin of two frames on each side. Across the four pairs Claude independently evaluated **908** individual frame records, of which **664** are decisive; the 908 records must not be mislabelled "908 decisive frames". The paired-media source hashes in pair reports exactly match their corresponding admission hashes; all eight media hashes are distinct. A fully static, all-ties case is presently classified FAIL where INCONCLUSIVE could be more semantically accurate, but both block use of paired metrics; no present source engages that edge case.

Eight S2-I2 descriptive diagnostic passes ran to completion over all eight sources, with CSV reports generated and marked `REPORTED_NOT_GATE`. Five historical legacy S2-I2 dispositions are PASS; **SP, SP_blocky and 3A are BLOCKED** by the legacy phase-contrast test's preconditions, *not* misregistration. All three pass P0's exact identity gate. A legacy `FAIL` in `known_bad_offsets.csv` is a desired rejection of an injected bad offset. The accepted S2-I2 source (`stage2_registration_stats_v0_1.py`) defines `caught = (cx == 0 and ry == 0) or any(result != PASS for result in (shift,column,row))`. Thus the aligned-reference row is **True by definition**, while a nonzero-offset row is True when any component rejects or cannot pass. It is **not** a P0 admission verdict; the **(0,0) row is the aligned reference, not a deliberately bad offset**. In particular its `caught=True` alongside a 3A row `INCONCLUSIVE` must not be read as a false rejection of correct alignment. Claude independently verified this interpretation against the accepted source-code rule in its 2026-10-18 Route A review; this is an explanation of existing CSV logic, not a redefinition. `auc_proxy=NaN` in source diagnostics is an unresolved descriptive implementation detail, not a gate defect.

## 7. Independent audit, reproducibility and limits

Claude reviewed the **entire** 137-file evidence tree, recomputed 8/8 `per_P_picture` identity totals and all 908 pair `frame_evidence` decisions, and verified 24 spatial/3 temporal control populations per source; eight index SHA and source/hash chains; 8 runtime records; all expected diagnostics; exact source allow-list and exclusion of hold-outs; and `P0_summary.json`. No gate-bearing field failed, and the global summary records all eight admissions REGISTERED, four pair PASS, `problems=[]` and `ready_is_numerical_only=true`. Claude's acceptance verdict was **P0 EVIDENCE ACCEPTED**, with zero evidence MUST. This review is the independent source of these assertions; the present ChatGPT draft did not access the underlying Windows `results/` data.

**Environment:** Windows x64, VapourSynth R81; BestSource PluginVersion 22.0, DLL SHA-256 `fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c`; isolated/embedded CPython 3.14.8 MSC v.1944 x64; NumPy 2.5.4. BestSource DLL bytes match accepted S2-I2. Linux research was CPython 3.13 / NumPy 2.5.3; Windows S2-I2 was NumPy 2.5.3. Do not claim the whole environments are identical. The cross-platform generated `.idx` SHA match is established **on these eight development samples**, not every possible MPEG-2 stream. P0 itself did **not** prove per-pixel cross-decoder equivalence.

## 8. Transfer of pre-P0 descriptive findings and corrected interpretations

Sections below are **durable empirical annexes** derived from the Claude-consolidated and owner-ratified interim knowledge bridge, with the evidence class of each retained. They are not owner-run P0 quality results. This deliberate distinction preserves corrected technical knowledge while making P0 admission and gate status independent of speculative filter performance.

## 9. Transfer annexes: corrected measurements and methods from the interim bridge

The eleven annex entries reproduce the controlled interim bridge's sections 3-8, 12, and 14-17, with section-heading depth adjusted only. Their reported classifications and measured numbers are historical evidence **not rerun by ChatGPT**; the original exploratory Linux analyses did not preserve their scripts or raw per-frame CSVs. Text referring to future work is a proposal/limitation, not a permission to act. The P0-specific results above supersede dated operational checkpoints when these annexes mention them.

### 3. Geometry: established facts versus new empirical support

**RATIFIED / DO NOT REDECIDE.** K-02: mixed FRAME/FIELD residual transform organisation can vary per
macroblock. K-03: in a frame picture, a FRAME-coded luma residual has a mid-height horizontal internal
seam (between frame rows 7 and 8 of the 16x16 macroblock), whereas FIELD-coded residual luma has its
horizontal internal layout on a field-line grid and **no** seam across frame rows 7/8; both have the
luma internal **vertical** transform seam at x=8. K-07: FRAME/FIELD/NONE denotes applicable **coded
residual transform geometry**, not merely the presence or value of `dct_type`; NONE covers skipped
macroblocks and effective-CBP-zero non-intra macroblocks, and an absent `dct_type` bit does **not**
automatically mean NONE. K-08: motion compensation can carry older blocking away from the current
grid. Frame ownership (D-09) and field-parity-aware access constrain safe pixel operations; selecting
FRAME DCT does **not** authorise cross-field temporal mixing.

**Terminology, correction M1.** A **vertical boundary** runs along fixed x and is shared by
side-by-side macroblocks. A **horizontal boundary** runs along fixed y and is shared by stacked
macroblocks. The Stage 1 analyzer's labels `neigh_h` and `neigh_v` describe **neighbour traversal
direction, not line orientation**: `neigh_h` pairs `i` with `i+1` (side by side, **shared vertical
boundary**); `neigh_v` pairs `i` with `i+mb_width` (stacked, **shared horizontal boundary**). Claude
verified this against the analyzer source.

### 4. Recomputed index measurements: composition and mixed regime

**CLAUDE RECOMPUTED INDEX STATISTICS.** Fractions of ALL macroblocks including NONE; "frames
containing both" means records containing both FRAME and FIELD anywhere, NONE neither required nor
excluded. Rounding can affect totals.

| Original group | FIELD (%) | FRAME (%) | NONE (%) | Frames containing both FRAME and FIELD (%) |
|---|---:|---:|---:|---:|
| XP | 70.9 | 12.1 | 17.0 | 99.1 |
| SP | 73.4 | 5.9 | 20.8 | 99.5 |
| LP | 52.7 | 23.0 | 24.3 | 97.1 |
| TEST 3A | 7.6 | 67.9 | 24.5 | 92.3 |

Project material has markedly different transform regimes and extensive within-frame mixing, so a
global FRAME-or-FIELD choice cannot model all applicable coded residual geometry. **XP is 70.9% FIELD
while TEST 3A is 67.9% FRAME - opposite regimes.** This is a SOURCE-CHARACTERISATION result
strengthening the existing index-driven concept, and the strongest available measured support for the
owner's requirement to develop across source types. It is not new codec policy.

**Corrected neighbour transitions (M1 + M2).** A mixed transition requires both macroblocks coded
FRAME/FIELD with different states. The `coded denominator` counts a pair only if BOTH are FRAME or
FIELD; the `all-pairs` percentage uses every adjacent pair including NONE. **Never quote these
percentages without their denominator.**

| Original group | Shared VERTICAL: mixed / coded pairs | V: % coded | V: % all pairs | Shared HORIZONTAL: mixed / coded pairs | H: % coded | H: % all pairs |
|---|---|---:|---:|---|---:|---:|
| XP | 40777 / 263190 | 15.5 | 11.3 | 41093 / 261737 | 15.7 | 11.4 |
| SP | 17033 / 207878 | 8.2 | 5.6 | 17431 / 205755 | 8.5 | 5.8 |
| LP | 48341 / 204603 | 23.6 | 15.0 | 49005 / 204111 | 24.0 | 15.3 |
| TEST 3A | 29651 / 320772 | 9.2 | 6.4 | 31721 / 315915 | 10.0 | 6.9 |

Blocky counterparts, coded-pair basis only (VERTICAL / HORIZONTAL, percent): XP_blocky 26.2 / 21.3;
SP_blocky 22.5 / 19.4; LP_blocky 22.8 / 19.8; 3A_blocky 23.1 / 24.0.

The originally relayed 15.7 / 8.5 / 24.0 / 10.0 values are **HORIZONTAL** boundaries, not vertical.

### 5. Per-macroblock paired luma MAE, corrected row-7/8 interpretation (M3)

**CLAUDE MEASURED LUMA PIXELS.** Native decoded YUV420P8, plane Y only, all development frames;
per-pixel absolute difference between each higher-quality original and its Q62 `_blocky` transcode,
assigned by the **blocky encode's own** per-macroblock transform state. Comparison is **within** each
transform state. This is an empirical confirmation of existing mechanism, not a filter's gain and not
a quality threshold.

| Pair | MB state | H band rows 7,8 MAE | Within-state interior MAE | H-band excess | V band cols 7,8 MAE | V-band excess |
|---|---|---:|---:|---:|---:|---:|
| XP | FRAME | 4.465 | 3.735 | +19.5% | 4.609 | +23.4% |
| XP | FIELD | 6.255 | 6.059 | +3.2% | 7.525 | +24.2% |
| SP | FRAME | 2.977 | 2.562 | +16.2% | 3.088 | +20.5% |
| SP | FIELD | 5.642 | 5.462 | +3.3% | 6.856 | +25.5% |
| LP | FRAME | 6.495 | 5.539 | +17.3% | 6.792 | +22.6% |
| LP | FIELD | 6.696 | 6.522 | +2.7% | 8.048 | +23.4% |
| TEST 3A | FRAME | 6.611 | 5.860 | +12.8% | 6.829 | +16.5% |
| TEST 3A | FIELD | 8.484 | 8.296 | +2.3% | 9.877 | +19.1% |

For the FIELD state there is **no coded residual transform seam at frame rows 7/8**, so +2.3% to +3.3%
is a **control**, not a FIELD horizontal seam measurement. Applicable FIELD horizontal seams lie on
the field-line pitch, at different frame-line locations. The vertical x=8 seam exists in both states.
FRAME at rows 7/8 (+12.8% to +19.5%) against the FIELD control (+2.3% to +3.3%) - a factor of four to
eight - plus V signal in both states (+16.5% to +25.5%), supports **K-03** and the **x=8 independence**
on actual decoded project material.

Absolute MAE is much higher in FIELD regions because field DCT is chosen where vertical-temporal
activity is high. **Only within-state excess is comparable; never compare FRAME to FIELD absolute MAE
as a filter-effect estimate.**

**Critical correction.** The earlier Claude v0.2 whole-frame 8-line geometry-blind calculation reported
only 7-10% boundary excess and characterised paired MAE as a weak objective. Its mask sat at
nonexistent seams for most FIELD macroblocks - and XP, SP and LP are 53% to 73% FIELD - so the global
result **diluted a real signal**. **SUPERSEDED CONCLUSION:** "paired MAE is intrinsically too weak to
guide a deblocker". **Surviving narrower claim:** global geometry-blind paired MAE is dominated by
irrecoverable content differences, but a geometry-aware, seam-localised paired metric has usable
signal. Neither finding demonstrates a filter improvement. **This correction must accompany every
reuse of these numbers.**

#### Reproducible method

1. Index: `read_index` from `stage2_index_reader_v0_2`; map `{0:NONE,1:FRAME,2:FIELD}`; macroblocks in
   raster order via `rec.iter_macroblocks()`; grid from the record header. For original/blocky luma
   comparison use the **blocky** index.
2. Pixels: BestSource `VideoSource`, native YUV420P8, **no** pixel format conversion, plane 0;
   `d = abs(int16(original_Y) - int16(blocky_Y))` for corresponding decoded display frames.
3. Band masks within the macroblock: H rows `y % 16` in `{7,8}`; V columns `x % 16` in `{7,8}`;
   interior requires **both** `y % 16` and `x % 16` in `{2,3,4,5,10,11,12,13}`, which excludes outer
   macroblock edges, the inner seam bands and their immediate neighbours.
4. Accumulate absolute-difference sums **and** pixel counts per transform state across all frames;
   `excess_percent = 100 * (band_mean / interior_mean - 1)`. Compare within state only. Record no
   result for NONE, which defines no current coded residual seam.
5. Transition recipe: side by side `(i, i+1)` for `x+1 < mb_width`; stacked `(i, i+mb_width)` for
   `y+1 < mb_height`. Count as mixed only if both are coded and the states differ. Keep coded-pair and
   all-pair denominators separate.
6. Research runtime: VapourSynth R81, BestSource 22.0, NumPy 2.5.3, CPython 3.13 on Linux. The owner's
   P0 Windows environment is embeddable CPython 3.14.8 with NumPy 2.5.4 - **not** the research runtime.
7. **Claude's answer to the draft's question on script availability: the analysis scripts are NOT
   retained.** They lived in an ephemeral session workspace and no raw per-frame CSVs were kept; all
   test media was deleted after use as `NOTICE.md` requires. **The method above is complete enough to
   rewrite them from scratch**, which is why it is specified at this level of detail. Treat every
   number in sections 4 to 7 as a *result to be reproduced* rather than a *file to be located*.

### 6. Paired original/blocky baseline, exploratory probes, and metric caveats

**CLAUDE MEASURED LUMA PIXELS, whole-frame** - a valid global baseline, **not** a seam-specific
geometry model:

| Pair | Global original/blocky luma MAE | Old geometry-blind boundary MAE | Old geometry-blind interior MAE |
|---|---:|---:|---:|
| XP | 3.567 | 3.745 | 3.428 |
| SP | 3.266 | 3.436 | 3.134 |
| LP | 4.355 | 4.588 | 4.173 |
| 3A | 5.512 | 5.748 | 5.329 |

The global column remains a broad paired-reference descriptor. **Do not use the old boundary/interior
columns to argue about FRAME/FIELD seam placement** - that is the M3 error. The original is a
higher-quality **encoded MPEG-2 reference**, not uncompressed ground truth (D-26).

| Pair | Blur across vertical edges | Within-field vertical blur | Combined | Naive cross-frame-line vertical blur | Same naive blur: harm to the clean original |
|---|---:|---:|---:|---:|---:|
| XP | +1.2% | -1.2% | -0.2% | -12.3% | 1.092 |
| SP | +1.3% | -0.3% | +0.8% | -26.8% | 1.557 |
| LP | -0.2% | -3.8% | -4.1% | -7.5% | 1.051 |
| 3A | +2.3% | -4.7% | -2.9% | -20.3% | 2.244 |

These were **crude fixed-geometry probe filters**, not candidate or ratified index-driven kernels, and
the figures are changes in **global** MAE. They cannot be reinterpreted as S2-I3 results.

**The most consequential number here is the harm column.** A naive cross-frame-line vertical blur
damages a **clean** original by 1.051 to 2.244 MAE, which is comparable to a large part of the entire
blocky-versus-original gap of 3.5 to 5.5. On 576i material vertically adjacent frame lines belong to
different fields and therefore different instants. **Frame DCT is an encoder rate-distortion decision
and is never by itself evidence that cross-field frame-line filtering is safe.** Field-parity access
remains an explicit invariant (D-09, O-14).

Claude's own crude probes applied **one** geometry globally and so were wrong for the majority of
macroblocks in three of four sources. Their near-zero results are evidence against **uniform**
geometry, **not** against index-driven filtering.

**Historical "blockiness excess" values - preserve WITH INVALIDITY LABELS.** Claude v0.2 computed a
*difference* between the mean step at periodic edges and the mean interior step. The 'H' axis (across
the x=8 vertical seam) gave ORIGINAL/BLOCKY: XP 1.614/2.313; SP 1.950/2.816; LP 2.319/3.169;
3A 1.726/3.352; this axis is unaffected by the vertical-pitch error because x=8 is transform-type
independent. The 'V' axis (field-line 8 pitch) gave XP 1.011/2.145; SP 1.472/2.879; LP 1.189/2.221;
3A 3.715/6.197, **but it mixes FRAME and FIELD coded geometries and is NOT comparable between
sources**. Neither axis is a P0 gate.

**The ratio form of this metric must never be used as a gate.** Claude also computed boundary/interior
as a *ratio* and it diverges on Q62 material whose block interiors are flat: measured H ratios were XP
69.0, SP 10.9, **LP infinite** (zero denominator) and 3A 2.2. Use the **difference/excess** form with
documented masks and denominators.

**D-26 already controls the evidence hierarchy.** Real LG media are **PRIMARY** feasibility evidence,
assessed with seam-local diagnostics, collateral/no-harm results and the owner's visual assessment.
Software-encoded Q62 pairs are **SECONDARY** paired-reference evidence, measuring movement toward or
away from a higher-quality *decoded* source. A direction-separated blockiness-excess target
approaching the original's non-zero value, geometry-aware local MAE, and paired global/boundary/
interior MAE are **candidate analytical measures only**, not adopted replacements for the ratified
S2-I3 rubric. A filter that reduces a seam statistic while damaging off-seam content must **not** be
called successful on the seam statistic alone.

### 7. NONE composition and inherited-blocking concern

**CLAUDE RECOMPUTED INDEX STATISTICS.** Percentages are of **NONE macroblocks only** per source, not
of all macroblocks.

| Source | NONE count | Skipped in P (%) | Skipped in B (%) | INTER CBP=0 (%) | Other (%) |
|---|---:|---:|---:|---:|---:|
| XP | 62669 | 2.6 | 37.4 | 60.0 | 0.0 |
| XP_blocky | 272084 | 9.4 | 26.9 | 63.7 | 0.0 |
| SP | 64536 | 2.7 | 35.0 | 62.3 | 0.0 |
| SP_blocky | 210261 | 9.0 | 27.2 | 63.7 | 0.0 |
| LP | 80286 | 1.9 | 29.6 | 68.5 | 0.0 |
| LP_blocky | 242335 | 8.4 | 23.2 | 68.4 | 0.0 |
| TEST 3A | 116585 | 7.6 | 14.4 | 78.0 | 0.0 |
| 3A_blocky | 285701 | 6.4 | 25.9 | 67.8 | 0.0 |

Only skipped macroblocks in **P** pictures are guaranteed co-located under the zero-motion identity
model that underlies S2-I3 P-skip admission (section 11). Skipped **B** macroblocks may reuse prior
motion; INTER with effective CBP=0 may carry vectors. So **1.9% to 9.4% of NONE is the guaranteed
zero-motion co-located portion, and 90% to 98% is *potentially* - not provenly - off-current-grid
inherited content.** Motion interpolation is fractional-pixel, so a copied boundary is not necessarily
a rigid displaced grid. The index records motion signalling, type and direction but **no motion-vector
components** (section 12), so grid displacement cannot be reconstructed from today's index. K-08 and
O-04 already own the policy risk; adding vector data or an `.idx2` requires fresh evidence meeting
D-13 and explicit authorisation, and **Stage 1 stays frozen**. Nothing here establishes how many of
the remaining NONE cases actually show off-grid visible blocking.

Q62 raises the NONE share markedly (XP original 17.0%, XP_blocky 73.7%). The correlation is
descriptive; no causal analysis was done. For later work consider `NONE` and `NONE`-touching edge
breakouts and I/P/B stratification as **hypotheses**, not filter rules.

### 8. Open breadth, quantisation and chroma questions (NOT authorised modifications)

- Q62 `_blocky` variants are an **extreme single quantisation point**; LP_blocky has completely flat
  block interiors. Generalising kernel settings from Q62 alone is risky. Additional encodes around
  Q25-Q40 could be evaluated as an independent future design amendment, with source-group weighting
  and correlated-variant handling - re-encodes of the same content are **not** independent samples.
  The two S2-I4 QP estimands remain separately governed. This is not authorisation to add media or
  change folds.
- **Falsifiable orientation prediction.** Index-driven geometry should contribute its largest
  incremental benefit for **horizontal** seam handling, where FRAME versus FIELD changes the seam
  placement, and least for the **vertical** x=8 seam, whose location is transform-type independent.
  Measure direction-separated gains and clean-source harm under comparable optimisation budgets.
  Currently a hypothesis; section 5 supplies the baseline magnitudes to test against.
- All measures in this note are **luma only**. D-25 retains chroma in scope; K-04 establishes chroma
  geometry is **not** simply the per-macroblock luma `dct_type`. Do not extrapolate these seam
  findings to U/V; chroma needs separate geometry and performance evidence.
- Richer metadata is justified only if current indexes demonstrably fail predeclared gates. Do not
  propose index-format extensions or an ad hoc pixel-only detector (D-24 family restriction) from this
  note.
- `TEST_6A_home_576i` and `TEST_7A_home_576i` original/blocky pairs are four distinct media hashes
  after duplicate aliases were removed (20 total `*.mpg`, no duplicate content at last check). They
  are **not** admitted P0 members and remain role-unassigned. Hash prefixes: 6A original
  `0F8656F69591EC69`, 6A blocky `0D53680AB8037FDA`, 7A original `C68E209FDE087D7A`, 7A blocky
  `17ABBC2C4EEB85AF`. All four **were** committed in interim snapshot `6b7acc3`, contrary to the agreed
  separate bounded commit shape; their history permanence and any later privacy or role decision must
  be handled independently of P0. They are roughly five to seven times longer than any current pool
  member, so unnormalised weighting would let 6A outweigh all four existing content groups combined.

### 12. Stage 1 index record structure, and what it cannot express

**Evidence class: RATIFIED MECHANISM / verified from source. Destination: reference detail for the
Evidence Report; already consistent with `02_INDEX_FORMAT_SPEC`.**

The per-macroblock record is **8 bytes**, `struct.Struct("<8B")`, decoding to: `transform`, `coding`,
`q`, `q_update`, `cbp`, `motion_type_raw`, `motion_dir_bits`, and a packed byte carrying
`motion_source` in bits 0-1 plus the `valid`, `q_inherited`, `pred_derived` and `dct_read` flags.
Mappings: `TRANSFORM = {0: NONE, 1: FRAME, 2: FIELD}`, `CODING = {1: SKIPPED, 2: INTRA, 3: INTER}`,
`PICTURE_TYPE = {1: I, 2: P, 3: B}`.

**There are no motion-vector components.** This is the hard boundary behind section 7's limitation:
the index can flag that a block is prediction-only and whether motion was signalled, but **cannot
locate** the inherited grid. Any proposal to capture vectors meets D-13's higher bar.

File layout: 32-byte header with magic `S1MBIDX1`, `struct.unpack("<8sHHIQII")`, endian marker
0x01020304 and a complete flag in bit 0; then per output frame a 64-byte record header (magic `FRM1`,
ordinal, picture type at byte 30, macroblock count as uint32 at offset 40) followed by 8 bytes per
macroblock. Size is `32 + N * (64 + MBs * 8)`; records are in **display order**, one per output frame.
At 720x576 that is about 13 KB per frame, so the much longer 6A/7A clips would produce indexes in the
10-20 MB range.

The only readable text in an index is the magic `S1MBIDX1` - no paths, no names - which is why index
bytes are machine-independent and are **not** Restricted Media.

### 14. Cross-platform index determinism, and the eight index identities

**Evidence class: CLAUDE RECOMPUTED plus owner-run Windows confirmation. Destination: S2-I3 Evidence
and Gate Report; relevant to Stage 1 evidence provenance.**

Claude derived the eight development index SHA-256 values independently on Linux, using a `gcc -O2`
build of the frozen inspector sources, before any Windows run existed. The owner's Windows run, using
the MSVC-built frozen inspector, generated six of them and **reproduced every value byte-for-byte**,
along with frame count, geometry and P-skip count.

| Label | Frames | Geometry | P-skips | Index SHA-256 |
|---|---:|---|---:|---|
| XP | 228 | 720x576 | 1619 | `4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127` |
| XP_blocky | 228 | 720x576 | 25635 | `8d0326b5975b19b36742717a80be9eaf11bc21f379f2855eb22651e94dd16b20` |
| SP | 192 | 720x576 | 1764 | `40a97ce1a9920cd63e45da13371e0b41ff1619fed688d6145899a300463cc5d9` |
| SP_blocky | 192 | 720x576 | 19010 | `7e19ca6078075e7bf7a3a34bcda0816267e4d38ad02a56e01b6b0ed726ace746` |
| LP | 204 | 720x576 | 1533 | `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011` (frozen baseline) |
| LP_blocky | 204 | 720x576 | 20300 | `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238` |
| TEST 3A | 300 | 704x576 | 8812 | `9a60a8d24a7e4a45cbe82b4f41d232ede0e5c00624e82a8f8099f61351957f33` |
| 3A_blocky | 300 | 704x576 | 18190 | `e6f556dd4aaed0f4709b7c011fcf045193dccbb8abd2a01c646dddf0da893c83` |

Also measured by Claude but **not** a P0 member: `LG_576i_5_MLS_blocky.idx`
`915bee8ce95ea9fa58d283b38ba445427a7ab7402ee15e71e6c9dd38ab46d1da`.

**Finding: the frozen inspector is deterministic across compiler and platform**, and the index format
serialises no machine-dependent field - consistent with the magic being its only readable text.
Qualify this as holding **within these samples**; it is not a proof for every MPEG-2 stream.

**Q_fixed values**, the all-macroblock median effective quantiser used as the fixed-QP control: **XP
14, SP 16, LP 18, TEST 3A 14**, and **62 for every `_blocky` encode**. These are measured source
properties, not tuned results.

**A pair must never be assumed to share geometry.** `LG_576i_5_MLS_blocky` is **352x288 with
`progressive_frame=0`** while its original is 352x288 progressive - the pair cannot be used for paired
metrics without resampling. Always verify frame count **and** geometry for both members of any pair.
This is the generalisable trap, and it is why P0's structural checks test both members.

### 15. Operational knowledge that would be expensive to rediscover

**Evidence class: verified operational fact. Destination: role handovers and operational evidence.**

- **Embeddable/isolated Python does not add the launched script's directory to `sys.path`**, and
  **ignores `PYTHONPATH`**. Claude verified both: under `-I` the plain invocation fails with
  `ModuleNotFoundError` for the sibling module, and setting `PYTHONPATH` does **not** fix it. Explicit
  `sys.path.insert` is the only route. The owner's VapourSynth interpreter is exactly this case
  (`python314._pth`, `sys.flags.isolated=1`, `sys.flags.safe_path=True`). **Test every script
  invocation under `-I` as well as plain before clearing it.**
- The project's own `.vpy` adapters already solve this internally with
  `HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))`. Adding that idiom to a test
  module makes it robust under any interpreter - the more idiomatic long-term fix, deliberately not
  taken mid-run to keep the Python files byte-identical to the rehearsed set.
- **Reproducibility caution.** When re-testing that a unit suite fails closed, inject the failing test
  **before** the trailing `if __name__=='__main__': unittest.main()` line. Claude's first attempt
  appended after it, so the injected test was defined after the suite had already run and exited, and
  the run reported success. The fix is sound: a failing assertion, a syntax error and a missing
  sibling module each give a non-zero exit through `runpy.run_path`.
- **BestSource writes cache files outside the working tree** (on Linux, under a `bsindex` directory
  keyed by the media path). These are decode indexes, not pixels, but they are derived artefacts that
  should be removed along with media after any rehearsal. Claude deletes them and verifies none remain.
- **CMD traps** that have each cost real time: no two processes appending to one log; no digit directly
  before `>` or `>>`; **no unescaped `(` or `)` inside a parenthesised block's echo text**; `for /f`
  does **not** set ERRORLEVEL from the command it runs, so clear the target variable first and gate on
  `if not defined`; every `exit /b` should print a reason.
- **`git diff --cached --check` must not be used as a STOP gate.** It fails on the legitimate CRLF
  evidence files under `experiments/stage2/results/` and on Markdown two-space hard breaks.
- **`core.autocrlf=true`** on the owner's machine means `.py` and `.md` are stored LF in Git and appear
  CRLF in the working tree, so **every hash statement must name its representation**. Worked example:
  `stage2_index_reader_v0_2.py` is CRLF `139f02c6...` in the working tree and LF `f9892039...` in Git.
- The **BestSource plugin binary** used for the owner's P0 run is bit-identical to the one recorded in
  the accepted S2-I2 evidence (DLL SHA-256
  `fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c`, `PluginVersion(22,0)`). NumPy
  moved 2.5.3 to 2.5.4, which is immaterial to exact-integer work but belongs in the provenance record.

### 16. Correction history - Claude's own errors, recorded deliberately

**Evidence class: process record. Destination: role handovers; summarised in the Evidence Report's
provenance.**

Three of the four MUST findings against the rejected `Stage2_Interim_Findings_v0_1` were corrections
to **Claude's own** material, not ChatGPT transcription errors. Recorded so a successor understands why
the corrected values are the trustworthy ones.

1. **Inverted boundary direction (M1).** Claude described the `neigh_v` statistic as "vertical seams",
   when those pairs are stacked macroblocks sharing a **horizontal** boundary. The magnitudes were
   right; the label and therefore the mechanistic interpretation were wrong.
2. **Unstated denominator (M2).** Claude's percentages silently excluded all `NONE`-involving pairs.
3. **Mis-located measurement band (M3), which reversed a published conclusion.** Claude's band used a
   frame-line 8-pixel grid, correct only for FRAME-DCT macroblocks, in sources that are 53% to 73%
   FIELD. The corrected per-macroblock measurement shows two to three times the signal, so the
   "paired MAE is a weak objective" conclusion was withdrawn.
4. **Rediscovery of accepted knowledge (M4).** Claude presented as a finding what the project had
   accepted as **K-03** since 2026-10-08.

**Root cause.** Claude measured, concluded and relayed into a repository-document proposal **without
first checking the findings against `06_DEBLOCK_CONCEPT.md`**. The P0 code track, which has a review
gate, produced no comparable errors.

**Standing rules adopted as a result**, now in Claude's handover: check any finding against the
existing K and O items before describing it as new, and offer a confirming measurement as an
**evidence-level upgrade** rather than a new K item; and keep exploratory measurements in review
correspondence until a gate report needs them.

A separate Claude error of a different kind: the **S4 recommendation** to run the new unit tests under
the VapourSynth interpreter was correct in intent but verified inadequately - Claude tested
absolute-path invocation with a **non-isolated** interpreter while recommending one that is isolated by
default, having already seen `python3 -I` fail earlier in the same session. The lesson is in
section 15.

### 17. Why S2-I3 needed a new admission test, and what S2-I2 still provides

**Evidence class: CLAUDE MEASURED, plus accepted S2-I2 evidence. Destination: S2-I3 Evidence and Gate
Report.**

**The S2-I2 phase-contrast gate cannot admit the wider pool.** Run as a diagnostic over the eight
development sources, its original thresholds report **PASS** for XP, XP_blocky, LP, LP_blocky and
3A_blocky, but **BLOCKED** for **SP, SP_blocky and TEST 3A**. Claude established that these blocks
arise from **test preconditions, not misregistration** - the same three sources pass exact P-skip
identity at 100%. This is precisely why S2-I3 adopted the identity test, and it is why the S2-I2
diagnostics are **descriptive only** in S2-I3. A historical BLOCKED value is **not** a P0 failure.

**The S2-I2 numerical engine is sound and reusable.** `stage2_registration_stats_v0_1.py` is generic
across MB-aligned sizes, 704 width and leading B pictures, and S2-I3 reuses it unchanged. Claude
confirmed reuse fidelity directly: re-running the engine through the new S2-I3 adapter on LP and
LP_blocky produced CSV outputs **byte-identical** (after line-ending normalisation) to the committed
Windows S2-I2 evidence - all eight CSVs per source.

**What could not be reused:** the S2-I2 *adapter* hard-codes its label as
`'LP_blocky' if stem endswith '_blocky' else 'LP'`, so every source would be mislabelled LP; and the
S2-I2 BAT accepts only LP or LP_blocky. Hence the new per-source diagnostic adapter.
`stage2_check_result_v0_1.py` must **not** be used as an S2-I3 gate.

**Also from S2-I2, resolved and worth keeping:** the M4 discrepancy was settled - the engine is correct
at 23.79%, and the earlier 47% preview used adjacent-slope comparators, recorded separately as the
**M4a** proposal. And the BestSource/FFmpeg agreement claim must stay at its corrected strength:
byte-identical CSVs are **strong evidence of decoder agreement, not pixel-by-pixel proof**.

## 10. Cross-role v0.5 review additions, interpretation corrections and S2-I4-only questions

**Appearance instrument versus population sample (SHOULD S3).** The blocky/original pair is a controlled mechanism/appearance instrument: its known frame correspondence provides an original encoded reference at the candidate seam. It is **not** an empirical sample of how often/severely real captures exhibit blocking. A separate n-weighted joint-coding census in Claude v0.5 shows a coded residual transform in only **26.3%, 32.4%, 26.3% and 40.1%** of XP_blocky, SP_blocky, LP_blocky and 3A_blocky, versus **83.1%, 79.3%, 75.2% and 76.0%** in the corresponding originals. The synthetic Q62 encodes must not determine real-world prevalence or frequency weights. They remain valuable as a paired visual appearance, contrast and no-harm instrument. The owner did **not** approve a change to the ratified original:blocky 2:1 weighting. Claude's v0.1 allegation about damage originating in the originals and v0.3 criticism of the interim document's NONE denominator were **withdrawn**; the interim decomposition is correct. "Inherited" in K-08 means from preceding pictures **of the same transcode**; source damage is not asserted. Off-grid displacement is possible for motion-compensated residual-free blocks, **not proven** by their NONE label.

**Data classes must not be merged.** In the interim bridge section 7, "Skipped in P" percentages **1.9%-9.4% use NONE as denominator**; the v0.5 review's total SKIPPED census sums P plus B and is a different statistic. Similarly, the bridge's 90.2% whole-clip vertical fault and Windows 93.08% per-block horizontal control are complementary rather than rival measurements. These corrections are explicit to prevent recurrence of M1-M4 provenance defects.

**Quantiser observations; forward note only (SHOULD S4).** Across original development captures, the non-linear `q_scale_type` mapping was observed; `quantiser_scale_code` 1..31 maps through the linear table (ceiling 62) or nonlinear table (ceiling 112). LP has **4.23%** of its macroblock-edge weight above 62, with a severe ceiling spike (**49,113** observations at 112 versus **1,518** at 104). XP and SP reach 72 at 0.11% and 0.20% of edge weight; 3A reaches 56. This is a quantiser-saturation limitation for **future real-QP S2-I4**, not P0 or fixed-QP P1. Confirm whether `q_scale_type` is recoverable from existing indexed metadata and whether its omission has any practical effect **before** any proposed metadata extension, under D-13; do not presume it absent solely from a partial byte-layout inspection.

**Descriptive diagnostics (SHOULD S2).** The exact `known_bad_offsets.csv` source rule is `caught = (cx == 0 and ry == 0) or any(gate != 'PASS' for gate in ('shift','column','row'))`. Its zero-offset row is a control/reference recorded as True by construction; it is not evidence that zero offset was rejected. `auc_proxy=NaN` in all eight diagnostic CSVs remains a descriptive implementation follow-up (OPTIONAL), without impact on the P0 gate. Other MUST-free P0 SHOULD S1 is satisfied by section 5.1's **two distinct** 90.2% and 93.08% results.

**Future hypotheses, not authorised changes:** mixed seam orientation may change the incremental value of indexed geometry more strongly on horizontal than x=8 vertical boundaries; evaluate intermediate-QP encodes only under approved study design rather than treating Q62 variants as independent captures; retain source-separated I/P/B and NONE classes, no-harm collateral assessment, chroma-specific geometry and parity-safe access as subsequent Stage 2 requirements. Neither Stage 1 regeneration nor an `.idx2`/vector extension is authorised here.

## 11. Remaining uncertainty, negative findings and audit integrity

- **P0 is luma-only** and validates structural/temporal/skipped-P identity within eight allow-list development sources, not field parity identity. Independent verification is against the complete P0 137-file evidence, not an invented additional decode run by this report's author.
- **No filter quality improvement** has been demonstrated; neither unfiltered-vs-filtered visibility nor off-seam collateral change was measured by P0. Even the exploratory fixed-geometry blur results are **not** candidate index-directed filter results.
- Geometry-blind global original/blocky difference cannot replace FRAME/FIELD-aware seam-local analysis; the old 7-10% interpretation is withdrawn. The paired-reference original is higher quality **encoded** MPEG-2, not lossless ground truth.
- Even though P0 `READY_FOR_P1` is true numerically and the owner ratified its gate PASS, P1 requires a **separate owner authorisation**. EP / TEST 2A / TEST 4A (including blocky variants) remain protected until S2-I8; 6A/7A have no P0 admission or assigned future role.
- The observed cross-platform `.idx` agreement is bounded to these sources. The index does not store motion-vector components. It cannot by itself prove how many inherited steps are actually displaced.
- Stage 1 frozen baselines remain frozen. D-09 requires frame-owned processing and parity-aware sample access; no experimental finding in this report changes that invariant.

## 12. Permanent-transfer and document-control status

**Evidence Report** (this file): ratified project record, installed in a separately bounded report-only commit (**1 A / 0 M / 0 D**); no source media, P0 scratch archive, candidate ZIP, review correspondence or candidate patch belongs in the repository. The SHA-verified seven indexes are already installed under commit `35923a5`; do not stage them again.

**Concept authority:** the separately reviewed `06_DEBLOCK_CONCEPT.md` v1.3 revision carries narrow empirical annotations to **K-03/K-07/K-08**, with its own owner ratification and distinct installation commit. At this report's initial installation, the preceding v1.2 remains authoritative until that separate v1.3 commit is installed. No change is made to open O-04/O-09/O-14/O-15 or D-09/D-13/D-24/D-25/D-26. No new K-item is added.

**Operational transfer:** Annex 15 facts (isolated Python, filename imports, Git line endings, CMD and review artefact hygiene) still need deliberate incorporation/acknowledgement in the next **role handover** revision, rather than being mistaken for a new filtering rule. Record approved Git commit IDs in an updated knowledge-transfer matrix when the owner installs the evidence report and concept revision.

**Bridge retention:** `docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md` stays present until Claude independently checks completeness of the transfer, the owner ratifies it, and any remaining operational and future-design references are assigned durable destinations. Its section 10 operational snapshot (XP alone REGISTERED and remaining P0 stages outstanding) is historical, superseded by this report and Windows status v0.4; its empirical and methodological sections remain relevant pending full transfer. Then retire it by a separately authorised exact-path D-23 cleanup, not before.

## 13. Provenance and correction history

1. Ratified source designs: `docs/REPOSITORY/Stage2_Experiment_Design_v0_7.md`; `docs/REPOSITORY/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md`; `docs/REPOSITORY/05_DECISIONS_v1_2.md`.
2. Prior accepted gate: `docs/REPOSITORY/S2_I2_Evidence_and_Gate_Report_v0_1.md` (a distinct S2-I2 gate, not reused as P0 admission).
3. Reviewed full P0 evidence: `docs/Claude_P0_EVIDENCE_REVIEW_AND_GATE_RECOMMENDATION_v0_5.md`; earlier review revisions v0.1-v0.4 contain corrected commentary and must not override v0.5.
4. Owner Windows observational record: `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_4.md`, whose pre-acceptance and pre-cleanup "next actions" are historical, not current.
5. Interim empirical consolidation: `docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md`, whose corrections M1-M4 and annex methods are preserved here. Do not seek a nonexistent Claude paired-analysis v0.3, and do not quote the superseded v0.2 boundary and interior figures as valid measurements: the corrected, geometry-aware figures and the explicitly marked invalid old interpretation are in section 9.
6. Owner ratification on 2026-10-18: P0 gate PASS; the independently reported evidence is ACCEPTED. Accepted code and seven `.idx` commits are already in Git history and not staged by this draft.

## 14. Change log

### v0.1 - 2026-10-18 (RATIFIED; initial report installation)

- Synthesises ratified P0 PASS and independently reviewed 137-file evidence, with 8 exact admissions, 4 pair PASS outcomes, runtime, checks, negative controls and limitations.
- Preserves corrected quantitative and conceptual research in detailed annexes instead of re-opening K-02/K-03/K-07/K-08 or inventing filter thresholds.
- Carries all four Claude v0.5 SHOULD observations and both complementary 3A negative-control measurements.
- Leaves P1, hold-outs, interim retirement, metadata expansion and production-filter decisions unauthorised.
