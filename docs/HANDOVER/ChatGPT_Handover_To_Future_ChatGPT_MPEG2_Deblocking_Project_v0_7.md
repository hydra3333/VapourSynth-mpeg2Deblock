# ChatGPT Handover to Future ChatGPT Chat
## MPEG-2 Macroblock Index / VapourSynth Deblocking Project

**Filename:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md`
**Version:** 0.7
**Date:** 2026-10-14
**Author:** prepared by Claude on behalf of the ChatGPT role, because the ChatGPT development chat
reached its conversation limit without warning before it could refresh this handover. The content is
reconstructed from the committed v0.6, the last ChatGPT deliverables (S2-I1 v0.1 and v0.2 packages and
their review requests/evidence), Claude's reviews/executions and the project owner's relayed
messages. Where something is ChatGPT-internal and not visible to Claude, this file says so.
**Status:** REVIEW CANDIDATE for the current ChatGPT role-specific continuity handover. Not repository
authority. Current ratified repository authorities prevail on any conflict.
**As-at boundary:** repository HEAD `c45dcf0923cbbbe335266d2c4302327f16ab94fe` (pushed; `main` ==
`origin/main`), technical restart AUTHORISED for S2-I1 only, S2-I1 candidate v0.2 delivered and
cleared by Claude for the owner's Windows run, not yet run/committed.
**Supersedes:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_6.md` once accepted/installed

---

## Handover continuity purpose and maintenance rule

This document is fundamentally a communication from the current ChatGPT development chat to the
future ChatGPT chat that will eventually replace it.

Its purpose is **continuity**, not merely document indexing.

A successor should be able to read this handover and obtain a strong working understanding of the
project **as understood by this chat at the stated as-at point**, including useful knowledge that may
be spread across repository authorities, migration records, review history, the project owner's conversational
decisions, current working practice and unresolved items.

Accordingly, this handover should preserve, where materially useful:

- current project/repository/status state;
- current roles and working process;
- ratified rules and decisions;
- important the project owner decisions made in conversation, including decisions not yet formally propagated
  into repository documents;
- evolved working conventions and approaches;
- current technical understanding and rationale needed to avoid rediscovery;
- what is settled, provisional, open, superseded or explicitly rejected;
- important negative knowledge: things deliberately not being done;
- current sample roles and evidence limitations;
- immutable regression baselines;
- current build/test/plugin state;
- outstanding documentation/knowledge gaps;
- immediate next work;
- likely following work;
- explicit blockers and authorisation gates;
- known traps, caveats and lessons that would otherwise be easy to repeat;
- references to owning authority/evidence documents where exact detail belongs elsewhere.

Repository authorities still prevail on conflict. This handover does **not** replace them.

However, references must not make the handover so skeletal that a successor has to reconstruct the
project's present working model from scratch.

### Successor takeover model

At an actual chat handover, the successor should:

1. read this handover in full;
2. establish the live repository HEAD/status and current document versions;
3. read the named owning authorities/evidence needed for the task;
4. determine the **delta between this handover's as-at point and the actual takeover point**;
5. update its working understanding only for that delta;
6. continue development from the resulting reconciled current state.

The handover should therefore be refreshed periodically when major project state changes, not merely
written at the final moment when a chat is nearly exhausted.

The Claude role handover is intended to follow the same continuity purpose for Claude's independent
reviewer/designer role.

---

## 0. First actions for a future ChatGPT chat

**You are taking over mid-increment.** The previous ChatGPT chat ended abruptly (conversation length
limit) on 2026-10-14 immediately after delivering the S2-I1 v0.2 candidate. Read this section and
section 18 before anything else.

First establish the live repository state (`git log --oneline -5`, `git status --short`), then read
the current authorities in this order:

```text
docs/REPOSITORY/00_PROJECT_STATUS_v0_4.md
docs/REPOSITORY/05_DECISIONS_v1_2.md
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md
docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md
docs/REPOSITORY/Stage2_Experiment_Design_v0_6.md
NOTICE.md
README.md
```

(Per D-23 a versioned reference means that version **or later**.)

For build, Visual Studio, CI and release facts, use the live project files and workflow:

```text
vs/VapourSynth-mpeg2Deblock/*.vcxproj
.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml
.github/workflows/expected_stage_bplus_switches.csv
README.md  (Building / release orientation)
```

Also read the latest Claude role handover (`Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md` or later).

At this handover's as-at point:

```text
Stage 1:              COMPLETE / PASS / FROZEN
Stage 2 design:       v0.6 RATIFIED
Technical restart:    AUTHORISED by the project owner 2026-10-14, beginning with S2-I1 only
S2-I1:                IN PROGRESS - candidate v0.2 delivered, Claude-cleared, awaiting owner Windows run
S2-I1 code in Git:    NONE YET (uncommitted owner working files only)
S2-I2 and later:      NOT AUTHORISED
```

Immediate work for the successor (detail in section 18.6):

1. obtain the owner's Windows results for S2-I1 v0.2 (or ask the owner to run it);
2. apply the one-line BAT logging fix (Claude v0.2 S1) before commit;
3. support the first S2-I1 commit (v0.2 files only; v0.1 files deleted locally first);
4. report the S2-I1 result to the owner and propose the status-file update;
5. **do not start S2-I2** until the owner separately authorises it.

## 1. Purpose and authority boundary

This document exists so a future ChatGPT development chat can resume the project safely if the
current chat is unavailable or reaches its conversation limit.

It records:

- project identity and roles;
- current repository baseline and post-reset commits;
- current authority set;
- durable technical knowledge needed to avoid regressions;
- Stage 1 status and the in-progress Stage 2 S2-I1 increment, in enough detail to resume it;
- sample roles;
- immutable regression-baseline policy;
- current Restricted Media policy and lifecycle;
- build/CI/release continuity;
- the authorisation gates still in force;
- cautions, traps and non-goals.

This handover is **not** a technical authority.

Rules:

1. `00_PROJECT_STATUS_v0_4.md` (or later) is the first concise current-state index.
2. The owning ratified authority wins if this handover differs from it.
3. Build settings are owned by the Visual Studio project files.
4. CI/release verification is owned by the live workflow and `expected_stage_bplus_switches.csv`.
5. README `Building` and the current role handovers carry practical procedure/continuity summaries.
6. `NOTICE.md` separately governs Restricted Media.
7. Review documents explain provenance; they do not outrank current authority.
8. Superseded files and pre-reset commit SHAs are historical provenance only.
9. The deleted migration handback is not current authority and must not be reconstructed as one.
10. A project-owner decision made in conversation and not yet propagated into a repository authority
    is recorded here as such (section 17.2); do not pretend the repository already says it.

## 2. Project identity

### 2.1 Active repository

GitHub:

```text
https://github.com/hydra3333/VapourSynth-mpeg2Deblock
```

Active local repository:

```text
E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock
```

Branch:

```text
main
```

Current fresh-history root commit:

```text
11f47427624bf5f68b3426fe9f58aa26d40e47f7
```

Current root tree:

```text
45ad1f16a24d3cce0411863a9804472efa1c8529
```

The root has zero parents. Its author and committer are both `hydra3333 <10749357+hydra3333@users.noreply.github.com>`. The fresh HTTPS clone was verified with:

```text
HEAD == origin/main == 11f47427624bf5f68b3426fe9f58aa26d40e47f7
reachable commit count == 1
tracked file count == 124
tracked .idx count == 6
working tree clean
old pre-reset commit object absent
```

The exact tree equals the independently verified pre-reset cleanup tree. Therefore the history reset
changed repository ancestry/commit metadata, not tracked file content.

The externally recorded pre-reset source identity is:

```text
fd82d78715ed6a61ef4e80b9769655eefe23c384
```

That SHA is provenance only. It is intentionally absent from current repository history. The old
commits are correctly described as **removed from repository history**; direct-SHA views/unreachable
server objects may persist until GitHub garbage collection.

The old local clone was push-disabled, quarantined, replaced by a fresh HTTPS clone, verified, and then
deleted. Do not recover current work from an old pre-reset clone.

