# 00 - Project Status

**Document:** `00_PROJECT_STATUS_v0_3.md`
**Version:** 0.3
**Date:** 2026-10-13
**Drafted by:** ChatGPT from the completed role-handover refresh and independent ChatGPT/Claude knowledge-base reconciliation
**Status:** RATIFIED by the project owner on 2026-10-13. This file records the current state after application of the coordinated reconciliation correction set. It is a concise shared current-state index, not a competing technical authority; owning authorities prevail on conflict.

---

## 1. Purpose

This file answers one narrow question:

> Where does the `VapourSynth-mpeg2Deblock` project stand right now?

It is deliberately concise. Technical detail belongs in the owning authority documents. Build settings
are owned by the Visual Studio project files. CI/release are owned by the current GitHub Actions
workflow and its expected-switch CSV. The practical build/test procedure is summarized in README
`Building` and the current role handovers. The former final common migration handback is retained only
in Git history until the Development Closure history scrub.

---

## 2. Current repository state

Repository: `VapourSynth-mpeg2Deblock`
Development branch: `main`
Application base for the cleanup/reconciliation correction set: `06f2a4e` (`SNAPSHOT to make it lcean and up to date`).
The earlier `9c1ec9e` commit remains the first pre-cleanup snapshot.

Recent post-migration commits:

```text
06f2a4e  SNAPSHOT to make it lcean and up to date
9c1ec9e  SNAPSHOT before cleanup
1a3cb1c  Refresh ChatGPT and Claude continuity handovers
317d3f1  snapshot
2e4eab1  Correct VapourSynth header provenance to R81
5010b79  Ratify deblock concept v1.2, Stage 2 v0.4, and project status
e7f63d0  Retire migration working records and obsolete handoff artifacts
a0e7100  Pin CRLF checkout for VS project files and batch files (determinism only)
```

The migration itself was ratified CLOSED by the project owner on 2026-10-11. By project-owner ruling
on 2026-10-13, the ratified v0.21 final common migration handback ZIP is deleted from the current
tree and is **not** re-issued. It remains retrievable from Git history only until the planned
Development Closure history scrub.

The migration working/evidence subtree `docs/HANDOVER/migration/` has already been retired from the
current repository. The obsolete loose `MIGRATION_00_START_HERE_INTRO_FOR_DEVELOPMENT_CHATS.md`
message-template copy is also retired by this reconciliation. Build settings are owned by the Visual
Studio project files; CI/release by the current workflow and expected-switch CSV; README `Building`
and the current role handovers summarize the practical build/test procedure.

---

## 3. Technical state

### Stage 1

Stage 1 is frozen and accepted. `Mpeg2BlockInspector.exe` is the accepted legacy-C inspector/indexer
continuity baseline. The six tracked accepted `.idx` files are immutable regression baselines and are
not to be regenerated merely to make tests pass.

`TEST_4A_A003_blocky` was part of the formal Stage 1 evidence pair, but its `.idx` is not one of
those six tracked immutable baselines. Stage 2 v0.6 plans bounded generation/validation during S2-I1
if the index remains absent/untracked; the project owner decides separately whether it is ever tracked or granted
baseline status.
The generated index and log remain uncommitted unless the project owner explicitly decides to track them; check `git status --short` before any snapshot commit.


### Stage 2

Stage 2 v0.6 is RATIFIED as part of this coordinated correction set. It synchronizes media/lifecycle
policy and post-handover knowledge, records unassigned/spare material and the bounded 4A-blocky
index-validation plan, and changes no deblocking algorithm, existing assigned material role,
six-baseline identity or implementation-order sequence. **No Stage 2 implementation has started.**

The next technical increment, if and when development is separately restarted, is:

```text
S2-I1 - read-only Stage 1 index reader / validation
```

Technical restart is **NOT AUTHORISED** at this status point.

### Production plugin

The Visual Studio solution contains the production-plugin project skeleton. `mpeg2Deblock.dll` currently
exposes only the `mpeg2deblock.Identity` scaffold. It is not yet a deblocking filter.

---

## 4. Current authority/status index

Primary repository technical/status authorities are:

