# S2-I3 P1 - Implementation Kickoff and First Bounded Slice

**Version:** 0.1; 2026-10-18; FOR CLAUDE INDEPENDENT REVIEW (not a repository authority)
**Prepared by:** ChatGPT, following the project owner's explicit instruction on 2026-10-18 to start P1
**Status:** P1 START AUTHORISED by owner; this IMPLEMENTATION PLAN is proposed, not ratified; no code installed or filtering run by this document.
**Last owner-confirmed repository HEAD:** `82ba3e104b1f8ff9f3dd6214df1bbb4ae7cfc927`. Check live HEAD before any installation; local Claude handover v0.14 has been copied into `docs/HANDOVER/` but a commit has not been reported.

## 1. Scope and controlling sources

The P0 registration/correspondence gate is owner-ratified PASSED (2026-10-18); its evidence report was installed at `e7cf449`, and `06_DEBLOCK_CONCEPT.md` v1.3 at `82ba3e1`. P1 is **the S2-I3 fixed-QP luma filtering and procedure-selection experiment**. The owner's latest message supplies the *separate explicit P1 authorisation* previously lacking. It does not authorise S2-I4, S2-I5, P1 coding-context variant B1, protected hold-out contact, Stage 1 changes or production C++ work.

Normative sources consulted byte-for-byte from the locally supplied repository archive:

- `docs/REPOSITORY/Stage2_Experiment_Design_v0_7.md`, working-copy CRLF SHA-256 `d754b94869a2c77ee148a41f1ca38e9998f3fdca698fd6090372a300a8bbb787`, notably sections 1, 3, 5, 6.3, 7-8, 11-15 and 19.
- `docs/REPOSITORY/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md`, working-copy CRLF SHA-256 `67893a9acde830079fa382c5f0c62d32fee7d5a13d3eae77930905aa1eaa81d8`, notably sections 2, 4-5, 7-8.
- The installed v1.3 concept, accepted P0 report and Claude handover v0.14 supplied in the Route A work. Authority documents prevail over this proposal.
- `Claude_S2_Seam_Pixel_Test_Options_Table_v0_2.md`: NON-authoritative candidate inventory; S2-I3 v0.3 explicitly carries its options forward but supersedes its obsolete LP-even/odd training scheme.

This proposal introduces **no new authority, algorithm winner, numerical quality gate or change in experimental population**. It proposes an implementation order and a first source-code slice that can be reviewed and objectively tested before quality optimisation.

## 2. Invariants for all of P1

1. **Eight sources, four content groups:** XP, SP, LP, TEST 3A; original + `_blocky` in each. Use all quality-eligible frames. Do not resize/crop 3A (704x576) to 720x576. Both encodes stay together whenever a content group is held out.
2. **Fixed per-source QP throughout S2-I3:** original XP=14, SP=16, LP=18, 3A=14; all `_blocky`=62. These are all-macroblock full-index medians, not computed from selected quality frames. Actual per-macroblock QP variation is **not** a filtering input or comparison until S2-I4.
3. **B0 ONLY:** geometry, residual transform state and selected fixed QP; no coding-type / CBP-based boundary strength B1 and no motion-vector additions. No pixel-derived *locations* of seams. A pixel test may decide whether an indexed candidate seam should be corrected.
4. **Frame-owned luma only.** For suitable coded frame pictures, FRAME/FIELD/NONE determines internal residual seam eligibility. Vertical internal x=8 on FRAME or FIELD; horizontal internal 7|8 on FRAME only; NONE no internal residual seams. Macroblock outer edges remain candidates subject to separately explicit eligibility/support policy. Field-polarity-aware vertical sample access where appropriate; never mix fields accidentally. No chroma, field-picture support or separate field passes.
5. **Local and bounded:** correction support for one seam must not cross another known seam; clip to sample range, clamp maximum correction, protect genuine edges, and retain the same input/output frame geometry and format. Multiple eligible seams must not produce order-dependent or double-applied corrections.
6. **OFF byte-exact.** When strength is OFF, frame output including every plane must be byte-identical to source. Do not claim a VapourSynth source-frame pointer is writable.
7. **Admission provenance:** consume the existing accepted eight-source index and P0 identity/correspondence evidence; verify source/index/decoder identity and counts for each new run. Do not rerun P0 destructively or regenerate the six immutable Stage 1 indexes. The seven development indexes are already tracked at `35923a5`.
8. **Restrictions:** leading B pictures before first I are validated but excluded from quality evidence; no EP/2A/4A or their blocky counterparts before S2-I8; MLS is a later control, not fitting material; 6A/7A currently have no assigned role. Restricted Media remains controlled by NOTICE.md. No user-identifying text in commit candidates.

