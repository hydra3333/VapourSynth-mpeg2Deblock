# ChatGPT Handover to Future ChatGPT Chat
## MPEG-2 Macroblock Index / VapourSynth Deblocking Project

**Filename:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_5.md`
**Version:** 0.5
**Date:** 2026-10-12
**Author:** ChatGPT
**Status:** CURRENT role-specific continuity handover. Not repository authority. The current repository authorities and the final common migration handback prevail on any conflict.
**As-at boundary:** repository state verified at `317d3f1` plus explicit the project owner decisions made after that commit and recorded in this handover's post-snapshot delta section.
**Supersedes:** `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_4.md`

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

Do not begin technical implementation from this handover alone.

First establish the live repository state, then read the current authorities in this order:

```text
docs/REPOSITORY/00_PROJECT_STATUS.md
docs/REPOSITORY/05_DECISIONS.md
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md
docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md
docs/REPOSITORY/Stage2_Experiment_Design_v0_5.md
NOTICE.md
README.md
```

For build, Visual Studio, CI, release, packaging and migration-close-out facts, read the retained
common migration package:

```text
docs/HANDOVER/MIGRATION_Step4_Final_Common_Developer_Handback_v0_21_RATIFIED.zip
```

Also read the latest ChatGPT and Claude role handovers.

Then compare the live repository/document state against this handover's as-at boundary and the
post-snapshot decisions recorded later in this handover. Resolve only the actual delta; do not
re-open settled history merely because the successor is new.

Confirm with the project owner whether the mandatory post-handover knowledge-base reconciliation gate has already
been completed and whether he has separately authorised technical restart.

Unless both are true:

```text
DO NOT START S2-I1.
```

---

## 1. Purpose and authority boundary

This document exists so a future ChatGPT development chat can resume the project safely if the
current chat is unavailable or reaches its conversation limit.

It records:

- project identity and roles;
- current repository/status baseline;
- current authority set;
- durable technical knowledge needed to avoid regressions;
- Stage 1 and Stage 2 status;
- sample roles;
- immutable regression-baseline policy;
- the current Restricted Media policy;
- the exact pre-restart sequence;
- the next technical increment if the project owner later authorises restart;
- cautions and non-goals.

This handover is **not** a technical authority.

Rules:

1. `00_PROJECT_STATUS.md` is the first concise current-state index.
2. The owning ratified authority wins if this handover differs from it.
3. The final common migration handback owns build/CI/release/migration knowledge.
4. Review documents explain provenance; they do not outrank current authority.
5. Superseded documents are history only.

---

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

Current verified committed/pushed state at this handover refresh:

```text
317d3f1  snapshot
```

At the verification performed immediately before this handover refresh:

```text
HEAD -> main
origin/main
origin/HEAD
```

all pointed to `317d3f1`, and the working tree was clean.

Relevant post-migration commit sequence:

```text
a0e7100  Pin CRLF checkout for VS project files and batch files (determinism only)
e7f63d0  Retire migration working records and obsolete handoff artifacts
5010b79  Ratify deblock concept v1.2, Stage 2 v0.4, and project status
2e4eab1  Correct VapourSynth header provenance to R81
317d3f1  snapshot
```

`317d3f1` contains the directly ratified Restricted Media policy, Stage 2 v0.5 and Project Status
v0.2 state verified by the read-only audit.

Always re-check the live repository before acting.

### 2.2 Previous local tree

The previous tree:

```text
E:\SOFTWARE-Win11\MULTIMEDIA\Mpeg2BlockInspector\Mpeg2BlockInspector
```

is rollback/reference material only.

Do not use it as the active development tree.

### 2.3 Important repository locations

```text
src\Mpeg2BlockInspector\
    frozen Stage 1 inspector/indexer source

tools\Stage1_Inspector_Analyzer_v0_2.py
    frozen Stage 1 analyzer

vs\VapourSynth-mpeg2Deblock\
    x64 Visual Studio solution/projects

TESTING\
    regression/build/test scripts

VHSC_samples\
    Source Recordings, accepted indexes and associated test material

docs\REPOSITORY\
    current technical/status authorities