```text
docs/REPOSITORY/05_DECISIONS_v1_2.md                    decision authority
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md                   v1.2 RATIFIED 2026-10-11
docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md                  v0.4 current ratified-constraints baseline; not frozen final packing
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md  RATIFIED / Stage 1 frozen evidence
docs/REPOSITORY/Stage2_Experiment_Design_v0_6.md          Stage 2 design
docs/REPOSITORY/00_PROJECT_STATUS_v0_3.md                current-state index
NOTICE.md                                                governing Restricted Media permission/restrictions
```

Build settings are owned by the Visual Studio project files. CI/release are owned by
`.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml` and
`.github/workflows/expected_stage_bplus_switches.csv`. README `Building` and the current role
handovers summarize the practical build/test procedure. The deleted migration handback remains in
Git history only until the Development Closure history scrub. `NOTICE.md` separately governs
Restricted Media policy; `05_DECISIONS` remains the technical/design decision authority.

---

## 5. Settled post-migration housekeeping

The following are complete:

- migration ratified CLOSED;
- deterministic `.gitattributes` CRLF rules added for Visual Studio project/solution files and BAT files;
- the five accepted Visual Studio working-tree hashes reproduced with `core.autocrlf=false`;
- all TESTING BAT files verified CRLF;
- LP inspector smoke output reproduced the immutable LP `.idx` baseline byte-for-byte;
- GitHub-generated source ZIP empirically reproduced the accepted Visual Studio hashes and CRLF BAT files;
- obsolete Stage A evidence files and the old Stage 1 handoff ZIP removed;
- `docs/HANDOVER/migration/` working/evidence subtree removed;
- current working tree was clean after commit `e7f63d0` and that commit was pushed to `origin/main`;
- authority/status update committed/pushed as `5010b79`;
- VapourSynth header provenance corrected to R81 / retained post-R81 `master` snapshot and committed/pushed as `2e4eab1`;
- Restricted Media policy ratified directly by the project owner on 2026-10-12 at `317d3f1`;
- ChatGPT v0.5 / Claude v0.7 continuity handovers plus common continuity-purpose text committed/pushed
  as `1a3cb1c`;
- pre-cleanup snapshot committed/pushed as `9c1ec9e`; final clean review baseline committed/pushed as
  `06f2a4e`, adding the latest Claude builder review to `docs/in-progress/`; all eight `docs/in-progress/`
  reconciliation working files are deliberately removed from the cleaned current tree and remain available
  through Git history until the Development Closure history scrub;
- mandatory independent ChatGPT + Claude knowledge-base inventories/cross-classification completed;
- project-owner identity scrub and superseded-version current-tree purge applied in this reconciliation round; Git history remains untouched until Development Closure;
- project owner ruled 2026-10-13 that the v0.21 final common migration handback ZIP is deleted from
  the current tree and is not re-issued; build/CI/release ownership therefore rests with the live
  project/workflow/CSV files, with README `Building` and role handovers carrying procedural summaries;
- the project owner ruled that project-document filenames become versioned on their next actual revision and that
  a version reference means that version or later except for exact historical-event/identity records;
- the project owner ruled that `LG_576i_3_LP_blocky`, `LG_576i_4_EP_blocky` and `LG_576i_5_MLS_blocky`
  currently have no Stage 2 role and are unassigned/spare;
- the project owner clarified that Development Closure means active development finished; Restricted Media cleanup
  occurs then and the repository may continue afterward as an ongoing maintenance project.

---

## 6. Current pre-restart sequence

The coordinated cleanup/reconciliation correction set has been ratified and applied. The independent
ChatGPT/Claude knowledge-base reconciliation that produced it is complete. Technical restart remains
**NOT AUTHORISED**.

Remaining sequence before any technical restart decision:

1. Update the ChatGPT and Claude role handovers to the final reconciled state (expected v0.6 / v0.8).
2. Verify the resulting current knowledge base and repository state after those handover touch-ups.
3. Only then may the project owner separately decide whether to authorise technical restart / S2-I1.

No step in this sequence itself authorises S2-I1.

**Development Closure** means the point at which the project owner expressly declares active development
finished. At Development Closure all Restricted Media is removed from the current repository tree
and project-controlled assets/storage and the planned Git-history purge removes historical repository
media copies, purged superseded current-tree files and owner-identifying text. The narrow ChatGPT/Claude AI development-media authorisation ends at that point. The
project/repository may then continue as an ongoing maintenance project. Development Closure cleanup
is not a prerequisite for Stage 2 restart.

