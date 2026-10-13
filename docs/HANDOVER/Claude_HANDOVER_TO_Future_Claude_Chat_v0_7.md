# Claude Handover to a Future Claude Chat - MPEG-2 Index-Driven Deblocker

**Filename:** `Claude_HANDOVER_TO_Future_Claude_Chat_v0_7.md`
**Version:** 0.7 (supersedes v0.6)
**Date:** 2026-10-12 , as at repository commit `317d3f1`
(`317d3f1dad3dfa2988deb8f58abf84d59aa5878e`, verified from the GitHub source ZIP comment)
**Companion:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_5.md` (same as-at point)
**From:** the original Claude technical-development chat (reviewer/researcher role)
**To:** the follow-on Claude chat taking over the same role
**Status:** Role handover, not project authority. Where this document and a named authority file
differ, the authority file wins, and the difference should be raised with the project owner.

---

## 0. How to use this document

**Purpose (the project owner, 2026-10-12).** This is the current chat's communication to its successor. It is
meant to give a strong working understanding of the project *as at the date and commit above*, so
the successor can continue without rediscovering decisions, conventions and history. It
deliberately includes material that is not repository authority: conversational rulings, working
conventions, review habits, lessons and traps.

The project owner's own statement of the purpose (2026-10-12, verbatim, keep it in every future version):

> the handover doc is to be a communication between this chat and a the follow-on chat when this
> one is nearing its limits. as such it is intended to be a highly informative document (perhaps
> referencing other documents like the repository and decisions which may not be formally
> documented) ensuring all the evolved current rules and approaches and status and outstanding and
> upcoming items etc "as at this point in time" are clear for the follow on chat enabling it to
> pickup development where you leave off without any hiccup apart from determining any gaps between
> that "as at" and the point in time of the handover occurring - hence it should contain as much
> useful information as is reasonable to well achieve the purpose of the document.

Repository authorities still prevail on conflict; the handover references them rather than
replacing them, but must not be so skeletal that the successor has to reconstruct the project.

**Common continuity-purpose text (agreed for both role handovers, 2026-10-12, verbatim; keep it in
every future version of both):**

> The role handover is fundamentally a communication from the current development chat to its
> eventual successor when the current chat approaches its conversation limit.
>
> Its purpose is continuity. It should be a reasonably comprehensive "state of the project as
> understood by this chat, as at this point in time" document, not merely a short index into
> repository authority.
>
> It should preserve whatever a successor would materially benefit from knowing, including current
> status, roles/process, ratified rules, important the project owner conversational decisions, evolved
> conventions, technical understanding, settled/provisional/open/superseded matters, negative
> decisions, sample roles/evidence limitations, immutable baselines, build/test/plugin state,
> outstanding work/gaps, next and upcoming work, blockers/authorisation gates, known
> traps/caveats/lessons, and references to owning authority/evidence documents.
>
> Authority documents still prevail on conflict and the handover does not replace them. However,
> references must not make the handover so skeletal that the successor has to reconstruct the
> current working model from scratch.
>
> At takeover:
> 1. read the handover;
> 2. establish live repository/document state;
> 3. read owning authorities needed for the task;
> 4. determine the delta between the handover's stated as-at point and takeover;
> 5. reconcile only that delta;
> 6. continue development.
>
> Refresh the handover periodically as major state changes, not only at final conversation
> exhaustion.

**Takeover model (this role's working form of the six steps above).**

1. Read this whole document. It is long on purpose.
2. Ask the project owner for the **GitHub source ZIP of the current `main` commit** and the latest ChatGPT role
   handover. A GitHub source ZIP records its commit SHA in the archive comment (`unzip -z`).
3. Read the named authorities where exact wording matters (section 6).
4. Determine only the **delta** between this document's as-at point (`317d3f1`) and the actual
   state: `git log` messages from the project owner, the source ZIP, and anything the project owner reports.
5. State to the project owner which authority versions you are working from and ask him to confirm.
6. Pick up the pending task (section 13).

**Evidence marks used here.** "(verified)" = this chat checked it against files or source.
"(reported by the project owner)" = relayed by the project owner, not checked by this chat. Unmarked = settled project record.

---

## 1. The project

The project owner (developer; sole committer) is building an **MPEG-2-specific,
index-driven deblocking filter for VapourSynth (API4, C++, AVX2)** for his own LG DVD-recorder
captures of VHS-C home video (MPEG-2 4:2:0, mostly interlaced PAL 720x576, top-field-first).

The idea: MPEG-2 decoders discard per-macroblock coding information. **Mpeg2BlockInspector** (the
MSSG MPEG-2 reference decoder plus minimal instrumentation) parses the elementary stream and writes a
per-frame, per-macroblock binary index. The future deblocker reads decoded frames from BestSource
plus that index, so it knows authoritatively, per macroblock, the effective quantiser and the luma
transform organisation (FRAME/FIELD/NONE), instead of guessing codec structure from pixels.

This is a **new project**. It is NOT Deblock4 (abandoned by the project owner 2026-08-26; never propose resuming
it; it may be consulted only as historical reference). CNR3 (`hydra3333/vapoursynth-cnr3`) is
The project owner's other VapourSynth plugin; it served as a build-settings reference during migration only.

### 1.1 Stage plan (proposal v0.5, D-01)

Stage 0 concept and research -> Stage 1 evidence tooling (inspector + index + analyzer) -> **Stage 2
Python experimental prototype** -> **feasibility gate** (the project owner decides; a negative result is an
acceptable outcome) -> Stage 3 freeze the production index (`.idx2`) -> Stage 4 inspector as minimal
diff (largely done) -> Stage 5 frame-identity proof -> Stage 6 C++ scalar validated against the
Python oracle -> Stage 7 API4 wrapper -> Stage 8 AVX2 (scalar kept as reference) -> Stage 9
distribution (wheel/PyPI later; proposed name `vapoursynth-mpeg2deblock`).

### 1.2 Where things stand (summary)

- Stage 0: done (prior art, codec mechanics, concept `06`).
- Stage 1: **PASSED and frozen** (gate report v0.3).
- Repository and build migration: **CLOSED 2026-10-11**.
- Post-migration documentation and housekeeping: closed (section 4).
- Stage 2: design **v0.5 RATIFIED 2026-10-12**; **no code written; technical restart NOT authorised**.
- Next: knowledge-base reconciliation gate, then the project owner's restart decision, then S2-I1.

---

## 2. Who does what, and how

| Party | Role |
|---|---|
| **the project owner** | Owner, final authority; ratifies everything; runs all builds and tests on Windows; commits and pushes |
| **ChatGPT** (separate chat) | Drafter: designs, repository and authority drafts, code, procedures, reconciliations |
| **Claude** (this role) | Independent reviewer and researcher: cold reviews against source and evidence, reference-decoder verification, research, mechanical checks on every package, small helper scripts when asked |

- Workflow: **ChatGPT drafts -> Claude reviews -> the project owner ratifies -> the project owner applies**. Neither chat can
  talk to the other; the project owner relays everything. Reviews come back to the other chat as files or pastes.
- Claude writes no production code unless the project owner explicitly asks.
- the project owner's memory profile uses role handles: W3X = the project owner (coordinator/committer), W3D =
  designer/reviewer, W3C = coder. In this project ChatGPT drafts and codes; Claude reviews.

### 2.1 the project owner's working style (follow it)

- Values independent, honest assessment over agreement; disagree with evidence when warranted.
- Distrusts assertion: verify against source with file:line, recompute hashes, diff files.
- Strong aversion to summaries displacing the authorities they summarise.
- **Every document Claude emits: US-ASCII, CRLF, mechanically verified after each write** (script:
  all bytes < 128, zero bare LF; report the counts). Check incoming packages the same way.
- Naming: `Claude_TOPIC_vX_Y.md`; reviews `Claude_REVIEW_OF_ChatGPT_TOPIC_vX_Y.md` (the trailing
  version is the review's own version; an embedded version is the reviewed document's). Small
  same-day amendments to an unratified Claude document may keep the filename with an internal
  version bump and change-log line (the project owner has accepted this).
- **A ratified repository file is never edited in place**; a revision is a new version, old copy to
  `docs/REPOSITORY/superseded/`, status line flipped to RATIFIED with date.
- Labels: DECIDED / PROPOSED / AGREED / HYPOTHESIS / RESEARCHED / VERIFIED / OPEN. VERIFIED means
  the project owner's test or a cold read of authoritative source; never promote an inference.
- Review findings: **MUST / SHOULD / OPTIONAL / NO OBJECTION**, each with evidence.
- Decisions for the project owner in plain English: question / why it matters / recommendation / options.
- Hard abort over silent continuation in code. Pause at review points until the project owner's explicit go.
- **Git staging (the project owner, 2026-10-11):** controlled or scoped commits use named staging; the project owner may use
  `git add -A` for deliberate snapshot commits after inspecting state (e.g. `317d3f1 snapshot`).
- **End any review that needs relaying to ChatGPT with a short paste-ready block** (the project owner's stated
  preference; he relies on these).
- Chat replies concise; substance in the file; give the file with a one-line caption.
- **Commands for the project owner's Windows CMD** (from the ChatGPT handover v0.5 section 14.1; pasting is
  unreliable and has dropped first characters or joined lines): start with
  `cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"`; keep
  commands short; **one command per code block**; avoid long PowerShell one-liners; for several
  controlled operations prefer a reviewed `.bat`.
