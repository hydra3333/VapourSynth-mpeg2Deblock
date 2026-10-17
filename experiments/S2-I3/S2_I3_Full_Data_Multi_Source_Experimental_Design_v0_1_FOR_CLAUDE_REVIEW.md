# S2-I3 - Full-Data, Multi-Source Luma Kernel Experimental Design

**Filename:** `S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_1_FOR_CLAUDE_REVIEW.md`
**Version:** 0.1
**Date:** 2026-10-17 (Australia/Adelaide)
**Author:** ChatGPT, drafting for the project owner and independent Claude review
**Status:** DISCUSSION/REVIEW DRAFT ONLY. Owner authorised S2-I3 DESIGN PREPARATION, NOT implementation. NOT RATIFIED. No repository authority modified.
**Verified repository baseline:** `6e7b5c53df1c65775524936fc945c449cc9fa100`; S2-I2 CLOSED/PASS.

## 0. Purpose and decision boundary

Develop a practical, index-directed MPEG-2 luma deblocker from **the available real decoded recording data**. Use complete quality-eligible frames during the main development experiments; do not choose favourable frames, impose one recording's GOP partitions on another, or replace actual index geometry with a synthetic model. Include independent supplemental split-data checks and broader cross-source evaluation rather than making a reduced development subset the primary engineering path.

This document is a proposal to CHANGE a part of ratified `Stage2_Experiment_Design_v0_6.md` (notably sections 3, 8.4, 10, 14 and 19). That document currently reserves even usable LP GOPs for selecting K0 and odd GOPs for S2-I4 fixed-QP versus indexed-QP evaluation. The owner has authorised drafting an alternative, not silently superseded the ratified design. Claude shall review the conflict and identify the required formal ratification/change procedure **before any implementation or viewing filtered hold-out results**.

No S2-I3 software, sample indexing, filter execution, source selection by test outcome, Stage 2 authority edit, S2-I4, or S2-I8 is authorised by this draft.

## 1. Authority, provenance and fixed constraints

Controlling technical sources at the verified baseline:

- `docs/REPOSITORY/Stage2_Experiment_Design_v0_6.md` (especially sections 1, 3, 4, 5, 8.4, 9, 10, 13-15 and 19).
- `docs/REPOSITORY/05_DECISIONS_v1_2.md` (D-07, D-09, D-10, D-12, D-13, D-23, D-24, D-26).
- `docs/REPOSITORY/06_DEBLOCK_CONCEPT.md` (v1.2), `02_INDEX_FORMAT_SPEC.md` (v0.4 constraints), Stage 1 frozen evidence, S2-I1 and S2-I2 installed evidence/gate reports, and `NOTICE.md`.
- `docs/Claude_S2_Seam_Pixel_Test_Options_Table_v0_2.md` is a NON-AUTHORITATIVE options register, not a new decision. Proposed M4a is an addition, not an amendment to ratified S2-I2 M4.
- Earlier `S2_I3_Entry_Plan_v0_1_FOR_DISCUSSION.md` reflected the OLD even/odd restriction and is superseded **for this proposed design only**, not as a repository authority.

Hard technical invariants inherited unchanged:

1. **Index-driven Family A**: index gives eligible geometry; decoded pixels decide blocking resemblance, flatness and no-harm. Never infer FRAME/FIELD/NONE or move seam coordinates from pixels (D-24). No required pixel-only Family B benchmark; Family C is optional, non-blocking research.
2. **Frame-owned** processing with same-field-parity access wherever interlaced horizontal filtering would mix fields; preserve `progressive_frame` per picture; do not process field pictures in this prototype (D-09).
3. **Actual coded geometry**: FRAME/FIELD/NONE retain authoritative meanings; NONE has no coded internal residual seam, though outer MB edges may remain candidates. Never interpret absent `dct_type` as NONE. No filter support crossing another known transform seam.
4. **First metadata set**: effective QP and transform state, plus required index validation/picture flags. B0 (no extra coding-context boundary-strength input) is the default. B1 would add coding-state/CBP use as a filtering input beyond D-13 and needs separate owner authorisation; this draft does NOT authorise B1.
5. **A bounded, edge-protected, QP-scalable short-support luma kernel**, constrained output/sample range, deterministic operation, single manual global strength, OFF bit-exact. No chroma, C++ production plugin, AVX2, motion vectors or additional Stage 1 metadata work in S2-I3.
6. **Leading-B exclusion**: process/validate frames before the first I picture, but exclude those leading B pictures from quality tuning/aggregates and visual selection. Do not infer all frames are eligible solely from frame count.
7. **Protected hold-outs**: `LG_576i_4_EP` original, `TEST_2A_A001` original, `TEST_4A_A003` original must not enter S2-I3 development, comparison-driven selection or filtered-output browsing. The six accepted `.idx` files are immutable. Derived scratch indexes never become accepted baselines implicitly.
8. **Evidence and media**: preserve text/numerical evidence and provenance; actual recordings and picture-like filtered visuals are Restricted Media as governed by `NOTICE.md`, irrespective of output extension. No casual Git inclusion or external transfers.

