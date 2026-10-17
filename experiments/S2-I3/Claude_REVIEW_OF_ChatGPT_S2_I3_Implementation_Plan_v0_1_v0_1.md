# Claude review of ChatGPT S2-I3 implementation plan v0.1 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: `ChatGPT_S2_I3_Implementation_Plan_v0_1_FOR_CLAUDE_REVIEW.md`
Baseline: `35cd543b459a5856688f7c3795f73226e72311f8`.

## 1. Verdict

**P0 PLAN CLEARED, subject to the SHOULD items below.** There are no MUST findings.

- **Integrity:** the manifest hashes match. The files are US-ASCII CRLF with no identity text.
- **Consistent with the installed authorities:** the plan is consistent with Stage 2 v0.7 section 6.3 and S2-I3 v0.3 on every point:
  - hold-out protection;
  - the fixed-QP-only scope and B0;
  - the six immutable indexes;
  - the qualifying-block definition;
  - the display-order anchor;
  - native uint8 16x16 comparison;
  - the same-offset in-bounds controls;
  - FAIL-versus-INCONCLUSIVE precedence;
  - the 200-block / 10-picture floor.
- **Recommendation:** ChatGPT can author the P0 code candidate once the SHOULD items below are written into it. Claude will rehearse that code on Linux before any owner run.
- **Pair rule:** review question 3 asked for a predeclared pair rule. Section 3 supplies one, and Claude has rehearsed it on all four pairs.

## 2. Answers to the plan's questions

**Q1 - decomposition and reader invariants.**

- A pure P-skip core with an injected frame provider, plus a thin BestSource adapter, is the right split.
- Add these invariants to the core:
  - **(a) Display order.** Assert that `index.records[i].output_ordinal == i` for every record, so the records are in display order. Claude's rehearsal relied on this, and the reader exposes it.
  - **(b) Anchor derivation.** Derive each picture's anchor by scanning display order for the last I or P picture before it, never as `n-1`.
  - **(c) Type agreement.** Check the picture type per frame against BestSource `_PictType` before comparing.
- Unit tests must include:
  - a P picture whose anchor is two or more frames earlier, with B pictures between;
  - a P picture with no earlier anchor, which is excluded;
  - a mixed SKIPPED and INTER-CBP0 frame, where only SKIPPED blocks qualify.

**Q2 - controls.**

- The 24 spatial offsets match "declared diagonal offsets" in v0.7. They include all seven S2-I2 known-bad offsets as axis shifts.
- Do **not** expand the set. The axis shifts already cover every coordinate error the gate must detect; more diagonals add no discrimination.
- Temporal controls A, B and C are correct, with these clarifications to write into the code and plan:
  - **Executability is aggregated per source.** A control counts as executed if at least one valid block comparison exists across the source's P pictures. Exclusions at individual pictures are counted and logged:
    - A, the earlier anchor, is missing for P pictures in the first GOP;
    - B, the next picture, is missing at the end of the clip;
    - C, the immediately previous picture, is excluded wherever that picture is the true anchor.
  - **INCONCLUSIVE, at source level,** applies only when a control has **zero** valid comparisons for the whole source, or when its aggregate identity is 100%.
  - **Every development source should execute all three controls.** All eight contain B pictures, and in Claude's rehearsal every control had more than 1,500 valid blocks on every source.

**Q3 - pair correspondence.** Section 3.

**Q4 - Stage 1 regression.**

- Run the six-index S2-I1 regression (v0.2, unchanged) **once per campaign**, at the start.
- Separately, before each source is used, hash-check the index file actually being read: an accepted baseline against its frozen hash, a scratch index against its generation manifest. This is cheaper and just as safe.

**Q5 - reusing the S2-I2 engine (SHOULD S1).**

- `stage2_registration_stats_v0_1.py` is generic. It handles 704 width, any MB-aligned size and leading B, so it can be reused unchanged.
- The S2-I2 **adapter** (`stage2_registration_clip_v0_1.vpy`) and **BAT** cannot be reused:
  - the adapter hard-codes its label as `'LP_blocky' if stem endswith '_blocky' else 'LP'`, so XP, SP and 3A results would be written as `S2_I2_LP_result.txt` and labelled LP;
  - the BAT accepts only LP or LP_blocky.
- Provide a **new** S2-I3 diagnostic adapter that passes an explicit source label, writes to a per-source output folder, and records "S2-I2 diagnostic (original thresholds), not admission".
- Do not use `stage2_check_result_v0_1.py` as a gate, as the plan already says.
- No accepted S2-I2 file needs editing.

**Q6 - provenance and tracking.**

- The indexes contain no paths or names: the only readable text is the magic `S1MBIDX1`. Their bytes are therefore machine-independent, as the earlier gcc/Windows LP_blocky match showed.
- They are not Restricted Media (NOTICE, index files clause).
- **SHOULD S2: admission and tracking must use the same bytes.**
  - Run P0 admission on the generated scratch index.
  - Record its SHA-256 in `source_manifest.json`.
  - At the separate tracking step, copy that same file into `VHSC_samples/` and verify the hash is identical before `git add`.
  - Never regenerate an index between admission and tracking.

