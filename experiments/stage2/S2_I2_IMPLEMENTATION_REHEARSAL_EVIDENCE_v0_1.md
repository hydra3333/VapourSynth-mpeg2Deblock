# S2-I2 v0.1 - ChatGPT local execution evidence (NOT Windows acceptance)

**Date:** 2026-10-15  
**Status:** independent reviewer evidence; not repository technical authority, not owner acceptance.  
**Code:** S2-I2 candidate v0.1, pure NumPy statistics + FFmpeg rehearsal adapter.  
**Host:** Linux, Python 3.13.5, NumPy 2.3.5, FFmpeg 7.1.5. Windows 10/11 CMD, VapourSynth R81/BestSource and VS native inspector executable **NOT executed here**.

## Frozen-input and baseline checks

- The six-index S2-I1 v0.2 regression suite PASS (all six immutable hashes/totals and four negative mutations).
- Unmodified frozen inspector C source was compiled on Linux with compatibility headers; FFmpeg demuxed **regular-file** MPEG-2 ES, then frozen inspector generated LP_blocky index with SHA-256 `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238`. `stage2_validate_lp_blocky_v0_1.py`: PASS expected 204 frames, I/P/B 19/50/135, FRAME/FIELD/NONE 54292/33853/242335, QP 62 across 330480 macroblocks, no leading B. The index is scratch, not a seventh immutable baseline.
- Frozen LP tracked `.idx` SHA-256: `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011` (match).
- Synthetic no-media tests: PASS (offset sign, tie-aware AUC, proxy percentile, parity row/column phases, 5%-versus-10% gate separation, horizontal/vertical signed segment scores, outside aggregate row-phase FAIL and wrong-phase tie disposition).
- Both FFmpeg rehearsals compared every decoded-frame type/count/dimensions with the S2-I1 reader before any statistics. Each processed native yuv420p frames serially without writing decoded media, and used exactly the same NumPy engine as the proposed `.vpy` adapter.

## Registration outcomes: FFmpeg rehearsal ONLY

| Diagnostic | LG_576i_3_LP | LG_576i_3_LP_blocky |
| --- | ---: | ---: |
| Index/decoded frames | 204 | 204 |
| Excluded leading B (quality only) | 2 | 0 |
| Included frames | 202 | 204 |
| Raw C(0,0) | 5.9121 | 4.7161 |
| Best alternative raw C | 4.2721 | 3.0377 |
| 3x3 raw C gate (10% and >=2/3 frame wins) | PASS | PASS |
| Column margin (minimum 10%) | 35.15% | 46.00% |
| Column phase gate | PASS | PASS |
| Row margin (minimum 5%, q6/q7 rank and >=2/3 frames) | 11.48% | 25.24% |
| Row phase gate | PASS | PASS |
| All seven displaced-pixel controls caught by >=1 gate | YES | YES |
| Overall structural/registration rehearsal | **PASS** | **PASS** |

Expected negative-control coverage observed:

- +4 columns: **column-phase FAIL**;
- +8/+16 columns: **3x3 FAIL**;
- +1/+2 rows: **row-phase FAIL**;
- +8/+16 rows: **3x3 FAIL or INCONCLUSIVE** (on LP_blocky, +8 rows was INCONCLUSIVE; valid as a captured non-PASS under the ratified control criterion).

All results distinguish registration diagnostics from the non-gating boundary-strength report. The secondary LP_blocky cannot rescue a primary-LP failure.

## Descriptive seam/control separability (not artifact ground truth)

Below, *coded internal seam* rates pool FRAME/FIELD **within one clip and one orientation** for reporting only, with the ratified 5%-proxy-FA calibration performed separately for that clip/orientation/metric. The formal CSV retains separate FRAME/FIELD, picture-type and QP-band populations and actual achieved FA.

| Clip / orientation | Plain seam-proxy hit | Robust seam-proxy hit |
| --- | ---: | ---: |
| Original LP / vertical boundaries | 20.22% | 23.79% |
| Original LP / horizontal boundaries | 14.46% | 18.49% |
| LP_blocky / vertical boundaries | 50.85% | 45.29% |
| LP_blocky / horizontal boundaries | 30.93% | 30.29% |

**Independent review item:** Claude's earlier informal vertical-coded internal LP preview quoted ~20% plain and ~47% robust (both at 5% FA). The formalized implementation reproduced the *plain* rate approximately but **not** the robust preview figure (23.79% here). Differences in subpopulation, exact per-parity signed/comparator averaging, controls, decoder version or preview statistic may explain it, but none has been proven. Please inspect the code's precise M4 computation against the ratified v0.4 sampling contract and the preview definitions. Do **not** tune the S2-I2 descriptive measure or its threshold to reproduce an informal result. A discrepancy would be a reason to correct the code if the design was misimplemented, not to amend the registration acceptance gate. The earlier informal results are not a formal expectation or target.

## Output schema and restrictions

The local rehearsals produced CSVs for seam counts, the nine shifted-label contrasts for eight offsets, column and same-field row phases, all seven known-bad offsets, both-orientation descriptive detectability (fixed per-clip/orientation/metric control cutoff), frame/GOP descriptive quartiles, outer edges (with both neighbour coding states/transform/QP), plus an identity/threshold/offset manifest and a human-readable result text. No images or clips are included. Source video and generated `.m2v` are **Restricted Media** and not provided in the implementation package.

## Limits of evidence

- Linux FFmpeg rawvideo frames are a useful independent mechanical rehearsal but **not proof of Windows BestSource sample identity, stride handling, plugin loading, or vspipe output-setting behaviour**.
- Windows BAT redirection, file locks, arguments, tool paths and errorlevel decisions have not been executed under real Windows CMD here and require Claude's line-by-line audit and the owner's separately cleared run.
- No filter output, kernel tuning, hold-out test, all-16 census, production plugin or Stage 1 change was performed.
- Final owner acceptance still depends on BestSource's Windows results, Claude's review and the owner's explicit gate decision. S2-I3 remains unauthorised.
