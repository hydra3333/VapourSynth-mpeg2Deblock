# ChatGPT technical assessment — Copilot and Grok MPEG-2 blocking-detection research

**Date:** 2026-10-14  
**Project:** `VapourSynth-mpeg2Deblock`  
**Status:** Discussion and independent-review material; **not ratified project authority**  
**Intended recipients:** project owner and Claude (independent reviewer/designer)  
**Input:** owner-provided `Pasted text.txt` containing three Copilot answers and one Grok answer; Claude's `Claude_S2_Seam_Pixel_Test_Options_Table_v0_1.md` as supplied in the conversation.  
**Source preservation:** Appendices A and B reproduce the user-supplied conversation text **verbatim in wording**, with only CRLF/LF line-ending normalisation. Markdown code fences prevent its original Markdown and embedded fences from being modified. The exact prompt to Grok was **not** supplied; only the owner's description of asking Grok a similar question is available.

## 1. Executive judgement

**The sources help identify promising families of measurements, but neither provides defensible evidence for a best-to-worst ranking on our particular material.** They share several legitimate sources—Liu–Bovik, Wang–Bovik–Evans and List et al.—yet repeatedly blur three different problems:

1. **Candidate seam geometry:** _where_ a coded seam can be. Our frozen MPEG-2 index governs this, not a blind pixel detector.
2. **Seam-local decision and estimated severity:** _whether_ a known candidate seam contains compression-related discontinuity, how large or visible it is, and whether smoothing might be justified without damaging real detail. This is the project's unresolved pixel-measurement problem.
3. **Image-/region-level blockiness quality assessment:** _how blocky_ an image looks overall. A no-reference quality metric may be excellent for (3) yet not identify each seam reliably for (2).

Copilot and Grok are most useful as **a map of candidate feature families**, not as tested selections. Their numerical ratings such as 9.5/10, assertions of 'highest recommendation', and forecasts about 'likely to outperform' contain no head-to-head validation on our VHS-C / LG / MPEG-2 corpus. They should not be promoted into project decisions.

**Recommended disposition:** keep Claude's M1–M4 / F1–F3 baseline experiment; add a small, explicitly justified research inventory and a no-reference/global blockiness diagnostic, rather than replacing the method or implementing a large hybrid detector immediately.

## 2. Why Claude's `_blocky` 44–52% 'hit rates' are not necessarily poor

Claude's preliminary, **FFmpeg-decoded and vertical-seam-only** demonstration at **5% false-alarm rate** reported:

| Metric | Original LP: hit / AUC | LP_blocky: hit / AUC |
|---|---:|---:|
| M2, segment mean abs step minus background | 20% / 0.74 | 52% / 0.85 |
| M3, signed field-segment mean minus slope | 25% / 0.78 | 48% / 0.86 |
| M4, M3 divided by local activity + 1 | 47% / 0.81 | 44% / 0.86 |

**Those positives and negatives are structurally labelled seam versus non-seam samples, not human- or ground-truth-labelled 'visibly blocked' versus 'not blocked' samples.** Therefore 52% does **not** mean 48% of true block artefacts were missed; nor does AUC 0.86 establish a 86% real-edge/artificial-edge classification accuracy. A 5% allowed false-alarm rate is deliberately strict, and AUC measures the overall ranking over a full range of thresholds.

Possible contributors to overlap—**hypotheses to examine, not findings**—include:

- Many index-defined transform boundaries have no **visible** jump in their decoded pixels; genuine scene edges can land on seam or control positions. Conversely, prediction can propagate earlier blocking into nominal non-seam positions; NONE has no internal **coded residual transform seam** but is not guaranteed free of inherited artefacts.
- VHS noise/texture and genuine detail weaken segmentation of seam steps; high quantisation alone does not guarantee a discontinuity at every candidate edge.
- A re-encoded `_blocky` clip may be visually strongly blocked in some positions or orientations without showing high discrimination in *every sampled vertical segment*; a frame-average visual impression is not a per-seam label.
- The sampling geometry, field parity, FRAME/FIELD/NONE eligibility, phase alignment, edge polarity, signed averaging, control-selection method and treatment of flat/strong-natural-edge subsets all materially affect the result.
- The owner has approved `LP_blocky` as a **secondary S2-I2 diagnostic/control**; its coding distribution and independently validated scratch index are **not established** by the evidence available to this assessment. Do **not** assume precise geometry or successful BestSource/index correspondence before validation.

A useful **sanity-control experiment** would be to compare original LP and LP_blocky on independently validated indexes, both directions and appropriate coded seam classes, while retaining matching source-frame/subset information. An original-LP versus re-encode pair can estimate **additional** compression changes; original LP is already MPEG-2-compressed and is **not** an artefact-free reference. All outcomes must be reported with the proxy-label caveat.

Before redesigning a detector, Claude should provide or confirm: (a) explicit positive/negative definitions and counts; (b) per-orientation, seam class, I/P/B and GOP results; (c) actual index/clip hashes and validated registration; (d) field/sample coordinates; (e) ROC and threshold provenance; (f) control positions and any matching or exclusions; and (g) distributions/percentiles as well as single hit/AUC numbers. Report confidence/uncertainty at the *frame/GOP* level rather than treating many adjacent pixel samples as independent observations.

## 3. Research findings: what is substantiated, and what is overstated

### 3.1 Liu–Bovik (2001; related 2002 paper): high-interest severity/visibility concept

**Verified:** The 2001 *DCT-domain blind measurement of blocking artifacts in DCT-coded images* models a blocking discontinuity across adjacent blocks as a two-dimensional step in a re-formed/shifted block. Its research programme estimates blocking severity and perceptual visibility in the **DCT domain** and includes reduction. The authors' laboratory explains the method and its domain clearly [R1–R3].

**Caution:** Calling this a proven per-seam classifier of 'real VHS detail versus compression artefact' in **decoded interlaced MPEG-2 pixels** is a substantial extrapolation. The original DCT-domain efficiency presumes the relevant DCT representation. Our current Stage 1 index contains coded-structure metadata but not a retained table of actual DCT coefficients. A decoded-pixel adaptation would need explicit computation/design and interlace-aware testing. It must not silently enlarge the index or reopen frozen Stage 1.

**Recommendation:** Research **one local shifted-block / step-versus-continuation feature** if M2/M3/M4 underperform on representative material. Treat full paper-faithful DCT implementation as a separate feasibility decision, not immediate S2-I2 scope.

