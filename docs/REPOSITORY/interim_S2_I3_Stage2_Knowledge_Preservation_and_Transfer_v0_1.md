# INTERIM - Stage 2 empirical knowledge preservation and planned transfer (v0.1)

Date: 2026-10-17
Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Intended installation path: `docs/REPOSITORY/interim_S2_I3_Stage2_Knowledge_Preservation_and_Transfer_v0_1.md`
Status: TEMPORARY PRESERVATION BRIDGE. Drafted by ChatGPT; **independently reviewed, corrected and
expanded by Claude in a single consolidation pass on 2026-10-17**, with Claude's own acquired knowledge
added directly into this file (sections 11 to 17). Installed on the project owner's ratification as an
evidence holding area, **not** as design authority.
Technical research baseline: `35cd543b459a5856688f7c3795f73226e72311f8`
Repository HEAD at consolidation: `3f8f45a77a8bbdd9d6bbc42718e6e74a2abd5e21` (an interim snapshot plus
one follow-up deletion; its miscellaneous review files are **not** authority and are pending removal)

**What this document is.** A single temporary register of Stage 2 empirical knowledge that exists
nowhere else in the repository, written because both development chats are long and may end without
warning. It records measurements, negative results, corrections and open questions, together with the
permanent destination agreed for each. It creates no criteria and changes no ratified design.

**Claude's consolidation verdict.** The draft was **technically accurate**. Claude re-checked every
figure against its own run records and found **no incorrect value**; the corrections in sections 3 to
7 are faithfully carried, including the three errors that originated with Claude. Claude made two
presentational corrections (the one-pass instruction block and the status wording, which would both
have been false once installed), answered the two questions the draft addressed to Claude
(sections 2 and 5), and added sections 11 to 17, which contain substantial Stage 2 knowledge the draft
did not hold - most importantly the **P-skip identity admission method** and the **pair-correspondence
rule**, which are the two methodological inventions of S2-I3 and were almost absent. No blocking
factual contradiction was found.

## 1. Why this note exists, and why it does NOT reverse Route A

The owner explicitly prioritises preventing technical knowledge loss across chat failure. Earlier on
2026-10-17 the owner ratified **Route A** after Claude reviewed the rejected
`Stage2_Interim_Findings_v0_1` candidate. Route A remains the intended FINAL disposition: (a) corrected
quantitative findings, limitations, methods, and provenance go into the eventual **S2-I3 Evidence and
Gate Report**; (b) durable confirmations/strengthenings of existing mechanism knowledge go into the
next controlled version of `06_DEBLOCK_CONCEPT` under **K-03, K-07 and K-08**; (c) no duplicate
permanent K-items or competing standalone authority.

This ONE interim file is an **exception for continuity/preservation**, due to credible risk of losing
two chats' uncommitted technical findings before the eventual gate report. It is an **evidence holding
area**, not a new source of operative criteria. Install by one exact named path; do not commit the
unreviewed draft, its patches, or correspondence. On completion of the eventual transfers, mark the
interim superseded and remove it from the current tree in a controlled versioned housekeeping change
under D-23 v1.2. Git history retains it until the project's Development Closure scrub. This cleanup is
not permission to alter history now.

Existing authoritative material (consult the current actual repository versions before updating):
`docs/REPOSITORY/05_DECISIONS_v1_2.md` including D-05, D-13, D-23, D-24, D-25, D-26;
`docs/REPOSITORY/06_DEBLOCK_CONCEPT.md` v1.2 or later including K-02/K-03/K-04/K-07/K-08 and
O-04/O-14; `docs/REPOSITORY/Stage2_Experiment_Design_v0_7.md`;
`docs/REPOSITORY/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md`; accepted
`S2_I2_Evidence_and_Gate_Report_v0_1.md`.

**Evidence taxonomy** used throughout: (1) **RATIFIED MECHANISM**: already in `06`, not re-decided
here; (2) **CLAUDE RECOMPUTED INDEX STATISTICS**: independently analysed from the eight development
indexes, metadata only, no pixels; (3) **CLAUDE MEASURED LUMA PIXELS**: exploratory Linux/BestSource
measurement on development sources, **not** an owner-run P0 result and **not** a Stage 2 filter gate;
(4) **INTERPRETATION/HYPOTHESIS**: testable claim, not established performance; (5) **SUPERSEDED**:
retained only so future chats know why it is wrong.

## 2. Provenance and correction chain - do not lose this

- `Claude_ANALYSIS_OF_Paired_Reference_Metric_and_Sample_Pool_Extension_v0_2.md` (Claude: whole-frame
  MAE, exploratory blur, blockiness, duplicate media); its seam-placement interpretation was
  subsequently corrected.
  **Claude's answer to the draft's question: no v0.3 of that analysis was ever produced.** It was
  offered and not requested before this document superseded the need for it. A successor should not
  search for a v0.3. **This file is now the corrected record**, and v0.2's boundary/interior figures
  must not be quoted (section 5).
- `Stage2_Interim_Findings_v0_1_FOR_CLAUDE_REVIEW.md` (ChatGPT: **not ratified and NOT installed**;
  faithful to its then-source but carrying propagated upstream errors).
- `Claude_REVIEW_OF_ChatGPT_Stage2_Interim_Findings_v0_1_v0_1.md` - the controlling correction record:
  **M1** inverted adjacent-boundary naming; **M2** missing denominator excluding `NONE`; **M3**
  incorrect row-7/8 seam mask and overly pessimistic interpretation; **M4** duplication of established
  K-02/K-03/K-07/K-08. Corrected tables and the counting recipe below originate in that review.
  **Three of those four were Claude's own errors**, not ChatGPT transcription errors; see section 16.
- Claude's role handover v0.10 section 7.7 independently carries a condensed corrected table.
- `Claude_VERIFICATION_OF_S2_I3_P0_Windows_Run_Status_v0_1.md` and
  `Claude_URGENT_Repository_Hygiene_Finding_3f8f45a_v0_1.md` matter for sequencing and integrity but
  are not measurement sources.

