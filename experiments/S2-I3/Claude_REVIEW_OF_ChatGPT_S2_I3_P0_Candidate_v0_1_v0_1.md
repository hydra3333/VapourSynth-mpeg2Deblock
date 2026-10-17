# Claude review of ChatGPT S2-I3 P0 implementation candidate v0.1 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: `S2_I3_P0_IMPLEMENTATION_CANDIDATE_v0_1_FOR_CLAUDE_REVIEW.zip`
Baseline: `35cd543b459a5856688f7c3795f73226e72311f8` (still GitHub main HEAD at review time).

## 1. Verdict

**NOT YET CLEARED: one MUST, a one-line BAT fix.** Once M1 is fixed, the candidate is cleared for the owner's Windows P0 run. S1-S3 should be applied in the same revision.

All the Python and VPY logic is correct. It reproduces every expected result when run with the owner's own runtime versions, so no logic changes are needed.

**Integrity:**

- all 17 manifest hashes match;
- US-ASCII throughout: the BATs are CRLF and the `.py`/`.vpy` files are LF;
- no identity text, no trailing whitespace, and no tabs;
- all files compile;
- none of the 15 overlay names collides with an existing repository file.

**Scope:**

- No hold-out media is decoded. The P0A regression reads only the six frozen `.idx` files.
- No filtering takes place.
- Nothing is written to `VHSC_samples/` or anywhere else in the repository. The only exception is `__pycache__/`, which `.gitignore` line 48 already ignores.

## 2. What Claude ran

**Setup.** Claude ran everything on Linux:

- VapourSynth **R81**, BestSource **22.0** (`vapoursynth-bestsource`), NumPy **2.5.3**. These are exactly the versions recorded in the owner's committed S2-I2 `run_manifest.json`.
- The candidate's own `vspipe` scripts were run unchanged on the eight development `.mpg` files from a sparse clone of `35cd543`.
- EP, 2A, 4A and MLS media were never checked out.
- All media, BestSource cache files and the clone were deleted afterwards. A search confirmed that no `.mpg`, `.m2v`, `.yuv` or `.bsindex` file remains.

**Unit tests.**

- The supplied tests pass: 9 P-skip tests, 5 pair tests, plus the S2-I2 synthetic checks.
- Claude's own adversarial core tests also all behave as specified:
  - **floors:** exactly 200 blocks across 10 P pictures gives REGISTERED; 190 blocks, or 9 pictures, gives INCONCLUSIVE;
  - **FAIL cases:** a 1-pixel corruption, an index skip map shifted by one macroblock, and a 1-frame display slip all FAIL;
  - **structure:** a field picture raises a structural error;
  - **anchors:** the anchor is the last I/P picture across intervening B pictures;
  - **precedence:** FAIL takes precedence over INCONCLUSIVE.
- An IPPP stream (no B pictures) is INCONCLUSIVE, because control C can never execute. This matches the ratified "missing control" rule. All eight development sources contain B pictures, so it does not affect P0.

**P0B.** All seven scratch indexes plus the frozen LP index pass `verify-index`. Their P-skip counts equal the S6 reference values exactly.

**P0C admission** (actual `vspipe` + BestSource): all eight are **REGISTERED**.

| Source | Exact P-skip | P pictures | Highest control |
|---|---|---|---|
| XP | 1619/1619 | 54 | 83.9% (previous) |
| XP_blocky | 25635/25635 | 55 | 73.2% (+1,0) |
| SP | 1764/1764 | 46 | 77.7% (previous) |
| SP_blocky | 19010/19010 | 46 | 73.3% (0,+1) |
| LP | 1533/1533 | 46 | 94.8% (previous) |
| LP_blocky | 20300/20300 | 50 | 69.2% (+1,0) |
| 3A | 8812/8812 | 133 | 96.7% (previous) |
| 3A_blocky | 18190/18190 | 73 | 78.6% (-1,0) |

**Negative tests** on real BestSource frames, through the core: all FAIL.

| Case | Exact matches |
|---|---|
| XP frames with the XP_blocky index | 8.7% |
| The reverse (XP_blocky frames with the XP index) | 34.0% |
| LP with a +1 frame slip | 80.4% |
| 3A with a -1 frame slip | 84.8% |
| SP_blocky shifted 2 px | 71.1% |
| 3A shifted 1 line | 90.2% |

`vspipe` returns 1 on a SHA mismatch and on a protected label.

**P0D diagnostics.**

- **Labels:** all eight ran and are labelled per source (`S2_I2_<label>_result.txt`). The old gate is reported only.
  - PASS: XP, XP_blocky, LP, LP_blocky, 3A_blocky;
  - BLOCKED: SP, SP_blocky, 3A. These are the same precondition blocks as found in preflight.
- **Engine unchanged:** for LP and LP_blocky, all 8 CSVs per source are byte-identical (after line-ending normalisation) to the committed Windows S2-I2 evidence. This strongly indicates the engine is unchanged and the new adapter is equivalent.

**P0D pair:** all four groups PASS.

| Group | Decisive frames | Violations | Mean MAE, k=0 vs best other |
|---|---|---|---|
| XP | 140/228 | 0 | 3.53 vs 9.88 |
| SP | 175/192 | 0 | 3.23 vs 13.98 |
| LP | 81/204 | 0 | 4.39 vs 9.93 |
| 3A | 268/300 | 0 | 5.53 vs 19.95 |