#### Post-reset commits (as at this handover)

```text
11f4742  fresh zero-parent root (tree 45ad1f16...)
eac5526  first of two handover-install commits
bfb6cc2  second handover-install commit (adds ChatGPT v0.6)
         net of the two: ChatGPT v0.6 + Claude v0.8 added; ChatGPT v0.5 + Claude v0.7 deleted
c45dcf0  Refresh project status after history reset (00_PROJECT_STATUS v0.3 -> v0.4)
```

`c45dcf0923cbbbe335266d2c4302327f16ab94fe` is HEAD and was pushed (`bfb6cc2..c45dcf0 main -> main`).
Claude verified the GitHub source ZIP of `c45dcf0`: exactly two path changes versus `bfb6cc2`
(status v0.3 deleted, v0.4 added), all other 123 files byte-identical, zero owner-identity hits. All
commits after the root are documentation-only; every frozen hash and the six `.idx` are unchanged.
The tree has 124 files.

The local working tree additionally holds **uncommitted** S2-I1 files under `experiments\stage2\`
(v0.1 files already placed by the owner; v0.2 to be placed). See section 18.

Repository-local Git identity for future commits is:

```text
user.name  = hydra3333
user.email = 10749357+hydra3333@users.noreply.github.com
```

### 2.2 Fresh `v0.1.0` snapshot pre-release

A replacement `v0.1.0` pre-release was published against the new root commit. It remains explicitly
**NOT FOR USE, SNAPSHOT RELEASE ONLY** and is not a functional deblocking release.

Workflow-built asset:

```text
mpeg2Deblock-v0.1.0-win-x64.zip
SHA-256 (owner-reported): f8ddb2da0b38e9639231fc63600c28da0f0bf0e95429a5033812726f36d17785
```

The remote `v0.1.0` tag points to the new root commit.

### 2.3 Previous local/reference trees

The pre-history-reset clone has been deleted after fresh-clone verification.

Any older pre-migration/source tree still present elsewhere is rollback/reference material only. Do
not use it as the active development tree.

### 2.4 Important repository locations

```text
src\Mpeg2BlockInspector\
    frozen Stage 1 inspector/indexer source

tools\Stage1_Inspector_Analyzer_v0_2.py
    frozen Stage 1 analyzer

vs\VapourSynth-mpeg2Deblock\
    x64 Visual Studio solution/projects

TESTING\
    Stage 1/regression test drivers and support files

VHSC_samples\
    16 Source Recordings, six accepted .idx baselines, six .log files
    recordings are Restricted Media; indexes/logs are not Restricted merely by derivation

docs\REPOSITORY\
    current authority/status documents

docs\HANDOVER\
    current role continuity handovers

.github\workflows\
    CI/release workflow plus strict expected-switch CSV
```

Stage 2 experimental Python lives under:

```text
experiments\stage2\
```

At the as-at point that folder exists only in the owner's working tree (uncommitted). The first S2-I1
commit will add the accepted S2-I1 files there; scratch outputs (generated 4A-blocky index, logs,
`.m2v`) are never committed.

## 3. Product architecture and goal

The project is an MPEG-2-specific, index-driven VapourSynth deblocker.

Conceptually:

```text
MPEG-2 stream
    ->
Mpeg2BlockInspector.exe
    ->
matching MPEG-2 macroblock index

VapourSynth decoded clip
    +
matching index
    +
user strength
    ->
mpeg2Deblock
    ->
deblocked output
```

The production architecture is **index-driven by definition**.

The plugin does not parse `.mpg`/MPEG-2 program-stream input itself.

The external inspector/indexer provides coded-structure metadata; the future VapourSynth filter
operates on decoded pixels plus the matching index.

---

## 4. People and workflow

### the project owner

- project owner;
- final authority;
- project manager;
- runs/controls local repository, builds and tests;
- ratifies decisions and acceptance;
- judges visual quality.

### ChatGPT

- primary drafter / implementation partner;
- technical-mechanics analysis;
- specification and test drafting;
- coding when authorised;
- reviews Claude proposals;
- must not promote drafts silently into authority.

### Claude

- independent reviewer / designer;
- performs cold review against pristine source/evidence/current authority;
- identifies blocking versus optional issues;
- maintains its own role handover.

### Claude's execute-before-owner-runs duty (owner ruling 2026-10-13)

After several ChatGPT-supplied tools failed when the owner ran them, the owner ruled that **Claude
executes or rehearses every tool and procedure before the owner runs it**. Practical consequences
for ChatGPT:

- deliver tools as a package Claude can execute: code, run procedure, stated expected outputs and
  hashes, manifest;
- state what you could not execute (for example Windows CMD, VapourSynth/BestSource) so Claude can
  rehearse or audit it;
- Claude cannot run Windows CMD itself; BAT files therefore get a line-by-line CMD audit (redirections,
  handle numbers, ERRORLEVEL, quoting) in addition to Linux rehearsal of the commands they call;
- the owner runs a tool only after Claude has cleared it.

### Default technical workflow

```text
ChatGPT drafts
    ->
Claude independently reviews
    ->
The project owner resolves / ratifies
    ->
ChatGPT implements or proceeds
```

The project owner may explicitly close a review cycle and directly ratify a bounded change, as occurred for the
final Restricted Media policy / Stage 2 v0.6 alignment.

The project owner remains final authority.

---

## 5. Current repository authority/status set

### 5.1 Current concise status index

```text
docs/REPOSITORY/00_PROJECT_STATUS_v0_4.md
Version: 0.4
Status: RATIFIED 2026-10-14 by the project owner
Committed: c45dcf0 (replaced and deleted v0.3 per D-23)
```

This is the first current-state document a future development chat should inspect. It is an index,
not competing technical authority.

v0.4 records the fresh-history root, the handover install, the last verified pre-refresh commit
`bfb6cc2`, pre-reset SHAs as provenance only, and "technical restart NOT AUTHORISED" **as at its
ratification**. The owner authorised restart later the same day (section 17.2); that decision is not
yet propagated into a status file. Propose a status refresh (v0.5) together with or after the first
S2-I1 commit.

### 5.2 Decision authority

```text
docs/REPOSITORY/05_DECISIONS_v1_2.md
Version: 1.2
Status: RATIFIED
Date: 2026-10-13
```

Important current decisions include:

```text
D-23  drafting/version/current-tree/identity/EOL conventions
D-24  production architecture is index-driven
D-25  native MPEG-2 4:2:0 chroma is in production scope
D-26  evidence hierarchy prioritises real recorder material
```

D-23 now includes the versioned-filename/current-tree predecessor-removal rule, version-or-later
reference rule, identity-neutral project-artifact rule and the deliberate no-repository-wide-Markdown-
renormalisation policy. Earlier decisions superseded or amended by current decisions must not be
revived accidentally.

### 5.3 Deblocking concept authority

```text
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md
Version: 1.2
Status: RATIFIED
Date: 2026-10-11
```

Version 1.2 incorporates the corrected FRAME/FIELD/NONE geometry, including NONE having no internal
transform seams. Items explicitly labelled HYPOTHESIS or OPEN remain hypotheses/open questions despite
document ratification.

### 5.4 Index-format authority

```text
docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md
Version: 0.4
Status:
    current ratified-constraints baseline
    DRAFT / NOT FROZEN final binary packing
```

Critical distinction:

```text
INDEX-DRIVEN ARCHITECTURE:
    decided

INDEX CONSTRAINTS / SEMANTICS NEEDED BY CURRENT WORK:
    current baseline

FINAL BINARY PACKING:
    not frozen
