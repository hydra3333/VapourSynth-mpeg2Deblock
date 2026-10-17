# Claude Independent Review Request - S2-I2 Design Plan v0.3

**Date:** 2026-10-15  
**Status:** REVIEW CANDIDATE ONLY; no implementation, installation or owner Windows run requested.

## Deliverable and requested decision

Please independently review `ChatGPT_S2_I2_Design_Plan_v0_3_FOR_CLAUDE_REVIEW.md` against the ratified Stage 2 v0.6 authority, geometry/decisions/NOTICE and pristine accepted S2-I1 code. Owner approval follows your reviewed outcome; only then will ChatGPT code and package the tools for your execute/rehearse-before-owner duty.

This is a revision of ChatGPT v0.2, *not* a new implementation family. It incorporates your `Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_2_v0_1.md` M1, S1-S4 and optional comments, plus the project owner's single clean paste of additions. The attached `Claude_S2_Seam_Pixel_Test_Options_Table_v0_2.md` is copied **byte-identically**, as a non-authoritative future-options inventory.

## Review priorities (concrete)

1. **M1 (MUST):** row phase `F(y)=|Y[y+2]-Y[y]|`, expected phases 6 and 7 highest, margin >=10%, parity-safe synthetic +1/+2 shift tests.
2. **S1 (SHOULD):** raw 3x3 C peak at zero, >=10% difference to each competitor, >=2/3 support across applicable frames; both phase tests >=10% margins; explicit FAIL versus INCONCLUSIVE. Flag the documented prior exposure to informal values.
3. **S2 (SHOULD):** `D_norm = D_raw - mean(in-block same-field 2|4,3|5,10|12,11|13)`; raw D gates, normalised D only reported.
4. **S3 (SHOULD):** seven known-bad pixel offsets (+4/8/16 columns, +1/2/8/16 rows) with >=1 non-PASS test each; LP_blocky expected SHA-256 `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238`, 204 records, I/P/B 19/50/135, FRAME/FIELD/NONE 54292/33853/242335, all QP62, no leading B, no baseline promotion.
5. **S4 (SHOULD):** preflight NumPy in the *actual* VapourSynth Python; explicit interpreter, versions and abort before data runs.
6. **Owner descriptive addition:** separate LP/LP_blocky **both-orientation** index seam/control pixel strength, plain M2 and robust M4, fixed 5% proxy false-alarm percentile, tie-aware AUC, seam classes, QP and I/P/B, NONE x8 separately, frame/GOP uncertainty. Is the horizontal sampling and denominator/calibration policy unambiguous, implementable and free of proxy-as-truth confusion?
7. **Scope and samples:** no filtering, no tuning, no new ratified authority, no held-out clips in S2-I2; additional MLS/2A_blocky/4A_blocky conditional on a later owner confirmation, all-16 census at S2-I8 after freeze.
8. **Future options:** M1-M5, F1-F3, R1-R4, B0/B1, T1/T2, P0-P2, K1-K4, G1/G2, D0/D1 retained for separately authorised S2-I3/S2-I5. No option discarded without written rationale; B1 uses additional metadata beyond D-13 and requires later owner ruling.
9. **Runner feasibility:** six proposed components plus an optional narrow reporting helper; regular-file inspector, safe CMD redirection/ERRORLEVEL, scratch media lifecycle, deterministic tests, source/index identities and full report schemas.

Please classify findings MUST/SHOULD/OPTIONAL, offer exact replacement language where necessary and state whether the design is suitable for owner ratification and subsequent bounded S2-I2 implementation. No code, executable scripts, media or indexes are supplied here.
