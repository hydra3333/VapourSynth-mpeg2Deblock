# ChatGPT Handover to Future ChatGPT Chat
## MPEG-2 Macroblock Index / VapourSynth Deblocking Project

**Document:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md`

**Version:** 0.8

**Date:** 2026-10-17

**Prepared by:** current ChatGPT development role from v0.7, the owner-supplied GitHub source archive, ratified repository documents, Claude reviews/rehearsals, and the current conversation

**Status:** CURRENT CHATGPT ROLE HANDOVER on installation under D-23 v1.2; a continuity record, **not** technical or design authority.

**Supersedes in the current tree:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md` (which accurately describes its 2026-10-14 as-at state but is now operationally obsolete).

**Repository baseline as at this handover:** `main` HEAD `35cd543b459a5856688f7c3795f73226e72311f8`, last independently verified by Claude on 2026-10-17. The owner-supplied GitHub ZIP was also examined by ChatGPT. **The owner's local checkout has not been rechecked after this point.**

**Operational stop point:** S2-I3 P0 implementation revised candidate **CLEARED by Claude**; further optional S4-only improvement **prepared but NOT YET sent to Claude for its promised one-file diff-check**. No owner Windows P0 run, S2-I3 overlay installation, or P0 index-tracking commit has occurred as far as reported.

---

## Reading this handover correctly

This is the current ChatGPT role's substantive continuity record, not merely a list of filenames. It is intended to let a successor recover the practical project model, decisions, code/test state, limitations and immediate tasks without reconstructing several days of conversations. Preserve negative knowledge and procedural cautions as well as positive findings. At actual takeover, **first verify the live checkout and any developments after 2026-10-17**; do not assume the as-at state is still current.

Authority hierarchy: owner-ratified `docs/REPOSITORY/` documents and `NOTICE.md` prevail over this handover. Visual Studio projects own build settings; GitHub Actions workflow and expected-switch CSV own CI/release settings. Review and handover material are provenance/continuity, not competing authorities. An owner decision communicated after an authority was committed must be labelled as a **post-commit conversational authorisation**, not misquoted as text already in Git.

**Agreed continuity-purpose text** (verbatim from `docs/HANDOVER/ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT_FOR_BOTH_ROLES.md`, also reproduced in Claude handover v0.10):

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

The previous v0.7 handover was prepared by Claude for ChatGPT after the former ChatGPT chat hit its length limit on 2026-10-14. This v0.8 is a new full replacement drafted by the current ChatGPT role; it carries forward stable knowledge while replacing the then-current S2-I1-only state.

## 0. Read this first: current state and next action

| Area | Status at 2026-10-17 |
|---|---|
| Migration/repository restart | Migration **CLOSED** 2026-10-11; fresh-history root established; active development restarted |
| Stage 1 | **COMPLETE / PASS / FROZEN**; six accepted baseline indexes immutable |
| S2-I1 | **COMPLETE / COMMITTED**, accepted code commit `4221f7f9f3c015da4ca70b4f8c0249536cd7e3b5` |
| S2-I2 | **COMPLETE / RATIFIED / COMMITTED**; code commit `190bd06ded88130ffddac7bb9adde4175d82f9f8`, evidence/docs through `6e7b5c53df1c65775524936fc945c449cc9fa100` |
| Current docs | Stage 2 Experimental Design **v0.7**, S2-I3 Full-Data Design **v0.3**, Project Status **v0.7**, all ratified 2026-10-17, installed in documentation-only commit `35cd543b...` |
| S2-I3 authority | Design ratified; **owner subsequently separately authorised S2-I3 implementation**, beginning with **P0 admission/registration only**, not a filtering or QP experiment |
| S2-I3 P0 candidate | Revised candidate with M1 + S1-S3 **CLEARED by Claude**; Linux/BestSource rehearsal all eight REGISTERED, four pairs PASS |
| S4 variant | One-file P0A adjustment to run new NumPy tests under VapourSynth's own Python; package delivered by ChatGPT **but owner explicitly had NOT passed it to Claude yet** |
| Windows P0 | **NOT STARTED**. Owner must be guided one small reviewed CMD block at a time after package choice/clearance |
| Seven development indexes | Owner approved future separate tracking commit; **not yet admitted or committed**; six need Windows generation, one is previously accepted scratch LP_blocky |
| New home sample pairs | 6A/7A (four `.mpg` files) genuinely new, **uncommitted, unassigned, outside P0 allow-list**; no role or weighting changes authorised |
| Findings/knowledge proposal | `Stage2_Interim_Findings_v0_1` **NOT CLEARED / NOT INSTALLED**; owner/AI agreed Route A: corrected evidence goes into future S2-I3 gate report, mechanism confirmations into existing K items later |
| S2-I4 and later | **NOT AUTHORISED**; S2-I4 real-QP comparisons are design only, not executable scope |