```

### 5.5 Stage 1 evidence

```text
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md
Status: RATIFIED / Stage 1 frozen
```

### 5.6 Stage 2 design

```text
docs/REPOSITORY/Stage2_Experiment_Design_v0_6.md
Version: 0.6
Status: RATIFIED
Date: 2026-10-13
```

Version 0.6 is the current Stage 2 design. It synchronized the Restricted Media/lifecycle wording,
current sample-role clarifications, diagnostic-output treatment and bounded `TEST_4A_A003_blocky.idx`
plan while preserving the established algorithmic scope and S2-I1..S2-I10 implementation sequence.

Stage 2 implementation has started with S2-I1 only (section 18). No S2-I1 code is committed yet.

## 6. Migration, build, CI and release continuity

### 6.1 Migration status and deleted handback

Repository migration remains historically:

```text
CLOSED / RATIFIED
Date: 2026-10-11
```

The former final common migration handback v0.21 was deliberately deleted from the current tree on
2026-10-13 and was **not** re-issued as v0.22. The later repository-history reset removed the old
commit ancestry from current Git history as well.

Do not direct a successor to the deleted archive. Build/CI/release ownership now rests with the live
project files, workflow and expected-switch CSV, with README and role handovers carrying procedural
continuity.

### 6.2 Durable migration/build acceptance facts

The final migration acceptance had established, for plain-CMD Debug and Release x64 rebuilds:

```text
Mpeg2BlockInspector:
    17 accepted legacy-C warnings
    0 errors
    build exit code 0

mpeg2Deblock plugin:
    0 warnings
```

The 17 inspector warnings are the known legacy-C set. New/different warnings are a delta to explain,
not something to accept automatically.

All six accepted reference `.idx` hashes matched through migration, cleanup, owner-identity scrub,
pushed-cleanup verification and fresh-history tree verification. Stage 1 remains frozen.

### 6.3 Build-system authority and orientation

The Visual Studio solution is x64-only and contains two projects:

```text
Mpeg2BlockInspector.exe
    frozen Stage 1 legacy-C inspector/indexer baseline

mpeg2Deblock.dll
    C++20 VapourSynth API4 production-plugin scaffold
    currently exposes only mpeg2deblock.Identity
    NOT yet a deblocking filter
```

Build settings are owned by the `.vcxproj` files. Accepted high-level invariants include:

```text
Visual Studio 2026
x64 only
Debug + Release
AVX2 minimum CPU target
Release /MT
Debug /MDd
/fp:precise
plugin C++20
inspector legacy C
project files own compiler/linker policy
```

Release `/MT` carries an important DLL-boundary rule: do not casually pass ownership of CRT-allocated
memory/objects across module boundaries for another module to free/manage. VapourSynth objects should
follow VapourSynth API ownership.

The scalar implementation planned later is a **reference path inside the AVX2-targeted binary**, not
a pre-AVX2 compatibility fallback.

### 6.4 CI switch gate and release rules

Current CI/release authority:

```text
.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml
.github/workflows/expected_stage_bplus_switches.csv
```

The workflow supports:

- manual verification builds from any branch;
- published-Release builds only when the tagged commit belongs to `main` history;
- Debug and Release x64 rebuilds of both native projects;
- strict comparison of the reviewed CL/LINK/RC switch inventory against the CSV;
- positive HostX64\x64 compiler/linker invocation checks for both projects/configurations;
- release-binary inspection and packaging;
- a published-release ZIP whose root contains only `Mpeg2BlockInspector.exe`, `mpeg2Deblock.dll`,
  `LICENSE` and `NOTICE.md`.

The CSV is the executable expected-switch authority. A legitimate switch change requires review of
the actual difference and a coordinated update of the CSV/workflow reference; do not merely loosen
the gate until CI passes.

The fresh-history replacement `v0.1.0` pre-release was successfully rebuilt/published from the new
root and attached `mpeg2Deblock-v0.1.0-win-x64.zip` with owner-reported SHA-256
`f8ddb2da0b38e9639231fc63600c28da0f0bf0e95429a5033812726f36d17785`.

### 6.5 VapourSynth header provenance

Current provenance records:

```text
VapourSynth4.h   R81
VSHelper4.h      R81
VSScript4.h      R81
VSConstants4.h   R81
VSVulkan4.h      retained post-R81 master snapshot
```

The old correction commit SHA belongs to pre-reset provenance and is intentionally not part of
current history. The current vendored files are the authority; do not revive historical R78 claims.

## 7. Settled architecture decisions

### 7.1 D-24 - index-driven production filter

Do not implement:

- a pixel-only production seam-position detector;
- Family B;
- an index-vs-pixel-only architecture contest.

The index supplies authoritative coded-structure geometry/eligibility.

Pixels are still used at known candidate seams for local decisions such as:

- block-versus-real-edge judgement;
- activity/detail protection;
- correction limiting.

Conceptual split:

```text
INDEX
    -> candidate geometry / coded-state semantics

PIXELS
    -> local blocking/detail judgement
    -> protection / limiting

INDEXED QP + USER STRENGTH
    -> correction scale
```

### 7.2 D-25 - native 4:2:0 chroma in production scope

Stage 2 does not need to re-prove that chroma blocking exists.

It must establish a safe/useful production treatment, including:

- threshold;
- strength;
- horizontal/vertical treatment;
- interlaced access;
- no field mixing;
- no colour smearing;
- useful visual benefit.

### 7.3 D-26 - evidence hierarchy

Primary product evidence:

```text
real LG recorder material
```

Secondary evidence:

```text
software blocky transcode pairs
```

No single metric decides the project.

The project owner's visual judgement on target material remains essential.

### 7.4 No external-deblocker yardstick

No existing external deblocker is a planned Stage 2 comparison yardstick.

Do not add one unless the project owner explicitly reopens that question for a concrete reason.

---

## 8. Critical coded-geometry knowledge

### 8.1 FRAME / FIELD / NONE semantics

The transform state describes **coded residual transform geometry**.

It is not merely whether a `dct_type` bit was present or read.

```text
FRAME
FIELD
NONE
```

`NONE` applies where no coded residual transform geometry exists, including:

- skipped macroblocks;
- effective-CBP-zero non-intra macroblocks.

A `dct_type` bit being read does not by itself mean FRAME/FIELD residual geometry exists.

### 8.2 Internal seam rules

For coded FRAME/FIELD macroblocks:

```text
internal vertical luma x=8 seam:
    exists
```

For NONE:

```text
internal vertical x=8 seam:
    NONE

internal horizontal transform seam:
    NONE

candidate locations:
    outer macroblock edges only
```

For FRAME:

```text
internal horizontal transform seam:
    exists
    uses same-field sample access in interlaced frame material
```

FIELD has its own field-transform horizontal geometry.

### 8.3 Useful spacing intuition

Ratified concept consequences include approximately:

```text
vertical direction, FRAME:
    about 4 samples per field from outer MB edge to internal centre seam

vertical direction, FIELD:
    about 8 between MB edges

vertical direction, NONE:
    about 8 between MB edges because there is no internal horizontal seam

horizontal direction, FRAME/FIELD:
    8 between MB edge and internal x=8 seam

horizontal direction, NONE:
    16 between MB edges because there is no internal x=8 seam