These are source titles for traceability, **not** instructions to commit working review artefacts.
All source analyses used development data only. No hold-out quality use is claimed anywhere. No
candidate filter has been evaluated in any of this work.

## 3. Geometry: established facts versus new empirical support

**RATIFIED / DO NOT REDECIDE.** K-02: mixed FRAME/FIELD residual transform organisation can vary per
macroblock. K-03: in a frame picture, a FRAME-coded luma residual has a mid-height horizontal internal
seam (between frame rows 7 and 8 of the 16x16 macroblock), whereas FIELD-coded residual luma has its
horizontal internal layout on a field-line grid and **no** seam across frame rows 7/8; both have the
luma internal **vertical** transform seam at x=8. K-07: FRAME/FIELD/NONE denotes applicable **coded
residual transform geometry**, not merely the presence or value of `dct_type`; NONE covers skipped
macroblocks and effective-CBP-zero non-intra macroblocks, and an absent `dct_type` bit does **not**
automatically mean NONE. K-08: motion compensation can carry older blocking away from the current
grid. Frame ownership (D-09) and field-parity-aware access constrain safe pixel operations; selecting
FRAME DCT does **not** authorise cross-field temporal mixing.

**Terminology, correction M1.** A **vertical boundary** runs along fixed x and is shared by
side-by-side macroblocks. A **horizontal boundary** runs along fixed y and is shared by stacked
macroblocks. The Stage 1 analyzer's labels `neigh_h` and `neigh_v` describe **neighbour traversal
direction, not line orientation**: `neigh_h` pairs `i` with `i+1` (side by side, **shared vertical
boundary**); `neigh_v` pairs `i` with `i+mb_width` (stacked, **shared horizontal boundary**). Claude
verified this against the analyzer source.

## 4. Recomputed index measurements: composition and mixed regime

**CLAUDE RECOMPUTED INDEX STATISTICS.** Fractions of ALL macroblocks including NONE; "frames
containing both" means records containing both FRAME and FIELD anywhere, NONE neither required nor
excluded. Rounding can affect totals.

| Original group | FIELD (%) | FRAME (%) | NONE (%) | Frames containing both FRAME and FIELD (%) |
|---|---:|---:|---:|---:|
| XP | 70.9 | 12.1 | 17.0 | 99.1 |
| SP | 73.4 | 5.9 | 20.8 | 99.5 |
| LP | 52.7 | 23.0 | 24.3 | 97.1 |
| TEST 3A | 7.6 | 67.9 | 24.5 | 92.3 |

Project material has markedly different transform regimes and extensive within-frame mixing, so a
global FRAME-or-FIELD choice cannot model all applicable coded residual geometry. **XP is 70.9% FIELD
while TEST 3A is 67.9% FRAME - opposite regimes.** This is a SOURCE-CHARACTERISATION result
strengthening the existing index-driven concept, and the strongest available measured support for the
owner's requirement to develop across source types. It is not new codec policy.

**Corrected neighbour transitions (M1 + M2).** A mixed transition requires both macroblocks coded
FRAME/FIELD with different states. The `coded denominator` counts a pair only if BOTH are FRAME or
FIELD; the `all-pairs` percentage uses every adjacent pair including NONE. **Never quote these
percentages without their denominator.**

| Original group | Shared VERTICAL: mixed / coded pairs | V: % coded | V: % all pairs | Shared HORIZONTAL: mixed / coded pairs | H: % coded | H: % all pairs |
|---|---|---:|---:|---|---:|---:|
| XP | 40777 / 263190 | 15.5 | 11.3 | 41093 / 261737 | 15.7 | 11.4 |
| SP | 17033 / 207878 | 8.2 | 5.6 | 17431 / 205755 | 8.5 | 5.8 |
| LP | 48341 / 204603 | 23.6 | 15.0 | 49005 / 204111 | 24.0 | 15.3 |
| TEST 3A | 29651 / 320772 | 9.2 | 6.4 | 31721 / 315915 | 10.0 | 6.9 |

Blocky counterparts, coded-pair basis only (VERTICAL / HORIZONTAL, percent): XP_blocky 26.2 / 21.3;
SP_blocky 22.5 / 19.4; LP_blocky 22.8 / 19.8; 3A_blocky 23.1 / 24.0.

The originally relayed 15.7 / 8.5 / 24.0 / 10.0 values are **HORIZONTAL** boundaries, not vertical.

## 5. Per-macroblock paired luma MAE, corrected row-7/8 interpretation (M3)

**CLAUDE MEASURED LUMA PIXELS.** Native decoded YUV420P8, plane Y only, all development frames;
per-pixel absolute difference between each higher-quality original and its Q62 `_blocky` transcode,
assigned by the **blocky encode's own** per-macroblock transform state. Comparison is **within** each
transform state. This is an empirical confirmation of existing mechanism, not a filter's gain and not
a quality threshold.

| Pair | MB state | H band rows 7,8 MAE | Within-state interior MAE | H-band excess | V band cols 7,8 MAE | V-band excess |
|---|---|---:|---:|---:|---:|---:|
| XP | FRAME | 4.465 | 3.735 | +19.5% | 4.609 | +23.4% |
| XP | FIELD | 6.255 | 6.059 | +3.2% | 7.525 | +24.2% |
| SP | FRAME | 2.977 | 2.562 | +16.2% | 3.088 | +20.5% |
| SP | FIELD | 5.642 | 5.462 | +3.3% | 6.856 | +25.5% |
| LP | FRAME | 6.495 | 5.539 | +17.3% | 6.792 | +22.6% |
| LP | FIELD | 6.696 | 6.522 | +2.7% | 8.048 | +23.4% |
| TEST 3A | FRAME | 6.611 | 5.860 | +12.8% | 6.829 | +16.5% |
| TEST 3A | FIELD | 8.484 | 8.296 | +2.3% | 9.877 | +19.1% |

