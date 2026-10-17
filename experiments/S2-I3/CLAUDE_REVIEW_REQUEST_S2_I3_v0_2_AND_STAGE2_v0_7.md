# CLAUDE - Review request: S2-I3 full-data redesign v0.2 and Stage 2 v0.7

Date: 2026-10-17. Both documents are DRAFTS. Owner authorised design preparation ONLY.
Baseline: 6e7b5c53df1c65775524936fc945c449cc9fa100.

The owner has put technical refinement back with ChatGPT and Claude, without
wanting further rounds of broad methodological decisions. Please independently
review the proposed Stage2_Experiment_Design_v0_7 and S2-I3 v0.2 together,
not isolated from each other. v0.7 is a full versioned replacement drafted
from the exact available ratified v0.6 source, with a unified diff included.

Review priorities, as MUST/SHOULD/OPTIONAL with exact fixes:

1. Registration admission gate. Critically evaluate the provisional >=64 MB,
   >=10% per class and >=2/3-frame 3x3 applicability policy. The previously
   observed SP, SP_blocky, 3A and MLS_blocky outcomes MUST NOT dictate a
   retrospectively convenient cutoff. Determine an independent mechanistic
   alternative proof for weak row/3x3 sources BEFORE authorising any filtering.
   No silent weakening of S2-I2 results or accepted threshold numbers.
2. Four content groups / grouped CV correctness, training/evaluation leakage,
   old LP-only comparator not meaningful on the held-out LP fold, 2:1 within-
   group original weighting, full-eight joint K0 and comparator freeze logic.
3. S2-I4: frozen-parameter QP-only switch versus identically calibrated two-
   branch QP comparison; ensure no circular selection or accidentally moving
   S2-I4 execution into S2-I3.
4. Stage 2 authority consistency across sections 2, 3, 4, 5, 6, 8.4, 9.1,
   10, 13.3, 15, 19, 22 and 23. Detect any old LP-only or old even/odd
   requirement that remains actively operative after the proposed revision.
5. Index frame dimensions (especially 704x576 3A), correct native content-
   group pairing, leading-B exclusions, Q_fixed whole-index population, hard
   fail versus statistical INCONCLUSIVE. Six frozen indexes unchanged.
6. Protect EP/2A/4A *and their blocky encodes* until S2-I8; MLS pair controls;
   all-16-census stage after final freeze; NOTICE / Restricted Media compliance.
7. Options register coverage including proposed M4a versus ratified M4,
   B0 versus separately gated B1, G1/G2, and unbiased no-harm measurements.

Please give a concrete consolidated response suitable for ChatGPT revision.
NO Windows owner commands, repo staging, code writing, filtering, media export,
Git commit or assertion of new owner ratification are requested.
If v0.7 should not be ratified yet, distinguish repairable design issues from
implementation-preflight tests that must instead precede code quality runs.
