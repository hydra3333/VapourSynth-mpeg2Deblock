# Claude review - Stage B+ step 4 CI proving candidate v0.1

File: Claude_REVIEW_OF_ChatGPT_StageBPlus_Step4_CI_Candidate_v0_1.md
Version / date: v0.1 / 2026-10-11
Author: Claude (migration chat, independent reviewer)
Reviewed: StageBPlus_Step4_CI_CANDIDATE_FOR_CLAUDE_v0_1.zip (6 files plus PACKAGE_SHA256.txt).
Compared against:
- the live GitHub `main`, fetched read-only today: workflow, A3 CSV, both `.vcxproj`;
- the Stage B+ gate evidence;
- the Step 1 run logs.

## 1. Verdict

NEARLY READY. The design is right, and the checks I could run against real logs and dumps all behave correctly. Two small required fixes (F1, F2) and two recommended ones (F3, F4) should go into a v0.2. I will check v0.2 as a diff.

## 2. Verified

- SHA-256: 6/6 OK. The workflow, CSV and checker are ASCII with CRLF line endings.
- The live `main` workflow, normalised to CRLF, hashes to `8388a445...646f`, the stated preimage. The live `main` `.vcxproj` files are exactly the ratified B+ v0.2, and the live A3 CSV is unchanged.
- The new CSV: all 256 rows, keys and ordinals are identical to the measured `C_Measured_Switches.csv`. The only addition is the `disposition` column, and exactly the 4 B6 rows carry it.
- Checks run against real evidence:
  - **HostX64 classifier (Q2):** run against the Step 1 CI detailed logs, the regex finds exactly 1 CL and 1 LINK invocation per configuration, both classified INSPECTOR, with no ambiguous lines and no unmatched HostX64 tool lines. The DLL patterns (`\src\mpeg2deblock\plugin.cpp`, `/out:...mpeg2deblock.dll`) match the DLL command lines in Dave's tlogs. This is positive proof for each of the 8 groups, with no false positives seen.
  - **Tlog discovery (Q1):** `Mpeg2Blo.F4B1A357` is MSBuild's `$(ShortProjectName)`, set in `Microsoft.Cpp.MSVC.Toolset.Common.props` and visible in the Step 1 CI log. It is derived from the project name and GUID, so it is the same locally and on the runner. The DLL folder is `mpeg2Deblock`. The exactly-ten-traces check is robust.
  - **PE, loadconfig and export checks (Q3):** every pattern passes on Dave's B+ Release dumps for both binaries: x64, PE32+, LAA, HEVA, Dynamic base, NX, CFG and CET; TSAWARE and CUI for the inspector, GUI for the DLL; RSDS with a bare file name; CF instrumented, FID, EH Continuation table present; cookie, CF count and EH count; the single unmangled export. None is too strict for valid output, apart from F3.
- LINK parsing reads the first tlog line only. That works because MSBuild writes the first input (`.obj` for the inspector, `.RES` for the DLL) on line 1, as Dave's tlogs show. Note only.
- **G5/G7 (Q4):** retained. A missing or extra token is fatal, LINK comparisons ignore case, no flags are injected, and the B6 rows are annotated, not omitted.
- **O1-O7 and K1/K2 (Q5):** consistent. Manual dispatch on `main` only, no six-index run in CI (O7), and K2 is closed by this run.

## 3. Required (v0.2)

**F1. Do not hard-code `0.1.0.0` in the workflow (lines 402-404).** That is a second version literal, which breaks O3's single owner. Read `MPEG2D_VERSION_MAJOR`, `MINOR`, `PATCH` and `BUILD` from `src/mpeg2Deblock/plugin_version.h`. Fail if any of the four is missing or not a number. Compare the DLL's FileVersion and ProductVersion with that `M.m.p.b`, and record both in the evidence.

**F2. Record the Windows SDK the build actually used (D-SDK (c): "recorded on every build").** Today the workflow records only the newest installed `mt.exe` folder, which need not be the build's SDK.
- Extract the version from the Release detailed log, e.g. the distinct `Windows Kits\10\lib\<ver>\ucrt\x64` (or `\Include\<ver>`) values. In the Step 1 log these were all `10.0.26100.0`.
- Require exactly one distinct version.
- Write `Windows SDK (used by build): <ver>` to `tool_versions.txt`.
- Prefer `mt.exe` from `Windows Kits\10\bin\<that ver>\x64`, falling back to the newest only if it is missing, and record which was used.

## 4. Recommended

**F3. The EH continuation count must not be required to be nonzero (lines 360-364).** N3, already agreed: "the count may legitimately be 0". Require "EH Continuation table present" (already checked at line 366) and record the count. Today the counts are 0xF and 0xB, because the static CRT supplies targets, so this is not failing now, but it is the wrong rule. The error text "missing/nonzero" is also confusing.

**F4. Header lines 1-3.** "CANDIDATE v0.1 - CLAUDE REVIEW ONLY" would be committed to `main`. Change it to an accurate header, e.g. "Stage B+ proving workflow, reviewed 2026-10-11, manual only". This is the same point as S5.

## 5. Noted for step 3 (not now)

- The workflow repeats data that lives in the CSV: `expected_counts` (lines 138-144) and the two B6 tokens (lines 156-157). Under G5, a reviewed switch change should be "update the CSV in one commit". In step 3, keep only the fixed 10-key inventory and an allowed list of `disposition` values in the workflow, and take counts from the CSV.
- S4 (upload the Release EXE and PDB), S6 (Node 20 actions) and the G7 reference block remain step 3 items.
- Debug binaries are not dumped; that is acceptable, as at the gate.

## 6. After v0.2

1. I check v0.2 as a diff.
2. Dave applies the two files, commits and pushes.
3. Dave runs the workflow with the manual button.
4. I review the run artifact. That closes Stage B+ and K2.