For the FIELD state there is **no coded residual transform seam at frame rows 7/8**, so +2.3% to +3.3%
is a **control**, not a FIELD horizontal seam measurement. Applicable FIELD horizontal seams lie on
the field-line pitch, at different frame-line locations. The vertical x=8 seam exists in both states.
FRAME at rows 7/8 (+12.8% to +19.5%) against the FIELD control (+2.3% to +3.3%) - a factor of four to
eight - plus V signal in both states (+16.5% to +25.5%), supports **K-03** and the **x=8 independence**
on actual decoded project material.

Absolute MAE is much higher in FIELD regions because field DCT is chosen where vertical-temporal
activity is high. **Only within-state excess is comparable; never compare FRAME to FIELD absolute MAE
as a filter-effect estimate.**

**Critical correction.** The earlier Claude v0.2 whole-frame 8-line geometry-blind calculation reported
only 7-10% boundary excess and characterised paired MAE as a weak objective. Its mask sat at
nonexistent seams for most FIELD macroblocks - and XP, SP and LP are 53% to 73% FIELD - so the global
result **diluted a real signal**. **SUPERSEDED CONCLUSION:** "paired MAE is intrinsically too weak to
guide a deblocker". **Surviving narrower claim:** global geometry-blind paired MAE is dominated by
irrecoverable content differences, but a geometry-aware, seam-localised paired metric has usable
signal. Neither finding demonstrates a filter improvement. **This correction must accompany every
reuse of these numbers.**

### Reproducible method

1. Index: `read_index` from `stage2_index_reader_v0_2`; map `{0:NONE,1:FRAME,2:FIELD}`; macroblocks in
   raster order via `rec.iter_macroblocks()`; grid from the record header. For original/blocky luma
   comparison use the **blocky** index.
2. Pixels: BestSource `VideoSource`, native YUV420P8, **no** pixel format conversion, plane 0;
   `d = abs(int16(original_Y) - int16(blocky_Y))` for corresponding decoded display frames.
3. Band masks within the macroblock: H rows `y % 16` in `{7,8}`; V columns `x % 16` in `{7,8}`;
   interior requires **both** `y % 16` and `x % 16` in `{2,3,4,5,10,11,12,13}`, which excludes outer
   macroblock edges, the inner seam bands and their immediate neighbours.
4. Accumulate absolute-difference sums **and** pixel counts per transform state across all frames;
   `excess_percent = 100 * (band_mean / interior_mean - 1)`. Compare within state only. Record no
   result for NONE, which defines no current coded residual seam.
5. Transition recipe: side by side `(i, i+1)` for `x+1 < mb_width`; stacked `(i, i+mb_width)` for
   `y+1 < mb_height`. Count as mixed only if both are coded and the states differ. Keep coded-pair and
   all-pair denominators separate.
6. Research runtime: VapourSynth R81, BestSource 22.0, NumPy 2.5.3, CPython 3.13 on Linux. The owner's
   P0 Windows environment is embeddable CPython 3.14.8 with NumPy 2.5.4 - **not** the research runtime.
7. **Claude's answer to the draft's question on script availability: the analysis scripts are NOT
   retained.** They lived in an ephemeral session workspace and no raw per-frame CSVs were kept; all
   test media was deleted after use as `NOTICE.md` requires. **The method above is complete enough to
   rewrite them from scratch**, which is why it is specified at this level of detail. Treat every
   number in sections 4 to 7 as a *result to be reproduced* rather than a *file to be located*.

## 6. Paired original/blocky baseline, exploratory probes, and metric caveats

**CLAUDE MEASURED LUMA PIXELS, whole-frame** - a valid global baseline, **not** a seam-specific
geometry model:

| Pair | Global original/blocky luma MAE | Old geometry-blind boundary MAE | Old geometry-blind interior MAE |
|---|---:|---:|---:|
| XP | 3.567 | 3.745 | 3.428 |
| SP | 3.266 | 3.436 | 3.134 |
| LP | 4.355 | 4.588 | 4.173 |
| 3A | 5.512 | 5.748 | 5.329 |

The global column remains a broad paired-reference descriptor. **Do not use the old boundary/interior
columns to argue about FRAME/FIELD seam placement** - that is the M3 error. The original is a
higher-quality **encoded MPEG-2 reference**, not uncompressed ground truth (D-26).

| Pair | Blur across vertical edges | Within-field vertical blur | Combined | Naive cross-frame-line vertical blur | Same naive blur: harm to the clean original |
|---|---:|---:|---:|---:|---:|
| XP | +1.2% | -1.2% | -0.2% | -12.3% | 1.092 |
| SP | +1.3% | -0.3% | +0.8% | -26.8% | 1.557 |
| LP | -0.2% | -3.8% | -4.1% | -7.5% | 1.051 |
| 3A | +2.3% | -4.7% | -2.9% | -20.3% | 2.244 |

These were **crude fixed-geometry probe filters**, not candidate or ratified index-driven kernels, and
the figures are changes in **global** MAE. They cannot be reinterpreted as S2-I3 results.

**The most consequential number here is the harm column.** A naive cross-frame-line vertical blur
damages a **clean** original by 1.051 to 2.244 MAE, which is comparable to a large part of the entire
blocky-versus-original gap of 3.5 to 5.5. On 576i material vertically adjacent frame lines belong to
different fields and therefore different instants. **Frame DCT is an encoder rate-distortion decision
and is never by itself evidence that cross-field frame-line filtering is safe.** Field-parity access
remains an explicit invariant (D-09, O-14).

Claude's own crude probes applied **one** geometry globally and so were wrong for the majority of
macroblocks in three of four sources. Their near-zero results are evidence against **uniform**
geometry, **not** against index-driven filtering.

**Historical "blockiness excess" values - preserve WITH INVALIDITY LABELS.** Claude v0.2 computed a
*difference* between the mean step at periodic edges and the mean interior step. The 'H' axis (across
the x=8 vertical seam) gave ORIGINAL/BLOCKY: XP 1.614/2.313; SP 1.950/2.816; LP 2.319/3.169;
3A 1.726/3.352; this axis is unaffected by the vertical-pitch error because x=8 is transform-type
independent. The 'V' axis (field-line 8 pitch) gave XP 1.011/2.145; SP 1.472/2.879; LP 1.189/2.221;
3A 3.715/6.197, **but it mixes FRAME and FIELD coded geometries and is NOT comparable between
sources**. Neither axis is a P0 gate.