- **Packaging:** the project owner prefers multi-document review/application sets as ZIPs (this chat has also
  supplied SHA-256 manifests with them).
- **Direct ratification:** the project owner may close a review cycle and ratify a bounded change himself (he did
  so for the Restricted Media policy and Stage 2 v0.5 on 2026-10-12). Respect the actual decision
  history; do not insist on another review round.
- the project owner has a large token budget but chats hit length limits; this handover exists for that reason.

### 2.2 How this chat reviews (method that has caught real errors)

- Unzip each package into a fresh scratch directory; run Python with `-I`.
- Check every file: ASCII, CRLF, manifest SHA-256 values.
- **Diff candidates against the current repository copy** (from the latest source ZIP) and against
  the previous draft; review only what changed unless asked for a full read.
- Check that a candidate file matches its own supplied diff (one draft silently stripped trailing
  spaces on 16 unrelated lines).
- Recompute hashes of frozen files and reference indexes from each new source ZIP.
- When something is reported "done", confirm it in the source ZIP (twice, on 2026-10-11, ratified
  items reported complete were still pending).
- Fetch upstream when provenance is claimed (e.g. VapourSynth headers compared against GitHub tags).
- Check arithmetic (index sizes, totals, pair counts).

---

## 3. Key decisions and rulings (authoritative text is in the files)