**Q7 - checkpoints.** The P0A-P0E split is reviewable. Deliver P0A (core and tests) together with the P0B/P0C/P0D scripts as **one code drop**, but with separate owner-run steps. Rehearsing them together is more efficient and still bounded.

## 3. Proposed predeclared pair-correspondence rule (SHOULD S3)

**Notation:**

- `b_N` is blocky frame N and `o_N` is original frame N, each a full luma plane.
- `MAE(x, y)` is the mean absolute difference.
- Candidates are offsets k = -2..+2, kept within range.
- Mean absolute difference is a norm, so the triangle inequality holds: `MAE(b_N, o_{N+k}) >= MAE(o_N, o_{N+k}) - MAE(b_N, o_N)`.

**Decisive frame.** Frame N is decisive if `min over k != 0 of MAE(o_N, o_{N+k}) >= 2 * MAE(b_N, o_N)`.

- If the pair is correctly aligned, the triangle inequality makes it **impossible** for any k != 0 to beat k = 0 in a decisive frame.
- In non-decisive frames (static or fading content), the candidate originals are too similar to tell apart. Those frames are reported as ambiguous and not judged.

**PAIR PASS requires all of:**

1. equal frame counts (otherwise HARD FAIL);
2. the clip-mean MAE over frames in range is a strict minimum at k = 0;
3. **zero** decisive-frame violations, meaning no decisive frame where some k != 0 has strictly lower MAE than k = 0 (otherwise FAIL);
4. at least 20 decisive frames **and** at least 10% of frames decisive (otherwise INCONCLUSIVE, which blocks paired metrics only).

Conditions 1-3 involve no tunable threshold. Condition 4 is a sample-size floor.

**Claude's rehearsal** (FFmpeg/Linux, all frames, no filtering; media deleted afterwards):

| Pair | Aligned: clip-mean MAE k=0 vs best other | Decisive frames | Violations | Simulated 1-frame slip (either direction): argmin / decisive |
|---|---|---|---|---|
| XP | 3.57 vs 10.09 | 143/228 (63%) | 0 | moves to +/-1 / 0-1 frames |
| SP | 3.27 vs 14.15 | 178/192 (93%) | 0 | moves to +/-1 / 0-1 frames |
| LP | 4.35 vs 10.17 | 85/204 (42%) | 0 | moves to +/-1 / 0-1 frames |
| 3A | 5.51 vs 19.81 | 268/300 (89%) | 0 | moves to +/-1 / 0 frames |

**Disclosure:** the floor in condition 4 was set after seeing these numbers. The aligned (42-93%) and slipped (0-1%) regimes are so widely separated that any floor between them behaves the same way.

Under v0.7 section 15, ambiguous frames are reported, not failed. Paired-reference metrics may use every frame once the pair passes.

## 4. Further SHOULD items

**S4. CMD safety for index generation.** Reuse the cleared S2-I2 prepare-BAT patterns:

- the `ffmpeg -c:v copy` output goes to a regular `.m2v` file in an owned scratch folder;
- the inspector is run as `-b file -m idx`, with no pipe;
- log echoes put the redirection first (`>>"%log%" echo ...`);
- one writer at a time;
- `%rc%` is captured immediately;
- the zero-size checks are kept;
- only named scratch files are deleted.

On top of that, the BAT must **refuse** to run if a target name already exists in `VHSC_samples/`, and must never write there.

**S5. Restricted Media lifecycle.**

- The scratch `.m2v` files are Restricted Media: delete them at the end of each generation run (owned names only).
- P0 needs no decoded media on disk. BestSource decodes in memory, and the pair checks operate in memory.

**S6. Expected-value cross-check (informational).**

- Claude's rehearsal counts of P-skip blocks were: XP 1619, XP_blocky 25635, SP 1764, SP_blocky 19010, LP 1533, LP_blocky 20300, 3A 8812, 3A_blocky 18190.
- The Windows results should reproduce these counts exactly, because the counts come from the index, not the decoder. Any difference points to an index or reader discrepancy.
- Record the comparison. Do not use it as a gate.

## 5. OPTIONAL

**O1.** Also check the two 8x8 chroma blocks of each qualifying macroblock as an additional report. It is cheap. It is not a gate.

**O2.** In `P0_summary.json`, record the runtime identity (vspipe, Python, NumPy and BestSource version plus plugin SHA), as S2-I2 did.

## 6. Next step

ChatGPT authors the P0 code candidate (P0A-P0D) with S1-S6 applied. Claude then:

- reviews it line by line, including CMD auditing;
- runs its unit tests;
- rehearses the core on FFmpeg-decoded development sources;
- clears or rejects it before any owner Windows run.

No hold-out media is touched, and no filtering takes place.