## 3. Proposed short sequence within authorised P1

### P1A - Geometry, validation and OFF/identity foundation (FIRST IMPLEMENTATION SLICE)

Purpose: prove the experimental processing path's *mechanics* before any optimised deblocking or subjective scoring. New code is review-only until Claude checks it and owner accepts the bounded installation/run.

Suggested minimal files under `experiments/stage2/` (names are proposed; resolve existing namespace collisions before writing):

- `stage2_i3_p1_geometry_v0_1.py`: reusable read-only geometry/segment enumerator and explicit parity-aware sample-coordinate helpers, using `stage2_index_reader_v0_2.py`, not a second index parser. Output geometry descriptors only; no actual filtering and no consumption of per-MB QP as a strength input.
- `stage2_i3_p1_geometry_tests_v0_1.py`: deterministic synthetic tests for FRAME/FIELD/NONE, internal x=8, 7|8 versus absent horizontal seam, outer edges, 720/704 width, start/end-of-frame support, parity isolation, overlapping support, unsupported picture structures and fail-closed invalid metadata. Test exact OFF identity on synthetic YUV planes and full-frame hashes. Include a deliberately failing test to verify non-zero exit and place it *before* `unittest.main()`.
- `stage2_i3_p1_identity_clip_v0_1.vpy`: source allow-list + BestSource + matching index validation, reusable local helper import (`HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))`), and a lossless identity/OFF path. The identity path must be independently checked via pixel/plane hashes; a simple pass-through alone does not prove later filtering correctness.
- `S2_I3_P1A_validate_identity_v0_1.bat`: strict Windows orchestration for the tests and all-eight OFF validation; explicit interpreter provenance; per-source log and manifest; no held-out material or index regeneration; fail closed and do not overwrite accepted P0 evidence.

**Implementation decisions for Claude to review before code:** whether to expose geometry as per-seam iterators or immutable maps; how to represent field-parity-aware *horizontal* corrections and segment-wise *vertical* statistics; avoid cross-seam overlaps; how to retain untouched chroma and avoid introducing YUV conversion. Do not infer per-picture `progressive_frame` solely from file extension or nominal scan metadata.

**P1A completion evidence (engineering QA, not a new quality gate):** synthetic tests PASS, injected failures exit non-zero, 8/8 approved sources independently show exact OFF pixel identity and correct frame counts/format, fixed QP and index hashes match the P0/ratified design, no unexpected path staged or baseline altered. Record any unsupported format as a FAIL or explicit blocker, never silently coerce. P1A emits no claimed deblocking benefit and no K0 winner.

### P1B - Read-only candidate screening and declared search plan

Implement M1-M5 seam-step and F1-F3 side-activity diagnostics, in both orientations with correct field sampling, beginning with D0 (no decision-only denoiser). Carry R1-R4, T1/T2, P0-P2, K1-K4, G1/G2, D1 and B1 on the option ledger with an explicit disposition: B1 forbidden without new owner decision, K4 optional Family C, G1/G2 aggregate-only, D1 requires evidence, T2 starting point not a borrowed normative table.

**No leakage:** screen and shortlist within the three *training* groups of each leave-one-group-out fold. Once a fold's choice is fixed, compute untouched-group evaluation. Do not choose an overall procedure from held-out data and then present the selected procedure's cross-validated score as independent external performance.

Predeclare fixed false-alarm operating points and seam/off-seam control positions *before* reading candidate outputs; the distinction is an index-directed **proxy**, not proven perceptual artefact labels. Include per-orientation, seam class, FRAME/FIELD/NONE, I/P/B, QP/source and frame/GOP uncertainty. Report full candidate inventory and rejection reasons. Shortlist 2-3 practical M/F/R/T/P/K combinations for filtering inside each fold using the same algorithm-selection rule and effort for O/X/J.