### 3.2 Wang–Bovik–Evans (2000): valuable no-reference impairment metric, not local truth labels

**Verified:** *Blind Measurement of Blocking Artifacts in Images* models a non-blocky image plus an interfering blocky signal and estimates that block signal's power; authors explicitly discuss possible luminance/texture masking [R4].

**Caution:** A useful *blockiness severity* estimator is not automatically a reliable **binary local artefact classifier** or a calibrated per-MB deblock strength control. The source does not establish exceptional immunity to VHS noise or superiority over M2–M4 on this corpus.

**Recommendation:** Candidate for **diagnostic / pre-vs-post no-reference impairment score**, preferably calculated per field and grid/seam class before aggregation. Keep local detector selection separate.

### 3.3 H.264 / List et al. (2003): excellent engineering pattern, not a transferable probability

**Verified:** The H.264 adaptive deblocking mechanism combines **codec-side boundary strength** (intra/inter coding, motion and presence of residual), **QP-dependent sample-level thresholds**, and tests of differences across and on either side of the boundary [R5–R6]. The original paper explicitly discusses interlaced complications and propagation of blocking by motion compensation.

**Material correction to both AIs:** H.264 boundary strength **Bs = 0..4 is not a probability** that a discontinuity was caused by coding, and it is not simply a blind pixel-based classifier. It depends on H.264 syntax and coding structure; the pixel checks are a separate component. Its 4x4 coding grid and QP-to-threshold tables cannot be copied naively into MPEG-2's 8x8 residual coding and quantiser scales, and our frozen index does not necessarily contain the H.264-style motion-reference detail.

**Recommendation:** Retain **H.264-inspired** local side-gradient, QP-scaled limits and non-destructive edge guard as low-cost candidate features, while designing their parameters **for MPEG-2**, not importing H.264 boundary-strength semantics or QP thresholds.

### 3.4 GBIM (Wu–Yuen, 1997): a useful omission from the AI shortlists

**Verified:** Wu and Yuen's *A generalized block-edge impairment metric for video coding* is a no-reference measure designed specifically for blocking distortion and includes perceptual weighting [R7]. A later research comparison notes a family of alternatives, including mean squared difference of slope, boundary discontinuity, phase correlation, power spectrum and DCT-step metrics [R8].

**Recommendation:** Include **GBIM** as a concrete candidate aggregate metric alongside Wang–Bovik, rather than treating all 'HVS-aware metrics' as one vaguely attributed method. Comparing several aggregate scores with the owner's visual judgment is worthwhile; this does **not** identify the winning local deblocking kernel.

### 3.5 Continuity, orientation, periodicity and field consistency: hypotheses, not universal rules

- **Continuity:** Real contours often persist beyond one 8/16-pixel block; however, genuine short details exist, and predicted compression edges can also propagate. Good possible **real-edge veto**, not proof of origin.
- **Grid periodicity / Fourier peaks:** Useful to **validate grid phase and aggregate blockiness**; poorly suited on its own to classifying each individual seam, especially after interpolation, motion compensation or inherited blocking. We already know seam locations from the index.
- **Orientation:** The 0°/90° preference of blocking is helpful diagnostically but does not make every axis-aligned scene edge an artefact.
- **Field-to-field correspondence:** Potentially valuable but **motion, field time separation and analogue timebase errors** make naive equality/coherence tests unreliable. Keep separate top/bottom-field access and an explicitly motion-aware design if considered later.
- **Denoising before measurement:** A denoised **decision-only** branch could improve variance of a statistic, but could also suppress exactly the discontinuity we need to measure. Compare D0 against D1 only after simpler measurements are fairly tested; original pixels must remain the filter input unless separately authorised.

Grok's 'hybrid detector likely to outperform' and both AIs' VHS-suitability scores remain **unverified predictions**. A larger feature set can overfit or increase false positives as easily as improve performance.

### 3.6 Filtering tools are not detector rankings

**QED**, the HolyWu VapourSynth **Deblock** plug-in, DFTTest and BM3D are useful historical/practical context but primarily **filters or denoisers**, not head-to-head evaluations of local detection accuracy [R9–R10]. In particular, Deblock_QED's documented approach combines full-frequency correction at block borders with low-pass/DCT-filtered correction inside blocks; it is not a demonstrated probabilistic classifier of artificial edges.

Consistent with the existing project ruling, **do not insert existing external deblockers as Stage 2 quality yardsticks** merely because Copilot lists them. The idea underlying a method may be studied separately where authorised.

## 4. My evidence-based priority order for our actual project

This is an **investigation priority**, **not a validated quality ranking**:

| Priority | Candidate / feature | Primary function | Recommended treatment |
|---|---|---|---|
| A, retain now | M2/M3/M4 and M1 control; F1–F3 | Local step/activity discrimination at *known* seams | Baseline study first; proper orientation, field, class and noise controls |
| A, retain now | QP-scaled H.264-*inspired* gradient/edge protection; P1 continuity | Avoid destroying real detail; limit correction | Candidate for later S2-I3/S2-I5 screening, not H.264 Bs copied literally |
| B, cheap supplementary | Wang–Bovik and/or GBIM; periodic/grid-phase score | Image/region aggregate impairment, strength, independent sanity check | Read-only diagnostics; keep separate from per-seam classifier |
| B, conditional | Simple local continuity / cross-block coherence | Supplementary real-edge veto | Only if simpler measures have significant no-harm shortcomings |
| C, research | Liu–Bovik step/DCT visibility adaptation | Advanced local visibility/severity feature | Prototype only with scoped cost, required data and objective evaluation defined |
| C, defer | Multiscale contours, motion-aware field consistency, D1 decision-only denoise | Address special failure modes | Test after evidence of simpler methods failing |
| Not recommended as evidence | General 'best deblocker' lists; 9.5/10 or 'excellent' labels | None for this project's comparison | Treat as opinions only |

No blind method can **always** infer whether a local step originated in the scene, VHS artefacts or MPEG quantisation from the decoded pixels alone. The practical objective is **selective, bounded and visually safe correction**, with explicit uncertainty and no-harm checks, not an impossibly perfect classifier.

## 5. Proposed experiment sequence without scope creep

