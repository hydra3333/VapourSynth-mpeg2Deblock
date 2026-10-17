# ChatGPT Handover to Future ChatGPT Chat
## MPEG-2 Macroblock Index / VapourSynth Deblocking Project

**Document:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_9.md`

**Version:** 0.9

**Date / evidence cut-off:** 2026-10-17, after the owner's final `3A_blocky` P0D diagnostics console output, before any P0D pair run.

**Prepared by:** the active ChatGPT development role, revising Claude-cleared v0.8 with owner Windows P0 outputs, Claude's P0 review and consolidated interim findings, and the owner's reported snapshot commits.

**Status:** Full ChatGPT role continuity record, **not** technical/design authority. Replaces v0.8 in the current tree **only when** the owner approves and installs it under D-23 v1.2 (one addition, one predecessor deletion). Previous v0.8 correctly described its own earlier as-at boundary and must not be used as the current operational checkpoint.

**Verified HEAD of `main`:** `4636c33ebd7fd053149bebac8bc2dbe2d754d090` (owner reported the short SHA `4636c33`; Claude resolved the full SHA and commit contents from a fresh clone on 2026-10-18), following `6b7acc3` and `3f8f45a`. The ratified S2-I3 design/code REVIEW reference remains `35cd543b459a5856688f7c3795f73226e72311f8`; do not mistake it for live HEAD. HEAD may have moved after 2026-10-18, so verify it again before any Git change.

**Immediate stop point:** P0A PASS; P0B all eight index identities available/verified (six generated, one copied, one frozen); P0C **8/8 REGISTERED**; P0D descriptive diagnostics **8/8 COMPLETE**, all exit 0; P0D pair tests **0/4 RUN**; summary and independent complete-evidence review pending. The next operation is **PAIR_XP**. No filtering, seven-index Git tracking commit or P1 authorisation.

---

## Reading this handover correctly

This v0.9 is a full continuity handover. A future development chat should read it, verify the actual live repository and scratch evidence, read owning ratified documents, determine any later delta, and continue without reconstructing days of conversations. The current P0 event log lives in the companion status handback v0.3. Its review-candidate filename carries a `_FOR_CLAUDE_...` suffix, but on installation under D-23 it takes the repository name `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_3.md`, exactly as v0.2 did; look for that path, not the review-candidate name, which never enters the tree. This v0.9 does NOT claim v0.3 has already been installed or that Claude has inspected the final P0 evidence.

Authority hierarchy: owner-ratified `docs/REPOSITORY/` specifications/decisions and `NOTICE.md` prevail. Design v0.3 and Stage 2 v0.7 control requirements. The interim knowledge bridge is not a new authority. Visual Studio projects own build settings; CI/workflows own release checks. Claude review is an independent evidence source, not authority; owner ratification governs changes. Later conversational owner authorisations must be distinguished from earlier committed status-doc as-at claims.

**Agreed continuity-purpose text**, quoted verbatim from `docs/HANDOVER/ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT_FOR_BOTH_ROLES.md`. Claude checked the quote against the committed file and it is faithful, including the garbled phrase `important the project owner conversational decisions` at line 11, which is a defect in the committed source file (it reads as a substitution into `important owner conversational decisions`) and not an error introduced here. Leave the quote as it stands; repairing the source file is a separate bounded D-23 change:

> The role handover is fundamentally a communication from the current development chat to its eventual
> successor when the current chat approaches its conversation limit.
>
> Its purpose is continuity. It should be a reasonably comprehensive "state of the project as
> understood by this chat, as at this point in time" document, not merely a short index into repository
> authority.
>
> It should preserve whatever a successor would materially benefit from knowing, including current
> status, roles/process, ratified rules, important the project owner conversational decisions, evolved conventions,
> technical understanding, settled/provisional/open/superseded matters, negative decisions, sample
> roles/evidence limitations, immutable baselines, build/test/plugin state, outstanding work/gaps,
> next and upcoming work, blockers/authorisation gates, known traps/caveats/lessons, and references to
> owning authority/evidence documents.
>
> Authority documents still prevail on conflict and the handover does not replace them. However,
> references must not make the handover so skeletal that the successor has to reconstruct the current
> working model from scratch.
>
> At takeover:
> 1. read the handover;
> 2. establish live repository/document state;
> 3. read owning authorities needed for the task;
> 4. determine the delta between the handover's stated as-at point and takeover;
> 5. reconcile only that delta;
> 6. continue development.
>
> Refresh the handover periodically as major state changes, not only at final conversation exhaustion.

## 0. Read this first: current state and next action

| Area | Actual state at v0.9 evidence cut-off |
|---|---|
| Migration/repository restart | CLOSED on 2026-10-11; development is in post-migration history |
| Stage 1 | COMPLETE / PASS / FROZEN; six immutable accepted indexes |
| S2-I1/S2-I2 | COMPLETE / COMMITTED, including S2-I2 accepted numerical evidence |
| Controlling design | Stage 2 v0.7, S2-I3 Full-Data v0.3; 2026-10-17 P0-only implementation authorisation granted after status v0.7 |
| P0 code | S4 independently CLEARED, then one-BAT isolated-Python fix also CLEARED; 15 implementation files installed and committed at `4636c33` (count verified by Claude at HEAD) |
| P0A | Owner Windows PASS, 9/9 P-skip + 5/5 pair unit tests and runtime preflight |
| P0B | Six generated reference-equal indexes; LP_blocky byte-copy verified; LP original frozen index reused |
| P0C | **8/8 REGISTERED** with exact P skips and P-picture counts matching Claude references |
| P0D descriptive diagnostics | **8/8 COMPLETE**, full frame counts and rc=0; not admission or a quality gate |
| P0D pairs | **0/4 run**, XP next, then SP, LP and 3A |
| Global summary / evidence acceptance | NOT RUN / NOT ACCEPTED; Claude has not inspected complete `results/` tree |
| Seven new index tracking commit | NOT MADE; separate only AFTER evidence acceptance |
| P1, filtering, S2-I4 | NOT AUTHORISED |
| Knowledge preservation | Claude consolidated `interim_` once, installed at `4636c33`; eventual evidence/K-item transfer still pending |
| Git hygiene | Four publicly tracked identity-bearing review paths remain, re-confirmed present at verified HEAD on 2026-10-18; the two D-23 predecessors likewise; `4636c33` added 8 further review-only paths but **no new identity carrier**; owner deferred until tests finish |

**Immediate owner action:** run the reviewed `S2_I3_P0D_pair_v0_1.bat` **for XP only**, then inspect console output and `results\PAIR_XP\pair.log`. Start the CMD block with `cd /d` to the repository root. A future developer MUST NOT rerun already completed preparation, admission, or diagnostics; these tools refuse overwrites and the evidence must remain intact. The complete command and expected metrics are in status handback v0.3 section 6.

**Safety constraints:** EP/2A/4A original and all blocky hold-outs locked until S2-I8 regardless of filename. New 6A/7A media unassigned. No filtering or intermediate-QP media changes. A numerical `READY_FOR_P1` is not permission for P1; owner and Claude evidence acceptance plus owner authorisation are separate.

## 1. Project identity, scope and responsibility

Repository: `https://github.com/hydra3333/VapourSynth-mpeg2Deblock`, branch `main`.

