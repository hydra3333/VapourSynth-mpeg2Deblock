# S2-I3 P0 Windows run - status, results, and continuation handback v0.1

Date: 2026-10-17 (run in progress)
Project: VapourSynth-mpeg2Deblock
Prepared by: ChatGPT, for Claude independent verification and owner continuity
Status: WORKING EVIDENCE RECORD - NOT A GATE REPORT, NOT RATIFIED, NOT PERMISSION FOR P1

## 1. Executive state / exact stopping point

- P0 implementation code review: COMPLETE. Claude cleared the S4 candidate, then the narrow Windows isolated-Python correction, with no outstanding MUST or SHOULD findings.
- P0A preparation: PASS under the owner's Windows environment, final ERRORLEVEL=0.
- P0B: COMPLETE. All SIX generated scratch indexes passed exact independent-SHA verification, and the separately sourced LP_blocky index was copied byte-for-byte from accepted S2-I2 scratch and verified. The original LP index remains the frozen repository index. Thus all eight allow-listed indexes are available for P0C.
- P0C: XP is REGISTERED, exact P-skip 1619/1619, P pictures=54, 228 frames, vspipe successful, ERRORLEVEL=0. No other source has yet been reported admitted.
- NEXT UNEXECUTED OPERATION: P0C admission of XP_blocky, individually. Do NOT repeat successful P0A/P0B or XP admission; scripts refuse overwrite and the scratch folder is deliberately retained.
- P0D per-source diagnostics, four paired-correspondence tests, global summary, independent evidence review, and seven-index tracking commit: NOT YET RUN / NOT YET APPROVED.
- No filtering and no P1 authorisation. EP, TEST_2A, TEST_4A, and all their blocky versions are LOCKED until S2-I8 regardless of filename. The unassigned 6A/7A recordings are outside the eight-source allow-list.

## 2. Authority, versions, and provenance

This is a task-specific observational handback; it does not amend the ratified design or repository knowledge. The governing design is the accepted S2-I3 multi-source design v0.3 and Stage 2 experiment design v0.7, alongside repository decisions and deblocking concept. The technical candidate's originally reviewed repository baseline was:

    35cd543b459a5856688f7c3795f73226e72311f8

The owner made an explicit interim snapshot and pushed it:

    6b7acc38168d0dea9278d1ba930bc09a174a50fe  SNAPSHOT after handovers updated

Then removed an offending handover review ZIP from the current tree in a separate pushed commit:

    3f8f45a77a8bbdd9d6bbc42718e6e74a2abd5e21  Remove handover review ZIP containing identity text

`3f8f45a...` is the last owner-reported HEAD. Snapshot cleanup is explicitly deferred. The snapshot commit included many interim/review assets, four new 6A/7A MPG samples, and both new and old role handover revisions; it is NOT a clean handover-version swap. The removed ZIP still exists in historical Git objects at `6b7acc3`, so deleting it from current HEAD did not remove its previously published contents. Separate repository-history/privacy cleanup decision remains outside P0.

The last observed pre-P0 stage2 status listed the 15 implementation overlay files as untracked. The owner also reported `experiments/S2-I3/Claude_DIFF_CLEARANCE_S2_I3_P0_S4_Candidate_v0_1.md` as untracked. There has been no reported P0 commit. Do not assume a newly created Git status without checking.

Source basis of THIS report: owner's actual CMD console outputs provided to ChatGPT during the run; Claude's supplied clearance documents; and direct inspection of the final correction ZIP's BAT and verifier source. ChatGPT has NOT read the owner's local scratch evidence files directly. Values in sections 3-5 are transcribed from console reports; the full index reference table is independently cross-checked against the inspected verifier's EXPECTED map.

Relevant reviewer documents:

