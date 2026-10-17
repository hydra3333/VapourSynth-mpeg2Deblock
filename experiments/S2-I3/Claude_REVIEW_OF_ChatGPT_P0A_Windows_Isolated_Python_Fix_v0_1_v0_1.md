# Claude review of the S2-I3 P0A Windows isolated-Python fix v0.1 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: `S2_I3_P0A_WINDOWS_ISOLATED_PYTHON_FIX_v0_1_FOR_CLAUDE_REVIEW.zip`
Baseline: the cleared S4 candidate (`Claude_DIFF_CLEARANCE_S2_I3_P0_S4_Candidate_v0_1.md`)
Repository: `35cd543b459a5856688f7c3795f73226e72311f8`

## 1. Verdict

**CLEARED. Replace only this one BAT and rerun P0A.** No MUST, no SHOULD.

The diagnosis is correct, the fix is correct and minimal, and Claude has reproduced both the failure
and the repair under genuine isolation. Exactly one of the 15 overlay files changes.

**The defect was Claude's.** S4 was Claude's recommendation, and Claude's verification of it was
inadequate in a specific, identifiable way. Section 2.

## 2. How Claude got this wrong

The owner's VapourSynth interpreter is the **Windows embeddable Python distribution**. A
`python314._pth` file beside `python.exe` puts it in isolated mode: `sys.flags.isolated = 1` and
`sys.flags.safe_path = True`. **In that mode Python does not add the script's own directory to
`sys.path`**, so `stage2_i3_pskip_tests_v0_1.py` could not import its sibling
`stage2_i3_pskip_core_v0_1`.

Claude specifically tested the risk this fix addresses and got a false pass. In clearing S4, Claude
staged the overlay, moved to an unrelated working directory, invoked both suites by absolute path, saw
9/9 and 5/5, and wrote that "Python adds the script's own directory to `sys.path`, so the form is
sound". That statement is true only for a **non-isolated** interpreter, which is what Claude tested
with - while recommending an interpreter that is isolated by default.

Worse, the evidence was already in Claude's own output. At the very start of the P0 candidate review,
Claude ran the supplied test files with `python3 -I` and both failed with **exactly this error**:

```
ModuleNotFoundError: No module named 'stage2_i3_pskip_core_v0_1'
```

Claude re-ran them without `-I`, saw them pass, recorded "14 supplied unit tests pass", and never
registered that isolated mode was the trigger. Two separate chances to catch it were missed. The
general lesson, which belongs in the handover lesson list: **an embeddable or isolated Python does not
put the script's directory on `sys.path`; any script invocation must be tested under `-I` as well as
plain.**

One thing worth saying plainly to the owner: **the gate behaved correctly.** P0A failed before
creating any scratch folder, so there is no partial state, nothing to clean up, and no ambiguity about
what ran. That is the sequencing working as designed.

## 3. What Claude verified

All tests used the exact `-c` string extracted from line 23 of the candidate BAT, single quotes
included.

**1. The owner's failure, reproduced exactly.** Isolated interpreter, plain script invocation:

```
ModuleNotFoundError: No module named 'stage2_i3_pskip_core_v0_1'   rc=1
```

Identical to the reported output. Flags under test: `isolated 1`, `safe_path True` - matching what the
owner reported from his interpreter.

**2. The fix works under genuine isolation.** With `-I` and the new `-c` form, both suites pass:
**9/9 P-skip and 5/5 pair, rc=0 each**.

**3. `PYTHONPATH` would not have worked.** Claude checked the obvious simpler alternative: isolated
mode ignores environment variables, and with `PYTHONPATH` set the plain invocation **still fails**
(rc=1). So explicitly inserting the directory into `sys.path` was **necessary, not stylistic**. This
validates the approach taken rather than merely permitting it.

**4. Fail-closed on every failure mode.** `SystemExit` from `unittest.main()` propagates correctly
through `runpy.run_path`:

| Injected fault | Result |
|---|---|
| A deliberately failing assertion (inserted before `unittest.main()`) | 6 tests ran, 1 failure, **rc=1** |
| A syntax error in the test file | **rc=1** |
| The sibling core module deleted | **rc=1** |

So `if errorlevel 1` fires and P0A stops with its message in each case.

A caution for whoever repeats this test: Claude's first attempt appended the failing test **after** the
`if __name__=='__main__':unittest.main()` line, so it was defined after the suite had already run and
exited, and the run reported rc=0. That was a flaw in the test, not in the fix. The injected test must
go **before** that final line.

**5. `sys.argv=[script]` is necessary, not decoration.** Removing it and rerunning gives
`FAILED (errors=1)` with rc=1, because `unittest.main()` then treats the path left in `sys.argv[1]` as
a test name. The reassignment is doing real work.