## 2. Explicit owner-preferred experimental principle

Primary engineering method:

`characterise all -> optimise on all eligible REAL recording frames -> measure all -> report separately and jointly -> inspect generalisation -> freeze a bounded K0`

Here **all** means the complete quality-eligible population of each recording assigned to an experiment, not the protected hold-outs and not excluded leading B pictures. No cherry-picked development intervals, forced correspondence between unrelated GOP numbering, artificial training pictures or proxy observations substituted for pixels. Exact full-frame populations, omissions and preflight failures shall be recorded in a manifest.

The owner additionally requests even-versus-odd evaluations and supplementary reduced-subset training runs **for comparison**, not as a prerequisite that limits all-data development. Results on frames used to develop a candidate are explicitly **in-sample**, even when displayed separately for even and odd GOPs. Supplemental cross-fold results may provide partially out-of-training evidence, but not across an independent recording. These labels must travel with every report.

## 3. Sources and proposed roles

### 3.1 Primary full-data development, three paths

| Path ID | Kernel identity | Development inputs | Initial fixed-QP value(s) | Purpose |
|---|---|---|---|---|
| A | K0-A | ALL eligible `LG_576i_3_LP.mpg` frames | LP = 18 | Real LG baseline / detail-preservation optimisation |
| B | K0-B | ALL eligible LP AND ALL eligible `LG_576i_3_LP_blocky.mpg` frames, each on its native index/GOP structure | LP = 18; LP_blocky = 62 | Balanced joint optimisation; seek stress resistance without harming original LP |
| C | K0-C | ALL eligible LP_blocky frames | LP_blocky = 62 | Severe-blocking stress-specific optimisation and sensitivity reference |

The LP values above use the ratified Stage 2 fixed-QP definition: median **of all macroblocks** in each clip, including NONE. For original LP, Q_fixed = 18; the alternative coded-only median 16 is NOT substituted. LP_blocky has verified constant effective QP 62. Q_fixed is not recalculated from a filtered-result-selected frame subset. If the accepted index contradicts any declared value, stop and refer to Claude/owner.

Use real decoded pixels and each source's actual transform geometry, picture flags and GOP structure. A fixed-QP *control input* does not mean synthetic video or fabricated geometry. For B, declare source-balanced aggregation (initial proposal: equal per-source weight in the selection judgement, with each source's separate raw scores visible). Never let an accidentally larger seam/frame population silently choose the outcome. The weights/selection process must be locked **before** candidate scores are examined.

### 3.2 Three additional same-dimensions, different-content blocky evaluation sources

| Source (nominated) | Proposed role | Current verification status |
|---|---|---|
| `LG_576i_1_XP_blocky.mpg` | Extra LG XP-mode stress/generalisation, evaluation only | File name known; dimensions, index and characteristics NOT verified in this draft |
| `LG_576i_2_SP_blocky.mpg` | Extra LG SP-mode stress/generalisation, evaluation only | Same preflight outstanding |
| `TEST_3A_A002_blocky.mpg` | Different TEST-series content stress/generalisation, evaluation only | Same preflight outstanding |

