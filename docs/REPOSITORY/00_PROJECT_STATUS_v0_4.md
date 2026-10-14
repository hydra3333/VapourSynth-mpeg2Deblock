# 00 - Project Status

**Document:** `00_PROJECT_STATUS_v0_4.md`
**Version:** 0.4
**Date:** 2026-10-14
**Drafted by:** ChatGPT from the completed fresh-history reset, role-handover refresh and Claude final knowledge-base / repository verification
**Status:** RATIFIED 2026-10-14 by the project owner. Supersedes v0.3. This file is a concise shared current-state index, not a competing technical authority; owning authorities prevail on conflict.

---

## 1. Purpose

This file answers one narrow question:

> Where does the `VapourSynth-mpeg2Deblock` project stand right now?

It is deliberately concise. Technical detail belongs in the owning authority documents. Build settings
are owned by the Visual Studio project files. CI/release are owned by the current GitHub Actions
workflow and its expected-switch CSV. The practical build/test procedure is summarized in README
`Building` and the current role handovers.

The 2026-10-13 interim history reset deliberately replaced the prior repository history with a new
single-root baseline while retaining the Restricted Media needed for active development. Pre-reset
commits cited by project documents are now external historical provenance only: they are **removed
from repository history**. Direct-SHA GitHub views may persist until GitHub garbage collection; that
does not make those commits part of the current repository history.

This interim reset is distinct from **Development Closure**. Development Closure still requires
Restricted Media removal from the current tree and project-controlled assets, followed at or promptly
after closure by another history purge/reset so that Restricted Media is absent from the resulting
repository history.

---

## 2. Current repository state

Repository: `VapourSynth-mpeg2Deblock`
Development branch: `main`

Fresh-history root:

```text
11f47427624bf5f68b3426fe9f58aa26d40e47f7
```

Root tree:

```text
45ad1f16a24d3cce0411863a9804472efa1c8529
```

Root author and committer:

```text
hydra3333 <10749357+hydra3333@users.noreply.github.com>
```

Last commit verified before this status refresh (final bounded KB/repository check):

```text
bfb6cc272eb23508225fb8ba199b078d64101abe
```

Repository history through the final pre-refresh verification:

```text
11f4742  fresh zero-parent repository baseline after history reset
    |
eac5526  first of two handover-install commits
    |
bfb6cc2  handover replacement completed; verified by the final KB check
```

The commit that installs this status file follows `bfb6cc2`. For the current HEAD, use the live
repository.

The final handover result versus root `11f4742` is exactly four path changes:

```text
deleted: docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_5.md
added:   docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_6.md
deleted: docs/HANDOVER/Claude_HANDOVER_TO_Future_Claude_Chat_v0_7.md
added:   docs/HANDOVER/Claude_HANDOVER_TO_Future_Claude_Chat_v0_8.md
```

All other 122 files at `bfb6cc2` are byte-identical to the fresh root tree. Accordingly, all frozen
source/analyzer/build-contract hashes, the six immutable `.idx` baselines, the 16 Source Recordings
and the six retained logs are unchanged.

The externally recorded pre-reset source identity is:

```text
fd82d78715ed6a61ef4e80b9769655eefe23c384
```

It identifies the verified source tree immediately before the history reset. It and all other
pre-reset SHAs are provenance only and are not commits in the current repository history.

Important pre-reset provenance includes:

```text
fd82d78  reconciliation corrections + identity scrub + 37-path current-tree purge
06f2a4e  final pre-cleanup review snapshot
9c1ec9e  first pre-cleanup snapshot
1a3cb1c  earlier ChatGPT v0.5 / Claude v0.7 handover refresh
317d3f1  Restricted Media policy / Stage 2 v0.5 state
2e4eab1  VapourSynth header provenance corrected to R81
5010b79  deblock concept v1.2 / Stage 2 v0.4 / earlier status ratification
e7f63d0  migration working-record retirement
a0e7100  deterministic CRLF checkout rules for VS/BAT files
5141a23  final migration commit
f6ea380  old pre-reset v0.1.0 release/tag identity
```

These SHAs are historical references only. The old migration handback, `docs/in-progress/` working
files, superseded current-tree versions and the other ratified purge targets were removed from the
current tree before the reset and are now also **removed from repository history**.

The old `v0.1.0` Release and tag and all old GitHub Actions workflow runs were deleted before the
reset. A fresh `v0.1.0` pre-release titled:

```text
v0.1.0 NOT FOR USE, SNAPSHOT RELEASE ONLY
```

was published against root `11f4742`. Its workflow-built asset is:

