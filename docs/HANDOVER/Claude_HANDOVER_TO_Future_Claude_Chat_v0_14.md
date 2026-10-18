# Claude Handover to a Future Claude Chat - MPEG-2 Index-Driven Deblocker

**Filename:** `Claude_HANDOVER_TO_Future_Claude_Chat_v0_14.md`
**Version:** 0.14 (supersedes v0.12; v0.13 was never installed)
**Date:** 2026-10-18
**As-at repository state:** HEAD `82ba3e104b1f8ff9f3dd6214df1bbb4ae7cfc927` (pushed; verified by this
chat from a fresh GitHub clone on 2026-10-18), on top of the single root commit
`11f47427624bf5f68b3426fe9f58aa26d40e47f7` (tree `45ad1f16a24d3cce0411863a9804472efa1c8529`).
215 tracked files, zero `.zip` files.
**As-at work state:** Stage 1 frozen; S2-I1 and S2-I2 COMPLETE; Stage 2 design v0.7 and S2-I3 design
v0.3 RATIFIED. **S2-I3 P0 RATIFIED PASSED by the project owner on 2026-10-18.** The seven admitted
development indexes are tracked (`35923a5`); cleanup Commits A, B and C are complete, with four
leftovers (12.5); the
**S2-I3 P0 Evidence and Gate Report v0.1** (`e7cf449`) and **`06_DEBLOCK_CONCEPT.md` v1.3** (`82ba3e1`)
are ratified and installed. **Route A is down to its last step:** both role handovers must carry
interim-bridge sections 15-16 (this v0.14 does; ChatGPT v0.10's content was cleared by Claude on
2026-10-18 and its install copy follows this document's installation), then the transfer matrix records
the commit IDs, then the owner separately decides bridge retirement. **P1 remains unauthorised.**
**Companion:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_9.md` is the tracked
ChatGPT handover at this as-at point; its successor v0.10 is content-cleared and pending installation.
**From:** the Claude technical-development chat (reviewer/researcher role)
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
2. Ask the project owner for the current repository state. A public clone works and is the fastest
   route: `git clone --filter=blob:none --no-checkout https://github.com/hydra3333/VapourSynth-mpeg2Deblock`
   then a sparse checkout of what you need. Also ask for the latest ChatGPT role handover.
3. Read the named authorities where exact wording matters (section 6).
4. Determine only the **delta** since this document's as-at point `82ba3e1`: `git log 82ba3e1..HEAD`
   (history starts at `11f4742`; see 4.2), and anything the owner reports.
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
- Repository/build migration **CLOSED 2026-10-11**. Knowledge-base reconciliation gate **closed
  2026-10-13**; history reset to the single root commit `11f4742`; fresh `v0.1.0` snapshot pre-release.
- **S2-I1 COMPLETE** (reader and validation v0.2; committed `4221f7f`; status v0.5 `2286341`).
- **S2-I2 COMPLETE, registration gate PASS** on LP and LP_blocky. Code committed `190bd06`;
  evidence, gate report and status v0.6 committed `6e7b5c5`.
- **Stage 2 design v0.7, S2-I3 design v0.3 and Project Status v0.7 RATIFIED and installed
  2026-10-17** (`35cd543`). This replaced Stage 2 v0.6 and status v0.6 under D-23.
- **S2-I3 P0 COMPLETE and REVIEWED.** The design is ratified; the P0 code was cleared on 2026-10-17
  and **executed in full on 2026-10-18**: 8/8 admissions REGISTERED, 8/8 descriptive diagnostics,
  **4/4 pair tests PASS**, global summary run. Claude's comprehensive evidence review recommends the
  gate be recorded as **PASSED** and the ChatGPT role independently agreed. **The owner RATIFIED the
  P0 gate as PASSED on 2026-10-18** (7.8, 13), so the gate is closed and the seven-index tracking
  commit followed at `35923a5`. The 15-file P0 overlay, the `interim_` bridge, status v0.4, Claude
  review v0.5, the ratified P0 Evidence and Gate Report (`e7cf449`) and `06` v1.3 (`82ba3e1`) are all
  committed.
- Still to come in S2-I3 after P0: P1 onwards (fixed-QP experimentation), which needs both P0
  acceptance and a separate explicit owner authorisation.

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
- The owner may close a review cycle and ratify a bounded change directly. Respect the actual
  decision history.
- Claude writes no production code unless the owner explicitly asks.
- **The owner has asked that routine design and QA choices be settled between Claude and ChatGPT
  without repeated arbitration** (2026-10-16). Decide, state the decision, and only escalate what
  genuinely needs the owner.

### 2.1 Working style and conventions (follow them)

- Independent, honest assessment over agreement; disagree with evidence. Verify against source with
  file:line, recompute hashes, diff files; never accept "done" without checking.
- Strong aversion to summaries displacing the authorities they summarise.
- **Every document Claude emits: US-ASCII, CRLF, mechanically verified after each write** (all bytes
  < 128, zero bare LF; report the counts). Check incoming packages the same way. Watch for stray
  Unicode punctuation: an em dash slipped into a draft on 2026-10-17 and was caught by the check.
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
  stated preference; relied on heavily, and he asks for it again when it is missing).
- Chat replies concise; substance in the file; give the file with a one-line caption.
- **Windows CMD delivery:** paste is unreliable (dropped first characters, joined lines). Start with
  `cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"`; **one
  command per code block**; no long PowerShell one-liners; prefer a reviewed `.bat` for multi-step
  controlled work. Variables set with `set` exist only in that CMD window: multi-step procedures must
  say "one window throughout". The owner does also like a single block where one is genuinely safe.
- **CMD caret trap:** unquoted `^` is CMD's escape character, so `HEAD^{tree}` must be quoted
  (`"HEAD^{tree}"`); an unquoted `sha^{commit}` silently becomes `sha{commit}`.
- **Git staging:** named staging for controlled changes; `git add -A` allowed for a deliberate,
  inspected snapshot commit. `git diff --cached --check` warnings on lines that already ended in two
  spaces (Markdown hard breaks) are informational, not corruption. **Do not use
  `git diff --cached --check` as a STOP gate**: it fails on legitimate CRLF evidence files and on
  Markdown trailing spaces (this was corrected during S2-I2 Step B).
- Use `--no-renames` when counting deletions/additions in a staged diff (Git otherwise reports
  versioned-file replacements as renames).
- ZIP packaging with a SHA-256 manifest for multi-file deliveries. Note that ChatGPT sometimes wraps
  manifest hashes in backticks, which defeats `sha256sum -c`; parse rather than assume a mismatch.

### 2.2 How this chat reviews (methods that caught real defects)

- Unzip each package into a fresh scratch directory; check manifest, ASCII, CRLF, identity text, and
  name collisions against the current repository.
- Diff every candidate against the current repository copy and against the previous draft; check
  that a candidate equals its own supplied diff. For a revision, confirm **which files changed** by
  hash before reading anything, so the review is scoped to the actual delta.
- **Execute tools, do not just read them.** Run ChatGPT's scripts against a reconstructed repository,
  then independently verify every output. Reading alone has missed defects that running found.
- **A full environment is available in this workspace and should be used.** VapourSynth R81,
  BestSource 22.0 and NumPy 2.5.3 install from pip (`pip install --break-system-packages vapoursynth
  vapoursynth-bestsource`), and these are the **same versions recorded in the owner's committed
  S2-I2 `run_manifest.json`**. That means the candidate's own `.vpy` scripts can be run under real
  `vspipe` with real BestSource, not merely proxied. Do this; it is far stronger evidence than a
  proxy. `ffmpeg` is present. The frozen inspector builds with
  `gcc -O2 -w -o inspector *.c -lm` and reproduces the accepted `.idx` files byte-for-byte.
- Media comes from the public GitHub repository by sparse checkout, so recordings need not be
  uploaded for most work. **Delete all media, and BestSource's `.bsindex` cache files (they land
  under `/root/bsindex/...`), after every rehearsal, then verify none remain.**
- Rehearse Git procedures against a local bare "origin" or a real clone. A clone from a local path
  copies the whole object store; use `--no-local` (or HTTPS) to see what a real clone holds.
- Recompute frozen-file and baseline hashes from every new source; confirm "done" claims.
- **Run adversarial tests of your own, not only the supplied ones.** Tamper with evidence, swap
  indexes between encodes, simulate frame slips and pixel shifts, and check the gate refuses. This is
  what established confidence in the S2-I3 P0 admission logic.
- **Check any finding against the existing authorities before calling it new.** See 2.3.

### 2.3 A rule this chat added on 2026-10-17, after getting it wrong

Tracks with a review gate went well; one without a gate did not. This chat measured something,
concluded from it, and relayed the conclusion into a proposed repository document **without first
checking it against `06_DEBLOCK_CONCEPT.md`**. The consequences were three corrections in one day:

- a boundary **direction label inverted** (the statistic was for macroblocks adjacent *vertically*,
  sharing a *horizontal* boundary; it was reported as a vertical boundary);
- an **unstated denominator** (percentages silently excluded all `NONE`-involving macroblock pairs);
- a **mis-located measurement band** whose correction **reversed a published conclusion** (see 7.7).

Worse, the headline "finding" was already accepted knowledge: **K-03**, ratified 2026-10-08.

**Two rules, now standing:**

1. Before describing any finding as new, check it against `06_DEBLOCK_CONCEPT.md`'s K and O items and
   against `05_DECISIONS_v1_2.md`. Where it confirms an existing item, say so - a measurement that
   confirms a RESEARCHED item on real project material is valuable as an **evidence-level upgrade**,
   and should be offered that way rather than as a new K number.
2. Exploratory measurements stay in review correspondence. They do not become proposed repository
   documents until a gate report needs them.

---

## 3. Key decisions and rulings (authoritative text is in the files)

### 3.1 Technical and repository decisions (`05_DECISIONS_v1_2.md`, D-01..D-26)

- D-01 order of work; D-03 Python reference prototype first; D-09 frame-owned processing with
  field-parity-aware sample access (no separate-field deblocking pass); D-12 Family C optional; D-14
  prediction diagnostic only; D-16 report I/P/B separately.
- **D-05 starter knowledge documents:** add documents only on demonstrated need, and note its own
  wording - "durable findings should be incorporated into the appropriate project document". That
  points **away** from new standalone notes.
- **D-13 first metadata set** = per-macroblock quantiser and transform state only. Motion vectors
  need a higher evidence bar; do not propose capturing them casually.
- **D-20 (clarified v1.2):** `05` is the technical/design decision authority; `NOTICE.md` separately
  governs Restricted Media permission and restrictions.
- **D-23 (amended v1.2):** versioned filenames + delete-from-tree on revision; "or later" version
  references; **owner-identity rule**; text/EOL/hash rule (delivered documents US-ASCII CRLF and
  checked; Git-stored and GitHub-archive Markdown may be LF; hashes must name the representation;
  **no `*.md eol=crlf` pin**). Normal sequence ChatGPT draft -> Claude review -> owner ratification,
  which the owner may waive.
- **D-24 index-driven product (DECIDED):** the production deblocker requires its matching index and
  takes luma seam geometry from it. No pixel seam-position detector, no pixel-only Family B.
  Supersedes D-11, D-17, D-18; amends D-15 and D-08.
- **D-25 chroma in scope** on mechanism; same-field chroma filtering stays an experimental choice.
- **D-26 evidence hierarchy:** real LG recordings are **primary** Stage 2 feasibility evidence, judged
  by **seam-local diagnostics, collateral-change/no-harm measures and the owner's visual assessment**.
  The software-transcode `_blocky` pairs are **secondary paired-reference evidence**, interpreted only
  as movement toward or away from their higher-quality decoded sources, **not pristine ground truth**.
  Read this before proposing any paired metric: it already decides the framing.
- `05` D-09 wording "where geometry requires" deliberately left as ratified history.

### 3.2 Owner rulings (some recorded only in reviews, status and handovers)

- No existing-filter yardstick in Stage 2 (2026-10-08).
- LG recorder quality, best to worst: **XP -> SP -> LP -> EP -> MLS**; not the Stage 2 role order.
- Python and native helpers must be **64-bit**.
- **AI media authorisation (2026-10-12, verbatim):** "i authorize chatgpt and claude AI to access and
  use the images, videos and audios for the purpose of this project and only for the duration of
  development of this project until development closure as stated by me."
