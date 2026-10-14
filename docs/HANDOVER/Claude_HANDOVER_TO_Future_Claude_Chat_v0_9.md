# Claude Handover to a Future Claude Chat - MPEG-2 Index-Driven Deblocker

**Filename:** `Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md`
**Version:** 0.9 (supersedes v0.8) - DRAFT FOR OWNER REVIEW
**Date:** 2026-10-14
**As-at repository state:** HEAD `c45dcf0923cbbbe335266d2c4302327f16ab94fe` (pushed; verified by this
chat from the GitHub source ZIP), on top of the single root commit
`11f47427624bf5f68b3426fe9f58aa26d40e47f7` (tree `45ad1f16a24d3cce0411863a9804472efa1c8529`).
**As-at work state:** technical restart AUTHORISED for S2-I1 only; S2-I1 candidate v0.2 delivered by
ChatGPT and cleared by this chat for the owner's Windows run; nothing from S2-I1 committed yet
(section 7.4).
**Companion:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md`, **prepared by this
chat on behalf of the ChatGPT role** because the ChatGPT chat reached its length limit on 2026-10-14
before refreshing its own handover. Same as-at point.
**From:** the original Claude technical-development chat (reviewer/researcher role)
**To:** the follow-on Claude chat taking over the same role
**Status:** Role handover, not project authority. Where this document and a named authority file
differ, the authority file wins, and the difference should be raised with the project owner.
**Identity rule:** this file names the owner only as "the project owner" (GitHub account
`hydra3333`), per `05_DECISIONS_v1_2.md` D-23. Keep it that way in every future version.

---

## 0. How to use this document

**Purpose.** This is the current chat's communication to its successor: a strong working
understanding of the project *as at the commit above*, so the successor can continue without
rediscovering decisions, conventions and history. It deliberately includes material that is not
repository authority: conversational rulings, working conventions, review habits, lessons and traps.

The project owner's own statement of the purpose (2026-10-12, verbatim, keep it in every future version):

> the handover doc is to be a communication between this chat and a the follow-on chat when this
> one is nearing its limits. as such it is intended to be a highly informative document (perhaps
> referencing other documents like the repository and decisions which may not be formally
> documented) ensuring all the evolved current rules and approaches and status and outstanding and
> upcoming items etc "as at this point in time" are clear for the follow on chat enabling it to
> pickup development where you leave off without any hiccup apart from determining any gaps between
> that "as at" and the point in time of the handover occurring - hence it should contain as much
> useful information as is reasonable to well achieve the purpose of the document.

**Common continuity-purpose text** (agreed for both role handovers, 2026-10-12; quoted exactly as it
stands in `docs/HANDOVER/ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT_FOR_BOTH_ROLES.md`, which carries the
2026-10-13 identity-only scrub; keep it in every future version of both):

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

**Takeover model (this role's working form of the six steps).**

1. Read this whole document. It is long on purpose.
2. Ask the project owner for the current repository state: a GitHub source ZIP of `main` (its
   archive comment holds the commit SHA; `unzip -z`) or, better, a ZIP of the owner's clone including
   `.git`, and the latest ChatGPT role handover.
3. Read the named authorities where exact wording matters (section 6).
4. Determine only the **delta** since `c45dcf0`: `git log` (history starts at `11f4742`; see 4.2),
   the source ZIP, the owner's S2-I1 run results, and anything the owner reports.
5. State which authority versions you are working from and ask the owner to confirm.
6. Pick up the pending task (section 13).

**Evidence marks.** "(verified)" = this chat checked it against files, Git objects or source.
"(reported)" = relayed by the project owner, not checked by this chat. Unmarked = settled record.

---

## 1. The project

The project owner (developer; sole committer; GitHub `hydra3333`) is building an **MPEG-2-specific,
index-driven deblocking filter for VapourSynth (API4, C++, AVX2)** for the owner's LG DVD-recorder
captures of VHS-C home video (MPEG-2 4:2:0, mostly interlaced PAL 720x576, top-field-first).

The idea: MPEG-2 decoders discard per-macroblock coding information. **Mpeg2BlockInspector** (the
MSSG MPEG-2 reference decoder plus minimal instrumentation) parses the elementary stream and writes a
per-frame, per-macroblock binary index. The future deblocker reads decoded frames from BestSource
plus that index, so it knows authoritatively, per macroblock, the effective quantiser and the luma
transform organisation (FRAME/FIELD/NONE), instead of guessing codec structure from pixels.

This is a **new project**. It is NOT Deblock4 (abandoned 2026-08-26; never propose resuming it; it
may be consulted only as historical reference). CNR3 (`hydra3333/vapoursynth-cnr3`) is the owner's
other VapourSynth plugin; it served only as a build-settings reference during the migration.

### 1.1 Stage plan (proposal v0.5, D-01)

Stage 0 concept and research -> Stage 1 evidence tooling (inspector + index + analyzer) -> **Stage 2
Python experimental prototype** -> **feasibility gate** (the owner decides; a negative result is
acceptable) -> Stage 3 freeze the production index (`.idx2`) -> Stage 4 inspector as minimal diff
(largely done) -> Stage 5 frame-identity proof -> Stage 6 C++ scalar validated against the Python
oracle -> Stage 7 API4 wrapper -> Stage 8 AVX2 (scalar kept as reference) -> Stage 9 distribution
(wheel/PyPI later; proposed name `vapoursynth-mpeg2deblock`).

### 1.2 Where things stand

- Stage 0 done; Stage 1 **PASSED and frozen**.
- Repository/build migration **CLOSED 2026-10-11**.
- Knowledge-base reconciliation gate (2026-10-12/13) **done**: corrections ratified and applied
  (`05` v1.2, Stage 2 v0.6, status v0.3, `NOTICE.md`, `README.md`), owner-identity scrub and
  37-path current-tree purge applied (pre-reset commit `fd82d78`), then the **history reset** to a
  single root commit `11f4742` and a fresh `v0.1.0` snapshot pre-release (section 4).
- Handovers ChatGPT v0.6 / Claude v0.8 cross-reviewed and installed (`eac5526`, `bfb6cc2`); final
  knowledge-base / repository verification **done**; Project Status **v0.4** ratified and committed
  (`c45dcf0`). The pre-restart gate is closed.
- **Technical restart AUTHORISED by the owner on 2026-10-14, for S2-I1 only** (3.2).
- Stage 2: design **v0.6 RATIFIED 2026-10-13**; **S2-I1 in progress** (candidate v0.2 cleared to run;
  owner Windows run pending; nothing committed). **S2-I2 and later NOT AUTHORISED.**

---

## 2. Who does what, and how

| Party | Role |
|---|---|
| **the project owner** | Owner, final authority; ratifies everything; runs all builds, tests and Git operations on Windows; commits and pushes |
| **ChatGPT** (separate chat) | Drafter: designs, repository and authority drafts, code, procedures, tools |
| **Claude** (this role) | Independent reviewer and researcher: cold reviews against source and evidence, reference-decoder verification, research, mechanical checks on every package, **rehearsal of every tool or procedure before the owner runs it**, small helper scripts when asked |

- Workflow: **ChatGPT drafts -> Claude reviews (and executes/rehearses) -> the owner ratifies -> the
  owner applies.** The chats cannot talk to each other; the owner relays everything (files and short
  pastes).
- The owner may close a review cycle and ratify a bounded change directly (done for the Restricted
  Media policy and Stage 2 v0.5 on 2026-10-12). Respect the actual decision history.
- Claude writes no production code unless the owner explicitly asks.

### 2.1 Working style and conventions (follow them)

- Independent, honest assessment over agreement; disagree with evidence. Verify against source with
  file:line, recompute hashes, diff files; never accept "done" without checking.
- Strong aversion to summaries displacing the authorities they summarise.
- **Every document Claude emits: US-ASCII, CRLF, mechanically verified after each write** (all bytes
  < 128, zero bare LF; report the counts). Check incoming packages the same way.
- **No personal name or geographic location of the owner in anything that may be committed**:
  "the project owner", "the project maintainer" (defined in `NOTICE.md`) or `hydra3333`. This
  includes Claude's own review documents, which have been committed before.
- Naming: `Claude_TOPIC_vX_Y.md`; reviews `Claude_REVIEW_OF_ChatGPT_TOPIC_vX_Y.md` (trailing version
  is the review's own). Small same-day amendments to an unratified Claude document may keep the
  filename with an internal version bump and a change-log line.
- **Repository file rules (D-23 v1.2):** versioned filenames; a revision is a new versioned file and
  the previous version is **deleted from the tree in the same change** (no `superseded/` folder; Git
  history is the only archive until the Development Closure history scrub). The still-unsuffixed
  `02_INDEX_FORMAT_SPEC.md` and `06_DEBLOCK_CONCEPT.md` (and the role-handover purpose-text file)
  take versioned names at their next real revision; nothing is renamed just for the rule.
  `README.md`, `NOTICE.md`, `LICENSE`, `.gitattributes` keep conventional names.
- **Version references (D-23 v1.2):** a mention of a versioned document means that version **or
  later**; a statement recording a past event (reviewed, ratified, hashed, frozen, superseded,
  change log) means exactly that version. No document is revised merely to chase a version mention.
- Labels: DECIDED / PROPOSED / AGREED / HYPOTHESIS / RESEARCHED / VERIFIED / OPEN. VERIFIED means the
  owner's test or a cold read of authoritative source; never promote an inference.
- Review findings: **MUST / SHOULD / OPTIONAL / NO OBJECTION**, each with evidence.
- Decisions for the owner in plain English: question / why it matters / recommendation / options.
- Hard abort over silent continuation in code. Pause at review points until the owner's explicit go.
- **End any review that needs relaying to ChatGPT with a short paste-ready block** (the owner's
  stated preference; relied on heavily).
- Chat replies concise; substance in the file; give the file with a one-line caption.
- **Windows CMD delivery:** paste is unreliable (dropped first characters, joined lines). Start with
  `cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"`; **one
  command per code block**; no long PowerShell one-liners; prefer a reviewed `.bat` for multi-step
  controlled work. Variables set with `set` exist only in that CMD window: multi-step procedures must
  say "one window throughout".
