In 2 parts.

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