```

These are geometry consequences, not permission to infer seam positions from pixels.

### 8.4 Frame-owned interlaced processing

The design remains frame-owned.

Do not split decoded images into independently filtered field images.

Use parity-aware/same-field sample access where needed to avoid mixing temporally different fields.

### 8.5 Partially-coded residual caveat

`06_DEBLOCK_CONCEPT.md` v1.2 carries an OPEN/HYPOTHESIS item concerning partially coded
FRAME/FIELD macroblocks where CBP may leave some luma blocks prediction-only.

Do not turn that hypothesis into production policy pre-emptively.

Investigate only if Stage 2 diagnostics show unexplained behaviour that justifies it.

---

## 9. Chroma knowledge retained from reference-decoder work

The project previously established the following bounded findings from the inspected MPEG-2
reference-decoder implementation:

### V1

Luma frame-picture block placement supports the relevant FRAME/FIELD geometry.

### V2

For MPEG-2 4:2:0, chroma transform placement does not simply follow luma `dct_type`.

### V3

In the inspected reference-decoder MPEG-2 4:2:0 path:

- chroma uses the macroblock's same `quantizer_scale`;
- the inspected luma matrix-selection path applies to 4:2:0 chroma.

Treat this as a verified implementation finding from the inspected decoder.

Do not silently promote it to a stronger normative H.262 statement without separate standards
verification.

### V4

For inspected 4:2:0 field prediction in frame pictures:

```text
even chroma line -> top field
odd chroma line  -> bottom field
```

This supports the premise for parity-aware chroma handling.

The exact post-filter chroma access/treatment remains a Stage 2 evidence question under the ratified
design.

---

## 10. Stage 1 status and immutable indexes

Stage 1 is:

```text
COMPLETE / PASS / FROZEN
```

Do not reopen it without concrete evidence of a requirement.

In particular, do not reopen merely to collect more metadata because it might be interesting.

The six accepted tracked `.idx` files are immutable regression baselines.

Rule:

> Never regenerate an accepted `.idx` merely to make a later test pass.

Known LP baseline:

```text
VHSC_samples\LG_576i_3_LP.idx
SHA-256:
849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011
```

Migration/cleanup regression checks preserved all six accepted indexes.

---

## 11. Current sample roles

Recorder quality order, best to worst:

```text
XP -> SP -> LP -> EP -> MLS
```

That quality order is **not** the same thing as Stage 2 experimental role.

### Primary development / tuning

```text
LG_576i_3_LP
```

Known important characteristics include:

```text
720x576
strong real-recorder quantisation
rich FRAME/FIELD/NONE mixture
~97.06% mixed FRAME/FIELD frames
I/P/B coverage
```

### Locked interlaced hold-outs

```text
LG_576i_4_EP
TEST_4A_A003 original
TEST_2A_A001 original
```

Do not tune on them.

### Progressive/control

```text
LG_576i_5_MLS
```

Important:

```text
352x288
progressive/control role
FIELD = 0
```

Do not use MLS as a FRAME-versus-FIELD interlaced exercise source.

### Secondary paired-reference / stress

```text
TEST_4A_A003_blocky
TEST_2A_A001_blocky
```

These remain secondary evidence.

The known blocky transcodes use effective QP 62 throughout, so they cannot establish the value of a
spatial per-MB QP map.

### Present but unassigned / spare

```text
LG_576i_1_XP and _blocky
LG_576i_2_SP and _blocky
TEST_3A_A002 and _blocky
LG_576i_3_LP_blocky
LG_576i_4_EP_blocky
LG_576i_5_MLS_blocky
```

Do not infer their resolution/interlace/transform distributions or silently assign hold-out/tuning
roles.

Analyse first and obtain owner-approved disposition if they become relevant.

---

## 12. Stage 2 design and implementation sequence

### 12.1 Current state

```text
Stage 2 design:
    v0.6 RATIFIED

Technical restart:
    AUTHORISED 2026-10-14 by the project owner, beginning with S2-I1 only

S2-I1:
    IN PROGRESS (candidate v0.2 delivered and Claude-cleared; owner Windows run pending)

S2-I2 .. S2-I10:
    NOT AUTHORISED; each advance needs the owner's separate decision after reviewed results
```

### 12.2 S2-I1 scope (Stage 2 v0.6 sections 6.1 and 19)

```text
S2-I1
    read-only Stage 1 index reader / validation
    reproduce analyzer v0.2 summary totals for each formal clip
    if absent/untracked, generate + validate TEST_4A_A003_blocky.idx as a non-baseline candidate
    progressive_frame and picture-type handling
    leading-B quality exclusion accounting
    cheap temporal/structural checks: index records == BestSource frames, dimensions,
    record ordinals, supported picture structure
```

The generated `TEST_4A_A003_blocky.idx` is not a seventh accepted baseline and stays uncommitted
unless the owner separately decides otherwise. Full state and history are in section 18.

### 12.3 Ratified implementation order

```text
S2-I1
    read-only Stage 1 index reader / validation

S2-I2
    seam-map diagnostics
    spatial registration validation

S2-I3
    initial luma candidate kernel
    K0 selection on designated LP material

S2-I4
    fixed-QP versus real indexed per-MB QP comparison
    with K0 frozen

S2-I5
    real-QP luma kernel / threshold / strength development

S2-I6
    NONE policy and evidence-driven alternatives only

S2-I7
    bounded native 4:2:0 chroma experiment

S2-I8
    locked hold-out / no-harm evaluation

S2-I9
    secondary paired-reference reporting

S2-I10
    Stage 2 feasibility / metadata-retention gate report
```

Use the current Stage 2 v0.6 file for precise methodology. Do not implement from this abbreviated
handover summary.

## 13. Important Stage 2 methodological safeguards

These were already ratified before migration and remain current unless the Stage 2 authority says
otherwise.

### 13.1 Spatial registration must be validated

Temporal correspondence was established in Stage 1.

Before filtering-quality conclusions, Stage 2 must validate spatial index-to-pixel registration.

The ratified design includes detector-free controls such as:

```text
FRAME-versus-FIELD shifted-label contrast
x/y shifts around zero