- **CMD caret trap:** unquoted `^` is CMD's escape character, so `HEAD^{tree}` must be quoted
  (`"HEAD^{tree}"`); an unquoted `sha^{commit}` silently becomes `sha{commit}` (this made a
  "must fail" gate always pass in a draft runbook, 2026-10-13).
- **Git staging:** named staging for controlled changes; `git add -A` allowed for a deliberate,
  inspected snapshot commit. `git diff --cached --check` warnings on lines that already ended in two
  spaces (Markdown hard breaks) are informational, not corruption.
- Use `--no-renames` when counting deletions/additions in a staged diff (Git otherwise reports
  versioned-file replacements as renames).
- ZIP packaging with a SHA-256 manifest for multi-file deliveries.

### 2.2 How this chat reviews (methods that caught real defects)

- Unzip each package into a fresh scratch directory; run Python with `-I`; check manifest, ASCII,
  CRLF.
- Diff every candidate against the current repository copy and against the previous draft; check
  that a candidate equals its own supplied diff (a draft once stripped trailing spaces on 16
  unrelated lines).
- **Execute tools, do not just read them.** Run ChatGPT's builders/scripts against a reconstructed
  repository (LF and `core.autocrlf=true` CRLF trees), then independently verify every output: per
  line, line counts, line-ending counts, residual searches, hashes. Reading alone missed defects that
  running found: a greedy regex that deleted four lines inside a ZIP member, a substitution that
  produced nonsense text, a global rule that would have rewritten `Trim()`/`always()` in the
  workflow, and a CMD gate that could never fail.
- Rehearse Git procedures against a local bare "origin". Note: a clone from a local path copies the
  whole object store; use `--no-local` (or HTTPS) to see what a real clone holds.
- Recompute frozen-file and baseline hashes from every new source ZIP; confirm "done" claims there.
- Fetch upstream when provenance is claimed; check arithmetic.

---

## 3. Key decisions and rulings (authoritative text is in the files)

### 3.1 Technical and repository decisions (`05_DECISIONS_v1_2.md`, D-01..D-26)

- D-01 order of work; D-03 Python reference prototype first; D-09 frame-owned processing with
  field-parity-aware sample access (no separate-field deblocking pass); D-12 Family C optional; D-14
  prediction diagnostic only; D-16 report I/P/B separately.
- **D-20 (clarified v1.2):** `05` is the technical/design decision authority; `NOTICE.md` separately
  governs Restricted Media permission and restrictions.
- **D-23 (amended v1.2, 2026-10-12/13):** original 2026-10-06 text kept with superseded clauses
  marked; amendments: versioned filenames + delete-from-tree on revision; "or later" version
  references; **owner-identity rule** (no personal name or location in committed files; an
  identity-only scrub is maintenance, no version bump); text/EOL/hash rule (delivered documents
  US-ASCII CRLF and checked; Git-stored and GitHub-archive Markdown may be LF; hashes must name the
  representation; **no `*.md eol=crlf` pin**). Normal sequence ChatGPT draft -> Claude review ->
  owner ratification, which the owner may waive.
- **D-24 index-driven product (DECIDED):** the production deblocker requires its matching index and
  takes luma seam geometry from it. No pixel seam-position detector, no pixel-only Family B. Pixels
  still judge blocking versus real edges and limit correction. Supersedes D-11, D-17, D-18; amends
  D-15 and D-08.
- **D-25 chroma in scope** on mechanism; same-field chroma filtering stays an experimental choice.
- **D-26 evidence hierarchy:** real LG recordings primary; software `_blocky` transcodes secondary.
- `05` D-09 wording "where geometry requires" deliberately left as ratified history.

### 3.2 Owner rulings (some recorded only in reviews, status and handovers)

- No existing-filter yardstick in Stage 2 (2026-10-08).
- LG recorder quality, best to worst: **XP -> SP -> LP -> EP -> MLS**; not the Stage 2 role order.
- **Unassigned/spare (no Stage 2 role, nothing inferred until indexed and assigned):** XP, SP,
  `TEST_3A_A002` and their `_blocky` copies, **and `LG_576i_3_LP_blocky`, `LG_576i_4_EP_blocky`,
  `LG_576i_5_MLS_blocky`** (2026-10-12). A role for EP_blocky would expose hold-out content.
- Python and native helpers must be **64-bit**.
- **AI media authorisation (2026-10-12, verbatim):** "i authorize chatgpt and claude AI to access and
  use the images, videos and audios for the purpose of this project and only for the duration of
  development of this project until development closure as stated by me." Now in `NOTICE.md` as a
  narrow exception: only the project maintainer may supply Restricted Media, only to ChatGPT and
  Claude, only for this project's own development conversations, until Development Closure; no
  training, dataset, publication or post-closure retention permission.
- **Development Closure** = the owner's express declaration that active development is finished.
  Restricted Media cleanup at closure; history purge at or promptly after; the repository may then
  continue as a maintenance project.
- **Filenames versioned; references mean "or later"** (2026-10-12; recorded in D-23).
- **Owner identity** never in committed files (2026-10-12; D-23). Fix everything in the current tree
  now; scrub old history later (done early: see 4.2).
- **Purge superseded versions from the tree** (2026-10-12): done in the 37-path purge.
- **Delete the migration handback ZIP; no v0.22** (2026-10-13). Its essential content is carried in
  sections 4.4-4.6 of this handover and in ChatGPT's handover.