The owner states that each LG `_blocky` recording differs and each TEST `_blocky` differs. Do not assume that the names prove matching dimensions or index compatibility. The intended comparison target is LP's **720x576 coded/decoded luma geometry**. Before granting an evaluation role, measure decoded width/height, frame count, format, `progressive_frame` and picture-type properties; obtain and validate a matching index and S2-I2-equivalent spatial-registration controls. Indexes not already tracked are non-baseline SCRATCH only, with their own hashes. A low-blocking source may provide weak spatial-phase contrast; do not silently waive checks or apply LP-tuned thresholds blindly. Escalate an ambiguous failure.

If any nominee is not 720x576 or otherwise unsuitable, report **NOT ELIGIBLE** with evidence; do not auto-replace it with a protected hold-out, rescale video, crop it to force compatibility or invent a fallback. Claude and the owner decide any replacement. These extra sources are evaluated after candidate and K0 freeze **without retuning**. They are not promoted to independent held-out real-recorder evidence under S2-I8 automatically.

Where corresponding higher-quality originals are available, original/blocky paired-reference metrics are permissible only after proving frame correspondence; interpret as movement toward the higher-quality decoded source, not restoration ground truth. Their originals are NOT automatically tuning/hold-out material. Do not consult original 2A/4A/EP hold-outs.

### 3.3 Protected and future sources

- `LG_576i_4_EP.mpg`, `TEST_2A_A001.mpg`, `TEST_4A_A003.mpg`: LOCKED (S2-I8 after explicit authorisation and freeze).
- `LG_576i_5_MLS.mpg`: progressive/control under the ratified later-stage plan; not silently S2-I3 tuning.
- Existing 2A/4A blocky paired-reference samples retain their existing later-stage roles; this experiment does not use them to bypass the corresponding locked originals.
- The owner's proposed all-16-source census at S2-I8 is a future addition to ratified v0.6, not a license to run all sources during S2-I3.

## 4. Supplementary split-data sensitivity (additional runs)

These runs supplement A/B/C, not override the all-data preference:

| Track | Develop kernel using actual material | Evaluate frozen kernel on actual material | Claim |
|---|---|---|---|
| D | LP even usable GOPs | LP odd usable GOPs | Out-of-training GOPs within the SAME recording |
| E | LP odd usable GOPs | LP even usable GOPs | Reverse-fold sensitivity |
| F (optional) | LP_blocky even usable GOPs | LP_blocky odd usable GOPs | Native-structure blocky sensitivity |
| G (optional) | LP_blocky odd usable GOPs | LP_blocky even usable GOPs | Reverse blocky sensitivity |

Use native display-order GOPs for each source. For LP, the accepted historical manifest reports 17 usable GOPs: even 9 GOPs/106 frames, odd 8 GOPs/96 frames, after the two leading-B exclusions. Reconfirm from the frozen index before running; never assume LP_blocky has identical GOPs (it does not).

For D/E select and freeze independent candidates from only their respective training fold; show fold-specific training quality and held-out-fold performance. Do not later claim A/B/C's even and odd outputs are out-of-training evaluations: A/B/C saw both. In B/C, LP_blocky is a re-encode of related LP pictures; ordinary GOP splits **do not prove content independence** and cannot be labelled wholly independent validation. Report this limitation, but do not force blocky frames into LP GOP buckets or discard authentic frames merely to mimic a split.

No result from D/E/F/G may be used to change the A/B/C protocol after looking at the results. The split tracks are sensitivity/quality-assurance evidence, not a hidden way to retune the main result. If a fold exposes instability, report it even if full-data development scores are good.

## 5. Candidate inventory and bounded research process

Preserve, screen or explicitly defer *every* option in Claude's v0.2 register, with the proposed M4a included in the next reviewed register. No silent deletion and no full Cartesian explosion.