- **Development Closure** = the owner's express declaration that active development is finished.
- **Owner identity** never in committed files (2026-10-12; D-23).
- Pause discipline: one Stage 2 increment at a time, each reviewed before the next.
- The owner has questioned project viability after repeated non-working tools (2026-10-13). Standing
  answer: every tool or procedure is executed or rehearsed by Claude before the owner runs it;
  increments stay small with known expected answers.
- **Strong methodological preference (2026-10-16, verbatim):** "I am keen on evaluating developing and
  testing against a range of real-world data and not just selective parts of it eg odds or evens or
  one file source ... I hope you get understand my strong preference to not develop a method based on
  just one input or type of input !!" This drove the replacement of the even/odd-GOP scheme with the
  full eight-source multi-content design (Stage 2 v0.7, S2-I3 v0.3). Honour it.
- Also stated then: "developing on partial data is never a good idea"; characterise all sources,
  develop on all, and evaluate even/odd splits separately rather than developing on one of them.
- **Routine design and QA choices should be settled between Claude and ChatGPT** without repeated
  arbitration (2026-10-16).
- **2026-10-17, new sample material:** the owner added twelve files, then **removed eight of them**
  after this chat showed they were renamed copies of existing clips, two of them a locked hold-out
  and a control (5.6). Only `TEST_6A_home_576i` and `TEST_7A_home_576i`, with their `_blocky` copies,
  are genuinely new.
- **2026-10-17, media commit permission:** "the new mpg files can be treated like the others,
  committed temporarily." The four recordings were in fact committed in snapshot `6b7acc3`, inside a
  mixed sweep rather than the separate bounded commit planned. The owner has **not yet** decided how
  "temporarily" is achieved; `git rm` cannot remove historical blobs, so this is a Development Closure
  question (12.17).

---

## 4. Repository and build state

### 4.1 Layout (verified at `82ba3e1`; 215 tracked files, zero `.zip`)

```text
README.md  LICENSE (AGPL-3.0-or-later)  NOTICE.md  .gitattributes  .gitignore (now ignores *.zip *.patch *.diff)
.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml
.github/workflows/expected_stage_bplus_switches.csv   (256 rows; current)
.github/workflows/expected_a3_v0_10_switches.csv      (historical; kept deliberately)
src/Mpeg2BlockInspector/   16 .c + 4 .h, FROZEN
src/mpeg2Deblock/          plugin.cpp, plugin_version.h, mpeg2Deblock.rc (Identity scaffold)
tools/Stage1_Inspector_Analyzer_v0_2.py   FROZEN
TESTING/                   7 .BAT + 7 .vpy (absolute paths to the active root)
VHSC_samples/              20 .mpg recordings (Restricted Media, including the four 6A/7A files),
                           13 .idx (six frozen Stage 1 baselines + seven development indexes), 6 .log
third_party/vapoursynth/include/  VapourSynth4.h VSHelper4.h VSScript4.h VSConstants4.h (R81),
                                  VSVulkan4.h (post-R81 master snapshot), VERSION.txt
vs/VapourSynth-mpeg2Deblock/  VapourSynth-mpeg2Deblock.slnx, two .vcxproj, two .filters
experiments/stage2/        29 files: S2-I1, S2-I2 and the 15-file S2-I3 P0 overlay; plus 25 files of
                           results/S2_I2_v0_1/{LP,LP_blocky}/ evidence (CSV/JSON/log/txt)
experiments/S2-I3/         3 leftover tracked copies, byte-identical to docs/REPOSITORY 00_PROJECT_STATUS_v0_7,
                           S2_I3 design v0_3 and Stage2 design v0_7 (swept in by 6b7acc3; see 12.5)
experiments/               S2_I2_Closure_v0_3.md, a superseded closure review draft (6b7acc3; see 12.5)
docs/REPOSITORY/           00_PROJECT_STATUS_v0_7, 02_INDEX_FORMAT_SPEC (v0.4), 05_DECISIONS_v1_2,
                           06_DEBLOCK_CONCEPT (v1.3, unsuffixed - see 12.3), S2_I2_Evidence_and_Gate_Report_v0_1,
                           S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3,
                           S2_I3_P0_Evidence_and_Gate_Report_v0_1, Stage1_Evidence_and_Gate_Report_v0_3,
                           Stage2_Experiment_Design_v0_7, interim_ bridge (temporary)
docs/HANDOVER/             ChatGPT v0.9, Claude v0.12 (v0.14 on installation), P0 status v0.4,
                           ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT
docs/                      47 single-version research, review and proposal files (provenance),
                           including Claude_P0_EVIDENCE_REVIEW_AND_GATE_RECOMMENDATION_v0_5
```

`.gitattributes` gained one line during S2-I2 Step B: `experiments/stage2/results/** -text`, which
pins the committed evidence files so Git does not renormalise them.

### 4.2 History

**Current history** starts at the root commit `11f47427624bf5f68b3426fe9f58aa26d40e47f7`
(2026-10-13, no parents, tree `45ad1f16a24d3cce0411863a9804472efa1c8529`). All commits are by
`hydra3333 <10749357+hydra3333@users.noreply.github.com>`.