```text
mpeg2Deblock-v0.1.0-win-x64.zip
owner-reported SHA-256:
f8ddb2da0b38e9639231fc63600c28da0f0bf0e95429a5033812726f36d17785
```

Neither AI has independently inspected that binary release asset.

The migration itself was ratified CLOSED by the project owner on 2026-10-11. The deleted v0.21
final common migration handback is not current authority and was not re-issued as v0.22. Build settings
are owned by the Visual Studio project files; CI/release by the current workflow and expected-switch
CSV; README `Building` and the current role handovers summarize the practical build/test procedure.

---

## 3. Technical state

### Stage 1

Stage 1 is frozen and accepted. `Mpeg2BlockInspector.exe` is the accepted legacy-C inspector/indexer
continuity baseline. The six tracked accepted `.idx` files are immutable regression baselines and are
not to be regenerated merely to make tests pass.

`TEST_4A_A003_blocky` was part of the formal Stage 1 evidence pair, but its `.idx` is not one of
those six tracked immutable baselines. Stage 2 v0.6 plans bounded generation/validation during S2-I1
if the index remains absent/untracked; the project owner decides separately whether it is ever tracked
or granted baseline status. The generated index and log remain uncommitted unless the project owner
explicitly decides to track them; check `git status --short` before any snapshot commit.

### Stage 2

Stage 2 v0.6 is RATIFIED. It synchronizes media/lifecycle policy and post-handover knowledge, records
unassigned/spare material and the bounded 4A-blocky index-validation plan, and changes no deblocking
algorithm, existing assigned material role, six-baseline identity or implementation-order sequence.

**No Stage 2 implementation has started.**

The next technical increment, if and when development is separately restarted, is:

```text
S2-I1 - read-only Stage 1 index reader / validation
```

Technical restart / S2-I1 is **NOT AUTHORISED** by the history reset, handover refresh, final KB check,
or this status refresh.

### Production plugin

The Visual Studio solution contains the production-plugin project skeleton. `mpeg2Deblock.dll`
currently exposes only the `mpeg2deblock.Identity` scaffold. It is not yet a deblocking filter.

---

## 4. Current authority/status index

Primary repository technical/status authorities are:

```text
docs/REPOSITORY/05_DECISIONS_v1_2.md                    decision authority
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md                   v1.2 RATIFIED 2026-10-11
docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md                 v0.4 current ratified-constraints baseline; not frozen final packing
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md RATIFIED / Stage 1 frozen evidence
docs/REPOSITORY/Stage2_Experiment_Design_v0_6.md        Stage 2 design; RATIFIED 2026-10-13
docs/REPOSITORY/00_PROJECT_STATUS_v0_4.md               current-state index
NOTICE.md                                               governing Restricted Media permission/restrictions
README.md                                               public project/build summary
```

Build settings are owned by the Visual Studio project files. CI/release are owned by:

```text
.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml
.github/workflows/expected_stage_bplus_switches.csv
```

README `Building` and the current role handovers summarize the practical build/test procedure.

The deleted migration handback is not current authority and is not present in current repository
history. `NOTICE.md` separately governs Restricted Media policy; `05_DECISIONS` remains the
technical/design decision authority.

Per D-23, references to versioned authorities mean that version **or later** unless the reference
records an exact historical event/version. Therefore this status refresh does not require unrelated
authority documents to be revised merely to chase version references.

---

## 5. Settled migration, reconciliation and history-reset housekeeping

The following are complete:

- migration ratified CLOSED;
- deterministic `.gitattributes` rules retained for Visual Studio project/solution files and BAT files;
- accepted Visual Studio/build-contract hashes and six Stage 1 `.idx` baselines preserved;
- Stage 1 remains frozen;
- obsolete Stage A evidence, the old Stage 1 handoff ZIP, the migration working/evidence subtree and
  the obsolete loose migration start-here template were removed before the reset;
- Restricted Media policy and the narrow ChatGPT/Claude development-media exception were ratified;
- the independent ChatGPT + Claude knowledge-base inventories/cross-classification were completed;
- project-owner identity scrub and superseded-version current-tree purge were applied;
- the 37-path purge and all eight `docs/in-progress/` removals were verified before the reset;
- the v0.21 final common migration handback ZIP was deleted and not re-issued as v0.22;
- D-23 versioning/current-tree/identity/EOL rules were ratified in `05_DECISIONS_v1_2.md`;
- `LG_576i_3_LP_blocky`, `LG_576i_4_EP_blocky` and `LG_576i_5_MLS_blocky` were explicitly recorded as
  unassigned/spare Stage 2 material;
- the interim history reset replaced all pre-reset repository history with the fresh zero-parent root
  `11f4742`, while intentionally retaining the 16 Restricted Media recordings needed for active development;
