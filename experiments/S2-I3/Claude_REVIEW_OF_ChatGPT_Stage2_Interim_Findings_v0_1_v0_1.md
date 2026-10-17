# Claude review of ChatGPT Stage 2 Interim Findings v0.1 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: `STAGE2_INTERIM_FINDINGS_v0_1_FOR_CLAUDE_REVIEW.zip`
Baseline: `35cd543b459a5856688f7c3795f73226e72311f8`

## 1. Verdict

**NOT CLEARED FOR INSTALLATION IN ITS CURRENT FORM. Four MUST findings.** None is a drafting slip; three arise from errors in Claude's own relayed material, which this review corrects with new measurements.

The document's authority discipline is sound: the evidence classifications, the "cannot supersede" boundary, the "NOT adopted" and "none authorised" markers, and the stand-down of the characterisation BAT are all correct. Nothing operative is smuggled in (question 4 answered in section 7).

The problems are technical:

- **M1.** The boundary direction is **inverted**. The statistic Claude relayed is for macroblocks adjacent *vertically*, which share a *horizontal* boundary. The document labels it a vertical boundary and then attaches the mechanistic interpretation to the wrong geometry.
- **M2.** The transition denominator is unstated, and the figures exclude all `NONE`-involving pairs. Over all adjacent pairs the numbers are roughly a third lower.
- **M3.** Section 4's boundary/interior split is geometrically mis-assigned, so the conclusion it supports understates the paired metric. Recomputed with per-macroblock geometry, the seam excess is **12.8% to 25.5%**, not the 7% to 10% the whole-frame figure implied. **This is Claude's error, not ChatGPT's**, and it propagated from Claude's analysis v0.2.
- **M4.** Sections 3 and 5 largely restate **K-02, K-03, K-07, K-08** and the existing `x=8` statement in `06_DEBLOCK_CONCEPT.md` as though they were new observations.

**Integrity:** both manifest hashes match (the backtick formatting defeats `sha256sum -c`, but the values are correct). All three files are US-ASCII with CRLF and contain no identity text. The proposed filename is correctly formed under the D-23 v1.2 filename amendment.

**Disposition recommendation (question 3):** do not install this as a standalone document. See section 8.

## 2. Faithfulness to Claude's source material (question 2)

Every figure attributed to Claude was checked against Claude's own run records. **All are faithfully transcribed**, including the negative results and caveats:

- section 3's four-row transform table, all five columns, matches exactly;
- section 4's paired MAE table (all/boundary/interior) and both blockiness columns match exactly;
- the blur results `+1.2%, +1.3%, -0.2%, +2.3%`, the `7.5%-26.8%` harm range and the `1.051-2.244` clean-original damage all match;
- `NONE` for XP rising "approximately 17% original to 74% blocky" matches the measured 16.97% and 73.66%;
- the ratio-divergence caveat and the "crude probes do not falsify per-MB-index-driven filtering" framing are both correctly preserved.

The transcription is accurate. The errors below are in the underlying material or its interpretation, not in the copying.

## 3. MUST findings

### M1. The boundary direction is inverted

**Verified from the analyzer source.** `Stage1_Inspector_Analyzer_v0_2.py` computes:

- `neigh_h`: pairs macroblock `i` with `i+1` - macroblocks **side by side**, sharing a **vertical** boundary (fixed x);
- `neigh_v`: pairs macroblock `i` with `i+w` - macroblocks **stacked**, sharing a **horizontal** boundary (fixed y).

Claude relayed the `neigh_v` figures. Those are transitions across a **horizontal** boundary. The document's own convention statement (section 1: "a vertical boundary is at a fixed x; a horizontal boundary is at a fixed y") makes the mislabelling unambiguous.

Claude's original phrasing, "vertical seams where type changes", was ambiguous and invited this. **The error originates with Claude.**

**Consequence for the mechanistic paragraph.** Section 3's interpretation currently reads:

> An MB-state transition at a *vertical* macroblock boundary does NOT mean that the location of that outer vertical boundary changes; it means the internal horizontal-transform geometry on the adjacent sides can differ.

That reasoning is correct *for a vertical boundary*, but the statistic is not about vertical boundaries. The correct statement for the relayed figures is:

> A FRAME/FIELD transition between vertically adjacent macroblocks means the **horizontal transform-seam pitch differs across that horizontal boundary**: the FRAME-DCT side carries an internal seam at 8 frame lines, while the FIELD-DCT side carries macroblock-edge seams only, at 8 field lines (16 frame lines). This is K-03 applied across a seam.