| Commit | Date | Content |
|---|---|---|
| `11f4742` | 10-13 | Fresh repository baseline after history reset |
| `eac5526` | 10-14 | first handover-install commit |
| `bfb6cc2` | 10-14 | second handover-install commit |
| `c45dcf0` | 10-14 | status v0.3 deleted, v0.4 added (**v0.9's as-at point**) |
| `bfaed24` | 10-14 | SNAPSHOT (ChatGPT chat died); installed Claude handover v0.9 |
| `10956a1` | 10-14 | SNAPSHOT2 |
| `4221f7f` | 10-14 | **S2-I1 code v0.2 added**; v0.1 drafts, package ZIPs and superseded handovers removed |
| `2286341` | 10-14 | **status v0.5 ratified: S2-I1 complete** |
| `190bd06` | 10-16 | **S2-I2 code v0.1** (nine files) |
| `6e7b5c5` | 10-16 | **S2-I2 evidence + gate report + status v0.6** (40 A / 1 M / 1 D; the M is `.gitattributes`) |
| `35cd543` | 10-17 | **Stage 2 v0.7 + S2-I3 v0.3 + status v0.7 installed** (3 A / 2 D); v0.6 documents removed (**v0.10's as-at point**) |
| `6b7acc3` | 10-17 | SNAPSHOT after handovers updated: **58 files added**, 181 -> 239, 158.8 MB. Swept in review artefacts, 16 ZIPs, a 54 MB copy of the repository inside itself, and the four authorised 6A/7A recordings |
| `3f8f45a` | 10-17 | Removed one identity-bearing handover-review ZIP; four other carriers missed (12.17) |
| `4636c33` | 10-17 | Owner's second snapshot: **25 A / 0 M / 0 D**, 239 -> 264. Installed the 15-file P0 overlay with the corrected P0A, the consolidated `interim_` knowledge bridge, status v0.2, and 8 further review artefacts |
| `f4a40e1` | 10-18 | **2 A / 0 M / 0 D**, 264 -> 266: ChatGPT handover v0.9 and status v0.3. No predecessor deletions, so three ChatGPT handover versions coexisted |
| `03edabf` | 10-18 | **Bad staging, 7 A / 0 D.** Swept in two WITHDRAWN Claude review drafts, a duplicate status v0.4 at `docs/` root, two review ZIPs, and installed the UNCORRECTED status v0.4 at the authoritative path while the cross-reviewed one landed at `docs/` root |
| `584f5dd` | 10-18 | **Remediation, 1 M / 7 D.** Swapped the correct status v0.4 into `docs/HANDOVER/`, deleted both withdrawn drafts, the duplicate, both ZIPs, and the overdue status v0.2 and v0.3 predecessors |
| `166af3a` | 10-18 | **`.gitignore` extended** with `*.zip`, `*.patch`, `*.diff` (1 M). **v0.11 and v0.12 as-at point**; 266 tracked files |
| `0fad5ea` | 10-18 | SNAPSHOT: added Claude v0.11 and v0.12 (2 A). v0.11 had been superseded before installation and was removed again at `b83ab3e` |
| `45664d5` | 10-18 | SNAPSHOT: the two-sentence Claude v0.12 update recording the owner's decision not to re-version three documents (1 M) |
| `7f8e445` | 10-18 | **Commit A**: the four identity carriers removed (4 D) |
| `b83ab3e` | 10-18 | **Commit B**: ChatGPT v0.7 and v0.8, Claude v0.9, v0.10 and v0.11 removed (5 D) |
| `35923a5` | 10-18 | Seven development indexes tracked (7 A). Claude verified all seven byte-identical to the admitted references and the six frozen Stage 1 indexes unchanged |
| `8ffaa7d` | 10-18 | **Commit C**: 52 review-only artefacts removed (52 D), including the nested repository ZIP; 214 files, zero ZIPs |
| `e7cf449` | 10-18 | S2-I3 P0 Evidence and Gate Report v0.1 installed (1 A), byte-identical to the install copy Claude diff-cleared |
| `82ba3e1` | 10-18 | `06_DEBLOCK_CONCEPT.md` v1.3 installed in place (1 M), byte-identical to its cleared install copy, after the report as required. **v0.14's as-at point** (v0.13 was drafted at the same point and never committed); 215 tracked files |

**Pre-reset commits are provenance only.** They are cited in documents but are **not in the
repository**; nobody can check them out. Wording: "removed from repository history". Direct-SHA views
on GitHub may persist until GitHub garbage collection; that is not "erased". The pre-reset chain was
`f6ea380`, `5141a23`, `a0e7100`, `e7f63d0`, `5010b79`, `2e4eab1`, `317d3f1`, `1a3cb1c`, `9c1ec9e`,
`06f2a4e`, and `fd82d78` (reconciliation + identity scrub + 37-path purge; tree `45ad1f16...`; the
externally recorded pre-reset source identity).

### 4.3 Release and Actions state (reported unless marked)

- Old `v0.1.0` Release and tag deleted before the reset; all old Actions runs and artifacts deleted.
- Fresh pre-release **`v0.1.0`**, title "v0.1.0 NOT FOR USE, SNAPSHOT RELEASE ONLY", tag on
  `11f4742`; asset `mpeg2Deblock-v0.1.0-win-x64.zip`, SHA-256
  `f8ddb2da0b38e9639231fc63600c28da0f0bf0e95429a5033812726f36d17785` (reported; not seen by Claude).

### 4.4 Build facts (owners now: the VS project files)

- Two x64-only projects in one `.slnx`: `Mpeg2BlockInspector.exe` (legacy C, `/TC`, console, SDL off,
  `_CRT_SECURE_NO_WARNINGS`) and `mpeg2Deblock.dll` (C++20, `/permissive-`, SDL on). Debug `/MDd`,
  Release `/MT` (no VC++ redistributable). Both `/arch:AVX2`, `/favor:blend`, `/fp:precise` with no
  `/fp:contract`, `/GS`, CFG, CET, `/guard:ehcont`, ASLR/high-entropy VA, large-address-aware;
  Spectre mitigation deliberately off. Release PDBs with `/PDBALTPATH:%_PDB%`; Release imports
  KERNEL32 only. Exact switch lines are recorded as comments at the top of the workflow.
- Toolset `$(DefaultPlatformToolset)` with a guard target rejecting anything below v145. Windows SDK
  unpinned but recorded (local 10.0.28000.0, CI 10.0.26100.0).
- Build: VS2026 GUI (Release|x64 or Debug|x64), or plain CMD via `vswhere` + amd64 MSBuild. Do not
  override settings on the command line. 17 known inspector warnings per configuration; DLL zero
  warnings.
- Plugin: exports only `VapourSynthPluginInit2`; namespace `mpeg2deblock`, id
  `com.hydra3333.mpeg2deblock`; `Identity` function only; version 0.1.0.0 from `plugin_version.h`.
  `/MT` boundary rule: no CRT-owned object crosses the DLL boundary.
- Both binaries require an AVX2 CPU; no runtime CPU detection.

### 4.5 CI and release (owners: the workflow file and `expected_stage_bplus_switches.csv`)

- One workflow, triggered only by **manual dispatch** or a **published Release**. A push does not
  trigger it.
- On a Release it checks the tag commit is in `main` history, builds Debug and Release, checks 256
  switch tokens and 8 HostX64 groups against the expected-switch CSV, and attaches one ZIP with
  exactly `Mpeg2BlockInspector.exe`, `mpeg2Deblock.dll`, `LICENSE`, `NOTICE.md`.
- Release procedure: bump `plugin_version.h` first; publish a Release on a `main` commit containing
  the current workflow; no manual uploads.

### 4.6 Change control and local tests

- Inspector project-file change, or an exact MSVC toolset/compiler change => run **all six local index
  regressions** (never in CI). `.filters`-only changes exempt. Infrastructure-only => one LP smoke
  run. SDK-only => record only. Documentation-only => nothing.
- The six regressions: run the six `TESTING` BATs serially, then prove the tracked indexes unchanged
  with `git diff --exit-code -- "VHSC_samples/*.idx"` and SHA-256. The BATs **overwrite the tracked
  `.idx` and `.log`**: do not commit regenerated files with `git add -A`.
- The seventh BAT generates the untracked `TEST_4A_A003_blocky.idx` (non-baseline).

### 4.7 Line endings and accepted hashes

- `.gitattributes` (9 lines): `getpic.c`, `mpeg2dec.c` `eol=lf`; analyzer `eol=crlf`; the five VS
  files and `*.bat`/`*.BAT` `eol=crlf`; `experiments/stage2/results/** -text`. Markdown is not pinned
  (D-23 v1.2).
- The owner's git has **`core.autocrlf=true`**: `.py` and `.md` files are **stored LF** and appear
  CRLF in his working copy; BATs are pinned CRLF. Example (verified): `stage2_index_reader_v0_2.py`
  working copy CRLF `139f02c6...`, Git-stored LF `f9892039...`. **Always name the representation.**
- `.idx` files are auto-detected as **binary** (`git ls-files --eol` shows `-text`); they contain only
  the magic `S1MBIDX1` as readable text, no paths, so their bytes are machine-independent. The same is
  true of `.mpg`. No `.gitattributes` change is needed to add either.
- Five build-contract files (CRLF working form):
  - `Mpeg2BlockInspector.vcxproj` `c95ebed0750819032f689f436aac40094fcb6466a751e0bbdafe40908176ce8a`
  - `Mpeg2BlockInspector.vcxproj.filters` `a5a794a321f79122f6221a3f37669466417326a78126af4f3a2d9e8953c85269`
  - `mpeg2Deblock.vcxproj` `ca1d04cac4ab8af6a31e179a0ef1615ffa115c6085391c8802a5724996483467`
  - `mpeg2Deblock.vcxproj.filters` `5840b9fd4997395765b358f3c0af4f1b94acbc219e1eb3ccc70db253f0a99e16`
  - `VapourSynth-mpeg2Deblock.slnx` `852cc033e098a6d39afee9414053fce6401541157d16a49384b871f284c7d525`
- Installed authority documents, **CRLF working form** (verified 2026-10-17):
  - `Stage2_Experiment_Design_v0_7.md` `d754b94869a2c77ee148a41f1ca38e9998f3fdca698fd6090372a300a8bbb787`
  - `S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md` `67893a9acde830079fa382c5f0c62d32fee7d5a13d3eae77930905aa1eaa81d8`
  - `00_PROJECT_STATUS_v0_7.md` `e7d2d422186f66bfe8b199291aa8e1f265c6f14e43f2556a6d8c5db53060f64d`

---

## 5. Stage 1 (frozen) - what the successor needs

### 5.1 The tool and harness

- Command: `ffmpeg -v error -i <clip.mpg> -c:v copy -an -f mpeg2video <scratch.m2v>`, then
  `Mpeg2BlockInspector.exe -b <scratch.m2v> -m <out.idx>`, then
  `python tools\Stage1_Inspector_Analyzer_v0_2.py summary <idx>`, then `vspipe --info` comparing index
  picture types with BestSource `_PictType`. Paths in the BATs: ffmpeg `C:\SOFTWARE\ffmpeg\ffmpeg.exe`,
  vspipe `D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe`.
- **The VapourSynth Python is `D:\TEST\Vapoursynth_x64_R81\python.exe`** (recorded as `sys_executable`
  in the committed S2-I2 evidence). It has NumPy. The system `python` on PATH has never been required
  to have NumPy by this project - every script any BAT previously invoked with plain `python` is
  NumPy-free. Any new NumPy-dependent script run from a BAT should use the VapourSynth interpreter.
- The index is written under a temporary name (`.s1tmp`) and renamed on success; exit 0 success, 1
  failure.
- **Short-read trap:** `getbits.c` `Fill_Buffer()` treats any `read()` shorter than 2048 bytes as end
  of stream, pads, marks the index COMPLETE and exits 0. Under Linux an ffmpeg **pipe** gave a 1-record
  LP index with exit 0; **file input gives the exact accepted bytes**. Always generate via a scratch
  `.m2v` and gate on exact counts. The inspector stays frozen.

### 5.2 Temporary Stage 1 index format (authority: Stage 1 design v0.3 and `02` v0.4)

- 32-byte file header: magic `S1MBIDX1`, `struct.unpack("<8sHHIQII")`, endian marker 0x01020304,
  complete flag bit 0.
- Per output frame: 64-byte record header (magic `FRM1`, size, ordinal, picture type at byte 30, MB
  count as uint32 at offset 40) then **8 bytes per macroblock**.
- File size = 32 + N x (64 + MBs x 8). Records in **display order**, one per output frame. At 720x576
  that is about 13 KB per frame.
- The 8-byte macroblock record is `struct.Struct("<8B")`: transform, coding, q, q_update, cbp,
  motion_type_raw, motion_dir_bits, packed (motion_source in bits 0-1, plus valid / q_inherited /
  pred_derived / dct_read flags). **There are no motion-vector components.** `TRANSFORM = {0: NONE,
  1: FRAME, 2: FIELD}`, `CODING = {1: SKIPPED, 2: INTRA, 3: INTER}`, `PICTURE_TYPE = {1: I, 2: P,
  3: B}`.
- K-07: FRAME/FIELD/NONE = coded residual transform geometry. NONE covers skipped macroblocks and
  non-intra macroblocks with effective CBP 0. Field pictures: the inspector refuses to publish.

### 5.3 Frozen identities and baselines

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

### 5.4 Reference-decoder verifications by Claude (`REFERENCE-mpeg2dec-src.zip`)

| ID | Finding | Source | Level |
|---|---|---|---|
| V1 | Luma placement: field DCT no mid-height seam; frame DCT seam between frame lines 7 and 8 | getpic.c 436-449 | VERIFIED (implementation) |
| V2 | 4:2:0 chroma ignores `dct_type` | getpic.c 467-482 | VERIFIED |
| V3 | Same `quantizer_scale` for all blocks of a macroblock; luma matrices for 4:2:0 chroma | getblk.c 274-276, 443-445 | VERIFIED (implementation) |
| V4 | 4:2:0 chroma field prediction: even chroma lines top field, odd bottom | recon.c 267-286 | VERIFIED; same-field chroma *filtering* remains a design choice |

Other: output only via `Write_Frame()`; `progressive_frame` swapped at getpic.c 768-773; skipped
macroblocks carry stale `macroblock_type`; CBP 0 decodable. Line numbers may drift by one or two.

### 5.5 Sample material and the S2-I3 development pool

**Stage 1 formal clips** (VALID: frame counts = BestSource, I/P/B match):

| Clip | Size | Scan | FIELD/FRAME/NONE % | QP median (max) | Role |
|---|---|---|---|---|---|
| `LG_576i_3_LP` | 720x576 | interlaced | 52.7/23.0/24.3 | 18 (112) | S2-I3 development |
| `LG_576i_4_EP` | 352x576 | interlaced | 76.2/9.7/14.1 | 14 (112) | **locked hold-out to S2-I8** |
| `TEST_4A_A003` | 720x576 | interlaced | 68.7/19.5/11.8 | 14 (36) | **locked hold-out to S2-I8** |
| `TEST_2A_A001` | 704x576 | interlaced | 6.2/59.2/34.7 | 12 (80) | **locked hold-out to S2-I8** |
| `LG_576i_5_MLS` | 352x288 | progressive | 0/85.4/14.6 | 10 (62) | control |

**The ratified S2-I3 development pool (Stage 2 v0.7 section 6.3, S2-I3 v0.3):** four content groups,
original and `_blocky` each, eight sources in all.

| Group | Original | Blocky | Size | Q_fixed (all-MB median) |
|---|---|---|---|---|
| XP | `LG_576i_1_XP` | `LG_576i_1_XP_blocky` | 720x576 | 14 / 62 |
| SP | `LG_576i_2_SP` | `LG_576i_2_SP_blocky` | 720x576 | 16 / 62 |
| LP | `LG_576i_3_LP` | `LG_576i_3_LP_blocky` | 720x576 | 18 / 62 |
| 3A | `TEST_3A_A002` | `TEST_3A_A002_blocky` | 704x576 | 14 / 62 |

- **Leave-one-content-group-out cross-validation**; the final K0 is fitted on all eight. Arms O/X/J,
  with L/LB on the XP/SP/3A folds only. **2:1 original:blocky weighting within each group.**
- S2-I3 is **fixed-QP only**; S2-I4 has the two QP estimands.
- The MLS pair is a control. EP, 2A, 4A and their `_blocky` copies stay **locked until S2-I8**.
- Measured transform mix of the development originals (verified; see 7.7 for why it matters):
  XP 70.9 FIELD / 12.1 FRAME / 17.0 NONE; SP 73.4 / 5.9 / 20.8; LP 52.7 / 23.0 / 24.3;
  **3A 7.6 / 67.9 / 24.5**. The LG captures are FIELD-dominated; 3A is FRAME-dominated. **Opposite
  regimes** - direct support for the owner's breadth requirement.
- All `_blocky` encodes are **Q62**, a single extreme operating point; at that QP block interiors are
  effectively flat. Intermediate-QP re-encodes (around Q25-Q40) have been suggested for S2-I4 but are
  **not adopted**, and correlated variants of the same content are not independent samples.
- `LG_576i_5_MLS_blocky` is **352x288 with `progressive_frame=0`**, so the MLS pair cannot be used for
  paired metrics without resampling. Always check that a pair's two encodes agree on frame count and
  geometry; this is the trap to look for.

### 5.6 The 2026-10-17 sample additions (verified)

The owner added twelve files, then removed eight after this chat showed they were renamed copies -
sizes identical and the original stem embedded in each name - including `TEST_9A_LG_576i_4_EP`
(the **EP hold-out**) and `TEST_8A_LG_576i_5_MLS` (the MLS control). Admitting those would have
destroyed the hold-out irrecoverably.

After removal, a SHA-256 grouping over `VHSC_samples\*.mpg` returned **20 files with 20 distinct
hashes, no duplicate group** (owner-run, relayed). Content hash prefixes of the genuinely new
material: `TEST_6A_home_576i` `0F8656F69591EC69`, its `_blocky` `0D53680AB8037FDA`,
`TEST_7A_home_576i` `C68E209FDE087D7A`, its `_blocky` `17ABBC2C4EEB85AF`.

These two pairs are **tracked (since `6b7acc3`), outside the P0 allow-list, and carry no experimental
role.** They
are roughly 5-7x longer than anything in the pool (20.5 MB and 12.4 MB against about 3 MB), so expect
indexes of 10-20 MB and proportionally longer runs, and note that unnormalised weighting would let
`TEST_6A` outweigh all four existing groups combined.

The `TEST_nA_` naming scheme is now partial (2A, 3A, 4A, 6A, 7A exist; the five `LG_576i_*` clips keep
their names; 1A, 5A, 8A, 9A, 10A unused). Harmless, because **protection and fold membership follow
content, not filename**. Any future renaming must be a rename, not a copy.

---

## 6. Authority and status files at `82ba3e1`

| File | State |
|---|---|
| `docs/REPOSITORY/00_PROJECT_STATUS_v0_7.md` | RATIFIED 2026-10-17; concise current-state index, not a competing authority |
| `docs/REPOSITORY/05_DECISIONS_v1_2.md` | RATIFIED 2026-10-13; D-01..D-26 |
| `docs/REPOSITORY/06_DEBLOCK_CONCEPT.md` | **v1.3 RATIFIED 2026-10-18**, installed `82ba3e1` in place under its unsuffixed name, which D-23 v1.2 did not provide for (12.3); **K-01..K-11 and O-01..O-15** unchanged in mechanism. v1.3 adds only bounded evidence annotations to K-03/K-07/K-08 in a new section 3.1, including that "inherited" means from earlier pictures of the same encoded stream |
| `docs/REPOSITORY/S2_I3_P0_Evidence_and_Gate_Report_v0_1.md` | **RATIFIED 2026-10-18**, installed `e7cf449`. The durable record of the P0 gate, the raw-audit attribution, both 3A control figures with 610 and 289 mismatches correctly assigned, and the corrected empirical annexes transferred from the `interim_` bridge |
| `docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md` | v0.4: constraints C-1..C-5 ratified; packing frozen only at Stage 3 |
| `docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md` | RATIFIED; Stage 1 PASS |
| `docs/REPOSITORY/Stage2_Experiment_Design_v0_7.md` | **RATIFIED 2026-10-17**; supersedes v0.6 |
| `docs/REPOSITORY/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md` | **RATIFIED 2026-10-17**. Its `Q_fixed` values are now independently CONFIRMED by the P0 diagnostics (7.8). Cosmetic staleness only: the Role column still reads "admission pending" for SP and 3A |
| `docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md` | Committed `4636c33`; 681 lines, byte-verified. **TEMPORARY preservation bridge, not authority.** Its section 9 is the transfer/retirement checklist. Route A's report and concept installs are done (`e7cf449`, `82ba3e1`); it stays load-bearing until both role handovers are installed and the transfer matrix is recorded (12.1). **It is correct: a v0.3 Claude review claim that it conflated scopes was withdrawn (11, 7.8)** |
| `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_4.md` | Operational checkpoint, ChatGPT family, drafted by Claude at owner request and then cross-reviewed editorially by ChatGPT. Correct content installed at `584f5dd` |
| `docs/Claude_P0_EVIDENCE_REVIEW_AND_GATE_RECOMMENDATION_v0_5.md` | Claude's comprehensive P0 evidence review; verdict ACCEPTED, gate PASS recommended. An independent evidence source, **not** the S2-I3 Evidence and Gate Report, which was written separately, cites it, and is installed at `e7cf449` |
| `docs/REPOSITORY/S2_I2_Evidence_and_Gate_Report_v0_1.md` | RATIFIED; S2-I2 registration PASS |
| `NOTICE.md` | licence scope and Restricted Media (including the AI exception) |
| `README.md` | public summary; release link to `v0.1.0` |

**Read `06_DEBLOCK_CONCEPT.md` early.** Its K items are the knowledge that stops a successor
rediscovering what is already settled - see 2.3 for why that matters. In particular:

- **K-02** luma transform organisation varies **per macroblock** between frame and field DCT in
  suitable frame pictures.
- **K-03** horizontal luma transform seams: a frame-DCT macroblock has an **internal** seam plus
  macroblock-edge seams; a field-DCT macroblock has **macroblock-edge seams only**. RESEARCHED
  (H.262) + VERIFIED (reference decoder, V1).
- **K-04** 4:2:0 chroma does **not** follow the per-macroblock luma `dct_type`.
- **K-07** FRAME/FIELD/NONE is applicable coded residual transform geometry; `NONE` includes skipped
  macroblocks **and** non-intra macroblocks with effective CBP 0, where a `dct_type` bit may still
  have been read. `NONE` is **not** a synonym for SKIPPED.
- **K-08** motion compensation can copy blocking off the current transform grid, bounding what a
  current-grid post-filter can target. HYPOTHESIS supported by RESEARCHED evidence.
- **K-11** 4:2:0 field prediction reconstructs chroma with alternating field parity by line.
- The same section states that the internal **vertical** transform seam lies at **luma x=8 and does
  not depend on frame versus field DCT**, and that any multi-row decision or activity measure must use
  field-parity-aware access on interlaced material.
- **O-04** filtering policy for outer edges touching `NONE` is open; **O-08** field pictures;
  **O-14** which operations need parity-aware access.

---

## 7. Technical understanding for Stage 2

### 7.1 Geometry (`06` v1.2)

- Per 16x16 luma macroblock, frame picture: macroblock edges always candidate locations. FRAME and
  FIELD add the internal vertical seam at x = 8. Only FRAME adds the mid-height horizontal seam
  (between frame lines 7|8). **NONE: no internal seam in either orientation; outer edges only.**
- Support rule: a correction for one seam must not cross another known seam. Vertical: FRAME about 4
  samples per field, FIELD and NONE about 8. Horizontal: FRAME/FIELD 8, NONE 16. Chroma 4 per field.
- Chroma 4:2:0: one 8x8 block per plane per macroblock on a fixed grid; luma `dct_type` does not apply
  (V2, K-04); same QP (V3); parity premise verified (V4, K-11).
- Off-grid, prediction-propagated blocking bounds any grid-based post-filter; report I/P/B separately.

### 7.2 Stage 2 design (v0.7; read the file for exact wording)

- Question: given authoritative indexed geometry and QP, what filtering gives useful luma and chroma
  deblocking without unacceptable damage, and which index metadata does the final filter need?
- Prototype: Python 3 (64-bit), VapourSynth/BestSource, NumPy, serial runs; home `experiments/stage2/`.
- Leading B pictures output before the first I picture are excluded from quality evidence (still
  processed and validated).
- Ladder: unfiltered baseline -> indexed geometry + fixed clip-median QP (K0) -> same with real per-MB
  QP -> kernel/threshold/strength development -> NONE policy N0 -> bounded chroma C0/C1/C2 -> hold-outs
  -> transcode reporting -> gate.
- Increments: S2-I1 reader/validation **(done)**; S2-I2 seam maps + registration **(done)**; S2-I3
  K0 on the full eight-source pool **(in progress)**; S2-I4 fixed versus real QP; S2-I5 kernel;
  S2-I6 NONE N0; S2-I7 chroma; S2-I8 hold-outs; S2-I9 transcode reporting; S2-I10 gate report.
- Gate: the owner decides; no preset numeric threshold; ends with a metadata-retention list for Stage 3.
- **Section 15** covers paired-reference metrics; **section 6.3** the S2-I3 admission scheme.

### 7.3 Review watch points for Stage 2 code

Scripts print the files they read; OFF bit-exact; no correction crosses another seam; hold-outs not
viewed during tuning; registration established before any quality conclusion; frame ordinals match
BestSource; generated files written to scratch paths, never over tracked baselines.
**Claude runs any script it can before the owner does**, and states what it could not run.

**Windows CMD cannot be executed here.** Every BAT therefore gets a line-by-line audit in addition to
Linux rehearsal of the commands it calls:

- no two processes appending to the same file at the same time (an S2-I1 v0.1 BAT piped ffmpeg
  `2>>log` into the inspector `>>log`; CMD failed with a sharing violation while Linux allowed it);
- no digit directly before `>`/`>>` (`echo code: %rc%>>log` with `rc=0` becomes handle 0; write
  `>>"%log%" echo ...`);
- **no unescaped `(` or `)` inside a parenthesised block's echo text.** This was a real MUST on
  2026-10-17: `if errorlevel 1 (echo ERROR: problem (not a gate failure)& exit /b 2)` has its block
  closed by the inner `)`, leaving `& exit /b 2)` to be parsed separately, so the exit code on that
  failure path is unreliable. Quoted paths containing parentheses are safe;
- **`for /f` does not set ERRORLEVEL from the command it runs.** An `if errorlevel 1` after a
  `for /f` capture is dead code. Clear the target variable with `set "x="` first (because `setlocal`
  inherits the caller's environment) and gate on `if not defined x`;
- quoting, `^` carets, `%ERRORLEVEL%` captured on its own line outside blocks, `if errorlevel 1` after
  the right command (`setlocal enableextensions` resets ERRORLEVEL to 0);
- every `exit /b` should print a reason: a silent exit in a guided step-by-step run is baffling;
- compare every redirection with the accepted `TESTING` BATs, not only the command line;
- `--info` / `--arg` vspipe forms as in the accepted BATs; certutil SHA-256 checked with
  `findstr /i /c:`.

### 7.4 S2-I1 - complete

Reader and validation v0.2, committed `4221f7f`, status v0.5 `2286341`. Files:
`stage2_index_reader_v0_2.py`, `stage2_index_reader_regression_v0_2.py` (six baselines: SHA-256 then
analyzer totals, plus negative tests), `stage2_validate_bestsource_v0_2.vpy`,
`S2_I1_validate_all_accepted_pairs_v0_2.bat`, `S2_I1_generate_4A_blocky_candidate_v0_2.bat`.

The regression prints `EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent...` when that
non-baseline index is missing. **That line is expected, not an error** - it will appear in every
S2-I3 P0A run too.

Verified facts: leading-B ordinals are LP/EP/MLS `[0, 1]`, none for 2A/2A-blocky/4A/4A-blocky; mixed
FRAME/FIELD frames LP 198, EP 215, MLS 0, 2A 263, 2A-blocky 300, 4A 299, 4A-blocky 300.

**FFmpeg QP side data** (owner query, closed; informational): BestSource never enables
`export_side_data=venc_params`, so O-01 is answered - not via BestSource. PyAV does expose
`AVVideoEncParams` whose per-MB QP equals the index `q` for every MB in 2033/2040 frames across all 7
clips. It does not replace the index (no FRAME/FIELD/NONE).

### 7.5 S2-I2 - complete, gate PASS

Code committed `190bd06` (nine files); evidence, gate report and status v0.6 committed `6e7b5c5`
(40 A / 1 M / 1 D, the M being `.gitattributes`).

- **Registration gate PASS on LP and LP_blocky.** Evidence lives in
  `experiments/stage2/results/S2_I2_v0_1/{LP,LP_blocky}/`.
- BestSource and FFmpeg produced **byte-identical CSVs**: strong evidence of decoder agreement, **not**
  pixel-by-pixel proof. An earlier Claude verification overstated this and was corrected in v0.2 of
  that document. Keep the weaker, accurate wording.
- **M4 discrepancy, resolved:** the engine is correct at 23.79%. An earlier 47% preview had used
  adjacent-slope comparators; that variant is recorded as the separate proposal **M4a**.
- `stage2_registration_stats_v0_1.py` is **generic** (any MB-aligned size, leading B, 704 width) and is
  reused unchanged by S2-I3. The S2-I2 *adapter* and *BAT* are not reusable: the adapter hard-codes its
  label as `'LP_blocky' if stem endswith '_blocky' else 'LP'`, and the BAT accepts only LP/LP_blocky.
- `stage2_check_result_v0_1.py` must **not** be used as an S2-I3 gate.
- The S2-I2 thresholds are **diagnostic only** in S2-I3. On the eight development sources they report
  PASS for XP, XP_blocky, LP, LP_blocky and 3A_blocky, and BLOCKED for SP, SP_blocky and 3A - because
  of test preconditions, **not** misregistration. This is exactly why S2-I3 needed a different
  admission test.

### 7.6 S2-I3 - the design, the admission method and the P0 clearance (execution is in 7.8)

**The admission problem.** S2-I2's phase-contrast gate cannot admit the wider pool (7.5). S2-I3 v0.3
therefore adopts an **exact P-skip identity** admission test, which this chat proposed and proved.

**P-skip identity registration proof.** In an MPEG-2 **frame P picture**, a macroblock the index marks
SKIPPED is reconstructed by forward frame prediction with a **zero** motion vector and no residual.
There is no in-loop filter. Therefore its 16x16 luma must equal the co-located block of the
**immediately preceding I or P picture in display order**, bit-exact. Properties:

- a single mismatch is a hard FAIL - there is no threshold to tune;
- it detects spatial misregistration **and** temporal slips;
- a **field swap remains undetectable** by it; note that limitation.

**Rehearsal (verified, real `vspipe` + BestSource):** 100% exact on all eight development sources,
every control below 100% (highest 96.7%, 3A `previous_display`).

| Source | Exact P-skips | P pictures | Source | Exact P-skips | P pictures |
|---|---|---|---|---|---|
| XP | 1619/1619 | 54 | XP_blocky | 25635/25635 | 55 |
| SP | 1764/1764 | 46 | SP_blocky | 19010/19010 | 46 |
| LP | 1533/1533 | 46 | LP_blocky | 20300/20300 | 50 |
| 3A | 8812/8812 | 133 | 3A_blocky | 18190/18190 | 73 |

Negative rehearsals all FAIL: swapping an encode's index with its pair's (8.7% and 34.0% exact), a
+/-1 frame slip (80.4%, 84.8%), a 2-pixel shift (71.1%), a 1-line shift (90.2%).

**Pair-correspondence rule** (predeclared by this chat before seeing outcomes, then rehearsed). With
`MAE` the mean absolute difference, `b` blocky and `o` original, candidates k = -2..+2:

- frame N is **decisive** if `min over k != 0 of MAE(o_N, o_{N+k}) >= 2 * MAE(b_N, o_N)`. Because MAE
  is a norm, the triangle inequality makes it impossible for any k != 0 to beat k = 0 in a decisive
  frame when the pair is aligned;
- **PASS** requires equal frame counts (else HARD FAIL), a strict clip-mean minimum at k = 0, **zero**
  decisive-frame violations (else FAIL), and at least 20 decisive frames **and** at least 10% decisive
  (else INCONCLUSIVE).

Rehearsal: all four groups PASS - XP 140/228 decisive, SP 175/192, LP 81/204, 3A 268/300, zero
violations; clip-mean MAE at k=0 of 3.53 / 3.23 / 4.39 / 5.53 against best-other 9.88 / 13.98 / 9.93 /
19.95. Simulated +/-1 slips FAIL on all four, with the argmin moving to the slip and decisive frames
collapsing. **Disclosure to carry forward:** the 20-frame and 10% floors were set after seeing these
numbers; the aligned (42-93%) and slipped (0-1%) regimes are so far apart that any floor between them
behaves identically.

**Scratch index SHA-256 values** (gcc build of the frozen inspector, independently reproduced; the
Windows run must match these):

| Label | SHA-256 |
|---|---|
| XP | `4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127` |
| XP_blocky | `8d0326b5975b19b36742717a80be9eaf11bc21f379f2855eb22651e94dd16b20` |
| SP | `40a97ce1a9920cd63e45da13371e0b41ff1619fed688d6145899a300463cc5d9` |
| SP_blocky | `7e19ca6078075e7bf7a3a34bcda0816267e4d38ad02a56e01b6b0ed726ace746` |
| LP | `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011` (frozen baseline) |
| LP_blocky | `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238` |
| 3A | `9a60a8d24a7e4a45cbe82b4f41d232ede0e5c00624e82a8f8099f61351957f33` |
| 3A_blocky | `e6f556dd4aaed0f4709b7c011fcf045193dccbb8abd2a01c646dddf0da893c83` |
| MLS_blocky | `915bee8ce95ea9fa58d283b38ba445427a7ab7402ee15e71e6c9dd38ab46d1da` |

**P0 code state.** Fifteen files for `experiments/stage2/`: seven CRLF BATs (`P0A_prepare_campaign`,
`P0B_copy_LP_blocky`, `P0B_generate_index`, `P0C_admit_source`, `P0D_diagnostics`, `P0D_pair`,
`P0D_summary`) and eight LF `.py`/`.vpy` files (`stage2_i3_pskip_core_v0_1.py`,
`stage2_i3_pskip_tests_v0_1.py`, `stage2_i3_pair_correspondence_v0_1.py`,
`stage2_i3_pair_tests_v0_1.py`, `stage2_i3_preflight_verdict_v0_1.py`,
`stage2_i3_admission_clip_v0_1.vpy`, `stage2_i3_diagnostic_clip_v0_1.vpy`,
`stage2_i3_pair_clip_v0_1.vpy`). None collides with an existing repository file.

History: candidate v0.1 reviewed 2026-10-17 - **one MUST** (the CMD parenthesis, 7.3) plus S1-S3 and
six OPTIONALs; revised candidate diff-checked the same day and **CLEARED**, with one further SHOULD
(S4: run the two new NumPy-importing test suites under the VapourSynth Python, 5.1). All Python and
VPY files are byte-identical between the two candidates, so the rehearsal evidence above carries
forward unchanged.

The admission allow-list in `stage2_i3_preflight_verdict_v0_1.py` is **pure data** - label, stem,
index SHA-256, frame count, geometry, reference P-skip count - so extending the pool later is a
`v0_2` of that one file plus hashes, with no logic change. It is **fail-closed** against any other
name: `argparse` rejects unknown labels and both adapters require the source basename to equal the
allow-listed stem exactly (verified by trying `EP` and `4A_blocky`).

### 7.7 Measurements from 2026-10-17, and a correction to carry forward

This chat measured the paired original/blocky relationship and the transform geometry. **Read 2.3
first**: most of the mechanism below is already K-02, K-03 and K-07, and the value here is
confirmation on real project material, not new knowledge.

**Per-macroblock geometry, confirmed in decoded pixels.** Using each blocky encode's own index to
label every pixel by its macroblock's transform state, luma only, all frames, comparing against the
original:

| Group | MB state | H-seam excess (MB rows 7,8) | V-seam excess (MB cols 7,8) |
|---|---|---:|---:|
| XP | FRAME | +19.5% | +23.4% |
| XP | FIELD | +3.2% | +24.2% |
| SP | FRAME | +16.2% | +20.5% |
| SP | FIELD | +3.3% | +25.5% |
| LP | FRAME | +17.3% | +22.6% |
| LP | FIELD | +2.7% | +23.4% |
| 3A | FRAME | +12.8% | +16.5% |
| 3A | FIELD | +2.3% | +19.1% |

At the **same pixel rows**, FRAME-DCT macroblocks show four to eight times the excess of FIELD-DCT
macroblocks - exactly what **K-03** predicts. The vertical seam is present in both states with no
systematic difference, confirming the ratified `x=8` independence. Absolute MAE is much higher in
FIELD regions (field DCT is chosen where vertical-temporal activity is high), so **only within-state
excess is comparable**; never compare absolute values across states.

**The correction.** An earlier Claude analysis (v0.2, uncommitted) put the boundary excess at only
7-10% and concluded that paired MAE is a weak objective. That measurement used a frame-line 8-pixel
grid, which is correct **only** for FRAME-DCT macroblocks, and three of four sources are
FIELD-dominated - so the band was placed where no seam exists for most macroblocks. Correctly
located, the signal is two to three times larger. **The surviving, narrower claim:** a
geometry-*blind* global MAE is diluted by irrecoverable interior detail loss, but a geometry-*aware*,
seam-localised paired measure has a healthy signal. Do not carry the stronger pessimistic claim.

**Interlace is the dominant practical trap.** A naive frame-based vertical blur lost 7.5% to 26.8% of
paired MAE and **damaged a clean original by up to 2.244 MAE** - comparable to a large part of the
entire blocky-versus-original gap of 3.5 to 5.5. On 576i, vertically adjacent frame lines are
different fields, hence different moments. Vertical processing must be within-field or driven by the
per-macroblock transform flag. Note also that **FRAME DCT is an encoder rate-distortion choice, not a
guarantee that the two fields are temporally similar**, so it is never by itself permission to filter
across frame lines.

**A falsifiable prediction worth testing in S2-I4.** The vertical seam is at `x=8` regardless of
transform type, so its geometry needs no index; the horizontal seam pitch is knowable only from the
per-macroblock state. **Prediction: index-driven geometry adds most of its value on horizontal seams
and little on vertical ones.** Direction-separated scoring measures this at no extra cost.

**Transform-state transitions between adjacent macroblocks** (coded-pair denominator, meaning both
sides carry FRAME or FIELD; `NONE`-involving pairs excluded from numerator and denominator - state
this whenever quoting the figures). Side-by-side pairs share a **vertical** boundary; stacked pairs
share a **horizontal** boundary:

| Source | Vertical bdy, % of coded pairs | Horizontal bdy, % of coded pairs | Horizontal, % of all pairs |
|---|---:|---:|---:|
| XP | 15.5 | 15.7 | 11.4 |
| SP | 8.2 | 8.5 | 5.8 |
| LP | 23.6 | 24.0 | 15.3 |
| 3A | 9.2 | 10.0 | 6.9 |

92.3% to 99.5% of frames contain **both** FRAME and FIELD macroblocks, so no global geometry
assumption can be correct.

**`NONE` composition, as a percentage of `NONE` macroblocks** (new measured support for **K-08**):

| Source | SKIPPED in P | SKIPPED in B | INTER CBP=0 |
|---|---:|---:|---:|
| XP / XP_blocky | 2.6 / 9.4 | 37.4 / 26.9 | 60.0 / 63.7 |
| SP / SP_blocky | 2.7 / 9.0 | 35.0 / 27.2 | 62.3 / 63.7 |
| LP / LP_blocky | 1.9 / 8.4 | 29.6 / 23.2 | 68.5 / 68.4 |
| 3A / 3A_blocky | 7.6 / 6.4 | 14.4 / 25.9 | 78.0 / 67.8 |

Only **SKIPPED in P** is guaranteed zero-motion-vector and therefore co-located; INTER CBP=0 can carry
a non-zero vector, and a B-picture skip reuses the previous macroblock's vectors. So the guaranteed
grid-aligned share of `NONE` is just **1.9% to 9.4%**: between 90% and 98% is potentially off-grid
inherited content, making K-08's concern the dominant case rather than a corner case. Note too that
prediction uses fractional-pixel interpolation, so inherited blocking is interpolated, not rigidly
displaced - and the index carries **no motion-vector components** (5.2), so it cannot locate the
inherited grid. Any proposal to capture vectors meets D-13's higher bar; Stage 1 stays frozen.

At Q62 the blocky encodes become `NONE`-dominated (XP 17.0% `NONE` as an original, 73.7% as blocky).

### 7.8 S2-I3 P0 - executed, reviewed, and RATIFIED PASS by the owner (2026-10-18)

**Gate status: PASSED, ratified by the project owner on 2026-10-18**, on the evidence and review
summarised below. This closes the S2-I3 P0 registration gate. It unblocks the seven-index tracking
commit and nothing else: **P1 still requires a separate explicit owner authorisation**, and a
numerical `READY_FOR_P1=true` was never that authorisation either. The limitations at the end of this
subsection travel with the ratified result and are not waived by it.

**Execution is complete and must not be repeated.** P0A PASS after the isolated-Python fix; P0B six
generated indexes plus the LP_blocky byte copy, with LP original reused frozen; **P0C 8/8 REGISTERED**;
**P0D descriptive diagnostics 8/8 COMPLETE**; **P0D pair correspondence 4/4 PASS**; global summary run.
Every index SHA-256, frame count, geometry, exact P-skip count and qualifying P-picture count matched
the references this role published *before* the Windows runs existed (7.6). The scripts refuse to
overwrite existing output, so a re-run at best fails and at worst damages the evidence.

**Claude's review recomputed the two headline results rather than trusting reported verdicts.**
Admission identity was re-summed from `per_P_picture` for all eight sources; the decisive rule was
re-evaluated over all **908 evaluated frame records, of which 664 are decisive** (140 + 175 + 81 + 268
against common interiors 224 / 188 / 200 / 296). Both reproduce exactly, with no per-frame flag
inconsistency. Pair results: XP 140 decisive, mean MAE at k=0 3.5250 against best competitor 9.8761;
SP 175, 3.2322 / 13.9828; LP 81, 4.3876 / 9.9337; 3A 268, 5.5276 / 19.9471. Zero decisive violations
throughout, strict k=0 argmin in all four, both sample-size floors met with margin (tightest LP at 81
frames and 39.7%).

**The threshold-free design is vindicated by the owner's own run, and this is the strongest single
result in the evidence set.** A one-pixel *horizontal* shift of 3A (`-1,0`) still reproduces **93.08%**
of its skipped-macroblock blocks exactly; previous-display reaches 96.72% on 3A and 94.85% on LP. Any
tolerance-based registration test below roughly 93% would have **passed a misregistered 3A**. In
absolute terms on 3A the true position has 0 non-matching blocks of 8812; the `-1,0` spatial control
has **610** (8202 of 8812), and the strongest control of any kind, the wrong `previous_display`
temporal hypothesis at 96.72%, has **289** (8523 of 8812). v0.12 and review v0.5 said only "289 for
the best competing hypothesis" beside the 93.08% figure; that is strictly true of `previous_display`
but invited the misreading that 289 belonged to `-1,0`, and the Evidence Report draft made exactly that
error before Claude caught it. Always name the hypothesis with its mismatch count. **This does NOT supersede the `interim_` document's 90.2% figure** (its section
11), which is a whole-clip *vertical* one-line injected fault from the Linux rehearsal - a different
fault with a different qualifying population. Carry BOTH with their mechanisms named; today's vertical
per-block controls were 77.22% and 28.86%, which do not contradict the injection result.

**Integrity properties worth preserving.** The media hash chain is closed: each admission
`source_sha256` equals the corresponding pair-test `original_sha256`/`blocky_sha256`, so the pair
tests provably ran on the admitted bytes. All eight media hashes are distinct - the duplicate-sample
failure mode that nearly cost the EP hold-out is clean on this run. Runtime is byte-identical across
all eight admissions (R81, BestSource `PluginVersion(22,0)`, DLL `fa5b9016...f69c` equal to accepted
S2-I2, adapter `154c9046...aa41`, Python 3.14.8, NumPy 2.5.4 against 2.5.3 in S2-I2). A sweep of all
137 evidence files for protected and non-allow-list media returned **zero hits**.

**Two ratified parameters independently re-derived** from the diagnostic CSV strata, which is worth
more than a value that only appears once: `Q_fixed` reproduces exactly for all eight sources (XP 14,
SP 16, LP 18, 3A 14, every blocky single-valued at 62), and the transform mix confirms within 0.1 to
0.8 percentage points including 3A's opposite FRAME-dominant regime at 68.3%. Caveat: the derivation
is boundary-pair weighted, not a strict all-macroblock census, so exact agreement on all eight is a
stronger result than the method guarantees.

**The original/`_blocky` pair: what it is for.** It is a **controlled appearance and mechanism
instrument** - what blocky seams look like, where they sit relative to the coded grid, and what the
undamaged content was at that location, with frame correspondence now *demonstrated* rather than
assumed. That is the only way to separate damage from real detail, and a real poor capture with no
clean twin can never answer it. It is **not a population sample** of real-world blocking: the blockys
carry a coded transform in only 26 to 40% of macroblocks against 75 to 83% in the originals, at a
constant `quantiser_scale` 62 that is not real rate-control behaviour, so **never tune frequency
thresholds, prevalence estimates or severity distributions on blocky statistics**. Blocking in the
blockys is transcode-created, not carried over from the originals: every blocky I picture is 100%
INTRA at scale 62, and blocky P pictures carry a far higher INTRA share than their originals (XP 0.1%
to 19.4%, SP 0.1% to 32.3%, LP 2.0% to 12.5%; 3A falls 25.4% to 21.1%).

**Scope care with SKIPPED figures.** The `interim_` section 7 table decomposes NONE into *Skipped in
P*, *Skipped in B*, *INTER CBP=0* and *Other*. Its 1.9 to 9.4% range is the **Skipped-in-P column
alone**, correctly described as the guaranteed zero-motion co-located portion. Total SKIPPED is the
first two columns summed, 20 to 41% of NONE, and that agrees with the P0 census. State which scope is
meant.

**Four SHOULDs, all carried into the ratified Evidence and Gate Report (`e7cf449`)** (no MUST against the evidence): S1 carry
both 3A control figures with their mechanisms named and state the floor as at least 93%; S2 define the
`caught` column in `known_bad_offsets.csv` and note its `(0,0)` row is an aligned reference, not a
known-bad case, since 3A reports `row=INCONCLUSIVE` with `caught=True` there; S3 record the
appearance-instrument versus population-sample distinction and the withdrawn claims; S4 before S2-I4,
confirm whether `q_scale_type` is recoverable from the current index.

**S4 in full, because it is a real trap.** All four real captures use the MPEG-2 **non-linear**
quantiser table. `quantiser_scale_code` is 5 bits (1..31) mapped through one of two tables selected by
`q_scale_type`: linear gives `scale = 2 * code`, maximum 62; non-linear reaches 112. LP carries 4.23%
of its macroblock-edge weight above 62, as a clamp spike of **49,113 occurrences at exactly 112**
against 1,518 at 104 - rate-control saturation, above which indexed QP stops discriminating severity.
So a strength mapping monotone in indexed QP treats all clamped content identically, precisely where
damage is worst. And a 62 from the linear table is not the same step size as a 62 from the non-linear
table, so without the selector indexed values cannot be compared across sources. `02_INDEX_FORMAT_SPEC`
records `q` and `q_update`; whether the table selector is stored is **unconfirmed**. A D-13
extra-metadata question to settle before S2-I4, not during it. No effect on P0 (no QP values) or P1
(fixed-QP).

**Limitations unchanged and still travelling with the result:** a field swap is undetectable; an IPPP
stream would be INCONCLUSIVE (not engaged here - maximum previous-display was 96.72%); the two pair
floors were set after seeing preflight data and the disclosure must accompany the rule; luma only, no
chroma registration established; determinism observed for these samples, not proven generally.

---

## 8. Licence and Restricted Media (`NOTICE.md` governs; read it for exact terms)

- Project material AGPL-3.0-or-later; reference-decoder files keep their own notices.
- **Project maintainer** = the owner of GitHub account `hydra3333`.
- **Source Recordings**: recordings expressly included for testing (`VHSC_samples/*.mpg`).
  **Derived Media**: transformed picture/sound content, and visualisations of metadata or measurements
  derived from Source Recordings. **Restricted Media** = both. Index files, hashes, logs, metadata,
  source and purely numerical/text diagnostics are **not** Restricted Media unless they embed it.
- In the repository only as bounded test/evidence/review material during active development.
  Otherwise no copying, upload or transmission, **except** the narrow AI exception: until Development
  Closure the project maintainer may supply Restricted Media to ChatGPT and Claude for this project's
  own development conversations; no training, datasets, publication or post-closure retention.
- **This chat deletes extracted recordings, `.m2v`, `.yuv` and BestSource `.bsindex` caches from its
  workspace after every use, and verifies none remain.** Scratch `.m2v` files generated on Windows are
  Restricted Media and the BATs delete them on success and failure.
- Stage 2 gate-report charts are Restricted Media; keep numbers and text as the durable record.
- The 2026-10-13 history reset was **not** Development Closure; the recordings are intentionally still
  present and authorised.

---

## 9. Things deliberately NOT being done

- No pixel seam detector, no Family B, no existing-filter yardstick (D-24 and owner ruling).
- No CSV index output; no field-picture filtering yet; no damaged-stream or multi-sequence support yet.
- No runtime AVX2 detection or non-AVX2 build; no Spectre mitigation; no x86 builds.
- No six-index runs in CI; no PDB retention beyond Actions artifact expiry.
- No wheel/PyPI until Stages 7-9; **no motion-vector capture and no `.idx2` commitment** without
  evidence meeting D-13's bar; Stage 1 stays frozen.
- No editing of ratified files in place: a revision is a new versioned file (D-23 v1.2). **`06` v1.3 was
  nonetheless installed in place at `82ba3e1`** (12.3). No `superseded/` folder; no `*.md eol=crlf` pin.
- **No new standalone knowledge document** merely to hold measurements (D-05; 12.7).
- **No admission of `TEST_6A`/`TEST_7A` through the current eight-source allow-list.**
- No filtering until the owner separately authorises P1. P0 is ratified PASSED, but neither that nor
  `READY_FOR_P1` is authorisation.
- No Stage 2 increment beyond the one authorised without the owner's explicit authorisation.
- The characterisation BAT `S2_I3_P0B_characterise_new_source_v0_1.bat`, drafted by ChatGPT, is
  **stood down** and must not be installed or run. The media are committed (`6b7acc3`); Claude
  characterises the new pairs directly only when the owner asks.

---

## 10. Claude documents (this role)

Committed provenance in `docs/` (identity-scrubbed): prior art + addendum; codec-mechanics review;
source-comparison review; Stage 1 design, patch/first-run and gate-report reviews; chroma discussion
review; questions after handover; reconciliation after handover; repository drafts v1.1 review;
Stage 2 v0.2 reviews; migration proposal review; StageC MSBuild review; S2-I1 candidate v0.1 and v0.2
reviews; S2-I2 design plan v0.2/v0.3/v0.4 reviews; S2-I2 implementation review; S2-I2 closure/entry
review; `Claude_VERIFICATION_OF_S2_I2_Windows_Run_v0_2.md`; `Claude_S2_Seam_Pixel_Test_Options_Table_v0_2.md`;
`TESTING/show_source_clip_info*.vpy`.

**Route A reviews, delivered 2026-10-18, NOT committed** (the owner holds them, two of them untracked
under `experiments/S2-I3/`; they are review correspondence and must not be staged):
`Claude_REVIEW_OF_Route_A_Transfer_Packet_v0_1_v0_1.md` (report and concept candidates: two MUSTs,
the 289/610 error and install-time wording); `Claude_DIFF_CLEARANCE_Route_A_Install_Copies_v0_2_v0_1.md`
(both install copies cleared, with the date and install-order conditions both later met);
`Claude_REVIEW_OF_ChatGPT_Handover_v0_10_v0_1.md` (ChatGPT handover v0.10, four MUSTs);
`Claude_DIFF_CLEARANCE_ChatGPT_Handover_v0_10_Rev2_v0_1.md` (its second candidate: content cleared).

**Committed 2026-10-18 in `docs/`:** `Claude_P0_EVIDENCE_REVIEW_AND_GATE_RECOMMENDATION_v0_5.md` (the
comprehensive P0 evidence review; `1 A / 0 M / 0 D` at `03edabf`, with v0.3 and v0.4 wrongly swept in
and removed again at `584f5dd`). Claude also drafted, at owner request, the ChatGPT-family operational
checkpoint `docs/HANDOVER/S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_4.md`, which ChatGPT then
cross-reviewed editorially; **that document and status v0.3 before it are the weakest-reviewed items
in the tree, because their author is the project's reviewer.**

**Delivered 2026-10-15/17, not in the repository** (the owner holds them). The S2-I2 set:
closure-note v0.2 review; closure v0.3 + Step B v0.2 review (includes the Copilot scan); closure v0.4
+ Step B v0.3 review; Step B final-documents review; `Claude_Step_B_install_wording_corrections_v0_1.diff`;
Claude-corrected install copies of `S2_I2_Evidence_and_Gate_Report_v0_1.md` and
`00_PROJECT_STATUS_v0_6.md`; and `S2_I2_Step_B_stage_v0_1.py`, a staging script that verifies HEAD and
hashes, extracts 25 evidence files, appends the `.gitattributes` pin, runs `check-attr`, stages 41
paths plus a `git rm`, and asserts 40 A / 1 M / 1 D and blob identity - it never commits. The S2-I3
set: full-data design v0.1 review; v0.2 + Stage 2 v0.7 review (introduced the P-skip proof); v0.3 +
Stage 2 v0.7 revision review; final-wording clearance; ratified-document install review with
`Claude_S2_I3_Install_Wording_Corrections_v0_1.diff` and three corrected install files; implementation
plan v0.1 review (P0 plan cleared with SHOULD S1-S6).

**Delivered 2026-10-17:**

| File | Content |
|---|---|
| `Claude_REVIEW_OF_ChatGPT_S2_I3_P0_Candidate_v0_1_v0_1.md` | P0 candidate v0.1: one MUST, S1-S3, O1-O6; full rehearsal evidence |
| `Claude_ANALYSIS_OF_Paired_Reference_Metric_and_Sample_Pool_Extension_v0_2.md` | paired-metric analysis and the sample-pool MUST. **Carries the mis-located-band error** (7.7); do not quote its boundary/interior figures. A corrected v0.3 was offered |
| `Claude_REVIEW_OF_ChatGPT_Stage2_Interim_Findings_v0_1_v0_1.md` | four MUSTs, three of them corrections to Claude's own material |
| `Claude_P0_REVISED_CLEARANCE_AND_PROJECT_STATE_OF_PLAY_v0_1.md` | P0 revised candidate CLEARED, plus a consolidated state-of-play and supersession ledger |

Useful ChatGPT documents: its role handover (latest), `Stage1_Inspector_Instrumentation_Design_v0_3.md`.
`Response_to_Claude_Index_Driven_Ruling_and_Revised_Stage2_Plan_v0_1.md` came from the **wrong Claude
chat** of 2026-10-07: provenance only, kept and scrubbed.

---

## 11. Lessons and traps

- Wrong-chat incident (2026-10-07): if something contradicts the authorities, ask where it came from.
- Do not reconstruct files from memory or summaries; ask the owner to upload them.
- Scripts must print what they read.
- "Done" may not be done: confirm in the source or a clone.
- A candidate file may differ from its own diff: check both.
- LF/CRLF: compare like with like; name the representation when hashing.
- Recorder modes differ sharply (EP half width; MLS progressive SIF; the development pool splits into
  opposite transform regimes). **Never assume one clip represents the archive** - this is the owner's
  stated position and the measurements support it.
- The TESTING BATs regenerate tracked baselines in place (4.6).
- Running ChatGPT's tools against a realistic reconstruction has found every defect that reading
  missed. Keep doing it, and now also run the real `vspipe`/BestSource stack (2.2).
- Quotes marked verbatim must be verbatim. Paraphrases must be labelled.
- Commit metadata is part of identity, including the time-zone offset (12.11).
- Old tags keep old history alive; local-path clones copy every object (use `--no-local`).
- Keep relay pastes short and self-contained; the owner carries them between chats and asks for them
  when missing.
- **A Linux rehearsal does not prove a Windows BAT.** Audit CMD semantics line by line (7.3).
- **Chats end without warning.** Refresh handovers at each milestone, not at the end.
- Frozen-inspector short-read trap (5.1): never trust a piped index without exact count gates.
- When the owner asks a side question, answer it with evidence and do not widen scope.
- **Install-time wording:** a document that says "proposed / pending / not yet ratified" becomes false
  the moment it is installed. This recurred across the S2-I2 report, status v0.6, Stage 2 v0.7, S2-I3
  v0.3 and status v0.7 - every install package needs a wording pass, and Claude has supplied the diffs.
- **Do not use `git diff --cached --check` as a STOP gate** (2.1).
- **Check findings against the existing K/O items before calling them new** (2.3). This is the
  biggest process lesson of 2026-10-17.
- **Fixing a review finding can introduce a new one.** S3 of the P0 review (run the new unit tests in
  P0A) created a NumPy dependency on the system `python` where none had ever existed. Re-review your
  own recommendations as implemented.
- **Before asserting that another document is wrong, incomplete or superseded, re-read the passage
  being characterised - not the topic, the passage.** On 2026-10-18 this role twice criticised correct
  documents from memory while its own numbers were properly verified: it claimed the committed
  `interim_` document conflated scopes (it does not; it decomposes NONE into four named columns and
  agrees with the P0 census), and it claimed a new 93.08% control figure superseded the `interim_`'s
  90.2% (different fault, different axis, different population). Thirty seconds of grep settled both.
  This is the M4 pattern of 2026-10-17 recurring: measure, then describe someone else's document from
  memory.
- **When withdrawing a claim, check the retraction does not reach further than the error.** Having
  correctly withdrawn a claim about the `_blocky` artefact's statistics, this role over-generalised and
  dismissed the original/`_blocky` **pair as an experimental instrument** - which is the backbone of
  the project's evidence design and what D-26 is about. The owner challenged both the original claim
  and the over-correction. Both were right.
- **After being corrected, the next failure mode is over-delivery.** The same session inflated a minor
  observation into a full document section immediately after a correction, to show something real had
  been found. The owner asked whether it was useful; it mostly was not.
- **Check your own prior documents before calling a finding new.** The `NONE`-dominance figure
  presented as a new 2026-10-18 finding was already recorded in v0.10 of this very handover (end of
  section 7). Search this file before claiming novelty.
- **Verify committed CONTENT, not just staged shape.** At `03edabf` the staged shape looked correct
  while the **uncorrected** draft of status v0.4 landed at the authoritative path and the cross-reviewed
  one landed at `docs/` root. Shape checks do not catch swapped content. Where a document's identity
  matters, grep the committed blob for a phrase that only the correct version contains - that is how
  the remediation commit was gated.
- **`git diff --cached --name-status --no-renames` before every commit, without exception.** Three
  successive commits swept in unintended files (`6b7acc3` 58 files, `4636c33` 25, `03edabf` 7) and all
  three were caught only after pushing. The staging step is the one part of the pipeline with no review
  gate in front of it. `166af3a` added `*.zip`, `*.patch` and `*.diff` to `.gitignore`, which would
  have stopped every ZIP that has ever caused a problem here, including all four identity carriers -
  but `.gitignore` does nothing about already-tracked files, so it prevents recurrence and replaces no
  cleanup.
- **Cross-role review earns its cost.** On 2026-10-18 the owner found five substantive errors in this
  role's work and the ChatGPT role found nine more across two documents, including an internal
  contradiction and a wrong staged shape. Every one was editorial or citational; none touched the
  evidence, the recomputations or the verdict. Two documents this role both wrote and would have
  reviewed are the exception that proves the rule.
- **Transferred from `interim_` bridge sections 15 and 16 (bridge retirement condition 3).** v0.12 was
  described by this role as already carrying these sections. **It lacked four of their seventeen
  items**, listed here. The other thirteen were already present elsewhere in this handover: BestSource
  `bsindex` caches, the five CMD traps, the `git diff --cached --check` rule, the `core.autocrlf`
  representation rule with its `139f02c6`/`f9892039` example, the BestSource DLL identity and NumPy
  provenance, and M1 to M4 with their root cause and standing rules.
    - **Embeddable/isolated Python does not add the launched script's directory to `sys.path`, and
      ignores `PYTHONPATH`.** The owner's VapourSynth interpreter is exactly this case
      (`D:\TEST\Vapoursynth_x64_R81\python.exe`, CPython 3.14.8, `python314._pth`,
      `sys.flags.isolated=1`, `sys.flags.safe_path=True`). Under `-I` a plain invocation fails with
      `ModuleNotFoundError` for a sibling module; setting `PYTHONPATH` does **not** fix it; explicit
      `sys.path.insert` is the only route. The cleared P0A fix launches each NumPy-dependent suite
      through `-c` with `runpy.run_path`, prepending the script directory and setting
      `sys.argv=[script]`. **Rehearse every script invocation under `-I` as well as plain before
      clearing it.**
    - **The project's `.vpy` adapters already solve this internally** with
      `HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))`. Adding that idiom to the
      test modules is the more idiomatic long-term fix; it was deliberately not taken mid-run so the
      Python files stayed byte-identical to the rehearsed set.
    - **Fail-closed proof: inject the failing test BEFORE the trailing
      `if __name__=='__main__': unittest.main()` line.** This role's first attempt appended it after, so
      the injected test was defined only after the suite had already run and exited, and the run
      reported success - a false demonstration of fail-closed behaviour. Done correctly, a failing
      assertion, a syntax error and a missing sibling module each give a non-zero exit through
      `runpy.run_path`.
    - **The S4 testing error (bridge section 16).** This role recommended running the new unit tests
      under the VapourSynth interpreter - right in intent - but verified it with absolute-path
      invocation under a **non-isolated** interpreter while recommending one that is isolated by
      default, having already seen `python3 -I` fail with that exact `ModuleNotFoundError` earlier in
      the same session. The owner's P0A then failed closed at rc=2 before creating scratch. **Test the
      deployed invocation, not an equivalent-looking one.**
- **Do not assert coverage you have not grepped.** On 2026-10-18 this role told the owner and the
  ChatGPT role three times that v0.12 carried bridge sections 15-16, and ChatGPT's v0.10 draft relied on
  that assertion in its retirement table. Checking each item by pattern search took one command and
  found four absent. It is the same describe-from-memory failure recorded above for other documents,
  applied to this role's own file - which is where it is least expected and least checked.
- **Sweep for stale state by state-words, not by the phrases you remember writing.** v0.13's own
  stale-claim check searched for the specific old phrases this role recalled, found none, and v0.13
  still said Route A had not happened, that the Evidence Report did not yet exist, that the 6A/7A media
  were uncommitted, and that the takeover delta ran from `35cd543`. The ChatGPT role found three of
  these. A sweep over words like "not yet", "pending", "uncommitted", "does not exist", "has not" and
  every superseded commit ID found them all in one pass, plus four more.
- **Check a proposed install shape against D-23, not only against the content.** `06` v1.3 was proposed
  in place, cleared twice by this role and installed as `0 A / 1 M / 0 D`, although D-23 v1.2 says an
  unsuffixed document adopts a versioned filename at its next actual revision (12.3).
- **Verify a cleanup by listing what survives, not only by counting what was removed.** Commit C was
  checked as exactly 52 deletions of the agreed paths, which it was; nobody listed the files still
  under `experiments/` afterwards, and four leftovers from the same snapshot stayed tracked (12.5).
- **The owner can lose track when several tracks run at once.** On 2026-10-17 he said he was "starting
  to get lost with what I perceived may be forward backtracking". The remedy that worked: separate the
  tracks explicitly, say which one is on the critical path, give a supersession ledger, and state
  plainly that nothing erroneous reached the repository. Offer that unprompted when activity is dense.

---

## 12. Outstanding items and known gaps

1. **Route A, last step.** Bridge retirement needs all four conditions: (a) P0 Evidence and Gate Report
   installed and ratified - **DONE** `e7cf449`; (b) `06` v1.3 installed and ratified - **DONE**
   `82ba3e1`; (c) both role handovers carry bridge sections 15-16 - **this v0.14 does once installed;
   ChatGPT v0.10's content is cleared and its install copy follows**;
   (d) the transfer matrix updated with the actual commit IDs and reviewed. Then retirement is a
   **separate** owner decision by exact-path D-23 removal. Until then the bridge is load-bearing.
2. **ChatGPT handover v0.10.** Second candidate content-cleared by Claude on 2026-10-18. Its install
   copy needs only the install-time wording and this v0.14's version and commit ID, then a diff check,
   the owner's ratification, and `1 A / 0 M / 1 D` replacing v0.9 - **after** this v0.14 is installed.
3. **`06` filename deviation - owner decision.** D-23 v1.2: "existing unsuffixed project documents adopt
   versioned filenames at their next actual revision". `06` v1.3 was installed in place as
   `06_DEBLOCK_CONCEPT.md` instead of as `06_DEBLOCK_CONCEPT_v1_3.md` with v1.2 deleted. ChatGPT
   proposed it and Claude cleared it twice without checking D-23. Renaming now would leave dangling
   the path the ratified Evidence Report cites. Claude recommends the owner **accept v1.3 in place as a
   recorded one-off** and apply the versioned filename at `06`'s next revision (v1.4).
4. **Local untracked v0.13.** It was placed in the owner's `docs/HANDOVER/` but never committed. Delete
   the local file; do not stage it. v0.14's install deletes the tracked v0.12.
5. **Four leftover files from snapshot `6b7acc3` - owner decision, not blocking.** Commit C removed 52
   review-only paths but not these: `experiments/S2-I3/00_PROJECT_STATUS_v0_7.md`,
   `experiments/S2-I3/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md` and
   `experiments/S2-I3/Stage2_Experiment_Design_v0_7.md` are byte-identical (same blob) to the ratified
   copies in `docs/REPOSITORY/`; `experiments/S2_I2_Closure_v0_3.md` is the superseded closure review
   draft whose header still says "not yet ratified/installed" and "S2-I3 remains NOT AUTHORISED". No
   tracked file refers to any of the four. The duplicates invite a later edit to the wrong copy, and the
   draft reads as live state. Recommended: one separate exact-path commit, `0 A / 0 M / 4 D`, using
   `git rm` on the four paths only (never the folder: the owner keeps untracked review files there).
   Nothing is lost; the ratified copies stay and history keeps all four.
6. **P1 onwards** of S2-I3 only after a separate explicit owner authorisation. A numerical
   `READY_FOR_P1=true` and the gate ratification are neither of them that authorisation.
7. **`Stage2_Interim_Findings_v0_1`**: never cleared, never installed, superseded by the bridge and now
   by the Evidence Report. Do not install it.
8. **The four 6A/7A home recordings** are tracked (since `6b7acc3`) but have **no experimental role**.
   Before any role: Claude verifies the four hashes, generates reference indexes and characterises both
   pairs (frame count, geometry, MB-grid alignment, picture structure, `progressive_frame`,
   `q_scale_type`, Q_fixed, FRAME/FIELD/NONE mix, P-skip counts, pair correspondence), and a design
   revision assigns the role. Which transform regime the home captures fall into is a question of real
   interest (5.5). Their persistence in Git history is an open owner decision for Development Closure.
9. **`q_scale_type` recoverability** (7.8 S4) - settle from the index writer source, not from the record
   layout alone, before S2-I4. The ChatGPT role correctly qualified this role's earlier framing.
10. **All-zero-ties edge case** in the pair rule (Evidence Report section 6): a fully static frame is
   counted decisive and a violation, hence FAIL rather than INCONCLUSIVE. Not engaged in the P0 evidence
   (no record has `mae_at_0 == 0`); review it if the rule is reused on static material.
11. **Owner decision (minor):** commits record the committer's local time-zone offset.
12. Six `VHSC_samples/*.log` kept temporarily; remove when no longer needed.
13. Archive-wide questions still open: field pictures (O-08), recorder modes in the owner's archive,
    matrix effects (O-07), chroma geometry (nothing measured yet - all 7.7 figures are **luma only**).
14. Claude's `ANALYSIS ... v0.2` carries the M3 error; it is uncommitted and its boundary/interior
    figures must not be quoted. The Evidence Report section 13 item 5 now records that prohibition.
15. **Committed as-at records that are now historical:** status v0.4, Claude review v0.5, ChatGPT
    handover v0.9, and the `interim_` bridge's section 10 snapshot. Each was true at its installing
    commit. The owner decided not to re-version them; the Evidence Report carries the ratified gate.
16. Not yet seen by Claude: the fresh `v0.1.0` release page and asset (4.3).
17. Future: Development Closure plan (media removal, history purge including the identity blobs in
    `6b7acc3`, uploads deletion); wheel/PyPI identity at Stages 7-9.

---

## 13. State and next steps

**State at `82ba3e1`:**

- history: root plus twenty-five commits, all verified from GitHub; **215 tracked files, zero ZIPs**;
- ratified authorities: `05` v1.2, **`06` v1.3**, `02` v0.4, Stage 1 report v0.3, Stage 2 v0.7, S2-I3
  v0.3, S2-I2 report v0.1, **S2-I3 P0 Evidence and Gate Report v0.1**, status v0.7;
- **S2-I3 P0 ratified PASSED**; the gate is closed and recorded; **P1 unauthorised**;
- 13 tracked `.idx`: six frozen Stage 1 baselines unchanged, seven development indexes byte-identical to
  the admitted references; all 13 binary-detected;
- current-tree cleanup complete except four leftover files (12.5); the identity blobs remain in
  history until Development Closure;
- the `interim_` bridge is tracked and still load-bearing pending condition (c) and (d) of 12.1;
- hold-outs EP/2A/4A intact and locked to S2-I8; 6A/7A tracked but role-unassigned;
- no filtering has been attempted anywhere.

**Next, in order:**

1. Install this v0.14: `1 A / 0 M / 1 D`, adding it and deleting the tracked Claude v0.12. Delete the
   local untracked v0.13 file first; it must not be staged.
2. ChatGPT prepares its v0.10 install copy (install-time wording plus v0.14's version and commit ID);
   Claude diff-checks it; the owner ratifies; install `1 A / 0 M / 1 D` replacing ChatGPT v0.9.
3. The owner decides the `06` filename question (12.3; recommended: accept in place, fix at v1.4) and
   the four leftover files (12.5; recommended: one `0 A / 0 M / 4 D` exact-path commit). Neither blocks
   steps 1-2.
4. Update the transfer matrix with `e7cf449`, `82ba3e1` and both handover commit IDs; independent review.
5. The owner's **separate** decision on retiring the `interim_` bridge, then an exact-path D-23 removal.
6. **P1** only on a separate explicit owner authorisation, within Stage 2 v0.7 and S2-I3 v0.3.
7. Refresh this handover after step 5, or sooner if a chat shows signs of ending.

**Verify before any Git work.** HEAD was `82ba3e1` on 2026-10-18 and may have moved. Run
`git rev-parse HEAD`, and `git diff --cached --name-status --no-renames` before every commit without
exception (11). After committing, check the committed **content**, not only the shape.

**Stop points.** No filtering until the owner separately authorises P1. `TEST_6A`/`TEST_7A` get no
experimental role until characterised and a design revision assigns one. EP, 2A and 4A stay locked
until S2-I8 under any filename or alias. The six frozen Stage 1 indexes are never rewritten, and
`VHSC_samples/LG_576i_3_LP.idx` stays byte-unchanged.

---

## 14. Change log

### v0.14 - 2026-10-18

- Supersedes v0.12; **v0.13 was drafted, found to carry stale state, and never committed.** The ChatGPT
  role found three of its stale claims; a wider sweep found the rest. Corrected: the takeover delta now
  runs from `82ba3e1`; the 4.1 layout re-verified at `82ba3e1` from Git (it was the `35cd543` layout);
  the 6A/7A media recorded as tracked since `6b7acc3` in 3 and 5.6; section 6's bridge and review rows no
  longer say Route A has not happened or that the Evidence Report does not exist; 7.8's SHOULDs recorded
  as carried into the report; three section 9 lines brought current; a stale placeholder row removed
  from 10.
- New **12.3**: `06` v1.3 was installed in place contrary to D-23 v1.2's filename amendment; owner
  decision, with Claude's recommendation. New 12.4 on the untracked local v0.13. New **12.5**: four
  files swept in by `6b7acc3` that Commit C did not remove (three byte-identical copies of ratified
  documents and a superseded closure draft); owner decision. Old 12.3-12.14 become 12.6-12.17.
- Four cross-references into 12 corrected (all four were already wrong in v0.13); the
  time-zone offset value removed from 12.11, since it narrows the owner's region and the item does not
  need it.
- Three lessons added to 11: sweep by state-words, check install shapes against D-23, and verify a
  cleanup by what survives.
- Everything v0.13 added is retained: all seventeen bridge section 15-16 items and the 289/610 fix.

### v0.13 - 2026-10-18 (drafted, never committed)

- **Lands the four bridge section 15-16 items v0.12 lacked** (11): isolated Python and `PYTHONPATH`,
  the `.vpy` HERE idiom, fail-closed test placement before `unittest.main()`, and the S4
  non-isolated-testing error. Records the lesson that coverage was asserted three times without being
  checked, and that the ChatGPT v0.10 draft relied on the assertion.
- **Fixes the 289/610 ambiguity** in 7.8 that this role promised to correct: 610 for `-1,0`, 289 for
  `previous_display`, each named.
- As-at point moved from `166af3a` to **`82ba3e1`**: nine commits added to 4.2, covering Commits A, B
  and C, the seven-index tracking, and the ratified report and `06` v1.3 installs; section 6 updated.
- Rewrote 12 and 13 for the post-installation state: Route A down to its last step, ChatGPT v0.10
  reviewed, install order v0.13 then ChatGPT v0.10.
- **Version line carries no DRAFT label.** v0.10 and v0.12 of this handover were committed reading
  "DRAFT FOR OWNER REVIEW" - an instance of the install-time wording defect this role keeps raising in
  other documents. This handover is a role record, not an authority, and its status line says so; it
  needs no ratification label to be true on installation.

### v0.12 - 2026-10-18 (draft for owner review)

- **The project owner ratified the S2-I3 P0 registration gate as PASSED.** v0.11 was written hours
  earlier and said acceptance was outstanding and the only blocker; it was never installed, and v0.12
  replaces it. Updated the header, 2, 7.8, 12.1 and 13 accordingly.
- Reordered 13 so the now-unblocked seven-index tracking commit is step 1 and Commit A step 2.
- Added **12.17**: three committed documents still say acceptance is pending. They were true at their
  installing commits and were overtaken afterwards. **The owner decided not to re-version them**; the
  ratification goes into the Evidence and Gate Report, and this handover is the current statement of
  gate status until then.
- Restated in three places that gate ratification is **not** P1 authorisation, which remains a separate
  explicit owner decision.

### v0.11 - 2026-10-18 (superseded before installation)

- As-at point moved from `35cd543` to **`166af3a`**: seven further commits recorded (4.2), including
  two snapshots that swept in unintended files, one bad staging commit and its remediation, and the
  `.gitignore` extension.
- Added **7.8**: S2-I3 P0 executed in full and independently reviewed - 8/8 admissions REGISTERED,
  8/8 descriptive diagnostics, **4/4 pair tests PASS**, summary run, verdict ACCEPTED and gate PASS
  recommended, with both headline results recomputed from raw per-item data. Records the 93.08% control
  result and why it does **not** supersede the `interim_`'s 90.2%; the closed media hash chain; the
  `Q_fixed` and transform-mix re-derivations; the appearance-instrument versus population-sample framing
  of the `_blocky` pair; the SKIPPED scope distinction; the four SHOULDs; and S4's two-quantiser-table
  trap in full.
- Rewrote **13** around the single remaining blocker, the owner's acceptance decision, and reordered
  the queue so the time-sensitive identity cleanup is not waiting behind it.
- Updated **12** to the real outstanding set: acceptance, Commits A, B and C with their exact shapes,
  the untouched Route A transfer, and S4.
- Added **six lessons to 11**, five of them from this role's own errors on 2026-10-18: re-read the
  passage before criticising another document; do not let a retraction reach further than the error;
  over-delivery is the failure mode that follows a correction; check your own prior handover before
  calling a finding new; verify committed content and not just staged shape; and stage-diff before
  every commit. Also records what cross-role review caught.
- Noted in **10** that the two ChatGPT-family documents this role drafted are the weakest-reviewed
  items in the tree, and in **6** that the `interim_` document is correct and a criticism of it was
  withdrawn.

### v0.10 - 2026-10-17 (draft for owner review)

- As-at point moved from `c45dcf0` to **`35cd543`**: seven further commits recorded (4.2), including
  the S2-I1 code and status v0.5, the S2-I2 code and evidence with status v0.6, and the ratified
  Stage 2 v0.7 / S2-I3 v0.3 / status v0.7 installation.
- Recorded **S2-I1 complete** (7.4) and **S2-I2 complete with registration gate PASS** (7.5),
  including the M4/M4a resolution, the BestSource-versus-FFmpeg wording correction, and which S2-I2
  components S2-I3 may and may not reuse.
- Added **7.6 S2-I3**: the ratified eight-source pool, the exact P-skip identity admission proof with
  full rehearsal and negative-test figures, the predeclared pair-correspondence rule with its
  disclosure, the nine scratch index hashes, the fifteen P0 files, and the review history ending in
  clearance.
- Added **7.7**: the per-macroblock geometry measurement confirming K-03 and the `x=8` independence in
  decoded pixels, the transform-transition and `NONE`-composition tables, the interlace harm result,
  the falsifiable H/V prediction - **and the correction of Claude's own mis-located measurement band**,
  which reversed an earlier published conclusion.
- Added **2.3**, a new standing rule: check findings against the existing K/O items before calling
  them new, and keep exploratory measurements out of repository-document proposals. This follows three
  Claude errors on 2026-10-17.
- Updated the development pool, Q_fixed values and sample roles (5.5), and added **5.6** on the
  2026-10-17 sample additions, the eight removed renamed copies, the hold-out hazard they posed, and
  the two genuinely new home-recording pairs.
- Expanded the CMD audit rules (7.3) with the parenthesis-in-block MUST, the `for /f` ERRORLEVEL trap
  and the silent-exit rule; recorded the VapourSynth Python and the NumPy dependency boundary (5.1).
- Recorded that this workspace can run the real VapourSynth/BestSource stack at the owner's own
  versions, and that media can be sparse-checked out from GitHub rather than uploaded (2.2).
- Updated `.gitattributes`, `core.autocrlf` and installed-document hashes (4.7); the layout and
  tracked-file count (4.1); the authority list with K/O pointers (6).
- New lessons: install-time wording, fixing a finding can introduce a new one, and how to help the
  owner when several tracks run at once (11).
- Rewrote outstanding items (12) and state/next steps (13) around the P0 run.

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
- Updated sample roles, media policy, conventions, review method, lessons and next steps.
- Removed the owner's personal name and city throughout; corrected the log count to six.

### v0.7 - 2026-10-12

- Common continuity-purpose text; as-at `317d3f1`; ChatGPT v0.5 facts; verbatim authorisation quote.

### v0.6 and earlier - 2026-10-07/12

- Earlier states; pre-reset history (provenance only).