| Category | IDs | Planned handling |
|---|---|---|
| Seam-step measurement | M1, M2, M3, M4, **M4a proposed**, M5 | Screen all on source-complete real pixels in both orientations; keep ratified S2-I2 M4 definitions unchanged |
| Side flatness/activity | F1, F2, F3 | Compare objectively and for noise sensitivity |
| Decision rule | R1, R2, R3, R4 | Small declared shortlists; genuine-edge/no-harm controls essential |
| Coding-context input | B0, B1 | **B0 first and default**; B1 separate future owner decision; no silent use |
| Threshold source | T1, T2 | T1 default; T2 H.264 tables only as hypothesis, never blindly copied |
| Real-edge protection | P0, P1, P2 | P1 cost/benefit comparison; P2 conditional on stronger no-harm evidence |
| Correction family | K1, K2, K3, K4 | Short-support K1 first; K2/K3 contingent; K4 optional Family C, cannot block S2-I3 |
| Aggregate diagnostics | G1, G2 | Optional read-only measurements; no per-seam decisions |
| Decision-only preprocessing | D0, D1 | D0 default; D1 only if justified without adding unbounded tuning |

Feature-screen using predeclared proxy metrics, including hit rate at a **fixed false-alarm rate** and area under the curve (AUC), by orientation, coded seam class, picture type, QP band and field parity as applicable. The S2-I2 statistical labels distinguish coding-grid boundaries from control positions; they are **not ground-truth labels of visible blocking**. Do not choose a filter solely because it detects more coding positions. Preserve frame/GOP-level uncertainty; individual pixel or seam counts are correlated.

Shortlist a small number (proposed 2-3) of COMPLETE M/F/R/T/P/K/B/D candidate combinations, with the same selection budget and comparable search space for paths A/B/C. Preserve all screened choices in a disposition register (screened, implemented, deferred, rejected and reason). Predeclare the selection rule before seeing comparative filtering outputs; combine seam improvement, real-edge/texture preservation, collateral change, visual judgement and consistency across original/stress paths. Do not invent a single objective score whose arbitrary weights silently override the owner's visual judgement (D-26).

One global manually supplied strength dimension shall be applied consistently; OFF must be byte-identical. Start with a bounded proposed strength sweep; exact levels and all threshold coefficients must be in a manifest and reviewed before code. Do not tune strengths separately to manufacture superiority of one path.

## 6. Execution and evaluation matrix

The implementation plan, if later authorised, would produce a reproducible serial campaign with clearly separated phases and outputs:

**Phase 0 - preflight (no filtering):** verify source SHA-256/identity, decoder and index correspondence, exact dimensions/formats, field-picture support, quality frame exclusions, native GOP lists, first/last frame, source-specific Q_fixed, row/column and shifted-label spatial alignment, and input/evidence permissions. STOP on unsupported/misaligned input, rather than forcing it through.

**Phase 1 - full-source baseline/characterisation:** every eligible LP and LP_blocky frame; unfiltered index-aware seam/no-seam activity, histogram and noise/QP/FRAME/FIELD/NONE/I/P/B reports. Produce source-separate and overall summaries. Read-only statistical census may characterise other nominated evaluation sources but MUST NOT influence pre-locked candidate selection if their outputs will be used as a generalisation test.

**Phase 2 - bounded feature screening:** same M/F screening definitions and implementation across the three full-data paths; statistical uncertainty by frame/GOP, avoiding naive seam-as-independent-sample inference. Unfiltered data only, no code modification after observing preview results without an explicit revised protocol.

**Phase 3 - full-data optimisation:** A LP-only, B LP+LP_blocky, C LP_blocky-only. Run selected complete candidate combinations at fixed QP, keep every result (including losses and zero-effect). Do not derive a K0 by pooling all blocky seams and overpowering original LP by count. Compare all three candidates on both LP and LP_blocky using a 3-by-2 matrix, reporting full source and native even/odd subdivisions.

**Phase 4 - supplementary splits:** D and E (and optionally F/G), with separately trained split-kernels. Report train/test difference and stability. No substitution of partial training for the primary A/B/C full-data method.

**Phase 5 - provisional selection and FREEZE:** the owner and Claude review A/B/C including the separate LP and LP_blocky outputs, no-harm evidence and visual results. Choose one frozen `K0` (or report that no acceptable kernel exists), with exact algorithm, feature IDs, parameters, strength, code hash, source manifest, weighting, Q_fixed definition and all-data development provenance. This is selection based on DEVELOPMENT evidence, not the three additional evaluation recordings. K0-A/B/C remain archived for contrast even if unselected. If results are genuinely Pareto-incomparable, report a trade-off and request owner decision; do not quietly select by an arbitrary final score.

