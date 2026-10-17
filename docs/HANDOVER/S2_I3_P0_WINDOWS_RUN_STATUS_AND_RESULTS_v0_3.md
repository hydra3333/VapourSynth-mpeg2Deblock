# S2-I3 P0 Windows run - status, results, hygiene and continuation (v0.3)

Date: 2026-10-17; P0 run STILL IN PROGRESS
Project: VapourSynth-mpeg2Deblock
Prepared by: ChatGPT for owner continuity and Claude independent evaluation
Status: OBSERVATIONAL HANDOVER - NOT THE S2-I3 EVIDENCE/GATE REPORT; NOT P1 AUTHORISATION
Supersedes in the current tree on approved installation: `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_2.md` under D-23 v1.2 (1 A / 1 D).
Current observational checkpoint: P0A PASS; P0B COMPLETE; P0C 8/8 REGISTERED; P0D diagnostics 8/8 COMPLETE; P0D pairs 0/4 NOT RUN; global summary NOT RUN.
Independent review boundary: Claude verified v0.2 against its Linux/committed references BEFORE these later Windows admissions and diagnostics. Claude has NOT YET reviewed the accumulated P0C/P0D evidence; it HAS reviewed this v0.3 candidate (one-time review, 2026-10-18) and the corrections are incorporated below.

**TO CLAUDE / SUCCESSOR CHAT:** This v0.3 carries forward the independently checked v0.2 index/runtime facts, incorporates all owner-reported P0C and P0D console results through 3A_blocky, and captures the changed Git HEAD after the owner's second snapshot. Do NOT repeat any successful P0A, P0B, P0C or P0D diagnostics calls. The next unexecuted P0 test is PAIR_XP. Treat console PASS/REGISTERED as observed execution results, not a substitute for eventual examination of the complete `results/` tree. This handback is role continuity, not authoritative criteria. Protected hold-outs remain locked. In parallel, four identity-bearing current-tree files and the historical scrub requirement remain urgent. The owner has explicitly deferred repository hygiene work until tests finish; do not conflate the streams.

## 1. Executive status - checkpoint after eight diagnostics

| Work unit | Status at latest owner-supplied console output | Evidence boundary |
|---|---|---|
| S2-I3 P0 code | CLAUDE-CLEARED, installed | S4 plus single-BAT isolated-Python correction; fixed version used successfully |
| P0A scratch preparation | **PASS**, ERRORLEVEL=0 | six frozen index regressions, four negatives, 9/9 + 5/5 tests, runtime preflight |
| P0B six generated indexes | **6/6 PASS** | reference-equal full SHA-256, frame count, geometry and P-skip count |
| P0B LP_blocky copy | **PASS** | verified S2-I2 source and byte-identical P0 copy |
| P0B LP original | FROZEN BASELINE | repository `VHSC_samples/LG_576i_3_LP.idx` reused, not regenerated |
| P0C source admission | **8/8 REGISTERED, ERRORLEVEL=0** | exact P-skip identities; all qualifying P-picture counts match Claude Linux rehearsal |
| P0D numerical diagnostics | **8/8 COMPLETE, ERRORLEVEL=0** | full-frame runs and report-written messages; descriptive S2-I2 engine, not admission verdicts |
| P0D pair correspondence | **NOT RUN (0/4)** | XP, SP, LP, 3A still required |
| P0 summary and independent evidence review | NOT RUN | no numerical READY, P0 acceptance or P1 authorisation claimed |
| Seven-index tracking commit | NOT MADE | only after owner and Claude accept full P0 evidence |
| Filter/P1 | NOT AUTHORISED | no deblocking work is implied |

**Do not delete, overwrite or reset the owned P0 scratch results, regenerate verified indexes, or rerun completed diagnostic/admission steps.** EP, TEST 2A and TEST 4A, including every `_blocky` copy or alias, remain protected until S2-I8. TEST 6A/7A are outside the P0 allow-list. A failure or INCONCLUSIVE in any future pair test stops progress. The status document is intended to be updated/retired under D-23 only after its successor is accepted.

## 2. Reviewed baseline, actual Git state and separate urgent cleanup

Reviewed implementation/design reference: `35cd543b459a5856688f7c3795f73226e72311f8`.

