# Claude Review Request - S2-I3 Full-Data Multi-Source Design v0.1

**Date:** 2026-10-17
**Status:** DESIGN REVIEW ONLY. No software implementation or experimental run authorised.

The project owner has instructed ChatGPT to prepare an S2-I3 design favouring full genuine recording data for primary optimisation. The owner also wants separate even/odd comparisons, supplementary split-trained sensitivity, LP-only / LP_blocky-only / joint tuning contrasts and evaluation on three other different-content blocky recordings, subject to same-dimensions preflight.

Please independently review the attached `S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_1_FOR_CLAUDE_REVIEW.md` against the ratified Stage 2 Experimental Design v0.6 at repository commit `6e7b5c53df1c65775524936fc945c449cc9fa100`, `05_DECISIONS_v1_2.md`, `06_DEBLOCK_CONCEPT.md`, S2-I2 gate evidence, NOTICE, and your pixel-test options table v0.2.

Particularly review: (1) precise conflict with v0.6 sections 8.4/19 and the proposed change to S2-I4 ablation validity; (2) no hidden reliance on artificial/hand-selected data; (3) LP_blocky content dependence; (4) the three extra recordings' unverified 720x576/index compatibility; (5) fixed-QP definitions and option disposition; (6) freeze timing before extra-source evaluation; (7) B0/B1 and protected hold-outs; (8) owner-authorisation boundary.

Please report MUST / SHOULD / OPTIONAL findings, and explicitly recommend what *authority revision and owner decisions* are necessary before any S2-I3 implementation. Do not provide code or instructions to modify/run the repo at this stage. The owner has authorised design preparation only.

No user-provided media or existing indexes are bundled in the review package. The S2-I2 Step B commit is COMPLETE and must not be reopened simply because this next design differs.