**Phase 6 - extra-source evaluation ONLY:** apply all three already-frozen K0-A/B/C variants (and nominated winner K0) to all eligible frames of each validated XP_blocky, SP_blocky and TEST_3A_blocky candidate; no retuning or replacing test cases to improve outcomes. Report each source separately, along with native even/odd GOP subdivisions, differences and error cases. The moment results from these three are used to pick/revise K0, they become **selection evidence**; disclose the change, revoke their independent-evaluation claim and reserve fresh sources for a future unbiased test.

**Phase 7 - report/freeze gate:** complete all promised runs, publish numerical/textual metrics, negative and anomalous results, visual-owner decision record and provenance. Stop at S2-I3 review; do NOT launch S2-I4 without a separate owner authorisation and an explicitly revised S2-I4 control protocol.

The complete matrix is a proposed execution contract, **not** an instruction to start code or Windows test runs now. Serial execution is acceptable; runs may be orchestrated as one reproducible campaign after design approval.

## 7. S2-I4 implications: substantive protocol change requiring ratification

**Existing binding design**: Stage 2 v0.6 8.4/19 freezes K0 tuned on **even LP GOPs**, then tests fixed vs indexed QP on **untouched odd LP GOPs**. It is designed to avoid same-frame kernel-selection bias.

**Proposed new engineering question**: after the full-data A/B/C campaign, compare **the SAME frozen all-data-selected K0** at fixed median QP and real indexed per-MB QP, on identical LP frames; report all, even-only and odd-only results separately; use identical seam geometry, edge tests, strength and parameters; break down boundaries touching NONE, high QP disparities and QP 112.

This yields an interpretable **paired within-development-data comparison** of QP modes for the actually selected practical kernel. It is NOT an independently held-out estimate. Because K0 was selected using fixed QP, acknowledge possible bias toward fixed QP. The cross-fold D/E kernels, tested on their other fold under both QP modes, are a proposed *supplemental* sensitivity check addressing some same-GOP selection bias; they cannot turn K0's all-data result into a held-out evaluation. LP_blocky, with effective QP 62 everywhere, is not evidence that indexed spatial QP is useful.

**Required formal action before implementation/advancing to S2-I4:** Claude must review whether to amend the ratified Stage 2 v0.6 protocol, explicitly identify every consequential section/authority affected and obtain the owner's separate ratification. Until then, the existing even/odd S2-I4 contract remains the ratified authority. S2-I3 design preparation alone does not authorise deviation or implementation.

## 8. Measurements, acceptance and interpretation

Minimum source-separate reporting for each candidate/path/strength:

- Eligibility and exposure: eligible/excluded frames, native GOP counts, indexed seam counts by class, QP population, I/P/B and progressive/interlaced distribution; original LP even/odd breakdown.
- Read-only baseline, before/after boundary-step and activity measures, known-seam versus non-seam discriminability at declared false-alarm rate, frame/GOP uncertainty and score limitations.
- No-harm/collateral change: mean absolute output-input change; number and fraction of altered pixels; **off-support** change; natural-edge/texture change; corrections under each seam class; clamping/saturation behaviour. OFF is byte-exact and bounds safe.
- Actual-frame qualitative evaluation by project owner: matched representative moving-picture excerpts and stills, including flat/blocky regions, genuine edges, texture/noise, motion, FRAME, FIELD, NONE and different picture types; labels blinded/shuffled when practicable. Such excerpts remain Restricted Media under `NOTICE.md`.
- If a suitable decoded higher-quality source can be frame-matched, report paired MAE/MSE/PSNR seam-local and away-from-seam, **only as relative movement**, not pristine ground truth. Check cross-pair temporal correspondence independently of within-file index-to-frame validation.
- Failure handling: no accepted candidate is a valid negative conclusion; do not claim quality improvement from seam statistics alone. Unexpected field mixing, delocalised blur, cross-seam support, invalid alignment or reproducibility mismatch is a STOP for quality conclusions.