**Verified Git HEAD of `main`:** `4636c33ebd7fd053149bebac8bc2dbe2d754d090`. The owner reported the short SHA `4636c33`; Claude resolved the full SHA and the commit contents by a fresh clone of GitHub `main` on 2026-10-18, so this is a verified value, not an owner-reported fragment only. Commit date 2026-10-17 20:29:59 +1030. The owner has not reported a subsequent commit; a successor must still re-run `git rev-parse HEAD` before any Git change, because HEAD may have moved after this verification. Do not treat the earlier `3f8f45a` as current HEAD.

| Commit | Owner-reported action |
|---|---|
| `6b7acc38168d0dea9278d1ba930bc09a174a50fe` | Snapshot with 58 additional tracked files including authorised 6A/7A recordings, successor role handovers and many review-only artefacts; 181 -> 239 files / 158.8 MB in Claude's audit |
| `3f8f45a77a8bbdd9d6bbc42718e6e74a2abd5e21` | Deleted one identity-bearing handover-review ZIP from current tree; historical blob remains |
| `4636c33ebd7fd053149bebac8bc2dbe2d754d090` | Owner's second snapshot, **25 added files** (Claude verified the staged shape as exactly 25 A / 0 M / 0 D against `3f8f45a`; tracked files 239 -> 264). Includes the full 15-file installed P0 overlay with corrected P0A (Claude counted exactly 15 matching paths under `experiments/stage2/`), the owner-reviewed consolidated interim knowledge document, the v0.2 Windows status handback, and 8 further review/rehearsal artefacts |

**Positive continuity result:** Current ChatGPT handover v0.8 and Claude handover v0.10 are committed; Claude independently verified their bytes against cleared candidates. The single-pass Claude-consolidated `docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md` is also committed by `4636c33`. Claude re-verified on 2026-10-18 that the committed copy is byte-identical (LF-normalised) to the document it delivered, 681 lines, and likewise for the committed `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_2.md` and the two Claude review artefacts now under `experiments/S2-I3/a/`. So the knowledge the owner wanted protected against abrupt chat loss is demonstrably preserved in the repository. The interim remains a TEMPORARY preservation bridge; the permanent Evidence and Gate Report / K-item transfers are pending.

**Outstanding current-tree hygiene:** four more identity-bearing review paths documented in section 8; two superseded handover predecessors (ChatGPT v0.7, Claude v0.9); review-only material and large nested source ZIPs. The second snapshot added further review artefacts, so the historical '44 remaining' count is **not** asserted as the exact current cleanup count. The earlier 6b7acc3 identity blobs, including the already-deleted fifth carrier, remain in Git history. The owner chose to finish P0 testing before cleanup; the exposure exists independently of test validity. All deletions require exact pathlists and staged-shape checks, never a wildcard sweep of `experiments/stage2/`.

Git `core.autocrlf=true` produced expected LF-to-CRLF warnings for the eight `.py`/`.vpy` additions in the second snapshot. This warning alone does not show source corruption; distinguish normalized Git blob hashes from working-tree hashes. Do not assume the owner's current `git status` without checking when Git work resumes.

## 3. P0A Windows failure, diagnosis and corrected PASS

Initially installed S4 overlay: 15 files = 7 BATs, 3 VPYs and 5 Python modules. First P0A run passed all six frozen-index regressions and four negative index tests, then failed in the P-skip suite:

    ModuleNotFoundError: No module named 'stage2_i3_pskip_core_v0_1'
    ERROR: S2-I3 P-skip unit tests failed
    Final ERRORLEVEL=2

Owner's diagnostic test established: portable `D:\TEST\Vapoursynth_x64_R81\python.exe` is CPython 3.14 embedded/isolated (`sys.flags.isolated=1`, `sys.flags.safe_path=True`, `python314._pth` present); module exists; Python's default search path excludes the sibling script directory; explicit `sys.path.insert(0,...)` makes import succeed; P0 scratch ROOT WAS ABSENT after failure. Isolated Python ignores `PYTHONPATH`, so setting it would not solve the problem. Claude acknowledged its original S4 testing mistakenly used a non-isolated interpreter even though earlier `-I` tests had exposed the failure.

Claude reviewed and **CLEARED** a one-BAT-only correction (`S2_I3_P0A_WINDOWS_ISOLATED_PYTHON_FIX_v0_1_FOR_CLAUDE_REVIEW.zip`): the two NumPy-dependent suites are launched through the actual VapourSynth Python using `-c` with `runpy.run_path`, explicit script-directory insertion in `sys.path` and `sys.argv=[script]`. Python modules, VPYs, and other six BATs remained byte-identical to fully rehearsed S4. No modifications were made to Python itself or `_pth`. Claude independently reproduced isolated failure and both repaired suites under Linux CPython `-I`; the **owner's Windows rerun** is the real platform proof.