Owner's Windows local working repository:

```text
E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock
```

Product architecture (D-24):

```text
MPEG-2 programme/elementary stream
    -> external frozen Mpeg2BlockInspector.exe
    -> matching MPEG-2 macroblock index (.idx)

Matching index + VapourSynth decoded frames + user strength
    -> future native MPEG-2 deblocking VapourSynth plugin
    -> corrected frames
```

The plugin will not itself parse the programme stream. Index metadata is authoritative for coded transform geometry and eligibility; local decoded pixels may decide whether a candidate seam is actual blocking or legitimate detail, and limit corrections. **No pixel-only production architecture or Family B contest**: these were superseded by D-24. Production scope includes native 4:2:0 chroma (D-25), although current P0 and S2-I3 early luma work are luma-focused.

Roles:

- **Owner:** project manager, ratifier, local Windows operator, final judge of visual quality; preserves real inputs, decides changes/commits.
- **ChatGPT:** primary drafting and coding partner; inspects authoritative source; prepares controlled packages and guided owner commands; reviews Claude proposals; never promotes a draft silently.
- **Claude:** independent technical/code/document reviewer against pristine committed source; executes/rehearses what can be executed under Linux/BestSource and audits Windows CMD semantics before owner execution; provides verdict, evidence and review/handback records.

Working sequence: ChatGPT drafts -> Claude independently reviews -> owner resolves/ratifies -> ChatGPT implements/proceeds. Either assistant can recommend a change of division of labour when justified; the owner decides. The owner prefers AI partners to resolve routine engineering matters rather than continuously escalating trivial choices.

**Execute-before-owner-runs (owner ruling 2026-10-13):** Claude should rehearse every executable procedure before owner use. A Linux run cannot prove Windows CMD syntax; BATs require source-level CMD audit as well. The owner runs only Claude-cleared candidates, with one small CMD block per message/step, sends back output/evidence, and stops on unexpected behaviour. Explicitly distinguish Claude's rehearsal from acceptance on the owner's actual Windows/BestSource path.

## 2. Repository, authority and implementation location

### 2.1 Git state and chronology

Project: `https://github.com/hydra3333/VapourSynth-mpeg2Deblock`, `main`. Owner's Windows repository root:

```text
E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock
```

The fresh-history root is `11f47427624bf5f68b3426fe9f58aa26d40e47f7`. Relevant accepted development milestones: `4221f7f` S2-I1 code, `190bd06` S2-I2 code, `6e7b5c5` S2-I2 evidence, `35cd543` ratified Stage 2 v0.7/S2-I3 v0.3/Project Status v0.7 documents. `6b7acc3` was the owner's interim snapshot adding successor role handovers, four new 6A/7A media files and review artefacts; `3f8f45a` removed one identity-bearing ZIP; `4636c33` was a second pushed snapshot adding 25 files, including the 15 P0 implementation files, the interim knowledge preservation bridge and P0 status v0.2. **HEAD is verified as `4636c33ebd7fd053149bebac8bc2dbe2d754d090`** (Claude, fresh clone, 2026-10-18: staged shape exactly 25 A / 0 M / 0 D against `3f8f45a`, tracked files 239 -> 264). A future chat must still verify `git rev-parse HEAD` before Git changes, because HEAD may have moved since.

The snapshots mean D-23 predecessor removal was NOT performed: `docs/HANDOVER/ChatGPT_...v0_7.md` and `Claude_...v0_9.md` coexisted with cleared successors v0.8 and v0.10. On v0.9 installation additionally remove ChatGPT v0.8 rather than keeping three versions. Cleanup should be organised as exact-path bounded commits, never a new blanket `git add -A`.

The v0.1.0 workflow-generated release remains a SNAPSHOT RELEASE, NOT a functional deblocker.

### 2.2 Actual repository authorities and evidence to consult

```text
docs/REPOSITORY/00_PROJECT_STATUS_v0_7.md
docs/REPOSITORY/05_DECISIONS_v1_2.md
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md
docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md
docs/REPOSITORY/S2_I2_Evidence_and_Gate_Report_v0_1.md
docs/REPOSITORY/Stage2_Experiment_Design_v0_7.md
docs/REPOSITORY/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md
docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md
NOTICE.md
README.md
```

The `interim_` document, consolidated once by Claude and committed in the owner's second snapshot, is a **temporary evidence bridge**, not technical/design authority. Its section 9 owns the transfer/retirement checklist. The S2-I3 Evidence and Gate Report and updated `06` K-03/K-07/K-08 are NOT yet written/ratified.