No numerical acceptance threshold is invented here. Claude and owner must ratify a pre-result candidate-selection/acceptance rubric balancing visible block suppression against real-detail preservation. The selection outcomes and objective measures must be published even when they conflict.

## 9. Traceability, outputs, and gate

Proposed deliverables **after a separate code authorisation**, not files generated by this design phase:

1. Manifest of SHA-256, clip format/dimensions, index hash, GOP definition and native grouping, QP population and value, leading-B exclusions, checked read-only Stage 1/S2-I1/S2-I2 baseline results, code/tool versions.
2. Predeclared feature/combination disposition table, fixed search budget, multi-source weighting/selection rule, no-harm rubric, qualitative review protocol, runnable command contract.
3. Complete A/B/C full-data results and per-source/per-GOP breakdown, D/E and optional F/G sensitivity, plus 3-by-3 candidate-to-extra-source evaluation if preflight passes.
4. Exact candidate K0-A/B/C identities and provisional selected K0 freeze manifest, with provenance and recorded owner ratification after the run. If none passes, failure report instead of forced winner.
5. Separate proposed S2-I4 protocol revision and outstanding S2-I8 all-16-census change, presented openly rather than enacted by implementation.
6. Human-readable summary of all caveats: known-seam proxies versus visible artefact truth; LP/LP_blocky content dependence; in-sample versus cross-fold versus different-content evaluation; dimensions/preflight unknowns; fixed QP versus real-QP control limits.

No new `.idx` may overwrite a Stage 1 accepted baseline. S2-I3 results are not a reason to rewrite completed S2-I2 metrics or the installed gate report. New documentation uses US-ASCII/CRLF under D-23 unless the owner grants a new exception (none proposed).

## 10. Explicit questions for Claude's independent review

**M1 (authority conflict):** Enumerate all ratified Stage 2 v0.6 clauses and D-13/D-26 implications that need owner-approved change for the full-data K0 and modified S2-I4 comparison. Would a staged appendix/amendment or a new version of Stage 2 be cleaner? Do not claim authority by merely updating this working draft.

**M2 (evaluation independence):** Is provisional K0 selection after viewing both LP and LP_blocky, but before viewing the three external evaluations, a defensible separation? Are the D/E controls properly described, given temporal and related-source dependence?

**M3 (preflight):** Verify from evidence, NOT filenames, that the three nominated `_blocky` recordings are 720x576, frame-picture supported and registrable. Identify minimal safe scratch-index steps and evidence needed. Do not request/transfer Restricted Media unless separately allowed and necessary.

**M4 (QP):** Confirm fixed QP all-MB median (LP=18; blocky=62), uniform on a clip, valid under multi-source weighting; identify if any Stage 2 source-specific changes are required.

**M5 (options and scope):** Ensure M1-M5 + proposed M4a, F1-F3, R1-R4, B0/B1, T1/T2, P0-P2, K1-K4, G1/G2, D0/D1 have a defensible screening/deferment protocol without premature silent deletion; confirm B0 default and that B1 requires explicit authorisation.

**M6 (practical engineering and QA):** Challenge hidden dataset selection, proxy-label reliance, similarity leakage, statistical pseudo-replication, filtered-output bias, edge/no-harm safety, prototype/Restricted Media rules, and the proposed freeze chronology. Recommend any bounded change before owner ratification.

**M7 (stage boundaries):** Preserve S2-I8 as locked hold-out generalisation/no-harm in current ratified v0.6; note that owner-requested all-16-source census is still proposed for a future authoritative revision. Do not accidentally advance later stages.

## 11. Change log

### v0.1 - 2026-10-17 (WORKING REVIEW DRAFT)

- First full-data S2-I3 design after owner-requested real-data, three-path LP/LP_blocky optimisation, split-data sensitivity and three extra different-content blocky evaluation nominations.
- Explicitly identifies conflict with existing even-GOP K0 / odd-GOP S2-I4 protocol for Claude/owner change control.
- Carries C-S1 (QP all-MB median), C-S2 (S2-I8 all-16-census proposal), B0 default and M4a as a proposed option.
- No implementation, sample role change in ratified authority, or S2-I4 authorisation.