**Immediate action:** give Claude `S2_I3_P0_IMPLEMENTATION_CANDIDATE_v0_1_S4_FOR_CLAUDE_DIFF_CHECK.zip` for its narrow S4 diff review. Once cleared, guide the owner through the agreed Windows P0A/P0B/P0C/P0D sequence. The already-cleared pre-S4 revised package is a permissible fallback; S4 is a SHOULD, not a MUST. Do not let the sample-pool or findings/documentation tracks obstruct P0.

**The owner is not expected to run anything yet at this exact handover boundary.** The previous response offered the S4 package and the owner said they had not yet passed it to Claude. A future chat must check whether that subsequently happened before issuing any commands.

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

## 2. Live repository and document authorities

### 2.1 Current committed state

Active zero-parent history root:

```text
11f47427624bf5f68b3426fe9f58aa26d40e47f7
```

Root tree:

```text
45ad1f16a24d3cce0411863a9804472efa1c8529
```

Important verified post-reset progress (abbreviated):

```text
11f4742  fresh-history root after identity/media-policy reconciliation
eac5526  first handover-install commit
bfb6cc2  second handover-install commit
c45dcf0  Project Status v0.4
bfaed24  SNAPSHOT; Claude handover v0.9 installed
10956a1  SNAPSHOT2
4221f7f  S2-I1 accepted code, after owner Windows run/review
2286341  Project Status v0.5
190bd06  S2-I2 nine-file accepted implementation
6e7b5c5  S2-I2 accepted numerical evidence and status v0.6
35cd543  Stage 2 v0.7 + S2-I3 v0.3 + Project Status v0.7, docs only
```

Full current HEAD:

```text
35cd543b459a5856688f7c3795f73226e72311f8
```

The S2-I2 evidence-install commit's full SHA is `6e7b5c53df1c65775524936fc945c449cc9fa100`; the S2-I2 code commit's full SHA is `190bd06ded88130ffddac7bb9adde4175d82f9f8`. Pre-reset SHAs are external historical provenance; not reachable current history. The migration handback was retired from current-tree authority and must not be reconstructed as one. The `v0.1.0` workflow-generated release is explicitly **NOT FOR USE, SNAPSHOT RELEASE ONLY**, not a functional deblocker.

**As-at distinction:** `00_PROJECT_STATUS_v0_7.md` says S2-I3 implementation was not authorised at the time that file was ratified. The owner **subsequently authorised S2-I3 implementation/P0** in conversation. That fact is not yet a committed status-file update. Never silently rewrite the earlier document's as-at meaning or claim it contains this subsequent authorisation.

### 2.2 Actual current authority files to consult

```text
docs/REPOSITORY/00_PROJECT_STATUS_v0_7.md
docs/REPOSITORY/05_DECISIONS_v1_2.md
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md
docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md
docs/REPOSITORY/S2_I2_Evidence_and_Gate_Report_v0_1.md
docs/REPOSITORY/Stage2_Experiment_Design_v0_7.md
docs/REPOSITORY/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md
NOTICE.md
README.md
```

At the reference commit `35cd543`, the installed companion role handover was `docs/HANDOVER/Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md`. Claude **delivered v0.10 on 2026-10-17**, also as at `35cd543`, as a draft for owner review; check whether v0.10 was subsequently installed. At the same reference commit the installed ChatGPT handover was v0.7. **This v0.8 is its intended separately committed replacement.** The two handovers require separate review and reconciliation at takeover.

Decisions worth remembering: D-05 and D-21 determine knowledge ownership and evidence labels; D-09 frame-owned interlace; D-13 constrains capture of extra metadata; D-16 I/P/B breakdown; D-20 decisions authority; D-23 current versioned-file and identity/EOL conventions; D-24 index-driven architecture; D-25 4:2:0 chroma scope; D-26 primary real recorder vs secondary software-pair evidence. `06_DEBLOCK_CONCEPT` carries K-01 to K-11 and O-items: RATIFIED DOCUMENT does not mean its HYPOTHESIS/OPEN statements become FACT/DECIDED.