This is the substantive case, and the mislabelling currently points the reader away from it. Both directions should be tabulated, since both are now measured (M2).

### M2. The denominator must be stated; the figures exclude `NONE`

Claude's percentages used as denominator only those adjacent pairs where **both** macroblocks carry a coded residual transform (`FRAME` or `FIELD`). All pairs involving `NONE` were excluded from both numerator and denominator. The document does not say this, and asks for it directly.

Recomputed directly from the index reader, both directions, both denominators:

| Source | Shared VERTICAL boundary (side by side): mixed / coded pairs | % of coded pairs | % of all pairs | Shared HORIZONTAL boundary (stacked): mixed / coded pairs | % of coded pairs | % of all pairs |
|---|---|---:|---:|---|---:|---:|
| XP | 40777 / 263190 | 15.5 | 11.3 | 41093 / 261737 | **15.7** | 11.4 |
| SP | 17033 / 207878 | 8.2 | 5.6 | 17431 / 205755 | **8.5** | 5.8 |
| LP | 48341 / 204603 | 23.6 | 15.0 | 49005 / 204111 | **24.0** | 15.3 |
| TEST 3A | 29651 / 320772 | 9.2 | 6.4 | 31721 / 315915 | **10.0** | 6.9 |

The bolded column is what the document currently reports. The two directions happen to be close for the originals, so the magnitudes in section 3 are not wrong - but the label and the interpretation are, and the "all pairs" denominator is materially lower.

For completeness, the blocky encodes, coded-pair basis: XP_blocky 26.2 / 21.3, SP_blocky 22.5 / 19.4, LP_blocky 22.8 / 19.8, 3A_blocky 23.1 / 24.0 (vertical / horizontal). The blocky encodes converge on a similar transition rate despite very different originals.

### M3. Section 4's boundary/interior split is mis-assigned, and understates the metric

**This is Claude's error.** The boundary band in Claude's analysis v0.2 was defined on a frame-line 8-pixel grid in both directions. Per **K-03**, that is correct only for FRAME-DCT macroblocks: a FIELD-DCT macroblock has no internal horizontal seam at frame row 8. XP, SP and LP are 53% to 73% FIELD-DCT, so for most macroblocks in three of four sources the horizontal band was placed where **no seam exists**, diluting the measured excess with non-seam pixels.

Claude has recomputed the split using the per-macroblock transform state read from each blocky encode's own index, upsampled to pixels. Luma only, all frames, within-state comparison:

| Group | MB state | H-seam MAE (MB rows 7,8) | Interior MAE | H excess | V-seam MAE (MB cols 7,8) | V excess |
|---|---|---:|---:|---:|---:|---:|
| XP | FRAME | 4.465 | 3.735 | **+19.5%** | 4.609 | +23.4% |
| XP | FIELD | 6.255 | 6.059 | **+3.2%** | 7.525 | +24.2% |
| SP | FRAME | 2.977 | 2.562 | **+16.2%** | 3.088 | +20.5% |
| SP | FIELD | 5.642 | 5.462 | **+3.3%** | 6.856 | +25.5% |
| LP | FRAME | 6.495 | 5.539 | **+17.3%** | 6.792 | +22.6% |
| LP | FIELD | 6.696 | 6.522 | **+2.7%** | 8.048 | +23.4% |
| TEST 3A | FRAME | 6.611 | 5.860 | **+12.8%** | 6.829 | +16.5% |
| TEST 3A | FIELD | 8.484 | 8.296 | **+2.3%** | 9.877 | +19.1% |

Three things follow, and they matter more than anything in the draft.

**(a) K-03 is confirmed in the decoded pixels of the project's own material.** At the same pixel locations (macroblock rows 7 and 8), FRAME-DCT macroblocks show a 12.8% to 19.5% excess and FIELD-DCT macroblocks show 2.3% to 3.3% - a ratio of four to eight times. K-03 currently stands on H.262 text plus reference-decoder implementation; this is independent confirmation on real development material, which is a different and stronger evidence class.

**(b) The existing `x=8` statement is confirmed too.** The vertical-seam excess is 16.5% to 25.5% and present in **both** transform states, with no systematic FRAME/FIELD difference. That is exactly `06_DEBLOCK_CONCEPT.md`'s "the internal vertical transform seam lies at luma x=8 and does not depend on frame versus field DCT", now measured.

