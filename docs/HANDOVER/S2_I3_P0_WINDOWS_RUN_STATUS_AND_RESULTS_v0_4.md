# S2-I3 P0 Windows run - status, results, hygiene and continuation (v0.4)

Date: 2026-10-18; **P0 EXECUTION COMPLETE; owner acceptance decision outstanding**
Project: VapourSynth-mpeg2Deblock
Prepared by: **Claude, at owner request, standing in for the ChatGPT role.** This document belongs to the
ChatGPT document family. The owner asked Claude to draft v0.4 directly rather than wait for the ChatGPT
chat. **Consequence to record honestly: v0.4 has NOT had independent cross-role review, because its
author is the project's reviewer and cannot independently review its own draft.** Everything it asserts
about the evidence is independently verified against the evidence tree; everything it asserts about
project process carries only one role's judgement. The ChatGPT role should review it when available.
Status: OBSERVATIONAL HANDOVER - NOT THE S2-I3 EVIDENCE/GATE REPORT; NOT P1 AUTHORISATION
Supersedes in the current tree on approved installation: `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_3.md` AND the still-present `..._v0_2.md`, under D-23 v1.2. Expected staged shape **1 A / 0 M / 2 D** (see section 8).
Current observational checkpoint: P0A PASS; P0B COMPLETE; P0C 8/8 REGISTERED; P0D diagnostics 8/8 COMPLETE; **P0D pairs 4/4 PASS; global summary RUN, `READY_FOR_P1=true` numerical only; Claude independent evidence review COMPLETE, verdict ACCEPTED/gate PASS recommended.**
Independent review boundary: Claude has now reviewed the COMPLETE `results/` tree (137 files) and recomputed both headline results from raw per-item data. See `docs/Claude_P0_EVIDENCE_REVIEW_AND_GATE_RECOMMENDATION_v0_3.md`. **What remains is the owner's acceptance decision, not further verification.**

**TO A SUCCESSOR CHAT IN EITHER ROLE:** **P0 execution is finished. Do NOT re-run any P0 step** - not P0A, not P0B, not the eight P0C admissions, not the eight P0D diagnostics, not the four pair tests, not the summary. The scripts refuse to overwrite existing output and the evidence must stay intact. The complete `results/` tree has been independently reviewed and the review recommends the gate be recorded as PASSED. **The next action is the owner's acceptance decision**, after which the seven-index tracking commit becomes available and P1 authorisation becomes a separate request. Protected hold-outs remain locked regardless of filename. Repository hygiene remains outstanding and is now the largest open item: four identity-bearing current-tree files, three superseded handover predecessors, and a ~52-path review-artefact cleanup. The owner deferred that until tests finished; tests have now finished.

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
| P0D pair correspondence | **4/4 PASS, ERRORLEVEL=0** | decisive 140/175/81/268, zero decisive violations, strict k=0 minimum, both floors met |
| P0 global summary | **RUN**, `READY_FOR_P1=true`, `problems: []` | `ready_is_numerical_only=true`; all 8 diagnostics marked `REPORTED_NOT_GATE` |
| Claude independent evidence review | **COMPLETE: ACCEPTED, gate PASS recommended** | 137 files; both headline results recomputed from raw per-item data; no MUST |
| **Owner acceptance decision** | **OUTSTANDING - this is the next action** | nothing further is gated on verification |
| Seven-index tracking commit | NOT MADE; **Claude precondition now met** | awaits owner acceptance only; `7 A / 0 M / 0 D` |
| Filter/P1 | NOT AUTHORISED | no deblocking work is implied |

**Do not delete, overwrite or reset the owned P0 scratch results, regenerate verified indexes, or rerun any completed step.** EP, TEST 2A and TEST 4A, including every `_blocky` copy or alias, remain protected until S2-I8. TEST 6A/7A are outside the P0 allow-list. **Retirement condition for this document family:** once the S2-I3 Evidence and Gate Report exists and both role handovers are refreshed, the P0 event log belongs there and this status family should be RETIRED rather than carried to v0.5. It is a temporary operational record, like the `interim_` bridge.

## 2. Reviewed baseline, actual Git state and separate urgent cleanup

Reviewed implementation/design reference: `35cd543b459a5856688f7c3795f73226e72311f8`.