### P1C - Bounded K0 filtering prototype and four-fold O/X/J comparison

Implement small-support edge-protected correction (beginning with K1 bounded `p0`/`q0`; K2 optional smaller `p1`/`q1` where safe) without assuming either wins. Use fixed QP and one common declared OFF/LOW/NOMINAL/HIGH strength convention. No cross-seam support; no field mixing; deterministic composition if pixels participate in two candidate corrections. Use source- and seam-separated measures: before/after seam response, changed-pixel fraction, off-support/no-harm changes, natural-edge changes, and paired-reference MAE/MSE/PSNR only for P0-confirmed frame-matched pairs.

Run four leave-one-CONTENT-group-out folds. For each fold, fit the same-budget comparison procedures separately: O=three originals; X=three blockys; J=all six encodes with equal content-group weight and within each group **2/3 original, 1/3 blocky**. Score on both untouched pair members; publish each held-out group and the balanced summary without counting frames/seams as independent samples. Historical L/LB optional; if used, compare **all** arms on the common XP/SP/3A folds only and mark LP-held-out N/A.

Use a *predeclared*, multi-criterion procedure-selection rubric: original no-harm and natural-edge preservation first, credible seam improvement, no catastrophic failure on any original, separate blocky stress/paired-reference movement, then blinded/shuffled owner visual assessment where practical. Do not force one scalar score or treat Q62 `_blocky` as a population prevalence sample.

### P1D - Final fit and freeze

After fold-level method selection: fit K0-J on **ALL EIGHT** eligible source populations; also fit and identify K0-O and K0-X comparators, cross-evaluate all three on all eight, and label this final-fit evidence IN-SAMPLE. Record exact algorithm version and code/hash, source/index hashes, Q_fixed, candidate family, trained thresholds, strength, excluded leading-Bs, frame counts and parameters. No substitution of O/X for J without owner decision. Native GOP even/odd only descriptive. K0 is frozen for separately authorised S2-I4; it is NOT the S2-I8 final candidate, and no S2-I8 content is touched in P1.

## 4. Run control, evidence boundaries and separation from other work

- Initial developer changes are confined to P1A files. Do not edit Stage 1, the accepted P0 files, `02`, `05`, `06`, Stage 2 v0.7 or S2-I3 v0.3 to start P1.
- Use non-destructive scratch/output paths, provenance and a SHA manifest. `git add -- <explicit paths>` only; audit with `git diff --cached --name-status --no-renames` and verify the staged blobs. Existing local untracked Claude review files, v0.13 (if still present), and v0.14 are not part of a P1 code commit.
- Windows isolate: `D:\TEST\Vapoursynth_x64_R81\python.exe` has isolated path behaviour. A normal script invocation or `PYTHONPATH` can fail to find siblings. Rehearse exact deployed invocation with `-I`; tests must fail closed. P0A's `-c`/`runpy.run_path` mechanism is known, but reuse only after source check and Claude's Windows CMD audit.
- Four leftover tracked review/duplicate files, the D-23 `06` filename deviation, the ChatGPT/Claude role handover installation, transfer ledger and interim bridge retirement are separate administrative tracks; the owner's decision is to defer non-blocking cleanup. Nothing in P1 is permission to delete/rename them.

## 5. Independent reviewer request and decision boundary

Claude: please review **the proposed P1A first slice for adequacy and minimum cost**, and then check the P1B-P1D sequence against ratified Stage 2 v0.7 / S2-I3 v0.3, with MUST/SHOULD/OPTIONAL findings only for material technical or safety issues. Explicitly assess: (i) geometry support and parity, (ii) OFF identity proof and fail-closed tests, (iii) available P0 code/module reuse, (iv) four-fold O/X/J selection leakage, (v) proper B0 fixed-QP scope, (vi) no hold-out contact, and (vii) unnecessary process overhead. Source-reviewed concrete objections are preferable to new documents.

**Next deliverable after review:** ChatGPT writes the P1A source-code candidate and its test harness; Claude runs/rehearses what it can and audits Windows CMD; the owner installs/runs an explicit bounded set. Nothing here requires waiting for the handover/bridge retirement track, and no further *P1 start* authorisation should be requested: the owner has already provided it. Any new B1 policy, protected use or S2-I4 work still requires its own owner decision.