### 2.3 Code and build locations

```text
src/Mpeg2BlockInspector/                 frozen Stage 1 legacy-C indexer source
tools/Stage1_Inspector_Analyzer_v0_2.py   frozen Stage 1 analyzer
experiments/stage2/                     accepted S2-I1/S2-I2 scripts and P0 overlay destination
experiments/stage2/results/S2_I2_v0_1/  accepted historical LP and LP_blocky diagnostics
VHSC_samples/                           source recordings, six immutable baseline indexes, logs
vs/VapourSynth-mpeg2Deblock/            Visual Studio solution/projects
.github/workflows/                     workflow + expected switch contracts
docs/REPOSITORY/                        ratified specifications/status/evidence
docs/HANDOVER/                          role handovers
```

Use the actual `*.vcxproj`, current workflow and `expected_stage_bplus_switches.csv` for exact build flags. Windows build environment is Visual Studio 2026 developer command prompt x64; Visual Studio Code is used for source editing. VapourSynth R81 / BestSource 22.0 / NumPy 2.5.3 recorded in accepted S2-I2 evidence; interpreter `D:\TEST\Vapoursynth_x64_R81\python.exe`; `vspipe.exe` at `D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe`; ffmpeg commonly `C:\SOFTWARE\ffmpeg\ffmpeg.exe`. Check these paths at runtime, do not overwrite them speculatively.

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

The owner said the four home `.mpg` recordings MAY be committed temporarily and treated as development media. Claude warned that `git rm` later does **not** erase public history, third-party clones or caches; the owner had not selected among accepting persistence, later history rewrite, or attaching media privately instead, at this handover boundary. Avoid describing this as a final public-release/privacy disposition. A proposed **separate bounded four-file commit** is not yet reported as made. Once committed, Claude can independently regenerate indexes/characterise; no owner Windows characterisation BAT is then needed. The drafted `S2_I3_P0B_characterise_new_source_v0_1.bat` / characterisation ZIP was **STOOD DOWN**; do not install/run it. No change to `.gitattributes` is needed merely for `.mpg`/`.idx` (Claude checked Git treats tracked examples as binary).

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

## 6. P0: admitted scope, tools, gates, evidence

### 6.1 Only authorised executable checkpoint

**P0 is the admission/registration preflight, NOT a deblocking experiment and NOT authorisation to filter.** It precedes P1 kernel development. The ratified eight are all mandatory; don't quietly redefine the population when one source is difficult. P0 does not use fixed QP to reject/alter source files.

Structural checks: index header/content, `records[i].output_ordinal == i`, per-picture type against BestSource `_PictType`, native YUV420P8, geometry including 704 width, unsupported picture structure fail, per-source hash match and index-selection provenance. A P-picture reference anchor is the last **earlier I/P in display order**, even across one or more B pictures, not mechanically `n-1`.

For every eligible actual P-picture skipped macroblock, decode its true-position 16x16 luma and compare bit-exactly against the co-located 16x16 in its last usable prior I/P anchor. **Any true-position mismatch is HARD FAIL**. Distinguish SKIPPED-in-P from non-skipped INTER CBP0; NONE is not automatically a skip. Require at least 200 P-skips over 10 P pictures for evidential quality; too few or lack of necessary controls -> **INCONCLUSIVE**, not PASS. Correctness failures are not concealed by an inconclusive-quality floor.

Negative controls: precisely the 24 ratified spatial shifts (including seven old known-bad offsets), applied to both current/reference same-window coordinates only when wholly in bounds, plus temporal controls A/B/C with their own per-source executability; at least one meaningful comparison for each, and each aggregate identity rate <100% (not a 100%-identical negative control). Controls are evaluated over source-level eligible opportunities, not artificially treated as failures for excluded frames. Old S2-I2 spatial diagnostic thresholds remain **descriptive only**, not P0 admission gates.

For each original/blocky content group, P0D pair correspondence uses decoded full-plane luma, same frame count/geometry and all frames with possible offsets k=-2..+2. The clip-wide mean must have a strict minimum at k=0; on decisive frames, no nonzero offset may beat equality of the original frame; require both >=20 decisive and >=10% decisive frames, otherwise paired metrics **INCONCLUSIVE**. Static ambiguity is not itself a wrong-frame FAIL. Protected material is never passed to this procedure.

### 6.2 Implementation package state and supersession