- **Interim history reset** (2026-10-13): replace all history with one root commit holding the
  verified tree; delete the old `v0.1.0` Release and tag and all old Actions runs; publish a fresh
  `v0.1.0` pre-release on the new root. Done (4.2, 4.3).
- `VSVulkan4.h` stays the post-R81 snapshot; `VERSION.txt` records it.
- Pause discipline: one Stage 2 increment at a time, each reviewed before the next.
- The owner has questioned project viability after repeated non-working tools (2026-10-13). Standing
  answer agreed: every tool or procedure is executed or rehearsed by Claude before the owner runs it;
  increments stay small with known expected answers.
- **Project Status v0.4 ratified 2026-10-14** (`c45dcf0`); it records restart as NOT AUTHORISED *as at
  its ratification*.
- **Technical restart authorised (2026-10-14, verbatim):** "i am authorising chatgpt to tell me about
  the next stages and begin the first." Meaning: S2-I1 only. Not yet propagated into a status file
  (propose status v0.5 with or after the first S2-I1 commit). S2-I2 needs a separate decision after
  reviewed S2-I1 results.
- **FFmpeg/BestSource QP side data** (owner query 2026-10-14, closed, no scope change): see 7.4.
- Clarified for the owner: the inspector and analyzer stay frozen; S2-I1 adds only a new read-only
  reader and validation scripts; Stage 2 uses no DLL (the plugin is post-Stage-2 work).

---

## 4. Repository and build state

### 4.1 Layout (verified at `11f4742`; deltas to `c45dcf0` noted; 124 tracked files)

```text
README.md  LICENSE (AGPL-3.0-or-later)  NOTICE.md  .gitattributes  .gitignore
.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml
.github/workflows/expected_stage_bplus_switches.csv   (256 rows; current)
.github/workflows/expected_a3_v0_10_switches.csv      (historical; kept deliberately)
src/Mpeg2BlockInspector/   16 .c + 4 .h, FROZEN
src/mpeg2Deblock/          plugin.cpp, plugin_version.h, mpeg2Deblock.rc (Identity scaffold)
tools/Stage1_Inspector_Analyzer_v0_2.py   FROZEN
TESTING/                   7 .BAT + 7 .vpy (absolute paths to the active root)
VHSC_samples/              16 .mpg recordings (Restricted Media), 6 reference .idx, 6 .log
third_party/vapoursynth/include/  VapourSynth4.h VSHelper4.h VSScript4.h VSConstants4.h (R81),
                                  VSVulkan4.h (post-R81 master snapshot), VERSION.txt
vs/VapourSynth-mpeg2Deblock/  VapourSynth-mpeg2Deblock.slnx, two .vcxproj, two .filters
docs/REPOSITORY/           00_PROJECT_STATUS_v0_4 (v0.3 at 11f4742), 02_INDEX_FORMAT_SPEC (v0.4), 05_DECISIONS_v1_2,
                           06_DEBLOCK_CONCEPT (v1.2), Stage1_Evidence_and_Gate_Report_v0_3,
                           Stage2_Experiment_Design_v0_6   (no superseded/ folder)
docs/HANDOVER/             ChatGPT v0.6, Claude v0.8 (v0.5/v0.7 at 11f4742), ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT
docs/                      single-version research, review and proposal files (provenance)
experiments/stage2/        not in Git yet; exists only in the owner's working tree (S2-I1 v0.1 and v0.2
                           candidate files, uncommitted; section 7.4)
```

No ZIPs remain in the tree. Size: working files about 67 MB (recordings 49 MB, indexes 16 MB),
`.git` about 51 MB (one pack, 142 objects = 1 commit + 17 trees + 124 blobs) (verified).

### 4.2 History: the reset and the pre-reset provenance

**Current history (verified 2026-10-13 from a ZIP of the owner's fresh clone, and from the GitHub
source ZIP of `main`, whose archive comment is `11f4742...` and whose files rebuild exactly to tree
`45ad1f16...`, 124 files, zero owner-identity hits, no ZIPs):** at that time exactly one commit,
`11f47427624bf5f68b3426fe9f58aa26d40e47f7`, no parents, message "Fresh repository baseline after
history reset", author and committer `hydra3333 <10749357+hydra3333@users.noreply.github.com>`, tree
`45ad1f16a24d3cce0411863a9804472efa1c8529`. The clone's only refs are `main` and `origin/main` at that
commit; `fd82d78` is absent from its object database; repository-local `user.name`/`user.email` are
the same `hydra3333` no-reply identity. Claude independently rebuilt tree `45ad1f16...` from the
verified `fd82d78` source ZIP before the reset (124 files, all mode 100644).

**Commits after the root (all documentation-only; verified from GitHub ZIPs):**

| Commit | Content |
|---|---|
| `eac5526484061965e052f4de854944a28d4f72a2` | first of two handover-install commits |
| `bfb6cc272eb23508225fb8ba199b078d64101abe` | second (adds ChatGPT v0.6); net of both: ChatGPT v0.6 + Claude v0.8 added, v0.5 + v0.7 deleted; other 122 files byte-identical to `11f4742` |
| `c45dcf0923cbbbe335266d2c4302327f16ab94fe` | "Refresh project status after history reset": status v0.3 deleted, v0.4 added; other 123 files byte-identical; pushed `bfb6cc2..c45dcf0` |

`eac5526` and `bfb6cc2` show author `hydra3333`, offset `+1030` (reported `git log` output);
`c45dcf0`'s metadata was not shown to this chat.

**Pre-reset commits are provenance only.** They are cited in documents and in this handover but are
**not in the repository**; nobody can check them out. Wording: "removed from repository history".
Direct-SHA views on GitHub may persist until GitHub garbage collection; that is not "erased".

| Pre-reset commit | Content |
|---|---|
| `f6ea380` | old `v0.1.0` pre-release tag (Identity scaffold); release, tag and runs since deleted |
| `5141a23e5768b1be863de1094089d04d1f11245b` | final migration commit |
| `a0e7100` | `.gitattributes` CRLF pins for VS files and `*.bat` |
| `e7f63d0` | post-migration housekeeping |
| `5010b79` | `06` v1.2, Stage 2 v0.4, status v0.1 ratified |
| `2e4eab1` | `VERSION.txt` corrected to R81 |
| `317d3f1dad3dfa2988deb8f58abf84d59aa5878e` | Restricted Media policy, Stage 2 v0.5, status v0.2 |
| `1a3cb1c` | ChatGPT v0.5, Claude v0.5-v0.7, purpose text committed |
| `9c1ec9e`, `06f2a4e87f42188fdb864a7b7b41e47a47c8551f` | pre-cleanup snapshots (`docs/in-progress/`) |
| `fd82d78715ed6a61ef4e80b9769655eefe23c384` | reconciliation corrections + identity scrub + 37-path purge; tree `45ad1f16...`; **the externally recorded pre-reset source identity** |

The cleanup commit `fd82d78` was verified by this chat before the reset: zero owner name/location
hits (text and file names), all 37 deletions absent, all 37 changed files equal to the ratified final
forms, and every file outside `docs/`, `NOTICE.md`, `README.md` byte-identical to `317d3f1`.

### 4.3 Release and Actions state (reported unless marked)

- Old `v0.1.0` Release and tag deleted before the reset; all old Actions workflow runs (and their
  artifacts) deleted.
- Fresh pre-release **`v0.1.0`**, title "v0.1.0 NOT FOR USE, SNAPSHOT RELEASE ONLY", tag on
  `11f4742`; workflow-built asset `mpeg2Deblock-v0.1.0-win-x64.zip`, SHA-256
  `f8ddb2da0b38e9639231fc63600c28da0f0bf0e95429a5033812726f36d17785` (reported). The README link to
  the `v0.1.0` release page is therefore valid without edit. Not yet verified by Claude (asset not
  seen).

### 4.4 Build facts (formerly in the deleted migration handback; owners now: the VS project files)