docs\HANDOVER\
    AI role handovers and retained final common migration handback
```

Future Stage 2 experimental Python belongs under:

```text
experiments\stage2\
```

when and only when S2-I1 is authorised.

---

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
final Restricted Media policy / Stage 2 v0.5 alignment.

The project owner remains final authority.

---

## 5. Current repository authority/status set

### 5.1 Current concise status index

```text
docs/REPOSITORY/00_PROJECT_STATUS.md
Version: 0.2
Status: RATIFIED
Date: 2026-10-12
```

This is the first current-state document a future development chat should inspect.

It is an index, not competing technical authority.

### 5.2 Decision authority

```text
docs/REPOSITORY/05_DECISIONS.md
Version: 1.1
Status: RATIFIED
```

Important current decisions include:

```text
D-24  production architecture is index-driven
D-25  native MPEG-2 4:2:0 chroma is in production scope
D-26  evidence hierarchy prioritises real recorder material
```

Earlier decisions superseded or amended by these must not be revived accidentally.

### 5.3 Deblocking concept authority

```text
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md
Version: 1.2
Status: RATIFIED
Date: 2026-10-11
```

Version 1.2 incorporates the corrected FRAME/FIELD/NONE geometry, including NONE having no internal
transform seams.

Items explicitly labelled HYPOTHESIS or OPEN remain hypotheses/open questions despite document
ratification.

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
docs/REPOSITORY/Stage2_Experiment_Design_v0_5.md
Version: 0.5
Status: RATIFIED
Date: 2026-10-12
```

Version 0.5 is the current Stage 2 design.

Version 0.4 is superseded.

The v0.5 change was media-policy alignment only. It did **not** change:

- Stage 2 algorithm;
- sample roles;
- immutable-index rules;
- implementation sequence;
- technical-restart status.

No Stage 2 implementation has started.

---

## 6. Migration and build state

### 6.1 Migration status

Repository migration is:

```text
CLOSED / RATIFIED
Date: 2026-10-11
```

The retained common record is:

```text
docs/HANDOVER/MIGRATION_Step4_Final_Common_Developer_Handback_v0_21_RATIFIED.zip
```

Keep that ZIP **unextracted in the repository**.

The former migration working/evidence subtree was deliberately retired from the current tree.

Do not reconstruct migration state from old Stage A plans or old role-handover narrative.

### 6.2 Final migration acceptance facts useful to development

The migration's final source commit was:

```text
5141a23e5768b1be863de1094089d04d1f11245b
```

The final migration handback/package was independently consumed by the receiving development chats.
The migration delivered Visual Studio 2026 projects, the GitHub Actions build/release workflow and
the initial `v0.1.0` Identity-scaffold pre-release.

The final plain-CMD F2(a) evidence established, for both Debug and Release x64 rebuilds:

```text
17 accepted legacy-inspector warnings
0 errors
build exit code 0
plugin warnings: 0
```

The 17 inspector warnings are the known legacy-C set. New/different warnings are a delta to explain,
not something to accept automatically.

The six accepted reference `.idx` hashes matched through final migration verification.

Exact migration/build/CI/release evidence and invariants remain owned by the final common migration
handback. This summary exists so a successor understands what has already been proven without having
to rediscover the migration story.

### 6.3 Build-system orientation only

The Visual Studio solution is x64-only and contains two projects:

```text
Mpeg2BlockInspector.exe
    frozen Stage 1 legacy-C inspector/indexer baseline

mpeg2Deblock.dll
    C++20 VapourSynth API4 production-plugin scaffold
    currently exposes only mpeg2deblock.Identity
    NOT yet a deblocking filter
```

Current high-level accepted build policy includes:

```text
x64 only
AVX2 minimum for both native binaries
Debug + Release
Release /MT
Debug /MDd
/fp:precise
project files own the build settings
```

Security/build/release details are owned by the final common migration handback and must not be
re-created from memory.

Useful accepted invariants a successor should nevertheless keep in its mental model include:

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

Release `/MT` also carries an important DLL-boundary rule: do not casually pass ownership of
CRT-allocated memory/objects across module boundaries for another module to free/manage. VapourSynth
objects should follow VapourSynth API ownership. If the exact rule matters to a code change, read
the common handback before implementation.

