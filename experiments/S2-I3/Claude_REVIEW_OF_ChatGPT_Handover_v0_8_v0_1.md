# Claude continuity review of ChatGPT role handover v0.8 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: `ChatGPT_Handover_v0_8_FOR_CLAUDE_REVIEW.zip`, containing
`HANDOVER_CANDIDATE/docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md`
Baseline: `35cd543b459a5856688f7c3795f73226e72311f8`
Scope: continuity review only. **Independent of the pending S4 one-file diff-check**, which has not
been supplied to Claude and is not covered by any clearance in this document.

## 1. Verdict

**NOT CLEARED AS DRAFTED: two MUST findings, both one-line fixes. Cleared on their correction.**

This is a strong continuity document - the best-prepared handover either role has produced. Its
technical content is **accurate in every figure Claude could independently check**, which is 40-odd
numbers including all eight admission rows, all four pair rows, seven index hashes and seven commit
SHAs (section 3). It also carries forward the three corrections Claude had to make to its own
material on 2026-10-17, correctly, and in one place more carefully than Claude stated them.

The two MUSTs are not technical:

- **M1. Identity leak.** Line 6 appends a parenthesised time-zone string naming a city and region to the date. This file is
  destined for `docs/HANDOVER/` in the public repository, and D-23 v1.2's owner-identity amendment
  forbids geographic location in committed files. **This is the third recurrence of this exact error
  class** (the S2-I3 design v0.1 header, its v0.2, and Claude's own review text).
- **M2. A pointer to a file that the same commit deletes.** Line 162 sends the reader to "previous
  handover v0.7 (section 9)" for the V1-V4 reference-decoder evidence. Under D-23, installing v0.8
  **removes v0.7 from the current tree in the same change**, so that reference is broken the moment
  it is committed.

**Integrity:** both manifest hashes match. The candidate is US-ASCII, consistently CRLF (460/460
lines), no trailing whitespace, no tabs. `REVIEW_ONLY/` is correctly excluded from the proposed
install. One file, one additive path, correct `docs/HANDOVER/` placement, correct versioned filename
under D-23.

## 2. MUST

### M1. Geographic location in a file destined for the public repository

Line 6:

```
**Date:** 2026-10-17 (<city/region time zone - redacted in this review>)
```

Replace with:

```
**Date:** 2026-10-17
```

A time zone may be stated in review correspondence if it is ever useful, but not in a committed file.
Note for both roles: a bare date is sufficient throughout this project, and no committed file has ever
needed a zone.

### M2. The V1-V4 pointer is broken by the install itself

Line 162 currently reads, in part:

> Reference decoder evidence V1-V4 in previous handover v0.7 (section 9) remains historical bounded
> supporting knowledge.

Under D-23 v1.2, the commit that adds v0.8 **deletes v0.7**. The successor would then be pointed at a
file that is not in the tree, recoverable only from Git history - which is precisely what the
versioned-filename rule is meant to avoid for live references.

**The knowledge itself is safe**, which is why this is a one-line fix rather than a content problem.
All four verifications are cited in `06_DEBLOCK_CONCEPT.md`'s K table, which is ratified authority:

- **V1** -> K-03 (frame-DCT internal horizontal seam; field-DCT macroblock-edge seams only);
- **V2** -> K-04 (4:2:0 chroma does not follow luma `dct_type`);
- **V3** -> K-10 (same `quantizer_scale` across a macroblock; luma matrices for 4:2:0 chroma);
- **V4** -> K-11 (4:2:0 field prediction alternates chroma parity by line).

Suggested replacement:

> Reference-decoder verifications V1-V4 are carried as ratified knowledge in
> `06_DEBLOCK_CONCEPT.md` (V1 in K-03, V2 in K-04, V3 in K-10, V4 in K-11); the current Claude role
> handover also records them with source line references. Do not upgrade decoder-implementation
> observations to normative standards claims without checking the relevant source or standard.

Claude's handover carries the V1-V4 table with file and line references, so that is a second live
home for the detail.

## 3. Independent verification of the technical content

Claude re-checked every figure attributable to its own rehearsals and records. **All are correct.**
This is worth stating explicitly, because it is a large body of transcribed numbers.

**The eight-source admission table (section 6.3)** - correct in all eight rows, including which
negative control was highest and its offset. Claude confirmed each against its run records: the
"highest" value correctly picks the larger of the spatial maximum and the temporal controls in every
case (for example XP's spatial maximum is 48.9% at offset `-1,0`, so 83.9% for the previous frame is
right; XP_blocky's spatial maximum of 73.2% at `+1,0` correctly beats its temporal maximum of 37.6%).

**The four pair rows (section 6.3)** - correct: XP 140/228 with 3.53 against 9.88, SP 175/192 with
3.23 against 13.98, LP 81/204 with 4.39 against 9.93, 3A 268/300 with 5.53 against 19.95.

**The seven non-baseline index SHA-256 values (section 4.1)** - all seven correct, and correctly
distinguished from the six frozen baselines. The LP original baseline
`849b6a9c...0011` is correct and correctly excluded from the seven.

**Commit identities (section 2.1)** - `11f4742`, root tree `45ad1f16...`, `c45dcf0`, `4221f7f`,
`2286341`, `190bd06`, `6e7b5c5` and HEAD `35cd543...` all correct in their full forms.

**Q_fixed values** - XP 14, SP 16, LP 18, 3A 14, blocky Q62: correct, and the description as the
clip-wide median over all macroblocks including leading B and NONE is right.

**Section 7's corrected measurements** - every figure correct: the transform mix; the transition rates
in both directions and under both denominators; the seam-excess table for FRAME and FIELD in both
orientations; the 1.9-9.4% guaranteed-co-located share of NONE; the 2.244 MAE harm figure.

**The P0 gate description (section 6.1)** - matches the implementation. The 24 spatial offsets, the
three temporal controls, the requirement that each executed control have at least one valid comparison
and an aggregate identity rate below 100%, the display-order anchor rather than `n-1`, the 200-block
and 10-picture floors, and FAIL taking precedence over INCONCLUSIVE are all stated correctly.

### 3.1 Conceptual corrections carried forward correctly

The document handles the 2026-10-17 corrections properly, which was the main risk:

- the direction convention is now stated **correctly** - side-by-side macroblocks share a **vertical**
  boundary at fixed x, stacked macroblocks share a **horizontal** boundary at fixed y - and section 7
  adds the warning that a bare "vertical seam" label is dangerous unless it names the orientation;
- the FIELD organisation is correctly described as using an 8-field-line pitch (16 frame lines) with
  no frame-row-8 horizontal seam, which is K-03;
- Claude's **erroneous** v0.2 conclusion is explicitly refused, by name, with instructions not to
  quote its boundary figures;
- the vertical blockiness-index limitation (one field-grid pitch applied to all macroblocks) is
  recorded as not cross-source-comparable;
- the caution that FRAME DCT is an encoder choice and **not** permission to mix fields is stated
  prominently and tied to D-09.

**One place where the document is more careful than Claude was.** On the NONE composition it says the
remainder beyond guaranteed P-skips "**may** be off-grid predicted content, **not proof that all are
off-grid**". That is the correct epistemic status and a better formulation than Claude's. Keep it.

### 3.2 Other things checked and found right

- S4 is correctly held as **not cleared**, with the explicit instruction not to infer clearance from
  the base revised candidate. Accurate: Claude raised S4 and has not seen an S4 package.
- The as-at distinction on `00_PROJECT_STATUS_v0_7.md` is handled exactly right: the file says S2-I3
  implementation was unauthorised as at its ratification, the owner authorised it subsequently in
  conversation, and that is labelled a post-commit conversational authorisation rather than
  back-written into the document.
- `READY` is correctly described as a numerical report and not permission to filter.
- Hold-out protection "follows content, not filename" - correct, and the right lesson from the
  duplicate-sample episode.
- The MLS 352x288 / `progressive_frame` trap is recorded, with the correct generalisation that a
  nominal pair cannot be assumed to share geometry.
- The characterisation BAT is correctly stood down.
- The inspector short-read hazard and the no-pipe rule are correct.
- The CMD trap list is correct and complete, including the M1 parenthesis issue and the `for /f`
  ERRORLEVEL point.
- The three-track separation is preserved, with the instruction not to let the sample-pool or findings
  tracks obstruct P0.

## 4. SHOULD

**S1. The Status line will be false once installed.** Line 8 reads "ROLE HANDOVER DRAFT FOR REVIEW;
**NOT RATIFIED / NOT INSTALLED**". The moment it is committed, "NOT INSTALLED" is untrue.

This is the **sixth** occurrence of the install-time wording class in this project (the S2-I2 report,
status v0.6, Stage 2 v0.7, S2-I3 v0.3, status v0.7, and now this). Note the precedent, though: both
committed handovers carry a draft marker - Claude v0.9 says "DRAFT FOR OWNER REVIEW" and ChatGPT v0.7
says "REVIEW CANDIDATE" - so a draft marker in an installed handover is accepted practice and is
**not** a MUST. The specific claim "NOT INSTALLED" is the problem. At install, supply a copy whose
Status line is true at its own installing commit, as has been done for every other install package.

**S2. Line 4's parenthetical is factually wrong, and review item 7 asks about exactly this.** It says
"(review-file suffix added to this candidate only)", but the candidate filename is already
`ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md` - the intended installed name,
with no review suffix. The ZIP isolates it under `HANDOVER_CANDIDATE/` instead, which is a cleaner
approach anyway. **Delete the parenthetical.** As it stands the naming is unambiguous in the ZIP but
the document contradicts itself about it.

**S3. `git diff --cached --check` is listed without its known caveat.** Section 8 includes it among
the Git discipline commands. It **must not be used as a STOP gate**: it fails on the legitimate CRLF
evidence files under `experiments/stage2/results/` and on Markdown lines ending in two spaces (hard
breaks). This was found during S2-I2 Step B, where a proposed gate built on it would have blocked a
correct commit, and it was replaced by a check on `.gitattributes` only. Add the caveat, or the next
drafter will rebuild the same gate.

**S4. Durable operational rules present in the Claude handover are absent here.** Delegating build
*flags* to the `.vcxproj` and workflow files is right, and Claude is not asking for those to be
restated. But the following are **operational rules and traps**, several of which live only in the
role handovers, and the drafting role is the one most likely to need them:

- **The six local index regressions** are mandatory after an inspector project-file change or an exact
  MSVC toolset or compiler change, including a routine Visual Studio update that moves the compiler
  version; `.filters`-only changes are exempt; infrastructure-only means one LP smoke run. ChatGPT is
  the role that would propose such a change.
- **The `TESTING` BATs overwrite the tracked `.idx` and `.log` in `VHSC_samples/` in place.** Never
  commit regenerated baselines with `git add -A`. This is a live footgun.
- **The owner's git has `core.autocrlf=true`**, so `.py` and `.md` files are stored LF and appear CRLF
  in his working copy. Any hash statement must name the representation. ChatGPT quotes hashes
  constantly, so this belongs in its handover (example: the S2-I1 reader is CRLF `139f02c6...` in the
  working copy and LF `f9892039...` in Git).
- **`git ls-files --eol` should show the `.idx` files as `-text`** after staging, the check agreed for
  the seven-index commit.
- **Bump `plugin_version.h` before publishing a Release**, and the workflow checks the tag commit is
  in `main` history with `merge-base --is-ancestor`.
- Both binaries require an AVX2 CPU with no runtime detection, so there is no non-AVX2 fallback to
  offer.

None of this is lost project-wide, because Claude's handover carries it - but a ChatGPT successor
reading only its own handover would not have it.

**S5. Claude handover v0.10 now exists.** Line 132 and the supersession table say Claude "is
preparing" an updated handover. `Claude_HANDOVER_TO_Future_Claude_Chat_v0_10.md` was delivered on
2026-10-17, as at the same `35cd543` baseline, and is itself a draft for owner review. Update both
places so the two role handovers are mutually consistent when installed. They agree on every
substantive point Claude has compared.

## 5. OPTIONAL

**O1.** Section 2.1's abbreviated history jumps from `11f4742` to `c45dcf0`, omitting `eac5526`,
`bfb6cc2`, `bfaed24` and `10956a1`. It is labelled "abbreviated", so this is acceptable - but
`bfaed24` is the commit that installed Claude handover v0.9, which is mildly relevant in a handover.
One line would complete it.

**O2.** Section 6.2 says the overlay is "Seven BAT/three VPY/five Python". Correct, and it totals 15 -
worth keeping that arithmetic visible, since the count is also the install check.

**O3.** The document is 460 lines against Claude's 1116. That is a legitimate difference of style -
v0.8 delegates more to the owning authorities - and the owner's purpose text permits either, provided
the successor is not left reconstructing the model. With S4 applied, Claude judges it sufficient.

## 6. Continuity completeness (review item 6)

Claude compared v0.8 against the committed v0.7, which Claude wrote, so the comparison is
straightforward. v0.8 **gains** the whole S2-I2 closure, the ratified Stage 2 v0.7 and S2-I3 v0.3
design, the P0 state and rehearsal evidence, the sample-pool resolution and the findings track. It
**drops** only the build and change-control material covered in S4 above, plus the five
build-contract file hashes, which are legitimately delegated to the project files.

Nothing else that genuinely belongs in a role handover is missing. The policy, Restricted Media,
interlace and chroma, role, CMD and Git material is all carried, and in several places improved.

## 7. Verdict and install path

**CLEARED once M1 and M2 are applied.** Claude recommends S1 to S5 in the same revision; none needs a
further review round beyond a diff check.

Install path, when the owner ratifies:

1. ChatGPT applies M1 and M2 plus the accepted SHOULD items, and supplies an install copy whose Status
   line is true at its own installing commit (S1), with a fresh manifest.
2. Claude diff-checks that only those edits changed.
3. A separate bounded documentation commit adds
   `docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md` and **deletes**
   `..._v0_7.md`, under D-23 v1.2. Expect **1 A / 1 D** with `--no-renames`.
4. Claude verifies the pushed commit from GitHub, as for every previous commit.

**Claude recommends the two handovers be installed as two separate bounded commits**, Claude v0.10 and
ChatGPT v0.8, so each can be reviewed and verified on its own. They may also be combined into one
documentation commit (2 A / 2 D) if the owner prefers; in that case both must be cleared first.

**None of this blocks P0.** P0's revised candidate remains cleared, and the S4 variant remains
unreviewed and should be sent to Claude separately whenever the owner chooses.
