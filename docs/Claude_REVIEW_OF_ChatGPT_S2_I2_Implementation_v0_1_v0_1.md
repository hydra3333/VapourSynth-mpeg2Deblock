# Claude review of ChatGPT S2-I2 implementation candidate v0.1 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude (independent reviewer and rehearsal executor)
Subject: S2_I2_IMPLEMENTATION_CANDIDATE_v0_1_FOR_CLAUDE_REVIEW.zip
Baseline tree: commit 4221f7f plus status commit 2286341
Design reference: S2-I2 Design Plan v0.4 (ratified), Options table v0.2

## 1. Verdict

**CLEARED FOR OWNER WINDOWS RUN** - for v0.1 exactly as delivered.

- There are no MUST findings.
- There are four SHOULD findings (section 6) and six OPTIONAL findings (section 7).
- None of them changes any registration verdict on LP or LP_blocky.
- None of them needs to be fixed before the owner's Windows run.

Recommendation:

- Run v0.1 as delivered.
- Commit exactly the bytes that were run. Each run manifest records the SHA-256 of the statistics engine.
- Carry the SHOULD items into the next versioned files.

If the owner prefers to fix the SHOULD items first, ChatGPT issues v0.2 and Claude rechecks it before the run. A recheck takes one pass, because the rehearsal harness below is reusable.

## 2. What Claude executed

All work was done on Linux, on a copy of the 4221f7f tree with the nine overlay files added.

1. **Package integrity.**
   - All 13 manifest entries matched their SHA-256 values.
   - All files are US-ASCII.
   - There are zero identity hits.
2. **Synthetic tests.** `stage2_registration_tests_v0_1.py` printed 15 PASS lines and exited with code 0. It also passed with the files converted to CRLF.
3. **LP_blocky index.**
   - Built with ffmpeg stream copy to a scratch `.m2v`, then `inspector -b file -m idx` (the gcc build of the frozen inspector source).
   - SHA-256 `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238`, as expected.
   - `stage2_validate_lp_blocky_v0_1.py` passed.
4. **Unmodified engine on both clips.**
   - Run through `stage2_ffmpeg_rehearsal_v0_1.py`, decoding with FFmpeg rawvideo yuv420p and `-fps_mode passthrough`.
   - About 17 s per clip; peak memory 253 MB.
   - A second LP run gave byte-identical CSVs, so the output is deterministic.
5. **Independent re-implementation of the robust vertical measure (M4).** It reproduced the engine's LP figure exactly: 23.79%.
6. **Mutation tests.** Every eligible frame was fed with a deliberate decode error (section 4).
7. **Negative-input tests** (section 5).
8. **Line-by-line audit** of both BATs and both new `.vpy` files (section 8).

All extracted recordings, `.m2v` files and `.yuv` files were deleted from Claude's workspace afterwards.

## 3. Gate results reproduced (FFmpeg rehearsal)

| Measure | LP | LP_blocky |
|---|---|---|
| 3x3 C(0,0) | 5.9121 | 4.7161 |
| 3x3 best other shift | 4.2721 | 3.0377 |
| 3x3 frames won | 92.9% | 88.8% |
| Column phase margin | 35.15% | 46.00% |
| Row phase margin | 11.48% | 25.24% |
| Row frames won | 92.1% | 77.9% |
| 3x3 / column / row | PASS / PASS / PASS | PASS / PASS / PASS |
| Seven known-bad offsets caught | 7/7 | 7/7 |
| Gate | PASS | PASS |

These match ChatGPT's rehearsal evidence to every printed digit.

