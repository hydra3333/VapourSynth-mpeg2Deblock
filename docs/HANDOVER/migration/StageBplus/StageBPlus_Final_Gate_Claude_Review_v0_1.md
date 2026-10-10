# Stage B+ v0.2 — consolidated local gate evidence for Claude (2026-10-11)

**Role:** ChatGPT candidate coder's evidence handoff for Claude's *independent Stage B+ post-application gate review*, then Dave's ratification. **This is not Claude approval, a Git commit, or a claim of CI-binary functional testing.** Production files are not modified by this package.

## Decision requested from Claude

Review whether applied Stage B+ candidate **v0.2** satisfies the ratified migration policy and whether the supplied local Gates A–F warrant acceptance. In particular, explicitly disposition two toolchain-generated DLL switch/definition entries (B6 below). Please distinguish any genuine blocker from normal Visual Studio defaults, and do not modify the candidate without Dave's authorisation.

## Baseline, application, and scope

- Repository: `VapourSynth-mpeg2Deblock`, `main`; preapplication snapshot `3564f8581a3628e07ccc9f8338efb6a1bbfed2c0`, accepted A3 inspector project SHA-256 `73e9019cda7d1061ecdb06526c60f4ee84baa4c385b7ca0dde4269544e4fdb46`.
- Prior independent candidate verdict: Claude's `Claude_REVIEW_OF_ChatGPT_StageBPlus_Candidate_v0_2.md`: **ready for Dave to ratify/apply** after fixing v0.1 B1–B6. Dave ratified. Windows toolset probe validated package integrity; seven production files were copied from the ratified candidate. Reported `git diff --check` PASS for initial application; no inspector C/H source changes were reported.
- Two modified tracked files: inspector `.vcxproj` and solution `.slnx`. Five new files: DLL `.vcxproj`, `.filters`, `src/mpeg2Deblock/plugin.cpp`, `plugin_version.h`, `mpeg2Deblock.rc`. Other material in `docs/HANDOVER/migration/StageBplus/` is working/review evidence and not automatically part of production.
- Inspector relative to A3: only two toolset property replacements (`v145` -> `$(DefaultPlatformToolset)`), two native CL EHCONT properties, two native LINK EHCONT properties, and a numeric minimum toolset target. Inspector `.filters` untouched. No source edits.

## Local gate results