**Current S4 package, NOT YET CLAUDE-CLEARED:**

```text
S2_I3_P0_IMPLEMENTATION_CANDIDATE_v0_1_S4_FOR_CLAUDE_DIFF_CHECK.zip
```

It contains:

```text
REPO_OVERLAY/experiments/stage2/   15 additive implementation files
REVIEW_ONLY/                       one-file S4 patch, review request,
                                   proposed owner-run sequence, SHA-256 manifest
```

Prior **CLEARED** fallback:

```text
S2_I3_P0_IMPLEMENTATION_CANDIDATE_v0_1_REVISED_FOR_CLAUDE_DIFF_CHECK.zip
```

Original non-cleared P0 candidate is superseded. The first Claude review found one Windows CMD MUST (M1) plus SHOULD S1-S3. The revised candidate fixed:

1. `S2_I3_P0D_diagnostics_v0_1.bat` illegal `)` in echo inside `if (...)`; changed to a hyphenated explanatory text, reliable fail-close.
2. Cleared `for /f` capture variables first; no reliance on `ERRORLEVEL` after `for /f`; added clear error messages for missing data/silent exits.
3. Added P-skip and pair unit tests to P0A (9+5 tests), checked prerequisites, before creating scratch campaign.

Claude independently diff-audited the **revised** candidate; verdict **CLEARED**. All Python and `.vpy` code is byte-for-byte unchanged from the fully rehearsed first candidate; exact 15 additive paths; manifest 18/18, BATs US-ASCII CRLF and Python/VPY LF, no identity text, no unintended repo write. Claude's P0 clearance/grounding record:

```text
Claude_P0_REVISED_CLEARANCE_AND_PROJECT_STATE_OF_PLAY_v0_1.md
```

**S4-only SHOULD** arose because the newly added NumPy-importing P0 unit tests would otherwise run under plain `python`, which might differ from actual VapourSynth Python. The S4 package makes **only** `S2_I3_P0A_prepare_campaign_v0_1.bat` different from the cleared revision:

```bat
set "vspython=D:\TEST\Vapoursynth_x64_R81\python.exe"
```

It existence-checks that interpreter, invokes the two S2-I3 suites using `"%vspython%"`, and prints specific failure messages; it **leaves** the numpy-free accepted reader-regression under plain `python`. The package has an exact `P0A_ONLY_S4_DIFF_AGAINST_CLEARED_REVISED.patch`. ChatGPT locally checked 9/9 P-skip and 5/5 pair unit tests after packaging, and confirmed other 14 overlay files unchanged. The owner explicitly had not yet passed this package to Claude when asking for the handover update; **do not call S4 cleared merely because the base revised candidate is cleared**. Claude promised one-file diff-only audit, not a new full Linux rehearsal.

No tool package is committed or installed as at the stated boundary. The review-only artifacts and `.patch` must **never** be copied into the repository overlay or tracked. Seven BAT/three VPY/five Python comprise 15 overlay files; see the actual ZIP manifest for exact names.

### 6.3 Claude full rehearsal results (pre-S4 logic; carried forward)

Linux, VapourSynth R81 / BestSource 22.0 / NumPy 2.5.3; exactly eight development media files from verified HEAD; no EP/2A/4A/MLS downloaded or decoded; rehearsal media and caches deleted after. All 14 supplied unit tests passed, along with independent adversarial controls. Eight source admissions:

| Source | Exact P-skips | P pictures | Highest negative-control identity |
|---|---:|---:|---:|
| XP | 1619/1619 | 54 | 83.9% (previous frame) |
| XP_blocky | 25635/25635 | 55 | 73.2% (+1,0) |
| SP | 1764/1764 | 46 | 77.7% (previous frame) |
| SP_blocky | 19010/19010 | 46 | 73.3% (0,+1) |
| LP | 1533/1533 | 46 | 94.8% (previous frame) |
| LP_blocky | 20300/20300 | 50 | 69.2% (+1,0) |
| 3A | 8812/8812 | 133 | 96.7% (previous frame) |
| 3A_blocky | 18190/18190 | 73 | 78.6% (-1,0) |

All are **REGISTERED** on Claude's Linux rehearsal; these are comparison expectations, not owner Windows acceptance. Encode/index swaps, one-frame slips, and small spatial shifts were rejected. S2-I2 diagnostic CSVs for LP and LP_blocky were byte-identical to committed Windows historical data after line-ending normalization; historical diagnostic BLOCKED for SP/SP_blocky/3A is **not** P0 admission failure.