**(c) Section 4's pessimism is wrong and must be corrected.** The 7% to 10% whole-frame boundary excess that underpins the "global MAE is a weak objective" framing was an artefact of mis-located bands. Correctly located, the signal is two to three times larger. The weaker claim that survives is narrower: *most of the absolute paired error remains interior and irrecoverable, so a geometry-blind global MAE is diluted - but a geometry-aware, seam-localised paired measure has a healthy signal.* The draft must not carry the stronger claim.

Note that absolute MAE is much higher in FIELD-DCT regions than FRAME-DCT regions (XP 6.059 against 3.735 interior). Field DCT is chosen where vertical-temporal activity is high, so those regions are intrinsically harder. **Only within-state excess is comparable**; cross-state absolute comparison is meaningless and should not be drawn.

### M4. Sections 3 and 5 duplicate accepted knowledge

The mechanism content is already owned by `06_DEBLOCK_CONCEPT.md` v1.2:

- **K-02** - luma transform organisation varies per macroblock between frame and field DCT in suitable frame pictures.
- **K-03** - frame-DCT macroblock has an internal horizontal seam plus edge seams; field-DCT macroblock has edge seams only. This *is* section 3's mechanistic finding.
- **K-07** - `FRAME`/`FIELD`/`NONE` is applicable coded residual transform geometry; `NONE` includes skipped macroblocks and non-intra macroblocks with effective CBP zero, where a `dct_type` bit may still have been read. This *is* section 5's `NONE` correction, verbatim in substance.
- **K-08** - motion compensation can copy blocking off the current transform grid, bounding what a current-grid post-filter can target. This *is* section 5's inherited-blocking point.
- The `x=8` vertical-seam independence, and the requirement that multi-row operations use field-parity-aware access on interlaced material, are already stated in the same section.
- **O-04** owns the `NONE`-touching-edge policy question; **O-14** owns the parity-aware access question.

Sections 3 and 5 must be rewritten to **cite** these and present only what is new, which is measurement. Presenting accepted knowledge as fresh observation is precisely the "second incompatible verdict" risk the draft itself warns against in section 6 item 5.

## 4. What is genuinely new

Separating the measurement from the mechanism, these are the defensible new contributions:

1. **Pixel-domain confirmation of K-03 and the `x=8` statement on project material, with magnitudes** (section 3, M3 table). New evidence class for existing knowledge.
2. **Source heterogeneity in transform regime.** XP 70.9% FIELD against TEST 3A 67.9% FRAME. This is source characterisation, covered by no K item, and is the strongest available support for the owner's requirement to develop across source types.
3. **Quantified `NONE` composition**, which materially strengthens K-08 (section 5 below).
4. **Measured harm from geometry-blind filtering:** 1.051 to 2.244 MAE inflicted on clean originals.
5. **Transition rates between transform states**, both directions, both denominators (M2 table).

## 5. `NONE` composition: new support for K-08

The draft states correctly that `NONE` is not synonymous with `SKIPPED`. Claude has now measured the composition, as a percentage of all `NONE` macroblocks:

| Source | `NONE` MBs | SKIPPED in P | SKIPPED in B | INTER CBP=0 | other |
|---|---:|---:|---:|---:|---:|
| XP | 62669 | 2.6 | 37.4 | 60.0 | 0.0 |
| XP_blocky | 272084 | 9.4 | 26.9 | 63.7 | 0.0 |
| SP | 64536 | 2.7 | 35.0 | 62.3 | 0.0 |
| SP_blocky | 210261 | 9.0 | 27.2 | 63.7 | 0.0 |
| LP | 80286 | 1.9 | 29.6 | 68.5 | 0.0 |
| LP_blocky | 242335 | 8.4 | 23.2 | 68.4 | 0.0 |
| TEST 3A | 116585 | 7.6 | 14.4 | 78.0 | 0.0 |
| 3A_blocky | 285701 | 6.4 | 25.9 | 67.8 | 0.0 |

**Why this matters.** A skipped macroblock in a P picture has a zero motion vector by definition - that is the basis of the S2-I3 P-skip identity admission test - so its inherited content is **co-located** and remains grid-aligned. Every other `NONE` category may carry a non-zero motion vector: INTER with CBP zero explicitly can, and a skipped macroblock in a B picture reuses the previous macroblock's vectors rather than zero.

So the **guaranteed grid-aligned** share of `NONE` is only the SKIPPED-in-P column: **1.9% to 9.4%**. Between 90% and 98% of `NONE` macroblocks are potentially off-grid inherited content. K-08's concern is therefore the dominant case, not a corner case. That is a measured strengthening of a HYPOTHESIS-level item and should be recorded as such, not as a new K number.