### 3.1 Technical decisions (`05_DECISIONS.md` v1.1, D-01..D-26)

- D-01 order of work; D-03 Python reference prototype first; D-09 frame-owned processing with
  field-parity-aware sample access (no separate-field deblocking pass); D-12 Family C optional; D-14
  prediction diagnostic only; D-16 report I/P/B separately; D-20 decision authority; D-23 drafting
  workflow (clarified: ChatGPT drafts, Claude reviews).
- **D-24 index-driven product (DECIDED):** the production deblocker requires its matching index and
  takes luma seam geometry from it. No pixel seam-position detector, no pixel-only "Family B"
  deblocker. Pixels still judge blocking versus real edges and limit correction. A scope decision,
  not an experimental finding. Supersedes D-11, D-17, D-18; amends D-15 and D-08.
- **D-25 chroma in scope** on mechanism; same-field chroma filtering stays an experimental choice.
- **D-26 evidence hierarchy:** real LG recordings primary; `_blocky` software transcodes secondary
  (paired-reference numerics only).
- `05` D-09 still says same-field access is used where "geometry requires"; deliberately left as
  ratified history (`06` states it precisely). Not a required correction.

### 3.2 Conversational rulings by the project owner (some recorded only in reviews and handovers)

- No existing-filter yardstick in Stage 2 (2026-10-08).
- LG recorder quality order, best to worst: **XP -> SP -> LP -> EP -> MLS** (sample files
  `LG_576i_1_XP` .. `LG_576i_5_MLS`). Quality order is **not** the Stage 2 role order.
- XP, SP, `TEST_3A_A002` and their `_blocky` copies: **present but unassigned**; infer nothing about
  their format until indexed; assigning a role needs a Stage 2 design decision.
- Python and native helpers must be **64-bit** (binding, from the migration).
- Derived-media policy and Restricted Media terms (section 8), including option (a).
- **Authorisation (2026-10-12, verbatim):** "i authorize chatgpt and claude AI to access and use the
  images, videos and audios for the purpose of this project and only for the duration of development
  of this project until development closure as stated by me." So the project owner may share recordings and
  derived media with the two project chats until he declares development closed. Where this is
  recorded in the authorities is open (section 12).
- End-of-development **Git-history purge** planned, as its own future plan/review/ratification.
- Deleting `docs/HANDOVER/migration/` was deliberate; that initiative is closed.
- `VSVulkan4.h` stays as is (post-R81 snapshot).
- Pause discipline: one Stage 2 increment at a time, each reviewed before the next.

---

## 4. Repository and build state (migration handback is the authority)

### 4.1 Layout at `317d3f1`

```text
README.md  LICENSE (AGPL-3.0-or-later)  NOTICE.md  .gitattributes  .gitignore
.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml
.github/workflows/expected_stage_bplus_switches.csv   (256 rows; current)
.github/workflows/expected_a3_v0_10_switches.csv      (historical; kept deliberately)
src/Mpeg2BlockInspector/   16 .c + 4 .h, FROZEN
src/mpeg2Deblock/          plugin.cpp, plugin_version.h, mpeg2Deblock.rc (Identity scaffold)
tools/Stage1_Inspector_Analyzer_v0_2.py   FROZEN
TESTING/                   7 .BAT + 7 .vpy (absolute paths to the active root)
VHSC_samples/              16 .mpg recordings, 6 reference .idx, 8 .log (logs kept temporarily)
third_party/vapoursynth/include/  VapourSynth4.h VSHelper4.h VSScript4.h VSConstants4.h (R81),
                                  VSVulkan4.h (post-R81 master), VERSION.txt
vs/VapourSynth-mpeg2Deblock/  VapourSynth-mpeg2Deblock.slnx, two .vcxproj, two .filters
docs/REPOSITORY/           authorities + 00_PROJECT_STATUS.md; superseded/
docs/HANDOVER/             role handovers; migration handback ZIP (unextracted)
docs/                      historical research, reviews, proposals (provenance only)
experiments/stage2/        NOT yet created; S2 code goes here when authorised
```

### 4.2 Commit milestones

| Commit | Content |
|---|---|
| `f6ea380` | `v0.1.0` pre-release tag (Identity scaffold; four-file ZIP: EXE, DLL, LICENSE, NOTICE.md) |
| `674a374` | migration handovers recorded (audited by migration Claude) |
| `5141a23` | migration handback ZIP added; **final migration commit** (verified) |
| `a0e7100` | `.gitattributes` CRLF pins for VS project files and `*.bat`/`*.BAT` (verified via `e7f63d0` ZIP) |
| `e7f63d0` | housekeeping: patches ZIP, four `StageA_A3_Release_*.txt` and `docs/HANDOVER/migration/` removed (verified) |
| `5010b79` | "Ratify deblock concept v1.2, Stage 2 v0.4, and project status" (from ChatGPT handover v0.5; content verified at `317d3f1`) |
| `2e4eab1` | `VERSION.txt` corrected to R81 (content verified at `317d3f1`) |
| `317d3f1` | snapshot: Restricted Media policy, Stage 2 v0.5, status v0.2; HEAD at handover (verified from source ZIP `main_3`) |