Design/decisions still in force: D-05/D-21 knowledge ownership, D-09 frame-owned interlace, D-13 extra-metadata constraint, D-16 I/P/B stratification, D-20 authority, D-23 version/identity controls, D-24 index-driven architecture, D-25 native 4:2:0 chroma, D-26 real-primary/paired-secondary evidence. An authority document with a HYPOTHESIS or OPEN label does not convert it into an established fact.

### 2.3 Code/build locations and actual runtime

```text
src/Mpeg2BlockInspector/                 frozen Stage 1 indexer
experiments/stage2/                     accepted S2-I1/S2-I2 + installed 15-file S2-I3 P0 overlay
experiments/stage2/results/S2_I2_v0_1/  accepted prior registration diagnostics
VHSC_samples/                           media, six frozen indexes and logs
vs/VapourSynth-mpeg2Deblock/            Visual Studio solution and projects
.github/workflows/                     CI/release workflow
docs/REPOSITORY/                        ratified specs/evidence + temporary interim bridge
docs/HANDOVER/                          role handovers and P0 status continuity
```

Owner uses Windows CMD, Visual Studio 2026 x64 developer prompt for builds, Visual Studio Code for editing. P0 observed VapourSynth R81, BestSource PluginVersion(22,0) with DLL SHA256 `fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c`, same DLL as accepted S2-I2; embedded Python **3.14.8** under `D:\TEST\Vapoursynth_x64_R81\python.exe`, NumPy **2.5.4** (earlier S2-I2 2.5.3). The `python314._pth` creates isolated imports and ignores `PYTHONPATH`. The owner-cleared P0A BAT invokes unit suites via explicit `sys.path.insert` and `runpy`; no edits to `_pth` or Python modules.

## 3. Core technical knowledge not to rediscover

### 3.1 MPEG-2 residual geometry and interlace

The `FRAME`, `FIELD`, `NONE` index state denotes **applicable coded residual-transform geometry**, not simply whether a `dct_type` syntax bit was read. Per K-07, `NONE` includes skipped macroblocks and non-intra macroblocks whose effective coded block pattern is zero, even if a `dct_type` bit might have been present. `NONE` has **no internal coded residual transform seams**; this does not prove it contains no visible inherited blocking. O-04 owns edges touching NONE.

In frame pictures, MPEG-2 luma FRAME/FIELD DCT organisation is selected **per macroblock** (K-02/K-03). The internal luma **vertical seam at x=8** occurs for both coded FRAME and coded FIELD; the internal **horizontal seam at frame row 8** exists for FRAME coding, but the FIELD organisation uses an 8-field-line pitch (16 frame lines) and does not have that same frame-row-8 horizontal seam. A FRAME/FIELD boundary comparison must name **which direction the shared boundary faces**: side-by-side macroblocks share a VERTICAL boundary (fixed x); stacked macroblocks share a HORIZONTAL boundary (fixed y).

**Critical access caution:** knowing FRAME/FIELD coded-residual geometry does **not** itself give permission to mix interlaced fields in the filter. A FRAME DCT is an encoder coding choice, not a guarantee of same-time adjacent frame lines. Frame-owned processing (D-09) stays in force; use field-parity-aware/same-field sample access where necessary. Do not implement separate independent field passes by inference.

For 4:2:0 chroma, per K-04, chroma transform organisation does not blindly follow luma `dct_type`; chroma remains part of the production mechanism scope, but **none of the new Oct 17 paired-pixel findings validates chroma**. Reference-decoder verifications V1-V4 are carried as ratified knowledge in `06_DEBLOCK_CONCEPT.md` (V1 in K-03, V2 in K-04, V3 in K-10, V4 in K-11); the current Claude role handover also records them with source line references. Do not upgrade decoder-implementation observations to normative standards claims without checking the relevant source or standard.

Motion-compensated content may inherit blocking displaced from the current macroblock grid (K-08). Stage 1 indexes store relevant coding/motion type/direction bits but **not numeric motion-vector values**. A skipped P-picture MB is guaranteed zero-vector and co-located; B skips can inherit vectors, and INTER CBP=0 can use nonzero vectors. Fractional-pixel prediction may interpolate inherited edges. Missing vectors are a possible limitation, not a demonstrated need to redesign/fork the frozen indexer. D-13 sets a high bar before extra metadata or `.idx2` is proposed.

### 3.2 Algorithm policy and negative knowledge

- Only current MPEG-2 index-driven architecture is in scope. Do not revive pixel-only seam discovery or superseded Family B.
- Native 4:2:0 chroma is not optional forever; current luma-first phases are staged, not a permanent exemption.
- Every candidate correction needs bounded support and edge/texture protection; **OFF must be pixel-bit-exact**.
- Stage 2 must explicitly report I/P/B and FRAME/FIELD/NONE effects where specified; leading B pictures before first usable reference are accounted for in structural diagnostics but excluded from appropriate quality inference.
- No external third-party deblocker is an authorised benchmark; do not quietly add one.
- The original member of an original/`_blocky` pair is the **higher-quality decoded reference**, not ground truth or an uncompressed source (D-26). Numerical movement toward it is secondary evidence; real recorder material and owner visual assessment remain central.
- A software `_blocky` re-encode with constant effective QP62 has deliberately severe damage. It **cannot** by itself establish the value of real spatial per-macroblock QP.

### 3.3 Frozen Stage 1 indexes and indexer traps

**Never regenerate, reformat or replace the six accepted `.idx` files.** They are SHA-guarded, formally accepted Stage 1 regression baselines. LP original:

```text
VHSC_samples/LG_576i_3_LP.idx
SHA-256 849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011
```

S2-I1's separately generated `TEST_4A_A003_blocky.idx` is a non-baseline scratch candidate for a protected hold-out; do not feed its source media to S2-I3 P0. New S2-I3 indexes must be generated into scratch, admitted against the known hashes, and only **the same bytes** later installed as seven non-baseline Stage 2 development inputs. Stage 1 itself stays frozen.