1. **S2-I2 remains registration-only.** Complete spatial index-to-pixel validation on original LP as the formal gate; use the separately approved `LP_blocky` diagnostic role, if the needed index/metadata validation passes. Do not turn S2-I2 into a filter contest.
2. **All-sample read-only survey where practicable:** develop later automation from a source manifest, one shared analysis engine and a reviewed BAT front-end. Separate structural characterisation of all available sources from formal tuning/hold-outs. Never overwrite six frozen indexes or commit new candidate `.idx` without owner approval.
3. **Audit Claude's preliminary metrics:** rerun both x/y directions and stratify by interlaced geometry and I/P/B; document matching negative controls and sample counts. In particular, test a visually strong, separately validated `_blocky` case and investigate any conflict with the expected phase/geometry.
4. **During S2-I3:** screen existing M1–M4/F1–F3 first, with original LP even GOPs for K0 selection as ratified. Compare justifiable additional features only if they answer a specific weakness. Do not rank a blind *global* metric as if it were a per-seam detector.
5. **During S2-I4:** freeze K0 and compare fixed-versus-indexed QP using the reserved LP odd GOPs. Do not adjust thresholds after seeing the controlled test outcome.
6. **During S2-I5:** revisit the options using real QP and actual failure modes, including possible visibility/step and edge-continuity features; allow more ambitious work only if evidence justifies the extra complexity.
7. **During S2-I8:** final frozen-parameter all-source/no-harm/visual reporting with hold-outs, not training on hold-outs. The owner's judgement remains the final quality criterion.

If changes to ratified Stage 2 v0.6 or experimental sample-role assignments are necessary, identify and ratify them explicitly. None is silently enacted by this research note.

## 6. Specific review questions for Claude

Please independently assess **each** issue below and separate MUST/SHOULD/OPTIONAL findings.

1. Do you agree that the published 'hit rate' is a **seam-versus-control proxy**, not sensitivity for a true 'visible artefact' ground truth? If not, supply your exact definitions/labels.
2. What **precise statistics, coordinates, field handling, sample counts, thresholds, source/index hashes and negative-control selection** produced the LP and LP_blocky results? Were both recordings independently registered and indexed?
3. Does the regression show expected behaviour in **both orientations** and all applicable FRAME/FIELD/NONE, outer/internal, I/P/B classes? Are unclassifiable or unsupported cases explicitly excluded/reported?
4. How much of `_blocky` low hit rate could come from **true proxy-label overlap**, geometry, field structure, high scene detail, activity normalization or insufficient registration? What is a minimally costly falsification test for each hypothesis?
5. Would you assign Wang–Bovik and GBIM **global/region impairment** roles, rather than promise seam-by-seam classification? Can they be added as optional numerical diagnostics without complicating S2-I2?
6. For Liu–Bovik, what is the exact input data and implementation scope needed for a **decoded-pixel analogue**? Is a lightweight shifted-block statistic sufficient as an initial experiment? Would anything require extra bitstream metadata (and therefore an explicit authorisation gate)?
7. For H.264, do you agree **Bs is an integer codec-side filtering control**, not a probability, and that MPEG-2 QP/geometry require separate rules? Which pixel-local features are cheap enough to warrant comparison?
8. Is a small **continuity veto** more relevant than a multiscale, optical-flow or field-to-field detector for the first K0 screening? Specify failure modes and no-harm measures.
9. Which proposed research additions **actually change Stage 2 v0.6** and require owner ratification? Which can remain options table / research evidence only?
10. Recommend a bounded next step that does **not** start unapproved S2-I3 work, alter frozen Stage 1, use outside deblockers as yardsticks or contaminate locked hold-outs.

**Request:** Please provide an independent summary answering the owner's question, distinguishing **verified literature claims**, **reasonable engineering adaptations** and **unsupported AI exaggerations**, and discuss whether the existing M2/M3/M4 results should change our near-term plan.

## 7. Sources independently checked for this assessment

These references document the existence and relevant mechanisms of the methods, **not** proof that one is superior for our recordings. Web metadata, abstracts, author laboratory descriptions and available paper text were checked on 2026-10-14; no exhaustive systematic review or validated VHS-specific leaderboard was found in this bounded check.

- **[R1]** A. C. Bovik and S. Liu, *DCT-domain blind measurement of blocking artifacts in DCT-coded images*, ICASSP 2001. DOI: `10.1109/ICASSP.2001.941272`. https://dblp.org/rec/conf/icassp/BovikL01
- **[R2]** S. Liu and A. C. Bovik, *Efficient DCT-domain Blind Measurement and Reduction of Blocking Artifacts*, IEEE TCSVT, vol. 12 no. 12, 2002. DOI: `10.1109/TCSVT.2002.806819`. https://www.researchgate.net/publication/3308460_Efficient_DCT-Domain_blind_measurement_and_reduction_of_blocking_artifacts
- **[R3]** Liu/Bovik authors' research summary: https://www.live.ece.utexas.edu/research/dct_video/dct_index.htm
- **[R4]** Z. Wang, A. C. Bovik and B. L. Evans, *Blind Measurement of Blocking Artifacts in Images*, ICIP 2000. DOI: `10.1109/ICIP.2000.899622`. https://ece.uwaterloo.ca/~z70wang/publications/icip00.html
- **[R5]** P. List, A. Joch, J. Lainema, G. Bjøntegaard and M. Karczewicz, *Adaptive Deblocking Filter*, IEEE TCSVT vol. 13 no. 7, 2003. DOI: `10.1109/TCSVT.2003.815175`. https://ieeexplore.ieee.org/document/1218194
- **[R6]** Public paper copy: https://mcube.lab.nycu.edu.tw/wiki/core/uploads/Research/SelectedTopics/Adaptive%20Deblocking%20filter.pdf
- **[R7]** H. R. Wu and M. Yuen, *A generalized block-edge impairment metric for video coding*, IEEE Signal Processing Letters, 4(11), 317–320, 1997. DOI: `10.1109/97.641398`. https://research.monash.edu/en/publications/a-generalized-block-edge-impairment-metric-for-video-coding
- **[R8]** Overview of comparative no-reference metric families: *No-reference visually significant blocking artifact metric for natural scene images* (2009). https://www.sciencedirect.com/science/article/pii/S0165168409000681
- **[R9]** Didée Deblock_QED explanation retained in public AviSynth script comments: https://github.com/Dogway/Avisynth-Scripts/blob/master/EX%20mods/DeblockPack.avsi
- **[R10]** HolyWu VapourSynth-Deblock documentation: https://github.com/HolyWu/VapourSynth-Deblock
- **[R11]** S. D. Kim, J. Yi, H. M. Kim and J. B. Ra, *A Deblocking Filter With Two Separate Modes in Block-Based Video Coding*, IEEE TCSVT, 1999. https://ieeexplore.ieee.org/document/744282/ (valid option for flat vs textured filtering, not a direct head-to-head detector ranking)

