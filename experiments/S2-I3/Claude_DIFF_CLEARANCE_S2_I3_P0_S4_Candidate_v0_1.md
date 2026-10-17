# Claude diff-only clearance: S2-I3 P0 S4 candidate (v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: `S2_I3_P0_IMPLEMENTATION_CANDIDATE_v0_1_S4_FOR_CLAUDE_DIFF_CHECK.zip`
Prior clearance: `Claude_P0_REVISED_CLEARANCE_AND_PROJECT_STATE_OF_PLAY_v0_1.md`
Baseline: `35cd543b459a5856688f7c3795f73226e72311f8`
Scope: one-file diff audit, as promised. No new full Linux rehearsal was needed (section 4).

## 1. Verdict

**CLEARED. This is the package to run.** No MUST, no SHOULD, no OPTIONAL requiring action.

S4 is applied exactly as recommended, verbatim down to the error-message text. **Exactly one of the
15 overlay files differs** from the already-cleared revised candidate, and that one difference is
precisely S4 with no unrelated edits.

The S2-I3 P0 code is now fully cleared with every finding from both review rounds closed: the M1
Windows CMD parenthesis, S1 to S3 from the first review, and S4 from the diff check.

## 2. Mechanical verification

| Check | Result |
|---|---|
| Manifest | 18 entries, **all 18 hashes match** |
| Files differing from the cleared revised candidate | **exactly 1** - `S2_I3_P0A_prepare_campaign_v0_1.bat` |
| The other six BATs and all eight Python/VPY files | **byte-identical** to the cleared candidate |
| Overlay paths | the same 15, no additions, removals or renames |
| Encoding | BATs US-ASCII CRLF (38/38, 20/20, 68/68, 43/43, 40/40, 30/30, 11/11); `.py`/`.vpy` LF with zero CR bytes |
| Identity text | **none anywhere in the package**, including `REVIEW_ONLY/` |
| `PROPOSED_OWNER_RUN_SEQUENCE_NOT_YET_CLEARED.md` | **byte-identical** to the cleared package |
| ChatGPT's supplied patch versus Claude's independent diff | **exactly identical**: 6 added, 4 removed on both sides, zero lines in one and not the other |
| Parenthesis-in-block scan, all seven BATs | **none** |

## 3. The P0A change, audited line by line

The complete change is:

```
+set "vspython=D:\TEST\Vapoursynth_x64_R81\python.exe"
-for %%F in ("%regression%" "%preflight%" "%vspipe%" "%pskip_tests%" "%pair_tests%") do ...
+for %%F in ("%regression%" "%preflight%" "%vspipe%" "%pskip_tests%" "%pair_tests%" "%vspython%") do ...
-python "%pskip_tests%"
-if errorlevel 1 exit /b 2
-python "%pair_tests%"
-if errorlevel 1 exit /b 2
+"%vspython%" "%pskip_tests%"
+if errorlevel 1 (echo ERROR: S2-I3 P-skip unit tests failed& exit /b 2)
+"%vspython%" "%pair_tests%"
+if errorlevel 1 (echo ERROR: S2-I3 pair unit tests failed& exit /b 2)
```

Audit findings, all satisfied:

- **Interpreter path is correct.** The committed S2-I2 evidence records `sys_executable` as
  `d:\test\vapoursynth_x64_r81\python.exe`. S4 uses
  `D:\TEST\Vapoursynth_x64_R81\python.exe`, which is the same file - Windows paths are
  case-insensitive. This is the interpreter `vspipe` actually uses, so it certainly has NumPy.
- **Guarded before use.** `%vspython%` is added to the existing existence-check loop at line 12,
  which runs before the first use at line 23. A missing interpreter stops P0A with
  `ERROR: missing ...` and exit 2.
- **Quoting correct.** Both the interpreter and the script path are quoted on each invocation.
- **No new parenthesis hazard.** Neither new echo text contains `(` or `)`; `S2-I3` uses a hyphen.
  This was the original M1 defect class, and the fix does not reintroduce it.
- **Reason-bearing failure**, which the earlier silent `exit /b 2` lacked - consistent with S2.
- **The accepted pattern is preserved.** `python "%regression%"` is deliberately left on the system
  interpreter. Correct: the reader regression imports no NumPy, and that invocation is the accepted
  S2-I2 pattern which should not change.