**The ratio form of this metric must never be used as a gate.** Claude also computed boundary/interior
as a *ratio* and it diverges on Q62 material whose block interiors are flat: measured H ratios were XP
69.0, SP 10.9, **LP infinite** (zero denominator) and 3A 2.2. Use the **difference/excess** form with
documented masks and denominators.

**D-26 already controls the evidence hierarchy.** Real LG media are **PRIMARY** feasibility evidence,
assessed with seam-local diagnostics, collateral/no-harm results and the owner's visual assessment.
Software-encoded Q62 pairs are **SECONDARY** paired-reference evidence, measuring movement toward or
away from a higher-quality *decoded* source. A direction-separated blockiness-excess target
approaching the original's non-zero value, geometry-aware local MAE, and paired global/boundary/
interior MAE are **candidate analytical measures only**, not adopted replacements for the ratified
S2-I3 rubric. A filter that reduces a seam statistic while damaging off-seam content must **not** be
called successful on the seam statistic alone.

## 7. NONE composition and inherited-blocking concern

**CLAUDE RECOMPUTED INDEX STATISTICS.** Percentages are of **NONE macroblocks only** per source, not
of all macroblocks.

| Source | NONE count | Skipped in P (%) | Skipped in B (%) | INTER CBP=0 (%) | Other (%) |
|---|---:|---:|---:|---:|---:|
| XP | 62669 | 2.6 | 37.4 | 60.0 | 0.0 |
| XP_blocky | 272084 | 9.4 | 26.9 | 63.7 | 0.0 |
| SP | 64536 | 2.7 | 35.0 | 62.3 | 0.0 |
| SP_blocky | 210261 | 9.0 | 27.2 | 63.7 | 0.0 |
| LP | 80286 | 1.9 | 29.6 | 68.5 | 0.0 |
| LP_blocky | 242335 | 8.4 | 23.2 | 68.4 | 0.0 |
| TEST 3A | 116585 | 7.6 | 14.4 | 78.0 | 0.0 |
| 3A_blocky | 285701 | 6.4 | 25.9 | 67.8 | 0.0 |

Only skipped macroblocks in **P** pictures are guaranteed co-located under the zero-motion identity
model that underlies S2-I3 P-skip admission (section 11). Skipped **B** macroblocks may reuse prior
motion; INTER with effective CBP=0 may carry vectors. So **1.9% to 9.4% of NONE is the guaranteed
zero-motion co-located portion, and 90% to 98% is *potentially* - not provenly - off-current-grid
inherited content.** Motion interpolation is fractional-pixel, so a copied boundary is not necessarily
a rigid displaced grid. The index records motion signalling, type and direction but **no motion-vector
components** (section 12), so grid displacement cannot be reconstructed from today's index. K-08 and
O-04 already own the policy risk; adding vector data or an `.idx2` requires fresh evidence meeting
D-13 and explicit authorisation, and **Stage 1 stays frozen**. Nothing here establishes how many of
the remaining NONE cases actually show off-grid visible blocking.

Q62 raises the NONE share markedly (XP original 17.0%, XP_blocky 73.7%). The correlation is
descriptive; no causal analysis was done. For later work consider `NONE` and `NONE`-touching edge
breakouts and I/P/B stratification as **hypotheses**, not filter rules.

## 8. Open breadth, quantisation and chroma questions (NOT authorised modifications)

- Q62 `_blocky` variants are an **extreme single quantisation point**; LP_blocky has completely flat
  block interiors. Generalising kernel settings from Q62 alone is risky. Additional encodes around
  Q25-Q40 could be evaluated as an independent future design amendment, with source-group weighting
  and correlated-variant handling - re-encodes of the same content are **not** independent samples.
  The two S2-I4 QP estimands remain separately governed. This is not authorisation to add media or
  change folds.
- **Falsifiable orientation prediction.** Index-driven geometry should contribute its largest
  incremental benefit for **horizontal** seam handling, where FRAME versus FIELD changes the seam
  placement, and least for the **vertical** x=8 seam, whose location is transform-type independent.
  Measure direction-separated gains and clean-source harm under comparable optimisation budgets.
  Currently a hypothesis; section 5 supplies the baseline magnitudes to test against.
- All measures in this note are **luma only**. D-25 retains chroma in scope; K-04 establishes chroma
  geometry is **not** simply the per-macroblock luma `dct_type`. Do not extrapolate these seam
  findings to U/V; chroma needs separate geometry and performance evidence.
- Richer metadata is justified only if current indexes demonstrably fail predeclared gates. Do not
  propose index-format extensions or an ad hoc pixel-only detector (D-24 family restriction) from this
  note.
- `TEST_6A_home_576i` and `TEST_7A_home_576i` original/blocky pairs are four distinct media hashes
  after duplicate aliases were removed (20 total `*.mpg`, no duplicate content at last check). They
  are **not** admitted P0 members and remain role-unassigned. Hash prefixes: 6A original
  `0F8656F69591EC69`, 6A blocky `0D53680AB8037FDA`, 7A original `C68E209FDE087D7A`, 7A blocky
  `17ABBC2C4EEB85AF`. All four **were** committed in interim snapshot `6b7acc3`, contrary to the agreed
  separate bounded commit shape; their history permanence and any later privacy or role decision must
  be handled independently of P0. They are roughly five to seven times longer than any current pool
  member, so unnormalised weighting would let 6A outweigh all four existing content groups combined.

## 9. Required final knowledge transfer - do not close this bridge early

After S2-I3 evidence gathering and review, the following must happen in versioned, independently
reviewed, owner-ratified repository updates. Mark completion explicitly with paths and commit IDs;
until then this interim document must not be silently discarded.