Verified at `317d3f1` (source ZIP, 2026-10-12): `06` v1.2, Stage 2 v0.5 and `00_PROJECT_STATUS` v0.2
are current with v1.1, v0.3, v0.4 and status v0.1 in `superseded/`; `NOTICE.md`/`README.md` carry the
Restricted Media policy; `VERSION.txt` says R81 for four headers and post-R81 for `VSVulkan4.h`. The
applied `NOTICE.md` is a later ChatGPT revision than the v2 draft this chat reviewed (it adds
Permitted Project Purposes, option (a) and the embedded-document rule); the project owner ratified it directly,
so this chat has not given it a full cold read; do so in the reconciliation gate.
`docs/HANDOVER/` at `317d3f1` holds role handovers up to ChatGPT v0.4 and Claude v0.4 only; the
v0.5 ChatGPT and v0.7 Claude handovers still need committing.

### 4.3 Build facts (handback v0.20 sections 4-9)

- Two x64-only projects in one `.slnx`: `Mpeg2BlockInspector.exe` (legacy C, `/TC`, console, SDL
  off, `_CRT_SECURE_NO_WARNINGS`) and `mpeg2Deblock.dll` (C++20, `/permissive-`, SDL on). Debug
  `/MDd`, Release `/MT` (no VC++ redistributable). Both `/arch:AVX2`, `/favor:blend`, `/fp:precise`
  with no `/fp:contract`, `/GS`, CFG, CET, `/guard:ehcont`, ASLR/HEVA, LAA; Spectre mitigation
  deliberately off. Release PDBs with `/PDBALTPATH:%_PDB%`. Release imports KERNEL32 only.
- Toolset `$(DefaultPlatformToolset)` with a guard target rejecting anything below v145. Windows SDK
  unpinned but recorded (local 10.0.28000.0, CI 10.0.26100.0; binaries differ; no identity claim).
- Builds: VS2026 GUI, or proven plain-CMD `vswhere` + amd64 MSBuild (handback 5.2). 17 known
  inspector warnings per configuration (C4013 on `read/open/write/close/exit`, all int-returning, no
  x64 truncation risk; C4996; C4101) (verified); DLL zero warnings.
- Plugin: exports only `VapourSynthPluginInit2`; namespace `mpeg2deblock`, id
  `com.hydra3333.mpeg2deblock`; `Identity` function only; version 0.1.0.0 from `plugin_version.h`.
  `/MT` boundary rule: no CRT-owned object crosses the DLL boundary.
- CI: one workflow, manual (any branch, artifacts only) or on published Release (tag commit must be
  in `main` history; attaches one verified four-file ZIP). 256 switch tokens and 8 HostX64 groups
  checked; CI never injects flags. Expected-switch CSV changes only by reviewed commit.
- **Change control (handback 6):** inspector project-file change or exact MSVC toolset/compiler
  change => all **six local index regressions** (never in CI); `.filters`-only exempt;
  infrastructure-only => one LP smoke run; SDK-only => record only; documentation-only => nothing.
  A routine Visual Studio update that changes the compiler version triggers the six-index gate.
- Releases: bump `plugin_version.h` first; tag a `main` commit containing the current workflow;
  publish (pre-release where appropriate); the workflow attaches the ZIP; no manual uploads.
- Both binaries require an AVX2 CPU; no runtime CPU detection (the project owner-O5). Any later "scalar" code is a
  reference path inside the AVX2 binary, not a fallback.
- Vocabulary trap: DR-O7/DR-O8 (Design Record items) are not the project owner-O1..O7 (ratified decisions).

### 4.4 Line endings and hashes

- `.gitattributes`: `getpic.c`, `mpeg2dec.c` `eol=lf`; analyzer `eol=crlf`; the five VS files and
  `*.bat`/`*.BAT` `eol=crlf`. Everything else follows the checkout setting.
- Accepted CRLF hashes of the five build-contract files (handback section 3): inspector `.vcxproj`
  `c95ebed0...ce8a`, its `.filters` `a5a794a3...c85269`, `mpeg2Deblock.vcxproj` `ca1d04ca...3467`,
  its `.filters` `5840b9fd...0e99e16`, `.slnx` `852cc033...c7d525`.
- **Source ZIPs made after `a0e7100` carry those five files as CRLF with matching raw hashes**
  (verified at `e7f63d0`). Older ZIPs hold them LF; compare CRLF-normalised.
- GitHub archives apply `eol` attributes (empirically observed; the analyzer was already CRLF).
- Markdown is not pinned in `.gitattributes`, so it is stored in Git with LF and **GitHub source ZIPs
  show every `.md` as LF** (at `317d3f1`: `NOTICE.md`, `README.md` and all `docs/REPOSITORY/*.md`
  are ASCII, 0 CRLF). This is expected and also true of older ZIPs; the project owner's Windows checkout gives
  CRLF. The ASCII/CRLF rule applies to documents as delivered; check CRLF on delivered files, not on
  ZIP extracts. Whether to pin `*.md eol=crlf` is a possible gate item, not a defect.

---

## 5. Stage 1 (frozen) - what the successor needs

### 5.1 The tool and harness