The scalar implementation planned later is a **reference path inside the AVX2-targeted binary**, not
a pre-AVX2 compatibility fallback.

### 6.4 VapourSynth header provenance

Current provenance records:

```text
VapourSynth4.h   R81
VSHelper4.h      R81
VSScript4.h      R81
VSConstants4.h   R81
VSVulkan4.h      retained post-R81 master snapshot
```

The provenance correction was committed/pushed as:

```text
2e4eab1  Correct VapourSynth header provenance to R81
```

Historical migration handback text remains historical and should not be rewritten merely because
later repository provenance metadata was corrected.

---

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
```

Do not infer their resolution/interlace/transform distributions or silently assign hold-out/tuning
roles.

Analyse first and obtain owner-approved disposition if they become relevant.

---

## 12. Stage 2 design and implementation sequence

### 12.1 Current state

```text
Stage 2 design:
    v0.5 RATIFIED

Stage 2 implementation:
    NOT STARTED

Technical restart:
    NOT AUTHORISED
```

### 12.2 Next technical increment if separately authorised

```text
S2-I1
    read-only Stage 1 index reader / validation
```

Its job includes reproducing accepted analyzer summaries and validating input/index semantics before
any filtering experiment.

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

Use the current Stage 2 v0.5 file for precise methodology.

Do not implement from this abbreviated handover summary.

---

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

## 15. Restricted Media policy

The coordinated Restricted Media policy is ratified and applied in:

```text
NOTICE.md
README.md
Stage2_Experiment_Design_v0_5.md
```

### 15.1 Source Recordings

Source Recordings are recordings expressly included for project testing/validation/diagnosis and
behaviour reproduction.

At present this includes the video recordings under:

```text
VHSC_samples\
```

Media file type alone does not make unrelated project-made or third-party media a Source Recording.

### 15.2 Derived / Restricted Media

Restricted Media includes Source Recordings plus Derived Media.

Derived Media includes:

- filtered/transformed picture or sound;
- crops/stills/difference images/audio extracts;
- visual or audible representations derived from Source Recording metadata or measurements;
- QP heat maps;
- seam-statistics plots;
- charts/maps/masks/similar media visualisations.

The project owner selected the cautious option that such visualisations remain Restricted Media even where they
contain no recognisable original frame pixels.

### 15.3 What is not Restricted Media merely by derivation

Examples:

```text
.idx files
hashes
logs
source code
metadata
purely numerical/textual diagnostics
```

remain non-media unless they themselves contain or embed Restricted Media.

A document that embeds Restricted Media is treated as Restricted Media while that embedded media
remains; a media-free/redacted version may remain under ordinary project terms.

### 15.4 Transmission / lifecycle

There is **NO private-review/person/service transmission exception**.

During active development, Restricted Media may remain in the repository as bounded
test/evidence/review material to the extent allowed by `NOTICE.md`.

Outside that permitted repository use, the governing NOTICE restricts sharing/upload/transmission
and requires deletion after the permitted use.

At project finalisation:

1. remove all Restricted Media from the current repository tree;
2. remove it from project-controlled release/assets/storage;
3. perform the separately planned Git-history purge to remove historical repository media copies;
4. thereafter keep Restricted Media out of the Git tree/history unless a separately reviewed and
   ratified decision says otherwise.

`NOTICE.md` is the governing text.

Do not paraphrase this handover as a substitute for reading it.

---

## 16. Post-snapshot project-owner decisions and known documentation delta

This section exists because the repository snapshot is **not** the entire current state.

After repository HEAD `317d3f1` and after ratification/application of the no-external-transmission
Restricted Media wording, the project owner made a later explicit conversational decision:

> i authorize chatgpt and claude AI to access and use the images, videos and audios for the purpose
> of this project and only for the duration of development of this project until development closure
> as stated by me.

Current continuity interpretation:

- this is a direct the project owner project-specific authorisation for **ChatGPT and Claude AI**;
- purpose is limited to this project's development;
- duration ends when the project owner explicitly declares development closed;
- it does not authorise unrelated reuse, publication, redistribution, model training or retention
  after project closure.

### Known repository-policy mismatch

At `317d3f1`, the ratified `NOTICE.md` says there is no private-review/person/service transmission
exception.

The project owner's later AI-specific authorisation therefore creates a **known post-snapshot policy/documentation
delta**.

Do not pretend the repository has already been updated.

The expected reconciliation task is to decide and document a narrow ChatGPT/Claude project-media
exception consistently in the relevant current documents, while preserving the broader prohibition
for other external sharing/services unless the project owner decides otherwise.

This delta belongs in the upcoming knowledge-base reconciliation unless the project owner resolves it earlier.

### Additional reconciliation candidate - Markdown line endings

Claude's source-ZIP verification at `317d3f1` observed:

```text
.gitattributes does not pin *.md line endings
GitHub-generated source ZIP Markdown members are LF
the Windows working checkout presents Markdown as CRLF under the current checkout setting
```

This is not currently treated as a defect and no repository change is authorised merely by recording
it here.

The reconciliation gate should decide one of two explicit policies:

1. add a deliberate `*.md` `eol=crlf` rule; or
2. leave Markdown governed by checkout settings and document that GitHub source ZIP LF is expected.

Do not perform a repository-wide Markdown renormalisation as an incidental consequence of that
decision.

---

## 17. Current pre-restart gate

This is the immediate project state at handover refresh.

Already complete:

```text
migration:
    CLOSED / RATIFIED