| Material to preserve | Permanent destination | Required treatment |
|---|---|---|
| M1/M2 transition table, transform-regime mixture, denominators, index reproducibility | S2-I3 Evidence and Gate Report | Full measurement/provenance; explicit index-only versus decoded classification; no retrospective gate inventions |
| M3 pixel seam table, mask and FIELD-control interpretation, and the correction history | S2-I3 Evidence and Gate Report | Preserve within-state comparisons and the discarded 7-10% conclusion; never mislabel the row-7/8 FIELD control as a seam |
| Baseline original/blocky luma, harmful blur probes, corrected metric hierarchy | S2-I3 Evidence and Gate Report, then any rubric change via existing decisions | Record what was exploratory; keep Q62 secondary evidence separate from real LG primary evidence |
| NONE-class table; P-skip guaranteed co-location versus potential displacement | S2-I3 Evidence and Gate Report | Values and uncertainty; no inference that all other NONE is off-grid |
| **P-skip identity admission method, controls, rehearsal and limits (section 11)** | S2-I3 Evidence and Gate Report | Preserve the standards basis, the field-swap blind spot and the IPPP limitation |
| **Pair-correspondence rule, derivation, rehearsal and floor disclosure (section 13)** | S2-I3 Evidence and Gate Report | Preserve the after-the-fact floor disclosure verbatim |
| **Cross-platform index determinism (section 14)** | S2-I3 Evidence and Gate Report, and Stage 1 evidence provenance | MSVC versus gcc byte identity, with the "within these samples" qualification |
| Real-media confirmation of horizontal seam geometry and the x=8 vertical seam | Next `06_DEBLOCK_CONCEPT` version, **K-03** | Evidence-level/citation upgrade; no new K item, no mechanism reversal |
| FRAME/FIELD/NONE semantics and sample applicability | Next `06_DEBLOCK_CONCEPT` version, **K-07** | Narrow proof/measurement links; preserve NONE non-synonymy with P-skip |
| Inherited motion / NONE empirical prevalence | Next `06_DEBLOCK_CONCEPT` version, **K-08** | Strengthen evidence and qualification; no implied motion-vector capture |
| H/V asymmetry, intermediate-QP breadth, chroma and field-safety open tests | Future Stage 2 / S2-I4+ design if authorised | Preserve as hypotheses; no gate or parameter policy change |
| Project hygiene and isolated-Python incident knowledge (section 15) | Next role handovers and operational evidence | No committed review ZIPs, no `git add -A`, scan inside archives, isolated-Python import behaviour |

**Retirement gate.** At the final transfer stage, verify every row above is reconciled and recorded in
its destination, then retire this bridge from the current tree under D-23 v1.2.

## 10. No accidental change of approved work

Nothing here authorises P1, filter implementation, additional media admission, a new QP branch,
deblocking thresholds, hold-out exploration, `.idx2`, Stage 1 changes, or modification of Stage 2 v0.7
or S2-I3 v0.3. S2-I3 P0A and P0B completed on Windows; P0C XP alone REGISTERED at last observed state;
remaining admissions, diagnostics, pairs, summary and independent review are outstanding. Exact
operational continuation belongs in `S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_2_FOR_CLAUDE_2026-10-17.md`,
not here. `READY_FOR_P1` is numerical, not owner authorisation. EP, 2A and 4A originals and blocky
hold-outs remain locked until S2-I8 **regardless of filename**. No filtering now.

---

# Claude's added knowledge (sections 11 to 17)

Added by Claude during the single consolidation pass. Each section states its evidence class and
permanent destination. These items were absent or only glancingly present in the draft.

## 11. The P-skip identity admission test - the central S2-I3 method

**Evidence class: RATIFIED MECHANISM (standards basis) plus CLAUDE MEASURED LUMA PIXELS (rehearsal).
Destination: S2-I3 Evidence and Gate Report.**

This is the methodological core of S2-I3 admission and was almost absent from the draft. It must not
be lost.

**Standards basis.** In an MPEG-2 **frame P picture**, a macroblock that the index marks SKIPPED is
reconstructed by forward frame prediction with a **zero** motion vector and **no** residual. There is
no in-loop filter in MPEG-2. Therefore its 16x16 luma block must equal, **bit-exactly**, the
co-located 16x16 block of the **immediately preceding I or P picture in display order**.

**Why this matters.** The test has **no tunable threshold**: a single mismatched pixel is a hard
failure. It detects spatial misregistration *and* temporal slips. That is why it replaced the S2-I2
phase-contrast gate for the wider pool (section 17).

**Known limitations, both important.**
- **A field swap is undetectable by this test.** If both fields were exchanged consistently, the
  co-located comparison still succeeds. Nothing in P0 detects that condition; it must not be claimed
  as covered.
- **A stream with no B pictures (IPPP) would be INCONCLUSIVE**, because the "previous picture in
  display order" control can never execute - it always equals the true anchor. All eight development
  sources contain B pictures, so this does not bite today, but it is a real limitation of the test.

**Structural preconditions enforced before any comparison:** `records[i].output_ordinal == i` for
every record (display order); picture type cross-checked against BestSource `_PictType` for every
frame; frame pictures only (`picture_structure == 3`); 4:2:0; coded dimensions and macroblock grid
consistent with the index header; native YUV420P8 with no format conversion; the anchor derived by
scanning display order for the last I or P picture, **never** as `n-1`.

**Qualifying block definition.** A qualifying block is a macroblock whose index coding state is
SKIPPED inside a P frame picture. `NONE` macroblocks of any other coding state - INTER with CBP 0, for
example, which may carry a non-zero motion vector - **do not qualify**. This is the K-07 distinction
applied operationally.

**Controls.** 24 spatial offsets (ten along x, ten along y, four diagonal), including all seven
historically known-bad S2-I2 offsets; the same offset is applied to **both** windows and only windows
wholly inside the picture are counted. Three temporal controls: the earlier anchor, the next picture
in display order, and the previous picture in display order, the last excluded wherever it equals the
true anchor. Controls are aggregated per source; per-picture exclusions are counted and reported.