---

## Appendix A — Original owner questions to Copilot and Copilot's three answers

The following block includes the exact questions transcribed by the owner, the owner's intervening comments, and all three Copilot responses in their original wording. Their claims are reproduced for **review**, not endorsed.

`````text
Hello. I asked copilot these questions:
#############################################
a query about video and vapoursynth processing for deblocking in regard to mpeg2 types of blocking in very noisy VHS-C to DVD (MPEG2) captures via an old LG VHS to DVD recorder using "LP" mode (the "best" mode) and ripping thos home DVDs to .mpg files witgh mpeg2 video and audio.  mpeg2 blocking is known to be quite complex especially for interlaced sources.  Can you extensively research good block-edge detection (and strength determination) algitithms and list them (with attributiion) in a list rated/ordered by you from best to works ?

and

precisely yes to "block-edge detection and blockiness measurement" and "Is this edge a DCT artifact or a real VHS detail edge?" as I am not interested at code right now, only identifying and ranking those 2 things.

and

ok please do that research paper in the context of those 2 things.
#############################################

I struggled with copilot somewhat.
With the the copilot results (below) I asked to grok a similar thing - with GROK's results below Copilot's answers.
After reading both sets of answers, what do you make of all that ?  Doe it make anything clearer ?
Please provide a .md (including clearly copying/identifying the question(s) and answers from each of copilot/grok in appendices) of your response I can provide to claude asking the same thing I asked you.

Copilot Answers in 3 parts:
#############################################
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# MPEG-2 Deblocking for VHS-C → DVD Recorder Captures

## Scope

This document focuses on MPEG-2 blocking artifacts produced by consumer DVD recorders (such as LG VHS-to-DVD units) when capturing noisy VHS-C material and recording in LP mode. The emphasis is on:

1. Block-edge detection
2. Blockiness strength estimation
3. Adaptive deblocking for interlaced MPEG-2 sources

---

# Ranked Algorithms and Approaches

## 1. H.264 Adaptive Deblocking Filter (Highest Recommendation)

**Authors:** Peter List, Anthony Joch, Jani Lainema, Gisle Bjøntegaard, Marta Karczewicz

**Paper:** Adaptive Deblocking Filter (IEEE TCSVT, 2003)

Links:
- https://mcube.lab.nycu.edu.tw/wiki/core/uploads/Research/SelectedTopics/Adaptive%20Deblocking%20filter.pdf
- https://ieeexplore.ieee.org/document/1218194

### Why it ranks #1

The filter evaluates:

- Boundary strength
- Quantisation severity
- Local gradients
- Neighbouring sample differences

before deciding how aggressively to filter an edge.

This remains the foundation of many modern adaptive deblocking systems.

### VHS MPEG-2 suitability

Excellent.

Particularly effective when severe MPEG-2 macroblocking coexists with analogue VHS noise.

---

## 2. QED (Didée)

**Author:** Didée

Link:
- http://avisynth.nl/index.php/Deblock_QED

### Key idea

QED attempts to estimate actual blocking severity rather than blindly smoothing all block boundaries.

It distinguishes:

- Boundary artifacts
- Internal block artifacts
- Legitimate image structure

### VHS MPEG-2 suitability

Excellent for preserving detail.

Often produces more natural results than stronger deblockers.

---

## 3. Edge-Classified Adaptive Deblocking

**Authors:** Sung Deuk Kim, Jaeyoun Yi, Hyun Mun Kim, Jong Beom Ra

Paper:

A Deblocking Filter With Two Separate Modes in Block-Based Video Coding

Link:
- https://static.aminer.org/pdf/PDF/000/323/430/deblocking_algorithm_in_mpeg_video_coding_using_block_boundary_characteristics.pdf

### Key idea

Classify regions as:

- Flat areas
- Edge/detail areas

and apply different filtering strengths.

### VHS MPEG-2 suitability

Very strong.

Especially useful when VHS noise could otherwise fool simpler detectors.

---

## 4. Wang-Bovik Blind Blockiness Measurement

**Authors:** Zhou Wang, Alan C. Bovik, Brian L. Evans

Links:
- https://ece.uwaterloo.ca/~z70wang/publications/icip00.html
- https://eceweb.uwaterloo.ca/~z70wang/publications/icip00.pdf

### Key idea

Model:

Image = Natural Image + Block Signal

Estimate the power of the block signal without access to the original image.

### VHS MPEG-2 suitability

Excellent block-strength estimator.

Particularly valuable for automated restoration pipelines.

---

## 5. Liu-Bovik DCT-Domain Detection and Visibility Analysis

**Authors:** Shizhong Liu, Alan C. Bovik

Links:
- https://live.ece.utexas.edu/publications/2001/sl_icassp_2001_dctblk.pdf
- https://www.colorado.edu/lab/live/home/research/DCT/blocky

### Key idea

Treats visible block boundaries as DCT-domain step functions.

Uses:

- Visibility estimation
- Edge classification
- Human visual system concepts

### VHS MPEG-2 suitability

One of the strongest research approaches for blockiness measurement.

Less likely to confuse analogue noise with blocking than simple spatial methods.

---

## 6. VapourSynth Deblock (Practical Choice)

Repository:
- https://github.com/HolyWu/VapourSynth-Deblock

Package:
- https://pypi.org/project/vapoursynth-deblock/

### Notes

Implements H.264-style adaptive deblocking logic as a post-processing filter.

Tunable through:

- quant
- aoffset
- boffset

### VHS MPEG-2 suitability

Very good practical starting point.

---

## 7. DFTTest-Assisted Deblocking

### Notes

DFTTest is not strictly a deblocker.

However many visible MPEG-2 artifacts originate from quantisation noise.

Light frequency-domain denoising can improve later block-edge detection significantly.

### VHS MPEG-2 suitability

Very useful companion stage.

---

## 8. BM3D-Assisted Detection and Cleanup

### Notes

BM3D is primarily a denoiser.

Reducing VHS noise before deblocking frequently improves adaptive edge classification.

### VHS MPEG-2 suitability

Highly recommended as a helper stage.

---

## 9. Classical Boundary Difference Metrics

### Method

Measure:

|pixel_left - pixel_right|

along known block boundaries.

### VHS MPEG-2 suitability

Only fair.

Highly susceptible to VHS noise.

---

## 10. Uniform Low-Pass Deblocking

### Method

Apply roughly equal smoothing to detected block boundaries.

### VHS MPEG-2 suitability

Poor.

Often destroys real detail while leaving difficult artifacts behind.

---

# Final Ranking

| Rank | Method Family | Rating for VHS MPEG-2 |
|------|------|------|
| 1 | H.264 Adaptive Deblocking | Excellent |
| 2 | QED | Excellent |
| 3 | Edge-Classified Adaptive Filters | Excellent |
| 4 | Wang-Bovik Detection | Excellent Detector |
| 5 | Liu-Bovik DCT Methods | Excellent Detector |
| 6 | VapourSynth Deblock | Very Good |
| 7 | DFTTest-Assisted Deblocking | Very Good |
| 8 | BM3D-Assisted Detection | Very Good |
| 9 | Boundary Difference Metrics | Fair |
| 10 | Uniform Deblocking | Poor |

---

# Recommended VapourSynth Strategy

For VHS-C captured to MPEG-2 DVD recorder media:

1. Preserve interlacing initially.
2. Apply light temporal/chroma denoising.
3. Apply adaptive deblocking.
4. Apply deringing.
5. Deinterlace (QTGMC).
6. Restore texture/grain.

Example flow:

```text
Source
 -> Light temporal denoise
 -> Adaptive deblock
 -> HQDeringmod
 -> QTGMC
 -> Light BM3D
 -> Adaptive grain
