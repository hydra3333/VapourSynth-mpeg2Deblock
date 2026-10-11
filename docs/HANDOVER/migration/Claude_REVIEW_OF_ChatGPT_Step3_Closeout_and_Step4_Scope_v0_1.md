# Claude review - step 3 close-out and step 4 scope

File: Claude_REVIEW_OF_ChatGPT_Step3_Closeout_and_Step4_Scope_v0_1.md
Version / date: v0.1 / 2026-10-11
Author: Claude (migration chat, independent reviewer)
Reviewed:
- `Claude_Step3_Closeout_Review_Request_v0_1.md`;
- `Step3_v010_DOCUMENTATION_REPOSITORY_FILES_v0_1.zip` (README.md, README_FIRST.md, Migration_Status v0.7, ChatGPT handover v0.13);
- my own read-only checks of the public repo and the public v0.1.0 release asset (section 2).

## 1. Verdict

**ACCEPT step 3 closure**, for Dave to ratify, with one decision for Dave (C1, PDB retention) and two minor document points (C2, C3). The step 4 scope is sufficient once the additions in section 4 are included.

## 2. My independent evidence (not relying on the TEST3 summary)

| Check | Result |
|---|---|
| Refs, via `git ls-remote` | `main` HEAD = `refs/tags/v0.1.0` = `f6ea38069a0e6fba10c08a80cd301d89a9fe8635`. The release tag is on `main`. |
| Deployed workflow | `mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml` at `main`, diffed against my reviewed v0.3. The only differences are the agreed v0.4 items: the 4-name list with a name-to-source map (binaries from `Release_Binaries`, LICENSE and NOTICE.md from the workspace root), Z1 `Add-Type`, count 4, the source-mapped hash check, and the new display name and messages. Nothing else changed. |
| Project files and CSV at `main` | Both `.vcxproj` files equal the ratified B+ v0.2. `expected_stage_bplus_switches.csv` is unchanged (256 rows). |
| Public asset | I downloaded `mpeg2Deblock-v0.1.0-win-x64.zip` (195,468 bytes, SHA-256 `7810486f08503ecf73d4b7837447a3c401acf3d48498b1e8d36af3414f5c9fd0`). It has exactly 4 root members: `Mpeg2BlockInspector.exe` (237,056), `mpeg2Deblock.dll` (105,472), `LICENSE`, `NOTICE.md`. LICENSE and NOTICE.md have the same content as the repo files (they differ only by CRLF, because the Windows runner checks out with CRLF). |
| Released EXE (pefile) | x64 PE32+, LAA, HEVA, DynamicBase, NX, CFG, TSAWARE, console, CET debug entry present. Imports KERNEL32.dll only. GuardFlags 0x10417500, EH continuation count 15, CF count 55. PDB name is the bare `Mpeg2BlockInspector.pdb`. |
| Released DLL (pefile) | x64 PE32+ DLL, LAA, HEVA, DynamicBase, NX, CFG, GUI, CET debug entry present. Imports KERNEL32.dll only. Single export `VapourSynthPluginInit2`. GuardFlags 0x10417500, EH count 11, CF count 46. File version 0.1.0.0. PDB name is the bare `mpeg2Deblock.pdb`. |
| Did the v0.1.0 run pass every check? | Yes, by construction. The attach step runs only on `success()` after every strict check, ancestry included. The asset exists, so the run passed. I do not need the v0.1.0 job log for this gate. Actions logs need sign-in, so I could not read it. |

The released binaries' security values (guard flags, EH and CF counts, imports, export, version) are identical to those in the accepted Stage B+ local and CI evidence.

## 3. Points

**C1 (decision for Dave): PDB retention.**
- README line 27 says the PDBs are "retained separately in GitHub Actions artifacts". Actions artifacts **expire**: the default is 90 days, and a public repo cannot keep them longer. Those numbers are from memory and unverified; check Settings > Actions > General.
- After that, nobody can symbolise a crash dump from a released binary.
- Options:
  - (a) Attach a second release asset `mpeg2Deblock-<tag>-win-x64-symbols.zip` holding the 2 PDBs, verified the same way. The user-facing binary ZIP stays the single download for normal users.
  - (b) Dave downloads each release run's artifact and keeps it locally or offsite.
  - (c) Accept the loss.
- I recommend (a), or at least (b). Correct the README wording to match whichever is chosen.

**C2 (minor): line endings.** `README.md` and `README_FIRST.md` in this package are LF-only. Migration_Status and the handover are CRLF. Git stores all of these as LF (`git ls-files --eol` shows `i/lf`), so the repository is not affected. But Dave's rule is CRLF for documents, and P2 says ChatGPT checks this by script. Convert the two before Dave copies them in.

**C3 (note only).** The release ZIP's LICENSE and NOTICE.md are CRLF, from the Windows checkout, while the repo stores LF. The content is identical, and that suits Windows users. No action.

## 4. Step 4 scope: sufficient, with these additions

1. **Release checklist** for the development chats:
   - bump `plugin_version.h` first;
   - commit to `main`;
   - publish a Release whose tag matches (e.g. `v0.1.1` for 0.1.1.0);
   - check the attached ZIP and its hash against the run's manifest.
   Nothing yet enforces tag = header version. Dave may want a fail-closed check of this in the workflow later (a workflow change, his decision).
2. **The C1 outcome**, and how to get symbols for a given release.
3. **How to handle a CI switch-check failure** after a Visual Studio or MSVC update:
   - read the printed missing and extra tokens;
   - decide;
   - update the CSV and the G7 comment block in one commit;
   - a compiler or toolset change also triggers the local six-index run.
   Also how a future v146 toolset is picked up (`DefaultPlatformToolset`, minimum-v145 guard).
4. **D-SDK (c) in practice:** where the SDK is recorded (`tool_versions.txt`), and that with `/MT` an SDK change alters the UCRT code in both binaries without triggering reruns.
5. **Branch rules as now decided:** manual runs on any branch, never attaching; releases only from `main` history.
6. **The `/MT` runtime-ownership rule** and the B6 inherited switches, with reasons.
7. **The historical files** (`expected_a3_v0_10_switches.csv`, old candidates and reviews) and the fact that they are not current instructions.

## 5. Known corrections for the final Design Record and Hard-Earned Knowledge

These come from decisions and findings in this chat; I have not compared the latest DR text line by line.

- G6: there was never a test branch. CI proving ran on `main`. CI manual runs are now any-branch (Dave, step 3).
- Stage E (wheel/PyPI) moved to the development chats (G1); naming is O1.
- O4: Large Address Aware is kept on the DLL (Dave overrode my recommendation). O5: no runtime CPU check ever. O6, O7 as ratified.
- D-SDK (c), plus the finding that under `/MT` the static UCRT comes from the Windows SDK (step 1: 10.0.26100.0 on CI against 10.0.28000.0 locally).
- `/guard:ehcont` on both binaries (O2), set through the native properties; `LinkGuardEHContMetadata` is a PropertyGroup property.
- Hard-Earned Knowledge:
  - N1-N4;
  - the W1 `/LTCGOUT` coupling inside the Link task;
  - `$(ShortProjectName)` intermediate folders (`Mpeg2Blo.F4B1A357`);
  - LINK tlog line 1 carries only the first input;
  - `release` events run the workflow file from the tagged commit.

## 6. Next

1. Dave ratifies step 3 and decides C1.
2. ChatGPT fixes C2 (and the README wording for C1).
3. Step 4: the final common developer handback, then the final migration close-out.
