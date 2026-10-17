# S2-I2 implementation v0.1 - design/code traceability for Claude

**Authority:** owner-ratified S2-I2 Design Plan v0.4 (2026-10-15); Stage 2 v0.6 remains the owning ratified experiment design. This file is review evidence, not new authority.

| Ratified requirement / Claude v0.4 finding | Implemented in candidate | Verification focus |
| --- | --- | --- |
| Frozen Stage 1 reader, exact LP/LP_blocky index identity | `stage2_registration_clip_v0_1.vpy`; `stage2_validate_lp_blocky_v0_1.py`; both BATs | No Stage 1 changes; six hash regressions; scratch candidate hash/counts |
| Known geometry and no internal seams in NONE | `stage2_registration_stats_v0_1.py`: `mb_labels`, `scored_segments`, `segment_category`; `seam_counts.csv` | Vertical FRAME/FIELD internal; horizontal FRAME internal only; NONE separate |
| Parity-safe horizontal pairs, vertical transpose | `_score_horizontal`, `_score_vertical`, `d_maps`, `phase_stats` | exact cross/comparator pairs and abs-after-signed-means within each parity/chunk |
| Raw D, D_norm, 3x3 contrast | `d_maps`, `contrast_for_shift`, `RegistrationRun.process` | fixed interior target MB lattice; no label mixing; frame-level support; pooled MB-weighted C |
| Column 0 phase +10% | `phase_stats`, `gates` | x = right-side column; 16-pixel interior; wrong peak vs ties |
| Same-field row q6/q7, +5%, >=2/3 | `phase_stats`, `gates` | q=y mod8; sample (y,y+2), no adjacent-field subtraction; fixed 16-pixel interior |
| Seven +pixel displacements, no wrapping | `OFFSETS`, `displaced`, `RegistrationRun.process` | controls +4/+8/+16 X and +1/+2/+8/+16 Y; any non-PASS catches |
| Both clips separate, LP primary not rescued | `S2_I2_run_registration_v0_1.bat`, `stage2_check_result_v0_1.py`, `RegistrationRun.finalise` | no implicit all; separate scratch output; each own disposition |
| M2/M4 both orientations, seam/control proxy, 5% FA, tie-AUC | `_score_*`, `scored_segments`, `percentile95_nearest`, `auc_rank`, `_detectability_reports` | evaluate exact signed arithmetic, controls and stratified thresholds; compare informal M4 preview discrepancy |
| Class/QP/I-P-B uncertainty; QP 112 isolation | `QP_BANDS`, `RegistrationRun._detectability_reports` | fixed `0-15/16-31/32-63/64-111/112/>112`, frame+GOP quartiles; no pseudo-independent segment CI |
| Owner NONE subdivisions 2026-10-15 | categorical mapping in `RegistrationRun.process`; `_none_subclass_name` in outer paired table | SKIPPED numeric enum 1, INTER 3; P/B distinct; outer two-neighbour QP/coding/transform |
| S1 preflight with `BlankClip.set_output` and plugin file SHA | `stage2_vspipe_env_preflight_v0_1.vpy` | no hardcoded Python path; missing plugin/version string handling; vspipe `--info` exits accurately |
| S2 read-only stride-correct luma/int16 and output `--arg` | `stage2_registration_clip_v0_1.vpy`; runner BAT | unmodified native plane0; 8-bit 420 only; no filtering; output from `--arg out=...` |
| Pure NumPy stats; independent FFmpeg rehearsal; bounded memory | stats engine separate from `.vpy`; `stage2_ffmpeg_rehearsal_v0_1.py` | FFmpeg 7.1.5 numeric rehearsal vs owner BestSource distinct; no media saved |
| Correct BAT generation and scratch isolation | `S2_I2_prepare_LP_blocky_index_v0_1.bat` | frozen inspector regular-file input; sequential appends; CMD digit-handle trap avoided; Restricted .m2v lifecycle |
| Numerical outputs, no Restricted graphics, no S2-I3 | `RegistrationRun.finalise`; README and ZIP audit | CSV/JSON/text only; no tuned thresholds, no hold-outs, no AVX2 plugin |

**Not carried forward into S2-I2 implementation:** S2-I3/S2-I5 algorithm options M1-M5, F1-F3, R1-R4, B0-B1, T1-T2, P0-P2, K1-K4, G1-G2, D0-D1 remain recorded in Claude's separate options table v0.2. S2-I8's eventual all-16 census remains a future owner-controlled gate. None of those futures is authorised by this candidate.