**Verified Git HEAD of `main`:** `f4a40e13251ace8201317ef6546353c4fbe6c679`, commit date 2026-10-18 07:33:10 +1030, subject `SNAPSHOT`. Claude resolved it by a fresh clone of GitHub `main` on 2026-10-18 and verified its staged shape as exactly **2 A / 0 M / 0 D** against `4636c33`, adding `docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_9.md` and `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_3.md`; tracked files 264 -> 266. **No predecessor deletions were made in that commit**, which is why three ChatGPT handover versions and two status versions now coexist (section 8). A successor must still re-run `git rev-parse HEAD` before any Git change, because HEAD may have moved after this verification.

| Commit | Owner-reported action |
|---|---|
| `6b7acc38168d0dea9278d1ba930bc09a174a50fe` | Snapshot with 58 additional tracked files including authorised 6A/7A recordings, successor role handovers and many review-only artefacts; 181 -> 239 files / 158.8 MB in Claude's audit |
| `3f8f45a77a8bbdd9d6bbc42718e6e74a2abd5e21` | Deleted one identity-bearing handover-review ZIP from current tree; historical blob remains |
| `f4a40e13251ace8201317ef6546353c4fbe6c679` | **Current HEAD.** Installed ChatGPT handover v0.9 and status v0.3, both byte-verified by Claude as the corrected files it returned. 2 A / 0 M / 0 D; no predecessors deleted |
| `4636c33ebd7fd053149bebac8bc2dbe2d754d090` | Owner's second snapshot, **25 added files** (Claude verified the staged shape as exactly 25 A / 0 M / 0 D against `3f8f45a`; tracked files 239 -> 264). Includes the full 15-file installed P0 overlay with corrected P0A (Claude counted exactly 15 matching paths under `experiments/stage2/`), the owner-reviewed consolidated interim knowledge document, the v0.2 Windows status handback, and 8 further review/rehearsal artefacts |

**Positive continuity result:** Current ChatGPT handover v0.8 and Claude handover v0.10 are committed; Claude independently verified their bytes against cleared candidates. The single-pass Claude-consolidated `docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md` is also committed by `4636c33`. Claude re-verified on 2026-10-18 that the committed copy is byte-identical (LF-normalised) to the document it delivered, 681 lines, and likewise for the committed `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_2.md` and the two Claude review artefacts now under `experiments/S2-I3/a/`. So the knowledge the owner wanted protected against abrupt chat loss is demonstrably preserved in the repository. The interim remains a TEMPORARY preservation bridge; the permanent Evidence and Gate Report / K-item transfers are pending.

**Outstanding current-tree hygiene:** four more identity-bearing review paths documented in section 8; two superseded handover predecessors (ChatGPT v0.7, Claude v0.9); review-only material and large nested source ZIPs. The second snapshot added further review artefacts, so the historical '44 remaining' count is **not** asserted as the exact current cleanup count. The earlier 6b7acc3 identity blobs, including the already-deleted fifth carrier, remain in Git history. The owner chose to finish P0 testing before cleanup. **Testing is now finished, so this is the largest
open item.** The exposure exists independently of test validity. All deletions require exact pathlists and staged-shape checks, never a wildcard sweep of `experiments/stage2/`.

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

## 6. P0D pair correspondence: all four PASS, and the actual next action

All four pair tests were run individually and all four PASSED with `ERRORLEVEL=0`. The decisive-frame
counts match Claude's independent Linux rehearsal expectations exactly, which were published before the
Windows runs existed.

| Group | Status | Decisive | Expected | Violations | Mean MAE k=0 | Best competing mean | Decisive fraction |
|---|---|---:|---:|---:|---:|---:|---:|
| XP | PASS | 140/224 | 140 | 0 | 3.5250 | 9.8761 | 61.4% |
| SP | PASS | 175/188 | 175 | 0 | 3.2322 | 13.9828 | 91.1% |
| LP | PASS | 81/200 | 81 | 0 | 4.3876 | 9.9337 | 39.7% |
| 3A | PASS | 268/296 | 268 | 0 | 5.5276 | 19.9471 | 89.3% |

Every group satisfied the full predeclared rule: equal original and blocky frame counts, a strict
clip-mean minimum at k=0 (`strict_zero_argmin: true`), zero decisive-frame violations, and both
sample-size floors - at least 20 decisive frames and at least 10% decisive - with margin, the tightest
being LP at 81 frames and 39.7%. The common-interior frame counts 224/188/200/296 are each four fewer
than the clip length, the correct consequence of a k = -2..+2 window needing two frames of margin at
each end. **The 20-frame and 10% floors were chosen after seeing preflight data; that disclosure must
travel with the rule wherever it is published.** The evidence files carry it themselves in `floor_note`.