- Command (TESTING `.BAT` files): `ffmpeg -v error -i <clip.mpg> -c:v copy -an -f mpeg2video - |
  Mpeg2BlockInspector.exe -b - -m <out.idx>`, then `python tools\Stage1_Inspector_Analyzer_v0_2.py
  summary <idx>`, then `vspipe --info` with `show_source_clip_info*.vpy` (written by Claude) comparing
  index picture types with BestSource `_PictType` per frame (`--arg "src=..." --arg "idx=..."`;
  `SHOW_FIRST`, `MAX_DIFFS_SHOWN`). Paths: ffmpeg `C:\SOFTWARE\ffmpeg\ffmpeg.exe`, vspipe
  `D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe`.
- The index is written under a temporary name and renamed on success; exit 0 success, 1 failure.
  Debug output goes to stderr only. No CSV output (the project owner rejected CSV; the index is binary,
  memory-mappable, in display order).
- **The LP `.BAT` deletes and recreates the tracked LP `.idx` and `.log`.** For a smoke test, write
  to a scratch path and compare with `fc /b` and SHA-256.

### 5.2 Temporary Stage 1 index format (authority: Stage 1 design v0.3 and `02` v0.4)

- 32-byte file header: magic `S1MBIDX1`, `struct.unpack("<8sHHIQII")`, endian marker 0x01020304,
  complete flag bit 0.
- Per output frame: 64-byte record header (magic `FRM1`, size, ordinal, picture type at byte 30,
  MB count as uint32 at offset 40) then 8 bytes per macroblock.
- File size = 32 + N x (64 + MBs x 8). Records are in **display order**, one per output frame.
- Per macroblock: transform state FRAME/FIELD/NONE, effective QP (derived scale; values match the
  non-linear table; linear values 26/30 seen only in the one `q_scale_type = 0` frame), plus other
  Stage 1 fields (CBP, prediction type) available but not consumed by the first filter.
- K-07: FRAME/FIELD/NONE = coded residual transform geometry. NONE covers skipped macroblocks and
  non-intra macroblocks with effective CBP 0 (a `dct_type` bit may have been read). Field pictures:
  the inspector refuses to publish (fail-safe).

### 5.3 Frozen identities and baselines (verified at `5141a23`, `e7f63d0` and `317d3f1`)

- `getpic.c` `e80239cf...0eca`; `mpeg2dec.c` `8e6053cc...0b947`; analyzer `8e0d5830...e02cda`.
- Six **immutable** reference indexes (never regenerate to make a test pass):
  `TEST_2A_A001.idx` AFE51F25..., `TEST_2A_A001_blocky.idx` CBF6E872..., `TEST_4A_A003.idx`
  5B989CED..., `LG_576i_3_LP.idx` 849b6a9c...0d011, `LG_576i_4_EP.idx` 11B42AAD...,
  `LG_576i_5_MLS.idx` 378980EA... (full values in handback section 6).
- The inspector is now built with Stage B+ settings (AVX2, `/O2 /GL`, `/MT`); all six indexes
  stayed byte-identical (Stage B+ local gate), so Stage 1 evidence holds.

### 5.4 Reference-decoder verifications by Claude (`REFERENCE-mpeg2dec-src.zip`)

| ID | Finding | Source | Level |
|---|---|---|---|
| V1 | Luma placement: field DCT no mid-height seam; frame DCT seam between frame lines 7 and 8 | getpic.c 436-449 | VERIFIED (implementation) |
| V2 | 4:2:0 chroma ignores `dct_type` (field path only if not 4:2:0) | getpic.c 467-482 | VERIFIED |
| V3 | Same `quantizer_scale` for all blocks of a macroblock; luma matrices selected for 4:2:0 chroma | getblk.c 274-276, 443-445; 411, 563 | VERIFIED (implementation, not a normative claim) |
| V4 | 4:2:0 chroma field prediction: even chroma lines top field, odd bottom | recon.c 267-286, calls 83-91 | VERIFIED; same-field chroma *filtering* remains a design choice |

Other: output only via `Write_Frame()` getpic.c 749/765/771; `progressive_frame` swapped at 768-773
(record fields come from the metadata slot); skipped macroblocks carry stale `macroblock_type`
(INTRA cleared at 896); `dct_type` read condition 388-392; CBP 0 decodable (getvlc.h 250). Line
numbers may drift by one or two. The project owner can re-upload the reference ZIP for any new check.

### 5.5 Sample material (Stage 1 VALID: frame counts = BestSource, I/P/B match)

| Clip | Size | Scan | FIELD/FRAME/NONE % | QP median (max) | Stage 2 role |
|---|---|---|---|---|---|
| `LG_576i_3_LP` | 720x576 | interlaced | 52.7/23.0/24.3 | 18 (112; 3.8% at 112) | development/tuning |
| `LG_576i_4_EP` | 352x576 | interlaced | 76.2/9.7/14.1 | 14 (112) | locked hold-out |
| `TEST_4A_A003` | 720x576 | interlaced | 68.7/19.5/11.8 | 14 (36) | locked hold-out |
| `TEST_2A_A001` | 704x576 | interlaced | 6.2/59.2/34.7 | 12 (80) | locked hold-out |
| `LG_576i_5_MLS` | 352x288 | progressive | 0/85.4/14.6 | 10 (62) | progressive/control |
| 4A/2A `_blocky` | as source | interlaced | mostly NONE | 62 constant | secondary paired-reference |
| XP, SP, 3A (+ `_blocky`) | unknown | unknown | not indexed | - | **unassigned** |

