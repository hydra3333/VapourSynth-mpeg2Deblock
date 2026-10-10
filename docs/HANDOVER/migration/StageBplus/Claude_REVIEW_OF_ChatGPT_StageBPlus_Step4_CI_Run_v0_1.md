# Claude review - Stage B+ step 4 CI proving run

File: Claude_REVIEW_OF_ChatGPT_StageBPlus_Step4_CI_Run_v0_1.md
Version / date: v0.1 / 2026-10-11
Author: Claude (migration chat, independent reviewer)
Reviewed: StageBPlus_Step4_CI_Run_CLAUDE_REVIEW_v0_1.zip, containing:
- the original artifact zip (29 files);
- the original job log;
- ChatGPT's gate assessment.
Run 38092449456, commit `3ccfa182`.

## 1. Verdict

ACCEPT. Stage B+ is CLOSED and K2 is CLOSED, pending Dave's ratification.

## 2. Independent checks

| Check | Result |
|---|---|
| Package and artifact | SHA-256 3/3 OK. The artifact zip hashes to `1e7d47d2...da41`, the same as ChatGPT states. |
| What ran is what I reviewed | I fetched read-only from GitHub at `3ccfa182`. The workflow equals my reviewed v0.2 and the expected CSV equals my reviewed CSV, both compared with line endings normalised. The A3 CSV is unchanged. The job log shows checkout of `3ccfa182` ("Snapshot Stage B+ Step 4 CI proving workflow") on `main`. |
| 64-bit MSBuild | `MSBUILD_IS64=True` |
| Switches | My own comparison of `actual_stage_bplus_switches.csv` with the expected CSV, by (project, configuration, tool, ordinal), with LINK ignoring case: **256/256 identical**. The job log prints PASS for all 10 keys. |
| K2, HostX64 | My own scan of both detailed logs finds exactly 4 real invocations per configuration: inspector CL and LINK, DLL CL and LINK. All are under `...\MSVC\14.51.36231\bin\HostX64\x64\`, with **zero HostX86**. All 8 groups are proven. |
| Warnings | Debug and Release each have 17 warnings and 0 errors. The (file, line, code) set is identical to Dave's local A3 and B+ builds, and the DLL has none. |
| SDK (D-SDK (c)) | Recorded: `Windows SDK (used by build): 10.0.26100.0`, and that is the only SDK in both logs. `mt.exe` came from the same SDK. |
| Release binaries | The workflow reports PASS for both. EH continuation counts are 15 (inspector) and 11 (DLL), the same as Dave's local build. VERSIONINFO 0.1.0.0 equals the header value, and OriginalFilename is correct. |

## 3. What this closes

- **Stage B+:**
  - local gates A-F, accepted 2026-10-11 (the six indexes are a real PASS);
  - and this CI proof, for both projects, from the project files only.
- **K2:** HostX64 is proven for both projects in both configurations.
- B6 inherited values are locked in the expected CSV and verified.

## 4. Unchanged and recorded

- A3 v0.10 six-index stays **WAIVED**. Stage B+ six-index is **PASS**, run locally (O7: never in CI).
- CI SDK 10.0.26100.0 against local 10.0.28000.0 falls under D-SDK (c). It is recorded, and no claim of identical binaries is made.
- Still for step 3:
  - S4: upload the Release EXE and PDB;
  - S6: actions on Node 24;
  - the G7 reference block;
  - the counts and B6 tokens taken from the CSV rather than hard-coded;
  - the `$matches` variable rename;
  - the release trigger.

## 5. Next

1. ChatGPT updates `Migration_Status.md` (P1): Stage B+ CLOSED, K2 CLOSED, and the Step 0 wording fix noted earlier ("Dave ran the validator").
2. Then step 3, the final release workflow. It should start from this proven workflow, not from scratch.
