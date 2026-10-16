# S2-I2 v0.4 - Claude v0.3 review resolution and continuity trace

**Status:** Review support only; not an authority or ratification.  
**Basis:** `Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_3_v0_1.md` plus complete v0.3 design. All v0.2 review findings and owner additions were already incorporated in v0.3 and must remain intact.

| Input | Specific issue | v0.4 design location | Resolution for Claude to verify |
| --- | --- | --- | --- |
| Claude v0.3 M1 MUST | 10% row-phase tie guard can make correctly aligned LP inconclusive | 3.4; gate J; 5.1, 6 | q6/q7 aggregate top-two, fixed 16-pixel border, >=5% row margin, >=2/3 eligible-frame top-two; outside aggregate top-two FAIL; other deficiencies INCONCLUSIVE. 3x3/column unchanged. |
| Claude v0.3 S1 SHOULD | Horizontal comparator pairs and segmentation implicit | 3.6; section 8 | Exact five-class horizontal table; lower-minus-upper, parity-safe comparator pairs; robust 2 parities x 2 8-column chunks; vertical transpose and per-field 8-row populations; M2/M4 math. |
| Claude v0.3 S2 SHOULD | Actual interpreter can differ from shell Python | 5; gate O; section 8 | Tiny `.vpy` run via same `vspipe --info`; stderr versions for sys/Python/NumPy/VapourSynth/BestSource; fail-closed and no guessed path. |
| Claude v0.3 S3 SHOULD | Need Claude to run real numerical implementation | 5; section 7/8 | NumPy luma arrays plus reader records; stats module no VapourSynth import; thin BestSource adapter; streaming per frame <=~1 GB; FFmpeg rehearsal with actual stats. |
| Claude v0.3 O1 OPTIONAL | Historical status commit and shift sign | Header, 0, 3.5, 5.1, 8 | Status v0.5 at 2286341; pixels right/down by k, unchanged index; `Y_shift(x,y)=Y_original(x-cx,y-ry)` in fixed common frame interior. |
| Prior Claude v0.2 M1/S1-S4 | Registration, D_norm, controls, LP_blocky identity and NumPy | 1.1; 3.1-3.5; 4.1; gates A-L | Retained; only row-phase margin corrected. |
| Owner additions | Separate LP/LP_blocky strength/detectability, both orientations and uncertainty | 1, 3.6, M/N, 5.1 | Retained: plain M2/noise-robust M4; 5% proxy FA, AUC, class/QP/type, no detector tuning. |
| Future scope boundary | Options M1-M5 etc. / all-16 at S2-I8 | 7 and attached options table | v0.2 options copied unchanged; S2-I3 not authorised; S2-I8 after freeze only. |

**Known prior informal numerical disclosure:** Claude saw FFmpeg-decoded LP and LP_blocky values before formal tests. Its v0.3-review LP row phase 16-pixel-interior margin was ~11.5%; central-half ~9.7%. These are feasibility observations, **not** formal BestSource acceptance data. Predeclared thresholds require owner approval before formal execution.

**Checklist for package review:** verify no source media, `.idx`, generated PNG, other Restricted Media or unrelated repository changes; all review files ASCII/CRLF except SHA manifest (also CRLF); quoted SHA values are assertions from Claude, not newly rerun Windows results.
