# 00 - Project Status

**Document:** `00_PROJECT_STATUS_v0_5.md`
**Version:** 0.5
**Date:** 2026-10-14
**Drafted by:** ChatGPT from ratified v0.4, the project owner's S2-I1 restart decision,
Claude's verification of commit `4221f7f`, and the reported successful Windows S2-I1 acceptance;
Claude review corrections applied.
**Status:** RATIFIED 2026-10-14 by the project owner. Supersedes v0.4. This file is a concise shared
current-state index, not a competing technical authority; owning authorities prevail on conflict.

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

Last independently verified S2-I1 commit before this status refresh (Claude's GitHub source-ZIP
comparison against `c45dcf0`):

```text
4221f7f9f3c015da4ca70b4f8c0249536cd7e3b5
```

Known post-reset commit sequence through that verified commit:

```text
11f4742  fresh zero-parent repository baseline after history reset
    |
eac5526  first handover-install commit
    |
bfb6cc2  second handover-install commit; final KB check
    |
c45dcf0  ratified Project Status v0.4 installation
    |
bfaed24  owner snapshot: ChatGPT v0.7 / Claude v0.9 handovers, Claude S2-I1 reviews,
    |        S2-I1 v0.1 drafts and candidate package ZIPs (transient)
    |
10956a1  owner snapshot: docs/VS2026_Copilot_Free_CheatSheet.md
    |
4221f7f  accepted S2-I1 v0.2 files; v0.1 drafts and package ZIPs removed; Claude S2-I1 reviews
         moved to docs/; ChatGPT v0.6 / Claude v0.8 handovers deleted
```

The transient v0.1 drafts and package ZIPs added in `bfaed24` are absent from the current tree but
remain in Git history (they contain code and documents only, no Restricted Media).

This identifies a **verified commit**, not necessarily the live/current HEAD. The commit that
installs v0.5 will follow it or another subsequently verified commit; check the live repository.

Claude's GitHub source-ZIP comparison of `4221f7f` against `c45dcf0` established:

```text
+5  accepted S2-I1 v0.2 implementation files under experiments/stage2/
+2  role handovers: ChatGPT v0.7; Claude v0.9
+2  Claude S2-I1 review documents under docs/
+1  docs/VS2026_Copilot_Free_CheatSheet.md (owner's unrelated document)
-2  superseded role handovers: ChatGPT v0.6; Claude v0.8
```

The five S2-I1 files match Claude's reviewed v0.2 content, except for the reviewed generation-BAT
line-77 logging correction. The fixed BAT's SHA-256 (CRLF form, identical in checkout and GitHub
archive because `*.bat` is pinned `eol=crlf`) is
`cddc566da8ee02bf0f62163fea8dd1f0bd7d4bec354f8b201134f32e864233ac`, verified by Claude in the
`4221f7f` source ZIP. Neither candidate ZIPs nor obsolete v0.1 files were retained in
that commit. All other files are byte-identical to `c45dcf0`, including the frozen source,
build-contract hashes and six immutable `.idx` files. Claude reported zero owner-identity hits and
132 tracked files at `4221f7f`.

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
those six tracked immutable baselines. Its S2-I1 candidate `.idx` was generated and validated against
all applicable Stage 1 Gate Report section 8.1 rows. It remains uncommitted/non-baseline scratch
material under `%TEMP%`, with its log; future tracking or baseline status requires a separate
project-owner decision. Accepted baseline indexes were not regenerated or changed.

### Stage 2

Stage 2 Experimental Design v0.6 remains RATIFIED. It governs the experiment methodology,
material roles and S2-I1 through S2-I10 order; implementation increments require separate
project-owner authorisation. No change to the Stage 2 design has been made here.

On 2026-10-14, after the knowledge-base/repository gate was closed, the project owner separately
authorised technical restart **for S2-I1 only**. This was a conversational decision made after
ratification of Project Status v0.4; it supersedes v0.4's historical "not authorised" state.

**S2-I1 - COMPLETE / WINDOWS ACCEPTANCE PASS / COMMITTED at `4221f7f`.**

S2-I1 delivers an independent, read-only Stage 1 v1 index reader and validation tooling under
`experiments/stage2/`. The frozen inspector and Stage 1 analyzer are not modified. Reported Windows
acceptance, subsequently checked by Claude:

```text
Six accepted .idx regression checks:          PASS
Six BestSource/index correspondences:        PASS
TEST_4A_A003_blocky candidate generation:    PASS
All applicable Stage 1 report 8.1 rows:      PASS
Corrected BAT inspector exit-code logging:   PASS (exit code 0)
```

