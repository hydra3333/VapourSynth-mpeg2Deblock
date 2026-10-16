# 00 - Project Status

**Document:** `00_PROJECT_STATUS_v0_6.md`
**Version:** 0.6
**Date:** 2026-10-16
**Drafted by:** ChatGPT from the exact owner-supplied, ratified Project Status v0.5
(Windows CRLF SHA-256 `a5f19fa8c9dfd83b8d701b4e327f48555be613f75558938f328e6c53f61881da`),
the owner-ratified S2-I2 Windows acceptance, Claude's independent verification, and the
GitHub-verified S2-I2 code commit `190bd06`; Claude final-review corrections applied.
**Status:** RATIFIED 2026-10-16 by the project owner. Supersedes v0.5, installed by the separate
Step-B documentation/evidence commit. This file is a
concise shared current-state index, not a competing technical authority; owning authorities
prevail on conflict.

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

Last independently verified S2-I2 code commit before this status refresh (Claude checked the pushed GitHub
source ZIP, all nine added implementation files and the six frozen baseline indexes):

```text
190bd06ded88130ffddac7bb9adde4175d82f9f8
```

Its parent `2286341` installed ratified Project Status v0.5 after the previously verified
S2-I1 implementation commit `4221f7f9f3c015da4ca70b4f8c0249536cd7e3b5`.

Known post-reset commit sequence through the verified S2-I2 code commit:

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
    |    moved to docs/; ChatGPT v0.6 / Claude v0.8 handovers deleted
    |
2286341  ratified Project Status v0.5 installed
    |
190bd06  nine accepted S2-I2 v0.1 spatial-registration files added; pushed and independently
         GitHub source-ZIP verified; six frozen baseline indexes unchanged
```

The transient v0.1 drafts and package ZIPs added in `bfaed24` are absent from the current tree but
remain in Git history (they contain code and documents only, no Restricted Media).

This identifies a **verified commit**, not necessarily the live/current HEAD. The separate Step-B
commit that installs S2-I2 evidence, the gate report and this Project Status v0.6 follows it;
check the live repository before making any new commit.

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
authorised technical restart **initially for S2-I1 only**. This was a conversational decision made
after ratification of Project Status v0.4; it superseded v0.4's historical "not authorised" state.
The owner subsequently authorised S2-I2 design and implementation as distinct bounded steps and
ratified its successful Windows gate on 2026-10-16.

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

**S2-I2 - COMPLETE / WINDOWS ACCEPTANCE PASS / OWNER-RATIFIED 2026-10-16 / CODE COMMITTED.**

The owner separately authorised S2-I2 design and implementation, ratified Design Plan v0.4
(including the three numeric registration thresholds), and accepted the Windows result conditional
on Claude's agreement. Claude independently confirmed PASS on original LP (mandatory primary)
and `LG_576i_3_LP_blocky` (S2-I2-only secondary diagnostic/control). The reviewed nine-file
implementation v0.1 was committed and pushed at
`190bd06ded88130ffddac7bb9adde4175d82f9f8` (parent `2286341`); Claude verified the
pushed GitHub source ZIP and that all six immutable Stage 1 indexes remained unchanged.

```text
                                      Original LP       LP_blocky