| Gate | Result | Evidence and qualifications |
|---|---|---|
| **A Toolset guard** | **PASS** | Candidate ZIP SHA inventory valid; VS Community 2026 `18.10.12224.181`; `MSBuild.exe` from `...\MSBuild\Current\Bin\amd64`. Real v0.2 project property/target evaluation Debug and Release: `DefaultPlatformToolset=v145`, `PlatformToolset=v145`, guard PASS both. Isolated *exact* target: `v145` PASS, `v143` rejected, synthetic `v150` PASS, `vX` rejected, empty rejected. Probe made no project builds or repository edits. `v150` is only synthetic, not an installed toolset. |
| **B GUI clean rebuilds** | **PASS** | Inspector EXE + plugin DLL, Debug x64 and Release x64: **2 succeeded / 0 failed / 0 skipped** in each configuration. Inspector **17 known C4013/C4101/C4996 warnings** in each configuration, DLL **0 warnings**, no LNK4291 observed. Build output in `evidence/B_GUI_Rebuild_Console.txt`. |
| **C measured CL/LINK/RC** | **PASS, B6 reviewer disposition outstanding** | Ten original UTF-16 `.tlog` traces (inspector CL/LINK x2, plugin CL/LINK/RC x2). Inspector 113 A3 tokens -> 117 current tokens, with exactly one `/guard:ehcont` added to each of Debug CL, Debug LINK, Release CL, Release LINK; no other baseline differences. New DLL has 139 normalized tokens; 256 combined tokens; DLL CL Debug `/MDd`, Release `/MT`, both `/arch:AVX2`, `/fp:precise`, CFG/EHCONT, DLL LINK protections, C++ settings and RC pins as specified. Measured CSV and technical review supplied. |
| **D Release binary analysis** | **PASS** | Both PE32+ x64 binaries Large Address Aware, DEP/NX, high-entropy ASLR, CFG, CET compatible, security cookie. `dumpbin /loadconfig`: Guard Flags `10417500`; inspector EH continuation table **0xF=15** entries, plugin **0xB=11**; CFG FID counts `0x37=55` and `0x2E=46`. Both Release binary imports list KERNEL32.dll only; PDB references filename only. Plugin unmangled export `VapourSynthPluginInit2`; GUI subsystem; empty embedded manifest with no elevation request; embedded VERSIONINFO 0.1.0.0 and correct file description/name. Inspector EXE uses `asInvoker` and SegmentHeap. **Scope: Release binaries were inspected; Debug binary PE tables were not independently dumped.** |
| **E portable R81 plugin runtime** | **PASS** | Dave ran portable `D:\TEST\Vapoursynth_x64_R81\python.exe` and loaded local Release `mpeg2Deblock.dll` through `core.std.LoadPlugin(path=...)`; `core.mpeg2deblock.Identity` on 64x64/2-frame `BlankClip` returned matching dimensions/count; retrieved two output frames and original frame. Actual console reported PASS and printed DLL path. Evidence transcript provided below in separate file. |
| **F six local inspector index regressions** | **PASS** | Dave ran all six required scripts locally and serially with Release inspector; every log shows `*** Inspector returned exit code: 0`, analyzer `VALID`, and VapourSynth R81 frame output for expected frame count. Four relevant `.vpy` scripts additionally compare BestSource picture-type vs indexed picture-type across all frames, twice (info/clip output): **300/300, 204/204, 216/216, 420/420**, all MATCH. The first two clips (300 frames each) use source-frame/decode validation without picture-type cross-comparison. Final explicit `git --no-pager diff --exit-code -- "VHSC_samples/*.idx"` returned `INDEX_COMPARE_RC=0` (all tracked reference indexes byte-identical); project/solution-only `git diff --check` returned `PROJECT_DIFF_CHECK_RC=0`. |

### Gate F case-by-case diagnostics

| Original index | Inspector result | Analyzer | VapourSynth result | Baseline comparison |
|---|---|---|---|---|
| `TEST_2A_A001.idx` | 0 | VALID, 704x576, 300 frames | 300 output frames | byte-identical |
| `TEST_2A_A001_blocky.idx` | 0 | VALID, 704x576, 300 frames | 300 output frames | byte-identical |
| `TEST_4A_A003.idx` | 0 | VALID, 720x576, 300 frames | 300/300 picture types MATCH, twice | byte-identical |
| `LG_576i_3_LP.idx` | 0 | VALID, 720x576, 204 frames | 204/204 picture types MATCH, twice | byte-identical |
| `LG_576i_4_EP.idx` | 0 | VALID, 352x576, 216 frames | 216/216 picture types MATCH, twice | byte-identical |
| `LG_576i_5_MLS.idx` | 0 | VALID, 352x288, 420 frames | 420/420 picture types MATCH, twice | byte-identical |

No runtime `Traceback`, `Error:`, or `Failed to` diagnostics were found in these original six logs. One **console-only** FFmpeg interactive parse error occurred on the *initial* first-script run when several `call` commands were pasted together; the inspector still returned zero and its index was byte-identical. The remaining calls were run individually; no such FFmpeg error appears in the archived six logs. The first index was separately compared early as well as in the final six-index Git check.

The first `git diff --check` across *all tracked files* reported trailing whitespace in six regenerated `.log` files. These log files contain captured program output and are **not** source changes. The subsequently scoped two-project/solution whitespace check passed. **The six tracked diagnostic logs have not been restored yet**; preserve the logs until review, then Dave may restore only those known files. Do not `git restore .` because that would discard ratified Stage B+ modifications.

