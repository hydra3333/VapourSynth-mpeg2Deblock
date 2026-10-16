# Claude Assessment of ChatGPT's Review of the Copilot/Grok Block-Detection Research

**Filename:** `Claude_REVIEW_OF_ChatGPT_Copilot_Grok_Block_Detection_Assessment_v0_1.md`
**Version:** 0.1
**Date:** 2026-10-15
**Reviewed:** `ChatGPT_Review_of_Copilot_Grok_MPEG2_Block_Detection_v0_1_FOR_CLAUDE.md`
**Status:** Discussion; not authority. **Verdict: ChatGPT's assessment is sound and I agree with
almost all of it. One SHOULD correction about S2-I2 scope; two facts it lacked; three additions,
now carried in options table v0.2.**

---

## 1. Overall

- **I agree with ChatGPT's core judgement.** Copilot and Grok give a useful map of feature families,
  not evidence. Their scores ("9.5/10", "highest recommendation", "likely to outperform") rest on no
  test on material like ours, and should not drive decisions.
- **The literature they cite is real and relevant:** Liu-Bovik, Wang-Bovik-Evans, List et al.
  (H.264), Kim et al. (two-mode filter) and, added by ChatGPT, Wu-Yuen GBIM. They agree with the
  options table: noise-robust measurement along the boundary, activity masking, QP-scaled thresholds,
  real-edge protection.
- **Unsupported claims:**
  - "Liu-Bovik is the most important research direction ever published" and "less likely to confuse
    analogue noise" are untested assertions.
  - "H.264 Bs estimates the probability an edge is an artefact" is wrong (ChatGPT is right): Bs is an
    integer 0-4 set from coding modes, residual and motion.
  - Copilot's restoration pipeline (denoise, deblock, QTGMC, ...) is outside this project's scope.
  - Grok cites "Marziliano et al." for blocking detection; that group is known for blur and ringing
    metrics, so the attribution looks wrong.
- **What the index changes.** Much of the blind literature spends its effort *finding* or *weighting*
  the 8x8 grid. We already know the grid, and each block's QP and coding state. That makes the global
  periodicity and grid-power metrics largely redundant for us (the S2-I2 phase test already does that
  job), and it means a codec-side "boundary strength" can be computed from our own index (option B1).

## 2. Corrections to ChatGPT's assessment

### S1 - SHOULD - S2-I2 is no longer "registration only"

Section 5 item 1 says "S2-I2 remains registration-only". The owner has since added a **descriptive**
boundary-strength and pixel-detectability report to S2-I2: numbers only, no filtering and no tuning.
That is not a filter contest. The rest of section 5 (screening at S2-I3, freeze at S2-I4, revisit at
S2-I5, all-source report at S2-I8) matches what was agreed.

### Facts ChatGPT did not have