- **Simulated slips:** a +1 or -1 slip FAILs on all four groups (argmin moves to the slip, 0 decisive frames).
- **Frame count:** a count mismatch gives a hard FAIL.

**Summary script.**

- On the complete evidence it returns READY with return code 0.
- It refuses, with return code 2 and a specific problem line, in each of these cases:
  - a missing `pskip_identity.json`;
  - an index changed after admission;
  - a source changed after admission;
  - a control tampered to 100%;
  - a pair SHA that does not match admission;
  - missing diagnostics;
  - a missing P0A marker;
  - another source's evidence copied into a folder (label mismatch).
- Protected labels are rejected by `argparse`.

**Numbers for the Windows run.** The table values above are what the Windows run should reproduce: it uses the same runtime versions, and MPEG-2 decoding is deterministic. Record the comparison; it is not a gate (S6).

## 3. MUST

**M1. `S2_I3_P0D_diagnostics_v0_1.bat` line 37: an unescaped `)` inside a parenthesised block.**

```
if errorlevel 1 (echo ERROR: diagnostic execution problem (not a phase-gate failure)& exit /b 2)
```

In CMD, the first `)` (after "failure") closes the IF block. The echo is cut short, and what follows is parsed as `& exit /b 2)`. The exit code on this error path then depends on how CMD reads the argument "2)", so the failure is not reliably fail-closed.

Replace the line with:

```
if errorlevel 1 (echo ERROR: diagnostic execution problem - not a phase-gate failure& exit /b 2)
```

No other BAT has a parenthesis inside a block's echo text. The only block text containing parentheses is inside quoted paths, which is safe.

## 4. SHOULD

**S1. A `for /f` capture does not set ERRORLEVEL from the command it runs.**

- In P0B-generate, P0C and P0D-diagnostics, the `if errorlevel 1` after each `for /f ... print-index-path` therefore has no effect. Only `if not defined` protects the run.
- Because `setlocal` inherits the caller's environment, clear the variables first:
  - add `set "source_name="` and `set "index_name="` before the `for /f` lines;
  - in P0D-pair, add `set "stem="` before the `if /I` lines.

**S2. Silent exits.** Several `exit /b 2` lines print nothing, which will confuse a guided step-by-step run.

- Affected lines:
  - P0C lines 21, 22, 27, 28, 33, 34;
  - P0B-generate lines 29-30;
  - P0D-diagnostics lines 13, 27, 28;
  - P0D-summary line 4.
- Add an `echo ERROR: <reason>` to each, in the same form as P0B, for example `(echo ERROR: missing source& exit /b 2)`.

**S3. Run the new S2-I3 unit tests in P0A.** P0A runs only the S2-I2 synthetic tests (through the `vspipe` preflight). After the regression, add:

```
python "%~dp0stage2_i3_pskip_tests_v0_1.py"
if errorlevel 1 exit /b 2
python "%~dp0stage2_i3_pair_tests_v0_1.py"
if errorlevel 1 exit /b 2
```

Add both files to the existence check as well.

## 5. OPTIONAL

**O1. Pair tie.** Fully static content, where the clip-mean is tied at k=0, is reported as FAIL. Strictly, it is non-discriminating and could be INCONCLUSIVE. Both outcomes block, and it cannot arise on the development pairs, so no change is needed.

**O2. Diagnostics runtime.** `stage2_i3_diagnostic_clip_v0_1.vpy` does not pass `runtime_info` to `RegistrationRun`, so its `run_manifest.json` runtime is empty. The admission manifest already records the same runtime.

**O3. Summary labelling.** In `summarise()`, a diagnostics problem also marks the source's admission as `NOT_VERIFIED`. Separate try blocks would report the two more clearly. READY is unaffected.

**O4. Error handling.** `verify-index` and `check-admission` already fail closed on `Stage2IndexError` and `KeyError`, but with a traceback (return code 1). Catching both would give one-line messages.

**O5. Label case.** The BATs accept labels case-insensitively (`if /I`), but Python is case-sensitive, so `xp` fails at `print-index-path`. Use exact case in the BATs, or accept the `argparse` message.

**O6. Interrupted P0B run.** If a P0B run is interrupted (Ctrl-C), the `.m2v` remains. The BAT then refuses to rerun until it is deleted, which is correct, but the owner should delete that named file by hand.

## 6. Proposed owner run sequence

The `PROPOSED_OWNER_RUN_SEQUENCE` is sound. Notes for ChatGPT's guided steps:

- **P0A:** the regression prints "EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent". This is expected and is not an error.
- **P0B-copy:** needs `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky\LG_576i_3_LP_blocky.idx`. If it is absent, STOP, as step 4 says.
- **Collecting evidence:** after each step, the owner should send the per-source JSON and logs. Claude checks them against section 2.
- **Step 9 (tracking the seven indexes)** stays a separate, later commit.

## 7. Re-check

After ChatGPT re-issues the candidate (it is uncommitted, so it may keep the v0_1 names) with a new manifest, Claude will run a diff-only check that only M1 and the accepted S/O items changed. No new rehearsal is needed unless Python or VPY logic changes.