- the old `v0.1.0` Release/tag and old Actions runs were deleted and a fresh snapshot pre-release was
  published on the new root;
- the old local clone was push-disabled, quarantined, replaced by a fresh HTTPS clone, verified, and deleted;
- current continuity handovers were refreshed to ChatGPT v0.6 and Claude v0.8;
- Claude's final bounded KB/repository verification at `bfb6cc2` verified the four-path handover delta,
  byte identity of the other 122 files, zero owner-identity hits, and agreement of the two handovers
  on shared facts.

The pre-reset SHAs and deleted artifacts remain useful as externally recorded historical provenance,
but they are **removed from current repository history**. No current project procedure should assume
that they can be checked out from the repository.

The interim reset was **not Development Closure**. Restricted Media remains intentionally present and
authorised for active project development under `NOTICE.md`.

---

## 6. Current restart gate

The coordinated cleanup/reconciliation correction set, owner-identity scrub, interim history reset,
role-handover refresh and bounded final KB/repository verification are complete.

Claude's final bounded verification at `bfb6cc2` reported no MUST finding and one SHOULD: refresh this
status file because v0.3 still described the pre-reset history as current. This v0.4 is that refresh.

With v0.4 ratified and installed, the knowledge-base/repository gate is complete. No further
documentation change is required before the owner considers restart merely because other documents
contain version references governed by D-23's "version or later" rule.

The remaining action is a **separate project-owner decision** whether to authorise technical restart.

Until the project owner expressly does so:

```text
S2-I1 IS NOT AUTHORISED
```

If restart is authorised, the first permitted technical increment is S2-I1 only, in accordance with
Stage 2 v0.6 and the current role handovers.

**Development Closure** remains a future, separate lifecycle event. It occurs only when the project
owner expressly declares active development finished. At Development Closure all Restricted Media is
removed from the current repository tree and project-controlled assets/storage, and at or promptly
after closure another history purge/reset is performed so Restricted Media is absent from the
resulting repository history. The narrow ChatGPT/Claude AI development-media authorisation ends at
that point. The repository may then continue as an ongoing maintenance project.

Markdown EOL/hash policy remains unchanged: no repository-wide `*.md eol=crlf` rule is added.
Documents delivered by either chat for review/application are US-ASCII with CRLF line endings and
mechanically checked before delivery. Git-stored and GitHub source-archive forms of Markdown may be
LF. Any byte hash/EOL assertion must identify the representation being checked.

---

## 7. Current role-handover state

Current continuity handovers:

```text
docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_6.md
docs/HANDOVER/Claude_HANDOVER_TO_Future_Claude_Chat_v0_8.md
docs/HANDOVER/ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT_FOR_BOTH_ROLES.md
```

The predecessor ChatGPT v0.5 and Claude v0.7 handovers are deleted from the current tree in accordance
with D-23.

ChatGPT v0.6 and Claude v0.8 are aligned on the shared repository baseline, authority set, frozen
Stage 1 state, Stage 2 v0.6 status, Restricted Media lifecycle, fresh-history reset and restart gate.
Role-specific content appropriately differs.

The handover replacement is continuity maintenance only. It does not authorise S2-I1.

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

### v0.4 - 2026-10-14 (RATIFIED)

- Refreshes the concise current-state index after the 2026-10-13 interim history reset and the
  completed v0.6/v0.8 role-handover replacement.
- Records fresh root `11f47427624bf5f68b3426fe9f58aa26d40e47f7`, root tree
  `45ad1f16a24d3cce0411863a9804472efa1c8529`, and the last pre-refresh commit verified by the
  final bounded KB/repository check, `bfb6cc272eb23508225fb8ba199b078d64101abe`.
- Reclassifies all pre-reset SHAs, including `fd82d78`, as external historical provenance only.
- Corrects obsolete v0.3 statements that deleted items remained in repository history or that Git
  history was untouched: the interim reset removed the pre-reset history.
- Records that the interim reset intentionally retained the 16 Restricted Media recordings and is
  distinct from future Development Closure media removal and history purge/reset.
- Updates the current handovers to ChatGPT v0.6 / Claude v0.8 and records completion of the bounded
  final KB/repository verification.
- Records the fresh `v0.1.0` snapshot pre-release and marks its binary asset SHA-256 as owner-reported.
- Leaves Stage 1 frozen, Stage 2 v0.6 RATIFIED, and S2-I1 NOT AUTHORISED.
- Makes no technical/design change and requires no unrelated document revision under D-23's
  "version or later" rule.

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
  deletes the v0.21 final common migration handback ZIP from the current tree without replacement.
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