Owner's corrected P0A output:

- Six accepted frozen S2-I1 `.idx` regressions PASS (LG LP, EP, MLS, TEST 2A original/blocky, TEST 4A original). Merely reading frozen metadata for regression does **not** admit or decode hold-out media.
- Four invalid-index negative tests PASS.
- The message `EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent` is **EXPECTED**, is not a failure, and is **not** permission to generate a protected hold-out index.
- P-skip suite `Ran 9 tests ... OK`; pair suite `Ran 5 tests ... OK`.
- S2-I2 synthetic runtime preflight PASS; `vspipe` produced RGB24 16x16, one frame.
- `PASS: P0A; scratch ... Run P0B for six named sources.`; final ERRORLEVEL=0. P0A owns an existing scratch directory and `P0A_READY.txt` marker.

Recorded Windows runtime:

| Component | Observed Windows P0A | Prior accepted S2-I2 / independent Claude comparison |
|---|---|---|
| VapourSynth | R81 | same context |
| BestSource plugin | `PluginVersion(major=22, minor=0)` | SAME version |
| BestSource DLL SHA-256 | `fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c` | **Identical DLL SHA-256 to committed S2-I2 run_manifest.json**, checked by Claude |
| Python | embedded `3.14.8`, MSC v.1944, x64 | isolated Windows environment; not the Linux rehearsal runtime |
| NumPy | `2.5.4` | prior committed S2-I2 and Claude rehearsal: **2.5.3** |

Claude assessed the NumPy patch difference as immaterial to P0 identity checks (uint8 equality and integer-promoted pair differences). Record it in final evidence for P0D provenance anyway. It has NOT been concealed or called an identical entire software environment. DLL binary identity is particularly relevant for comparison to the committed S2-I2 diagnostics CSVs.

**Handover lesson pending future revision:** test Python invocation under both plain and isolated/embeddable conditions; script-directory imports cannot be assumed. This correction and its full Windows evidence belong in operational knowledge, not as a new deblocking mechanism.

## 4. P0B: all index identities and cross-platform reference comparison

Actual owner P0B calls: six individual frozen-inspector generation invocations, each PASS and ERRORLEVEL=0; independently expected full SHA, frame count, geometry and skip count in generated JSON. `LP_blocky` source from accepted S2-I2 scratch verified, exact byte-copy to P0 scratch verified, ERRORLEVEL=0. Original LP index remains frozen in `VHSC_samples` and was NOT regenerated.

| Label | Frame count | Pixel geometry | P skips | Exact SHA-256 | Provenance / Windows observation |
|---|---:|---|---:|---|---|
| XP | 228 | 720x576 | 1619 | `4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127` | generated PASS |
| XP_blocky | 228 | 720x576 | 25635 | `8d0326b5975b19b36742717a80be9eaf11bc21f379f2855eb22651e94dd16b20` | generated PASS |
| SP | 192 | 720x576 | 1764 | `40a97ce1a9920cd63e45da13371e0b41ff1619fed688d6145899a300463cc5d9` | generated PASS |
| SP_blocky | 192 | 720x576 | 19010 | `7e19ca6078075e7bf7a3a34bcda0816267e4d38ad02a56e01b6b0ed726ace746` | generated PASS |
| LP | 204 | 720x576 | 1533 | `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011` | FROZEN repository original, NOT generated in P0B |
| LP_blocky | 204 | 720x576 | 20300 | `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238` | S2-I2 exact-copy PASS |
| 3A | 300 | 704x576 | 8812 | `9a60a8d24a7e4a45cbe82b4f41d232ede0e5c00624e82a8f8099f61351957f33` | generated PASS |
| 3A_blocky | 300 | 704x576 | 18190 | `e6f556dd4aaed0f4709b7c011fcf045193dccbb8abd2a01c646dddf0da893c83` | generated PASS |