**Inspector short-read hazard:** the frozen `getbits.c` `Fill_Buffer()` treats a short `read()` (less than 2048 bytes) as an end condition; Linux pipe experiments produced an apparently COMPLETE but truncated index. Therefore **never pipe FFmpeg directly into the inspector for fresh Stage 2 index generation**. First FFmpeg-demux to a regular owned scratch `.m2v`, then invoke `Mpeg2BlockInspector.exe -b <scratch.m2v> -m <scratch.idx>` serially, gate on structure/count/hash, delete the `.m2v` after use. A successful exit alone proves nothing.

**Windows BAT traps:** two piped subprocesses must not concurrently append to the same log (sharing violation); a digit next to `>>` is interpreted as a CMD handle number (`0>>log`), so write `>>"%log%" echo ...`; capture `%ERRORLEVEL%` immediately after external commands, not after `for /f`; clear inherited capture variables before `for /f`; beware `(` and `)` in `echo` within parenthesised blocks (P0 M1); preserve CRLF for BAT files. Follow exact owner-cleared scripts, not improvised long pasted commands.

### 3.4 Build/regression, Git normalisation and release traps that must survive a handover

- **Mandatory six-index local regression:** after any change to the inspector's Visual Studio project-file settings, or any change in the **exact MSVC compiler/toolset version** (including a routine Visual Studio update), run all six local Stage 1 index regressions. A `.filters`-only edit is exempt; infrastructure-only changes instead require one LP smoke run. These regressions are **not** CI checks. Preserve frozen index hashes exactly; see repository build/change-control authority for the full procedure.
- **Dangerous test side effect:** the accepted `TESTING` BATs **overwrite tracked `VHSC_samples/*.idx` and `*.log` files in place**. After running them, compare the six frozen index hashes and `git diff`; do not commit regenerated baselines with `git add -A`. The S2-I3 scratch procedure is separate and must never write an index directly into `VHSC_samples`.
- **Git EOL and hash representations:** the owner's Git has `core.autocrlf=true`. `.py` and `.md` are generally stored **LF in Git** but appear **CRLF in the Windows working tree**; a SHA-256 hash of the Git blob and a SHA-256 hash of the working file can therefore differ without a content error. Always label the representation in any hash statement. Example: `stage2_index_reader_v0_2.py` was reported with working-tree CRLF SHA starting `139f02c6` versus Git-stored LF SHA starting `f9892039`. BATs are pinned CRLF by `.gitattributes`; `experiments/stage2/results/** -text` protects numerical evidence from normalisation.
- **Seven-index tracking check:** after copying only the exact SHA-verified admitted scratch bytes for the seven added indexes, check `git ls-files --eol` reports **`-text`** for every staged `.idx`; verify the exact named staged paths and expected `7 A / 0 M / 0 D`. The six frozen Stage 1 indexes are not part of this commit.
- **Release guard:** bump `src/mpeg2Deblock/plugin_version.h` before publishing a new Release. The GitHub Actions release workflow checks via `merge-base --is-ancestor` that the released tag commit belongs to `main` history. Use the current workflow and project files for full build/CI settings; do not substitute a handover summary for those contracts.
- **Hardware constraint:** both current x64 binaries target **AVX2**; there is **no runtime AVX2 capability detection and no non-AVX2 fallback** to offer. Do not claim cross-CPU support that does not exist.

## 4. Current Stage 2 experimental population and roles

### 4.1 Ratified eight-source S2-I3 development pool

Four independent **content groups**, each original plus software-transcoded `_blocky`:

| Group | Original stem | Blocky stem | Dimensions | Original `Q_fixed` |
|---|---|---|---|---:|
| XP | `LG_576i_1_XP` | `LG_576i_1_XP_blocky` | 720x576 | 14 |
| SP | `LG_576i_2_SP` | `LG_576i_2_SP_blocky` | 720x576 | 16 |
| LP | `LG_576i_3_LP` | `LG_576i_3_LP_blocky` | 720x576 | 18 |
| 3A | `TEST_3A_A002` | `TEST_3A_A002_blocky` | **704x576** | 14 |

Blocky encodes have constant QP62. `Q_fixed` is the clip-wide median over **all macroblocks**, including leading B and NONE, not a tuned result. QP variation in originals remains intact, and no media are narrowed to favourable GOPs or scenes. S2-I3's **fixed-QP** requirement controls an experimental kernel input: it does **not** re-encode originals into constant-QP or disregard their true QP measurements. Real-indexed-QP filter comparisons are reserved for separately authorised S2-I4.

Seven expected **new non-baseline development index** identities (six generated, LP_blocky existing S2-I2 scratch):

| Index basename | Expected SHA-256 |
|---|---|
| `LG_576i_1_XP.idx` | `4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127` |
| `LG_576i_1_XP_blocky.idx` | `8d0326b5975b19b36742717a80be9eaf11bc21f379f2855eb22651e94dd16b20` |
| `LG_576i_2_SP.idx` | `40a97ce1a9920cd63e45da13371e0b41ff1619fed688d6145899a300463cc5d9` |
| `LG_576i_2_SP_blocky.idx` | `7e19ca6078075e7bf7a3a34bcda0816267e4d38ad02a56e01b6b0ed726ace746` |
| `LG_576i_3_LP_blocky.idx` | `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238` |
| `TEST_3A_A002.idx` | `9a60a8d24a7e4a45cbe82b4f41d232ede0e5c00624e82a8f8099f61351957f33` |
| `TEST_3A_A002_blocky.idx` | `e6f556dd4aaed0f4709b7c011fcf045193dccbb8abd2a01c646dddf0da893c83` |

All reference hashes above came from Claude's independent Linux inspector rehearsal and must be verified against Windows-generated, exact bytes. Indexes contain metadata, not pixels or original paths; they do not inherit Restricted Media status merely by derivation. Binary files should remain Git binary (`-text`), unchanged through any commit.

### 4.2 Protected and control content

