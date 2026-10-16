# Claude - Stage 2 Seam Pixel-Test Options Table

**Filename:** `Claude_S2_Seam_Pixel_Test_Options_Table_v0_2.md`
**Version:** 0.2
**Date:** 2026-10-15
**Status:** Options for discussion at S2-I3/S2-I5. The project owner asked that all of them be tabled,
none discarded in advance, and the choice made openly with reasons. Not authority; it elaborates
Stage 2 v0.6 sections 7, 8.2 and 8.3 without changing them.

---

## 1. Frame of reference (unchanged)

The index decides **where** seams are (D-24). A pixel test at each known seam decides **whether** the
step looks like a block artefact rather than real detail. QP plus the user's strength setting decide
**how much** to correct. Every option below is a way of building that pixel test or its correction.
None of them locates seams from pixels.

## 2. Objective scoring (applies to every option)

- **Seam discrimination.** The index tells us which positions are seams. Steps at non-seam positions
  (for example x mod 16 = 4 or 12) are real detail plus noise. Steps at seams are the same plus
  blocking. Score how well each measure separates the two: hit rate at a fixed false-alarm rate, and
  AUC. Break it down by seam class, QP band and I/P/B. Internal positions inside NONE macroblocks form
  their own class (no coded seam, but possibly propagated blocking, K-08).
- **No-harm** (v0.6 section 13.2): output change away from seams, and change around strong natural
  edges.
- **Seam diagnostics** (v0.6 section 13.1), before and after filtering.
- **The owner's visual judgement** (D-26) is final. A good score means the test finds blocking without
  touching detail; it does not mean the result looks better.

Claude's informal preview (FFmpeg decode, vertical boundaries, coded internal seams, 5% false alarms):

| Clip | M2 hit / AUC | M3 hit / AUC | M4 hit / AUC |
|---|---|---|---|
| LP | 20% / 0.74 | 25% / 0.78 | 47% / 0.81 |
| LP_blocky | 52% / 0.85 | 48% / 0.86 | 44% / 0.86 |

## 3. The options

### 3.1 How the step across the seam is measured

| ID | Option | Note |
|---|---|---|
| M1 | Single-line step `abs(q0 - p0)` per row (H.264 style) | Simplest. The most noise-sensitive. |
| M2 | Mean `abs(step)` along the segment minus the in-block background step | Preview "plain" measure. |
| M3 | Signed mean step along the 8-sample segment, **per field**, minus the local slope | Blocking is a consistent offset along a segment; noise is not, so it averages out. |
| M4 | M3 divided by in-block activity + 1 | Activity masking (GBIM-like). Best on noisy LP in the preview. |
| M5 | Least-squares fit, per field and per row segment, of "smooth ramp + step at the boundary" across a window that straddles the seam (4 samples each side); the step amplitude is the measure | Decoded-pixel analogue of Liu-Bovik's shifted-block step model (ICASSP 2001; TCSVT 2002). It is a principled version of M3. It needs only decoded pixels and the index grid, **not** bitstream DCT coefficients, so Stage 1 is unaffected. |

### 3.2 How side flatness / activity is measured

| ID | Option | Note |
|---|---|---|
| F1 | `abs(p1 - p0)` and `abs(q1 - q0)` (H.264 beta-style) | Per line; noise-sensitive. |
| F2 | Local range `max - min` on each side | v0.6 quantity R. |
| F3 | Mean absolute in-block step per side, per field, along the segment | Noise-averaged. |

### 3.3 Decision rule

| ID | Option | Note |
|---|---|---|
| R1 | Step below a QP-scaled limit AND both sides flatter than a QP-scaled limit (H.264 form) | Rejects strong real edges by construction. |
| R2 | Step relative to activity above k, capped by a QP-scaled maximum | Ratio form; pairs naturally with M4. |
| R3 | Two modes (MPEG-4 Part 2 Annex F style): a stronger smoothing mode in flat regions, a gentle default mode elsewhere | Flatness chooses the mode. |
| R4 | Continuous weight (masking-weighted) instead of a yes/no decision | Correction scales smoothly with confidence. |

### 3.3a Coding-context input (MPEG-2 analogue of H.264 boundary strength)

| ID | Option | Note |
|---|---|---|
| B0 | None: thresholds depend on QP and seam class only | Current Stage 2 v0.6 plan (D-13: QP + transform state). |
| B1 | Integer boundary class from index coding state on each side (INTRA / INTER-coded / NONE / SKIPPED), used to choose or scale the thresholds | Like H.264 Bs, this is a **codec-side control, not a probability**. The data are already in the Stage 1 index (coding state, CBP), but consuming them goes beyond D-13's first metadata set. It needs an explicit owner decision at S2-I3/S2-I5, and its value feeds the S2-I10 metadata-retention list. No Stage 1 change. |

