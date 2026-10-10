# Stage B+ Step 4 proving workflow candidate v0.2 — Claude diff review

**NOT YET RATIFIED. Do not install or dispatch.** This revises v0.1 ONLY for
Claude review findings F1–F4. Baseline repository: `main` commit `40fb6dd`.

## Production change scope (unchanged from v0.1)

Install only the TWO files AFTER Claude's v0.2 diff review and Dave's ratification:

- `.github/workflows/prove-project-build-windows-x64.yml` (replace)
- `.github/workflows/expected_stage_bplus_switches.csv` (new, **byte-identical** to v0.1)

Historical A3 CSV unchanged. No source, VS project or test script edits.
All six local indexes remain PASS; no index regressions run in CI.

## Changes requested by Claude

- **F1 REQUIRED — one version owner (O3).** At binary-validation time the
  workflow parses the four `MPEG2D_VERSION_{MAJOR,MINOR,PATCH,BUILD}` numeric
  `#define` values from `src/mpeg2Deblock/plugin_version.h`. It fails for a
  missing, repeated or non-numeric macro (also rejects uint32 overflow).
  The derived `M.m.p.b` is compared to DLL FileVersion and ProductVersion;
  the canonical header value plus both binary values are written to evidence.
  `OriginalFilename` check remains. No hard-coded `0.1.0.0` in workflow.
- **F2 REQUIRED — D-SDK(c).** Derives SDK versions from both
  `Windows Kits\10\lib\<version>\ucrt\x64` and
  `Windows Kits\10\Include\<version>...` occurrences in the ACTUAL
  Release detailed MSBuild log. Requires exactly one distinct 4-part SDK
  version, writes `Windows SDK (used by build): <version>` to
  `tool_versions.txt`. Uses `bin\<used version>\x64\mt.exe` where present;
  otherwise uses the newest installed mt.exe with the explicit fallback
  reason recorded. Discovery is per build; no SDK version comparison failure.
- **F3 RECOMMENDED — N3.** EHCONT table flag and field remain mandatory;
  `Guard EH continuation count` is present and recorded, with **zero allowed**.
  CF table count and security-cookie address remain nonzero.
- **F4 RECOMMENDED — production header.** Replaced v0.1 candidate-only header
  with a correct manual-on-main workflow description.

## What is intentionally NOT changed

- Ten strict CL/LINK/RC tlogs and 256 switches, including four inherited B6 rows.
- All eight HostX64 project/tool/config invocation positive checks.
- Exact native Windows CommandLineToArgvW tokenisation, no flag injection.
- PE validation except the F3 count rule; DLL export/manifest/other checks intact.
- Manual `workflow_dispatch` only. Step 3 improvements (S4/S6, G5 CSV
  deduplication) are deferred exactly as Claude requested.

## Static and evidence validation

- Original and v0.2 embedded Python checker **byte-for-byte equivalent** after
  line-ending normalisation; compilation PASS.
- Workflow YAML v1.2 load PASS; manual dispatch only.
- Expected CSV identical to v0.1: 256 tokens, ten expected groups.
- Actual Step 1 Release detailed CI log: extracted **one SDK, 10.0.26100.0**,
  from both UCRT-library and Include source patterns.
- Ratified B+ header `plugin_version.h`: macro extraction yields 0.1.0.0;
  the value is a test fixture, not a duplicate workflow version literal.
- SHA-256 package inventory covers every non-manifest file; ZIP integrity checked.

## Claude's requested review

Please perform **a focused diff review of `STEP4_v0_1_TO_v0_2.diff`** and
independently check F1–F4. No design revision beyond those findings is proposed.

Preimage workflow SHA-256: `8388a445d12e30e0b564f48ff20720e882d75a161eb14f9e75f4c3b15bd2646f`.

**No GitHub workflow was dispatched; repository remains at the accepted
Stage B+ snapshot pending review.**