Four pair correspondence rehearsals **PASS**, no decisive violations:

| Pair | Decisive frames | Mean MAE at k=0 | Best competing mean MAE |
|---|---:|---:|---:|
| XP | 140/228 | 3.53 | 9.88 |
| SP | 175/192 | 3.23 | 13.98 |
| LP | 81/204 | 4.39 | 9.93 |
| 3A | 268/300 | 5.53 | 19.95 |

A simulated +/-1 slip fails on all four. Final evidence summary returns `READY` with complete matching evidence and rejects missing, tampered, stale or mislabeled evidence with nonzero status. `READY` is **not** permission to start filtering.

### 6.4 Proposed guided owner Windows run: no steps have been run yet

The detailed file in the candidate is `REVIEW_ONLY/PROPOSED_OWNER_RUN_SEQUENCE_NOT_YET_CLEARED.md`. Its content is unchanged from the reviewed draft. A future ChatGPT must **not dump all commands at once**: start with one reviewed small CMD command block, ask for output, proceed only on success.

0. Verify repository HEAD/branch/working tree and inspect staged changes; do not assume clean if the owner has other files. Baseline is `35cd543...` until a new commit is independently identified.
1. Inspect candidate ZIP, its exact named overlay additions and SHA manifest. Stage outside repo first; copy only `REPO_OVERLAY/experiments/stage2/` files, never `REVIEW_ONLY/`, and only after Claude clears the chosen package.
2. Run `S2_I3_P0A_prepare_campaign_v0_1.bat` once. It runs the six-frozen-index reader regression, new 9+5 unit tests, vspipe preflight and creates new owned scratch campaign. Regression may print `EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent`; **this is expected diagnostic wording, not a P0 failure**. No hold-out media are decoded by P0A.
3. Serially run P0B for six indexes: XP, XP_blocky, SP, SP_blocky, 3A, 3A_blocky. Use exact reviewed label casing, match Linux reference hashes; use `.m2v` regular file, remove owned ES after each; never generate directly into `VHSC_samples`.
4. LP original uses its six-frozen-baseline index. LP_blocky uses previously accepted S2-I2 scratch index at `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky\LG_576i_3_LP_blocky.idx`; validate hash `b3f1...5238` then byte-copy with reviewed P0B_copy wrapper. If missing, **STOP** and consult Claude about re-running previously accepted S2-I2 preparation; do not invent bytes.
5. Serially run P0C admission for all eight and capture per-source JSON/log; STOP on HARD FAIL or INCONCLUSIVE. Confirm index hash, P-picture skip totals and negative controls.
6. Serially run P0D diagnostics on eight, explicitly labelled as **S2-I2 historical descriptive**, regardless of old BLOCKED thresholds. Check failures of diagnostic execution separately from historical negative results.
7. Run P0D pair for XP, SP, LP, 3A after both sources in each pair have admitted; STOP on FAIL/INCONCLUSIVE.
8. Run P0D summary and inspect `P0_summary.json`; READY only with complete matching evidence. Owner and Claude inspect the full evidence.
9. Only **after** P0 evidence acceptance and owner/Claude review, separately install **seven** SHA-exact index bytes into `VHSC_samples`, inspect binary Git status and commit **exact seven named `.idx` files in an index-only commit**. Six frozen Stage 1 indexes unchanged. No regeneration between admission and commit.

P0 scratch root, from reviewed P0A:

```text
%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1
```

P0A refuses existing root, deliberately preserving any previous evidence. No automatic broad recursive deletion. A Ctrl-C interrupted generation can leave restricted `.m2v`; identify and delete **exact named owned file** after review, not using an unbounded cleanup command.

## 7. Findings and knowledge-management: CLOSED FOR NOW, not repository change

Exploratory measurements by Claude on the eight development indexes and original/blocky pairs produced interesting source heterogeneity and pixel-domain confirmation of accepted K-items. However Claude's first `Claude_ANALYSIS_OF_Paired_Reference_Metric_and_Sample_Pool_Extension_v0_2.md` contained serious **known interpretation errors**, including inverted seam-direction labels, unstated coded-pair denominators, and an incorrectly located boundary mask. The resulting claims that global paired MAE was inherently a weak objective and that index-driven geometry primarily adds value at *vertical* seams were too broad/wrong. **Do not quote the v0.2 boundary figures or pessimistic metric conclusion as accepted evidence.** Claude planned a corrected v0.3 analysis; as at this handover it had not yet been supplied.