post-migration CRLF/determinism cleanup:
    COMPLETE

authority/status refresh:
    COMPLETE

VapourSynth header provenance correction:
    COMPLETE

Restricted Media policy + Stage 2 v0.5 + Project Status v0.2:
    COMPLETE / RATIFIED / COMMITTED / PUSHED
```

Current verified HEAD:

```text
317d3f1  snapshot
```

Remaining sequence before the project owner may even decide whether to restart technical work:

```text
1. Refresh ChatGPT role handover.
2. Refresh Claude role handover.
3. Independently perform the mandatory ChatGPT + Claude knowledge-base reconciliation gate.
4. Include the post-317d3f1 ChatGPT/Claude media-use authorisation/documentation mismatch in that
   reconciliation unless the project owner resolves it earlier.
5. Reconcile differences through the project owner.
6. Apply only owner-ratified corrections.
7. Touch handovers/status again if reconciliation changes current knowledge.
8. Only then may the project owner decide whether to authorise technical restart.
```

No step above automatically authorises S2-I1.

At the time this v0.5 handover is drafted:

```text
TECHNICAL RESTART:
    NOT AUTHORISED
```

---

## 18. Mandatory knowledge-base reconciliation gate

After both role handovers are refreshed, ChatGPT and Claude must independently inspect the current
knowledge base for:

- knowledge newly established since their prior handovers;
- corrections to prior knowledge;
- clarifications now needed to prevent ambiguity;
- superseded knowledge still presented as current;
- conflicting ownership between authority/status/handover documents;
- open questions that are being accidentally treated as settled;
- settled decisions that are being accidentally treated as open;
- stale migration-era instructions that should no longer drive development;
- explicit the project owner decisions made after the last repository snapshot that have not yet been propagated
  into their owning documents.

Each role should prepare a bounded delta inventory.

Then:

```text
ChatGPT inventory
    +
Claude inventory
    ->
The project owner reconciliation / decisions
    ->