### 3.4 Source of thresholds

| ID | Option | Note |
|---|---|---|
| T1 | Own QP-scaled curves, fitted on the designated development material | v0.6 default. |
| T2 | H.264 alpha/beta tables as a **starting point** only | v0.6: "not adopted blindly". |

### 3.5 Real-edge protection (add-on to any combination)

| ID | Option | Note |
|---|---|---|
| P0 | None (rely on R1/R2 to reject strong edges) | Baseline. |
| P1 | Continuity check: a step that continues beyond the block span is real; leave it | Cheap and seam-local. |
| P2 | Gradient/edge-detector veto (Sobel or Canny style) near the seam | Heavier. Keep only if no-harm shows a gain over P1. |

### 3.6 Correction (kernel) family

| ID | Option | Note |
|---|---|---|
| K1 | Bounded `p0`/`q0` correction (v0.6 section 8.3 start) | Short support. |
| K2 | K1 plus smaller `p1`/`q1` participation in flat regions | v0.6 section 8.3 option. |
| K3 | DC-offset smoothing across the segment in flat regions (Annex F "DC mode") | Pairs with R3. |
| K4 | Shifted-DCT re-quantisation driven by the QP map (the idea behind FFmpeg's spp/pp7 filters) | This is **Family C** (`05` D-12): an optional quality reference that must not delay the main work. Heavier. The owner's 2026-10-08 ruling excludes existing filters as a **yardstick**, not the idea. |

### 3.6a Aggregate (image / region) blockiness diagnostics; not per-seam decisions

| ID | Option | Note |
|---|---|---|
| G1 | Wang-Bovik-Evans blind block-signal power (ICIP 2000), per field and per orientation | Literature-comparable severity score; useful before/after filtering. With the grid known from the index it largely overlaps the S2-I2 phase test and per-clip M2 aggregates. |
| G2 | GBIM (Wu-Yuen, IEEE SPL 1997): boundary versus non-boundary differences with masking weights | The same idea as M2/M4 aggregated per frame; useful mainly for comparability with published work. |

These are optional, read-only diagnostics. They do not choose the per-seam test.

### 3.7 Pre-processing

| ID | Option | Note |
|---|---|---|
| D0 | None | Recommended. |
| D1 | Mild denoise used for the **decision only** (the correction is applied to the original pixels) | Listed at the owner's request. Risk: a denoiser also softens block edges and adds parameters to tune. Test only if M3/M4 prove too weak. |

## 4. How to test without an explosion of combinations

1. **Screen the measurements first; no filtering needed.** Score M1-M5 and F1-F3 by seam
   discrimination on the K0-selection material (LP even GOPs), in **both orientations** (horizontal
   boundaries with same-field row access). Report uncertainty at the frame/GOP level, because adjacent
   segments are not independent samples. This is cheap and objective.
2. **Shortlist two or three full combinations** (one choice from each of M, F, R, T, P, K) from the
   screen plus a stated reason for each. Record the reasons for leaving out the others; nothing is
   dropped silently.
3. **Filter and score the shortlist** on discrimination, no-harm and the owner's visual review, using
   a selection rule declared before results are viewed. The winner becomes K0.
4. **Revisit at S2-I5 with real QP.** QP-scaled thresholds matter more once QP varies per macroblock,
   so a combination that lost under fixed QP may win with real QP. Rescore the shortlist (and any
   option the S2-I4 result makes newly relevant).
5. **At S2-I8 (the owner's clean all-clip run),** report the chosen combination's discrimination and
   no-harm results for every source, hold-outs included.

## 5. Why S2-I3 and S2-I5 are separate (they are the same activity, split on purpose)

The split exists only to answer one question fairly: does the real per-macroblock QP map beat a single
fixed QP? S2-I3 chooses and **freezes** a kernel (K0) using fixed QP on LP's even GOPs. S2-I4 then
compares fixed versus real QP on the **odd** GOPs with K0 unchanged. If the kernel had been tuned
together with the QP map, the comparison would be biased. After S2-I4, development continues freely
(S2-I5), and the options table above is carried through both steps.

## 6. Change log

### v0.2 - 2026-10-15

- Added M5 (Liu-Bovik-style step fit, decoded-pixel analogue), B0/B1 (MPEG-2 coding-context boundary
  class; owner decision needed because it consumes more index metadata than D-13), and G1/G2
  (aggregate blockiness diagnostics). These follow the owner's Copilot/Grok research and ChatGPT's
  assessment of it.
- Screening now covers both orientations and requires frame/GOP-level uncertainty.

### v0.1 - 2026-10-14

- First issue.