The draft's two cautions here are both correct and Claude endorses them: prediction involves fractional-pixel interpolation, so inherited blocking is interpolated rather than rigidly displaced; and D-13's higher bar governs any motion-vector capture. Claude's earlier `.idx2` remark was raised as a possibility only, and the draft's handling of it is appropriate. **Stage 1 stays frozen.**

## 6. Reproducible procedure (question 1 and provenance request)

**Transform transitions and `NONE` composition.** Index metadata only; no media.

1. `read_index` from `stage2_index_reader_v0_2`; `TRANSFORM = {0: NONE, 1: FRAME, 2: FIELD}`.
2. Per record, macroblocks in raster order from `rec.iter_macroblocks()`, grid `rec.mb_width` x `rec.mb_height`.
3. Side-by-side pair = `(i, i+1)` where `x+1 < w`; shares a vertical boundary. Stacked pair = `(i, i+w)` where `y+1 < h`; shares a horizontal boundary.
4. Coded-pair denominator: both `transform != 0`. Numerator: coded pairs whose two values differ.
5. All-pair denominator: every adjacent pair, `NONE` included.
6. "Frames containing both" = records where the set of transform states contains both `FRAME` and `FIELD`; `NONE` is not required and not excluded.
7. `NONE` subclass: `coding == 1` split by `rec.picture_type`; else `coding == 3 and cbp == 0`; else other.
8. Summed over every record of the clip.

**Pixel measurement (M3 table).**