## Explicit Claude B6 review: inherited DLL values

1. **`/D _WINDLL`:** Appears in both DLL CL traces in addition to explicit `NOMINMAX`, `_DEBUG`/`NDEBUG`, `_WINDOWS`, `_USRDLL`; understood to be an automatically inherited Visual Studio DynamicLibrary macro. **Proposed disposition:** accept/document it as an expected toolchain-generated definition; no redundant explicit source/project macro necessary.
2. **`/TLBID:1`:** Appears in both DLL LINK traces despite no explicit `TypeLibraryResourceID` project pin. It is an MSVC default link switch; presence alone **does not prove a type library resource exists**. **Proposed disposition:** independently decide accept as inherited toolchain default, or demand an explicit pin solely for traceability; avoid changing the candidate silently. No observed functional problem.

## Boundaries / subsequent stages

- Gates A–F are **local** results. The inspector's earlier Stage A3 v0.10 six-index waiver remains accurately recorded as **WAIVED**, not retroactively PASS; this *new Stage B+* Gate F is genuinely PASS. As ratified in O7, **GitHub Actions does not execute the six-index regressions**, and Dave accepts residual divergence risk between tested local binary and Actions-built release EXE.
- DLL remains only an **Identity scaffold**. No actual MPEG-2 deblocking functionality has been implemented or represented as passing. Technical Stage2 experiments/development remain paused until migration closure and Dave authorises them (O6).
- Gate C tlogs and VS2026 `dumpbin` indicate matching toolchain version `14.51.36260.0`; the tlogs do **not independently expose host `cl.exe`/`link.exe` paths**. Native x64 MSBuild was discovered for the toolset probe, while the GUI itself performed the builds. If the final gate requires positive *actual GUI host-path* proof, flag that narrow evidence gap; do not assert path provenance from tlogs alone.
- Stage B+ code is **not yet committed**. Upon Claude review and Dave ratification, update the single living `Migration_Status.md` in the agreed minimal manner, clean only generated test logs/review debris as desired, and commit on `main`. The *existing* GitHub Step1 proving workflow/113-token reference must be **deliberately reconciled to the 117-token EHCONT inspector state** before rerun; final dual-project CI and release workflow belongs to Step3. Do not silently update CI expectations or claim Actions tests already passed.

## Evidence bundle inventory

- `candidate/StageBPlus_CANDIDATE_FOR_CLAUDE_v0_2.zip`: exact ratified candidate package supplied previously.
- `candidate/Claude_REVIEW_OF_ChatGPT_StageBPlus_Candidate_v0_2.md`: independent candidate approval **before** installation/testing.
- `evidence/A_Toolset_Guard_User_Console.txt`, `evidence/B_GUI_Rebuild_Console.txt`: Dave's reported local probe/build outputs.
- `evidence/C_Actual_Tlogs.zip`, `evidence/C_Measured_Switches.csv`, `evidence/C_Review_v0_1.md`: original compiler/linker/resource traces and analysis.
- `evidence/D_Release_PE_and_Resource_Evidence.zip`: original Release binary dumpbin/mt/version evidence.
- `evidence/E_Portable_R81_Identity_User_Console.txt`: Dave's literal PASS line and plugin path.
- `evidence/F_Original_Six_Logs.zip`, `evidence/F_Commands_and_Git_User_Console.txt`: original six diagnostic logs and local test/Git verification evidence.
- `PACKAGE_SHA256.txt`: hash inventory for outer package member files (excludes itself). Original nested ZIP archives are retained, byte-for-byte.

**Recommendation:** Gates A–F warrant local technical acceptance, conditional only upon the independent Claude B6 inherited-switch disposition and any specific evidence completeness objection; Dave decides final acceptance and next steps. No unreviewed source/project corrections recommended.