```

The most common restoration mistake is attempting strong deblocking before reducing VHS noise.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Narrowing to only the top 3 for Block-Edge Detection and the top 3 for Blockiness Measurement is, in my opinion, exactly the right scope for someone who intends to later prototype and benchmark detectors.

I would actually treat the two categories separately because they optimise different objectives.

Research Note
Candidate Algorithms for MPEG-2 Block Detection and Blockiness Measurement in Noisy VHS-Derived MPEG-2 Video
Scope

This note considers a difficult restoration scenario:

VHS-C
    ->
Consumer DVD Recorder
    ->
LP Mode MPEG-2
    ->
Ripped MPG File


The objective is not deblocking.

The objective is identifying algorithms suitable for answering:

Is this edge a genuine scene edge
or an MPEG compression artifact?


and

How severe is the blocking?

Part I
Top Three Block-Edge Detection Approaches
Rank #1
Liu–Bovik DCT Visibility Model
Primary References

Shizhong Liu & Alan C. Bovik

DCT-Domain Blind Measurement of Blocking Artifacts
Blind Measurement and Reduction of Blocking Artifacts

References:

DCT-Domain Blind Measurement of Blocking Artifacts
Research Overview
Core Idea

Most edge detectors ask:

Is there a discontinuity?


Liu-Bovik instead asks:

Does the discontinuity behave
like a DCT quantisation step?


This is a much more useful question.

The detector attempts to model the edge itself rather than merely measuring its magnitude.

Why It Matters For VHS

VHS noise creates many discontinuities.

Simple gradient detectors cannot distinguish:

noise


from

compression


Liu-Bovik explicitly models compression artefacts.

Strengths
DCT-aware
Compression-aware
Visibility-aware
Less dependent on edge magnitude
Weaknesses
More complex than classical methods
Not specifically designed for VHS
My Assessment
Scientific Merit:     10/10
Compression Awareness:10/10
VHS Relevance:         9/10


Overall Rank:

#1

Rank #2
H.264 Boundary-Strength Classification
Primary Reference

Peter List et al.

Adaptive Deblocking Filter

Reference:

Adaptive Deblocking Filter
Core Idea

Often misunderstood as merely a filter.

In reality the most valuable component is the classifier.

The algorithm evaluates:

local gradients
neighbouring activity
coding context
boundary characteristics

before deciding what sort of edge exists.

Why It Matters

The key innovation is:

Not all edges are equal


The system effectively estimates:

Probability(edge = coding artifact)


which is exactly the restoration problem.

VHS Relevance

Extremely high.

Particularly because noisy VHS-derived MPEG-2 often contains edges that should not be treated equally.

Strengths
Practical
Proven
Classification-focused
Weaknesses
Built for H.264
Requires adaptation to MPEG-2 scenarios
My Assessment
Scientific Merit:      9/10
Compression Awareness: 9/10
VHS Relevance:         8.5/10


Overall Rank:

#2

Rank #3
Multi-Scale Edge Continuity Analysis
Representative Sources

This is more a family of methods than a single paper.

Derived from scale-space and edge-continuity literature.

Core Idea

Real edges continue.

Blocking often does not.

Evaluate edge persistence across:

8 pixels
16 pixels
32 pixels
64 pixels


Real structure survives.

Many block artefacts collapse.

Why It Matters

This addresses something the DCT literature often ignores.

Compression artefacts generally lack semantic continuity.

Objects possess continuity.

VHS Relevance

Very high.

Particularly for:

faces
buildings
text
clothing
Strengths
Works independently of codec
VHS-friendly
Robust against random noise
Weaknesses
Not inherently DCT-aware
May miss very large artefacts
My Assessment
Scientific Merit:      8/10
Compression Awareness: 7/10
VHS Relevance:         9/10


Overall Rank:

#3

Part II
Top Three Blockiness Measurement Approaches
Rank #1
Wang–Bovik Block Signal Model
Primary Reference

Zhou Wang Alan C. Bovik Brian L. Evans

Reference:

Blind Measurement of Blocking Artifacts
PDF
Core Idea

Model:

Observed Image
=
Natural Scene
+
Block Signal


Estimate the strength of the block signal.

Why It Wins

Most methods measure:

edge strength


Wang-Bovik measures:

blockiness strength


Those are not the same thing.

VHS Relevance

Excellent.

Provides a conceptual framework that remains useful today.

Strengths
Elegant
Blind metric
Directly measures blockiness
Weaknesses
Less DCT-specific than Liu-Bovik
My Assessment
Scientific Merit:      10/10
Measurement Quality:   10/10
VHS Relevance:          9/10


Overall Rank:

#1

Rank #2
Liu–Bovik Visibility Metric
Primary References

Same Liu/Bovik family of work.

References:

DCT-Domain Blind Measurement
Research Summary
Core Idea

Blocking should only matter if it is visible.

The algorithm estimates:

visibility of blocking


not merely:

existence of blocking

Why It Matters

An edge may technically be a compression artefact while being perceptually irrelevant.

This metric attempts to model human perception.

VHS Relevance

Very high.

VHS already contains considerable natural texture and noise.

Visibility matters more than absolute measurements.

My Assessment
Scientific Merit:       10/10
Perceptual Relevance:   10/10
VHS Relevance:           9/10


Overall Rank:

#2

Rank #3
HVS-Aware Blockiness Metrics
Representative Family

Human Visual System based quality metrics derived from:

Wang
Bovik
perceptual coding research
visibility masking work
Core Idea

Human beings do not notice all blocking equally.

Visibility depends on:

luminance
local texture
contrast masking
edge masking
Why It Matters

Two mathematically identical artefacts may have dramatically different visual impact.

VHS Relevance

Especially important.

VHS often contains heavy texture and noise where certain artefacts disappear perceptually.

My Assessment
Scientific Merit:       8/10
Perceptual Utility:     9/10
VHS Relevance:          9/10


Overall Rank:

#3

Final Recommended Shortlist For Experimentation

If I personally had only a few months available and wanted to build test detectors for VHS-derived MPEG-2, I would focus entirely on:

Detection
Liu–Bovik DCT Visibility
H.264 Boundary Strength Classification
Multi-Scale Edge Continuity
Blockiness Measurement
Wang–Bovik Block Signal Estimation
Liu–Bovik Visibility Estimation
HVS-Based Blockiness Metrics

Everything else I'd treat as baseline controls rather than serious contenders.

Most importantly, I'd regard Liu–Bovik and Wang–Bovik as the foundational papers because they are among the few approaches that attempt to answer the correct question:

"Is this structure likely to have originated from block-based quantisation?" rather than merely asking whether an edge exists.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Absolutely. In fact, once we narrow the scope to block-edge detection and blockiness measurement, the resulting paper becomes much stronger because we don't get distracted by filter implementation details.

I would structure it as a genuine research monograph around a single question:

Central Research Question

Given a noisy interlaced VHS-derived MPEG-2 stream, how can we determine whether a visible edge is:

a true scene edge,
an analogue-VHS artifact,
or a compression-generated DCT blocking artifact?

Everything else becomes secondary.

A Different Ranking Framework

Most papers rank methods according to:

PSNR improvement


or

How well a deblocker removes artifacts


I think those are poor metrics for your use case.

For VHS-derived MPEG-2 I would instead rank by:

Block Identification Accuracy


specifically:

P(correctly identifying MPEG blocking)


and

P(not destroying legitimate image structure)


which is a fundamentally different objective.

The Research Problem Nobody Really Solved

A surprising conclusion from reading decades of deblocking literature is this:

Most authors spent far more effort designing filters than designing detectors.

The implicit assumption was often:

If boundary difference > threshold
then blocking exists.


For VHS this assumption fails catastrophically.

Why?

Because VHS noise produces:

random discontinuities
chroma discontinuities
luma discontinuities
field-based discontinuities

that look remarkably similar to MPEG artifacts.

Thus:

Edge ≠ Blocking


This distinction is the entire paper.

My Preliminary Research Ranking
Category A
Best Theoretical Blockiness Models
#1 Liu–Bovik DCT Step-Visibility Model

Strength:

The algorithm asks:

Does this edge behave like
a DCT quantisation step?


rather than:

Is there a discontinuity?


Major breakthrough.

For VHS-derived MPEG-2 this remains, in my opinion, the most important research direction ever published.

#2 Wang–Bovik Block Signal Model

Strength:

Explicitly models:

Natural Image
+
Blocking Layer


and attempts to estimate the blocking layer.

Conceptually elegant.

Still one of the closest models to what we actually want.

#3 H.264 Boundary Strength Theory

Often misunderstood.

Most people think it is merely:

a deblocking filter


It is actually:

an edge classifier
with a filter attached.


The classification system itself is extremely valuable.

Category B
Best Real-Edge Rejection Methods

This category interests me even more.

Because detecting blocking is actually easier than rejecting image structure.

#1 Multi-Scale Edge Continuity

Key observation:

Real objects continue.

Blocking usually does not.

Imagine:

8 pixels
16 pixels
32 pixels
64 pixels


Real contours tend to survive.

Block artifacts tend to collapse under scale expansion.

#2 Orientation Consistency

Real edges exhibit directional coherence.

DCT boundaries typically exhibit:

0°
90°


dominance.

#3 Cross-Block Correlation

A real edge often exists:

before the boundary
across the boundary
after the boundary

Blocking frequently exists only at the boundary itself.

Category C
VHS-Specific Tests

This is where I think entirely new research is needed.

Inter-Field Consistency

For interlaced MPEG-2:

Real scene edges should often appear in:

Field A
Field B


with predictable motion behaviour.

Blocking may be stronger in only one field.

This is largely ignored in existing literature.

Noise Coherence Test

VHS noise is:

stochastic


while blocking is:

periodic


A strong detector should exploit this.

Grid Periodicity Test

An underappreciated clue.

Blocking tends to produce:

8×8 repetition


or

16×16 repetition


throughout the frame.

A true object edge usually does not repeat at exact DCT intervals.

The Most Important Research Insight

After years of video restoration discussions, I think the industry has largely been solving the wrong optimisation problem.

Most work optimises:

How strongly should I smooth?


The harder and more important problem is:

What exactly am I smoothing?


Because once classification is correct, the filtering itself becomes almost trivial.

The Ranking I Expect To Survive Future Research

If we imagine a perfect benchmarking set consisting entirely of:

VHS-C
Video8
Hi8
DVDR recorder MPEG-2 encodes
interlaced material
noisy sources

I suspect the long-term ordering will remain:

Rank	Methodology	Confidence1	Liu–Bovik DCT Visibility Analysis	Very High
2	Wang–Bovik Block Signal Model	Very High
3	H.264 Boundary Strength Analysis	High
4	Multi-Scale Edge Continuity Models	High
5	Grid Periodicity Analysis	Moderate
6	Orientation Consistency Analysis	Moderate
7	Canny-Based Detection	Moderate
8	Sobel-Based Detection	Low
9	Boundary Difference Metrics	Very Low
My Strongest Conclusion

If I were reviewing the literature specifically for:

VHS-C → LG DVD recorder LP mode → MPEG-2 → restoration

then I would conclude that the most promising path is not a better deblocker but a hybrid detector combining:

Liu-Bovik DCT-step visibility
Wang-Bovik block-signal estimation
H.264-style boundary classification
multi-scale edge continuity
field-to-field consistency

because each addresses a different failure mode, and together they directly target the actual question:

Is this edge present because of the photographed scene, because of VHS noise, or because MPEG-2 quantisation created it?

That question, rather than deblocking strength itself, is where nearly all restoration quality is won or lost for VHS-derived MPEG-2.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#############################################
`````