**Claude independently compared all EIGHT rows on ALL FOUR values** against its prior Linux reference outputs; exact agreement. SIX new Windows indexes were generated with MSVC frozen inspector and are SHA-identical to Linux gcc frozen inspector outputs. This is strong evidence of cross-compiler, cross-platform deterministic index encoding (within these samples), and of no machine-dependent serialized fields; it is not a proof for every possible MPEG-2 stream. SEVEN indexed artefacts were checked during P0B (six generated plus LP_blocky copy); LP original is the eighth, pre-existing frozen baseline. This is the critical distinction to preserve in later evidence reports.

LP_blocky copy source: `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky\LG_576i_3_LP_blocky.idx`.
LP_blocky copy destination: `%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1\indexes\LG_576i_3_LP_blocky.idx`.

Six accepted Stage 1 frozen baseline indexes are NEVER to be rewritten. In particular `VHSC_samples\LG_576i_3_LP.idx` stays intact. No seven-index tracking commit has occurred or been authorised yet.

## 5. P0C Windows admissions: all eight REGISTERED

The following values are from the owner's actual Windows CMD output and admission logs, not derived from the Linux reference alone. Each admitted source returned `PASS: ... exact P-skip admission` and `ERRORLEVEL=0`, and each log reported the indicated REGISTERED identity and number of qualifying P pictures. Claude independently supplied the expected P-picture values before these later Windows calls; all eight observed counts agree.

| Source | Exact P-skips observed | Qualifying P pictures | Frames | Native decoded format | Windows result |
|---|---:|---:|---:|---|---|
| XP | 1619/1619 | 54 | 228 | 720x576 YUV420P8 | REGISTERED, rc=0 |
| XP_blocky | 25635/25635 | 55 | 228 | 720x576 YUV420P8 | REGISTERED, rc=0 |
| SP | 1764/1764 | 46 | 192 | 720x576 YUV420P8 | REGISTERED, rc=0 |
| SP_blocky | 19010/19010 | 46 | 192 | 720x576 YUV420P8 | REGISTERED, rc=0 |
| LP | 1533/1533 | 46 | 204 | 720x576 YUV420P8 | REGISTERED, rc=0 |
| LP_blocky | 20300/20300 | 50 | 204 | 720x576 YUV420P8 | REGISTERED, rc=0 |
| 3A | 8812/8812 | 133 | 300 | 704x576 YUV420P8 | REGISTERED, rc=0 |
| 3A_blocky | 18190/18190 | 73 | 300 | 704x576 YUV420P8 | REGISTERED, rc=0 |

Every index verification JSON reported `P_skip_count_matches_reference=true`, `status=PASS` and the expected source-specific full SHA from section 4. The LP admission explicitly used the FROZEN repository LP index; LP_blocky used the verified P0 scratch copy, not a fresh generation. P-picture counts are a valuable independent display-order/anchor check beyond the prepublished index allow-list.

**Limit of verification:** The owner showed the index-verifier JSON output, PASS lines and admission logs. The complete `pskip_identity.json`, `source_manifest.json` and `index_validation.json` for all sources have NOT been delivered for an end-to-end independent review. Do not label the full P0 gate accepted merely because all eight source invocations registered.

## 5A. P0D descriptive numerical diagnostics: all eight COMPLETE

All eight `S2_I3_P0D_diagnostics_v0_1.bat` calls were run individually, AFTER their source admissions. Each printed `REGISTERED: <label> (evidence and actual source/index hashes validated)`, its expected index-verification JSON, `COMPLETE: <label> S2-I2 numerical diagnostics (NOT admission)`, and `ERRORLEVEL=0`. Each corresponding `diagnostics.log` was displayed, progressed through the final frame and stated `reports written, no admission verdict`.

| Source | Final diagnostic frame | Output | Exit |
|---|---:|---|---:|
| XP | 228/228 | reports written, no admission verdict | 0 |
| XP_blocky | 228/228 | reports written, no admission verdict | 0 |
| SP | 192/192 | reports written, no admission verdict | 0 |
| SP_blocky | 192/192 | reports written, no admission verdict | 0 |
| LP | 204/204 | reports written, no admission verdict | 0 |
| LP_blocky | 204/204 | reports written, no admission verdict | 0 |
| 3A | 300/300 | reports written, no admission verdict | 0 |
| 3A_blocky | 300/300 | reports written, no admission verdict | 0 |