only ratified corrections are applied
```

The reconciliation gate is a knowledge-integrity exercise.

It is **not** permission to redesign the algorithm or reopen settled scope without evidence.

---

## 19. Things future ChatGPT must not do

1. Do not start S2-I1 unless the project owner has separately authorised technical restart after the reconciliation gate.
2. Do not revive Family B.
3. Do not build a pixel-only production seam-position detector.
4. Do not add an external deblocker yardstick unless the project owner explicitly reopens it.
5. Do not give NONE an internal vertical or horizontal transform seam.
6. Do not treat presence/reading of `dct_type` as equivalent to coded residual geometry.
7. Do not treat a NONE macroblock's indexed QP as having quantised residual pixels there.
8. Do not reopen Stage 1 without concrete evidence.
9. Do not regenerate accepted `.idx` baselines merely to make a test pass.
10. Do not capture extra metadata pre-emptively just because the format could hold it.
11. Do not treat `_blocky` QP-62 pairs as evidence for spatial QP-map value.
12. Do not infer roles/properties for XP/SP/TEST_3A spare material without analysis.
13. Do not use superseded Stage 2 v0.4 or earlier designs instead of v0.5.
14. Do not treat handovers/reviews as repository technical authority.
15. Do not duplicate migration/build/CI/release authority out of the final common migration handback.
16. Do not transmit Restricted Media externally on the assumption that project review creates an exception; the ratified policy contains no such exception.
17. Do not treat the planned final media/history cleanup as a prerequisite for Stage 2 restart unless the project owner later makes it one.
18. Do not silently turn OPEN/HYPOTHESIS items into accepted algorithm rules.
19. Do not assume `317d3f1` contains the project owner's later ChatGPT/Claude AI media-use authorisation; it does
    not, and that policy/documentation delta is explicitly pending reconciliation.
20. Do not give the project owner long fragile CMD paste sequences when a short command or reviewed BAT will do.

---

## 20. Documents a future ChatGPT should prioritise

### Current-state and authority

```text
docs/REPOSITORY/00_PROJECT_STATUS.md
docs/REPOSITORY/05_DECISIONS.md
docs/REPOSITORY/06_DEBLOCK_CONCEPT.md
docs/REPOSITORY/02_INDEX_FORMAT_SPEC.md
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md
docs/REPOSITORY/Stage2_Experiment_Design_v0_5.md
NOTICE.md
README.md
```

### Build/migration authority

```text
docs/HANDOVER/MIGRATION_00_START_HERE_INTRO_FOR_DEVELOPMENT_CHATS.md
docs/HANDOVER/MIGRATION_Step4_Final_Common_Developer_Handback_v0_21_RATIFIED.zip
```

### Development continuity

```text
latest ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_*.md
latest Claude_HANDOVER_TO_Future_Claude_Chat_v0_*.md
```

### Stage 1 implementation/evidence where a task requires it

```text
Stage1_Inspector_Instrumentation_Design_v0_3.md
tools/Stage1_Inspector_Analyzer_v0_2.py
docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md
```

### Historical provenance only when needed

```text
MPEG2_Macroblock_Index_VapourSynth_Deblocking_Project_Proposal_v0_5.md
older Stage 2 designs
older role handovers
selected Claude/ChatGPT review records
retired migration history via Git when genuinely required
```

Prefer current authority over provenance.

---

## 21. Suggested opening prompt for the next ChatGPT chat

The project owner can use approximately:

> We are continuing the `VapourSynth-mpeg2Deblock` project. First read the latest
> `ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_*.md`, then
> `docs/REPOSITORY/00_PROJECT_STATUS.md`, the current ratified `05_DECISIONS.md`,
> `06_DEBLOCK_CONCEPT.md`, `02_INDEX_FORMAT_SPEC.md`,
> `Stage1_Evidence_and_Gate_Report_v0_3.md`, and
> `Stage2_Experiment_Design_v0_5.md`. Also read the current `NOTICE.md` and `README.md`.
> For migration/build/CI/release facts, read the retained
> `MIGRATION_Step4_Final_Common_Developer_Handback_v0_21_RATIFIED.zip`.
>
> Migration is closed, Stage 1 is frozen, Stage 2 v0.5 is ratified, and no Stage 2 implementation
> has started. Before any technical work, establish whether the mandatory independent ChatGPT +
> Claude knowledge-base reconciliation gate has been completed and whether I have separately
> authorised restart. Also check the handover's post-snapshot decisions, especially my later
> ChatGPT/Claude project-media authorisation, against the live repository policy. Do not start S2-I1
> unless I explicitly authorise it.

---

## 22. Compact current-state summary

```text
REPOSITORY:
    VapourSynth-mpeg2Deblock
    main
    verified HEAD at handover refresh: 317d3f1
    committed/pushed/clean