LP: 204 frames, 45x36 MBs, 97.06% mixed FRAME/FIELD frames. LP, EP, MLS start with two leading B
pictures (open GOP). Custom non-intra matrices in 4A, LP, EP, MLS (not 2A). No field pictures in
any clip. Only single-sequence, undamaged clips tested. 4A frame 298 has `frame_pred_frame_dct=1`
and linear QP. `_blocky` clips cannot test the value of a spatial QP map (QP 62 everywhere).

---

## 6. Authority and status files at handover

| File | State |
|---|---|
| `docs/REPOSITORY/00_PROJECT_STATUS.md` | v0.2 RATIFIED (status index; owning authority wins) (verified present) |
| `05_DECISIONS.md` | v1.1 RATIFIED 2026-10-08 |
| `06_DEBLOCK_CONCEPT.md` | v1.2 RATIFIED 2026-10-11 (verified present; candidate reviewed by this chat) |
| `02_INDEX_FORMAT_SPEC.md` | v0.4: constraints C-1..C-5 ratified; contents/packing frozen only at Stage 3 |
| `Stage1_Evidence_and_Gate_Report_v0_3.md` | RATIFIED; Stage 1 PASS |
| `Stage2_Experiment_Design_v0_5.md` | RATIFIED 2026-10-12 (verified); v0.4 superseded |
| `NOTICE.md`, `README.md` | Restricted Media policy applied (verified present) |
| Migration handback v0.20 (inside the v0.21 ZIP) | build/CI/release authority; with DR v0.20, HEK v0.6, Migration_Status v0.9 |
| `docs/MPEG2_Macroblock_Index_VapourSynth_Deblocking_Project_Proposal_v0_5.md` | stage order (D-01) |

---

## 7. Technical understanding for Stage 2

### 7.1 Geometry (`06` v1.2)

- Per 16x16 luma macroblock, frame picture: macroblock edges always candidate locations. FRAME and
  FIELD add the internal vertical seam at x = 8. Only FRAME adds the mid-height horizontal seam
  (between frame lines 7|8; same-field view top 6|8, bottom 7|9). **NONE: no internal seam in
  either orientation; outer edges only.**
- Support rule: a correction for one seam must not cross another known seam. Vertical: FRAME about
  4 samples per field, FIELD and NONE about 8. Horizontal: FRAME/FIELD 8, NONE 16. Chroma 4 per field.
- Chroma 4:2:0: one 8x8 block per plane per macroblock on a fixed grid; luma `dct_type` does not
  apply (V2); same QP (V3); parity premise verified (V4).
- Off-grid, prediction-propagated blocking bounds any grid-based post-filter; report I/P/B separately.
- `06` O-04: filtering policy for outer edges touching NONE is open. O-15 (HYPOTHESIS): macroblocks
  whose CBP leaves some luma blocks uncoded have prediction-only internal seams; examine only if
  diagnostics show unexplained internal-seam behaviour.

### 7.2 Stage 2 design (v0.5; read the file for exact wording)

- Question: given authoritative indexed geometry and QP, what filtering gives useful luma and chroma
  deblocking without unacceptable damage, and which index metadata does the final filter need?
- Prototype: Python 3 (64-bit), VapourSynth/BestSource, NumPy, serial runs; home `experiments/stage2/`.
- Mandatory pre-filter validation: reader reproduces analyzer v0.2 totals per formal clip;
  **two-dimensional registration check** on LP (FRAME-minus-FIELD contrast with index labels shifted
  -1/0/+1 macroblock in x and y must peak at zero shift; 8-pixel column grid-phase check must peak at
  phase 0; an 8-pixel horizontal offset would show as an ambiguous, not wrong, peak; missing clear
  peak is a stop condition).
- Leading B pictures output before the first I picture are excluded from quality evidence (still
  processed and validated).
- Ladder: unfiltered baseline -> indexed geometry + fixed clip-median QP (K0) -> same with real
  per-MB QP (only QP changes) -> kernel/threshold/strength development (real QP, LP only) -> NONE
  policy N0 -> bounded chroma C0/C1/C2 -> locked hold-outs unchanged -> transcode reporting -> gate.
- **K0 selection bias control:** tune K0 on even-numbered usable LP GOPs, compare fixed versus real
  QP on odd ones (GOP = display-order run from one I picture to the next, numbered from 0).