**Do not read/decode/recharacterise protected hold-out media for S2-I3 work:** `LG_576i_4_EP`, `TEST_2A_A001`, `TEST_4A_A003` and **their `_blocky` counterparts** are locked until S2-I8. Protection follows content, not filename. `LG_576i_5_MLS` (+ `_blocky`) is a separate control; its blocky recording previously exposed a 352x288 / progressive-frame mismatch trap, so never infer that a nominal pair shares geometry. Neither hold-outs nor MLS are in the eight-source P0 allow-list.

### 4.3 New 17 October recordings and the resolved duplicates

The owner temporarily created additional TEST_1A/8A/9A/10A renamings of existing XP/MLS/EP/LP recordings, then **deleted the duplicate pairs**. A subsequent owner PowerShell SHA-256 grouping verified **20 `.mpg` files / 20 distinct full hashes** in `VHSC_samples`: the original sixteen plus four genuinely new recordings. No duplicate hold-out leakage; the four standard development groups remain unchanged.

Unassigned new files:

```text
TEST_6A_home_576i.mpg
TEST_6A_home_576i_blocky.mpg
TEST_7A_home_576i.mpg
TEST_7A_home_576i_blocky.mpg
```

Reported SHA-256 *prefixes* (NOT full hashes):

```text
6A          0F8656F69591EC69
6A_blocky   0D53680AB8037FDA
7A          C68E209FDE087D7A
7A_blocky   17ABBC2C4EEB85AF
```

These pairs differ in provenance and likely duration; sizes do not prove frame counts, transform mix, pair alignment or suitability. **They have not been assigned a development/evaluation role or incorporated into the P0 allow-list.** Do not infer that a later approved source-pool expansion would give them equal *per-frame* weight: groups must be normalised rather than allowing much longer recordings to dominate. A possible Stage 2 v0.8 / S2-I3 v0.4 design revision remains future work, contingent on characterization and owner ratification.

The owner committed the four home `.mpg` recordings in snapshot `6b7acc3` as development media. Claude warned that `git rm` later does **not** erase public history, third-party clones or caches; their historical persistence has not been finally disposed of; Development Closure history scrub is still expected. Avoid describing this as a final public-release/privacy disposition. The agreed separate four-file commit shape was NOT used: all four went in with the mixed snapshot. No 6A/7A characterisation or new role has been authorised merely because the files are committed. The drafted `S2_I3_P0B_characterise_new_source_v0_1.bat` / characterisation ZIP was **STOOD DOWN**; do not install/run it. No change to `.gitattributes` is needed merely for `.mpg`/`.idx` (Claude checked Git treats tracked examples as binary).

## 5. S2-I3 full-data design (authority is v0.3 and Stage 2 v0.7)

The owner specifically favours using all genuinely relevant frames and content types. Work with all eligible data; do not conceal bad frames/GOPs or mistake 16x16 macroblock samples for independent content-group replications.

- Four **leave-one-whole-content-group-out** cross-validation folds: XP, SP, LP, 3A. Each pair's two members stay in the same fold. Fit selection procedures afresh on three groups and evaluate the untouched group. Distinguish this from external S2-I8 untouched hold-out evaluation.
- O = training on originals, X = blockys, J = joint weighted 2:1 original:blocky *inside each group*. Equal group weight (25% in four-group reporting; three training groups equal per fold). Record source-level results without hiding dispersion.
- Historical L=LP only and LB=LP+LP_blocky comparisons exist only for XP/SP/3A held-out folds; **N/A** for LP fold. Do not compare three-fold L/LB results to four-fold O/X/J aggregates.
- Compare procedures with matched search budgets and predeclared no-harm/seam/detail and owner visual criteria. The selected procedure's CV score is subject to selection optimism; it is not a genuinely untouched test-set estimate.
- After procedure selection, fit final **K0-J** on all eight, freeze it; also fit K0-O and K0-X for an in-sample comparison matrix; these final full-data fits are not CV evidence.
- Initial S2-I3 kernel procedure is designed to use B0 only (geometry, transform state, QP); coding-context feature B1 and `.idx2` are **not** authorised. Candidate M1-M5/M4a, F1-F3, R1-R4, T1/T2, P0-P2, K1-K4, D0/D1, G1/G2 option families remain documented; alternatives should not be quietly discarded. K4/Family C optional; no third-party deblocker benchmark.
- For S2-I4 (**future, not authorised**), distinguish two questions: (Q1) frozen K0-J QP input substitution fixed-clip median vs actual per-MB map, and (Q2) separately and symmetrically tuned fixed/indexed branches with matched budgets under grouped CV. Do not conflate those estimands or label refitted candidates as unchanged K0-J. Blocky Q62 material provides no real QP spatial variation.
- Report I/P/B, FRAME/FIELD/NONE, QP strata, exclusions/leading B, false alarms, OFF bit-exactness, seam-local corrections, collateral detail/texture and field-parity changes. Final quality includes owner's blinded visual comparisons and no-harm on clean originals.

## 6. S2-I3 P0 - scope, exact gates, actual owner run and next step

**P0 is registration, not filtering.** The S2-I3 v0.3 design and Stage 2 v0.7 restrict the allowed sources to XP, XP_blocky, SP, SP_blocky, LP, LP_blocky, 3A, 3A_blocky. Index-format validity, `output_ordinal`, picture type against BestSource `_PictType`, frame-picture structure, YUV420P8, geometry (including 704 width), hashes and correct source/index pair are hard prerequisites. The anchor for a skipped P MB is the last earlier **I/P picture in display order**, not mechanically frame n-1. Qualifying skipped P MBs must match the co-located 16x16 luma in that anchor bit-exactly. A mismatch HARD FAILS, insufficient opportunities/controls INCONCLUSIVE. There are 24 spatial and 3 temporal negative controls. Original/blocky pair test uses clip-wide k=-2..+2 MAE and the decisive-frame correspondence rule with zero allowed decisive violations, >=20 decisive AND >=10% decisive frames. Full derivation and limitations live in consolidated `interim_` sections 11 and 13. A field swap is undetectable by P-skip; IPPP sequences make the previous-display control unavailable. Do not claim more than the tests prove.