Which tests caught each known-bad offset (unchanged from ChatGPT's evidence):

| Offset | LP | LP_blocky |
|---|---|---|
| +4 columns | column FAIL | column FAIL |
| +8 columns | 3x3 FAIL | 3x3 FAIL |
| +16 columns | 3x3 FAIL | 3x3 FAIL |
| +1 row | row FAIL | row FAIL |
| +2 rows | row FAIL | 3x3 INCONCLUSIVE, row FAIL |
| +8 rows | 3x3 FAIL | 3x3 INCONCLUSIVE |
| +16 rows | 3x3 FAIL | 3x3 FAIL |

The LP_blocky +8-row catch is not marginal. C(0,0) is negative there (-1.449, against +0.707 for the best other shift), but the code labels it INCONCLUSIVE rather than FAIL (see O1).

Structural checks on LP_blocky:

- the segment counts agree with the index transform totals (FRAME 54292, FIELD 33853, NONE 242335 = 20300 SKIPPED-P + 56289 SKIPPED-B + 165746 INTER-CBP0);
- no NONE segment is counted as a coded internal seam;
- no horizontal INTERNAL-FIELD class exists (field horizontals appear as MID-FIELD-NO-CODED-SEAM);
- the GOP counts are 17 (LP) and 19 (LP_blocky), equal to the I-frame counts.

## 4. Mutation tests (deliberate decode errors fed to the unmodified engine)

| Mutation | LP gate | LP_blocky gate | Caught by |
|---|---|---|---|
| None (control) | PASS | PASS | - |
| +1, +2, +4 columns; -1 column | BLOCKED | BLOCKED | column FAIL |
| +8 columns | BLOCKED | BLOCKED | 3x3 FAIL |
| +1, +2, +4 rows; -1 row | BLOCKED | BLOCKED | row FAIL |
| +8 rows | BLOCKED | BLOCKED | 3x3 FAIL / INCONCLUSIVE |
| +1 column and +1 row | BLOCKED | BLOCKED | column and row FAIL |
| Horizontal mirror | BLOCKED | BLOCKED | 3x3 INCONCLUSIVE |
| Frame n+1 or n-1 fed as frame n | **PASS** | BLOCKED | (LP not caught) |
| Top and bottom fields swapped | **PASS** | **PASS** | (not caught) |

`stage2_check_result_v0_1.py` returned exit code 2 for every BLOCKED run and 0 for every PASS run.

The spatial gates work as designed. The two cases that are not caught are expected limits of a spatial test, not code defects (see S4):

- **One-frame slip:** the labels of neighbouring frames are spatially very similar.
- **Field swap:** every measure uses same-field pixel pairs, so swapping the fields leaves the seam geometry intact.

## 5. Negative-input tests

Each of the following was rejected with a clear message (the scripts exit with code 2 where applicable):

- LP index with the LP_blocky source, and the reverse: picture-type mismatch.
- A truncated LP_blocky index: "parsed record count 76 != header final_record_count 204".
- `stage2_validate_lp_blocky_v0_1.py` given the LP index: SHA-256 mismatch.
- `stage2_check_result_v0_1.py` with a missing result folder, or with a BLOCKED manifest.
- `check_luma` given:
  - uint8 or float input;
  - a 704-wide frame;
  - a value of 256;
  - a value of -1.
- `displaced` offset 17 or -1.
- `finalise()` with no eligible frames.

Leading-B frames are excluded before any statistics are computed.

## 6. SHOULD findings

**S1. Line endings.**

- The seven new `.py`/`.vpy` files are LF.
- The committed S2-I1 `.py`/`.vpy` files and all the BATs are CRLF.
- Python and vspipe accept either, and Claude confirmed the tests still pass after conversion to CRLF.
- The engine's SHA-256 goes into every `run_manifest.json`, so the bytes that are run must be the bytes that are committed.
- **Recommendation:** run and commit v0.1 as LF, exactly as delivered, and use CRLF from the next versioned files. Do not convert v0.1 between the run and the commit.

**S2. Padding enters the column-phase sample at the +16-column control.**

- `phase_stats` measures `|Y[x] - Y[x-1]|` from x = 16.
- At the +16-column offset, column 15 is zero padding, so the x = 16 sample is a padding step.
- A flat grey frame shows it: phase 0 reads 1.163 at +16 columns and 0 at +0 and +8 columns.
- On LP, phase 0 at +16 columns rises from 6.06 to 6.38.
- No verdict changes: phase 0 is expected to PASS at +16 columns in any case, and the 3x3 test catches that offset.
- However, the docstring claim that "padding never enters those samples" is false for this case.
- **Fix in the next version:** start the column sample at x = 17, or otherwise exclude any pair that touches padding, and add a synthetic test that a flat frame gives zero at every phase for every declared offset.

**S3. The synthetic row-phase test passes only by tie-breaking.**

- The test sets rows 8, 9, 16, 17, ... to 50.
- That makes phases 0, 1, 6 and 7 all equal (50), so `argsort` happens to pick 6 and 7.
- The same impulse moved two rows down produces a four-way tie that the predicate rejects.
- **Fix:** use a step pattern (raise rows where `r % 16 >= 8`), so that only q6 and q7 rise. Assert with `rank_top`, and add the shifted negative case.

**S4. State the limits of the registration gate in the S2-I2 results note.**

- The gate verifies the spatial grid only. A one-frame temporal slip passed on LP, and a field swap passed on both clips (section 4).
- Temporal correspondence rests on two checks:
  - the full picture-type check in `stage2_validate_bestsource_v0_2.vpy`, which also runs inside the adapter;
  - the per-frame picture-type comparison in the adapter.
- That per-frame comparison skips n = 0, for no stated reason. It should cover every frame (trivial change, next version).
- Field-order inversion cannot be detected by these measures. No BestSource path is expected to produce it; record it as a known limitation, not a risk.

## 7. OPTIONAL findings

**O1. 3x3 labelling order.**

- `gates()` tests `zero <= 0` (giving INCONCLUSIVE) before `best_alt > zero` (giving FAIL).
- A wrong-sign C(0,0) with a positive alternative is a clear failure, but it is reported as INCONCLUSIVE (LP_blocky +8 rows).
- Reordering the two tests would label it FAIL. The gate outcome is unchanged either way.

**O2. AUC for every class.**

- AUC is computed only for seam classes 1, 2 and 8. The NONE subclasses and MID-FIELD-NO-CODED-SEAM report nan.
- These AUCs cost nothing to compute, and they bear on K-08 (inherited edges). For example, LP_blocky NONE-SKIPPED-P has a robust vertical hit rate of 32.1% against 5% for the controls.

**O3. Prepare BAT, line 49.**

- The BAT exits with code 2 without a console message. Add `echo ERROR: inspector exit code %rc%`.
- The scratch `.m2v` is kept "until Claude has reviewed the log". Claude does not need it: the log, the index SHA-256 and the reader output are sufficient. It can be deleted on success; the owner command is in section 9.

**O4. Run BAT, line 45.**

- The comment says "anchored 64-hex token", but `findstr /c:` is a substring match.
- This is harmless with a full 64-hex token. Reword the comment.

**O5. BestSource version.**

- `getattr(bs, 'version', ...)` will probably print "not exposed".
- Where BestSource offers its own version function (`core.bs.Version()`), its output is a better best-effort version string.
- The plugin path and SHA-256 remain the authoritative identity.

**O6. Comparator variant for the S2-I3 funnel** (see section 10).

- Record "M4a: adjacent-slope comparators" in the Options table for S2-I3.
- It is not for S2-I2, which is descriptive only.

## 8. BAT and adapter audit (line by line)

**`S2_I2_prepare_LP_blocky_index_v0_1.bat`**

- Tool paths are identical to the S2-I1 v0.2 BATs, which the owner has already run.
- The inspector is invoked exactly as in S2-I1 v0.2 line 75: `-b file -m idx`.
- There is no pipe into the inspector (the frozen `Fill_Buffer` trap is avoided), and the `.m2v` is a regular file.
- There is no concurrent append: each tool finishes before the next writes to the log.
- Every log echo puts the redirection first (`>>"%log%" echo ...`), so there is no digit-before-`>>` trap.
- `%rc%` is captured immediately after the inspector runs.
- `if errorlevel 1` follows every external tool.
- Zero-size checks use `%%~zI`. The only deletions are of named files in the scratch folder.
- Paths in blocks are quoted, so a `)` in `%TEMP%` cannot break parsing.
- `setlocal` comes first, so the ERRORLEVEL reset is harmless.
- The analyzer is run with `--expected-frames 204`, which is correct for LP_blocky.
- BestSource correspondence uses the committed `stage2_validate_bestsource_v0_2.vpy` with `--info`, the same form as S2-I1.

**`S2_I2_run_registration_v0_1.bat`**

- The argument gate allows LP or LP_blocky only.
- The index path agrees with the prepare BAT's scratch path: `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky\LG_576i_3_LP_blocky.idx`.
- The if/else block is expanded at parse time, but every value it uses (`repo_root`, `out`) is already set by then.
- The SHA-256 is checked with certutil plus findstr.
- The run order is:
  1. the LP_blocky validator (LP_blocky only);
  2. the six-index S2-I1 regression;
  3. the vspipe preflight (synthetic tests run in vspipe's own Python), whose provenance line is found by findstr after vspipe has exited (no concurrent writer);
  4. full BestSource correspondence;
  5. the statistics run;
  6. the manifest check.
- Each step exits with code 2 on failure.
- `if errorlevel` inside the LP_blocky block is evaluated at run time, so it is correct.
- No defects.

**`stage2_registration_clip_v0_1.vpy`**

- The format check requires 8-bit integer YUV 4:2:0.
- Plane 0 is read as a read-only NumPy view of VapourSynth's native stride, then copied to a new int16 array.
- The output folder is passed as `--arg out`. The script ends with `clip.set_output()`.
- Picture-type correspondence is validated before any statistics are computed.
- `bs.plugin_path` and the plugin's SHA-256 are recorded.
- No defects, apart from S4 (the n = 0 skip).

**`stage2_vspipe_env_preflight_v0_1.vpy`**

- The script fails closed if BestSource is not loaded or its plugin file cannot be found.
- It runs the synthetic tests in vspipe's Python environment; these raise on failure.
- It ends with `BlankClip(...).set_output()`, so `--info` completes.
- No defects.

**Engine geometry, checked against Design v0.4:**

- **Vertical:** cross `(x-1, x)`; comparators `(x-3, x-2)` and `(x+1, x+2)`, signed right minus left. The robust measure is computed per field parity and is the equal mean of the two ratios.
- **Horizontal:** pairs 6|8 and 7|9 at the middle, and -2|0 and -1|1 at the outer edge, with the ratified comparators, signed lower minus upper. The robust measure is the equal mean over 2 parities x 2 eight-column chunks. 7|8 is never used.
- **Controls:** 4 and 12 for vertical; 2|4 / 3|5 and 10|12 / 11|13 for horizontal.
- **NONE subclasses:** use coding codes SKIPPED = 1 and INTER = 3, split by picture type.
- **QP bands:** as declared, with 112 isolated.
- **Threshold:** the smallest control score with at least 95% of controls at or below it. A hit is strictly greater. The achieved false-alarm rate is at most 5%.
- **AUC:** handles ties.
- **Frame/GOP uncertainty:** quartiles of the per-frame and per-GOP hit rates.

All of these match the ratified design.

## 9. Owner Windows run (after ratifying this clearance)

Copy the nine `REPO_OVERLAY\experiments\stage2` files into `experiments\stage2`, then run the following, one block at a time:

```
cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"
```

```
experiments\stage2\S2_I2_prepare_LP_blocky_index_v0_1.bat
```

```
experiments\stage2\S2_I2_run_registration_v0_1.bat LP
```

```
experiments\stage2\S2_I2_run_registration_v0_1.bat LP_blocky
```

```
del "%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky\LG_576i_3_LP_blocky.m2v"
```

```
git status --short
```

Bring back (no media):

- `index_preflight.log`;
- `S2_I2_LP.log` and `S2_I2_LP_blocky.log`;
- from each of the two output folders, `run_manifest.json`, `known_bad_offsets.csv`, `shifted_label_contrast.csv`, `column_phase.csv`, `row_phase.csv` and `boundary_detectability.csv`;
- the console text;
- the `git status` output.

Expected:

- **Both gates PASS, with 7/7 known-bad offsets caught.** BestSource and FFmpeg both decode with libavcodec, so the figures should match section 3. Small differences would not matter if every gate still passes; a different verdict would.
- **`git status`** should list only the nine new overlay files as untracked; nothing inside the repository should be modified.

## 10. The M4 discrepancy (23.79% against the preview's 47%)

The engine is correct. Claude's earlier preview was the measure that differed.

- **The ratified v0.4 robust vertical numerator** compares the signed cross step `(x-1, x)` with the spaced comparators `(x-3, x-2)` and `(x+1, x+2)`.
- **Claude's preview numerator** used the adjacent slopes `(x-2, x-1)` and `(x, x+1)`. Its denominator used the ratified comparators.

Claude's re-implementation of the ratified formula, over all macroblock columns as the engine does, gives exactly 23.79%. The preview's figure of about 47% should not have been described as the ratified M4. That was Claude's error.

Same controls, same 95th-percentile threshold, coded internal vertical seams:

| Variant | LP hit | LP AUC | LP_blocky hit | LP_blocky AUC |
|---|---|---|---|---|
| Ratified comparators (engine) | 23.79% | 0.754 | 43.2% | 0.840 |
| Adjacent-slope comparators | 47.0% | 0.812 | 43.4% | 0.860 |

The LP_blocky figures were computed over interior columns only, so they differ slightly from the engine's per-class report.

The two definitions differ materially only on LP, which is lightly quantised. S2-I2 is descriptive and this result does not affect any gate, so the ratified definition stays for S2-I2. The adjacent-slope variant is worth carrying into the S2-I3 funnel as M4a (O6).

## 11. Paste-ready block for ChatGPT

```
Claude review of S2-I2 implementation candidate v0.1: CLEARED FOR OWNER WINDOWS RUN (v0.1 as delivered). No MUST.
Claude executed: manifest 13/13 OK; synthetic tests 15/15 PASS; LP_blocky scratch index rebuilt via file (not pipe),
SHA b3f1d714...5238 PASS; unmodified engine on FFmpeg-decoded LP and LP_blocky reproduced your evidence to every
printed digit (LP C00 5.9121/4.2721, col 35.15%, row 11.48%; LP_blocky 4.7161/3.0377, 46.00%, 25.24%; both 7/7
known-bad caught; gate PASS); deterministic; peak 253 MB.
Mutations: column shifts +1/+2/+4/-1 and row shifts +1/+2/+4/-1 all BLOCKED; mirror BLOCKED. NOT caught: one-frame
temporal slip on LP, and field swap on both (expected limits of a spatial gate). Negatives (wrong index/source,
truncated index, wrong SHA, bad luma dtype/size/range, offset 17/-1, no frames, missing/BLOCKED manifest) all rejected.
M4 discrepancy resolved: engine matches ratified v0.4 exactly (independent re-implementation = 23.79%). Claude's
preview used adjacent-slope comparators (x-2,x-1),(x,x+1) in the numerator; Claude's error. Variant gives LP 47.0%
(AUC 0.812 vs 0.754); LP_blocky about equal. Keep ratified for S2-I2; record "M4a adjacent-slope" for S2-I3 funnel.
SHOULD (next version, not before the run):
S1 new .py/.vpy are LF (S2-I1 precedent CRLF): run and commit v0.1 bytes as delivered; CRLF from next files.
S2 phase_stats uses Y[x]-Y[x-1] from x=16, so at the +16-column control the x=16 sample touches padding column 15
   (flat frame: phase0=1.163); no verdict changes but docstring is false. Start at x=17 or exclude padded pairs; add
   flat-frame zero test for every offset.
S3 synthetic row-phase test passes by argsort tie (q0,q1,q6,q7 all 50). Use step pattern r%16>=8, assert rank_top,
   add shifted negative.
S4 state gate limits in results note (spatial only; temporal via picture types); adapter per-frame type check
   should include n=0.
OPTIONAL: O1 gates(): test best_alt>zero before zero<=0 so wrong-sign C00 is FAIL not INCONCLUSIVE (LP_blocky +8
rows: C00 -1.449 vs 0.707). O2 report AUC for NONE subclasses/MID-FIELD too. O3 prepare BAT line 49 add error echo;
.m2v not needed by Claude, delete after success. O4 "anchored" comment wording. O5 use core.bs.Version() if
present. O6 add M4a to Options table.
Review file: Claude_REVIEW_OF_ChatGPT_S2_I2_Implementation_v0_1_v0_1.md
```
