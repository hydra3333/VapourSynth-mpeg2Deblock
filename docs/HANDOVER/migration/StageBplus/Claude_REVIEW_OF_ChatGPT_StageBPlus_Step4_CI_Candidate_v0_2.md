# Claude review - Stage B+ step 4 CI proving candidate v0.2 (diff check)

File: Claude_REVIEW_OF_ChatGPT_StageBPlus_Step4_CI_Candidate_v0_2.md
Version / date: v0.1 / 2026-10-11
Author: Claude (migration chat, independent reviewer)
Reviewed: StageBPlus_Step4_CI_CANDIDATE_FOR_CLAUDE_v0_2.zip (7 files plus PACKAGE_SHA256.txt), diffed against v0.1.

## 1. Verdict

READY FOR DAVE TO RATIFY, APPLY AND RUN. F1 to F4 are fixed, and nothing else changed.

## 2. Checks

- SHA-256: 7/7 OK. The workflow is ASCII with CRLF line endings. The expected CSV is byte-identical to v0.1, which I had already verified against the measured 256 rows.
- The diff is confined to:
  - the header (lines 1-3);
  - the SDK, mt.exe and version block (new lines 321-367);
  - the EH count rule;
  - the VERSIONINFO comparison.
  The embedded checker and every other step are unchanged.
- **F1, version.** The four numbers are parsed from `src/mpeg2Deblock/plugin_version.h`, with exactly one numeric `#define` each, and checked against uint32. The result is compared with the DLL's FileVersion and ProductVersion, and recorded. I tested the regex on the ratified header: it gives `0.1.0.0`. There is no version literal left in the workflow. FIXED.
- **F2, SDK.** The SDK is taken from the actual Release log (the UCRT lib and Include paths), and exactly one version is required. I tested the regex on two logs:
  - the Step 1 CI log gives `10.0.26100.0`;
  - Dave's local A3 log gives `10.0.28000.0`.
  So it reports the SDK each build actually used, not the newest installed. `mt.exe` comes from the same SDK, with the reason recorded if it falls back. FIXED.
- **F3, EH count.** "EH Continuation table present" is still required. The count field must exist and is recorded, and zero is allowed. The cookie and CF count must still be nonzero. FIXED.
- **F4, header.** It is an accurate production header. FIXED.

## 3. Note (no change needed)

The F1 loop assigns to `$matches`, which is PowerShell's automatic `$Matches` variable. It is harmless here, because no `-match` runs between the assignment and its use. Rename it in step 3 for clarity.

## 4. Next

1. Dave copies the two files into `.github/workflows/`.
2. Commit as a Snapshot on `main`, then push.
3. Dave runs "Prove project-owned MSBuild settings (manual)" from the Actions tab.
4. Send me the artifact `stage-bplus-project-owned-msbuild-proof` and the job log.
5. My review of the run closes Stage B+ and K2.