Eligible quality frames:              202 (B 0,1 out)   204
3x3 shifted-label registration:       PASS              PASS
Column-phase registration:           PASS              PASS
Same-field row-phase registration:    PASS              PASS
Deliberately wrong offsets blocked:  7/7               7/7
Overall spatial-registration gate:   PASS              PASS
```

The mandatory same-field row-phase test closes the demonstrated +1/+2-line blind spot of the
original proposed two-test spatial gate. The data also include read-only seam/step-strength and
proxy-labelled detectability reporting in both directions, with frame/GOP uncertainty; no
filtering, denoising, tuning or K0 kernel selection occurred. LP_blocky's scratch index
(SHA-256 `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238`)
remains **non-baseline and uncommitted**. Its S2-I2-only role does not grant it an S2-I3 role.
Locked hold-outs were not exposed.

Claude's Windows verification v0.2 reports byte-identical numerical CSVs from BestSource and
its separate FFmpeg rehearsal; that is strong evidence of corresponding decoded luma, **not** a
pixel-by-pixel proof. The gate checks **spatial grid registration**. A one-frame temporal slip
passed in an LP mutation, and a field swap passed in both recordings; picture-type checks provide
separate but incomplete temporal correspondence protection. A field-order swap is not detectable
by the registration measurements. These limits belong in the durable S2-I2 gate report.

**Step-B records are separate from the accepted code commit.** The bounded Step-B
documentation/evidence commit installs the owner-ratified S2-I2 evidence report at `docs/REPOSITORY/S2_I2_Evidence_and_Gate_Report_v0_1.md`, the 25 numerical/textual
Windows evidence files under `experiments/stage2/results/S2_I2_v0_1/`, reviewed supporting
documents and this status v0.6 in place of v0.5. The evidence is extracted at Step B from the
owner's untracked `experiments/stage2/Z/VapourSynth-mpeg2Deblock_S2_I2.zip` and its 25 SHA-256
values checked before staging. The scratch `.idx` is excluded; independent post-push
verification of the evidence hashes follows.

**S2-I3 THROUGH S2-I10 ARE NOT AUTHORISED.** Stage 2 Experimental Design v0.6 remains unchanged.
The owner-requested all-16-source objective census at S2-I8 is a separately recorded plan,
not yet incorporated into the ratified Stage 2 v0.6 text; carry it into that document's next
substantive revision without changing the hold-out restrictions.

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
docs/REPOSITORY/S2_I2_Evidence_and_Gate_Report_v0_1.md  accepted S2-I2 evidence; installed by Step B
docs/REPOSITORY/00_PROJECT_STATUS_v0_6.md               current-state index; replaces v0.5 at Step B
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
  unchanged frozen sources/six baseline indexes and zero owner-identity hits;
- ratified Project Status v0.5 was installed at `2286341`, after the accepted S2-I1 code;
- S2-I2 was subsequently authorised, passed Windows acceptance on original LP and LP_blocky, and
  was owner-ratified on 2026-10-16 after Claude's independent verification;
- its nine-file v0.1 implementation commit `190bd06` was pushed and GitHub-verified by Claude;
  all six frozen indexes remained unchanged.

The pre-reset SHAs and deleted artifacts remain useful as externally recorded historical provenance,
but they are **removed from current repository history**. No current project procedure should assume
that they can be checked out from the repository.

The interim reset was **not Development Closure**. Restricted Media remains intentionally present and
authorised for active project development under `NOTICE.md`.

---

## 6. Current restart gate

The coordinated cleanup/reconciliation correction set, owner-identity scrub, interim history reset,
role-handover refresh and bounded final KB/repository verification were completed before restart.
Project Status v0.4 recorded that completed gate. The project owner authorised the bounded S2-I1
restart on 2026-10-14 and later separately authorised S2-I2. Both increments have now passed owner
Windows acceptance and independent Claude verification, as recorded in section 3.

The authorisation boundary is now:

```text
S2-I1         AUTHORISED 2026-10-14; COMPLETE / ACCEPTED / COMMITTED at 4221f7f
S2-I2         SEPARATELY AUTHORISED; COMPLETE / PASS / RATIFIED 2026-10-16;
              code committed and pushed at 190bd06; records installed by Step B
