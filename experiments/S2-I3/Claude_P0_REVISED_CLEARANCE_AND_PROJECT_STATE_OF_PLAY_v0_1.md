# Claude: S2-I3 P0 revised candidate clearance, and project state of play

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Author: Claude
Date: 2026-10-17
Subjects: `S2_I3_P0_IMPLEMENTATION_CANDIDATE_v0_1_REVISED_FOR_CLAUDE_DIFF_CHECK.zip`, plus a consolidated statement of what is currently true
Repository: GitHub `main` HEAD is `35cd543b459a5856688f7c3795f73226e72311f8`, re-verified at the time of writing

## 1. Bottom line

**The revised P0 candidate is CLEARED for the owner's Windows run.** The diff contains exactly M1 and S1-S3 and nothing else; every Python and VPY file is byte-identical to the candidate Claude already rehearsed, so all of that rehearsal evidence carries forward unchanged.

**One new SHOULD (S4), one line, worth applying first.** The S3 change Claude itself asked for introduced a dependency that no previous step in this project had: P0A now runs two numpy-importing scripts under the system `python`. Section 2.3.

**Nothing erroneous has reached the repository.** HEAD is unchanged, nothing was committed today, and every ratified authority is exactly as it was this morning. The corrections of the last few hours all happened at the review gate, which is what it exists for.

## 2. Diff-check verdict on the revised candidate

### 2.1 What changed, mechanically verified

| Check | Result |
|---|---|
| Manifest | 18 entries, **all 18 hashes match** |
| Files changed vs prior candidate | **Exactly six BATs.** `S2_I3_P0B_copy_LP_blocky` and all eight Python/VPY files byte-identical |
| Files added or removed | None. The same 15 overlay names, unchanged |
| Encoding | BATs US-ASCII CRLF throughout; `.py`/`.vpy` LF, zero CR bytes |
| Identity text | None |
| ChatGPT's own patch | Applies cleanly to the prior BATs and **reproduces the shipped files exactly** |
| Proposed owner run sequence | **Byte-identical** to the version already reviewed |
| Unit tests (unchanged files) | 9/9 P-skip and 5/5 pair, re-run and PASS |

### 2.2 M1 and S1-S3 confirmed applied, and nothing else

- **M1 fixed.** `S2_I3_P0D_diagnostics_v0_1.bat` now reads `(echo ERROR: diagnostic execution problem - not a phase-gate failure& exit /b 2)`. The parenthesis is gone, so the IF block closes where intended and the path is fail-closed. Claude scanned all seven BATs for any parenthesis inside a parenthesised block's echo text: **none remain**.
- **S1 applied correctly.** `set "source_name="` and `set "index_name="` precede the `for /f` captures in P0B-generate, P0C and P0D-diagnostics; `set "stem="` precedes the label gate in P0D-pair. The ineffective `if errorlevel 1` lines after each `for /f` are removed, and the non-empty capture gates are retained and now carry reasons.
- **S2 applied.** Every silent exit site Claude identified now echoes a reason: P0C's six, P0B-generate's two, P0D-diagnostics' three including the label fall-through, and P0D-summary's one.
- **S3 applied, in the right place.** P0A checks both new test files exist, then runs them **after** the reader regression and **before** the vspipe environment preflight, each with `if errorlevel 1 exit /b 2`. A failure stops P0A before any scratch folder is created.
- **No OPTIONAL item adopted**, as stated. No change to admission logic, thresholds, source assignment, hold-out protection or index handling. The eight ratified labels remain the only admissible inputs.

### 2.3 S4 (new SHOULD): run the new unit tests under the VapourSynth Python

Claude checked every script that any BAT invokes with plain `python`. Before this revision, **all of them were numpy-free**: the index reader, the reader regression, `stage2_check_result_v0_1.py` and `Stage1_Inspector_Analyzer_v0_2.py` contain zero numpy imports. The owner's system `python` has therefore never needed numpy for this project.

The two new test files, and the core modules they import, **all import numpy**. So P0A now depends on numpy being available to whatever `python` is first on PATH. Two consequences:

1. If that interpreter lacks numpy, **P0A fails at its first step** - safely and loudly, but P0A gates everything else.
2. More importantly, a test that passes under the system `python` says nothing about the interpreter that will actually execute this code. The committed S2-I2 preflight makes this principle explicit in its own comment: *"Execute deterministic unit tests in the actual vspipe Python environment."* S3 as implemented runs the new tests somewhere else.

The VapourSynth interpreter is recorded in the owner's committed S2-I2 evidence as `d:\test\vapoursynth_x64_r81\python.exe`, and it certainly has numpy because vspipe uses it.

**Proposed change, P0A only.** Add the interpreter:

```
set "vspython=D:\TEST\Vapoursynth_x64_R81\python.exe"
```

add `"%vspython%"` to the existence-check loop, and change the two new invocations to:

```
"%vspython%" "%pskip_tests%"
if errorlevel 1 (echo ERROR: S2-I3 P-skip unit tests failed& exit /b 2)
"%vspython%" "%pair_tests%"
if errorlevel 1 (echo ERROR: S2-I3 pair unit tests failed& exit /b 2)
```

Leave `python "%regression%"` as it is: it needs no numpy and it is the accepted S2-I2 pattern.

**This is a SHOULD, not a MUST.** It cannot produce wrong evidence; the tests either pass or fail loudly. It does not block clearance. But it costs one line and removes both risks, so it is worth doing before the run. If the owner's system `python` already has numpy and he would rather not touch the file again, running as-is is acceptable and the only loss is that the tests exercise the wrong interpreter.

### 2.4 Answers to the five diff-review questions

1. **Only M1 and S1-S3, parsing and control flow sound.** Confirmed above. The new echoes use `&` separators inside the block in the same form P0B already used and Claude already cleared.
2. **P0A placement correct**, and failure stops P0A before the scratch folder is created.
3. **Fail-closed behaviour confirmed, including the two awkward cases.** If `print-index-path` produces no output, which is what happens when `argparse` rejects a label and writes only to stderr, the cleared variable stays undefined and the `if not defined` gate exits 2 with a reason. If the caller's environment is polluted with a stale `source_name`, `index_name` or `stem`, the new `set "x="` lines clear it first, so a stale value can no longer be silently reused. One incidental benefit: a lower-case label such as `xp` now passes the `if /I` gate, fails `print-index-path`, and produces a clean one-line error instead of the Python traceback noted as O5.
4. **Manifest, newlines, identity and names all verified.** Section 2.1. `REVIEW_ONLY/` must stay untracked, including the new `.patch`.
5. **CLEARED**, subject to S4 above and to the guided small-step run.

## 3. State of play: what is true right now

### 3.1 The repository has not moved

HEAD is `35cd543b459a5856688f7c3795f73226e72311f8`, the same commit that has been the baseline all day. **Nothing was committed today.** These remain ratified and untouched:

- `05_DECISIONS_v1_2.md`
- `06_DEBLOCK_CONCEPT.md` v1.2, with K-01 to K-11 and O-01 onwards
- `Stage2_Experiment_Design_v0_7.md`
- `S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md`
- `00_PROJECT_STATUS_v0_7.md`
- `S2_I2_Evidence_and_Gate_Report_v0_1.md`
- the six frozen Stage 1 indexes

**No design, criterion, threshold, fold, source role, hold-out or gate has changed today.** Everything from today is either a candidate awaiting a run, or a review, or a proposal that has not been installed.

### 3.2 Three separate tracks, only one of which is on the critical path

The sense of churn comes from three things running at once. They are independent, and it helps to see them apart.

| Track | What it is | Status now | On the P0 critical path? |
|---|---:|---|---|
| **1. P0 implementation** | The code the owner is about to run | **CLEARED** after one review and one fix | **Yes - this is the live one** |
| **2. Sample pool** | The 17/10 new sample files | Duplicate problem found and **resolved**; two genuinely new pairs parked | No |
| **3. Findings and knowledge** | Paired-metric and interlace measurements, and whether to record them | Proposal **not cleared, not installed**, deferred | No |

**Track 3 is where all the churn has been, and Track 3 touches nothing operative.** No ratified document, no code, no run depends on it.

### 3.3 The sample pool, settled

- 20 `.mpg` files, **20 distinct content hashes**, verified by the owner's own `Get-FileHash` grouping. No duplicate content.
- The **eight ratified development sources are unchanged**: XP, SP, LP and TEST 3A, each with its `_blocky` pair.
- **EP, 2A and 4A, with their `_blocky` copies, remain hold-outs locked until S2-I8.** MLS remains a control. No leakage occurred.
- `TEST_6A_home_576i` and `TEST_7A_home_576i`, with their `_blocky` copies, are new, **uncommitted, not in the P0 allow-list, and carry no experimental role.** P0 is fail-closed against their names; Claude verified this directly.

## 4. What supersedes what

**Claude's documents:**

| Document | Status |
|---|---|
| `Claude_REVIEW_OF_ChatGPT_S2_I3_P0_Candidate_v0_1_v0_1.md` | Findings remain valid and are the basis of the fix. Its **verdict** (NOT CLEARED) is **superseded by this document** |
| `Claude_ANALYSIS_OF_Paired_Reference_Metric_and_Sample_Pool_Extension_v0_2.md` | Supersedes v0.1 (deleted). **Contains a known error** in its sections 1 and 3 - the mis-located boundary band. Do not quote its boundary/interior figures |
| `Claude_REVIEW_OF_ChatGPT_Stage2_Interim_Findings_v0_1_v0_1.md` | **Current.** Its M1 to M3 are the corrections to the analysis above |
| This document | **Current.** Authoritative on the P0 clearance and on project state |

**ChatGPT's artefacts:**