MIGRATION:
    CLOSED / RATIFIED
    final common handback v0.21 retained

STAGE 1:
    COMPLETE / PASS / FROZEN
    six accepted .idx baselines immutable

ARCHITECTURE:
    index-driven by definition
    native 4:2:0 chroma in scope
    real recorder evidence primary

06 CONCEPT:
    v1.2 RATIFIED
    NONE has no internal transform seams

INDEX FORMAT:
    v0.4 current ratified-constraints baseline
    final packing not frozen

STAGE 2:
    v0.5 RATIFIED
    implementation NOT STARTED

PLUGIN:
    buildable API4 scaffold
    mpeg2deblock.Identity only
    not yet a deblocker

RESTRICTED MEDIA AT 317d3f1:
    ratified policy applied
    option (a) derived visualisations restricted
    no general external/private-review transmission exception
    finalisation removes media from tree + planned history purge

POST-317d3f1 the project owner DECISION:
    ChatGPT + Claude AI specifically authorised to access/use project image/video/audio
    only for this project's development duration until the project owner declares closure
    repository-policy wording not yet reconciled to this later decision

CURRENT MANDATORY WORK:
    refresh both role handovers
    then independent knowledge-base reconciliation

TECHNICAL RESTART:
    NOT AUTHORISED

NEXT TECHNICAL ITEM IF LATER AUTHORISED:
    S2-I1 read-only Stage 1 index reader / validation
```

---

## 23. Change log

### v0.5 - 2026-10-12

- Supersedes the migration-era v0.4 development handover once the project owner accepts this refresh.
- Replaces obsolete Stage A/A3 migration work with the ratified CLOSED migration state and delegates
  build/CI/release detail to the final common migration handback v0.21.
- Adds `00_PROJECT_STATUS.md` v0.2 as the first current-state index.
- Updates `06_DEBLOCK_CONCEPT.md` from v1.1 to current v1.2 and records the completed NONE geometry
  clarification as current authority.
- Updates Stage 2 from v0.3 to current v0.5 RATIFIED and records that implementation remains
  unstarted.
- Records current verified repository state at `317d3f1`.
- Records the two-project Visual Studio end-state and plugin `Identity` scaffold without duplicating
  migration-handback build authority.
- Records R81 VapourSynth header provenance and retained post-R81 `VSVulkan4.h` snapshot.
- Records the immutable six-index regression-baseline rule and LP accepted SHA-256.
- Updates sample roles, including XP/SP/TEST_3A as explicitly unassigned/spare.
- Adds the ratified Restricted Media policy, option (a) visualisations, no external/private-review
  transmission exception, and project-finalisation media/history cleanup.
- Replaces the obsolete immediate migration task with the mandatory dual-handover refresh followed
  by independent ChatGPT + Claude knowledge-base reconciliation.
- Adds the explicit continuity purpose: this is a rich chat-to-successor working-state snapshot, not
  merely an authority-file index, and takeover begins by determining the delta from its as-at point.
- Adds the project owner-facing operational continuity rules for command formatting, named staging, proportional
  verification, ZIP packaging and knowledge-management discipline.
- Adds the post-`317d3f1` the project owner decision authorising ChatGPT and Claude AI to access/use project
  image/video/audio only for this project's development duration, and explicitly records the current
  mismatch with the repository's no-external-transmission wording as a pending reconciliation item.
- Incorporates Claude handover-review touch-ups: the project owner's exact AI-media authorisation wording, the
  deliberate-snapshot `git add -A` allowance, and corrected Restricted Media subsection numbering.
- Records Markdown line-ending policy as a reconciliation candidate rather than silently choosing a
  new `.gitattributes` rule.
- Keeps technical restart explicitly NOT AUTHORISED and S2-I1 as the next technical increment only
  after separate the project owner authorisation.

### v0.4 - 2026-10-09

Historical predecessor. It correctly preserved much of the technical Stage 1/Stage 2 knowledge but
its immediate state was migration-era: Stage A/A3 and later migration stages were still pending.
Those migration instructions are superseded by the ratified migration close-out and must not drive
current development.

Earlier v0.1-v0.3 change history remains available in the historical handover files.
