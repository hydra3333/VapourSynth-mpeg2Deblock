# Stage B+ Gate C - measured CL/LINK/RC trace assessment (2026-10-10)

**Evidence:** `StageBPlus_GateC_Actual_Tlogs.zip`, provided by Dave, SHA-256 `dc4841e97b38e424e31db82c26211aaafccf03eb0aa0ed8d4c09fa526f844190`. ZIP integrity PASS; 10/10 nonempty UTF-16 command traces. All ten traces classified and extracted without unknown arguments. Original traces remain unmodified.

**Status:** Effective-switch comparison **PASS** against the accepted A3 v0.10 inspector and the ratified DLL build policy. The full Claude B6 source/pin reconciliation has two inherited entries requiring explicit review/acceptance (below). This is **not** a substitute for Gate D/E/F, or an assertion of a completed Stage B+ final gate.

## Inspector - exact comparison to accepted A3 v0.10

| Configuration | Tool | A3 tokens | Current | Exactly added | Removed | Other differences |
|---|---|---:|---:|---|---|---|
| Debug x64 | CL | 33 | 34 | `/guard:ehcont` | None | None |
| Debug x64 | LINK | 23 | 24 | `/guard:ehcont` | None | None |
| Release x64 | CL | 32 | 33 | `/guard:ehcont` | None | None |
| Release x64 | LINK | 25 | 26 | `/guard:ehcont` | None | None |

The original A3 baseline has **113** normalized tokens; the current inspector has **117**. Removing only `/guard:ehcont` from each current command yields the original baseline **in the same order** (LINK capitalization compared case-insensitively). All 16 inspector CL source records within each configuration have identical switch sets. No `/LTCGOUT` was introduced.

## DLL - first measured token inventory

| Configuration | CL | LINK | RC |
|---|---:|---:|---:|
| Debug x64 | 42 | 23 | 4 |
| Release x64 | 41 | 25 | 4 |

The DLL adds **139** normalized tokens, giving **256** normalized rows across both projects. The accompanying `StageBPlus_GateC_Measured_Switches.csv` retains each configuration/tool/ordinal/token, with path-valued arguments normalized. The active historical A3 switch CSV and YAML have **not** been modified.

### DLL checks supported directly by command traces

- Debug `/MDd`; Release `/MT` and `/GL` + linker `/LTCG`; no `/LTCGOUT`.
- Both configurations `/arch:AVX2`, `/favor:blend`, `/fp:precise`, `/GS`, `/guard:cf` and `/guard:ehcont` on **both CL and LINK**, and linker `/CETCOMPAT`, `/DYNAMICBASE`, `/NXCOMPAT`, `/HIGHENTROPYVA`, `/LARGEADDRESSAWARE`, `/MACHINE:X64`.
- Neither project uses `/fp:contract` nor `/Qspectre` in any current CL command.
- DLL `/sdl`, `/EHsc`, `/GR`, `/std:c++20`, `/permissive-`, `/TP` and `/I<PATH>`; Debug defines `NOMINMAX`, `_DEBUG`, `_WINDOWS`, `_USRDLL`, `_WINDLL`; Release defines `NOMINMAX`, `NDEBUG`, `_WINDOWS`, `_USRDLL`, `_WINDLL`. The DLL deliberately omits `_CRT_SECURE_NO_WARNINGS`.
- DLL LINK uses `/DLL`, `/SUBSYSTEM:WINDOWS`, `/MANIFESTUAC:NO`, `/manifest:embed` and `/LARGEADDRESSAWARE`; no EXE-only `/TSAWARE`, `/MANIFESTINPUT` or asInvoker manifest option. Both configurations emit `/TLBID:1` (see B6 note below).
- DLL RC Debug `/D _DEBUG`, Release `/D NDEBUG`, both `/l0x0409`, `/nologo`, `/fo<PATH>`. This is resource **compilation** evidence, not inspection of the embedded resource in the final DLL.

### Claude B6 - two measured inherited entries to disposition explicitly

1. **`/D _WINDLL` (Debug and Release):** This appears in the actual DLL CL traces even though the DLL `.vcxproj` lists only `NOMINMAX`, `_DEBUG`/`NDEBUG`, `_WINDOWS` and `_USRDLL` plus inherited definitions. It is an automatically inherited Visual Studio DynamicLibrary definition. Recommend **explicitly accept and document it as a toolchain-generated entry** (rather than add a redundant user definition).
2. **`/TLBID:1` (Debug and Release):** This appears in the DLL LINK traces even though the DLL `.vcxproj` deliberately omits an explicit `<TypeLibraryResourceID>` setting as 'EXE-only'. The corresponding accepted inspector explicitly sets `TypeLibraryResourceID=1`; Microsoft documents that 1 is the default resource ID **if a linker-generated type library exists**. This flag alone does **not** prove a type library exists. Recommend Claude explicitly decide whether to **accept the observed VS default** or **pin `TypeLibraryResourceID=1` for no-defaults traceability**, documenting that it is not needed for DLL product functionality. Do **not** alter the ratified production project silently.

All other measured DLL tokens correspond to accepted inspector conventions, native project properties, declared C++/DLL differences, or the standard VS toolchain/output controls. Library names in the LINK command are link *inputs*; they do **not** demonstrate runtime DLL imports. No program binary was present in this evidence ZIP.

## Method and limitations

- Decoded original UTF-16LE `.tlog` files; split command arguments using Microsoft-compatible quote/backslash rules; used a normalized `LIBS=` list and substituted `<PATH>` for output/PDB/import-lib/include/resource-output paths. The tool was run in a Linux container, so it did **not** invoke native `CommandLineToArgvW`; the extractor exactly reproduced all 113 historical baseline tokens when current EHCONT tokens were omitted. LINK switch capitalization differences are case-insensitive. Normalizations are confined to comparison output, not input evidence.
- The inspector tlogs contain 16 repeated compiler commands per configuration; the DLL contains 1 compiler and 1 RC command per configuration. Link tlogs list multiple object/resource input records; only the first line contains switches.
- A tlog records arguments, not necessarily executable host-path/version; actual HostX64 CL/LINK invocation/version still needs separate build-log or tooling evidence.
- **Gate D still required:** `dumpbin /headers`, `/loadconfig`, `/dependents`, `/imports`, `/exports`, embedded manifest and VERSIONINFO inspection; prove EH Continuation table/count, CFG, CET, PE protections, release imports, export and version resource. `/guard:ehcont` command-line presence by itself does not prove an EHCONT table was embedded.
- **Gate E still required:** VapourSynth `Identity(BlankClip())` call with frame retrieval.
- **Gate F still required:** all six inspector reference indexes run locally (O7). Stage A3 v0.10's earlier waiver remains **WAIVED**, not PASS.

**Recommendation:** The effective-switch portion of Gate C passes. Resolve the two B6 inherited-entry dispositions with Claude during acceptance review, without changing the existing A3 CSV. Proceed to Gate D to obtain binary-level evidence.