---

## Appendix B — Original Grok answer as provided by the owner

**Prompt provenance:** The owner wrote that, after reading Copilot, they asked Grok **"a similar thing"**. The precise words of the prompt to Grok are **not present** in the supplied text and therefore cannot be copied verbatim. Grok's response describes its understood question in its own opening paragraphs. The following is the exact Grok-labelled portion of the supplied paste.

`````text
Grok Answers in 1 part:
#############################################
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
**Yes. Here is a self-contained, original research-oriented Markdown document.** It is the result of my independent review of the literature on no-reference block-edge detection and blockiness measurement. I prioritized methods that directly address (or can be adapted to) the exact question you posed: *“Is this edge a DCT quantization artifact, or is it a genuine scene edge / VHS noise / analog detail?”* plus quantitative strength estimation.

The ranking is my own, based on suitability for **noisy, interlaced consumer MPEG-2** produced by VHS-C → LG-style VHS-to-DVD recorder in LP mode (high compression, variable quantization, field/frame DCT mixing, heavy analog noise, dropouts, and chroma issues). I deliberately avoided heavy emphasis on the downstream filters themselves and minimized repetition of the same papers.

Copy the entire content below into a file named `vhs-mpeg2-block-detection-measurement.md` (or download it if your interface supports it).

---

```markdown
# Block-Edge Detection and Blockiness Measurement for Noisy Interlaced MPEG-2 from VHS-C Captures