**Disposition precedence.** A structural failure or **any** true-position mismatch is a hard FAIL.
Insufficient qualifying blocks or P pictures, a missing valid control, or **any executed control also
reaching 100%** (non-discriminating content) is INCONCLUSIVE. **FAIL takes precedence over
INCONCLUSIVE** - a correctness failure is never masked by a quality floor. Floors are **at least 200
qualifying blocks and at least 10 P pictures**; Claude verified these are exact boundaries, with
200 blocks and 10 pictures passing while 190 blocks or 9 pictures give INCONCLUSIVE.

**Claude's Linux rehearsal, all eight development sources: 100% exact identity, every control below
100%.**

| Source | Exact P-skips | Qualifying P pictures | Highest control (and which) |
|---|---:|---:|---|
| XP | 1619/1619 | 54 | 83.9% previous display |
| XP_blocky | 25635/25635 | 55 | 73.2% offset (+1,0) |
| SP | 1764/1764 | 46 | 77.7% previous display |
| SP_blocky | 19010/19010 | 46 | 73.3% offset (0,+1) |
| LP | 1533/1533 | 46 | 94.8% previous display |
| LP_blocky | 20300/20300 | 50 | 69.2% offset (+1,0) |
| TEST 3A | 8812/8812 | 133 | 96.7% previous display |
| 3A_blocky | 18190/18190 | 73 | 78.6% offset (-1,0) |

The **qualifying P-picture counts** are durable reference values that were not published in the
admission allow-list. They derive from the display-order anchor logic, so agreement on them is
independent evidence that two implementations chose the same anchor structure. The owner's Windows XP
admission reproduced 54 exactly.

**Negative rehearsals - all correctly FAIL** (percentage of qualifying blocks still matching):

| Injected fault | Exact-match rate |
|---|---:|
| XP frames with the XP_blocky index (encode swap) | 8.7% |
| XP_blocky frames with the XP index (reverse swap) | 34.0% |
| LP with a +1 frame display slip | 80.4% |
| TEST 3A with a -1 frame display slip | 84.8% |
| SP_blocky shifted 2 pixels horizontally | 71.1% |
| TEST 3A shifted 1 line vertically | 90.2% |

Note how high these residual rates are. A threshold-based gate set anywhere below 90% would have
**passed** the 3A one-line shift. That is the argument for exact identity over a tuned threshold.

## 12. Stage 1 index record structure, and what it cannot express

**Evidence class: RATIFIED MECHANISM / verified from source. Destination: reference detail for the
Evidence Report; already consistent with `02_INDEX_FORMAT_SPEC`.**

The per-macroblock record is **8 bytes**, `struct.Struct("<8B")`, decoding to: `transform`, `coding`,
`q`, `q_update`, `cbp`, `motion_type_raw`, `motion_dir_bits`, and a packed byte carrying
`motion_source` in bits 0-1 plus the `valid`, `q_inherited`, `pred_derived` and `dct_read` flags.
Mappings: `TRANSFORM = {0: NONE, 1: FRAME, 2: FIELD}`, `CODING = {1: SKIPPED, 2: INTRA, 3: INTER}`,
`PICTURE_TYPE = {1: I, 2: P, 3: B}`.

**There are no motion-vector components.** This is the hard boundary behind section 7's limitation:
the index can flag that a block is prediction-only and whether motion was signalled, but **cannot
locate** the inherited grid. Any proposal to capture vectors meets D-13's higher bar.

File layout: 32-byte header with magic `S1MBIDX1`, `struct.unpack("<8sHHIQII")`, endian marker
0x01020304 and a complete flag in bit 0; then per output frame a 64-byte record header (magic `FRM1`,
ordinal, picture type at byte 30, macroblock count as uint32 at offset 40) followed by 8 bytes per
macroblock. Size is `32 + N * (64 + MBs * 8)`; records are in **display order**, one per output frame.
At 720x576 that is about 13 KB per frame, so the much longer 6A/7A clips would produce indexes in the
10-20 MB range.

The only readable text in an index is the magic `S1MBIDX1` - no paths, no names - which is why index
bytes are machine-independent and are **not** Restricted Media.

## 13. The pair-correspondence rule

**Evidence class: INTERPRETATION with CLAUDE MEASURED LUMA PIXELS rehearsal. Destination: S2-I3
Evidence and Gate Report.**

Also nearly absent from the draft. It is what licenses any paired-reference metric at all.

**Notation.** `b_N` is blocky frame N, `o_N` the original, `MAE(x,y)` the mean absolute difference.
Candidate offsets k = -2..+2, kept in range.

**Decisive frame.** Frame N is **decisive** if

    min over k != 0 of MAE(o_N, o_{N+k})  >=  2 * MAE(b_N, o_N)

Because MAE is a norm, the triangle inequality gives
`MAE(b_N, o_{N+k}) >= MAE(o_N, o_{N+k}) - MAE(b_N, o_N)`, so in a decisive frame it is **impossible**
for any k != 0 to beat k = 0 when the pair is correctly aligned. In non-decisive frames - static or
fading content - the candidate originals are too similar to distinguish, and those frames are reported
as ambiguous rather than failed.

**PASS requires all of:** equal frame counts (otherwise HARD FAIL); a strict minimum of the clip-mean
MAE at k = 0; **zero** decisive-frame violations (otherwise FAIL); and at least **20** decisive frames
**and** at least **10%** of frames decisive (otherwise INCONCLUSIVE, which blocks paired metrics only).
Conditions 1 to 3 involve no tunable threshold; condition 4 is a sample-size floor.

**Claude's rehearsal - all four pairs PASS, zero decisive violations:**

| Pair | Decisive frames | Clip-mean MAE at k=0 | Best competing mean |
|---|---|---:|---:|
| XP | 140/228 | 3.53 | 9.88 |
| SP | 175/192 | 3.23 | 13.98 |
| LP | 81/204 | 4.39 | 9.93 |
| TEST 3A | 268/300 | 5.53 | 19.95 |

