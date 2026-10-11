# ChatGPT Handover to a Future Migration Chat
## VapourSynth-mpeg2Deblock Repository / Visual Studio / Release Migration

**Filename:** `ChatGPT_Migration_Chat_Handover_v0_13.md`
**Version:** 0.13
**Date:** 2026-10-11
**From:** migration ChatGPT (coder/drafter)
**To:** successor migration ChatGPT, and Claude for independent context
**Status:** CURRENT migration-only continuity, following public `v0.1.0` pre-release; NOT a deblocking algorithm specification or a final developer handback.
**Current controlling status:** `docs/HANDOVER/migration/Migration_Status.md` v0.7 (living document).
**Historical preimage:** `ChatGPT_Migration_Chat_Handover_v0_12.md`, retained for detailed Stage A background. Its old outstanding-action checklists and unverified implementation proposals are superseded by the current status, not binding instructions.

## 1. Current checkpoint -- read this first

- **Stage A:** Accepted. Its A3 v0.10 six-index regression was specifically **WAIVED, NOT PASS**; never infer another waiver. Earlier v0.9 six-index results are separate.
- **Step 0 and Step 1:** CLOSED/PASS/ACCEPTED. Dave ran the live Step 0 structure validator, 140 pins PASS. Step 1 CI commit `bf241259...`, run `38034308907` accepted.
- **Stage B+ / K2:** Both **CLOSED, ACCEPTED AND RATIFIED by Dave on 2026-10-11**. Both projects compile (VS2026 x64); plugin API4 `Identity` loads under portable VapourSynth R81; local gates A-F PASS; six local indexes PASS. Stage B+ workflow commit `3ccfa182`, Actions run `38092449456`, all 256 strict switch tokens and eight positive HostX64 groups PASS; Claude independently accepted the run.
- **Step 3:** Release workflow IMPLEMENTED and thoroughly tested. Final four-file distribution workflow tested at commit `51dc6c5` in manual run `38100598879` and published TEST3 run `38100805228`, passing switches, HostX64, binary security, ZIP membership and hashes. Public [`v0.1.0` pre-release](https://github.com/hydra3333/VapourSynth-mpeg2Deblock/releases/tag/v0.1.0) exists at tag commit `f6ea380`, and Dave says it worked. **Do not yet claim formal Step 3 CLOSED:** final Claude acceptance and Dave ratification have not been recorded. Nor has a fresh independent byte audit of the versioned v0.1.0 asset been furnished in this chat.
- **Step 4:** Final common developer handback and migration closure remain NEXT; do not start technical implementation or experiments. Dave must separately authorise resumption after final migration closure (O6).

## 2. Current repository, workflow, version and publication

- Public repository: `https://github.com/hydra3333/VapourSynth-mpeg2Deblock`; development branch `main`. User works locally at `E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock`.
- **Current workflow filename:** `.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml` (do not use the old path in current instructions).
- **Actions display name:** `mpeg2Deblock - Windows x64 Build, Verify, manual or Release`.
- **Single-job deliberate decision:** `contents: write` (Dave rejected R1 separate jobs). Published Release check uses git ancestry to `main`; manual Actions run accepts **any branch** but never uploads Release assets. Both modes upload Actions evidence; only published Release attaches the verified user distribution. Both ordinary and pre-release publication are eligible.
- **Custom Release asset:** `mpeg2Deblock-<tag>-win-x64.zip` with exactly FOUR root entries: `Mpeg2BlockInspector.exe`, `mpeg2Deblock.dll`, `LICENSE`, `NOTICE.md`. EXE and DLL come from `Release_Binaries`; text files come from the checked-out repository root. Validate all four nonempty, exact archive membership, and source-to-extracted SHA-256. No PDB in distribution; two PDBs and both binaries retained in Actions proof artifact. GitHub automatically adds two separate source archives.
- **Version:** `v0.1.0` tag agrees with canonical DLL `0.1.0.0`. Release is explicitly a *pre-release*, development scaffold. The plugin is an `Identity` placeholder **NOT a deblocking filter**. Do not describe as a working deblocker.
- **Toolchain baseline:** VS2026 v145+, host x64 and `/arch:AVX2`; default/current toolset chosen, recorded not pinned; SDK unpinned and recorded each run (D-SDK c). Plugin `/fp:precise`, no automatic contraction. Release `/MT`, Debug `/MDd`; `/guard:cf`, `/guard:ehcont`, `/LARGEADDRESSAWARE`; CFG/CET and other PE checks in CI.

## 3. Preserved evidence and scope limits

- Claude Stage B+ local acceptance: `Claude_REVIEW_OF_ChatGPT_StageBPlus_Final_Gate_v0_1.md`.
- Claude Stage B+ CI closeout: `Claude_REVIEW_OF_ChatGPT_StageBPlus_Step4_CI_Run_v0_1.md`.
- Claude Step 3 candidate reviews v0.1 and v0.2; Dave approved one-job policy, made main-ancestry test mandatory for published Releases, and later requested the single user-facing four-file ZIP. Packaging v0.4 was directly accepted for test without another Claude candidate review by Dave.
- Final packaging acceptance: TEST3 manual `38100598879`, published Release `38100805228`, commit `51dc6c5`. Published TEST3 ZIP SHA-256 `c8733d0889c1c646ea6f1d3a2de2408272f0169655dc5e1b076610b9a6c8c3cb`. **This digest belongs to TEST3 alone, not the permanent v0.1.0 ZIP**.
- Manual-from-any-branch support was source-reviewed but a non-main manual run was not tested. A divergent, non-main-only Release ancestry rejection was tested synthetically, not using a public divergent release. Neither unexecuted scenario may be reported as an executed CI test.
- The Versioned v0.1.0 public Release page and its source commit are visible, and Dave confirmed operation. Do not invent the production job ID, artifact hash, or proof that its binary output matches TEST3. Request records only if final gate reviewer needs them.
- Under **O7**, all six MPEG-2 functional index regressions run on Dave's Windows machine only when triggered by project/toolchain changes. CI deliberately does not run functional six-index tests. CI and local EXE hashes can differ despite source identity; SDK 10.0.26100.0 in CI versus local 10.0.28000.0 was recorded and accepted under D-SDK (c).

## 4. Exact decision / responsibility boundary

1. Dave is project decision authority; ChatGPT drafts and validates; Claude independently reviews major candidate/gate evidence when required; Dave ratifies. Dave expressly waived an additional Claude review for the narrow v0.4 ZIP packaging edits, **not** a general waiver of final closeout review.
2. P1 knowledge policy: `Migration_Status.md` is the living checkpoint. Stage A plan is historical. Update Design Record and Hard-Earned Knowledge only when appropriate at migration close, and author the **one final common** `MPEG2_Deblocking_Developer_Handback` during Step 4 from provisional v0.16. Do not confuse this migration-chat handover with the eventual common handback for development.
3. O1-O7 are closed/ratified (see current `Migration_Status.md` for full rationales). Wheel/PyPI work belongs to future development Stages 7-9, not migration. No experimental or algorithm coding before O6 clearance.
4. Git hygiene: Dave may take interim snapshots/commits on `main`. Before `git add -A`, inspect all modified and untracked paths; a prior working tree contained candidate ZIPs, logs, and historical evidence under `docs/HANDOVER/migration/StageBplus/`. Do not silently delete evidence, nor assume all of it is desired in Git history. Do not modify repository files that were not actually verified against the user's local current baseline.

## 5. Next actions for the successor chat

- Dave applies/reconciles the current migration status, this v0.13 handover, the migration read-first index and public README scaffold notice. Run `git status --short`, `git diff --check`, stage, inspect staged file inventory and commit/push. Record actual SHA; previous baseline commit is the `v0.1.0` tag at `f6ea380`, **not** the upcoming documentation commit.
- Send a brief Step 3 closure review request to Claude with the tested TEST3 evidence, permanent v0.1.0 pre-release URL, latest status, current workflow path, and the new docs commit ID. Ask for Step 3 ACCEPT / corrections; keep TEST3 proof separate from uninspected permanent build bytes. Dave ratifies closure after the review.
- Then Step 4: produce final common developer handback with real working CLI/GUI examples, accepted build and release invariants, controls, regressions, troubleshooting, licence/wheel deferred knowledge. Claude reviews; Dave ratifies and commits/pushes. Update the living status to formally CLOSED only when supported.
- **Final stop line:** do not resume MPEG-2 filter logic design/implementation or Python Stage 2 experiments before final migration closure AND a separate express authorisation from Dave.