Claude independently reviewed ChatGPT's proposed `Stage2_Interim_Findings_v0_1`; **NOT CLEARED, NOT INSTALLED**, with four MUST findings. The owner/AI accepted **Route A**: do not create a redundant new knowledge authority; preserve corrected measurements and reproducibility in the later S2-I3 Evidence and Gate Report; at the next reviewed `06_DEBLOCK_CONCEPT.md` revision strengthen evidence behind existing K-03/K-07/K-08 rather than invent new K numbers. D-05 already requires durable findings in the appropriate owning documents. This track does not change S2-I3 authorisation, code or P0 gates and should not delay them.

Corrected important measurements (all luma-only, no chroma validation):

- Original transform mix FIELD / FRAME / NONE: XP 70.9/12.1/17.0%, SP 73.4/5.9/20.8%, LP 52.7/23.0/24.3%, 3A 7.6/67.9/24.5%. Opposite XP versus 3A coding regimes are strong support for diverse source development.
- Source-coded FRAME/FIELD transition across **shared VERTICAL MB boundary** (side by side): XP 15.5%, SP 8.2%, LP 23.6%, 3A 9.2% of both-coded adjacent pairs. Across **shared HORIZONTAL boundary** (stacked): XP 15.7%, SP 8.5%, LP 24.0%, 3A 10.0% of both-coded pairs. Including NONE in denominator (all pairs) lowers these to vertical 11.3/5.6/15.0/6.4% and horizontal 11.4/5.8/15.3/6.9%, respectively. A 'vertical seam' label is dangerous unless it specifies seam orientation rather than scanning direction.
- Paired luma error (`|original - blocky|`) split by the BLOCKY clip's own MB transform geometry, compared **within transform state** against that state's interior, shows HORIZONTAL internal frame-row-8 band excess: FRAME XP+19.5%, SP+16.2%, LP+17.3%, 3A+12.8%; FIELD at same rows XP+3.2%, SP+3.3%, LP+2.7%, 3A+2.3%. VERTICAL internal x=8 band excess in FRAME/FIELD: XP+23.4/+24.2%, SP+20.5/+25.5%, LP+22.6/+23.4%, 3A+16.5/+19.1%. Do **not** compare absolute MAE across FRAME/FIELD (different activity distributions). This confirms K-03 and x=8 in decoded pixels. Geometry-aware seam-local reference error has usable signal; geometry-blind full-frame MAE remains diluted by broader quantisation damage. Old 7-10% blanket boundary interpretation was incorrectly measured.
- Most NONE MBs are **not** zero-MV P skips. Among NONE, guaranteed co-located P-skips are 1.9-9.4% across eight sources; the remainder **may** be off-grid predicted content, **not proof that all are off-grid**. K-08 is strengthened quantitatively, without implying immediate `.idx2`. Numeric subclass proportions and reproduction steps are in `Claude_REVIEW_OF_ChatGPT_Stage2_Interim_Findings_v0_1_v0_1.md` and should be carried into the later report.
- Crude global geometry-blind vertical blurring damaged even cleaner originals by up to 2.244 luma MAE. FRAME/FIELD DCT mode is not permission to average temporally distinct fields. Predictions to test in kernel work: index-based geometry adds the most **at horizontal seams (fixed y)**; vertical x=8 seam position is shared by FRAME/FIELD. Measure arms independently and preserve do-no-harm.
- Early global vertical blockiness index used one field-grid pitch for every MB, invalid for FRAME MBs; these published vertical values are **not cross-source-comparable**. D-26 already settles paired reference status, and 4:2:0 chroma is not addressed.

The reusable corrected provenance is `Claude_REVIEW_OF_ChatGPT_Stage2_Interim_Findings_v0_1_v0_1.md` (currently review correspondence, **not installed technical authority**). Do not add it to the repo as an authoritative standalone finding note, nor let these exploratory findings silently replace the ratified metrics or rubric.

## 8. Restricted Media and Git hygiene

`NOTICE.md` governs. In development, expressly designated Source Recordings under `VHSC_samples` are Restricted Media, as are decoded audio/video, crops/stills, images, difference visualisations, quantiser heatmaps, seam visualisations, etc. **A numerical `.idx` file, numerical results, source code, plain logs and hashes are not Restricted Media merely by derivation** unless they embed actual Restricted Media. A picture-like spatial text grid is treated as Derived Media rather than ordinary numerical text.