The last completed command was `call "experiments\stage2\S2_I3_P0D_diagnostics_v0_1.bat" 3A_blocky`, with the owner showing 300/300, the output format 704x576 YUV420P8, and `P0D_3A_BLOCKY_ERRORLEVEL=0`. There is **no need to rerun it**. The legacy S2-I2 numerical reports are descriptive in S2-I3; prior S2-I2 threshold BLOCKED for SP/SP_blocky/3A arises from those tests' preconditions, not index misregistration, and does not reverse exact P-skip registration.

**Not yet evaluated independently:** raw diagnostic CSV contents, exact S2-I2 CSV equivalence for the Windows P0 results, and complete diagnostic report integrity. They are expected to be checked by Claude with the full `results/` tree once four pairs and summary have been run. A report-written console line is not a numerical quality verdict.

## 6. Exact next unexecuted P0 operation: pair correspondence 1/4, XP

**Mandatory owner CMD practice:** begin a new command block with `cd /d` to the actual repository root. The first remaining command is the reviewed `S2_I3_P0D_pair_v0_1.bat` with label `XP` (the source was inspected in the cleared isolated-Python overlay; it is unchanged from cleared S4). It first rechecks both admission evidence sets, refuses an existing `PAIR_XP` output directory, uses BestSource through `vspipe`, and writes into the owned scratch `results\PAIR_XP\` directory.

```bat
cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"
call "experiments\stage2\S2_I3_P0D_pair_v0_1.bat" XP
echo P0D_PAIR_XP_ERRORLEVEL=%errorlevel%
if exist "%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1\results\PAIR_XP\pair.log" type "%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1\results\PAIR_XP\pair.log"
```

Expected from Claude's independent Linux/BestSource P0 rehearsal (not yet observed on the owner's Windows run): XP pair **PASS**, 140/228 decisive frames, zero decisive violations, mean MAE at k=0 approximately 3.53 versus best competing mean approximately 9.88, and exit code 0. The decoded numeric evidence will control; rounding in displayed means is not an exact-match gate. **STOP** for nonzero exit, FAIL, INCONCLUSIVE, missing/contradictory evidence or unexpected decisive-frame count. Do not delete existing pair results merely to force a rerun.

Then, ONE PAIR AT A TIME after XP: SP (175/192 decisive), LP (81/204 decisive), 3A (268/300 decisive). Every pair requires a strict k=0 clip-mean minimum, zero decisive-frame violations, >=20 decisive frames AND >=10% decisive, plus frame-count/geometry correspondence. The 20-frame and 10% floors were chosen after initial results; retain that disclosure in the eventual gate report. The `interim_` document section 13 owns the full method and limitations.

After all four pair tests PASS, run `S2_I3_P0D_summary_v0_1.bat`, inspect `P0_summary.json` and summary console output. `READY_FOR_P1=true` or `PASS: P0 summary numerical checks` is a **numerical evidence disposition only**, NOT permission to begin P1/filter development. Send the complete `results/` tree, source JSONs, pair evidence, diagnostics, summary and relevant logs to Claude for ONE comprehensive independent P0 evidence review; stop and send relevant JSON immediately if a pair fails.

Only after owner/Claude evidence acceptance: propose the separate exact-hash seven-index tracking installation/commit; do not touch the six frozen Stage 1 indexes. Neither this status nor the interim knowledge file authorises filtering, protected-hold-out decoding, expanded media roles, or repository-cleanup-by-wildcard.

## 7. Evidence provenance and verification limits

Owner-observed Windows evidence: original S2-I1 regression and unit suite logs from corrected P0A; six independent-index-verifier results; two LP_blocky copy verifier results; eight source admission PASS/REGISTERED logs with P-picture counts and ERRORLEVEL=0; eight diagnostic runs with completion and `diagnostics.log` all ending at expected final frame. These reports are copied from the user-supplied console record, not independently read from `%TEMP%` by ChatGPT.

Claude-supplied external reference within this project: Linux P0 rehearsal indexed all eight development sources with matching SHA/frames/dimensions/P-skips; all eight admissions gave exactly the P-picture counts shown in section 5; all four pair tests passed with the expected decisive counts; accepted S2-I2 `run_manifest.json` records the exact same BestSource DLL bytes (`fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c`). The Windows runtime used VapourSynth R81, BestSource 22.0, embedded Python 3.14.8, NumPy 2.5.4 (S2-I2 and Claude rehearsal 2.5.3). This is provenance, not a claim of identical entire runtimes.

**Unverified until evidence submission:** complete on-disk P0 `results/` content and tamper-resistant relationships, all per-source negative-control JSON, all descriptive CSV reports, all four pair outputs, and the global summary. No filter has been run. A future ChatGPT should distinguish successful console commands from formal P0 acceptance; do not manufacture unreported JSON numbers, additional runs or Git commits.

## 8. URGENT parallel repository remediation (pending; owner deferred until tests complete)

Claude scanned every GitHub-tracked text file AND the members of tracked ZIPs, and identified FOUR **still-current** paths bearing owner-identifying geographic text. Claude re-confirmed on 2026-10-18 that all four are still present at verified HEAD `4636c33`, and that the two D-23 predecessors in Commit B are also still present. Do NOT copy the identifying text into another committed report. All four are review artefacts, not accepted implementation or ratified design. The one earlier ZIP deletion does not cover them.

### Commit A: remove four remaining identity carriers FIRST when cleanup resumes

Expected staged shape: **0 ADD / 0 MODIFY / 4 DELETE**; exact tracked paths:

```
experiments/S2-I3/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_1_FOR_CLAUDE_REVIEW.md
experiments/S2-I3/S2_I3_v0_2_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip
experiments/S2-I3/S2_I3_v0_3_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip
experiments/S2-I3/ChatGPT_Handover_v0_8_FOR_CLAUDE_REVIEW.zip
```

First path contains plain searchable text; ZIP 1 includes the v0.2 design draft, ZIP 2 contains a review patch with the REMOVED identifying line, ZIP 3 contains the pre-correction ChatGPT v0.8 draft. **Important:** review diffs can carry the very text their reviewed versions successfully removed. Deleting just plaintext drafts is not enough. Use exact named `git rm -- <paths>`, inspect `git diff --cached --name-status --no-renames` for EXACTLY 4 D, then commit/push as a bounded separate change. Avoid `git add -A` and wildcards. This affects no installed P0 code, no scratch or accepted handovers.

### Commit B: remove D-23 superseded handover predecessors

Expected staged shape: **0 ADD / 0 MODIFY / 2 DELETE**; exact paths:

```
docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md
docs/HANDOVER/Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md
```

**KEEP** their independently verified current successors `..._v0_8.md`, `..._v0_10.md` and the role continuity-purpose file. Predecessor deletion is required by D-23 v1.2, and prevents a new chat loading old handover material. A distinct bounded commit from A is recommended.

### Commit C: remaining review-only artefacts after an agreed exact pathlist

Claude reported **44 further review-only paths** as of the original `3f8f45a` snapshot audit, after Commit A, including ZIPs in that earlier inventory and review requests/patches. In particular `experiments/S2-I3/VapourSynth-mpeg2Deblock-main.zip` is ~54.1 MB and embeds a COPY OF THE REPOSITORY including 16 `.mpg` (~49 MB) and frozen indexes - duplication of Restricted Media. FIVE review artefacts were also committed under `experiments/stage2/`, which otherwise holds **accepted implementation code**: DO NOT delete accepted code with a blanket `git rm` or delete `experiments/stage2` as a folder. Claude has now identified the exact additional review-only paths that `4636c33` contributed, so the Commit C candidate pool is **44 (as at `3f8f45a`) + 8 = 52 paths**. The eight new ones are:

```
experiments/S2-I3/Claude_DIFF_CLEARANCE_S2_I3_P0_S4_Candidate_v0_1.md
experiments/S2-I3/Claude_REVIEW_OF_ChatGPT_P0A_Windows_Isolated_Python_Fix_v0_1_v0_1.md
experiments/S2-I3/S2_I3_P0A_WINDOWS_ISOLATED_PYTHON_FIX_v0_1_FOR_CLAUDE_REVIEW.zip
experiments/S2-I3/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_1_FOR_CLAUDE_2026-10-17.md
experiments/S2-I3/a/1.interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md
experiments/S2-I3/a/2.S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_2_FOR_CLAUDE_2026-10-17.md
experiments/S2-I3/a/Claude_URGENT_Repository_Hygiene_Finding_3f8f45a_v0_1.md
experiments/S2-I3/a/Claude_VERIFICATION_OF_S2_I3_P0_Windows_Run_Status_v0_1.md
```

None of these eight carries identifying text: Claude scanned all ten text files added by `4636c33` and all 19 members of the new P0A fix ZIP, and found no occurrence. So `4636c33` added review clutter but **no new identity carrier**; Commit A remains exactly four paths. The full 52-path list still needs owner agreement before Commit C. Do NOT perform Commit C by wildcard; file classification and exact list remain pending. The four authorised 6A/7A recordings, both cleaned successor handovers, and all files already present at 35cd543 should be retained under Claude's current recommendation.

The history caveat applies to all above: the original snapshot `6b7acc3` retains deleted blobs in Git history; a push of deletion commits only cleans CURRENT HEAD. The existing Development Closure history scrub under D-23 is intended also to remove historical owner-identifying text; third-party clones/forks/caches may nevertheless retain it. If owner judges immediate public exposure unacceptable, a present-day history rewrite is a SEPARATE, disruptive owner decision; do not silently rewrite. Mark all five identity carriers (four above and the previously deleted corrected handover review ZIP) for that future scrub. The four recorded media in `6b7acc3` also have historical permanence implications independent of their current tree presence.

**Prevention lesson for next role handovers:** a review ZIP/diff/superseded draft often retains removed sensitive text; untracked working directories must not be swept into commits (`git add -A`). Inspect ZIP members and member names, not only loose text. After cleanup, consider an agreed `experiments/*.zip` ignore pattern or other targeted rule (a new rule needs bounded proposal and owner approval), and continue exact-path staging.

## 9. Parallel interim knowledge bridge, now installed; final transfer pending

The owner explicitly requested ONE temporary consolidated `interim_` knowledge document to prevent loss of corrected Stage 2 measurements and two chats' methodological knowledge. Claude performed its **single requested consolidation pass**, verified the figures, added sections 11-18 (the committed document ends at section 18, `Consolidation record`, at 681 lines) and corrected installation wording. No further review cycle was requested. The owner installed it in the `4636c33` snapshot at:

`docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md`

It remains a TEMPORARY preservation bridge, not a competing ratified design authority. The agreed Route A permanent transfer has NOT happened: quantitative data, limitations and methodological provenance go into the eventual S2-I3 Evidence and Gate Report; durable evidence upgrades go into `06_DEBLOCK_CONCEPT.md` K-03, K-07 and K-08, under independent review and owner ratification. The interim's section 9 is the explicit transfer/retirement checklist. Do not revise it simply because more P0 console runs have succeeded; those belong in this status handback and later gate report.

The installed role handovers, ChatGPT v0.8 and Claude v0.10, are known to have earlier as-at states. Successors MUST read this newer v0.3 checkpoint and verify the live repository rather than repeating v0.8's obsolete "S4 awaits review" next action. The separate ChatGPT handover update to v0.9, if prepared, must replace v0.8 through D-23, not sit alongside both as competing current versions.

## 10. Successor / next developer instructions

1. Verify live Git HEAD/branch and staged/working-tree state when needed; the latest owner-reported successfully pushed commit is short `4636c33`. Do not assume a cleanup commit, a pair run, or a later ratification exists without evidence.
2. Continue at **PAIR_XP** from section 6, NOT P0A/B/C or any of the eight completed P0D diagnostics. One source/pair per reviewed CMD block, beginning with `cd /d`, and STOP on errors or INCONCLUSIVE.
3. Follow with SP, LP and 3A pair runs, and then the global P0 summary. Keep `READY` numerical only; do not begin filtering, new media characterization or hold-out work.
4. Preserve scratch folder `%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1`, seven verified non-baseline index bytes and frozen original LP. Submit the complete evidence tree to Claude once pairs and summary finish; only then pursue owner acceptance and a separate seven-index tracking commit.
5. Owner has deferred the urgent repository hygiene operations until tests finish. Once resumed, prioritize the exact four paths in Commit A, the two superseded handover files in Commit B, then get an up-to-date reviewed exact pathlist for Commit C. **Tree deletion cannot remove identity text from prior snapshot history.** Never run broad `git add -A` or wildcard `git rm` as routine cleanup.
6. Protect the installed `interim_` bridge until its detailed knowledge transfer checklist is satisfied; do not treat raw exploratory pixel measurements as P0 gate results or permanent filter evidence.

**Reporting vocabulary:** `PASS`/`REGISTERED` for the specific observed Windows steps; descriptive diagnostics `COMPLETE` without admission verdict; future pair PASS only after actually executed; summary `READY` numerical; independent P0 gate acceptance is a separate later owner/Claude decision.