Markdown EOL/hash policy from this reconciliation: no repository-wide `*.md eol=crlf` rule is added.
Documents delivered by either chat for review or application are US-ASCII with CRLF line endings and
are mechanically checked before delivery. Git-stored and GitHub source-archive forms of Markdown may
be LF. Any byte hash/EOL assertion must identify the representation being checked.

---

## 7. Current role-handover state

Current committed continuity handovers:

```text
ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_5.md
Claude_HANDOVER_TO_Future_Claude_Chat_v0_7.md
ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT_FOR_BOTH_ROLES.md
```

They were committed/pushed at `1a3cb1c`.

Following this applied reconciliation correction set, each role now requires a small successor
handover update (expected ChatGPT v0.6 / Claude v0.8) recording the resolved policy, document-management
and status state. That touch-up is continuity maintenance, not technical restart authorization.

---

## 8. Stage 2 material roles - current concise view

Recorder quality order, best to worst:

```text
XP -> SP -> LP -> EP -> MLS
```

Experimental roles are separate from that quality order:

```text
PRIMARY DEVELOPMENT / TUNING
    LG_576i_3_LP

LOCKED INTERLACED HOLD-OUTS
    LG_576i_4_EP
    TEST_4A_A003 original
    TEST_2A_A001 original

PROGRESSIVE / CONTROL
    LG_576i_5_MLS

SECONDARY PAIRED-REFERENCE / STRESS
    TEST_4A_A003_blocky
    TEST_2A_A001_blocky

PRESENT BUT UNASSIGNED / SPARE
    LG_576i_1_XP and _blocky
    LG_576i_2_SP and _blocky
    TEST_3A_A002 and _blocky
    LG_576i_3_LP_blocky
    LG_576i_4_EP_blocky
    LG_576i_5_MLS_blocky
```

Do not infer properties or assign experimental roles to the unassigned material without explicit
analysis and owner-approved disposition.

---

## 9. Change log

### v0.3 - 2026-10-13 (RATIFIED)

- Records handover refresh commit `1a3cb1c`, pre-cleanup snapshots `9c1ec9e` / `06f2a4e`, and
  completion of the independent ChatGPT/Claude reconciliation inventories/cross-classification.
- Updates the authority index for `05_DECISIONS_v1_2.md`, Stage 2 v0.6, this versioned status file
  and governing `NOTICE.md`.
- Records the project owner's Development Closure -> Restricted Media cleanup -> ongoing maintenance lifecycle.
- Records the narrow ChatGPT/Claude AI development-media exception and its end at Development Closure.
- Records the project owner's filename/version-reference rulings and the representation-aware Markdown EOL/hash
  policy; no `*.md eol=crlf` rule is added.
- Lists the three LG LP/EP/MLS `_blocky` clips as unassigned/spare.
- Records the bounded S2-I1 plan for the currently untracked/absent `TEST_4A_A003_blocky.idx`
  without changing the six immutable baselines.
- Retires the loose historical migration start-here template and, by project-owner ruling 2026-10-13,
  deletes the v0.21 final common migration handback ZIP from the current tree without replacement; it
  remains in Git history only until the Development Closure history scrub.
- Technical restart remains NOT AUTHORISED.

### v0.2 - 2026-10-12 (RATIFIED)

- Synchronized Project Status after the project owner's direct ratification of the coordinated Restricted Media
  policy and Stage 2 v0.5.
- Recorded Source Recording origin anchoring, option (a) visualisations, the no-external/private-
  review transmission rule then in force, and the planned final tree/history media cleanup.
- Recorded Stage 2 v0.5 as the current ratified design and preserved the no-code/separate-restart gate.
- This v0.2 change-log entry was omitted from the v0.2 file and is restored here as historical
  status bookkeeping.

### v0.1 - 2026-10-11 (RATIFIED)

- Claude delta recheck: NO OBJECTION; the project owner ratified v0.1 on 2026-10-11.
- Creates a shared concise project-current-state index at `docs/REPOSITORY/00_PROJECT_STATUS.md`; owning authorities prevail on conflict.
- Records migration closure, post-migration determinism/housekeeping completion, current technical
  state, current authority set, pre-restart sequence and role-handover/reconciliation requirements.
- Creates no new technical design decision and does not authorise technical restart.
- Incorporates Claude review: pending `VERSION.txt` correction, retired-record history note, and planned end-of-development history purge.