Development exception for necessary project usage with ChatGPT and Claude is narrow; it does not erase general restrictions, authorise unrelated services/uses, or automatically authorise publication. The current repo has original development recordings. At **Development Closure**, owner must remove Restricted Media from current tree/assets and perform the separately planned history purge/reset; the earlier October 13 history reset was *not* Development Closure. Even a later Git rewrite cannot reach third-party clones, forks or caches, which is why the new home-media commit question should be explicitly settled before publicly pushing the files.

Git discipline: `git status --short`, `git diff --cached --name-status`, exact named staging, inspect modified/added/deleted files, preserve D-23 predecessor removal when a document is updated. **Do NOT use `git diff --cached --check` as a STOP gate**: legitimate CRLF evidence in `experiments/stage2/results/` and Markdown two-space hard breaks can make it fail on a correct commit; this trap was established in S2-I2 Step B. `git add -A` is **not** a safe routine default. Respect `.gitattributes` CRLF for BATs and project files; don't globally normalise Markdown. Keep review ZIPs/patches out of repository unless independently instructed otherwise. Current `main` code identity remains `35cd543...` until actually committed and independently verified.

## 9. Owner interaction and handover-operating conventions

- Use clear plain English, expand abbreviations on first use when likely unfamiliar, and state STOP conditions and what success would look like.
- For Windows command blocks start with `cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"` when changing repository context. Prefer **one short, fully reviewed CMD code block per turn**, not a large combined procedure. CMD pasted characters have been dropped/concatenated in earlier interactions.
- Owner wants **complete data, varied content, clear per-source reports, negative controls, meaningful numerical evidence and visual inspection**, not hand-picked easy scenes or a single metric winner. Do not let the Q62 transcodes become the sole basis for a production filter.
- Ask the owner only decisions they actually need to make. Resolve routine code/design disputes with Claude first. The owner holds final ratification and runs Windows.
- Separate statements about *verified current commit*, *local file candidate*, *Linux rehearsal*, *owner Windows run*, and *proposed/ratified decision*. Never present one as the other.
- Stop on index hash mismatch, unexpected repo staging, missing scratch LP_blocky index, admission HARD FAIL/INCONCLUSIVE, pair mismatch, or source/provenance uncertainty.
- Refresh role handover **at every substantial milestone** before the conversation limit is reached. Avoid doc sprawl, stale summaries and knowledge accepted without cross-checking existing K/O items.

## 10. Known version/supersession map at as-at point

| Item | Correct status |
|---|---|
| Ratified repository `00_PROJECT_STATUS_v0_7` | Current, but its earlier 'S2-I3 not authorised' as-at was superseded by later conversational owner P0 authorisation |
| Ratified `Stage2_Experiment_Design_v0_7` | Current; v0.6 superseded |
| Ratified `S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3` | Current; earlier v0.1/v0.2 drafts superseded |
| Current `05_DECISIONS_v1_2`, `06_DEBLOCK_CONCEPT.md` v1.2 | Current authority; unchanged during 17 Oct review churn |
| `Claude_REVIEW_OF_ChatGPT_S2_I3_P0_Candidate_v0_1_v0_1` | Original real findings remain valid; original **NOT CLEARED** verdict superseded |
| `Claude_P0_REVISED_CLEARANCE_AND_PROJECT_STATE_OF_PLAY_v0_1` | Latest Claude **CLEARED** verdict for P0 pre-S4 revised candidate |
| Original P0 v0.1 implementation candidate | Superseded by REVISED package |
| P0 v0.1 REVISED candidate | **CLEARED** and usable if S4 skipped |
| P0 v0.1 S4 candidate | **Awaiting Claude one-file diff review**, not yet covered by that clearance |
| `Stage2_Interim_Findings_v0_1` | NOT CLEARED, NOT INSTALLED; Route A chosen instead |
| `Claude_ANALYSIS_OF_Paired_Reference_...v0_2` | Contains known M1-M3 technical errors; corrected v0.3 expected, **not yet supplied** |
| New home-source characterization BAT | STOOD DOWN, never install/run |
| Seven Stage 2 development `.idx` files | Approved for later tracking only; **not** part of six frozen baseline set |
| Claude role handover | v0.9 at reference HEAD `35cd543`; **v0.10 delivered 2026-10-17 as owner-review draft** at the same baseline; check whether separately installed |
| This ChatGPT v0.8 handover | Current successor continuity handover **on its D-23 installation**; replaces v0.7 in the current tree, subject to verifying actual commit at takeover |

