# Claude review of ChatGPT S2-I3 v0.3 and revised Stage 2 v0.7 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: S2_I3_v0_3_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip
Baseline: `6e7b5c53df1c65775524936fc945c449cc9fa100`.

## 1. Verdict

**READY FOR OWNER RATIFICATION, conditional on four small wording edits.**

- There are no MUST findings.
- The four SHOULD edits (section 3) make the P-skip gate's semantics exact. Claude's re-check of them is a diff check only; no further design round is needed.

Verified:

- **Package integrity:** all manifest hashes match, except the manifest's own self-hash, which cannot match itself. All files are US-ASCII CRLF.
- **Identity:** both committable drafts are free of identity text, and the location has been removed from the S2-I3 header (M1 closed).
- **The v0.6-to-v0.7 patch reproduces v0.7 exactly** when applied to the repository's v0.6 (LF `6178a4f1...0b77`).
- **v0.6 history is preserved:** the whole change-log history, from the `### v0.6 - 2026-10-13 (RATIFIED)` entry to the end, appears verbatim in v0.7 (7,761 characters).
- **All previous findings are correctly applied:**
  - M2: hard structural checks plus exact P-skip identity. The invented applicability thresholds are removed, and the S2-I2 tests are kept unchanged as diagnostics.
  - S1: section 21 is marked historical, section 5.2 accepts an admitted index, and section 15 includes the four pairs.
  - S2: L and LB comparisons use the same three folds for every arm.
  - S3: selection optimism is stated.
  - S4: index hashes and tracking are recorded.
  - S5: S2-I3 is fixed-QP only.
  - O1 and O2 are applied.
- **Versioning:** the draft is correctly still v0.7, and S2-I3 is v0.3.
- **Hold-outs:** EP, 2A and 4A, with their `_blocky` copies, stay locked until S2-I8. The MLS pair are later controls, and the 704x576 3A is a full development source.

## 2. P-skip gate: applicability check (review item 2)

**Standard basis.** In an MPEG-2 P frame picture, a skipped macroblock is reconstructed by forward frame prediction with a zero motion vector and no residual. In frame pictures the prediction is frame-based, and there is no in-loop filter. The co-located 16x16 luma copy from the forward reference is therefore exact. The design states this correctly.

**Reference.** The reference is the immediately preceding I or P picture in display order, which is also the most recently decoded anchor. That is what Claude's rehearsal used.

**Edge cases, all covered:**

- A P picture with no preceding anchor has no comparison and is excluded.
- Field pictures are already rejected by section 5.2 and section 6.3.1.
- Decoder concealment of a damaged stream breaks identity, so it correctly FAILs.
- Leading-B frames are irrelevant, because they are not P pictures.

**Pixel handling.** Compare BestSource plane-0 values as 8-bit integers through the native stride-aware view, with no format conversion, exactly as the S2-I2 adapter does. State this in the implementation plan. It is not needed in v0.7.

## 3. SHOULD (wording edits; exact text supplied)

Quoted v0.7 passages are wrapped across lines in the file; they were matched with whitespace normalised.

**S1. A negative control at 100% is INCONCLUSIVE, not FAIL** (v0.7 section 6.3.2, "Disposition").

- A shifted window that also scores 100% means the content is too static to discriminate the offset. It is not evidence that the index is misregistered.
- Labelling it FAIL would mislabel a correctly registered source.

Replace:

> structural FAIL, any true-position mismatch, or an executed negative control showing 100% is **REGISTRATION FAIL - HARD STOP**. Insufficient qualifying blocks or P pictures, or a missing valid negative control, is **INCONCLUSIVE - QUALITY BLOCKED**.

with:

> structural FAIL or any true-position mismatch is **REGISTRATION FAIL - HARD STOP**. Insufficient qualifying blocks or P pictures, a missing valid negative control, or any executed negative control also reaching 100% (non-discriminating content) is **INCONCLUSIVE - QUALITY BLOCKED**.

The S2-I3 v0.3 section 3.1 wording is already consistent with this ("no valid control evidence means INCONCLUSIVE"). Add the same "or a control reaching 100%" clause there.

**S2. Define the qualifying block from the index, not by inference** (v0.7 section 6.3.2, after "Using the actual source index's P-skip flags"). Add:

> A qualifying block is a macroblock whose index coding state is SKIPPED (skipped by macroblock_address_increment) inside a P frame picture. NONE macroblocks of any other coding state (for example INTER with CBP 0, which may carry a non-zero motion vector) do not qualify.

**S3. State display order explicitly** (v0.7 section 6.3.2, negative controls).

- Replace "next decoded picture, and immediately previous decoded picture" with "next picture in display order, and immediately previous picture in display order".
- Replace "(the prior I/P anchor in display order)" with "(the immediately preceding I or P picture in display order, which is also the most recently decoded anchor)".

**S4. Shifted-window mechanics** (v0.7 section 6.3.2, negative controls). Add:

> The same offset is applied to the current and reference windows; only windows lying wholly inside the picture are counted.

## 4. OPTIONAL

**O1.** v0.7 has two adjacent `---` rules (around lines 801-803), at the end of section 6.3.4. Delete one.

**O2. Index tracking (v0.7 section 3.6).** The paths in `VHSC_samples/` and the conditions are sound.

- After staging, `git ls-files --eol` should show the seven `.idx` files as `-text`. Git detects them as binary, as it does the existing six, so no `.gitattributes` change is needed.
- Verify this, and the seven hashes, after the push.
- The Windows LP_blocky index must equal `b3f1d714...5238`, which the owner's S2-I2 run already confirmed. The six new indexes should equal Claude's Linux cross-check hashes; any difference must be investigated.

**O3. Do not commit the review patch files.** `S2_I3_v0_2_to_v0_3_Diff_FOR_CLAUDE.patch` contains, as a removed line, the location text that M1 took out. Review patches are process artefacts and should stay untracked.

**O4.** Optionally extend the P-skip identity check to the two 8x8 chroma blocks of each qualifying macroblock, which must also be exact copies. It costs little and adds confirmation. It is not needed as a gate.

## 5. Path to ratification

1. ChatGPT applies S1-S4 (and the OPTIONAL items it accepts) to v0.7 and S2-I3 v0.3, as the same version numbers, with a diff against this package.
2. Claude checks that the diff contains only those edits.
3. The owner ratifies Stage 2 v0.7 and S2-I3 v0.3.
4. Installing the ratified documents is a separate, bounded document commit, with v0.6 replaced under D-23.
5. S2-I3 implementation requires a separate owner authorisation. Its first run is the admission preflight on Windows; no filtering may happen until it passes.
