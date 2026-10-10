# Stage B+ Step 4 — CI proving run gate assessment v0.1

Date: 2026-10-11 (Adelaide).  Prepared by ChatGPT for Claude's independent review.

## 1. Disposition

**ChatGPT assessment: PASS; ready for Claude's independent Step 4 final review.** This is a technical evidence assessment, **not** Claude's acceptance and not the final migration closure. No CI test rerun, source change or config change is proposed. K2 HostX64 positive-evidence requirement is met by the actual project-specific invocations; Claude makes the final disposition.

- Repository: `hydra3333/VapourSynth-mpeg2Deblock`, branch `main`.
- CI run: [38092449456](https://github.com/hydra3333/VapourSynth-mpeg2Deblock/actions/runs/38092449456).
- CI checkout: `3ccfa182c295bcade7ddacf653d6db218c3f2172` (Step 4 v0.2 approved workflow snapshot).
- Original artifact name: `stage-bplus-project-owned-msbuild-proof`, ID `11684263081`.
- Original artifact ZIP: 29 entries, ZIP CRC check PASS, SHA-256 `1e7d47d2207e08034b686b884bae01df2050c727adec6adec2251d778519da41` (matches upload digest printed in Actions job log).
- Original job log includes successful artifact upload, no GitHub `##[error]` lines; `checkout@v4` and `upload-artifact@v4` emit the known Node.js 20 deprecation warning at job cleanup (S6/Step 3; not a failing Stage B+ criterion).

## 2. Build and toolchain

- GitHub runner `windows-2025-vs2026`, Windows Server 2025, runner image `20260925.250.1`.
- VS Enterprise 2026 `18.10.12217.157`, 64-bit MSBuild `18.10.1.42706`, `MSBUILD_IS64=True` independently demonstrated by `msbuild-bitness.txt`.
- `Debug|x64`: inspector EXE and plugin DLL built; `Release|x64`: inspector EXE and plugin DLL built.
- Each configuration has the same inspector 17 unique source warnings (C4013 ×8, C4101 ×1, C4996 ×8). Detailed MSBuild logs echo them twice; these are 17 distinct warning locations/codes per configuration, not 34 separate source warnings. Plugin: no compiler or linker warnings observed. No LNK4291.
- Actual HostX64 tool directory `C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\bin\HostX64\x64`. CL version `19.51.36260.0`, LINK and dumpbin `14.51.36260.0`.
- Windows SDK actually used in the build: **10.0.26100.0**. Each detailed MSBuild log independently shows this unique SDK in Include/lib paths. Manifest tool selected from the same SDK, file version `10.0.26100.8249`.

## 3. Exact switch verification and positive HostX64 evidence

- **256/256 CSV tokens match** the Claude-approved v0.2 `expected_stage_bplus_switches.csv` when keyed by `(project, configuration, tool, ordinal)`. There are exactly 256 unique keys, ten groups, zero missing, extra, or changed tokens. The serialized order of the *groups* differs between reviewed CSV and runtime CSV; comparison is deliberately key/ordinal-based, not row-position-based.
- All ten CL/LINK/RC original command tlogs are in the artifact, plus the normalized actual CSV.
- I independently located exactly **four** real HostX64 CL/LINK invocation lines per configuration in the diagnostic logs. In Debug and Release, one each is attributable to inspector CL, inspector LINK, plugin CL, plugin LINK; **8/8 groups**, none ambiguous. This is not inferred from project XML or the tlog path alone.
- Inherited `_WINDLL` and `/TLBID:1` values remained exactly as ratified in B6, and are checked by the full token comparison.

| Project | Configuration | Tool | Reviewed/actual tokens |
|---|---|---|---|
| DLL | Debug | CL | 42 |
| DLL | Debug | LINK | 23 |
| DLL | Debug | RC | 4 |
| DLL | Release | CL | 41 |
| DLL | Release | LINK | 25 |
| DLL | Release | RC | 4 |
| INSPECTOR | Debug | CL | 34 |
| INSPECTOR | Debug | LINK | 24 |
| INSPECTOR | Release | CL | 33 |
| INSPECTOR | Release | LINK | 26 |

## 4. Release PE, manifest, exports and VERSIONINFO

The artifact includes raw dumpbin headers, imports, dependents, exports, load configuration and extracted manifests for Release binaries. The workflow's `pe_validation_result.txt` reports two PASS results. Independent inspection confirms:

- Both Release binaries: PE32+ x64, Large Address Aware, ASLR High Entropy VA, Dynamic Base, NX, CFG, CET-compatible and nonzero security cookie. Guard Flags include `EH Continuation table present`; count 0xF (15) for inspector and 0xB (11) for DLL.
- Both import **KERNEL32.dll only**, consistent with the static CRT Release policy. Inspector is Console and has `asInvoker` plus SegmentHeap manifest; plugin is Windows GUI with embedded empty assembly manifest (no UAC request).
- DLL has one named unmangled export `VapourSynthPluginInit2` (dumpbin prints a same-name alias) and `OriginalFilename=mpeg2Deblock.dll`.
- DLL VERSIONINFO is `FileVersion=0.1.0.0`, `ProductVersion=0.1.0.0`, equal to the sole canonical version obtained from `src/mpeg2Deblock/plugin_version.h`, and is recorded in the artifact.

## 5. Explicit limits / outstanding work

1. This CI workflow does **not** run the six functional index regressions (O7). Those were already run locally and accepted as Stage B+ Gate F. Do not relabel them as CI PASS.
2. The CI proving artifact contains diagnostics and verification outputs, **not** the compiled EXE/DLL/PDB distribution payloads. Release EXE+PDB artifact handling is already deferred to Step 3 (S4).
3. Step 3 is also the scheduled place to replace Node.js 20-based `actions/checkout@v4` and `actions/upload-artifact@v4` (S6), address the accepted blank-line whitespace and simplify the checker redundancy. These do not block Step 4 results.
4. The Release SDK is `10.0.26100.0` on CI; local was `10.0.28000.0`. This is the previously recognised D-SDK(c) recorded difference, not evidence of byte-identical outputs.
5. Only Claude's review and Dave's final ratification can close Stage B+ / K2. The living `Migration_Status.md` should then record the decision without losing the separate A3 v0.10 six-index WAIVED versus Stage B+ six-index PASS distinction.

## 6. Files provided for Claude

- `ORIGINAL_stage-bplus-project-owned-msbuild-proof.zip` — unmodified original downloaded artifact (29 internal evidence files).
- `ORIGINAL_stage-bplus-project-owned-msbuild-proof.log` — unmodified full GitHub Actions job log.
- This gate review — independently checked against the artifact, v0.2 approved expected CSV and the job log.
- `PACKAGE_SHA256.txt` — SHA-256 inventory for the three files above.

**Review requested:** confirm the CI verification (particularly all eight HostX64 groups and 256 exact switches), dispose of K2, and recommend Stage B+ closure or clearly identify any remaining action.
