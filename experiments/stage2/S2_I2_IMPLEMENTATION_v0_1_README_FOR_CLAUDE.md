# S2-I2 implementation candidate v0.1 - instructions / boundaries

**Date:** 2026-10-15  
**Status:** UNRATIFIED IMPLEMENTATION CANDIDATE; CLAUDE REVIEW AND EXECUTE/REHEARSE FIRST.  
**Design:** ChatGPT S2-I2 Design Plan v0.4, ratified by project owner 2026-10-15, including thresholds and descriptive NONE subclass request.  
**History:** S2-I1 accepted at commit `4221f7f9f3c015da4ca70b4f8c0249536cd7e3b5`; status v0.5 at `2286341`. Neither identifier asserts the live HEAD.

## Scope

Read-only spatial registration and luma boundary-strength / proxy detectability reports on **original LG_576i_3_LP** (mandatory primary) and **LG_576i_3_LP_blocky** (secondary only). No filtering, no denoising, no choice/tuning of pixel detector or kernel, no pixel-only seam identification, no Stage 1 changes, no hold-outs. Only numeric CSV/text/JSON. No media in this package. S2-I3 is NOT AUTHORISED.

All candidate source/scripts reside inside `REPO_OVERLAY/experiments/stage2/`. They require unchanged installed `stage2_index_reader_v0_2.py`, `stage2_index_reader_regression_v0_2.py`, `stage2_validate_bestsource_v0_2.vpy`, frozen `tools/Stage1_Inspector_Analyzer_v0_2.py`, and frozen inspector executable. Overlay only these candidate files; do not copy the top `REPO_OVERLAY` name into the repository path. Do **not** commit or give to owner before Claude clears.

## Components

| Candidate file | Purpose |
| --- | --- |
| `stage2_registration_stats_v0_1.py` | Pure-NumPy statistics, no VapourSynth import; all 3 registration diagnostics, 7 bad offsets, two-orientation scored seams, uncertainty and CSV outputs |
| `stage2_registration_clip_v0_1.vpy` | Thin native BestSource 8-bit 4:2:0 read-only luma frame adapter; full every-frame S2-I1 correspondence first |
| `stage2_vspipe_env_preflight_v0_1.vpy` | Tiny `vspipe --info` run with valid 1-frame BlankClip output; plugin file SHA and NumPy/Python/VS identity; runs synthetic tests in actual `vspipe` Python |
| `stage2_registration_tests_v0_1.py` | Synthetic tests of signed/field-safe arithmetic, gates, 8-phase, AUC/ties and offset convention |
| `stage2_validate_lp_blocky_v0_1.py` | Standard-library and frozen-reader scratch-index SHA and complete identity assertion; plain Python doesn't need NumPy |
| `stage2_check_result_v0_1.py` | Standard-library-only results PASS/BLOCKED reader for Windows runner |
| `stage2_ffmpeg_rehearsal_v0_1.py` | Claude Linux FFmpeg decode -> **same** statistics engine, separate from formal BestSource acceptance |
| `S2_I2_prepare_LP_blocky_index_v0_1.bat` | Windows scratch-only MPEG-2 elementary-file -> frozen inspector -> analyzer+reader+BestSource validation |
| `S2_I2_run_registration_v0_1.bat` | Windows LP/LP_blocky only; verifies baseline and runs preflight, BestSource index validation, statistics and result gate |

## Predeclared registration gates

- 3x3 FRAME-FIELD `C(dx,dy)`: zero shift positive strict maximum; >= 10% advantage over **every** other shift; zero winner in >= 2/3 eligible frames. A higher nonzero competitor FAILs; tie/weak/undersupported means INCONCLUSIVE.
- 8-column phase: phase 0 unique maximum by >= 10%; wrong maximum FAIL, tie/weak INCONCLUSIVE.
- 8-row **same-field** phase: fixed 16-pixel border, q6 and q7 aggregate top two; `row_margin >= 0.05`; these two lead in >= 2/3 eligible frames. Any other aggregate phase in the top two, including a tie, FAILs. Other weak cases INCONCLUSIVE.
- Bad controls: pixel displacements (+4,+8,+16 columns), (+1,+2,+8,+16 rows). Positive shifts mean pixels moved right/down, index unchanged, no wrap. Each must produce at least one non-PASS.
- Report the normalised D alongside raw D, but gate on raw D only. Original LP cannot be rescued by LP_blocky.

## Descriptive-only report

