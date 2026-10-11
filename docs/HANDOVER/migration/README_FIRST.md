# Migration documentation: current read-first index (2026-10-11)

Read this first when continuing the VapourSynth-mpeg2Deblock Visual Studio / build / release migration. This file supersedes the old 2026-10-10 Stage A3 v0.9 checkpoint instructions; the historical candidate and review files remain available as evidence, not current action items.

## Reading order

1. `Migration_Status.md` (living document; current v0.7) - the acceptance ledger, open gates and binding Dave decisions.
2. `ChatGPT_Migration_Chat_Handover_v0_13.md` - migration-chat continuity after published `v0.1.0` development-scaffold pre-release.
3. `Claude_REVIEW_OF_ChatGPT_StageBPlus_Final_Gate_v0_1.md` - Stage B+ local gates A-F; all six indexes PASS.
4. `Claude_REVIEW_OF_ChatGPT_StageBPlus_Step4_CI_Run_v0_1.md` - accepted 256-switch / HostX64 CI proving and K2 closure.
5. The current workflow `.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml` and the reviewed CSV `.github/workflows/expected_stage_bplus_switches.csv` - actual automated build/release contract.
6. Historical `ChatGPT_Migration_Chat_Handover_v0_12.md`, Stage A, Stage C and earlier Design Record/Plan versions only if needed to trace a decision. They are not substitutes for the current status.

## Current checkpoint

- Stage A A3 v0.10: ACCEPTED; its six-index result was WAIVED, **never PASS**.
- Step 0, Step 1 and Stage B+ / K2: ACCEPTED and CLOSED. Stage B+ six-index did PASS locally.
- Step 3: tested single-job manual + published-Release workflow; one verified user ZIP containing EXE, DLL, LICENSE and NOTICE.md; public `v0.1.0` pre-release published. Final Claude/Dave closeout decision still pending.
- Step 4: final common developer handback, final migration reviews and closure are next. Technical development stays paused under O6 until all migration work is closed and Dave separately authorises resumption.

Git hygiene: `git add -A` stages all new evidence, logs and ZIPs as well as documents. Review `git diff --cached --name-status`, `--stat`, and `--check` before committing; do not assume untracked items are irrelevant or that they all belong in the repository.
