# Claude review request - Mpeg2Assessor and adaptive filter selection discussion v0.1

**Review status:** exploratory; no ratification or implementation authorization.
**Date:** 2026-10-18

The project owner expressly corrected ChatGPT's erroneous assumption that the Windows inspector pipeline writes a scratch `.m2v`: the accepted process pipes an MPEG-2 elementary stream from FFmpeg directly to `Mpeg2BlockInspector.exe -b -`. The supplied repository source ZIP confirms this in all seven `TESTING` BATs. The `.s1tmp` is a temporary INDEX, not a temporary ES. Preserve this fact.

Please cold-review the attached discussion paper, not as a preapproved plan but as competing research hypotheses. In particular: (a) pre-pipe MediaInfo 26.10 Python feasibility and frame-count uncertainty, (b) actual decoded-pixel availability with a one-way ES pipe, (c) representative sampling including unknown N and long-source duration, (d) whole-source vs contiguous temporal ranges vs coarse spatial regions vs native per-seam adaptation, (e) one parameterised filter vs 2-5 different strengths/algorithms, (f) broad automated option/interaction screening under four grouped folds, and (g) whether an assessor earns its implementation cost over a simpler no-assessor baseline.

Distinguish VERIFIED source facts from proposed design, identify source/line support, and return MUST/SHOULD/OPTIONAL/NO OBJECTION findings. Do NOT silently modify Stage 1, S2-I3 v0.3 or Stage 2 v0.7; do not draft code or open held-out sources. The owner requested both roles iterate toward a joint assessment of worthwhile/not worthwhile and doable/not doable before approving implementation. ChatGPT should receive a short paste-ready relay summary.

This paper deliberately encompasses alternatives and test questions rather than selecting implementation granularity or filter count. A negative assessor recommendation is entirely acceptable.