8-pixel grid-phase checks
```

Correct registration should favour the expected zero alignment.

Diagnostics validate alignment; they do not replace index-driven geometry with pixel detection.

### 13.2 Stage 2 reader cross-check

The Stage 2 reader must reproduce accepted analyzer summaries for formal clips, including at least:

```text
record count
FRAME/FIELD/NONE totals
QP totals/histogram
```

Resolve any mismatch before filter experiments.

### 13.3 K0 tuning versus QP-map comparison

The ratified methodology separates material used to select K0 from material used to compare
fixed-QP versus real indexed QP.

Do not tune and evaluate that controlled comparison on the same designated evidence subset.

### 13.4 Leading B pictures

Leading B pictures before the first I picture are excluded from quality evidence but retained for
structural/robustness/diagnostic checks.

### 13.5 NONE QP caveat

For NONE macroblocks, the indexed QP is the quantiser scale in force at that point in the slice, but
it did not quantise residual in that macroblock.

Therefore boundaries touching NONE require separate reporting/interpretation where the design calls
for it.

---

## 14. Operational continuity rules and working conventions

These are not algorithm authority, but they materially affect safe project work with the project owner.

### 14.1 Command delivery on the project owner's Windows system

CMD copy/paste has repeatedly been unreliable: pasted command sequences may lose the first character
or concatenate unexpectedly.

For future command sets:

1. start with:

```cmd
cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"
```

2. keep commands short;
3. normally give **one command per code block**;
4. avoid long PowerShell one-liners when a simple CMD/BAT approach works;
5. where several controlled operations are needed, a reviewed `.bat` is often safer than a long
   paste sequence.

### 14.2 Git/change-control practice

For bounded controlled changes:

- use named staging by default;
- do not use `git add -A` casually;
- the project owner explicitly allowed `git add -A` on 2026-10-11 for a deliberate snapshot commit after the
  repository state had first been inspected and the intended snapshot scope was understood;
- inspect staged scope before commit;
- use `git diff --cached --check`;
- do not silently renormalise unrelated files;
- do not change frozen source/build settings merely because another task is nearby;
- interim commits are acceptable where useful; final cleanup can remove temporary material.

### 14.3 Verification proportionality

Use verification appropriate to the changed surface.

Examples:

- documentation-only edits do not automatically justify rebuild/index runs;
- build-adjacent changes should use the accepted build/smoke path;
- immutable tracked indexes are read-only regression baselines;
- unexpected build/file effects are STOP-and-investigate conditions.

### 14.4 Packaging and review

The project owner prefers multi-document review/application sets packaged as ZIPs.

For review-sensitive authority/policy changes, the normal pattern remains:

```text
ChatGPT drafts
Claude independently reviews
The project owner ratifies
ChatGPT applies/proceeds
```

But the project owner may explicitly close review and directly ratify a bounded decision. A successor must respect
the actual decision history rather than assuming every change requires one more review cycle.

### 14.5 Knowledge-management discipline

A key project-management lesson is to avoid knowledge drift and large piles of competing documents.

Therefore:

- identify an owning authority for durable technical knowledge;
- preserve useful continuity in role handovers;
- treat review/provenance documents as support, not competing current authority;
- explicitly mark superseded knowledge;
- do not infer silence as a decision;
- when a new conversational decision has not yet propagated into authority, record the gap rather
  than pretending the repository is already synchronized.

---

### 14.6 Lessons from the restart and S2-I1 so far (2026-10-14)

1. **Refresh this handover at every milestone**, not at the end. The previous chat reached its
   length limit without warning, immediately after delivering S2-I1 v0.2 and before updating the
   handover; Claude had to reconstruct this version. After each owner decision, commit or delivered
   package, update the handover (or at least a short addendum) before starting the next piece.
2. **Windows CMD: two processes must never append to the same file at the same time.** v0.1 piped
   `ffmpeg ... 2>>"%log%" | inspector ... >>"%log%" 2>&1`; CMD failed with "The process cannot access
   the file because it is being used by another process." Linux shells allow this, so a Linux
   rehearsal does not catch it.
3. **Windows CMD handle-number trap:** a digit immediately before `>`/`>>` is a handle number.
   `echo code: %rc%>>"%log%"` with `rc=0` becomes `0>>"log"` and nothing is logged. Write
   `>>"%log%" echo code: %rc%` (redirection first) or leave a space before `>>`.
4. **Frozen inspector short-read trap:** `getbits.c` `Fill_Buffer()` treats any `read()` shorter than
   2048 bytes as end of stream, pads with sequence-end codes, writes a COMPLETE index and exits 0.
   On Linux an ffmpeg pipe produced a 1-record LP index and a 2-record 2A-blocky index with exit 0.
   The Windows pipe produced all six accepted baselines correctly, but do not rely on it: for any new
   generation use `ffmpeg -> scratch .m2v -> inspector -b <file>`, and always gate on exact expected
   counts/totals or the BestSource frame count. The inspector itself stays frozen.
5. **Compare a new BAT against the accepted `TESTING` BATs** for every redirection, not only the
   command line; the accepted Stage 1 BAT logged only the inspector side of its pipe.
6. **State expected hashes/outputs** in every tool package so a run can be checked mechanically.

## 15. Restricted Media policy

The coordinated Restricted Media policy is ratified and applied in:

```text
NOTICE.md
README.md
docs/REPOSITORY/Stage2_Experiment_Design_v0_6.md
```

`NOTICE.md` is the governing exact text.

### 15.1 Source Recordings

Source Recordings are recordings expressly included for project testing/validation/diagnosis and
behaviour reproduction. At present this includes the video recordings under:

```text
VHSC_samples\
```

Media file type alone does not make unrelated project-made or third-party media a Source Recording.

### 15.2 Derived / Restricted Media

Restricted Media includes Source Recordings plus Derived Media. Derived Media includes:

- filtered/transformed picture or sound;
- crops/stills/difference images/audio extracts;
- visual or audible representations derived from Source Recording metadata or measurements;
- QP heat maps;
- seam-statistics plots;
- charts/maps/masks/similar media visualisations.

The project owner selected the cautious rule that such visualisations remain Restricted Media even
where they contain no recognisable original frame pixels.

### 15.3 What is not Restricted Media merely by derivation

Examples:

```text
.idx files
hashes
logs
source code
documentation
metadata
purely numerical/textual diagnostics
```

remain non-media unless they themselves contain or embed Restricted Media. A picture-like spatial
text grid is treated as a Derived Media visualisation rather than ordinary text diagnostics.

A document that embeds Restricted Media is treated as Restricted Media while that embedded media
remains; a media-free/redacted version may remain under ordinary project terms.

### 15.4 ChatGPT/Claude exception and lifecycle

During active development, Restricted Media may remain in the repository to the extent reasonably
necessary as project test/evidence/review material.

Until Development Closure, the project maintainer may supply Restricted Media to **ChatGPT and Claude
AI only**, and those services may access/use it, only as reasonably necessary for this project's own
development conversations. That narrow exception does not authorise other people/services, unrelated
reuse, publication, redistribution, post-closure retention, or model training/fine-tuning/adaptation.

Development Closure means the point at which the project owner expressly declares active development
finished. It is not the project/repository ceasing to exist; maintenance may continue afterward.

At Development Closure:

1. remove all Restricted Media from the current repository tree and project-controlled release/assets/storage;
2. create/verify the media-free closure tree;
3. perform the separately planned history reset/scrub so historical repository media copies are not
   part of the resulting repository history;
4. freshly realign local clones so old history cannot be accidentally reintroduced;
5. thereafter keep Restricted Media out of Git tree/history unless a separately reviewed and ratified
   decision says otherwise.

The 2026-10-13 fresh-history reset described elsewhere in this handover was **not** Development Closure
and intentionally retained the 16 active-development recordings.

## 16. Completed reconciliation, identity cleanup and fresh-history reset

The v0.5 handover described several items as pending. Those items are no longer pending.

### 16.1 Knowledge/policy reconciliation completed

The coordinated correction round:

- reconciled the project owner's narrow ChatGPT/Claude AI media-use authorisation into `NOTICE.md`,
  README and Stage 2 v0.6;
- ratified `05_DECISIONS_v1_2.md`, Stage 2 v0.6 and Project Status v0.3;
- resolved the Markdown/EOL question without a repository-wide `*.md eol=crlf` rule;
- established the current filename/version/predecessor-removal and identity-neutral artifact rules;
- deleted superseded/current-tree duplicates and all eight `docs/in-progress/` working files;
- deleted the v0.21 migration handback without replacement;
- scrubbed owner personal identity/location from retained current-tree project artifacts;
- preserved source/build/test/sample and six accepted `.idx` content unchanged.

The cleanup/application set was independently reviewed and verified before and after push.

### 16.2 Pre-reset cleanup provenance

The final verified pre-reset cleanup commit was:

```text
fd82d78715ed6a61ef4e80b9769655eefe23c384
```

It is retained here only as an **external provenance identifier** for the exact tree that was later
made the new root. It is not a current repository commit.

The tree was:

```text
45ad1f16a24d3cce0411863a9804472efa1c8529
```

### 16.3 Fresh-history reset

On 2026-10-13 the published `main` history was deliberately replaced with one zero-parent root commit:

```text
11f47427624bf5f68b3426fe9f58aa26d40e47f7
```

The root uses exactly the same tree `45ad1f16...`; therefore no tracked content changed.

Before the reset, the old `v0.1.0` Release and tag and all old GitHub Actions workflow runs (with
their stored artifacts) were deleted. After the reset, a fresh HTTPS clone proved one reachable commit,
124 tracked files, six `.idx`, clean status and absence of the old `fd82d78` object. The old clone was
push-disabled, quarantined and ultimately deleted.

A fresh `v0.1.0` snapshot pre-release was then published on the new root. The old commits are removed
from current repository history. Direct-SHA views or unreachable GitHub objects may persist until
GitHub garbage collection; do not claim physical erasure beyond what was verified.

### 16.4 Commit time-zone metadata note

Git commits also record the author/committer time-zone offset. The fresh root records the local `+1030`
offset. This is not a defect and does not require rewriting the root. If the project owner later prefers
future commits not to carry a locality signal, using UTC (`+0000`) for future commit metadata is an optional
Git-hygiene choice, not a project requirement. Any such change should be deliberate and verified with
`git show -s --format=fuller`.

## 17. Completed final gate and restart authorisation

### 17.1 Final knowledge-base / repository gate - COMPLETE

The sequence that v0.6 described as remaining is done:

1. ChatGPT v0.6 and Claude v0.8 were cross-reviewed (ChatGPT review of Claude v0.8: no MUST/SHOULD;
   Claude review of ChatGPT v0.6: one SHOULD - section 11 omitted three `_blocky` clips - applied,
   plus two optional edits) and installed in `eac5526`/`bfb6cc2`, deleting v0.5/v0.7.
2. Claude's bounded final KB/repository verification at `bfb6cc2` (GitHub ZIP): four-path delta only,
   122 other files byte-identical, zero identity hits, handovers consistent, 16/16 recordings
   accounted for. One SHOULD: `00_PROJECT_STATUS_v0_3.md` still described pre-reset history as
   current. Stage 2 v0.6 section 22 items 1 and 4 are dated (fix only at the next real Stage 2
   revision); D-23's "history retains until closure" wording is fine as a forward rule.
3. ChatGPT drafted `00_PROJECT_STATUS_v0_4.md`; Claude review: two SHOULDs (do not call `bfb6cc2`
   "current HEAD"; commit the RATIFIED form), both applied; committed as `c45dcf0` and verified.

### 17.2 Restart authorisation (conversational owner decision, not yet in a status file)

On 2026-10-14 the project owner wrote: "i am authorising chatgpt to tell me about the next stages and
begin the first." This authorises technical restart **beginning with S2-I1 only**. It does not
authorise S2-I2 or later increments. Propagate it into the next status-file refresh.

### 17.3 Owner clarifications during S2-I1 review (closed)

- The owner asked whether the inspector is frozen and what the new code is: answered - the inspector
  (`src\Mpeg2BlockInspector\`, builds `Mpeg2BlockInspector.exe`, writes `.idx`) and the analyzer
  (`tools\Stage1_Inspector_Analyzer_v0_2.py`) are frozen; S2-I1 adds only a new independent
  read-only reader plus validation scripts.
- The owner asked how FFmpeg/BestSource QP side data fits (Stage 2 v0.6 section 17, `06` K-09/O-01).
  Claude's findings (query closed, **no scope change**):
  - BestSource does **not** expose it: its `videosource.cpp` reads only mastering-display,
    content-light, Dolby Vision RPU, HDR10+ and ICC frame side data and never enables
    `export_side_data=venc_params`. O-01 answered: not via BestSource.
  - FFmpeg directly (PyAV, `codec_context.options={'export_side_data':'venc_params'}`) exports
    `AVVideoEncParams` type 2 (MPEG-2): `qp=0`, per-16x16-block `delta_qp` = per-MB QP. Compared with
    the Stage 2 reader's per-MB `q` on all 7 clips (six baselines + generated 4A-blocky): every MB
    identical in 2033/2040 frames; the only gap is each clip's final output frame, which carries no
    side data (FFmpeg end-of-stream flush). Zero mismatches.
  - This informally satisfies the v0.6 section 17 cross-check. FFmpeg QP does not replace the index
    (no FRAME/FIELD/NONE state). The owner was offered, and did not request, an optional
    `stage2_qp_sidedata_crosscheck` script.
  - Stage 2 uses no DLL; the production plugin (`mpeg2Deblock.dll`, Identity scaffold) is post-Stage-2
    work.

## 18. S2-I1 - current increment in full (resume here)

### 18.1 Files (candidate v0.2; all under `experiments/stage2/`)

```text
stage2_index_reader_v0_2.py                 independent read-only reader of the frozen Stage 1 v1 index
stage2_index_reader_regression_v0_2.py      six-baseline regression + negative tests
stage2_validate_bestsource_v0_2.vpy         BestSource/index correspondence (count, dims, every pict type)
S2_I1_validate_all_accepted_pairs_v0_2.bat  runs the .vpy on the six accepted .mpg/.idx pairs (read-only)
S2_I1_generate_4A_blocky_candidate_v0_2.bat scratch-only generation + validation of TEST_4A_A003_blocky.idx
```

Package files delivered by the previous chat (owner holds them):

```text
S2_I1_CANDIDATE_v0_2_FOR_CLAUDE_REVIEW.zip   (review request, evidence, manifest, REPO_OVERLAY/)
S2_I1_CANDIDATE_v0_2_REPO_OVERLAY.zip        (top-level folder S2_I1_CANDIDATE_v0_2_REPO_OVERLAY\experiments\stage2\...)
```

The five files must be copied into the repository's `experiments\stage2\`. If the overlay ZIP is
extracted with its top folder in the wrong place, the BATs fail safe ("required file not found")
because they locate the repository as `%~dp0..\..`.

The owner's working tree also holds the four **v0.1** files (`*_v0_1.*`). They were never committed and
must be deleted locally before the first S2-I1 commit, so only the accepted version enters Git.

### 18.2 Reader design (what the code does)

- Parses the frozen Stage 1 v1 format: 32-byte file header (`S1MBIDX1`, version 1, endian marker
  `0x01020304`, complete flag), 64-byte record header (`FRM1`), 8 bytes per macroblock (transform,
  coding, q, q_update, cbp, motion_type_raw, motion_dir_bits, packed flags).
- Reimplements **every** frozen analyzer v0.2 check, line for line (file header, record ordinal/size/
  flags/reserved, all MB invariants: SKIPPED is NONE, INTRA CBP 63, INTER CBP=0 is NONE, FIELD needs
  dct_type context, duplicate-flag consistency, and so on). It does not import the analyzer, so the
  two act as independent cross-checks.
- Adds Stage 2 current-domain gates: picture types I/P/B only; frame pictures only (field pictures
  rejected, v0.6 sections 5.2/6.1); `chroma_format` 4:2:0; boolean picture flags; positive and stable
  dimensions/MB grid. The MB-grid rule uses `ceil(h/16)` (progressive formula); interlaced MPEG-2 is
  `2*ceil(h/32)`; they coincide for current 576/288 material, and the code comments say so.
- Hard-aborts (exception, exit 2) on any malformed input.
- Exposes per-picture `progressive_frame`, picture type, MB access by (x,y), and the leading-B
  quality exclusion: **B pictures output before the first I picture** (computed once at load and
  cached). LP, EP and MLS each have leading B ordinals `[0, 1]`; 2A, 2A-blocky, 4A and 4A-blocky
  have none.
- `summary()` reports record count, picture types/structures, `progressive_frame`, `q_scale_type`,
  FRAME/FIELD/NONE, coding states, full effective-QP histogram, mixed FRAME/FIELD frames, MB Q
  updates, dct_type bits read, `frame_pred_frame_dct`, the four custom-matrix flags and leading-B.
- `validate_clip_metadata()` checks frame count, dimensions and every picture type against a decoded
  clip.
- `validate-4a-blocky` checks every Stage 1 Gate Report section 8.1 row available from the index
  (records 300; 720x576 / 45x36; I/P/B 26/75/199; FRAME/FIELD/NONE 56235/35243/394522;
  INTER/INTRA/SKIPPED 316290/46078/123632; `q_scale_type` 0 x300; QP 62 x486000; mixed 300; Q updates 0;
  dct bits read 91478; custom matrices absent; structure FRAME x300; `frame_pred_frame_dct` 0 x300)
  plus two labelled non-8.1 S2-I1 assertions (`progressive_frame` 0 x300; no leading B).

The regression file hard-codes, for each of the six accepted indexes, its SHA-256 and the frozen
analyzer's record count, picture types, `progressive_frame`, FRAME/FIELD/NONE and full QP histogram,
and checks the SHA-256 first. Claude independently confirmed every expected value against the frozen
analyzer's own `summary_data()`.

### 18.3 History of the increment

| When (2026-10-14) | Event |
|---|---|
| after restart authorisation | ChatGPT delivered S2-I1 v0.1 (4 files) for Claude review |
| Claude v0.1 review | No MUST; cleared to run. S1 short-read pipe trap; S2 complete the 8.1 check and print SHA-256; S3 BestSource check for all six pairs; O1 MB-grid comment; O2 analyzer `--expected-frames` is report-only; O3 cache leading-B |
| owner Windows run of v0.1 | **Generation BAT failed** before producing a usable index: CMD "The process cannot access the file because it is being used by another process." Cause: ffmpeg `2>>"%log%"` and inspector `>>"%log%" 2>&1` on two sides of one pipe appending to the same file. Claude had missed this (its rehearsal ran under Linux) and acknowledged it. Whether the v0.1 regression harness was run on Windows was not reported to Claude. |
| ChatGPT v0.2 | Removed the pipe entirely (ffmpeg -> scratch `.m2v` -> inspector `-b file`), fixing both the log collision and the short-read trap; incorporated S2, S3, O1-O3. ChatGPT's own Linux evidence: regression PASS; regular-file generation SHA-256 `57f3b60d...`; `validate-4a-blocky` PASS. Then the ChatGPT chat ended. |
| Claude v0.2 review | `Claude_REVIEW_OF_ChatGPT_S2_I1_Candidate_v0_2_v0_1.md`: **no MUST; cleared for the owner to run as delivered**; one SHOULD before commit (18.4) and two OPTIONAL |

### 18.4 Claude v0.2 review findings to act on

- **S1 SHOULD (before commit):** in `S2_I1_generate_4A_blocky_candidate_v0_2.bat` line 77,
  `echo Inspector exit code: %inspector_rc%>>"%log%"` hits the CMD handle-number trap (lesson 14.6.3);
  replace with `>>"%log%" echo Inspector exit code: %inspector_rc%`. Run outcome is unaffected (line 78
  tests the variable). Versioning: v0.2 has never been committed or ratified, so the owner may allow
  the one-line fix in place before the first commit; otherwise issue the BAT alone as `_v0_3`. Owner's
  choice.
- **O1:** the scratch `.m2v` is a remux of a Source Recording (Restricted Media) and remains in
  `%TEMP%\VapourSynth-mpeg2Deblock_S2_I1\`; delete it after the inspector step or tell the owner to
  delete the scratch folder after review.
- **O2:** the all-pairs BAT logs to the console only (acceptable; the owner pastes output).

### 18.5 Claude's execution evidence (for comparison with the owner's Windows run)

- v0.2 regression harness on the `c45dcf0` tree: PASS.
- Frozen inspector sources compiled with gcc reproduce all six accepted `.idx` byte-for-byte from
  file input (and from `< file` redirection).
- v0.2 generation order (ffmpeg `-y -v error -i ... -c:v copy -an -f mpeg2video <m2v>`, then
  `inspector -b <m2v> -m <idx>`): exit 0 / 0; `validate-4a-blocky` PASS; analyzer exit 0;
  **SHA-256 `57f3b60d1ea2108f29f222c7c658cb1ddc9eb26c14071cb056112a2f3b296e73`** (the BAT requires this
  exact value).
- New v0.2 summary fields equal the frozen analyzer on all 7 indexes; nine extra malformed-input
  mutations all rejected for the intended reason; feeding the original `TEST_4A_A003.idx` to
  `validate-4a-blocky` exits 2.
- FFmpeg `pict_type`/frame count/dimensions fed to `validate_clip_metadata()`: 7/7 PASS (proxy for
  the BestSource runs; BestSource itself cannot run in Claude's environment).

### 18.6 Next steps, in order

1. Owner copies the five v0.2 files into `experiments\stage2\` and runs (one command per block):

```cmd
cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"
```

```cmd
python experiments\stage2\stage2_index_reader_regression_v0_2.py
```

```cmd
experiments\stage2\S2_I1_validate_all_accepted_pairs_v0_2.bat
```

```cmd
experiments\stage2\S2_I1_generate_4A_blocky_candidate_v0_2.bat
```

```cmd
git status --short
```

   Expected: harness `PASS: S2-I1 v0.2 reader reproduces ...`; all-pairs `PASS: ... all six accepted
   baseline pairs`; generation `PASS SHA-256 = 57f3b60d...` then `PASS: ... generated and validated in
   scratch`; `git status` shows only `?? experiments/`. The owner sends console output and
   `%TEMP%\VapourSynth-mpeg2Deblock_S2_I1\TEST_4A_A003_blocky.log` to Claude (and the successor).
2. If any step fails: stop, diagnose from the log, fix in a new candidate version, Claude re-clears.
3. Apply the 18.4 S1 fix (and optionally O1/O2); Claude checks the changed BAT.
4. First S2-I1 commit (owner, named staging; never `git add -A` here): delete the four `*_v0_1.*`
   files; add only the five accepted files; check `git status --short` and
   `git diff --cached --name-status --no-renames` show exactly those five additions; suggested message
   "Add S2-I1 read-only Stage 1 index reader and validation"; push. Python creates
   `experiments\stage2\__pycache__\`, which `.gitignore` already excludes. Scratch outputs stay in `%TEMP%`.
5. Write a short S2-I1 result note for the owner: the six regression PASSes, the six BestSource
   correspondence PASSes, the 4A-blocky candidate (SHA-256, 8.1 match, non-baseline, uncommitted),
   leading-B counts per clip, and that S2-I1's v0.6 obligations are met.
6. Propose `00_PROJECT_STATUS_v0_5.md` recording restart authorisation (17.2), the S2-I1 commit and
   result; Claude reviews; owner ratifies; v0.4 deleted in the same commit.
7. **Stop.** S2-I2 (seam-map diagnostics, mandatory two-dimensional spatial index-to-pixel
   registration, shifted-label controls -1/0/+1 MB in x and y, 8-pixel grid-phase checks) begins only
   when the owner separately authorises it. Picture-like diagnostics from S2-I2 onward are Restricted
   Media (`NOTICE.md`; Stage 2 v0.6 section 3.6).
8. Refresh this handover after step 4 and again after step 6.

## 19. Things future ChatGPT must not do

1. Do not start S2-I2 or any later increment until the project owner separately authorises it after reviewed S2-I1 results.
2. Do not revive Family B.
3. Do not build a pixel-only production seam-position detector.
4. Do not add an external deblocker yardstick unless the project owner explicitly reopens it.
5. Do not give NONE an internal vertical or horizontal transform seam.
6. Do not treat presence/reading of `dct_type` as equivalent to coded residual geometry.
7. Do not treat a NONE macroblock's indexed QP as having quantised residual pixels there.
8. Do not reopen Stage 1 without concrete evidence.
9. Do not regenerate accepted `.idx` baselines merely to make a test pass.
10. Do not promote `TEST_4A_A003_blocky.idx` to a seventh immutable baseline without an owner decision; do not commit it.
11. Do not capture extra metadata pre-emptively just because the format could hold it.
12. Do not treat `_blocky` QP-62 pairs as evidence for spatial QP-map value.
13. Do not infer roles/properties for XP/SP/TEST_3A or LP/EP/MLS `_blocky` spare material without analysis/assignment.
14. Do not use superseded Stage 2 v0.5 or earlier designs instead of v0.6.
15. Do not treat handovers/reviews as repository technical authority.
16. Do not look for or reconstruct the deleted migration handback as current authority.
17. Do not override `.vcxproj` build policy from command lines merely to make a build pass.
18. Do not weaken the expected-switch CSV/workflow gate merely because legitimate toolchain output changed; review and ratify the delta.
19. Do not treat the completed 2026-10-13 history reset as Development Closure; Restricted Media intentionally remains.
20. Do not remove Restricted Media before Development Closure merely to satisfy this handover; the current policy permits bounded active-development use.
21. Do not silently turn OPEN/HYPOTHESIS items into accepted algorithm rules.
22. Do not identify the project owner by personal name/location in project artifacts; use `hydra3333`, project owner, project maintainer or equivalent neutral wording.
23. Do not rely on old pre-reset commit SHAs as live Git objects; record them only as external historical provenance where genuinely necessary.
24. Do not give the project owner long fragile CMD paste sequences when a short command or reviewed script/file will do.
25. Do not pipe input into the frozen inspector for new index generation; use a scratch regular file (lesson 14.6.4).
26. Do not let two processes append to the same file in one CMD command line; do not put a digit directly before a CMD redirection (lessons 14.6.2-3).
27. Do not give the owner a tool to run before Claude has executed/rehearsed and cleared it.
28. Do not modify the frozen inspector or analyzer; S2 work reads their outputs only.
29. Do not let the handover fall behind the work (lesson 14.6.1).

## 20. Documents a future ChatGPT should prioritise

### Current-state and authority

```text
docs/REPOSITORY/00_PROJECT_STATUS_v0_4.md   (or later)
docs/REPOSITORY/05_DECISIONS_v1_2.md
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md
docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md
docs/REPOSITORY/Stage2_Experiment_Design_v0_6.md
NOTICE.md
README.md
```

### Build / CI / release authority

```text
vs/VapourSynth-mpeg2Deblock/*.vcxproj
.github/workflows/mpeg2Deblock_build-windows-x64_workflow_manual_or_release.yml
.github/workflows/expected_stage_bplus_switches.csv
README.md  (Building / release orientation)
```

There is no current migration-handback ZIP.

### Development continuity

```text
latest ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_*.md
latest Claude_HANDOVER_TO_Future_Claude_Chat_v0_*.md
```

### Current increment (owner holds these; not in the repository)

```text
S2_I1_CANDIDATE_v0_2_FOR_CLAUDE_REVIEW.zip / S2_I1_CANDIDATE_v0_2_REPO_OVERLAY.zip
Claude_REVIEW_OF_ChatGPT_S2_I1_Candidate_v0_1_v0_1.md
Claude_REVIEW_OF_ChatGPT_S2_I1_Candidate_v0_2_v0_1.md
```

### Stage 1 implementation/evidence where a task requires it

```text
docs/Stage1_Inspector_Instrumentation_Design_v0_3.md
tools/Stage1_Inspector_Analyzer_v0_2.py
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md
TESTING/TEST_Mpeg2BlockInspector*.BAT and show_source_clip_info*.vpy  (accepted Stage 1 run patterns)
```

### Historical provenance only when genuinely needed

```text
docs/MPEG2_Macroblock_Index_VapourSynth_Deblocking_Project_Proposal_v0_5.md
selected retained Claude/ChatGPT review records
externally recorded pre-reset SHA fd82d78715ed6a61ef4e80b9769655eefe23c384
```

Older superseded files and old Git ancestry were deliberately removed. Prefer current authority over
provenance.

## 21. Suggested opening prompt for the next ChatGPT chat

The project owner can use approximately:

> We are continuing the `VapourSynth-mpeg2Deblock` project. The previous ChatGPT chat hit its length
> limit mid-increment. First read the attached
> `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md` in full (especially sections 0,
> 17 and 18), then the repository authorities it lists, starting with
> `docs/REPOSITORY/00_PROJECT_STATUS_v0_4.md` and `Stage2_Experiment_Design_v0_6.md`. Repository HEAD
> was `c45dcf0` at the handover. Technical restart is authorised for S2-I1 only; S2-I1 candidate v0.2
> is delivered and cleared by Claude, and I am about to run it / have run it (results attached). Resume
> S2-I1 from handover section 18.6. Do not start S2-I2 unless I explicitly authorise it. Claude
> executes or rehearses every tool before I run it.

The owner should attach: this handover, the latest Claude handover, the S2-I1 v0.2 review package and
Claude's two S2-I1 reviews, plus a GitHub ZIP of `main` if the repository has moved on.

## 22. Compact current-state summary

```text
REPOSITORY:
    VapourSynth-mpeg2Deblock, main
    root 11f47427624bf5f68b3426fe9f58aa26d40e47f7 (tree 45ad1f16...)
    HEAD c45dcf0923cbbbe335266d2c4302327f16ab94fe (pushed, verified by Claude)
    post-root commits documentation-only; 124 files; frozen hashes and six .idx unchanged

PRE-RESET PROVENANCE:
    fd82d78715ed6a61ef4e80b9769655eefe23c384 (external identifier only)

BUILD / CI / RELEASE:
    .vcxproj own build settings; workflow + expected-switch CSV own CI/release
    v0.1.0 snapshot pre-release on root; asset SHA-256 f8ddb2da... (owner-reported)

STAGE 1:
    COMPLETE / PASS / FROZEN; inspector and analyzer frozen; six .idx immutable

STATUS FILE:
    00_PROJECT_STATUS_v0_4.md RATIFIED (says restart NOT AUTHORISED as at ratification)

RESTART:
    AUTHORISED 2026-10-14 for S2-I1 only (conversational; propagate into status v0.5)

S2-I1:
    candidate v0.2 delivered; Claude: no MUST, cleared to run; S1 one-line BAT fix before commit
    owner Windows run of v0.2: PENDING at as-at point
    expected 4A-blocky candidate SHA-256 57f3b60d1ea2108f29f222c7c658cb1ddc9eb26c14071cb056112a2f3b296e73
    v0.1 files: uncommitted, to be deleted before first commit
    nothing from S2-I1 committed yet

FFMPEG QP SIDE DATA:
    not exposed by BestSource; via PyAV equals index QP in 2033/2040 frames (last frame has none)
    informational cross-check only; no scope change

S2-I2 AND LATER:
    NOT AUTHORISED

RESTRICTED MEDIA:
    policy unchanged; scratch .m2v/.idx under %TEMP% are scratch; .m2v is Restricted Media
```

## 23. Change log

### v0.7 - 2026-10-14

- Prepared by Claude for the ChatGPT role after the ChatGPT chat ended without warning; based on
  committed v0.6, ChatGPT's last deliverables, Claude's reviews/executions and the owner's messages.
- Re-bases the as-at point on HEAD `c45dcf0` (handover install `eac5526`/`bfb6cc2`, status v0.4).
- Records completion of the final KB/repository gate and Project Status v0.4.
- Records the owner's 2026-10-14 restart authorisation (S2-I1 only) as a conversational decision not
  yet in a status file.
- Adds section 18: full S2-I1 state (files, reader design, history including the v0.1 Windows CMD
  failure, v0.2 changes, Claude v0.2 review, execution evidence, exact next steps and commit plan).
- Adds the Claude execute-before-owner-runs duty (section 4) and lessons 14.6 (handover cadence, CMD
  concurrent-append and handle-number traps, frozen-inspector short-read trap).
- Records the closed owner queries (frozen inspector; FFmpeg/BestSource QP side data findings).
- Updates must-not list, priority documents, opening prompt and compact summary.

### v0.6 - 2026-10-13

- Supersedes v0.5 once accepted/installed.
- Re-bases continuity on fresh-history root `11f47427624bf5f68b3426fe9f58aa26d40e47f7` and tree
  `45ad1f16a24d3cce0411863a9804472efa1c8529`.
- Records `fd82d78715ed6a61ef4e80b9769655eefe23c384` only as external pre-reset provenance.
- Records successful owner-identity/current-tree cleanup, 37-path purge, fresh-history reset, fresh
  HTTPS clone verification and deletion of the quarantined old clone.
- Replaces stale unversioned authority paths with Project Status v0.3, Decisions v1.2 and Stage 2 v0.6.
- Removes the deleted migration handback as current authority and carries forward the build/CI/release
  continuity needed by a successor from the live project/workflow/CSV files.
- Records the fresh `v0.1.0` snapshot pre-release on the new root and its binary ZIP SHA-256.
- Records deletion of all old Actions runs, the fresh-root author/committer no-reply identity, the corrected
  six-log sample count, and the optional future UTC commit-offset hygiene choice.
- Final Claude cross-review S1 applied: section 11 now accounts for all 16 recordings; optional release-hash
  provenance and two `docs/` path clarifications also applied.
- Reconciles the Restricted Media section with the ratified narrow ChatGPT/Claude AI exception and
  Development Closure lifecycle.
- Distinguishes the completed 2026-10-13 history reset (media intentionally retained) from the future
  Development Closure media-removal/history-reset operation.
- Replaces the completed broad reconciliation gate with the remaining bounded final KB/repository
  consistency check after ChatGPT v0.6 / Claude v0.8.
- Keeps Stage 1 frozen, Stage 2 v0.6 ratified, Stage 2 implementation unstarted, technical restart NOT
  AUTHORISED and S2-I1 conditional on a separate owner decision.

### v0.5 - 2026-10-12

Historical predecessor. It captured the post-migration technical model but predates the coordinated
identity/policy cleanup, Stage 2 v0.6, deletion of the migration handback and the fresh-history reset.
Its stale current-state instructions must not drive development.

### v0.4 - 2026-10-09

Historical predecessor. It correctly preserved much of the technical Stage 1/Stage 2 knowledge but
its immediate state was migration-era. Those migration instructions are superseded and must not drive
current development.