The global summary was then run. `P0_summary.json` reports `READY_FOR_P1: true` with
`ready_is_numerical_only: true`, `requires_owner_and_claude_gate_review: true`, `problems: []`, all
eight sources `REGISTERED`, all four pairs `PASS`, and all eight diagnostics `REPORTED_NOT_GATE`.

### 6.1 Claude's independent evidence review is complete

The complete `results/` tree - 137 files, 8 sources x 16 plus 4 pair directories x 2 plus the summary -
was supplied to Claude and reviewed. **Verdict: P0 EVIDENCE ACCEPTED, gate PASS recommended, no MUST
against the evidence.** Four SHOULDs, all additive records for the eventual Evidence and Gate Report.
The full document is `docs/Claude_P0_EVIDENCE_REVIEW_AND_GATE_RECOMMENDATION_v0_3.md`.

The review did not rely on reported verdicts. It **recomputed** both headline results from the raw
per-item data the evidence carries: admission identity re-summed from `per_P_picture` for all eight
sources, and the decisive rule re-evaluated over all 908 `frame_evidence` records for the four pairs.
Both reproduce exactly, with no per-frame flag inconsistency. It also confirmed the media hash chain is
closed (each admission `source_sha256` equals the corresponding pair-test hash, so the pair tests
provably ran on the admitted bytes), all eight media hashes are distinct, runtime is byte-identical
across all eight admissions with the BestSource DLL identical to accepted S2-I2, and that no protected
hold-out or non-allow-list media name appears anywhere in the 137 files.

Two results worth carrying into the Gate Report:

- **The threshold-free method is vindicated by the owner's own run.** A one-pixel horizontal shift of
  3A still reproduces **93.08%** of its skipped-macroblock blocks exactly; previous-display reaches
  96.72% on 3A and 94.85% on LP. Any tolerance-based registration test below roughly 93% would have
  passed a misregistered 3A. On 3A the true position has 0 non-matching blocks of 8812 against 289 for
  the best competing hypothesis. This supersedes the 90.2% rehearsal figure as the method
  justification because it is owner-run evidence.
- **`Q_fixed` re-derives exactly from the diagnostic CSVs** for all eight sources - XP 14, SP 16, LP 18,
  3A 14, and every blocky single-valued at 62 - and the transform mix confirms within 0.1 to 0.8
  percentage points, including 3A's opposite FRAME-dominant regime at 68.3%.

### 6.2 The next action is the owner's acceptance decision

**No further execution or verification is gated.** The sequence from here:

1. **Owner accepts (or does not accept) the P0 evidence**, having read Claude's review. This is a
   judgement call reserved to the owner and is the only thing currently blocking.
2. On acceptance, the **seven-index tracking commit** becomes available: `7 A / 0 M / 0 D`, exact
   SHA-verified admitted bytes only, `git ls-files --eol` reporting `-text` for every staged `.idx`,
   and the six frozen Stage 1 indexes untouched. **LP original is not in this commit** - it is the
   pre-existing frozen baseline, which is why the count is seven and not eight.
3. **Repository hygiene** (section 8), now the largest open item since testing is finished.
4. **P1 fixed-QP luma kernel development** requires a separate explicit owner authorisation. A
   numerical `READY_FOR_P1` is not that authorisation.
5. **Route A knowledge transfer** into the S2-I3 Evidence and Gate Report and `06_DEBLOCK_CONCEPT.md`
   K-03/K-07/K-08, after which the `interim_` bridge and this status family can both be retired.

Preserve the P0 scratch root `%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1` and its results in place.
No filtering has been run and none is authorised.

## 7. Evidence provenance and verification limits

Owner-observed Windows evidence: original S2-I1 regression and unit suite logs from corrected P0A; six independent-index-verifier results; two LP_blocky copy verifier results; eight source admission PASS/REGISTERED logs with P-picture counts and ERRORLEVEL=0; eight diagnostic runs with completion and `diagnostics.log` all ending at expected final frame. These reports are copied from the user-supplied console record, not independently read from `%TEMP%` by ChatGPT.