- `Claude_DIFF_CLEARANCE_S2_I3_P0_S4_Candidate_v0_1.md` - original S4 final clearance, now superseded for P0A alone.
- `Claude_REVIEW_OF_ChatGPT_P0A_Windows_Isolated_Python_Fix_v0_1_v0_1.md` - narrow fix cleared with no MUST/SHOULD.
- Candidate archive: `S2_I3_P0A_WINDOWS_ISOLATED_PYTHON_FIX_v0_1_FOR_CLAUDE_REVIEW.zip` (15 REPO_OVERLAY files; 1 BAT change against S4; REVIEW_ONLY contents must never be copied into implementation or committed).

## 3. P0A: first failure, root cause, correction, actual Windows PASS

First owner run installed the 15 S4 overlay files in `experiments/stage2`. Six frozen S2-I1 index regressions and four negative index tests passed, but the first P-skip unit suite failed before scratch creation:

    ModuleNotFoundError: No module named 'stage2_i3_pskip_core_v0_1'
    ERROR: S2-I3 P-skip unit tests failed
    Final ERRORLEVEL=2

Owner's diagnostic evidence:

- Interpreter: `D:\TEST\Vapoursynth_x64_R81\python.exe`.
- `sys.flags.isolated=1`, `sys.flags.safe_path=True`; `python314._pth` exists.
- The sibling `.py` module existed on disk, but `importlib.util.find_spec(...)` returned None with the default isolated search path.
- Explicitly inserting `experiments\stage2` in `sys.path` made import PASS.
- The P0 scratch root was ABSENT after failure: preparation stopped before `mkdir`. No cleanup was necessary.

Root cause: an embeddable/isolated Python does not implicitly add the launched script's directory to its search path, and isolated mode ignores PYTHONPATH. Claude acknowledged that its original S4 non-isolated Linux launch test was insufficient; prior `python3 -I` failures had already exposed the issue.

Claude cleared the narrow correction to `S2_I3_P0A_prepare_campaign_v0_1.bat`. Its two unit suite invocations still use the intended VapourSynth Python but use `-c` with `runpy.run_path`, `sys.path.insert(0,os.path.dirname(script))`, and `sys.argv=[script]`. The other SIX BATs and all EIGHT Python/VPY files remain byte-identical to cleared S4. The owner replaced only this one BAT. Python itself and the `python314._pth` file were not changed.

Corrected P0A Windows rerun: PASS. Actual console evidence:

- Six accepted frozen index regression summaries PASS: `LG_576i_3_LP`, `LG_576i_4_EP`, `LG_576i_5_MLS`, `TEST_2A_A001`, `TEST_2A_A001_blocky`, `TEST_4A_A003`. This is index-metadata regression reading accepted baselines, NOT decoding or admitting hold-out media.
- Four malformed/unsupported index negative cases PASS.
- `EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent` printed as expected; NOT an error and NOT permission to generate a hold-out index now.
- P-skip unit suite: `Ran 9 tests ... OK`.
- Pair unit suite: `Ran 5 tests ... OK`.
- Runtime: VapourSynth R81; BestSource plugin 22.0, DLL SHA256 `fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c`; NumPy 2.5.4; embeddable Python 3.14.8 (MSC v.1944 64-bit AMD64). Runtime preflight's synthetic checks passed, vspipe reported RGB24 16x16 1 frame.
- Final message: `PASS: P0A; scratch "%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1". Run P0B for six named sources.` [Actual printed location was TEMP-expanded.]
- Final ERRORLEVEL=0. Therefore P0A created the owned scratch campaign tree and P0A_READY marker.

Lesson for role handovers, proposed for future ratification: test both ordinary and isolated (`-I` / embeddable `_pth`) Python import behaviour; the calling interpreter and its import path are BOTH environment dependencies. Explicit sys.path injection is required for this invocation pattern, not PYTHONPATH.

## 4. P0B: all six generated indexes and LP_blocky exact copy

P0B uses frozen inspector, ffmpeg video elementary-stream demux, analyzer, independent SHA and P-skip verifier. One allowed source per invocation; temporary `.m2v` is deleted; verified `.idx` and logs remain in owned scratch. The owner invoked six P0B generation calls individually; every call returned `PASS: <label> scratch index verified against independent Claude SHA` and ERRORLEVEL=0. The separate LP_blocky-copy script verified the accepted S2-I2 source and the destination identically, without regeneration.