- Two x64-only projects in one `.slnx`: `Mpeg2BlockInspector.exe` (legacy C, `/TC`, console, SDL off,
  `_CRT_SECURE_NO_WARNINGS`) and `mpeg2Deblock.dll` (C++20, `/permissive-`, SDL on). Debug `/MDd`,
  Release `/MT` (no VC++ redistributable). Both `/arch:AVX2`, `/favor:blend`, `/fp:precise` with no
  `/fp:contract`, `/GS`, CFG, CET, `/guard:ehcont`, ASLR/high-entropy VA, large-address-aware;
  Spectre mitigation deliberately off. Release PDBs with `/PDBALTPATH:%_PDB%`; Release imports
  KERNEL32 only. Exact switch lines are recorded as comments at the top of the workflow.
- Toolset `$(DefaultPlatformToolset)` with a guard target rejecting anything below v145. Windows SDK
  unpinned but recorded (local 10.0.28000.0, CI 10.0.26100.0; binaries differ; no identity claim).
- Build: VS2026 GUI (Release|x64 or Debug|x64), or plain CMD via `vswhere` + amd64 MSBuild. Do not
  override settings on the command line. 17 known inspector warnings per configuration (C4013 on
  `read/open/write/close/exit`, all int-returning, no x64 truncation risk; C4996; C4101); DLL zero
  warnings.
- Plugin: exports only `VapourSynthPluginInit2`; namespace `mpeg2deblock`, id
  `com.hydra3333.mpeg2deblock`; `Identity` function only; version 0.1.0.0 from `plugin_version.h`.
  `/MT` boundary rule: no CRT-owned object crosses the DLL boundary.
- Both binaries require an AVX2 CPU; no runtime CPU detection. Any later scalar code is a reference
  path inside the AVX2 binary, not a fallback.

### 4.5 CI and release (owners: the workflow file and `expected_stage_bplus_switches.csv`)

- One workflow, triggered only by **manual dispatch** (any branch; artifacts only) or a **published
  Release**. A push does not trigger it.
- On a Release it checks that the tag commit is in `main` history (`merge-base --is-ancestor`), then
  builds Debug and Release, checks 256 switch tokens and 8 HostX64 groups against the expected-switch
  CSV (CI never injects flags), and attaches one verified ZIP with exactly `Mpeg2BlockInspector.exe`,
  `mpeg2Deblock.dll`, `LICENSE`, `NOTICE.md`. PDBs and evidence go to Actions artifacts (expire by
  retention). The expected-switch CSV changes only by a reviewed commit, together with the workflow
  comment that references it.
- Release procedure: bump `plugin_version.h` first; publish a Release (pre-release where appropriate)
  on a `main` commit containing the current workflow; the workflow attaches the ZIP; no manual uploads.

### 4.6 Change control and local tests (formerly handback section 6)

- Inspector project-file change, or an exact MSVC toolset/compiler change (including a routine Visual
  Studio update that changes the compiler version) => run **all six local index regressions** (never
  in CI). `.filters`-only changes exempt. Infrastructure-only changes => one LP smoke run. SDK-only =>
  record only. Documentation-only => nothing.
- The six regressions: run the six `TESTING` BATs for the tracked indexes **serially**
  (`TEST_Mpeg2BlockInspector.BAT` 2A, `_blocky.BAT` 2A_blocky, `_2.BAT` 4A, `_LP_2`, `_EP_2`,
  `_MLS_2`), adapting local tool paths if needed; then prove the tracked indexes unchanged with
  `git diff --exit-code -- "VHSC_samples/*.idx"` and SHA-256; the LP case is mandatory. The BATs
  **overwrite the tracked `.idx` and `.log` in `VHSC_samples/`**: do not commit regenerated files with
  `git add -A`; restore known diagnostic logs after keeping any evidence.
- The seventh BAT, `TEST_Mpeg2BlockInspector_blocky_2.BAT`, generates the untracked
  `TEST_4A_A003_blocky.idx` (Stage 2 v0.6 plans it inside S2-I1; not a baseline; stays uncommitted
  unless the owner decides otherwise).
- For a smoke test, prefer writing to a scratch path and comparing with `fc /b` and SHA-256.

### 4.7 Line endings and accepted hashes (verified at `11f4742`)

- `.gitattributes` (8 lines): `getpic.c`, `mpeg2dec.c` `eol=lf`; analyzer `eol=crlf`; the five VS
  files and `*.bat`/`*.BAT` `eol=crlf`. Markdown is not pinned (D-23 v1.2): Git-stored and GitHub-ZIP
  Markdown is LF; the owner's Windows checkout gives CRLF.
- Five build-contract files (CRLF working form, as in the clone and post-`a0e7100` source ZIPs):
  - `Mpeg2BlockInspector.vcxproj` `c95ebed0750819032f689f436aac40094fcb6466a751e0bbdafe40908176ce8a`
  - `Mpeg2BlockInspector.vcxproj.filters` `a5a794a321f79122f6221a3f37669466417326a78126af4f3a2d9e8953c85269`
  - `mpeg2Deblock.vcxproj` `ca1d04cac4ab8af6a31e179a0ef1615ffa115c6085391c8802a5724996483467`
  - `mpeg2Deblock.vcxproj.filters` `5840b9fd4997395765b358f3c0af4f1b94acbc219e1eb3ccc70db253f0a99e16`
  - `VapourSynth-mpeg2Deblock.slnx` `852cc033e098a6d39afee9414053fce6401541157d16a49384b871f284c7d525`

---

## 5. Stage 1 (frozen) - what the successor needs

### 5.1 The tool and harness

- Command (TESTING `.BAT` files): `ffmpeg -v error -i <clip.mpg> -c:v copy -an -f mpeg2video - |
  Mpeg2BlockInspector.exe -b - -m <out.idx>`, then `python tools\Stage1_Inspector_Analyzer_v0_2.py
  summary <idx>`, then `vspipe --info` with `show_source_clip_info*.vpy` (written by Claude) comparing
  index picture types with BestSource `_PictType` per frame (`--arg "src=..." --arg "idx=..."`;
  `SHOW_FIRST`, `MAX_DIFFS_SHOWN`). Paths in the BATs: ffmpeg `C:\SOFTWARE\ffmpeg\ffmpeg.exe`, vspipe
  `D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe`.
- The index is written under a temporary name (`.s1tmp`) and renamed on success; exit 0 success, 1
  failure.
- **Short-read trap (found 2026-10-14):** `getbits.c` `Fill_Buffer()` treats any `read()` shorter than
  2048 bytes as end of stream, pads with sequence-end codes, finishes, marks the index COMPLETE and
  exits 0. Under Linux the ffmpeg pipe gave a 1-record LP index and a 2-record 2A-blocky index with exit
  0; file input or `< file` gives the exact accepted bytes. The Windows pipe evidently works (all six
  baselines came from it). New generation uses `ffmpeg -> scratch .m2v -> inspector -b <file>` and
  always gates on exact counts/totals. The inspector stays frozen. Debug output to stderr only. No CSV output (rejected; the index is binary,
  memory-mappable, in display order).

### 5.2 Temporary Stage 1 index format (authority: Stage 1 design v0.3 and `02` v0.4)

- 32-byte file header: magic `S1MBIDX1`, `struct.unpack("<8sHHIQII")`, endian marker 0x01020304,
  complete flag bit 0.
- Per output frame: 64-byte record header (magic `FRM1`, size, ordinal, picture type at byte 30, MB
  count as uint32 at offset 40) then 8 bytes per macroblock.
- File size = 32 + N x (64 + MBs x 8). Records in **display order**, one per output frame.
- Per macroblock: FRAME/FIELD/NONE, effective QP (derived scale; linear values 26/30 seen only in the
  one `q_scale_type = 0` frame), plus CBP and prediction type (available, not consumed first).