### 6.1 Actual cleared overlay and Windows incident

The 15-file overlay (7 BAT, 3 VPY, 5 Python) was installed under `experiments/stage2/`. Claude independently cleared the S4 change to run NumPy-based unit suites in the VapourSynth interpreter, but the initial Windows P0A found that its **embedded isolated** Python omits the script directory from `sys.path`: `ModuleNotFoundError: stage2_i3_pskip_core_v0_1`. P0A failed closed (rc=2) **before** creating scratch. A single-BAT-only correction explicitly provided the script directory with `runpy.run_path`, preserving all 8 original Python/VPY files; Claude cleared it and owner reran P0A successfully. Lesson: test invocations with `-I` and not just an ordinary interpreter; isolated Python ignores `PYTHONPATH`. Never redo P0A or reset scratch to revisit the defect.

P0A PASS: six frozen-index regressions, four negative cases, 9/9 P-skip unit tests, 5/5 pair unit tests, S2-I2 synthetic checks and VapourSynth runtime preflight, ERRORLEVEL=0. The regression line `EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent` was expected and NOT permission to generate a protected index.

P0B PASS: Windows MSVC frozen inspector generated 6 indexes with **full SHA equal** to Claude's independent Linux gcc outputs; LP_blocky copied without regeneration from S2-I2 scratch after both byte-level verifications, and LP original used its frozen repository index. Cross-platform determinism is observed **for these samples** only. Do not re-index or commit new indexes until P0 evidence acceptance.

### 6.2 All eight Windows source admissions (P0C) complete

| Label | P skips exact | Qualifying P pictures | Frames | Geometry | Status |
|---|---:|---:|---:|---|---|
| XP | 1619/1619 | 54 | 228 | 720x576 | REGISTERED, rc0 |
| XP_blocky | 25635/25635 | 55 | 228 | 720x576 | REGISTERED, rc0 |
| SP | 1764/1764 | 46 | 192 | 720x576 | REGISTERED, rc0 |
| SP_blocky | 19010/19010 | 46 | 192 | 720x576 | REGISTERED, rc0 |
| LP | 1533/1533 | 46 | 204 | 720x576 | REGISTERED, rc0 |
| LP_blocky | 20300/20300 | 50 | 204 | 720x576 | REGISTERED, rc0 |
| 3A | 8812/8812 | 133 | 300 | 704x576 | REGISTERED, rc0 |
| 3A_blocky | 18190/18190 | 73 | 300 | 704x576 | REGISTERED, rc0 |

Native decoded format YUV420P8. Every qualifying P-picture count agrees with the independent Claude rehearsal, supporting equal display-order anchor selection. All reported index hashes match the precommitted allow-list; full hashes are in status handback section 4 and interim section 14.

### 6.3 Eight descriptive diagnostic runs (P0D) complete

The existing S2-I2 numerical engine was run on each registered source via `S2_I3_P0D_diagnostics_v0_1.bat`. Each reverified actual source and index hashes, processed its entire frame count **228,228,192,192,204,204,300,300** respectively, wrote reports, explicitly printed **`no admission verdict`** and exited 0. Earlier S2-I2 BLOCKED thresholds for SP, SP_blocky and 3A concern test PRECONDITIONS, not source/index mismatch; these diagnostics are **descriptive** and do not override successful P0C.

The final completed Windows call was 3A_blocky diagnostics: **300/300, reports written, rc0**. All eight admissions and eight diagnostics are done. The COMPLETE evidence tree and CSVs have not yet been independently inspected.

### 6.4 Next: paired correspondence, global summary, evidence acceptance

Run **XP** pair only next: `S2_I3_P0D_pair_v0_1.bat XP`, then SP, LP, 3A, one checked CMD block at a time. The scripts write `results/PAIR_XP`, etc. and refuse to overwrite an existing output. Claude's independent rehearsal expected decisive counts **140/228 XP, 175/192 SP, 81/204 LP, 268/300 3A**, zero decisive violations. Owner Windows pair runs are **NOT YET EXECUTED**. The first exact command with mandatory `cd /d`, output inspection and STOP conditions is in the v0.3 status handback section 6.

After all four pair PASS, run `S2_I3_P0D_summary_v0_1.bat`; inspect the JSON summary and complete `results/` tree. Numerical `READY_FOR_P1` is not authorisation; full independent Claude evidence review + owner acceptance come first. Then, if accepted, **separate exact-seven `.idx` tracking commit** (7 A / 0 M / 0 D) and owner authorisation before any P1 kernel work. Original six Stage 1 baseline indexes are immutable.

P0 scratch root: `%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1`. It contains the existing indexes and accumulated results. Preserve in place. No filtering, no protected hold-out media, no automatic cleanup.

## 7. Stage 2 empirical knowledge: preservation bridge installed, permanent transfer pending

The owner required ChatGPT and Claude to preserve their acquired knowledge before revisiting filter approaches, specifically fearing abrupt chat failure. Following review of the rejected `Stage2_Interim_Findings_v0_1`, the owner ratified **Route A**: corrected measurement and provenance into S2-I3 Evidence and Gate Report later; confirmed mechanism evidence into existing `06_DEBLOCK_CONCEPT.md` K-03/K-07/K-08 at its next independently reviewed revision. No duplicative permanent K-items or stand-alone authority.

To avoid loss before that future work, ChatGPT drafted **one temporary `interim_` preservation document**; Claude performed **one consolidated correction/expansion pass**, then the owner committed the final document at `docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md` in `4636c33`. It records the corrected seam orientation, transform composition, coded-pair denominators, FRAME row7/8 versus FIELD controls, NONE subclassification, irrecoverable versus useful seam-local MAE, blur harm, exact P-skip method, pair correspondence mathematics, index layout and absence of numeric motion vectors, QP values, platform determination and negative experiments. The TEMPORARY document's section 9 is the detailed transfer/retirement checklist. **It does not authorise a filter or create new criteria.**