- QP: fixed control = per-clip median (LP 18, EP 14, MLS 10). Shared boundary = rounded mean
  (hypothesis); report high-disparity pairs (e.g. 112 next to 14) and boundaries touching NONE
  separately (NONE's QP quantised nothing there). Report QP-112 saturation separately.
- Strength: small declared sweep; OFF bit-exact; monotonic.
- Measurements: seam diagnostics, no-harm/collateral change, paired-reference metrics (transcodes
  only), I/P/B and QP-band splits; visual evidence for the project owner, blind A/B preferred; deterministic frame
  subsets chosen before viewing results.
- Gate: the project owner decides; no preset numeric threshold; ends with a metadata-retention list feeding Stage 3.
- Increments: S2-I1 reader/validation; S2-I2 seam maps + registration check; S2-I3 K0 on even GOPs;
  S2-I4 fixed versus real QP on odd GOPs; S2-I5 kernel development; S2-I6 NONE N0; S2-I7 chroma;
  S2-I8 hold-outs; S2-I9 transcode reporting; S2-I10 gate report. Each reviewed before the next.
- Section 3.6 (v0.5): derived-media policy restated in line with `NOTICE.md`; `NOTICE.md` governs.

### 7.3 Review watch points for Stage 2 code

Scripts print the files they read; OFF bit-exact; no correction crosses another seam; hold-outs not
viewed during tuning; registration check before any quality conclusion; frame ordinals match
BestSource; a Python oracle is not made bit-exact with later C++ by `/fp:precise` (check widths,
rounding, operation order, FMA).

---

## 8. Licence and Restricted Media (read `NOTICE.md` for exact terms)

- Project material AGPL-3.0-or-later; reference-decoder files keep their own notices; third-party
  material keeps its own terms.
- **Source Recordings**: recordings used for project testing (at present under `VHSC_samples/`).
  **Derived Media**: transformed picture/sound content, and by the project owner's **option (a)** also images or
  other media visualising metadata or measurements derived from Source Recordings (QP heat maps,
  seam-statistics plots). Index files, hashes, logs, metadata, source and purely numerical/text
  diagnostics are not Restricted Media unless they embed it (verified in `NOTICE.md` at `317d3f1`).
- **Embedded-document rule:** a document or file that embeds Restricted Media is itself Restricted
  Media while the embedded content remains; a version with it removed may be kept under the normal
  project terms. So a gate report with charts is Restricted; its text-only version is not.
- **Permitted Project Purposes** (`NOTICE.md`): development, testing, validation, diagnosis,
  reproduction of behaviour and review of this project and its results.
- No general exception for private review, persons or services in `NOTICE.md` ("Except for that
  active-development repository use, Restricted Media must not be ... transmitted ... or otherwise
  made available to another person or service"). The project owner's later owner authorisation covers ChatGPT
  and Claude until development closure (section 3.2). This is a **known post-snapshot
  documentation delta**: the committed `NOTICE.md` does not yet contain it; both handovers say so
  rather than pretending otherwise.
- Restricted Media may be in the repository during active development only as bounded test,
  evidence or review material. At finalisation all of it is removed from the tree and project
  assets, then the history purge removes historical copies; afterwards it stays out unless
  separately ratified.
- Consequence: charts in a Stage 2 gate report are Restricted Media and leave at finalisation; keep
  the numbers and text as the durable record.
- Copies held by AI providers after closure follow the providers' retention settings.

---

## 9. Things deliberately NOT being done

- No pixel seam detector, no Family B, no existing-filter yardstick (D-24, the project owner).
- No CSV index output; no field-picture filtering yet; no damaged-stream or multi-sequence support yet.
- No runtime AVX2 detection or non-AVX2 build; no Spectre mitigation; no x86 builds.
- No six-index runs in CI (the project owner-O7); no PDB retention beyond Actions artifact expiry (C1(c)).
- No wheel/PyPI until Stages 7-9; no matrix-coefficient capture unless evidence demands (Stage 1
  stays frozen); no CBP/motion vectors in the first filter.
- No editing of ratified files in place; no repository-wide line-ending renormalisation.
- No technical restart without the project owner's explicit authorisation.

---

## 10. Claude documents (this role)

Earlier: prior art + addendum; codec-mechanics review; source-comparison review; Stage 1 design,
patch/first-run and gate-report reviews; chroma discussion review (V1-V3); EP/MLS runs review;
questions after handover (V4); reconciliation after handover; repository drafts v1.1 review; Stage 2
v0.2 reviews (two); `show_source_clip_info*.vpy`. Since 2026-10-08:

| File | Content |
|---|---|
| `Claude_REVIEW_OF_ChatGPT_Repository_and_GitHub_Migration_Proposal_v0_1.md` | migration proposal review, file manifest |
| `Claude_ACKNOWLEDGEMENT_OF_Migration_Handback_v0_20_v0_1.md` | receipt, independent checks, deltas |
| `Claude_REVIEW_OF_ChatGPT_REVIEW_OF_Claude_ACKNOWLEDGEMENT_OF_Migration_Handback_v0_1.md` | line-by-line DR/HEK findings F1-F6 |
| `Claude_REVIEW_OF_ChatGPT_RECONCILIATION_AFTER_Claude_REVIEW_AND_OWNER_DECISIONS_v0_4_v0_1.md` | inventory items 1-15 |
| `Claude_REVIEW_OF_ChatGPT_Ratification_Summary_and_Step2A_Gitattributes_Draft_v0_1.md` | `.gitattributes` procedure |
| `Claude_REVIEW_OF_ChatGPT_Authority_Status_Update_Drafts_2026-10-11_v0_1.md` | `06` v1.2, Stage 2 v0.4, status; repo check at `e7f63d0` |
| `Claude_REVIEW_OF_ChatGPT_NOTICE_README_Media_Scope_Widening_Draft_v0_1.md` | first media-scope review |
| `Claude_REVIEW_OF_ChatGPT_Restricted_Media_v2_and_Stage2_v0_5_v0_1.md` | Restricted Media v2 |
| `Claude_HANDOVER_TO_Future_Claude_Chat_v0_5.md`, `..._v0_6.md` | previous handovers (superseded by this) |

Useful ChatGPT documents: its role handover (latest), `Stage1_Inspector_Instrumentation_Design_v0_3.md`,
`ChatGPT_RESPONSE_TO_Claude_QUESTIONS_After_Handover_v0_1.md`. Anything from the **wrong Claude chat**
of 2026-10-07 (e.g. `Response_to_Claude_Index_Driven_Ruling_and_Revised_Stage2_Plan_v0_1.md`) is
provenance only.

---

## 11. Lessons and traps

- Wrong-chat incident (2026-10-07): if something contradicts the authorities, ask where it came from.
- Do not reconstruct files from memory or summaries; ask the project owner to upload them.
- Change `06` open questions by meaning, not number.
- A hardcoded source path once made a count check silently test the wrong file: scripts must print
  what they read.
- "Done" may not be done: confirm in the source ZIP.
- A candidate file may differ from its own diff: check both.
- LF/CRLF: compare like with like (section 4.4).
- Recorder modes differ sharply (EP half width; MLS progressive SIF); never assume one clip
  represents the archive.
- The LP `.BAT` regenerates tracked baselines (section 5.1).
- Restricted Media wording must keep a permitted-purpose exception wherever it forbids publication,
  or it contradicts the project owner's own workflow (caught in review 2026-10-12).
- Tokens: the project owner relays between chats, so keep relay pastes short and self-contained.
- Quotes marked verbatim must be verbatim: v0.6 of this handover silently capitalised the project owner's
  authorisation ("I authorize"); he wrote "i authorize". Paraphrases must be labelled as such.

---

## 12. Outstanding items and known gaps

1. Where to record the project owner's 2026-10-12 AI-access authorisation (`00_PROJECT_STATUS`, Stage 2 3.6 or
   `05`): for the reconciliation gate.
2. Presence and frozen hashes verified at `317d3f1` (section 4.2). Still to do in the gate: a full
   cold read of the directly ratified `NOTICE.md`, `README.md`, Stage 2 v0.5 and status v0.2
   wording, which this chat has seen only as earlier drafts.
3. Eight `VHSC_samples/*.log` kept temporarily; remove when development no longer needs them.
4. Archive-wide questions still open: field pictures (O-08), recorder modes in the project owner's archive,
   matrix effects (O-07).
5. ChatGPT handover v0.5 review points (2026-10-12, sent to ChatGPT via the project owner): its section 16 shows
   the AI authorisation as a block quote but it is a paraphrase (label it or use the project owner's exact
   words); its 14.2 "do not use `git add -A`" should note the project owner's snapshot-commit allowance of
   2026-10-11; section 15's subsections are numbered 14.1-14.4. None blocks installing it.
6. Possible gate item: pin `*.md eol=crlf` in `.gitattributes`, or record that Markdown follows the
   checkout setting (section 4.4).
7. Future: end-of-development history purge (own plan); wheel/PyPI identity at Stages 7-9;
   optional tag/header version-equality check in the workflow.

---

## 13. State and next steps at handover

**State:** migration closed; post-migration housekeeping and authority updates closed; HEAD `317d3f1`
(reported). **No Stage 2 code exists. Technical restart is NOT AUTHORISED.**

**Next, in order (sequence agreed by ChatGPT and Claude, 2026-10-12):**

1. Both role handovers refreshed: ChatGPT v0.5 ready to install; this v0.7 is Claude's. The project owner
   commits both to `docs/HANDOVER/` (named staging).
2. **Mandatory independent knowledge-base reconciliation gate:** ChatGPT and Claude each inspect the
   current knowledge base (source ZIP of current `main`) for new, corrected, clarified or superseded
   knowledge; the project owner reconciles one delta list (owning file, current wording, proposed wording,
   provenance, kind: authority / operational / handover / history).
3. Apply only owner-ratified corrections; if anything material changes, **touch up** the handovers
   and status (do not rewrite them wholesale).
4. The project owner decides whether to authorise restart.
5. If authorised: **S2-I1 only** (read-only Stage 1 index reader and validation reproducing analyzer
   v0.2 totals; `progressive_frame` and picture-type handling; leading-B accounting) in
   `experiments/stage2/`; ChatGPT writes it, the project owner runs it, Claude reviews code and output before S2-I2.

---

## 14. Change log

### v0.7 - 2026-10-12

- Added the common continuity-purpose text agreed for both role handovers (section 0).
- Verified the as-at point from source ZIP `main_3`: commit `317d3f1`, five build-file hashes,
  frozen sources, six `.idx` baselines, `VERSION.txt`, presence of the ratified authority set.
- From ChatGPT handover v0.5: commit `5010b79`, CMD delivery conventions, ZIP packaging, direct
  ratification, embedded-document rule, the post-snapshot authorisation delta, and the agreed
  five-step sequence to the restart decision.
- Corrected the authorisation quote to the project owner's exact words; noted that Markdown is LF in source ZIPs.

### v0.6 - 2026-10-12

- Amended the same day: the project owner's verbatim statement of the handover's purpose added to section 0, to
  be carried into every future version. (His AI-access authorisation is already verbatim in 3.2.)
- Rewritten as a comprehensive continuity document at the project owner's direction (purpose and takeover model in
  section 0): adds project history and stage plan, review method, conversational rulings including
  the AI-access authorisation, repository layout and commit milestones, build and change-control
  facts, Stage 1 format and harness detail, full Stage 2 design summary, Restricted Media terms,
  things deliberately not done, lessons, and outstanding items.

### v0.5 - 2026-10-12

- Post-migration state; amended the same day for the AI-access authorisation.

### v0.4 and earlier - 2026-10-07/08

- Earlier states; see Git history.
