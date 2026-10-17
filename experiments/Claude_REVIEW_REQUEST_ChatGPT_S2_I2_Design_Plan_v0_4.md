# Claude Independent Review Request - S2-I2 Design Plan v0.4

**Date:** 2026-10-15  
**Status:** REVIEW CANDIDATE ONLY; no implementation, installation or owner Windows run requested.  
**Target:** Ratifiable S2-I2 design after resolving Claude v0.3 M1 and S1-S3. S2-I3 NOT AUTHORISED.

## Supplied files and authority

Read `ChatGPT_S2_I2_Design_Plan_v0_4_FOR_CLAUDE_REVIEW.md` in full. The accompanying `S2_I2_v0_4_CHANGE_TRACEABILITY.md` records changes against your v0.3 review; the diff is a convenience and does not replace the full design. `Claude_S2_Seam_Pixel_Test_Options_Table_v0_2.md` remains byte-identical to the previously supplied inventory. The SHA-256 manifest verifies packaged files. No executables, indexes, media or repository overlays are included.

Controlling project authorities remain Stage 2 v0.6, `05_DECISIONS_v1_2.md`, `06_DEBLOCK_CONCEPT.md` v1.2, `02_INDEX_FORMAT_SPEC.md` v0.4, frozen Stage 1 evidence and `NOTICE.md`. Historical S2-I1 commit `4221f7f...` and status v0.5 installation `2286341` are cited without claiming either is live HEAD.

## Exact review tasks

1. **M1 MUST:** Gate J now uses fixed 16-pixel interior, row q6/q7 aggregate top-two, `row_margin >=0.05`, and >=2/3 per-eligible-frame top-two support. Any *other* phase in aggregate top two => FAIL; insufficient margin/consistency/support => INCONCLUSIVE. Confirm +1/+2 row known-bad cases are detected, no 7|8 field mixing, and 3x3/column gates retain existing 10% conditions.
2. **S1 SHOULD:** Audit table of horizontal sample pairs for FRAME midpoint, outer MB boundary, 3|4, 11|12 controls and FIELD/NONE non-coded midpoint. Check in-block comparator pairs, parity, 8-column chunk splitting and equal 2 parity x 2 chunk weighting. Check vertical transpose (two 8-row field populations) and the exact plain/robust equations and signs.
3. **S2 SHOULD:** Preflight must be tiny `.vpy` invoked by the same `vspipe --info` executable/environment as actual BestSource run. It prints `sys.executable`, `sys.version`, NumPy/VapourSynth/BestSource versions to stderr, fails closed if unavailable, and does not guess Python paths. Please confirm feasible vspipe script semantics and version access before implementation.
4. **S3 SHOULD:** Statistics module imports NumPy but **not VapourSynth**, takes decoded per-frame Y arrays and accepted S2-I1 reader records, works both under FFmpeg replay and thin BestSource `.vpy` adapter; bounded memory (~1 GB), not seven full offset clips. This lets you independently execute the actual numerical code before the owner runs it.
5. **O1 OPTIONAL:** Status v0.5 recorded at `2286341` (pushed, not current HEAD assertion); manifest fixes the sign convention: `pixels moved right/down by k; index unchanged`, with `Y_shift(x,y)=Y_original(x-cx,y-ry)`. All seven known-bad offsets share an equal interior/test frame set.
6. **Regression of prior design:** Verify the original LP gate remains mandatory, LP_blocky separately indexed and non-baseline, all six accepted `.idx` immutable, structural preflights and descriptive M2/M4 both-orientation report (5% seam/control proxy FA, AUC, frame/GOP uncertainty) remain intact. These are **not** algorithm-tuning results, and no filtering or hold-out runs are authorised.
7. **Future option boundary:** All identifiers in the byte-identical options table v0.2 are retained for separate S2-I3/S2-I5 consideration. S2-I8 all-16 census after freeze remains future intent, not current test permission.

Please classify residual findings MUST/SHOULD/OPTIONAL with exact correction instructions, and say whether v0.4 is suitable for **owner ratification**. If clean and approved, implementation is a **separate** task. Claude rehearses/tests each tool and performs line-by-line BAT review before the owner's Windows run.