For each clip, separately, both seam orientations, output M2-like plain and M4-like noise-robust scores on index-known coded internal and MB-outer seams versus x=4/12 and horizontal 3|4/11|12 standard non-seam controls. Internal NONE positions remain a distinct no-coded-seam category. Split NONE into `NONE-SKIPPED-P`, `NONE-SKIPPED-B`, `NONE-INTER-CBP0` (and explicit residual OTHER if any); report their midpoints and outer-edge neighbour states/coding classes without selecting a NONE filtering policy. Outer-edge QP bands use the right/lower macroblock as the declared owner, while both neighbours' QP and coding state are retained in the paired outer diagnostics. For NONE, the indexed QP is only the slice quantiser in force, not evidence that residual was quantised in that macroblock. Strict greater-than on the 95th observed percentile of standard controls gives approximately 5% achieved proxy FA, which is reported. Rank-tie-aware AUC. The fixed QP bands are `0-15`, `16-31`, `32-63`, `64-111`, `112` separately, and `>112` as a separate out-of-range diagnostic band. Also I/P/B, exact counts, frame and GOP hit-rate quartiles. These are seam-vs-non-seam **proxies**, not known artifact labels; weak hit rates do not fail spatial registration.

## Owner runtime path after Claude clears (NOT instructions to run now)

1. Install reviewed overlay files directly to `experiments\stage2\` after a scope check.
2. Ensure the accepted S2-I1 reader/regression/vpy and Windows native inspector remain intact.
3. Run `S2_I2_prepare_LP_blocky_index_v0_1.bat` once to generate and validate scratch `.idx`; expected SHA-256 is `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238`, 204 frames, 720x576, I/P/B 19/50/135, transforms 54292/33853/242335, QP 62, no leading B.
4. Run `S2_I2_run_registration_v0_1.bat LP` and then `S2_I2_run_registration_v0_1.bat LP_blocky`, separately. There is NO all-sources switch.
5. Review `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP\` and `...\LP_blocky\` numeric outputs and logs. An exit code of 0 is NOT owner gate ratification.
6. After the required review and when no longer needed, remove the **Restricted** `.m2v` from the scratch LP_blocky folder. Scratch candidate `.idx` stays non-baseline/untracked unless the owner later directs otherwise. Never commit scratch/source media or any Restricted visualisation.

The BATs inherit expected tool paths from the previously reviewed S2-I1 scripts: ffmpeg `C:\SOFTWARE\ffmpeg\ffmpeg.exe`, vspipe `D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe`, x64 Release inspector path in the repository, and `python` for standard-library scripts. Claude must verify paths against the actual owner machine before clearance. No vspipe Python interpreter path is guessed.

## Mandatory checks before owner's run

- Claude runs actual pure-NumPy engine on unmodified FFmpeg-decoded LP **and** LP_blocky and validates the reported 3 registration tests, all seven offsets, and reporting schemas. Check that FFmpeg and BestSource decoding are different acceptance surfaces.
- Claude line-by-line audits both Windows BATs (quoted paths, `%%`/`%`, `errorlevel`, redirections, short-read avoidance, scratch ownership, duplicate outputs, `--arg`, log files); notes any differences between Windows CMD and Linux shell semantics.
- Claude independently checks baseline LP `.idx` SHA-256 `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011`, six unchanged regressions, scratch blocky expected hash and all 8 identity assertions, no Stage 1 source alteration.
- Preflight must emit a VALID `vspipe --info` output, fail closed on missing NumPy/vapoursynth/BestSource or unverifiable plugin path, and record the BestSource DLL path plus SHA-256. Missing plugin version *string* alone must not block.
- On Windows the adapter must see a native, stride-aware read-only plane 0, copy to `int16` for differences, get the output directory via `vspipe --arg out=...`, verify per-frame picture type and preserve source pixels.
- Verify `run_manifest.json` and the complete numerical report set exist on PASS **and** BLOCKED runs. Baseline hashes, sample inclusion, no cross-clip pooling, 5% proxy threshold, QP bands, NONE class reporting and frame/GOP-level uncertainty must remain auditable.
- Any inconsistency: no owner run. Report issue and issue versioned implementation correction for independent re-review. Do not modify ratified thresholds to make evidence pass.

## Local ChatGPT rehearsal (not formal acceptance)

Linux: synthetic unit suite PASS. The unmodified frozen inspector source compiled for a Linux regular-file run and produced the exact independently expected LP_blocky `.idx` hash. The unmodified S2-I1 six-index regression PASS. Both FFmpeg decoded clips passed all three registration gates and all seven known-bad offsets. See accompanying `S2_I2_IMPLEMENTATION_REHEARSAL_EVIDENCE_v0_1.md` for exact numbers and limitations. **No Windows `vspipe`, native BestSource, CMD or Visual Studio executable was run by ChatGPT.**