- K-07: FRAME/FIELD/NONE = coded residual transform geometry. NONE covers skipped macroblocks and
  non-intra macroblocks with effective CBP 0. Field pictures: the inspector refuses to publish.

### 5.3 Frozen identities and baselines (verified at `11f4742`)

- `getpic.c` `e80239cfe73a0c04490a9bf131714861254ed1d7d095b052aac616a887ef0eca`
- `mpeg2dec.c` `8e6053ccb3a40be8c0d985f2e35124bf728d1f61df9b6d0c01b71e13e13b0947`
- analyzer `8e0d58305ee4fe518c25b67bdbe74acc4fb392486f23e6137862d916e5e02cda`
- Six **immutable** reference indexes (never regenerate to make a test pass):
  - `LG_576i_3_LP.idx` `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011`
  - `LG_576i_4_EP.idx` `11b42aadf9f46b72dec20a8f3fdd754d07cdce78f0460a14eda08838336ffa87`
  - `LG_576i_5_MLS.idx` `378980ea462122a02d75f412faf9cfaf79962d503c68a8f6ee41c32b24d98d7f`
  - `TEST_2A_A001.idx` `afe51f251b2861d5c62e1629d95645c47b06f69d86f03b5fc531cf9fe3ea9273`
  - `TEST_2A_A001_blocky.idx` `cbf6e8720e47e1f097e6310540d8cbd20862e3a427ad53c61d9a235acdba9288`
  - `TEST_4A_A003.idx` `5b989ced016adfe5cc4546f196dd63cb2db9b431798a99203c830a98165b9a65`
- The inspector is built with Stage B+ settings (AVX2, `/O2 /GL`, `/MT`); all six indexes stayed
  byte-identical, so the Stage 1 evidence holds.

### 5.4 Reference-decoder verifications by Claude (`REFERENCE-mpeg2dec-src.zip`)

| ID | Finding | Source | Level |
|---|---|---|---|
| V1 | Luma placement: field DCT no mid-height seam; frame DCT seam between frame lines 7 and 8 | getpic.c 436-449 | VERIFIED (implementation) |
| V2 | 4:2:0 chroma ignores `dct_type` (field path only if not 4:2:0) | getpic.c 467-482 | VERIFIED |
| V3 | Same `quantizer_scale` for all blocks of a macroblock; luma matrices selected for 4:2:0 chroma | getblk.c 274-276, 443-445; 411, 563 | VERIFIED (implementation, not normative) |
| V4 | 4:2:0 chroma field prediction: even chroma lines top field, odd bottom | recon.c 267-286, calls 83-91 | VERIFIED; same-field chroma *filtering* remains a design choice |

Other: output only via `Write_Frame()` getpic.c 749/765/771; `progressive_frame` swapped at 768-773;
skipped macroblocks carry stale `macroblock_type` (INTRA cleared at 896); `dct_type` read condition
388-392; CBP 0 decodable (getvlc.h 250). Line numbers may drift by one or two. The owner can re-upload
the reference ZIP for any new check.

### 5.5 Sample material (Stage 1 VALID: frame counts = BestSource, I/P/B match)

| Clip | Size | Scan | FIELD/FRAME/NONE % | QP median (max) | Stage 2 role |
|---|---|---|---|---|---|
| `LG_576i_3_LP` | 720x576 | interlaced | 52.7/23.0/24.3 | 18 (112; 3.8% at 112) | development/tuning |
| `LG_576i_4_EP` | 352x576 | interlaced | 76.2/9.7/14.1 | 14 (112) | locked hold-out |
| `TEST_4A_A003` | 720x576 | interlaced | 68.7/19.5/11.8 | 14 (36) | locked hold-out |
| `TEST_2A_A001` | 704x576 | interlaced | 6.2/59.2/34.7 | 12 (80) | locked hold-out |
| `LG_576i_5_MLS` | 352x288 | progressive | 0/85.4/14.6 | 10 (62) | progressive/control |
| 4A/2A `_blocky` | as source | interlaced | mostly NONE | 62 constant | secondary paired-reference |
| XP, SP, 3A (+ `_blocky`), LP/EP/MLS `_blocky` | unknown | unknown | not indexed | - | **unassigned/spare** |

LP: 204 frames, 45x36 MBs, 97.06% mixed FRAME/FIELD frames. LP, EP, MLS start with two leading B
pictures (open GOP). Custom non-intra matrices in 4A, LP, EP, MLS (not 2A). No field pictures in any
clip. Only single-sequence, undamaged clips tested. 4A frame 298 has `frame_pred_frame_dct=1` and
linear QP. `_blocky` clips cannot test the value of a spatial QP map (QP 62 everywhere).
`TEST_4A_A003_blocky` (formal Stage 1 acceptance clip) has no tracked index; Stage 1 report section
8.1 gives its totals (300 records; FRAME 56,235 / FIELD 35,243 / NONE 394,522; QP 62 everywhere;
26 I / 75 P / 199 B) for validating a regenerated one.

---

## 6. Authority and status files at `11f4742`

| File | State |
|---|---|
| `docs/REPOSITORY/00_PROJECT_STATUS_v0_4.md` | RATIFIED 2026-10-14 (`c45dcf0`; v0.3 deleted); current-state index; says restart NOT AUTHORISED as at ratification (superseded in conversation, 3.2) |
| `docs/REPOSITORY/05_DECISIONS_v1_2.md` | RATIFIED 2026-10-13; technical/design decisions and repository conventions (D-23) |
| `docs/REPOSITORY/06_DEBLOCK_CONCEPT.md` | v1.2 RATIFIED 2026-10-11 (unsuffixed until next revision) |
| `docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md` | v0.4: constraints C-1..C-5 ratified; contents/packing frozen only at Stage 3 |
| `docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md` | RATIFIED; Stage 1 PASS |
| `docs/REPOSITORY/Stage2_Experiment_Design_v0_6.md` | RATIFIED 2026-10-13 |
| `NOTICE.md` | governs licence scope and Restricted Media (including the AI exception) |
| `README.md` | public summary; release link to `v0.1.0` |
| VS project files; workflow + expected-switch CSV | build settings; CI/release (sections 4.4-4.6) |
| `docs/MPEG2_Macroblock_Index_VapourSynth_Deblocking_Project_Proposal_v0_5.md` | stage order (D-01) |

Pre-reset SHAs in these files are provenance (D-23 history rule); no edit needed. Known dated text:
Stage 2 v0.6 section 22 items 1 and 4 (fix only at its next real revision).

---

## 7. Technical understanding for Stage 2

### 7.1 Geometry (`06` v1.2)

- Per 16x16 luma macroblock, frame picture: macroblock edges always candidate locations. FRAME and
  FIELD add the internal vertical seam at x = 8. Only FRAME adds the mid-height horizontal seam
  (between frame lines 7|8; same-field view top 6|8, bottom 7|9). **NONE: no internal seam in either
  orientation; outer edges only.**
- Support rule: a correction for one seam must not cross another known seam. Vertical: FRAME about 4
  samples per field, FIELD and NONE about 8. Horizontal: FRAME/FIELD 8, NONE 16. Chroma 4 per field.
- Chroma 4:2:0: one 8x8 block per plane per macroblock on a fixed grid; luma `dct_type` does not apply
  (V2); same QP (V3); parity premise verified (V4).
- Off-grid, prediction-propagated blocking bounds any grid-based post-filter; report I/P/B separately.
- `06` O-04: filtering policy for outer edges touching NONE is open. O-15 (HYPOTHESIS): partially
  coded macroblocks have prediction-only internal seams; examine only if diagnostics show
  unexplained internal-seam behaviour.

### 7.2 Stage 2 design (v0.6; read the file for exact wording)

- Question: given authoritative indexed geometry and QP, what filtering gives useful luma and chroma
  deblocking without unacceptable damage, and which index metadata does the final filter need?