| Artefact | Status |
|---|---|
| `S2_I3_P0_IMPLEMENTATION_CANDIDATE_v0_1` (original) | **Superseded** by the revised candidate |
| `S2_I3_P0_IMPLEMENTATION_CANDIDATE_v0_1_REVISED` | **CLEARED** by this document, subject to S4 |
| `Stage2_Interim_Findings_v0_1` | **NOT cleared, NOT installed.** Deferred - section 6 |
| `S2_I3_P0B_characterise_new_source_v0_1.bat` (drafted) | **STOOD DOWN.** Never to be installed or run |

## 5. Was there backtracking, and was it warranted?

Taking this honestly, track by track.

**Track 1 - no backtracking.** Candidate, one review finding one real bug and three improvements, one corrected candidate, clearance. That is a single clean cycle and exactly how the loop is meant to work. The bug was real: an unescaped parenthesis that would have made a failure path unreliable on Windows.

**Track 2 - one catch, warranted, resolved in minutes.** Four of the six new pairs were renamed copies of existing content, two of them a hold-out and a control. Had they been admitted, the EP hold-out would have been permanently lost, and no later analysis could have recovered it. The owner deleted them within minutes and the hash check confirmed the result. This was the gate doing its job on a genuine hazard.

**Track 3 - genuine backtracking, and it was Claude's.** Three self-corrections in one document: a direction label inverted, an unstated denominator, and a mis-located measurement band whose correction **reversed** a conclusion Claude had already published. On top of that, Claude presented as a discovery something the project had already accepted as **K-03** since 2026-10-08.

That is not the review loop working well; that is Claude generating work for everyone. The corrections were warranted, because the errors were real and the inverted direction would otherwise have been written into repository knowledge. But they were avoidable.

**Root cause, stated plainly.** Tracks 1 and 2 each have a gate: a candidate gets reviewed before it runs, and a hash gets verified before it is trusted. Track 3 had no gate. Claude measured, drew conclusions, and relayed them straight into a repository-document proposal without first checking them against `06_DEBLOCK_CONCEPT.md`. Had Claude read K-02, K-03 and K-07 before measuring, it would have known the mechanism was already documented, would have placed the measurement bands correctly the first time, and would have reported magnitudes confirming existing knowledge rather than announcing a finding.

**Prevention, going forward.** Two rules, which Claude will follow without being asked:

1. Before any finding is relayed as new, check it against `06_DEBLOCK_CONCEPT.md`'s K and O items and against `05_DECISIONS_v1_2.md`. Report it as confirmation of an existing item where that is what it is.
2. Exploratory measurements stay in review correspondence and do not become repository-document proposals until a gate report needs them.

The reassuring part: **none of it reached the repository.** Every error was caught before installation, and the cost was hours of review rather than a corrupted knowledge base or a lost hold-out.

## 6. The right course, in order

**Do now, Track 1:**

1. Apply S4 to P0A, one line plus two changed invocations, or knowingly accept running as-is. Either is acceptable; Claude recommends applying it.
2. **Run P0 on the ratified eight**, one small step at a time, following `PROPOSED_OWNER_RUN_SEQUENCE_NOT_YET_CLEARED.md`, which is unchanged and sound. ChatGPT guides the steps. Note that P0A's regression prints `EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent` - that is expected, not an error.
3. Send Claude the per-source JSON files and logs. Claude checks them against the expected values it has already published: eight REGISTERED, exact P-skip counts XP 1619, XP_blocky 25635, SP 1764, SP_blocky 19010, LP 1533, LP_blocky 20300, 3A 8812, 3A_blocky 18190, and four pairs PASS.
4. Then, and only then, the separate seven-index tracking commit.

**Parallel, no urgency, Track 2:**

5. Decide the history-permanence question for the four home `.mpg` files: accept that they persist in Git history, plan a rewrite at Development Closure, or keep them out of the repository. Then the separate bounded four-file commit, after which Claude characterises both pairs and supplies the allow-list entries for a `v0_2` of the verdict file.

**Deferred, Track 3, nothing to do now:**

6. Do **not** install `Stage2_Interim_Findings_v0_1`. Claude recommends Route A: fold the measurements into the S2-I3 evidence and gate report when it is written, and let the mechanism confirmations raise the evidence level of K-03, K-07 and K-08 at `06_DEBLOCK_CONCEPT`'s next revision. This needs no decision until P0 has run.
7. Claude will issue `Claude_ANALYSIS_...v0_3` correcting the mis-located band, so the record is clean. This is housekeeping on an uncommitted review artefact and blocks nothing.

## 7. What is not happening, and stays locked

- No filtering. P0 is registration and admission only.
- EP, 2A and 4A, with their `_blocky` copies, stay locked until S2-I8, under any filename.
- Stage 1 stays frozen; the six baseline indexes are untouched.
- The P0 allow-list stays at the eight ratified sources.
- No ratified metric, rubric, threshold, fold or source role changes.
- `REVIEW_ONLY/` content, including the new `.patch`, stays out of Git.
- No new knowledge document is installed.