**6. A path containing a space works** (rc=0). The owner's paths contain none, but the form is robust.

**7. No stdlib shadowing.** `sys.path.insert(0, ...)` puts the script directory ahead of the standard
library. The directory holds 12 `.py` modules and Claude checked every name against
`sys.stdlib_module_names`: **zero collisions**. So nothing in the standard library is masked for the
rest of that process.

**8. CMD quoting is sound.**
- The whole Python command is a single double-quoted argument containing **no embedded double
  quotes** - only single quotes around `'__main__'` - so there is nothing for CMD to mis-terminate.
- It contains **no `%` character inside the Python code**, so no `%%` doubling is required. The only
  `%...%` tokens on those lines are the three intended BAT variables: `%vspython%`, `%pskip_tests%`,
  `%pair_tests%`.
- Lines 23 and 25 are **bare commands, not inside a parenthesised block**, so the parentheses within
  the Python code cannot close a block. This is the original M1 defect class and it is not
  reintroduced. A scan of all seven BATs for a parenthesis inside a parenthesised block's echo text
  returns **none**.
- The `if errorlevel 1 (...)` guards and their messages on lines 24 and 26 are unchanged from the
  cleared S4 version.

## 4. Structural verification

| Check | Result |
|---|---|
| Manifest | 18 entries, **all 18 hashes match** |
| Files differing from the cleared S4 candidate | **exactly 1** - `S2_I3_P0A_prepare_campaign_v0_1.bat` |
| The other six BATs and all eight Python/VPY files | **byte-identical** to the cleared S4 package |
| `PROPOSED_OWNER_RUN_SEQUENCE_NOT_YET_CLEARED.md` | **byte-identical** |
| Encoding | BATs US-ASCII CRLF; `.py`/`.vpy` LF with zero CR bytes |
| Identity text | **none anywhere in the package** |
| Overlay paths | the same 15, no additions, removals or renames |
| `%vspython%` retained | yes - S4's purpose is preserved, the tests still run on the interpreter that runs the admission code |
| `python "%regression%"` | unchanged, correctly left on the system interpreter (NumPy-free, accepted S2-I2 pattern) |
| Ordering | unchanged: checks, scratch refusal, regression, both suites, `vspipe` preflight, then `mkdir` |

## 5. Disclosure of test limits

Claude tested on **CPython 3.13.16 on Linux**, simulating the isolation condition with `-I`. The
owner's interpreter is **Python 3.14, Windows embeddable**, and this was **not** run under Windows
CMD. `runpy.run_path`, `sys.flags.safe_path`, `sys.argv` reassignment and `SystemExit` propagation are
long-standing and version-stable behaviours, so Claude judges the residual risk low - but the owner's
rerun is the actual proof, exactly as it was for the original failure. Claude says this plainly rather
than implying a Windows verification it did not perform.

## 6. OPTIONAL, for later consideration only

**O1. A more idiomatic fix exists, and the project already uses it.** The project's own VapourSynth
adapters solve this problem inside the Python itself - `stage2_i3_admission_clip_v0_1.vpy` line 12 is
literally `sys.path.insert(0,str(HERE))` after computing `HERE` from `__file__`. Adding those same two
lines to the two test files would make them import correctly under **any** interpreter and **any**
invocation form, and would let P0A keep the short `"%vspython%" "%pskip_tests%"` form instead of
carrying a 180-character Python one-liner inside a BAT.

Claude is **not** asking for that now, for two good reasons: it would edit two Python files, breaking
the currently valuable property that all eight Python and VPY files are byte-identical to the fully
rehearsed set; and ChatGPT deliberately chose not to touch test sources, which is the more
conservative call mid-run. Worth adopting only if that `-c` line ever needs to change again.

## 7. What the owner should do

1. Replace **only** `experiments\stage2\S2_I3_P0A_prepare_campaign_v0_1.bat` in the already-installed
   overlay with the one from this package. The other 14 files are byte-identical, so nothing else
   needs touching. Do not copy `REVIEW_ONLY/` anywhere.
2. Confirm the scratch root `%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1` is absent. The owner
   reported it absent after the failure, which is correct; P0A refuses to run if it exists.
3. Rerun P0A. Expected, in order: the six index regressions pass; the line
   `EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent` appears and **is expected, not an
   error**; then `Ran 9 tests ... OK`; then `Ran 5 tests ... OK`; then the `vspipe` runtime preflight;
   then the three scratch folders and `P0A_READY.txt`; then `PASS: P0A`.
4. Send the console output. Then P0B, one source at a time.

**Unchanged:** no filtering; `READY` is a numerical report, not authorisation; EP, 2A and 4A with their
`_blocky` copies stay locked until S2-I8 under any filename; the seven-index tracking commit is
separate and follows P0 evidence acceptance.