- Prototype: Python 3 (64-bit), VapourSynth/BestSource, NumPy, serial runs; home `experiments/stage2/`.
- Mandatory pre-filter validation: the reader reproduces analyzer v0.2 totals per formal clip;
  **two-dimensional registration check** on LP (FRAME-minus-FIELD contrast with index labels shifted
  -1/0/+1 macroblock in x and y must peak at zero shift; 8-pixel column grid-phase check must peak at
  phase 0; an 8-pixel horizontal offset shows as an ambiguous, not wrong, peak; no clear peak = stop).
- Leading B pictures output before the first I picture are excluded from quality evidence (still
  processed and validated).
- Ladder: unfiltered baseline -> indexed geometry + fixed clip-median QP (K0) -> same with real per-MB
  QP (only QP changes) -> kernel/threshold/strength development (real QP, LP only) -> NONE policy N0
  -> bounded chroma C0/C1/C2 -> locked hold-outs unchanged -> transcode reporting -> gate.
- **K0 selection-bias control:** tune K0 on even-numbered usable LP GOPs, compare fixed versus real
  QP on odd ones (GOP = display-order run from one I picture to the next, numbered from 0).
- QP: fixed control = per-clip median (LP 18, EP 14, MLS 10). Shared boundary = rounded mean
  (hypothesis); report high-disparity pairs (e.g. 112 next to 14) and boundaries touching NONE
  separately (NONE's QP quantised nothing there). Report QP-112 saturation separately.
- Strength: small declared sweep; OFF bit-exact; monotonic.
- Measurements: seam diagnostics, no-harm/collateral change, paired-reference metrics (transcodes
  only), I/P/B and QP-band splits; visual evidence for the owner, blind A/B preferred; deterministic
  frame subsets chosen before viewing results.
- Gate: the owner decides; no preset numeric threshold; ends with a metadata-retention list for Stage 3.
- Increments: S2-I1 reader/validation (plus, if still absent, generate and validate
  `TEST_4A_A003_blocky.idx` against Stage 1 report 8.1 as a non-baseline); S2-I2 seam maps +
  registration; S2-I3 K0 on even GOPs; S2-I4 fixed versus real QP on odd GOPs; S2-I5 kernel; S2-I6
  NONE N0; S2-I7 chroma; S2-I8 hold-outs; S2-I9 transcode reporting; S2-I10 gate report.
- v0.6 section 3.0: unassigned list includes the three LP/EP/MLS `_blocky` clips; section 3.6
  restates the media policy (NOTICE governs), including the AI exception and Development Closure;
  machine-readable tables (CSV) are not visualisations, but a picture-like character grid is Derived
  Media; a later media-policy change goes into 3.6 in the same coordinated, owner-ratified change.

### 7.3 Review watch points for Stage 2 code

Scripts print the files they read; OFF bit-exact; no correction crosses another seam; hold-outs not
viewed during tuning; registration check before any quality conclusion; frame ordinals match
BestSource; generated files written to scratch paths, never over tracked baselines; a Python oracle is
not made bit-exact with later C++ by `/fp:precise` (check widths, rounding, operation order, FMA).
**Claude runs any script it can before the owner does** (with recordings supplied by the owner under
the AI exception), and states what it could not run.

**Windows CMD cannot be executed here.** Every BAT therefore gets a line-by-line audit in addition to
Linux rehearsal of the commands it calls:
- no two processes appending to the same file at the same time (v0.1 piped ffmpeg `2>>log` into the
  inspector `>>log`, and CMD failed with a sharing violation; Linux shells allow it, so the rehearsal
  passed);
- no digit directly before `>`/`>>` (`echo code: %rc%>>log` with `rc=0` becomes handle 0; write
  `>>"%log%" echo ...`);
- quoting, `^` carets, `%ERRORLEVEL%` captured on its own line outside blocks, `if errorlevel 1` after
  the right command (`setlocal enableextensions` resets ERRORLEVEL to 0);
- compare every redirection with the accepted `TESTING` BATs, not only the command line;
- `--info` / `--arg` vspipe forms as in the accepted BATs; certutil SHA-256 checked with
  `findstr /i /c:`.

### 7.4 S2-I1 - state, evidence and how to reproduce it

**Files (candidate v0.2, `experiments/stage2/`):** `stage2_index_reader_v0_2.py` (independent reader
of the Stage 1 v1 index), `stage2_index_reader_regression_v0_2.py` (six baselines: SHA-256 first, then
analyzer-v0.2 totals; four negative tests), `stage2_validate_bestsource_v0_2.vpy` (frame count,
dimensions, every `_PictType`), `S2_I1_validate_all_accepted_pairs_v0_2.bat` (vpy on the six accepted
pairs, read-only), `S2_I1_generate_4A_blocky_candidate_v0_2.bat` (scratch-only: ffmpeg to
`%TEMP%\VapourSynth-mpeg2Deblock_S2_I1\TEST_4A_A003_blocky.m2v`, inspector `-b file`, reader
`validate-4a-blocky`, analyzer, vspipe, certutil SHA-256 must equal the expected value, `git status`).
ChatGPT's full description is in ChatGPT handover v0.7 section 18.

**History (2026-10-14):**
1. v0.1 (4 files). Claude review: no MUST; S1 pipe short-read trap, S2 complete the 8.1 check and print
   SHA-256, S3 BestSource check for all six pairs; O1 MB-grid comment, O2 analyzer `--expected-frames`
   is report-only, O3 cache leading-B.
2. Owner Windows run of v0.1: the generation BAT failed with "The process cannot access the file
   because it is being used by another process" (ffmpeg and inspector appending to one log across a
   pipe). **This chat had cleared it and missed the defect**; acknowledged to the owner.
3. v0.2: the pipe was removed (scratch `.m2v` then file input), and S2, S3 and O1-O3 were applied.
   ChatGPT's chat then ended.