- **Order and fail-closed sequencing preserved.** Existence checks, then the scratch-folder refusal,
  then the regression, then the two new suites, then the `vspipe` preflight, and only then
  `mkdir "%root%"`. **A unit-test failure therefore stops P0A before any scratch folder is created**,
  leaving nothing to clean up.

## 4. Behavioural checks Claude ran

The change is a BAT, which cannot be executed here, so Claude tested the two behaviours S4 depends on.

**Absolute-path invocation from an unrelated working directory.** This is the one real risk in S4's
form: the BAT calls the test files by absolute path, and those files import sibling modules
(`stage2_i3_pskip_core_v0_1`, `stage2_i3_pair_correspondence_v0_1`). Claude staged the S4 overlay
beside the committed `experiments/stage2` scripts, changed to an unrelated working directory, and
invoked both suites exactly as the BAT does. Both resolved their imports and passed: **9/9 P-skip and
5/5 pair**. Python adds the script's own directory to `sys.path`, so the form is sound.

**Fail-closed when NumPy is absent.** With `numpy` made unimportable, the P-skip suite exits with
return code **1** and a clear `ModuleNotFoundError`. So `if errorlevel 1` fires and P0A stops with the
new message. That is exactly the failure mode S4 exists to make visible, and it now fails loudly
rather than silently or on the wrong interpreter.

**No new rehearsal was required.** All eight Python and VPY files are byte-identical to the candidate
Claude rehearsed in full under real `vspipe` and BestSource, so that evidence carries forward
unchanged: eight sources REGISTERED with exact P-skip counts, four pairs PASS, negative controls all
below 100%, LP and LP_blocky diagnostics byte-identical to the committed Windows evidence, and the
summary refusing missing, stale, tampered or mislabelled evidence. This matches what Claude promised:
a one-file diff audit, not a repeat rehearsal.

## 5. Which package to run

**Run the S4 package.** Both are cleared, so either is permissible, but S4 is strictly better: it
exercises the interpreter that will actually run the admission code, and it removes the possibility of
P0A failing on a missing NumPy in the system interpreter.

The expected values for the owner's run are unchanged from the prior clearance:

- eight sources **REGISTERED**, with exact P-skip counts XP 1619, XP_blocky 25635, SP 1764,
  SP_blocky 19010, LP 1533, LP_blocky 20300, 3A 8812, 3A_blocky 18190;
- the six generated scratch index SHA-256 values equal to Claude's Linux references, and LP_blocky
  equal to `b3f1d714...5238`;
- four pairs **PASS** with zero decisive violations;
- `P0A_READY.txt` created only after the regression, both unit suites and the `vspipe` preflight pass;
- the regression's line `EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent` is **expected
  and not an error**.

## 6. Notes, no action required

**N1.** `P0A_READY.txt` still reads "regression and vspipe preflight PASS; indexes pending" and does
not mention the two unit suites it now also gates on. Purely cosmetic: the file is a gate marker whose
**existence** alone is checked by `summarise()`, never its text. Claude verified that.

**N2.** As with the handover package, the `REVIEW_ONLY/` `.patch` and request must stay out of Git.
Nothing in this package carries identity text, so there is no leak risk here - only the usual rule.

**N3.** ChatGPT's patch headers use descriptive labels (`CLEARED_REVISED/...`, `S4_CANDIDATE/...`)
rather than applicable relative paths. As before, this cost nothing because Claude diffed
independently and the change-sets matched exactly.

## 7. Where this leaves P0

**The code is done being reviewed.** Nothing further is pending on Claude's side for P0.

Next: the owner copies only `REPO_OVERLAY/experiments/stage2/` into
`experiments/stage2/`, by exact name, never `REVIEW_ONLY/`, then runs the guided sequence one small
CMD block at a time per `PROPOSED_OWNER_RUN_SEQUENCE_NOT_YET_CLEARED.md`, which is unchanged and
previously reviewed. Then the owner sends the per-source JSON files and logs, and Claude checks them
against section 5.

**Still true and unchanged:** no filtering; `READY` is a numerical report, not authorisation; EP, 2A
and 4A with their `_blocky` copies stay locked until S2-I8 under any filename; the seven-index
tracking commit is separate and comes only after P0 evidence is accepted.