Key corrections that must survive: side-by-side neighbouring MBs share a VERTICAL seam, stacked MBs share a HORIZONTAL seam (Claude M1); coded FRAME/FIELD transition percentages exclude NONE from their coded-pair denominator, so denominator must be stated (M2); the original geometry-blind frame-row8 mask was wrong for most FIELD MBs, diluting the seam signal (M3), thus **"paired MAE is intrinsically weak" is a WITHDRAWN conclusion**; prior K-03/K-07/K-08 already contain much of the mechanism, so measured values upgrade evidence rather than invent new K-items (M4). The corrected paired luma horizontal row7/8 excess in FRAME macroblocks is XP+19.5%, SP+16.2%, LP+17.3%, 3A+12.8%; FIELD row7/8 control only +3.2/+3.3/+2.7/+2.3%; both coded states have x=8 vertical internal seams. Luma-only, no chroma proof. Many NONE cases **may**, not MUST, inherit displaced blocking; no motion-vector components in current indexes.

Important methodological facts Claude added: exact P-skip test is threshold-free; negative 3A one-line shift still matches 90.2%, proving weak thresholds are unsafe; P-skip has field-swap and IPPP limitations; pair rule uses a triangle inequality and two sample-size floors (20 frames/10%) selected after seeing the data, which MUST be disclosed; exploratory pixel-analysis scripts and raw CSVs were not retained, only enough methods to reproduce them. No `Claude_ANALYSIS_...v0_3` exists; v0.2 geometry-blind seam numbers are not authority. The interim was consolidated into one document; do not start another review cycle or revise it for ordinary P0 console progress.

**Still pending:** transfer every preservation row into owning evidence/knowledge documents, review/ratify, and retire the interim only once complete. A successful P0 diagnostics run cannot itself close these obligations.

## 8. Restricted Media, repository hygiene, Git history and risk

`NOTICE.md` governs Restricted Media. Source recordings/decoded images and pixels may be development-restricted even when temporarily tracked. Numerical index bytes, hashes and scalar reports are not pixel media simply by derivation. The six frozen Stage 1 indexes remain unmodified; future seven development indexes are separately authorised only after evidence acceptance. TEST 6A/7A remain role-unassigned despite being committed as development media; no automatic P0 admission.

**Four currently tracked identity-bearing review artefacts were discovered by Claude and remain outstanding as of the last audit:**

```text
experiments/S2-I3/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_1_FOR_CLAUDE_REVIEW.md
experiments/S2-I3/S2_I3_v0_2_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip
experiments/S2-I3/S2_I3_v0_3_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip
experiments/S2-I3/ChatGPT_Handover_v0_8_FOR_CLAUDE_REVIEW.zip
```

They contain identifying text in a superseded plaintext draft or ZIP member. One separate corrected-handover review ZIP was deleted in `3f8f45a`, but its blob remains in `6b7acc3` history. Current-tree deletion does NOT erase these from published Git history or third-party copies. Existing D-23 Development Closure history scrub includes owner-identifying historical material. Immediate history rewrite is a separate owner decision.

**Deferred cleanup, as owner requested (after tests):** Commit A exact four identity deletions (4 D only); Commit B delete the two superseded handovers v0.7/v0.9 (and handle v0.8 predecessor alongside installing this v0.9, if approved); Commit C remove unrelated review-only artefacts by an UPDATED Claude/owner-reviewed exact pathlist. The initial snapshot included 48 review artefacts and a ~54 MB repository ZIP duplicating ~49 MB restricted recordings; `4636c33` added 8 further review-only paths, which Claude has now enumerated exactly in status v0.3 section 8, giving a Commit C candidate pool of **44 + 8 = 52 paths** pending owner agreement. Claude scanned all ten text files and all 19 ZIP members added by `4636c33`: none carries identifying text, so Commit A stays at exactly four paths. The accepted implementation resides in `experiments/stage2/` alongside incidental review files: never delete that directory by wildcard.

**Critical prevention:** never routine `git add -A` over a working tree with review ZIPs/patches/superseded drafts; those are the *very files that preserve removed identifying text*. Audit ZIP members as well as loose text before commits. Use `git diff --cached --name-status --no-renames` and exact-path staging. `git diff --cached --check` is NOT a valid mandatory STOP gate in this repository due to legitimate CRLF evidence and Markdown hard breaks. `.py`/`.md` may be LF in Git blobs but CRLF in Windows worktree (`core.autocrlf=true`); name representation when hashing. Do not confuse a Git line-ending warning with loss of content. The owner has chosen tests first; avoid repeated unsolicited cleanup interruptions during pairs.

## 9. Owner interaction and handover-operating conventions

- Use clear plain English, expand abbreviations on first use when likely unfamiliar, and state STOP conditions and what success would look like.
- For Windows command blocks start with `cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"` when changing repository context. Prefer **one short, fully reviewed CMD code block per turn**, not a large combined procedure. CMD pasted characters have been dropped/concatenated in earlier interactions.
- Owner wants **complete data, varied content, clear per-source reports, negative controls, meaningful numerical evidence and visual inspection**, not hand-picked easy scenes or a single metric winner. Do not let the Q62 transcodes become the sole basis for a production filter.
- Ask the owner only decisions they actually need to make. Resolve routine code/design disputes with Claude first. The owner holds final ratification and runs Windows.
- Separate statements about *verified current commit*, *local file candidate*, *Linux rehearsal*, *owner Windows run*, and *proposed/ratified decision*. Never present one as the other.
- Stop on index hash mismatch, unexpected repo staging, missing scratch LP_blocky index, admission HARD FAIL/INCONCLUSIVE, pair mismatch, or source/provenance uncertainty.
- Refresh role handover **at every substantial milestone** before the conversation limit is reached. Avoid doc sprawl, stale summaries and knowledge accepted without cross-checking existing K/O items.