4. Claude v0.2 review (`Claude_REVIEW_OF_ChatGPT_S2_I1_Candidate_v0_2_v0_1.md`): **no MUST, cleared to
   run as delivered**. S1 SHOULD before commit: generation BAT line 77 handle-number trap. O1: the scratch
   `.m2v` is Restricted Media; delete it after use. O2: the all-pairs BAT logs to the console only. The
   overlay ZIP has a top-level folder; copy the five files into `experiments\stage2\`.

**Expected results of the owner run:**
- harness `PASS: S2-I1 v0.2 reader reproduces ...`;
- all-pairs BAT `PASS: ... all six accepted baseline pairs`;
- generation BAT `PASS SHA-256 = 57f3b60d1ea2108f29f222c7c658cb1ddc9eb26c14071cb056112a2f3b296e73`,
  then `PASS: ... generated and validated in scratch`;
- `git status --short` shows only `?? experiments/` (`__pycache__` is in `.gitignore`).

**Verified facts:**
- leading-B ordinals are LP/EP/MLS `[0, 1]`; 2A, 2A-blocky, 4A and 4A-blocky have none;
- mixed FRAME/FIELD frames: LP 198, EP 215, MLS 0, 2A 263, 2A-blocky 300, 4A 299, 4A-blocky 300;
- dct bits read: LP 250194, EP 146960, MLS 0, 2A 310442, 2A-blocky 171630, 4A 427107, 4A-blocky 91478.

**How this chat rehearsed it (repeat for later versions):**
- Build the frozen inspector on Linux: copy `src/Mpeg2BlockInspector/*` and run
  `gcc -O2 -w -o inspector *.c -lm`. With file input it reproduced all six accepted `.idx`
  byte-for-byte; check that first every time.
- Generate exactly as the BAT does: `ffmpeg -y -v error -i <mpg> -c:v copy -an -f mpeg2video <m2v>`,
  then `inspector -b <m2v> -m <idx>`.
- Cross-check the reader against the frozen analyzer by importing it (`load_index`, `summary_data`)
  and comparing every field.
- Mutation tests on a copy of `TEST_4A_A003.idx`:
  - field picture (byte 32+31);
  - `progressive_frame=2` (32+44);
  - `chroma_format=2` (32+49);
  - picture type 4 (32+30);
  - width change in record 1;
  - payload truncation;
  - dropped last record;
  - MB valid bit cleared;
  - `final_count+1`.
- BestSource proxy: `ffprobe -show_entries frame=pict_type,width,height` fed to
  `validate_clip_metadata()`. BestSource itself is not available here.
- Use `python3 -I`. Load modules with `importlib` and register them in `sys.modules`, because the
  reader's `slots=True` dataclasses need it.
- Delete extracted recordings and the `.m2v` afterwards.

**FFmpeg QP side data** (owner query, closed; informational only):
- BestSource's `videosource.cpp` reads only mastering-display, content-light, DoVi RPU, HDR10+ and ICC
  frame side data. It never enables `export_side_data=venc_params`, so O-01 is answered: not via
  BestSource.
- PyAV (`pip install av`; `codec_context.options={'export_side_data':'venc_params'}`) gives
  `AVVideoEncParams` type 2 with `qp=0` and 20-byte blocks `(src_x, src_y, w, h, delta_qp)`. Per-MB QP
  equals the index `q` for every MB in 2033/2040 frames across all 7 clips. Each clip's final output
  frame has no side data (end-of-stream flush).
- This informally satisfies Stage 2 v0.6 section 17. It does not replace the index (no
  FRAME/FIELD/NONE). The owner did not ask for a script.

---

## 8. Licence and Restricted Media (`NOTICE.md` governs; read it for exact terms)

- Project material AGPL-3.0-or-later; reference-decoder files keep their own notices; third-party
  material keeps its own terms.
- **Project maintainer** = the owner of GitHub account `hydra3333`.
- **Source Recordings**: recordings expressly included for testing (at present `VHSC_samples/*.mpg`).
  **Derived Media**: transformed picture/sound content, and (option (a)) visualisations of metadata or
  measurements derived from Source Recordings. **Restricted Media** = both. Index files, hashes, logs,
  metadata, source and purely numerical/text diagnostics are not Restricted Media unless they embed it.
  A document embedding Restricted Media is Restricted while it does so.
- **Permitted Project Purposes:** development, testing, validation, diagnosis, reproduction of
  behaviour and review of this project and its results.
- In the repository only as bounded test/evidence/review material during active development.
  Otherwise no copying, upload or transmission to any person or service, **except** the narrow AI
  exception: until Development Closure the project maintainer may supply Restricted Media to ChatGPT
  and Claude for this project's own development conversations; no permission to anyone else; no
  training, datasets, publication or post-closure retention. Copies are deleted when their purpose
  ends; this chat deletes extracted recordings from its workspace after use.
- **Development Closure** (owner's declaration that active development is finished): all
  Restricted Media leaves the tree and project-controlled assets; at or promptly after, a history
  purge/reset so media is absent from the resulting history; the repository may continue as a
  maintenance project. Leaving the project chats' uploads in place after closure is not permitted
  by `NOTICE.md`; the owner deletes them as far as each service allows.
- Stage 2 gate-report charts are Restricted Media; keep numbers and text as the durable record.
- The 2026-10-13 history reset was **not** Development Closure: the 16 recordings are intentionally
  still present and authorised.

---

## 9. Things deliberately NOT being done

- No pixel seam detector, no Family B, no existing-filter yardstick (D-24 and owner ruling).
- No CSV index output; no field-picture filtering yet; no damaged-stream or multi-sequence support yet.
- No runtime AVX2 detection or non-AVX2 build; no Spectre mitigation; no x86 builds.
- No six-index runs in CI; no PDB retention beyond Actions artifact expiry.
- No wheel/PyPI until Stages 7-9; no matrix-coefficient capture unless evidence demands (Stage 1
  stays frozen); no CBP/motion vectors in the first filter.
- No editing of ratified files in place; no `superseded/` folder; no `*.md eol=crlf` pin; no
  repository-wide line-ending renormalisation.
- No migration handback in the tree, and no v0.22.
- No Stage 2 increment beyond the one authorised (currently S2-I1) without the owner's explicit
  authorisation.

---

## 10. Claude documents (this role)

Committed provenance (in `docs/`, identity-scrubbed): prior art + addendum; codec-mechanics review;
source-comparison review; Stage 1 design, patch/first-run and gate-report reviews; chroma discussion
review (V1-V3); questions after handover (V4); reconciliation after handover; repository drafts v1.1
review; Stage 2 v0.2 reviews (two); migration proposal review; StageC MSBuild review;
`TESTING/show_source_clip_info*.vpy`.

Delivered in chat 2026-10-12/13 and **not in the repository** (the `docs/in-progress/` snapshot copies
were purged and are not in the reset history; the owner holds the delivered files):

| File | Content |
|---|---|
| `Claude_RECONCILIATION_GATE_Independent_Delta_Inventory_v0_1.md` | independent KB inventory (R1-R12) |
| `Claude_REVIEW_OF_ChatGPT_INDEPENDENT_KB_RECONCILIATION_v0_1_v0_1.md` | cross-classification; owner rulings on versioning |
| `Claude_REVIEW_OF_ChatGPT_KB_Reconciliation_Coordinated_Correction_Draft_v0_1.md` | M1 AI-exception actor; M2 identity |
| `Claude_PLAN_Superseded_Purge_and_Owner_Identity_Scrub_v0_1.md` | purge list and scrub rules |
| `Claude_REVIEW_OF_ChatGPT_Owner_Identity_Scrub_Candidate_Builder_v0_1.md`, `..._Builder_v0_4_v0_1.md`, `..._Builder_v0_5_v0_1.md` | builder reviews with execution results |
| `Claude_REVIEW_OF_ChatGPT_Final_Ratifiable_Texts_and_Apply_Procedure_v0_1.md` | final texts; apply rehearsal |
| `Claude_REVIEW_OF_ChatGPT_Interim_History_Reset_Proposal_v0_1.md` | reset approach; tag/identity/backup |
| `Claude_REVIEW_OF_ChatGPT_History_Reset_Runbook_v0_1_v0_1.md` | runbook rehearsal; CMD caret gate |

Delivered 2026-10-13/14 (not in the repository; the owner holds them):

| File | Content |
|---|---|
| `Claude_REVIEW_OF_ChatGPT_Handover_v0_6_v0_1.md` | cross-review; S1 three `_blocky` clips missing (applied) |
| `Claude_FINAL_KB_Repository_Verification_bfb6cc2_v0_1.md` | final gate; S1 status v0.3 stale |
| `Claude_REVIEW_OF_ChatGPT_Project_Status_v0_4_v0_1.md` | S1 "current HEAD" wording; S2 ratified form (both applied) |
| `Claude_REVIEW_OF_ChatGPT_S2_I1_Candidate_v0_1_v0_1.md` | S2-I1 v0.1 review with execution evidence |
| `Claude_REVIEW_OF_ChatGPT_S2_I1_Candidate_v0_2_v0_1.md` | S2-I1 v0.2 review; cleared; S1 line-77 fix |
| `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md` | written by this chat for the ChatGPT role (its chat ended) |

Earlier migration-era reviews (acknowledgement of handback v0.20, its review, reconciliation v0.4
review, Step 2A `.gitattributes`, authority/status drafts, media-scope reviews) exist only as delivered
files.

Useful ChatGPT documents: its role handover (latest), `Stage1_Inspector_Instrumentation_Design_v0_3.md`,
`ChatGPT_RESPONSE_TO_Claude_QUESTIONS_After_Handover_v0_1.md`. `Response_to_Claude_Index_Driven_Ruling_and_Revised_Stage2_Plan_v0_1.md`
came from the **wrong Claude chat** of 2026-10-07: provenance only, kept and scrubbed.

---

## 11. Lessons and traps

- Wrong-chat incident (2026-10-07): if something contradicts the authorities, ask where it came from.
- Do not reconstruct files from memory or summaries; ask the owner to upload them.
- Scripts must print what they read (a hardcoded path once made a check test the wrong file).
- "Done" may not be done: confirm in the source ZIP or clone.
- A candidate file may differ from its own diff: check both.
- LF/CRLF: compare like with like; name the representation when hashing.
- Recorder modes differ sharply (EP half width; MLS progressive SIF); never assume one clip
  represents the archive.
- The TESTING BATs regenerate tracked baselines in place (4.6).
- **Tools from the drafting chat failed repeatedly in October 2026** (greedy regex across lines,
  substitution nonsense, global rule hitting code, uncheckable gates). Running them against a
  realistic reconstruction found every defect before the owner's repository was touched. Keep doing it.
- Every ZIP left in the tree needs its own scan (a text-only scrub misses names inside ZIP members and
  member file names).
- Quotes marked verbatim must be verbatim (an earlier handover silently capitalised the owner's
  authorisation). Paraphrases must be labelled.
- Commit metadata is part of identity: author/committer name and e-mail, and also the time-zone offset
  recorded with each commit (section 12).
- Old tags keep old history alive: a reset is incomplete while any old tag or release remains.
- Local-path clones copy every object; rehearse with `--no-local`.
- Keep relay pastes short and self-contained; the owner carries them between chats.
- **A Linux rehearsal does not prove a Windows BAT.** v0.1's log collision passed here and failed for
  the owner. Audit CMD semantics line by line (7.3) and say plainly what was audited rather than run.
- **Chats end without warning.** ChatGPT's chat hit its limit on 2026-10-14 right after delivering
  S2-I1 v0.2, before updating its handover; this chat reconstructed it. Refresh handovers at each
  milestone (commit, ratification, delivered package), not at the end. That applies to this chat too.
- Frozen-inspector short-read trap (5.1): never trust a piped index without exact count gates.
- When the owner asks a side question (for example QP side data), answer it with evidence, and do not
  widen scope unless the owner asks.

---

## 12. Outstanding items and known gaps

1. **S2-I1 v0.2 owner Windows run** (7.4) and Claude's check of its console output and
   `TEST_4A_A003_blocky.log`.
2. S2-I1 S1 fix (generation BAT line 77), in place before the first commit if the owner agrees (v0.2
   was never committed or ratified), otherwise as a `_v0_3` BAT; Claude checks it.
3. First S2-I1 commit: delete the four `*_v0_1.*` files; add only the five accepted files by name;
   `git diff --cached --name-status --no-renames` must show exactly five additions; Claude verifies the
   pushed GitHub ZIP (only `experiments/stage2/` added; everything else byte-identical to `c45dcf0`).
4. Status v0.5 (restart authorisation, S2-I1 commit and result), drafted by ChatGPT and reviewed by
   Claude; delete v0.4 in the same commit.
5. A new ChatGPT chat must take over from ChatGPT handover v0.7. Its first deliverables deserve extra
   care (cold start).
6. Not yet seen by Claude: the fresh `v0.1.0` release page and asset (SHA-256 reported, 4.3).
7. **Owner decision (minor):** commits record the committer's local time-zone offset (`+1030` so
   far). If the owner wants no locality signal in future commits, commit with a UTC zone (for example
   `set TZ=UTC` in that CMD window, or `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` with `+0000`), checked with
   `git show -s --format=fuller`.
8. Six `VHSC_samples/*.log` are kept temporarily; remove when no longer needed.
9. Archive-wide questions still open: field pictures (O-08), recorder modes in the owner's archive,
   matrix effects (O-07).
10. Future: Development Closure plan (media removal, then history purge/reset, uploads deletion);
    wheel/PyPI identity at Stages 7-9; optional tag/header version-equality check in the workflow.
11. Optional: ask GitHub Support to purge cached views of old commits; delete any private backups of
    the pre-reset history once no longer needed.

---

## 13. State and next steps

**State at `c45dcf0` + working tree:**
- clean history (root plus three documentation commits);
- ratified authorities: `05` v1.2, `06` v1.2, `02` v0.4, Stage 1 report v0.3, Stage 2 v0.6, status
  v0.4;
- technical restart authorised for **S2-I1 only**;
- S2-I1 v0.2 cleared to run, not yet run, nothing committed;
- Restricted Media present and authorised;
- fresh `v0.1.0` snapshot pre-release.

**Next, in order:**

1. The owner places the five v0.2 files and runs the five commands in 7.4 (one per block, starting
   with the standard `cd /d`), then sends the console output and the log. Claude checks them against
   7.4's expected results. On any failure: stop, diagnose, fix in a new candidate, re-clear.
2. Line-77 fix (12.2); Claude checks the changed BAT.
3. First S2-I1 commit (12.3), then Claude's GitHub-ZIP verification.
4. S2-I1 result note to the owner (six regression PASSes, six correspondence PASSes, 4A-blocky
   candidate SHA-256 and 8.1 match, non-baseline, uncommitted; leading-B counts), then status v0.5.
5. **Stop.** S2-I2 (seam maps; two-dimensional registration with shifted labels -1/0/+1 MB in x and
   y; 8-pixel grid-phase check) only after the owner separately authorises it. Picture-like output from
   S2-I2 onward is Restricted Media. Claude rehearses S2-I2 code with recordings supplied under the AI
   exception and deletes them after use.
6. Refresh this handover after steps 3 and 4.

---

## 14. Change log

### v0.9 - 2026-10-14 (draft for owner review)

- As-at point moved to `c45dcf0` (handover install, final KB check, status v0.4) plus the S2-I1 v0.2
  working state.
- Recorded the restart authorisation (S2-I1 only, verbatim quote), closure of the pre-restart gate,
  and the owner's closed queries (frozen tools; FFmpeg/BestSource QP side data with findings).
- Added 7.4 (S2-I1 files, history, expected results, verified facts, rehearsal method) and the CMD
  audit rules (7.3); the frozen-inspector short-read trap (5.1); new lessons (Linux rehearsal is not
  proof for CMD; chats end without warning; side questions do not widen scope).
- Recorded that this chat missed the v0.1 log-collision defect.
- Listed the 2026-10-13/14 Claude documents, including the ChatGPT v0.7 handover prepared by this chat.
- Rewrote outstanding items and next steps for S2-I1 completion.

### v0.8 - 2026-10-13 (draft for cross-review)

- As-at point moved to the single root commit `11f4742` (tree `45ad1f16...`) after the history reset,
  verified from the owner's clone; pre-reset SHAs recorded as provenance only, `fd82d78` as the
  externally recorded pre-reset source identity.
- Recorded the knowledge-base reconciliation outcome: `05` v1.2 (D-20, D-23), Stage 2 v0.6, status
  v0.3, `NOTICE.md` AI exception and Development Closure, `README.md`; owner-identity scrub and
  37-path purge; deletion of the migration handback (no v0.22); history reset; old release, tag and
  Actions runs deleted; fresh `v0.1.0` pre-release.
- Carried the essential build, CI, release, change-control and test knowledge formerly in the
  handback (sections 4.4-4.6); full hashes for frozen files, baselines and build-contract files.
- Updated sample roles (three LP/EP/MLS `_blocky` clips unassigned; 4A-blocky index plan), media
  policy, conventions (versioned filenames, "or later", identity, no `superseded/`, no Markdown pin),
  review method (execute and rehearse tools), lessons and next steps.
- Removed the owner's personal name and city throughout; corrected the log count to six.

### v0.7 - 2026-10-12

- Common continuity-purpose text; as-at `317d3f1`; ChatGPT v0.5 facts; verbatim authorisation quote.

### v0.6 and earlier - 2026-10-07/12

- Earlier states; pre-reset history (provenance only).