Legend: `generated PASS` and `copied PASS` are actual owner CMD observations; `frozen reference` is the pre-existing accepted index, not newly generated in P0B. Hashes are full SHA-256 values. Dimensions are pixels. The P-skip values for generated/copied rows were actually reported in the verification JSON and matched the reference; LP's 1533 is from the inspected pre-agreed verifier EXPECTED map, not a fresh P0B execution.

| Label | Frames | Dimensions | P skips | SHA-256 | Index state at P0B exit |
|---|---:|---|---:|---|---|
| XP | 228 | 720x576 | 1619 | `4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127` | generated PASS, rc=0 |
| XP_blocky | 228 | 720x576 | 25635 | `8d0326b5975b19b36742717a80be9eaf11bc21f379f2855eb22651e94dd16b20` | generated PASS, rc=0 |
| SP | 192 | 720x576 | 1764 | `40a97ce1a9920cd63e45da13371e0b41ff1619fed688d6145899a300463cc5d9` | generated PASS, rc=0 |
| SP_blocky | 192 | 720x576 | 19010 | `7e19ca6078075e7bf7a3a34bcda0816267e4d38ad02a56e01b6b0ed726ace746` | generated PASS, rc=0 |
| LP | 204 | 720x576 | 1533 | `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011` | immutable accepted repository index; not newly generated |
| LP_blocky | 204 | 720x576 | 20300 | `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238` | source/destination verified, byte copy PASS, rc=0 |
| 3A | 300 | 704x576 | 8812 | `9a60a8d24a7e4a45cbe82b4f41d232ede0e5c00624e82a8f8099f61351957f33` | generated PASS, rc=0 |
| 3A_blocky | 300 | 704x576 | 18190 | `e6f556dd4aaed0f4709b7c011fcf045193dccbb8abd2a01c646dddf0da893c83` | generated PASS, rc=0 |

LP_blocky source:

    %TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky\LG_576i_3_LP_blocky.idx

LP_blocky destination:

    %TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1\indexes\LG_576i_3_LP_blocky.idx

Both printed the same hash and 20300/20300 P-skip count, and the script reported `PASS: LP_blocky scratch index bytes copied without regeneration.` No seven-index tracking commit has been made or authorised yet.

## 5. P0C: first admitted source, XP

Owner's actual command:

    call "experiments\stage2\S2_I3_P0C_admit_source_v0_1.bat" XP

Owner's console output established:

- Index validation JSON printed `label=XP`, status PASS, SHA256 `4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127`, 228 frames, 720x576, P_skip_mb_count=1619, matches reference.
- `PASS: XP exact P-skip admission`, ERRORLEVEL=0.
- `results\XP\admission.log` content included `S2-I3 P-skip XP: REGISTERED, exact=1619/1619, P pictures=54`.
- BestSource/vspipe reported 720x576, 228 frames, 25 fps, YUV420P8 (8-bit 4:2:0).
- Programmed P0C output artefacts under `results\XP\`: `index_validation.json`, `source_manifest.json`, `pskip_identity.json`, plus `admission.log`. Their full contents have NOT been separately supplied to Claude/ChatGPT yet. Console REGISTERED is a successful run, not a substitute for independent gate examination.

No execution evidence has been reported for XP_blocky, SP, SP_blocky, LP, LP_blocky, 3A or 3A_blocky admissions yet. NO P0D tests have been run.

## 6. Scratch location, evidence inventory, and preservation

Repository relative implementation: `experiments\stage2\` contains the 15 candidate files (14 S4-identical, one corrected P0A BAT). Preserve this installed overlay. Never copy `REVIEW_ONLY/` into implementation.

Owned P0 scratch root:

    %TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1

Expected/created substructure from P0A: `indexes\`, `results\`, and `P0A_READY.txt`.

- `indexes\<stem>.idx`, `indexes\<stem>.log`, and `indexes\<stem>.idx.verification.json` for six generated indexes; copied LP_blocky verification JSON also exists.
- LP original index is `VHSC_samples\LG_576i_3_LP.idx` and MUST remain unmodified.
- `results\XP\admission.log` and three JSON evidence files from the completed XP admission.
- Further `results\<label>\` directories should only be created when their one-source P0C invocation succeeds/attempts; P0C refuses pre-existing output directories. Do not delete existing directories to retry casually.
- `P0A_READY.txt` means preparation succeeded; it is NOT global P0 readiness.
- Preserve raw scratch evidence and scripts until Claude independently verifies the run. Do not commit the scratch folder, logs, or decoded media. Do not regenerate any admitted/verified index during later tracking.

## 7. Next Windows step and remaining ordered work

Immediate NEXT step, as agreed with owner, ONE source per execution/review (commands are shown separately here for transfer; the next developer chat should still inspect each result). Always begin each owner CMD command sequence with the mandatory `cd /d`:

```bat
cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"