## 10. Current and superseded document/status map

| Item | Correct as-at status |
|---|---|
| Stage 1 + six accepted `.idx` | COMPLETE, PASS, frozen |
| S2-I1 and S2-I2 implementation/evidence | Accepted, committed |
| `00_PROJECT_STATUS_v0_7` | Last ratified project-status reference; its earlier "P0 not authorised" line was overtaken by a subsequent owner decision. Do not misquote the earlier document |
| `Stage2_Experiment_Design_v0_7`, S2-I3 Full-Data v0.3 | Current ratified experiment design |
| `05_DECISIONS_v1_2`, `06_DEBLOCK_CONCEPT.md` | Current design/knowledge authority, not changed by P0 |
| `interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1` | Final single-pass consolidated version committed at `4636c33`, TEMPORARY evidence bridge, not authority |
| `S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_2.md` | Committed as-of XP admission; **operationally superseded by proposed v0.3** after P0C+P0D completion |
| This ChatGPT handover v0.9 | Successor to v0.8 only when Claude-cleared/owner-approved and installed under D-23 |
| Claude role handover v0.10 | Committed and independently verified; v0.9 predecessor still awaits deletion |
| S4 P0 code and isolated-Python correction | Independently Claude-cleared, installed, Windows P0A PASS |
| P0C admissions and P0D diagnostics | 8/8 of each complete, zero reported execution errors |
| P0D pair tests/summary/evidence acceptance | NOT RUN / NOT ACCEPTED |
| Seven-index development tracking commit | Not done; after complete P0 evidence review only |
| New home 6A/7A files | Tracked in mixed snapshot, no experiment role |
| Old `Stage2_Interim_Findings_v0_1` draft | NOT accepted; do not install |
| `Claude_ANALYSIS...v0_3` | Does NOT exist; corrected measurements are in installed interim |

## 11. Successor checklist - immediate and next increments

1. Read this v0.9 handover, owner-reported checkpoint status v0.3 (when reviewed/installed), ratified Stage 2 and S2-I3 plans, `NOTICE.md`, and installed interim section 9. Verify real Git HEAD and whether any pair tests have run after 3A_blocky diagnostics.
2. If still at this stop point, execute XP pair only. Follow reviewed CMD and check `results/PAIR_XP/pair.log`; STOP on mismatch or nonzero status. Do not rerun eight successful diagnostics or tamper with scratch.
3. Run SP, LP, 3A pairs individually; then global summary; collect complete `results/` evidence and refer to Claude for one independent review. The six frozen accepted indexes and LP original remain untouched. Numerical summary READY is not P1 permission.
4. Only after owner accepts evidence and Claude reports on it: exact-hash seven non-baseline `.idx` tracking commit, then request explicit owner authorisation for P1 fixed-QP luma kernel development. No S2-I4 or S2-I8 testing by inference.
5. Preserve the single-pass consolidated `interim_` bridge until permanent Evidence/Gate Report and `06` K-03/K-07/K-08 transfer is accepted. Do not create a rival knowledge register.
6. When the owner is ready after testing, prioritise urgent identity Commit A, D-23 predecessor Commit B, and a checked exact-path clean-up Commit C. A present tree deletion never proves Git history is scrubbed. Avoid `git add -A` during routine development.
7. Treat TEST 6A/7A as committed but UNASSIGNED; any later role, fold or weights need independent characterisation, design amendment and ratification. Check media public-history consequences separately.
8. At significant gate closure, update the handover/status with installation-true statements: every status sentence should remain true at the commit where the document is installed. Do not copy stale "awaits S4 review" statements from old handovers.

## 12. Suggested first response from a successor development chat

> I have read the current ChatGPT handover and the repository authorities. As at the 2026-10-17 checkpoint, P0A passed, six indexes were generated and hash-matched, LP_blocky was copied exactly, LP original stayed frozen, all eight P0C sources REGISTERED with correct P-picture counts, and all eight P0D numerical diagnostic runs completed successfully. Pair tests and summary were still pending; the next operation was PAIR_XP. I will verify whether the owner has progressed, preserve all scratch evidence, and proceed with one reviewed CMD block rather than rerun passed steps. The four identity-bearing review paths remain a separately deferred urgent Git issue. I will not run filtering, change hold-outs, or claim P0 acceptance before Claude's complete evidence review and owner authorisation.

## 13. Change log

### v0.9 - 2026-10-17, after P0D diagnostic completion

- Replaces v0.8's early S4-pending/P0-not-started snapshot with the actual current owner Windows checkpoint: code clearance, isolated-Python fix, P0A PASS, P0B index hash match, P0C 8/8 REGISTERED and P0D diagnostics 8/8 COMPLETE.
- Records observed P-skip counts, qualifying P-picture counts and full-frame diagnostic completion; isolates pending four pair tests, summary, Claude evidence review and seven-index tracking commit.
- Records owner-reported Git HEAD `4636c33`, new snapshots and identity/review-artefact hygiene debt without inventing a completed cleanup or a full SHA not provided.
- Recognises the independently consolidated temporary knowledge document committed to `docs/REPOSITORY/` and preserves Route A transfer obligations, correction history and methodological limitations.
- Retains the project model, immutable-baseline, interlace, chroma, motion, source-pool, experimental CV, owner-process and build/CI knowledge from v0.8. Adds isolated Python and review-ZIP-history incidents.
- Corrects as-at versus current status; v0.9 is the current handover only through separate D-23 installation and deletion of its v0.8 predecessor.

### v0.8 - 2026-10-17 (previously reviewed/committed; superseded by v0.9 upon installation)

The v0.8 handover accurately represented the state at `35cd543` before Claude's S4 clearance and all owner Windows P0 execution. Its earlier next-step narrative is obsolete; Git history retains it after its current-tree predecessor deletion. v0.7 was its own earlier 2026-10-14 predecessor and should also be removed from the current tree.
