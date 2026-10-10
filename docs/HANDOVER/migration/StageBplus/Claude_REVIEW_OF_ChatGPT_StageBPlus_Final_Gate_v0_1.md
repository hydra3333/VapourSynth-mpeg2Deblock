# Claude review - Stage B+ local gate (A-F)

File: Claude_REVIEW_OF_ChatGPT_StageBPlus_Final_Gate_v0_1.md
Version / date: v0.1 / 2026-10-11
Author: Claude (migration chat, independent reviewer)
Reviewed: StageBPlus_Final_Gate_Claude_Review_v0_1.zip, including:
- ChatGPT's `StageBPlus_Final_Gate_Claude_Review_v0_1.md`;
- the ten original tlogs;
- the measured CSV;
- the Release dumpbin, manifest, export and version captures;
- the Gate A, B, E and F consoles;
- the six original Gate F logs.

## 1. Verdict

ACCEPT the Stage B+ local gate. I checked the evidence myself rather than relying on the summary. Two conditions apply:
- K1: the commit order in section 5;
- K2: HostX64 proof comes from the CI rerun.

B6 is decided in section 4: accept both inherited values.

## 2. What I verified independently

| Gate | My check | Result |
|---|---|---|
| Package | SHA-256 inventory | 13/13 OK. The header line is text, which is why sha256sum warns about one line. |
| A | console | The real project resolves `DefaultPlatformToolset=v145` and `PlatformToolset=v145` in Debug and Release, and the guard passes. Isolated cases: v145 pass, v143 fail, v150 pass, vX fail, empty fail. VS Community 18.10.12224.181, amd64 MSBuild. |
| B | GUI console vs the A3 local logs | 2/2 projects succeeded in each configuration. Inspector warnings: 17 per configuration, and the (file, line, code) set is identical to A3 for both. DLL: 0 warnings. No LNK warnings, so no LNK4291. |
| C, inspector | measured CSV vs `expected_a3_v0_10_switches.csv` | The **only** change per key is one added `/guard:ehcont`: Debug CL 33 to 34, Debug LINK 23 to 24, Release CL 32 to 33, Release LINK 25 to 26 (113 to 117). Nothing is removed. |
| C, CSV fidelity | my own Windows-rules tokenisation (N1) of all ten tlogs vs ChatGPT's CSV | Same tokens in every key. The only differences are representation, using the A3 conventions: `/D X` joined, `LIBS=` grouped, `<PATH>`. |
| C, DLL | every DLL token | See section 3. All trace to pins except `/D _WINDLL` and `/TLBID:1` (B6). |
| C, RC | rc tlogs | `/D _DEBUG` or `/D NDEBUG`, `/l"0x0409"`, `/nologo`, `/fo`. These exactly match the pins. |
| D | Release dumpbin | Both binaries are x64, Large Address Aware, High Entropy VA, Dynamic base, NX, CFG and CET compatible, with a security cookie. Guard Flags `10417500`: "EH Continuation table present", the same value as Microsoft's own example. EH continuation count: inspector 0xF, DLL 0xB. Guard CF count: inspector 0x37 (unchanged from A3), DLL 0x2E. Both import KERNEL32.dll only. The PDB name is a bare file name. The DLL is subsystem Windows GUI, with one export `VapourSynthPluginInit2` (unmangled). The DLL manifest is empty `<assembly>`, with no trustInfo. VERSIONINFO is 0.1.0.0 with the expected strings. |
| E | console | Portable R81: LoadPlugin, `Identity` on BlankClip, dimensions and count match, both frames fetched, the source stays valid. PASS. |
| F | six logs, the Git console, the repo snapshot | All six report "Inspector returned exit code: 0". Each script **deletes and regenerates** the index in place under `VHSC_samples\`, and all six `.idx` files are tracked in the repo (confirmed in the GitHub snapshot). So `git diff --exit-code -- "VHSC_samples/*.idx"` = 0 is a real byte comparison of all six; a missing file would also have failed it. PASS. |

## 3. DLL token audit (Debug / Release)

- **CL** tokens and the pins they come from:
  - `/c`, `/I<PATH>` (include directory), `/Zi`, `/JMC` in Debug only (SupportJustMyCode), `/nologo`, `/W3`, `/WX-`, `/diagnostics:column`, `/sdl`;
  - `/Od` or `/O2`, `/Ob2`, `/Oi`, `/Ot`, `/GL` in Release only;
  - `/D NOMINMAX`, `/D _DEBUG` or `/D NDEBUG`, `/D _WINDOWS`, `/D _USRDLL`, **`/D _WINDLL`**;
  - `/GF-` or `/GF`, `/Gm-`, `/EHsc`, `/RTC1` in Debug, `/MDd` or `/MT`, `/GS`, `/guard:cf`, `/Gy-` or `/Gy`, `/arch:AVX2`, `/fp:precise` (with no `/fp:contract`), `/guard:ehcont`;
  - `/Zc:wchar_t`, `/Zc:forScope`, `/Zc:inline`, `/GR`, `/std:c++20`, `/permissive-`;
  - `/Fo`, `/Fd`, `/external:W3`, `/Gd`, `/TP`, `/FC`, `/favor:blend`.
- **LINK** tokens and the pins they come from:
  - `/OUT`, `/INCREMENTAL:NO`, `/NOLOGO`, `LIBS=` (the same inherited default list as the inspector, accepted at A3);
  - `/MANIFEST`, `/MANIFESTUAC:NO`, `/manifest:embed`, `/DEBUG:FULL`, `/PDB`, `/SUBSYSTEM:WINDOWS`, `/LARGEADDRESSAWARE`;
  - `/OPT:NOREF` and `/OPT:NOICF`, or `/OPT:REF` and `/OPT:ICF`; `/LTCG` in Release;
  - **`/TLBID:1`**, `/DYNAMICBASE`, `/NXCOMPAT`, `/IMPLIB`, `/MACHINE:X64`, `/CETCOMPAT`, `/guard:cf`, `/guard:ehcont`, `/HIGHENTROPYVA`, `/PDBALTPATH:%_PDB%` in Release, `/DLL`.
- Compared with the inspector, the DLL differs only by:
  - CL: the defines, `/GR`, `/I`, `/permissive-`, `/sdl`, `/std:c++20`, `/TP`;
  - LINK: `/DLL`, `/MANIFESTUAC:NO`, `/SUBSYSTEM:WINDOWS`.
  It drops `/TSAWARE`, `/MANIFESTINPUT` and the asInvoker UAC.
  These are exactly the ratified differences.

## 4. B6 disposition: accept both, record both

- `/D _WINDLL`: MSBuild adds it for every `ConfigurationType=DynamicLibrary`, in the same way it adds the inherited `LIBS=` list. Accept it; no pin is needed.
- `/TLBID:1`: this is the linker's type-library resource ID. It does nothing unless a type library is embedded, and none is. The inspector carries the same token through its `TypeLibraryResourceID=1` pin. Accept it as inherited.
- Why this is consistent with "no defaults": G5's strict switch check fails the build loudly if Microsoft ever changes either value. A default that is measured and locked in the expected file cannot drift silently. Mark both rows as "toolchain-inherited, accepted 2026-10-11" in the new expected CSV.
- Optional, later: pin `TypeLibraryResourceID=1` in the DLL to mirror the inspector. Not now, because it would reopen this gate for no change in output.

## 5. Conditions and next actions

**K1. Order of work.**
1. Dave decides the six regenerated tracked `.log` files. Either restore exactly those six paths (`git restore -- <six paths>`; the B+ copies are kept in the evidence zip), or commit them as the new run's logs. They contain captured output only. Do **not** run `git restore .`.
2. Commit the seven production files (inspector `.vcxproj`, `.slnx`, DLL `.vcxproj` and `.filters`, `plugin.cpp`, `plugin_version.h`, `mpeg2Deblock.rc`) to `main` as a Snapshot commit, then push.
3. ChatGPT prepares one small candidate for the proving workflow, which I review:
   - new expected-switch data from the measured CSV (256 rows: inspector 117, DLL CL, LINK and RC, plus the two B6 rows marked);
   - the checker extended to the DLL project and the RC tool;
   - the A3 CSV kept as history.
   If the workflow is not updated, it will fail on the 4 new inspector tokens. That is correct behaviour, but it is not a test.
4. Run the updated proving workflow on `main`, using the manual button only.

**K2. HostX64 for the GUI build.** The tlogs carry no tool path, as ChatGPT rightly says. `PreferredToolArchitecture=x64` is pinned in both projects. It was proven for the inspector at A3 (local detailed log) and Step 1 (CI). The step 4 CI run proves it positively for both projects, and that run is the closure.

**Notes:**
- Debug binaries were not dumped. That is acceptable: Debug is not distributed, and the Debug switches are fully covered by gate C.
- Migration_Status (P1): record Stage B+ gate PASS. The six-index result is **PASS** (new, Stage B+); A3 v0.10 stays WAIVED.
- Gate E used portable R81 while the vendored headers are R78. API4 is backward compatible, and the load proved it. Record R81 as the runtime tested.