S2-I3..I10    NOT AUTHORISED; require separate owner decisions
```

This status file does not itself authorise any further technical increment. Stage 2 v0.6 remains
in force, including its experiment controls and increment sequence. The S2-I3 entry outline is
discussion material only, including the candidate M4a pixel-score option and preservation of the
fixed-QP / K0-freeze / odd-GOP comparison boundary. Any S2-I3 design or implementation activity
requires a new explicit owner authorisation.

**Development Closure** remains a future, separate lifecycle event. It occurs only when the project
owner expressly declares active development finished. At Development Closure all Restricted Media is
removed from the current repository tree and project-controlled assets/storage, and at or promptly
after closure another history purge/reset is performed so Restricted Media is absent from the
resulting repository history. The narrow ChatGPT/Claude AI development-media authorisation ends at
that point. The repository may then continue as an ongoing maintenance project.

Markdown EOL/hash policy remains unchanged: no repository-wide `*.md eol=crlf` rule is added.
Project-authored documents delivered by either chat for review/application are US-ASCII with CRLF
line endings and mechanically checked before delivery, subject to the two explicitly named
historical-source exceptions below. Git-stored and GitHub source-archive forms of Markdown may
be LF. Any byte hash/EOL assertion must identify the representation being checked.

**Owner decisions ratified 2026-10-16 for the bounded Step-B commit:**

1. **Evidence byte preservation - YES.** Add exactly
   `experiments/stage2/results/** -text` to the root `.gitattributes`, limited to the S2-I2
   numerical/textual evidence subtree. Confirm via `git check-attr` BEFORE staging evidence;
   verify all 25 extracted Windows-file SHA-256 values before staging and again from GitHub
   after push. Applied in the Step-B commit.
2. **Narrow D-23 US-ASCII exception - YES.** Retain exactly these two verbatim third-party
   historical records unmodified, including their existing UTF-8 punctuation and names:
   `docs/ChatGPT_Review_of_Copilot_Grok_MPEG2_Block_Detection_v0_1_FOR_CLAUDE.md` and
   `docs/COPILOT-MPEG2_Deblocking_VHS_DVD_Research.md`. The exception does not apply to
   other repository documents. Claude has cleared the original research source for identity,
   NOTICE and rights-related recordkeeping; neither source is technical authority.

These two decisions do **not** authorise blanket staging or repository modification by the assistant.
Expected trailing-whitespace warnings in unchanged historical documents/evidence are not a
commit-failure gate: only `git diff --cached --check -- .gitattributes` is a STOP whitespace
check; numerical evidence integrity is verified using 25 declared hashes before staging and
again after push.

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

The handovers are continuity aids, not technical authority or authorisation for subsequent
increments. Their historical as-at statements do not override the later accepted S2-I1 and S2-I2
results or independently authorise S2-I3.

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

S2-I2-ONLY REGISTRATION / DESCRIPTIVE DIAGNOSTIC CONTROL
    LG_576i_3_LP_blocky (index remains non-baseline scratch; no S2-I3 role by default)

PRESENT BUT UNASSIGNED / SPARE
    LG_576i_1_XP and _blocky
    LG_576i_2_SP and _blocky
    TEST_3A_A002 and _blocky
    LG_576i_4_EP_blocky
    LG_576i_5_MLS_blocky
```

Do not infer properties or assign experimental roles to the unassigned material without explicit
analysis and owner-approved disposition. LP_blocky's temporary S2-I2-only assignment does not
relax the original LP development or EP/2A/4A hold-out boundaries.

---

## 9. Change log

### v0.6 - 2026-10-16 (RATIFIED)

- Prepared exclusively from the ratified v0.5 Windows-CRLF source with SHA-256
  `a5f19fa8c9dfd83b8d701b4e327f48555be613f75558938f328e6c53f61881da`;
  preserves all earlier change-log entries and historical repository provenance.
- Records S2-I2 COMPLETE / WINDOWS ACCEPTANCE PASS / owner-ratified 2026-10-16 and the
  independent Claude verification on LP and LP_blocky; documents spatial-only limitations.
- Records the pushed and verified nine-file S2-I2 code commit `190bd06` following status
  commit `2286341`; no Stage 1 index baseline or production-filter changes.
- Records the same-field row-phase registration test and S2-I2-only LP_blocky diagnostic role;
  leaves S2-I3 and later increments NOT AUTHORISED and Stage 2 Design v0.6 unchanged.
- Installed by the separate Step-B gate-report / numerical-evidence / document /
  status-replacement commit. The scratch LP_blocky index is excluded from Git.
- Records the owner's 2026-10-16 **YES** decisions: preserve exact Windows evidence bytes
  using an evidence-only `-text` attribute, and allow two named historical UTF-8 source
  records unchanged under a narrow D-23 ASCII exception. Both are applied in the Step-B commit.
  No general D-23, NOTICE or media-rule change.
- Supersedes v0.5: v0.6 added and v0.5 removed in the same bounded Step-B commit, after
  Claude final review and owner ratification. Claude final-review corrections applied so the
  text is true as at its installing commit.

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