**Research Note**  
**Author:** Grok (independent literature synthesis)  
**Date:** October 2026  
**Target Scenario:** VHS-C → consumer LG-style VHS-to-DVD recorder (LP mode) → interlaced MPEG-2 → ripped .mpg files.  
**Central Question:** Given a visible edge in noisy interlaced MPEG-2, is it a genuine scene edge, analog VHS detail/noise, or a DCT blocking artifact? How severe is the blockiness?

## Scope and Challenges

Consumer MPEG-2 encoders in LP mode on VHS-to-DVD devices are aggressive and inconsistent. They frequently mix field and frame DCT modes, apply non-uniform quantization, and produce blocking that interacts badly with VHS analog noise (luma/chroma fluctuations, dropouts, head-switching noise). Simple spatial gradient or difference metrics fail because VHS noise creates many discontinuities that mimic block edges.

Effective methods must therefore be:
- DCT-aware (model quantization steps rather than raw edges)
- Robust to additive stochastic noise
- Capable of distinguishing periodic grid-aligned artifacts from semantically continuous real edges
- Preferably field-aware or able to handle interlaced content without destroying motion detail
- Useful for both binary classification (“artifact or real?”) and continuous strength estimation

This note separates **block-edge detection/classification** from **blockiness strength/visibility measurement**. Rankings are ordered by estimated utility for the specific VHS-derived interlaced MPEG-2 case.

## Part 1: Block-Edge Detection – “Is this a DCT artifact or a real edge?”

These methods attempt to classify candidate edges rather than merely locate them.

### Ranked Approaches

**1. Liu–Bovik DCT-Domain Blind Measurement of Blocking Artifacts (2001)**  
**Authors:** Shizhong Liu, Alan C. Bovik  
**Core Papers:**  
- “DCT-Domain Blind Measurement of Blocking Artifacts in Images” (ICASSP 2001)  
- Related follow-on work on visibility and reduction (2002)  
**Links:** https://live.ece.utexas.edu/publications/2001/sl_icassp_2001_dctblk.pdf (and IEEE Xplore)  

**Why #1 for this use case:** Instead of asking “is there a discontinuity?”, it models whether the edge behaves like a quantized DCT coefficient step function across an 8×8 boundary. This is highly discriminative against random VHS noise. It operates in the DCT domain (natural for MPEG-2) and incorporates visibility weighting. Strongest theoretical foundation for distinguishing compression artifacts from scene content in noisy sources.  
**Limitations:** Computational cost; requires adaptation for interlaced field/frame DCT switching.  
**Relevance Score:** 9.5/10

**2. H.264-Style Boundary Strength (Bs) Classification (List et al., 2003)**  
**Authors:** Peter List, Anthony Joch, Jani Lainema, Gisle Bjøntegaard, Marta Karczewicz  
**Paper:** “Adaptive Deblocking Filter” (IEEE Transactions on Circuits and Systems for Video Technology, 2003)  
**Links:** https://ieeexplore.ieee.org/document/1218194 (and the widely cited PDF: https://mcube.lab.nycu.edu.tw/wiki/core/uploads/Research/SelectedTopics/Adaptive%20Deblocking%20filter.pdf)  

**Key Insight:** The boundary strength classifier (which evaluates local activity, gradient across boundary, quantization parameter, and coding mode) is more valuable than the subsequent filtering. It estimates the *probability* that an edge is a coding artifact. Although designed for H.264, the feature set transfers well to MPEG-2 and can be made field-aware. Excellent at rejecting strong real edges.  
**Relevance Score:** 8.5/10 (very practical; needs MPEG-2-specific tuning for interlaced modes)

**3. Grid Periodicity + Cross-Boundary Correlation Analysis**  
**Attribution:** Common technique in blind blocking detection literature; builds on foundations from Bovik group, Marziliano et al., and restoration community practices (e.g., autocorrelation or FFT along candidate 8/16-pixel lines; see also Wu & Yuen, Triantafyllidis et al. papers on blocking artifact detection).  

**Core Idea:** Real scene edges and VHS details rarely exhibit strict periodicity at the DCT grid (every 8 or 16 pixels horizontally/vertically) and usually maintain correlation and continuity on both sides of a putative boundary. Blocking artifacts are highly periodic and often decorrelated inside vs. across blocks. Multi-scale checking (8 px → 32 px) further separates stochastic VHS noise from structured blocking.  
**VHS-Interlaced Advantage:** Can be run per-field; very robust to random analog noise.  
**Relevance Score:** 8/10 (strong complementary method)

**4. Multi-Scale Edge Continuity and Orientation Consistency**  
**Attribution:** Scale-space and contour analysis literature (Lindeberg, Witkin) applied to artifact detection; seen in various deblocking and quality assessment papers that reject non-continuous or grid-dominant edges.  

