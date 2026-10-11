# Request for Claude - Step 3 final closeout review and Step 4 handback scope

**Date:** 2026-10-11
**From:** ChatGPT migration chat, for Dave to send after his documentation commit/push
**Repository:** https://github.com/hydra3333/VapourSynth-mpeg2Deblock
**Documentation commit:** `<INSERT DAVE'S NEW DOC COMMIT HASH AFTER PUSH>`

## Request

Please independently assess whether Migration **Step 3** can be accepted/closed and whether the following **Step 4** handback scope is complete. Dave remains the ratification authority. This message is a bounded gate/plan review, not an instruction to perform deblocking implementation.

## Observed and ratified context

1. Stage A A3 v0.10 six-index was **WAIVED, not PASS**. Stage B+ later ran all six indexes locally and PASSED. Stage B+ and K2 were independently accepted by you and formally ratified by Dave (2026-10-11). Stage B+ CI run `38092449456`, commit `3ccfa182` verified all 256 switch tokens and all eight positive HostX64 invocation groups.
2. Dave chose a single workflow job (`contents: write`), manual runs from **any branch** with no GitHub Release assets, and `release.published` automated publication only when the tagged revision belongs to `main` history. The Git ancestry check is a mandatory condition. Build settings remain project-owned, not injected by CI.
3. The current workflow was renamed at Dave's request to `.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml`, display name `mpeg2Deblock - Windows x64 Build, Verify, manual or Release`.
4. Dave requires a **single user-facing Windows x64 ZIP** containing four files at archive root: `Mpeg2BlockInspector.exe`, `mpeg2Deblock.dll`, `LICENSE`, `NOTICE.md`. The binaries are taken from `Release_Binaries`; the text files are taken from the checkout root. The workflow rejects missing/empty members and verifies root membership and decompressed SHA-256 values. Two PDBs remain only in the Actions proof artifact. This v0.4 packaging edit was explicitly exempted by Dave from another candidate review; it received functional test coverage.
5. The final test evidence was inspected by ChatGPT: TEST3 manual Actions run `38100598879`, published TEST3 run `38100805228`, both commit `51dc6c5`. Debug/Release builds, 256/256 switches, 8/8 HostX64, PE/security and four-file ZIP checks PASSED. The downloaded TEST3 ZIP SHA-256 equalled the value in its Release build log: `c8733d0889c1c646ea6f1d3a2de2408272f0169655dc5e1b076610b9a6c8c3cb`.
6. Dave subsequently published public pre-release [`v0.1.0`](https://github.com/hydra3333/VapourSynth-mpeg2Deblock/releases/tag/v0.1.0), pointing to GitHub-displayed commit `f6ea380`, and reports that publication worked. The release declares the plugin to be an `Identity` scaffold, NOT a deblocking implementation. **The versioned production run's own job log and downloaded ZIP were not uploaded to ChatGPT for a separate byte-level inspection.** Please treat the TEST3 verification separately; request final Release evidence only if it is necessary for your gate decision.

## Proposed documentation updates

- Update the one living `docs/HANDOVER/migration/Migration_Status.md` to v0.7, accurately recording Stage 3 tested/published but not yet formally closed.
- Add `ChatGPT_Migration_Chat_Handover_v0_13.md` as the current, concise migration-continuity orientation, retaining v0.12 for historical source-tracing.
- Replace stale 2026-10-10 A3 v0.9 migration `README_FIRST.md` with a current read-first index.
- Correct root `README.md` to state the API4 plugin `Identity` scaffold and published v0.1.0 four-file pre-release; do not rewrite the historical research sketch section.
- Intentionally do **not** revise the common `MPEG2_Deblocking_Developer_Handback_v0_16.md` or the Design Record yet: per P1, the final one-piece Developer Handback is the next Step 4 deliverable. No code or workflow flags changed in this documentation set.

## Questions to resolve

1. On the tested TEST3 evidence, published permanent pre-release and any supplied final run evidence, do you **ACCEPT Step 3 closure** or identify a specific outstanding gap? Dave will then ratify or direct corrections.
2. Is the Step 4 scope sufficient: final VS2026 GUI and plain-CMD MSBuild workflows, actual HostX64 and SDK/version audit, switch/reference ownership, CI triggers and Release distribution, security/import/export checks, local functional regression rules, troubleshooting, O1-O7 and D-SDK(c) decisions, deferred wheel/PyPI, and the O6 technical stop line?
3. Are there any known, material historical-knowledge corrections required in the final Design Record / Hard-Earned Knowledge at migration close? Avoid broad reopening of frozen historical stages without identified cause.

Please return a concise ACCEPT / corrections verdict, preserving Dave's decision authority and the difference between tested CI, production publication, and untested scenarios. No developer-algorithm work is authorised.