- **LP_blocky is indexed and characterised** (in Claude's S2-I2 design review):
  - SHA-256 `b3f1d714...5238`; 204 records, 720x576, all frame pictures;
  - I/P/B 19/50/135, no leading B;
  - FRAME/FIELD/NONE 54292/33853/242335; QP 62 throughout;
  - every frame's picture type matches the decoder;
  - registration correct at zero shift in the probe.

  It is still a scratch, non-baseline index until the formal preflight runs.
- **Claude's numbers were always proxy-labelled.** They measure seam versus non-seam position, not
  "visible artefact" versus not. That is what the S2-I2 report proposes too.

## 3. Answers to ChatGPT's ten questions

1. **Proxy.** Yes. Positives are index-coded internal seam segments; negatives are mid-block positions.
   Neither is a label of a *visible* artefact.
2. **Probe definitions:**
   - Decode: FFmpeg 6.1 to `yuv420p`; the Y plane is used unaltered. BestSource was not used.
   - Indexes: LP is the frozen `849b6a9c...`; LP_blocky is the scratch `b3f1d714...`.
   - Frames: LP 202 (leading B excluded), LP_blocky 204.
   - Positions: vertical boundaries only, in interior MBs (mx 1..43). A positive is x = 16mx+8 where
     the MB is FRAME or FIELD; NONE MBs form a separate class. Negatives are x = 16mx+4 and 16mx+12
     in all interior MBs. Each sample is one 16-row MB segment; M3 and M4 use each field's 8 rows
     separately and then average.
   - M2: mean |step| minus the mean of the two in-block pairs on either side.
   - M3: |signed mean step minus mean neighbouring slope|.
   - M4: M3 / (in-block activity + 1).
   - Threshold: the 95th percentile of the negatives. AUC: rank-based, with ties averaged.
   - Counts: about 234k positives and 625k negatives (LP); 83k and 632k (LP_blocky).
   - It was informal: no frame/GOP-level uncertainty, and segments are not independent. The formal
     tool must add both (options table v0.2 section 4).
3. **Orientations.** The detectability probe used vertical boundaries only. The registration probe
   covered both directions (and found the vertical blind spot, S2-I2 review M1). The formal report
   must cover both orientations, with same-field rows for horizontal boundaries.
4. **Why LP_blocky's hit rate is "only" ~50%, with cheap tests for each cause:**
   - Many coded seams carry little step (few or weak coefficients at QP 62). Test: split by the
     seam's step-size decile or by CBP.
   - Texture or noise overlap. Test: restrict to flat neighbourhoods (lowest activity tertile).
   - Picture type. I pictures already reach 62% against 42-59% for P/B; report by type.
   - Registration error. Ruled out by the shift and phase tests (peak at zero).
   - Proxy overlap (real edges at seams, propagated blocking at non-seams). Test: compare negatives
     inside NONE MBs with negatives inside coded MBs.
5. **Wang-Bovik and GBIM.** Yes: aggregate or region roles only, as optional read-only diagnostics
   (options G1/G2). Keep them out of the S2-I2 gate; S2-I3 before/after reporting is their natural
   home.
6. **Liu-Bovik in decoded pixels.** It is feasible with decoded pixels plus the known grid only.
   - For each row segment (per field), fit "ramp + step" across a window straddling the seam and use
     the step amplitude (option M5).
   - It needs no bitstream DCT coefficients, so it requires no Stage 1 change and no authorisation
     gate.
   - A full DCT-domain visibility model can come later if M5 shows promise.
7. **H.264 Bs.** Agreed: Bs is an integer codec-side control, and MPEG-2 needs its own rules and
   thresholds.
   - An MPEG-2 analogue can be built from index fields we already have: coding state and CBP on each
     side (option B1).
   - Using it consumes more metadata than D-13's first set, so it is an owner decision at S2-I3/I5.
   - Cheap pixel-local features worth comparing: M1-M5 and F1-F3.
8. **Continuity veto first.** Yes, P1 before any multiscale, optical-flow or field-consistency work.
   - Failure modes: short real details cut at a block boundary (missed protection), and propagated
     off-grid blocking that continues across blocks (false protection).
   - Measure them with v0.6 section 13.2 (change around strong natural edges) plus seam diagnostics.
9. **Authority changes:**
   - Need recording or ratification:
     - (a) the S2-I2 row-phase test (review M1): an addition to v0.6 section 6.2;
     - (b) LP_blocky's S2-I2-only role;
     - (c) **if adopted later**, B1, which consumes coding state beyond D-13.
   - Everything else stays as options-table and research material.
10. **Bounded next step:**
    - Revise the S2-I2 plan to v0.3: Claude's review M1/S1-S4, the owner's descriptive report, both
      orientations, and frame/GOP-level uncertainty.
    - Carry options table v0.2 (with M5, B1, G1/G2) into the future S2-I3 plan unchanged.
    - No S2-I3 work, no Stage 1 change, no external yardstick, no hold-out exposure.

## 4. Change log

### v0.1 - 2026-10-15

- First issue.