call "experiments\stage2\S2_I3_P0C_admit_source_v0_1.bat" XP_blocky

echo P0C_XP_BLOCKY_ERRORLEVEL=%errorlevel%

if exist "%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1\results\XP_blocky\admission.log" type "%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1\results\XP_blocky\admission.log"
```

Expected XP_blocky: exact 25635/25635 P skips, REGISTERED, frames=228, rc=0. STOP on fail/inconclusive; do not redo already-registered XP. Do NOT claim XP_blocky passed until owner supplies output.

Then separately run P0C, in this order, after each preceding PASS: `SP`, `SP_blocky`, `LP`, `LP_blocky`, `3A`, `3A_blocky`. Expected P skips respectively 1764, 19010, 1533, 20300, 8812, 18190. `LP` must use the frozen repository index; `LP_blocky` must use its verified copied index. Every admission must produce REGISTERED exact identity and zero rc.

After all eight admissions, and not before:

1. Run `S2_I3_P0D_diagnostics_v0_1.bat` separately for every one of the eight labels. These unchanged S2-I2 numerical diagnostics are descriptive and NOT P0 admission gates, including historical inconclusive values.
2. Run `S2_I3_P0D_pair_v0_1.bat` individually for `XP`, `SP`, `LP`, `3A`. Both versions must already be admitted; correspondence must PASS, with zero decisive violations. Stop on FAIL/INCONCLUSIVE.
3. Run `S2_I3_P0D_summary_v0_1.bat`; inspect `%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1\P0_summary.json`, eight per-source JSON sets, diagnostics, four pairs and logs. An eventual `READY_FOR_P1=true` is numerical only; it REQUIRES owner and Claude gate review and does NOT authorise filter code or P1.
4. Present actual complete evidence to Claude for independent comparison against accepted source and pair references. Only after owner/Claude evidence acceptance, separately COPY seven admitted index files into `VHSC_samples` with exact digest validation and exact named-path Git staging/commit. The six immutable indexes must never be rewritten. No public media/temporary artefact inclusion.

No P0 work includes S2-I8 hold-out testing or any deblocking filter implementation. The currently unassigned 6A/7A recordings and extra snapshot files are not P0 sources.

## 8. Requested Claude follow-up

Please independently assess this status against the owner CMD logs and the approved candidate/clearances; particularly distinguish the 7 actually verified P0B results from the 8th pre-existing frozen LP baseline, and P0C XP actual REGISTERED from the seven pending admissions. No reimplementation, retuning, or code review requested at this point. If this handback faithfully captures the observed state, acknowledge continuity and continue with XP_blocky using the corrected P0A overlay already in place. Keep the evidence-only/numerical nature of the gate explicit.

This report is intended for private role communication. If considered for Git tracking, review its appropriateness first; it is not itself a ratified replacement for any authoritative project document.