**Core Idea:** Genuine edges persist and maintain orientation coherence across multiple scales and neighboring blocks. DCT blocking tends to collapse or show strong 0°/90° bias at exact block boundaries. VHS noise is incoherent.  
**Strength for this scenario:** Excellent at preserving faces, text, clothing, and architectural lines common in home video while rejecting isolated block edges.  
**Relevance Score:** 7.5/10

**5. Noise-Robust Variance Ratio + Local Activity Classification**  
**Attribution:** Extensions of edge-classified adaptive methods (e.g., Kim, Yi, Kim, Ra – “A Deblocking Filter With Two Separate Modes…” and similar region classification approaches). Often combined with local variance or flat/edge/texture region detection.  

**Core Idea:** Compare activity *inside* a block versus *across* the boundary, while accounting for local noise floor. Flat areas are more sensitive to blocking; textured/VHS-noisy areas mask it.  
**Limitation:** Simpler versions are easily fooled by heavy VHS noise; needs the above methods as preprocessors.  
**Relevance Score:** 6.5/10

## Part 2: Blockiness Measurement – “How severe is the blocking?”

These produce a scalar or map estimating artifact strength or perceptual visibility (no original reference available).

### Ranked Approaches

**1. Wang–Bovik Blind Block Signal Model (2000)**  
**Authors:** Zhou Wang, Alan C. Bovik, Brian L. Evans  
**Paper:** “Blind Measurement of Blocking Artifacts in Images” (ICIP 2000)  
**Links:** https://ece.uwaterloo.ca/~z70wang/publications/icip00.pdf  

**Why #1:** Elegant model: observed image = natural image + periodic “block signal.” Estimates power of the block signal without reference. Directly measures *blockiness strength* rather than edge magnitude. Remains one of the most cited no-reference metrics and provides a clean conceptual framework that works even when strong analog noise is present.  
**Relevance Score:** 9.5/10

**2. Liu–Bovik Visibility-Weighted DCT Blocking Metric (2001 family)**  
**Attribution:** Same Liu & Bovik work as above, with explicit human visual system (HVS) visibility estimation.  

**Core Idea:** Not all blocking is equally important. Weights artifacts by local luminance, contrast masking, texture, and frequency content. An edge may be a clear DCT step but perceptually invisible in busy VHS texture.  
**Advantage for VHS:** Critical, because VHS grain and noise provide natural masking. Prevents over-filtering of perceptually irrelevant blocking.  
**Relevance Score:** 9/10

**3. Fourier-Domain Grid Energy / Periodicity Strength**  
**Attribution:** Widely used in quality assessment (extensions of Wang-Bovik, work by Wu, Yuen, and others on frequency-domain blocking detection). Compute power spectrum or autocorrelation emphasizing 8/16-pixel frequencies along horizontal and vertical lines.  

**Strength:** Highly robust indicator of periodic blocking even in noisy data. Can produce per-frame or per-region strength maps. Works well on interlaced content when applied per-field.  
**Relevance Score:** 8/10

**4. HVS-Aware Perceptual Blocking Metrics (Bovik group extensions & related perceptual QA)**  
**Attribution:** Builds on Wang/Bovik SSIM philosophy and contrast sensitivity function (CSF) / masking models (e.g., papers on “perceptual quality metrics for blocking artifacts” by various authors in the early 2000s, including Daly, Watson, and later Bovik lab work).  

**Core Idea:** Incorporates luminance masking, contrast masking, and viewing conditions to produce a perceptually weighted blockiness score.  
**Particularly useful for VHS:** VHS material has high natural texture; many blocking artifacts are masked. Pure mathematical strength can be misleading.  
**Relevance Score:** 7.5/10

**5. Practical Heuristic Local Blockiness Estimation (Didée QED-style analysis)**  
**Attribution:** Didée (AviSynth community), “Deblock_QED” (2000s). Not a formal paper but a well-documented heuristic that estimates both boundary and internal block artifacts while attempting to distinguish real structure.  
**Link:** http://avisynth.nl/index.php/Deblock_QED  

**Value:** Developed specifically for noisy consumer video. Analyzes activity inside blocks vs. boundaries and adapts strength. Serves as a strong practical baseline that many VapourSynth users adapt.  
**Relevance Score:** 7/10 (pragmatic rather than purely theoretical)

## Recommended Shortlist for Prototyping / Benchmarking

**Detection priority (classification “artifact or real?”):**  
1. Liu–Bovik DCT step modeling  
2. H.264-style boundary strength features (adapted to MPEG-2)  
3. Grid periodicity + multi-scale continuity (combine 3 & 4 above)

**Measurement priority (strength/visibility):**  
1. Wang–Bovik block signal model  
2. Liu–Bovik visibility weighting  
3. Fourier periodicity energy

**Strongest hybrid insight:** A detector that combines Liu–Bovik DCT awareness, Wang–Bovik signal modeling, grid periodicity, and field-to-field consistency (real edges tend to be coherent across interlaced fields with plausible motion; blocking often is not) is likely to outperform any single method on VHS-derived interlaced MPEG-2. Most classical literature under-emphasizes interlaced-specific and noise-coherence tests; this remains an open opportunity for targeted improvement.

**Key Research Takeaway**  
The literature has historically focused more on *filtering* than on *detection and classification*. For difficult material like noisy VHS-C LP MPEG-2, detection/classification quality dominates final restoration success. Once you reliably answer “Is this edge a DCT artifact?”, the filtering decision becomes far simpler and less destructive.

## References (Core Attribution List)

- Wang, Z., Bovik, A.C., Evans, B.L. (2000). Blind Measurement of Blocking Artifacts in Images. ICIP.  
- Liu, S., Bovik, A.C. (2001). DCT-Domain Blind Measurement of Blocking Artifacts. ICASSP.  
- List, P. et al. (2003). Adaptive Deblocking Filter. IEEE TCSVT.  
- Didée (AviSynth community). Deblock_QED algorithm documentation.  
- Related works in perceptual image/video quality assessment (Bovik lab, VQEG-related blocking metrics).

Further reading should include IEEE Xplore searches for “blind blocking artifact detection MPEG-2 interlaced” and “no-reference blockiness metric” post-2005 extensions that incorporate better noise modeling.

---

This document is self-contained, focused, and distinct from the Copilot output while acknowledging the same foundational papers where they are clearly dominant. It avoids hallucinated citations and concentrates on what you said mattered most: the two specific questions of edge classification and blockiness measurement in your exact capture pipeline.

If you need expansions on any method, additional references, a VapourSynth implementation sketch (with comments), or a benchmark design for testing these detectors on real VHS-LP samples, let me know.
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#############################################
`````