## 11. Successor handover checklist and likely following increments

At real takeover:

1. Verify the exact current repository HEAD, branch, staged/unstaged state and current authority filenames; obtain current source ZIP where needed. Do not infer commit from the filename of an upload.
2. Read current `00_PROJECT_STATUS` plus decisions/concept/Stage 2 v0.7/S2-I3 v0.3 and `NOTICE.md`; reconcile any changes after this v0.8 as-at date. Read latest Claude handover/reviews.
3. Determine whether S4 has been independently cleared and whether owner has already run/installed any P0 files. If not cleared, submit S4 for Claude narrow diff or explicitly use pre-S4 CLEARED candidate.
4. Guide owner through P0 steps with exact hash/read-only checks and STOP conditions. Collect per-source JSON and logs; request Claude review of evidence.
5. After all eight admissions/four pairs and the summary are reviewed, prepare separate seven-index installation/check/commit; preserve exact bytes and Stage 1 frozen set.
6. Only after P0 acceptance and owner approval, proceed to P1 fixed-QP luma kernel procedure development under the authorised S2-I3 design. Do **not** authorise yourself to run S2-I4 or unlock S2-I8 hold-outs.
7. Separately handle 6A/7A public media-history choice, independent source characterisation, role/weighting proposal, and any formal Stage 2 v0.8 / S2-I3 v0.4 ratification; do not add them to current P0 by convenience.
8. When S2-I3 evidence/gate reporting is due, incorporate the **corrected** Oct 17 source/pixel-domain findings with provenance; then propose appropriately constrained evidence upgrades to existing K-03/K-07/K-08 in `06_DEBLOCK_CONCEPT` at its next reviewed revision.
9. Update the handover and project status whenever a reviewed milestone actually changes what is true; do not proactively install interim exploratory findings documents.

## 12. Sample first message for a successor chat

> I have read the ChatGPT role handover v0.8 and the currently ratified repository authorities. The recorded baseline is Git HEAD `35cd543b...`; S2-I1/I2 are closed and Stage 1 frozen. S2-I3 P0's revised implementation is Claude-cleared, with an S4-only candidate pending Claude's one-file diff review as of the handover. I will first verify subsequent Git/review/run developments, then guide the next approved Windows P0 step. I will not alter the protected hold-outs, track exploratory findings as independent authority, or start filtering before the P0 gate and owner direction.

## 13. Change log

### v0.8 - 2026-10-17 (install-copy wording)

- Full continuity refresh from obsolete S2-I1-only v0.7 to verified S2-I2 closure and ratified S2-I3 design at commit `35cd543...`.
- Records the subsequent owner implementation authorisation and exact **P0 only** first executable checkpoint.
- Tracks original P0, revised Claude-cleared P0, and pending S4 one-file variant without conflating their clearances.
- Preserves all eight Linux BestSource admission, negative-control and pair results and Windows guided order, seven SHA-exact new index identities and baseline distinction.
- Adds current four-group S2-I3 full-data/CV methodology, fixed-QP scope, future S2-I4 two-estimand separation, and locked hold-outs.
- Records duplicate-sample resolution, new 6A/7A source uncertainty and unmade Git-history/public-exposure decision; stands down unnecessary characterisation BAT.
- Rejects uninstalled interim findings authority and preserves the **corrected** FRAME/FIELD seam orientation and pixel-error interpretation for future evidence-report treatment.
- Retains stable old handover technical, restricted-media, role, CMD, Git and build/CI lessons while explicitly pointing to owning authorities for complete normative wording. Restores the common handover-purpose text and the durable six-index regression, test-overwrite, Git EOL/hash, AVX2 and Release rules.
- Incorporates Claude continuity review v0.1: removes location identity from the date, repairs V1-V4 links, uses install-true status wording, corrects filename and companion handover references, and records the staged-diff caveat.

### v0.7 - 2026-10-14 (superseded committed handover)

Prepared by Claude from accepted v0.6 and the prior ChatGPT handoff. Its S2-I1 restart perspective was accurate as at 2026-10-14 but has now been superseded operationally by S2-I1/S2-I2 closure and the Stage 2 v0.7/S2-I3 v0.3 ratifications. v0.8 replaces v0.7 in the current tree only through its separately approved installation commit.