Simulated one-frame slips in either direction FAIL on all four: the argmin moves to the slip and
decisive frames collapse to 0-1. A frame-count mismatch gives a hard FAIL.

**Disclosure that must travel with this rule.** The 20-frame and 10% floors were **set after seeing
these numbers**. The aligned regime (42% to 93% decisive) and the slipped regime (0% to 1%) are so
widely separated that any floor between them behaves identically, but the disclosure is part of the
record and must not be dropped when this moves to the Evidence Report.

**Known limitation.** Fully static content, where the clip-mean is tied at k=0, is reported FAIL where
INCONCLUSIVE would be strictly more correct. Both outcomes block, and it cannot arise on the current
development pairs.

## 14. Cross-platform index determinism, and the eight index identities

**Evidence class: CLAUDE RECOMPUTED plus owner-run Windows confirmation. Destination: S2-I3 Evidence
and Gate Report; relevant to Stage 1 evidence provenance.**

Claude derived the eight development index SHA-256 values independently on Linux, using a `gcc -O2`
build of the frozen inspector sources, before any Windows run existed. The owner's Windows run, using
the MSVC-built frozen inspector, generated six of them and **reproduced every value byte-for-byte**,
along with frame count, geometry and P-skip count.

| Label | Frames | Geometry | P-skips | Index SHA-256 |
|---|---:|---|---:|---|
| XP | 228 | 720x576 | 1619 | `4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127` |
| XP_blocky | 228 | 720x576 | 25635 | `8d0326b5975b19b36742717a80be9eaf11bc21f379f2855eb22651e94dd16b20` |
| SP | 192 | 720x576 | 1764 | `40a97ce1a9920cd63e45da13371e0b41ff1619fed688d6145899a300463cc5d9` |
| SP_blocky | 192 | 720x576 | 19010 | `7e19ca6078075e7bf7a3a34bcda0816267e4d38ad02a56e01b6b0ed726ace746` |
| LP | 204 | 720x576 | 1533 | `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011` (frozen baseline) |
| LP_blocky | 204 | 720x576 | 20300 | `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238` |
| TEST 3A | 300 | 704x576 | 8812 | `9a60a8d24a7e4a45cbe82b4f41d232ede0e5c00624e82a8f8099f61351957f33` |
| 3A_blocky | 300 | 704x576 | 18190 | `e6f556dd4aaed0f4709b7c011fcf045193dccbb8abd2a01c646dddf0da893c83` |

Also measured by Claude but **not** a P0 member: `LG_576i_5_MLS_blocky.idx`
`915bee8ce95ea9fa58d283b38ba445427a7ab7402ee15e71e6c9dd38ab46d1da`.

**Finding: the frozen inspector is deterministic across compiler and platform**, and the index format
serialises no machine-dependent field - consistent with the magic being its only readable text.
Qualify this as holding **within these samples**; it is not a proof for every MPEG-2 stream.

**Q_fixed values**, the all-macroblock median effective quantiser used as the fixed-QP control: **XP
14, SP 16, LP 18, TEST 3A 14**, and **62 for every `_blocky` encode**. These are measured source
properties, not tuned results.

**A pair must never be assumed to share geometry.** `LG_576i_5_MLS_blocky` is **352x288 with
`progressive_frame=0`** while its original is 352x288 progressive - the pair cannot be used for paired
metrics without resampling. Always verify frame count **and** geometry for both members of any pair.
This is the generalisable trap, and it is why P0's structural checks test both members.

## 15. Operational knowledge that would be expensive to rediscover

**Evidence class: verified operational fact. Destination: role handovers and operational evidence.**

- **Embeddable/isolated Python does not add the launched script's directory to `sys.path`**, and
  **ignores `PYTHONPATH`**. Claude verified both: under `-I` the plain invocation fails with
  `ModuleNotFoundError` for the sibling module, and setting `PYTHONPATH` does **not** fix it. Explicit
  `sys.path.insert` is the only route. The owner's VapourSynth interpreter is exactly this case
  (`python314._pth`, `sys.flags.isolated=1`, `sys.flags.safe_path=True`). **Test every script
  invocation under `-I` as well as plain before clearing it.**
- The project's own `.vpy` adapters already solve this internally with
  `HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))`. Adding that idiom to a test
  module makes it robust under any interpreter - the more idiomatic long-term fix, deliberately not
  taken mid-run to keep the Python files byte-identical to the rehearsed set.
- **Reproducibility caution.** When re-testing that a unit suite fails closed, inject the failing test
  **before** the trailing `if __name__=='__main__': unittest.main()` line. Claude's first attempt
  appended after it, so the injected test was defined after the suite had already run and exited, and
  the run reported success. The fix is sound: a failing assertion, a syntax error and a missing
  sibling module each give a non-zero exit through `runpy.run_path`.
- **BestSource writes cache files outside the working tree** (on Linux, under a `bsindex` directory
  keyed by the media path). These are decode indexes, not pixels, but they are derived artefacts that
  should be removed along with media after any rehearsal. Claude deletes them and verifies none remain.
- **CMD traps** that have each cost real time: no two processes appending to one log; no digit directly
  before `>` or `>>`; **no unescaped `(` or `)` inside a parenthesised block's echo text**; `for /f`
  does **not** set ERRORLEVEL from the command it runs, so clear the target variable first and gate on
  `if not defined`; every `exit /b` should print a reason.
- **`git diff --cached --check` must not be used as a STOP gate.** It fails on the legitimate CRLF
  evidence files under `experiments/stage2/results/` and on Markdown two-space hard breaks.
- **`core.autocrlf=true`** on the owner's machine means `.py` and `.md` are stored LF in Git and appear
  CRLF in the working tree, so **every hash statement must name its representation**. Worked example:
  `stage2_index_reader_v0_2.py` is CRLF `139f02c6...` in the working tree and LF `f9892039...` in Git.