The BestSource checks cover frame count, dimensions and picture types. The independent reader
reproduces frozen analyzer totals, including FRAME/FIELD/NONE states and effective-QP histograms,
and handles progressive-frame, picture-type and leading-B exclusion information. Leading B pictures
before the first I picture are excluded from quality evidence, not structural checks: two each for
LP, EP and MLS; none for the tested 2A/4A original/blocky clips.

The scratch `TEST_4A_A003_blocky.idx` candidate matched SHA-256:

```text
57f3b60d1ea2108f29f222c7c658cb1ddc9eb26c14071cb056112a2f3b296e73
```

It is not a seventh accepted baseline and was not committed. S2-I1 establishes reader/temporal
validation only; it does not establish spatial index-to-pixel registration or filtering quality.

**S2-I2 AND ALL LATER INCREMENTS ARE NOT AUTHORISED.** S2-I2 requires a separate project-owner
decision after review of S2-I1. Its intended scope remains the Stage 2 v0.6 seam-map and mandatory
two-dimensional spatial-registration diagnostics.

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
docs/REPOSITORY/00_PROJECT_STATUS_v0_5.md               current-state index
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
- Claude's final bounded KB/repository verification at `bfb6cc2` verified the v0.6/v0.8 handover
  installation and the unchanged underlying technical baseline;
- Project Status v0.4 was ratified and installed at `c45dcf0`;
- technical restart for S2-I1 only was subsequently authorised on 2026-10-14;
- ChatGPT v0.7 / Claude v0.9 handovers were added in `bfaed24`; the accepted S2-I1 v0.2 files were
  committed, and the transient material and superseded handovers removed, at `4221f7f`;
- Claude's GitHub-ZIP verification of `4221f7f` confirmed the bounded change, 132 tracked files,
  unchanged frozen sources/six baseline indexes and zero owner-identity hits.

The pre-reset SHAs and deleted artifacts remain useful as externally recorded historical provenance,
but they are **removed from current repository history**. No current project procedure should assume
that they can be checked out from the repository.

The interim reset was **not Development Closure**. Restricted Media remains intentionally present and
authorised for active project development under `NOTICE.md`.

---

## 6. Current restart gate

The coordinated cleanup/reconciliation correction set, owner-identity scrub, interim history reset,
role-handover refresh and bounded final KB/repository verification were completed before restart.
Project Status v0.4 recorded that completed gate. The project owner subsequently authorised the
bounded S2-I1 restart on 2026-10-14, and S2-I1 acceptance/commit have now been reported and verified
as recorded in section 3.

The authorisation boundary is now:

```text
S2-I1         AUTHORISED 2026-10-14; COMPLETE / ACCEPTED / COMMITTED
S2-I2         NOT AUTHORISED; requires a separate project-owner decision
S2-I3..I10    NOT AUTHORISED; subsequent increments require separate decisions
```

This status file does not itself authorise any further technical increment. Stage 2 v0.6 remains
in force, including its experiment controls and increment sequence. The project owner must review
the accepted S2-I1 result and separately decide whether to begin S2-I2.

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
docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md
docs/HANDOVER/Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md
docs/HANDOVER/ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT_FOR_BOTH_ROLES.md
```

The predecessor ChatGPT v0.6 and Claude v0.8 handovers were deleted from the current tree at
`4221f7f` in accordance with D-23. ChatGPT v0.7 and Claude v0.9 were prepared before the owner's
final S2-I1 Windows acceptance and thus describe a historical as-at point: candidate delivered,
Windows acceptance pending. That wording is not evidence that the tests are still pending. This
status refresh records the later accepted result and commit; the role handovers should be updated
at the next appropriate continuity-maintenance milestone.

The handovers are continuity aids, not technical authority or authorisation for S2-I2.

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

### v0.5 - 2026-10-14 (RATIFIED)

- Records the project owner's separate 2026-10-14 technical restart authorisation for S2-I1 only.
- Records S2-I1 v0.2 acceptance on Windows: six reader regressions, six BestSource/index
  correspondences, validated scratch 4A-blocky candidate and corrected BAT logging.
- Records S2-I1 commit `4221f7f` and Claude's GitHub source-ZIP verification; identifies it as the
  last verified commit, not as an asserted current HEAD.
- Updates continuity-handovers index to ChatGPT v0.7 / Claude v0.9, recording their historical
  pre-acceptance as-at boundary.
- Preserves Stage 1 frozen status and six immutable indexes; confirms 4A-blocky remains non-baseline,
  uncommitted scratch material.
- Makes explicit that S2-I2 and later increments are **NOT AUTHORISED**; this status revision does
  not itself authorise technical advancement.
- Claude review applied: full commit chain including snapshots `bfaed24` and `10956a1`; full
  `4221f7f` SHA and full fixed-BAT SHA-256; ratified form.
- Makes no change to technical design, build/CI/release policy or Restricted Media rules. Supersedes
  v0.4, which is deleted from the current tree in the same commit.

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