Claude-supplied external reference within this project: Linux P0 rehearsal indexed all eight development sources with matching SHA/frames/dimensions/P-skips; all eight admissions gave exactly the P-picture counts shown in section 5; all four pair tests passed with the expected decisive counts; accepted S2-I2 `run_manifest.json` records the exact same BestSource DLL bytes (`fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c`). The Windows runtime used VapourSynth R81, BestSource 22.0, embedded Python 3.14.8, NumPy 2.5.4 (S2-I2 and Claude rehearsal 2.5.3). This is provenance, not a claim of identical entire runtimes.

**Now verified.** The complete `results/` tree was supplied and independently reviewed on 2026-10-18:
all per-source admission and index-validation JSON, all negative-control blocks, all descriptive CSV
reports, all four pair outputs and the global summary. The remaining gap is no longer verification but
**owner acceptance**. Still true and still worth stating: no filter has been run; a successor must
distinguish successful console commands from formal P0 acceptance; and nobody should manufacture
unreported JSON numbers, additional runs or Git commits.

**One item flagged for before S2-I4, not for now.** All four real captures use the MPEG-2 non-linear
quantiser table. LP carries 4.23% of its macroblock-edge weight above `quantiser_scale` 62, as a clamp
spike of 49,113 occurrences at the ceiling value 112, where indexed QP saturates and stops
discriminating severity. A 62 from the linear table is not the same step size as a 62 from the
non-linear table. **Whether `q_scale_type` is recoverable from the current index has not been
confirmed**; `02_INDEX_FORMAT_SPEC` records `q` and `q_update` but not evidently the table selector.
That is a D-13 extra-metadata question to settle before S2-I4 rather than during it. It does not affect
P0, which uses no QP values, nor P1, which is fixed-QP.

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

### Commit B: remove D-23 superseded handover predecessors - NOW THREE PATHS

At HEAD `f4a40e13251ace8201317ef6546353c4fbe6c679` the `docs/HANDOVER/` directory holds **three**
ChatGPT handover versions and **two** Claude handover versions, because neither the `4636c33` nor the
current snapshot deleted any predecessor. Expected staged shape **0 ADD / 0 MODIFY / 3 DELETE**:

```
docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md
docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md
docs/HANDOVER/Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md
```

**KEEP** the current successors `ChatGPT_..._v0_9.md` and `Claude_..._v0_10.md`, both byte-verified by
Claude, and the role continuity-purpose file. The fourth predecessor,
`S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_2.md`, is **not** listed here because it is removed by the
installation of this v0.4 instead (see the header: 1 A / 0 M / 2 D). Keeping the two cleanups separate
avoids one commit that both installs and prunes across two document families.

Three superseded handover versions coexisting is the specific harm D-23 exists to prevent. v0.8 in
particular still presents S4 as awaiting review, which is now two gates out of date, and v0.7 is older
still.

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

1. Verify live Git HEAD/branch and staged/working-tree state; HEAD was `f4a40e13251ace8201317ef6546353c4fbe6c679` on 2026-10-18 and may have moved. Do not assume a cleanup commit or a later ratification exists without evidence.
2. **Run nothing in P0.** Execution is complete: P0A, P0B, eight P0C admissions, eight P0D diagnostics, four pair tests and the global summary have all run and been independently reviewed. Re-running would at best be refused by the scripts and at worst damage the evidence.
3. Establish whether the owner has accepted the P0 evidence. If not, that decision is the only open blocker. If accepted, the seven-index tracking commit is next, then hygiene, then a separate P1 authorisation request.
4. Preserve scratch folder `%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1`, the seven verified non-baseline index bytes and the frozen original LP index.
5. Owner has deferred the urgent repository hygiene operations until tests finish. Once resumed, prioritize the exact four paths in Commit A, the two superseded handover files in Commit B, then get an up-to-date reviewed exact pathlist for Commit C. **Tree deletion cannot remove identity text from prior snapshot history.** Never run broad `git add -A` or wildcard `git rm` as routine cleanup.
6. Protect the installed `interim_` bridge until its detailed knowledge transfer checklist is satisfied; do not treat raw exploratory pixel measurements as P0 gate results or permanent filter evidence.

**Reporting vocabulary:** `PASS`/`REGISTERED` for the specific observed Windows steps; descriptive diagnostics `COMPLETE` without admission verdict; future pair PASS only after actually executed; summary `READY` numerical; independent P0 gate acceptance is a separate later owner/Claude decision.