- The **BestSource plugin binary** used for the owner's P0 run is bit-identical to the one recorded in
  the accepted S2-I2 evidence (DLL SHA-256
  `fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c`, `PluginVersion(22,0)`). NumPy
  moved 2.5.3 to 2.5.4, which is immaterial to exact-integer work but belongs in the provenance record.

## 16. Correction history - Claude's own errors, recorded deliberately

**Evidence class: process record. Destination: role handovers; summarised in the Evidence Report's
provenance.**

Three of the four MUST findings against the rejected `Stage2_Interim_Findings_v0_1` were corrections
to **Claude's own** material, not ChatGPT transcription errors. Recorded so a successor understands why
the corrected values are the trustworthy ones.

1. **Inverted boundary direction (M1).** Claude described the `neigh_v` statistic as "vertical seams",
   when those pairs are stacked macroblocks sharing a **horizontal** boundary. The magnitudes were
   right; the label and therefore the mechanistic interpretation were wrong.
2. **Unstated denominator (M2).** Claude's percentages silently excluded all `NONE`-involving pairs.
3. **Mis-located measurement band (M3), which reversed a published conclusion.** Claude's band used a
   frame-line 8-pixel grid, correct only for FRAME-DCT macroblocks, in sources that are 53% to 73%
   FIELD. The corrected per-macroblock measurement shows two to three times the signal, so the
   "paired MAE is a weak objective" conclusion was withdrawn.
4. **Rediscovery of accepted knowledge (M4).** Claude presented as a finding what the project had
   accepted as **K-03** since 2026-10-08.

**Root cause.** Claude measured, concluded and relayed into a repository-document proposal **without
first checking the findings against `06_DEBLOCK_CONCEPT.md`**. The P0 code track, which has a review
gate, produced no comparable errors.

**Standing rules adopted as a result**, now in Claude's handover: check any finding against the
existing K and O items before describing it as new, and offer a confirming measurement as an
**evidence-level upgrade** rather than a new K item; and keep exploratory measurements in review
correspondence until a gate report needs them.

A separate Claude error of a different kind: the **S4 recommendation** to run the new unit tests under
the VapourSynth interpreter was correct in intent but verified inadequately - Claude tested
absolute-path invocation with a **non-isolated** interpreter while recommending one that is isolated by
default, having already seen `python3 -I` fail earlier in the same session. The lesson is in
section 15.

## 17. Why S2-I3 needed a new admission test, and what S2-I2 still provides

**Evidence class: CLAUDE MEASURED, plus accepted S2-I2 evidence. Destination: S2-I3 Evidence and Gate
Report.**

**The S2-I2 phase-contrast gate cannot admit the wider pool.** Run as a diagnostic over the eight
development sources, its original thresholds report **PASS** for XP, XP_blocky, LP, LP_blocky and
3A_blocky, but **BLOCKED** for **SP, SP_blocky and TEST 3A**. Claude established that these blocks
arise from **test preconditions, not misregistration** - the same three sources pass exact P-skip
identity at 100%. This is precisely why S2-I3 adopted the identity test, and it is why the S2-I2
diagnostics are **descriptive only** in S2-I3. A historical BLOCKED value is **not** a P0 failure.

**The S2-I2 numerical engine is sound and reusable.** `stage2_registration_stats_v0_1.py` is generic
across MB-aligned sizes, 704 width and leading B pictures, and S2-I3 reuses it unchanged. Claude
confirmed reuse fidelity directly: re-running the engine through the new S2-I3 adapter on LP and
LP_blocky produced CSV outputs **byte-identical** (after line-ending normalisation) to the committed
Windows S2-I2 evidence - all eight CSVs per source.

**What could not be reused:** the S2-I2 *adapter* hard-codes its label as
`'LP_blocky' if stem endswith '_blocky' else 'LP'`, so every source would be mislabelled LP; and the
S2-I2 BAT accepts only LP or LP_blocky. Hence the new per-source diagnostic adapter.
`stage2_check_result_v0_1.py` must **not** be used as an S2-I3 gate.

**Also from S2-I2, resolved and worth keeping:** the M4 discrepancy was settled - the engine is correct
at 23.79%, and the earlier 47% preview used adjacent-slope comparators, recorded separately as the
**M4a** proposal. And the BestSource/FFmpeg agreement claim must stay at its corrected strength:
byte-identical CSVs are **strong evidence of decoder agreement, not pixel-by-pixel proof**.

## 18. Consolidation record

**2026-10-17, Claude, single pass as instructed.**

- Verified every figure in sections 3 to 8 against Claude's own run records: **no incorrect value
  found**. Both source documents were US-ASCII, CRLF, free of identity text and free of trailing
  whitespace on arrival.
- Replaced the draft's opening one-pass instruction block, and its "NOT YET REVIEWED / RATIFIED /
  INSTALLED" status line, with an installed-document header. Both would have been **false** in the
  repository the moment the file was committed - the same install-time wording class that has now
  recurred seven times in this project.
- Answered the two questions the draft addressed to Claude: **no v0.3** of the paired-reference
  analysis exists (section 2), and the **analysis scripts are not retained**, which is why the method
  is specified in full (section 5 item 7).
- Aligned the evidence-taxonomy labels, which the draft used inconsistently between its taxonomy and
  its section headings.
- Added sections 11 to 17, the substantive Claude-only knowledge: the P-skip identity method with its
  controls, rehearsal, negative tests and two limitations; the index record structure and its
  inability to express motion vectors; the pair-correspondence rule with its derivation and floor
  disclosure; cross-platform index determinism with all eight identities and Q_fixed; operational
  knowledge including isolated-Python behaviour; Claude's own correction history; and why S2-I3 needed
  a new admission test.
- Added four rows to the section 9 transfer table for the new material.
- **No category was left as `NONE IDENTIFIED`** - every heading the draft requested has content.
- No ratified design decision was reopened, no competing authority created, no number invented, and no
  further review cycle requested. **No blocking factual contradiction was found.**

This document is complete and install-ready. It remains a temporary bridge; section 9 governs its
retirement.