1. BestSource `VideoSource`, native YUV420P8, **plane 0 only**; no format conversion.
2. Per display frame: `d = |original_luma - blocky_luma|` in int16.
3. Transform map from the **blocky encode's own index** - the artifact being measured is in the blocky clip, so its residual geometry is the relevant one - per macroblock, upsampled 16x16 to pixel resolution.
4. Masks on macroblock-local coordinates `y % 16`, `x % 16`: H-seam band = rows 7, 8; V-seam band = columns 7, 8; interior = rows **and** columns both in {2,3,4,5,10,11,12,13}. Interior therefore excludes macroblock edges, internal seams and their immediate neighbours.
5. Accumulate `sum|d|` and pixel counts per (transform state, band) over all frames; excess = (band mean - that state's interior mean) / interior mean.
6. Luma only. No filtering. All media deleted afterwards; indexes retained.

Environment: VapourSynth R81, BestSource 22.0, NumPy 2.5.3 - the same versions recorded in the owner's committed S2-I2 `run_manifest.json`.

## 7. Answers to the seven review questions

**1. Accuracy, units, denominators, H/V language.** Three errors found: M1 (direction inverted), M2 (denominator unstated and excluding `NONE`), M3 (band mis-assignment). Exact definitions in section 6. The four-row transform table's magnitudes are reproducible; its label and interpretation are not correct.

**2. Faithfulness.** Confirmed in full, section 2. Negative results and caveats are preserved accurately.

**3. Duplication and D-05.** It does duplicate - M4. On D-05, note its own wording: "durable findings should be incorporated into the appropriate project document." That points away from a new standalone document. See section 8.

**4. Nothing smuggled in.** Confirmed. Claude checked specifically: no change to the ratified selection rubric (section 4's objective is marked NOT adopted); no QP branch adopted (section 6 item 3 is explicitly "under separately authorised S2-I4 or later"); no motion-index extension (section 5 defers to D-13); no media upload authorised by the note; the eight-source allow-list is preserved; EP/2A/4A hold-outs preserved to S2-I8; Stage 1 frozen; the characterisation BAT correctly stood down. The P0 status (M1 bracket fix plus S1-S3) is stated accurately.

**5. Missed distinctions.** Four, in section 9: chroma is absent entirely; the blockiness V figures mix two geometries; the paired-reference framing is already D-26 rather than new; and the H/V asymmetry deserves naming as a falsifiable test.

**6. 6A/7A, `NOTICE.md` and persistence.** Accurately stated. The persistence caution is correct and correctly scoped: `git rm` cannot remove historical blobs, and no later rewrite can reach third-party clones, forks or caches. Section 6.1's `.gitattributes` statement is correct - Claude verified no pattern matches `*.mpg` or `*.idx`, and existing tracked media reports `i/-text w/`, so the files are treated as binary with no EOL conversion. Claude will still verify the actual commit and full hashes from GitHub.

**7. D-23, identity, CRLF, install path.** Compliant. US-ASCII, CRLF, no identity text, versioned filename per the v1.2 amendment, and `docs/REPOSITORY/` matches the other authority and evidence documents. If installed, the predecessor-deletion rule does not apply, as there is no earlier version.

## 8. Recommended disposition (question 3)

**Do not install as drafted.** Two defensible routes; Claude recommends the first.

**Route A - defer to the S2-I3 evidence and gate report.** D-05 prefers incorporation into the appropriate document, and the project already has the pattern in `S2_I2_Evidence_and_Gate_Report_v0_1.md`. These are S2-I3-era measurements, and P0 has not yet run. Folding them into the S2-I3 evidence report when it is written is the cleanest fit, needs no new document, and avoids M4 entirely. The mechanism confirmations then enter `06_DEBLOCK_CONCEPT` at its next revision as evidence-level upgrades to K-03, K-07 and K-08 rather than as new K numbers.

**Route B - a much smaller interim note, if the owner wants the numbers recorded now.** The real argument for recording something now is that these measurements currently exist only in uncommitted Claude documents and chat, so there is a genuine loss risk. If the owner prefers that, the note should shrink to:

- provenance and limits (current section 2, which is good as written);
- the measurement tables only: M2's transition table with both directions and both denominators, M3's per-macroblock geometry table, section 5's `NONE` composition, the paired MAE and blockiness tables with the M3 correction applied;
- the open tests in section 6, trimmed;
- section 6.1 as written.

Sections 3 and 5 would become short pointers to K-02, K-03, K-07, K-08, O-04 and O-14, stating only that the measurements confirm them on project material. That removes the duplication and roughly halves the document.

Either way, **the M3 correction must be applied before anything is recorded.** The current section 4 framing would install a conclusion Claude has since shown to be too pessimistic.

## 9. SHOULD

**S1. Disclose or recompute the blockiness V figures.** Claude's vertical blockiness excess used a single 8-field-line pitch for every macroblock. Per K-03 that is right for FIELD-DCT and wrong for FRAME-DCT. The V column therefore mixes two geometries, and because the sources differ in regime (XP FIELD-dominated, 3A FRAME-dominated) the V values are **not comparable across sources** as published. Either recompute per transform state or state the limitation. The H column is unaffected, since the vertical seam is at `x=8` regardless.

**S2. Record that everything is luma-only.** Chroma appears nowhere in the draft. Under **D-25** chroma is in scope on mechanism, and **K-04** establishes that chroma does not follow the per-macroblock luma `dct_type` - so chroma geometry is a separate question that none of these measurements touch. One sentence prevents a later misreading.

**S3. State that the paired-reference framing is already D-26.** D-26 decides that the software-transcode pairs are secondary paired-reference evidence, "interpreted only as movement toward or away from their higher-quality decoded sources, not as pristine ground truth", and that real LG material is judged by seam-local diagnostics, no-harm measures and the owner's visual assessment. Claude's "move toward the original's own non-zero level" is a restatement of D-26, not a new proposal, and the seam-local measurement in M3 sits squarely in D-26's primary category. Saying so strengthens the note's own authority boundary.

**S4. Name the H/V asymmetry as a falsifiable test.** The vertical seam is at `x=8` irrespective of transform type, so its geometry needs no index; the horizontal seam pitch is knowable only from the per-macroblock state. **Prediction: index-driven geometry adds most of its value on horizontal seams and little on vertical ones.** M3 now gives the baseline magnitudes to test against, and section 6 item 2's direction-separated scoring would measure it at no extra cost.

**S5. Carry the `NONE` composition numbers.** Section 5 argues the point qualitatively; the table in section 5 above supplies the measured support, and the 1.9%-9.4% grid-aligned share is the single most useful number in it.

## 10. OPTIONAL

**O1.** Section 3's note that percentages may not sum to 100 from rounding is correct; the transform percentages are shares of all macroblocks including `NONE`, which is worth stating explicitly.

**O2.** Claude's own `Claude_ANALYSIS_OF_Paired_Reference_Metric_and_Sample_Pool_Extension_v0_2.md` carries the M3 error in its sections 1 and 3. It is an uncommitted review artefact, so it needs no formal supersession, but Claude will issue a corrected v0.3 if the owner wants a clean record.

**O3.** If Route B is taken, the "Reported" qualifier can be dropped from the tables Claude has now independently recomputed and documented in section 6, since the procedure is stated and repeatable.

## 11. Next step

1. ChatGPT decides between Route A and Route B with the owner, and applies M1 to M4 plus the accepted SHOULD items.
2. Claude diff-checks the result. No further rehearsal is needed; the measurements in this review are final and reproducible by the stated procedure.
3. Independently of this, P0 remains blocked only on the P0 M1 bracket fix plus S1-S3.
