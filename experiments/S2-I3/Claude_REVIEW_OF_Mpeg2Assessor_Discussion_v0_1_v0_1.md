# Claude review - Mpeg2Assessor discussion paper v0.1 and the breadth of S2-I3 P1

**Filename:** `Claude_REVIEW_OF_Mpeg2Assessor_Discussion_v0_1_v0_1.md`
**Version:** 0.1
**Date:** 2026-10-18
**Reviewer:** Claude (independent reviewer role)
**Subject:** `ChatGPT_DISCUSSION_PAPER_Mpeg2Assessor_and_Filter_Selection_v0_1_FOR_CLAUDE_REVIEW.md`,
SHA-256 `9ad149bda6390254a48acf2e6698184d47c9e6cc8b9418e19e1a78f4028a3a8c` (manifest matches; 39,680
bytes, CRLF, ASCII)
**Checked against:** repository at `98e89c8` (ratified S2-I3 v0.3, Stage 2 v0.7, `05` v1.2, P0 Evidence
and Gate Report v0.1, `TESTING/TEST_Mpeg2BlockInspector_LP_2.BAT`)
**Nature:** review correspondence. Not ratification; authorises nothing. Do not stage.

---

## 1. Summary

**On Mpeg2Assessor: do not build it now, and probably not as a separate program at all.** The
question it asks is a good one: does the best filter setting vary between recordings, or within a
recording, enough that one global setting plus local per-seam rules leaves quality on the table?
But that question can be answered from P1's own outputs at almost no extra cost (section 5), and
the production plugin already reads the whole index at start-up (D-24), so anything an assessor
could learn from metadata is available inside the plugin for free. Build nothing until the
headroom numbers say there is something to gain.

**On P1 breadth: the owner is right, and the reason is stronger than the paper states.** The
development pool is tiny: eight recordings of 192 to 300 frames each, 1,848 frames in all (about 74
seconds of video). At that size, actually filtering and measuring every structured combination is
cheap, so there is no reason to shortlist on diagnostic proxies first. A bounded amendment that
replaces "screen, then shortlist two or three" with "filter the whole predeclared grid, select
mechanically inside each fold" would improve P1. The real constraints are not CPU time but
**evaluation validity** (only four independent content groups, no ground truth for the originals)
and **human review capacity** (the owner cannot look at thousands of variants). Section 4 sets out
a design that respects both.

**The paper's biggest gap** is that its sampling, frame-count and temporal-range sections are
written for long recordings, but every development recording is 8 to 12 seconds long. On this pool,
every frame is measured, 1% sampling means two frames, and temporal-range policies cannot be tested
at all (finding M1).

## 2. Verified facts (with sources)

| Fact | Source |
|---|---|
| The accepted Windows BAT pipes the elementary stream straight into the inspector; no `.m2v` is written | LP BAT line 63: `ffmpeg ... -c:v copy -an -f mpeg2video - \| Mpeg2BlockInspector -b - -m index` |
| `.s1tmp` is the inspector's scratch **index**, renamed on completion | LP BAT lines 23 and 42 |
| **The accepted BAT already reads the original file twice**: a full FFmpeg pass to `NUL` with `-v info` logged, then the piped pass | LP BAT line 58, then line 63 |
| `%ERRORLEVEL%` after the pipe is the inspector's alone; FFmpeg's exit status is lost | LP BAT line 64; CMD pipeline semantics |
| FFmpeg's stderr in the piped command is not written to the log: the `>>log 2>&1` binds to the inspector only | LP BAT line 63 |
| Development pool: XP 228, SP 192, LP 204, 3A 300 frames, each with a `_blocky` partner of equal length; 1,848 frames | P0 Evidence Report, admission table |
| P1 currently says: measure diagnostic discrimination and no-harm sensitivity, then "shortlist two or three practical M/F/R/T/P/K combinations with reasons" | S2-I3 v0.3 section 5; Stage 2 v0.7 section 8.4 ("choose a small declared shortlist") |
| A declared strength sweep (OFF/LOW/NOMINAL/HIGH or numeric) is already part of Stage 2 | Stage 2 v0.7 section 12 |
| One manual global strength now; an `auto` or adaptive strength "may be considered later if evidence supports it" | `05` D-07 |
| No existing external deblocker is part of the Stage 2 comparison; "revisit only if later evidence creates a specific need" | Stage 2 v0.7 section 3.7; `05` D-26 |
| The production deblocker requires its index and takes geometry from it | `05` D-24 |

The paper's pipe description in section 1 is correct. Its statement that pipe failure accounting
needs explicit checks is also correct, and the BAT confirms why: only the inspector's exit code is
captured, and FFmpeg's error text from the piped pass goes to the console, not the log. Truncation
of an admitted source would still be caught by P0's hard structure checks (frame counts against
BestSource), so this is a gap for future tooling, not a defect in accepted evidence (S5).

## 3. Findings on the paper

### MUST

**M1. Ground the sampling, frame-count and granularity sections in the real pool.** All eight
development recordings are 192 to 300 frames. For P1 and any assessor study on this pool:

- every eligible frame is measured, as S2-I3 v0.3 already requires; sampling plans have nothing to
  sample (1% of 204 frames is two frames);
- pre-index frame-count estimation solves no development problem;
- **temporal-range policies cannot be tested**: an 8-second clip has no quality drift for a
  segment-level policy to exploit, and too few GOPs to tell real variation from noise.

Sampling and temporal-range questions need long-form recordings. None is currently available for
filtering: EP/2A/4A are locked until S2-I8, 6A/7A have no role, and archive material is unadmitted.
Any temporal study therefore needs an owner decision on source roles first (section 7, question D).

**M2. If P1's search widens, selection inside each fold must be fully mechanical and frozen before
any held-out result is viewed.** The paper keeps the four-fold structure and says early elimination
must be justified, which is right. But with thousands of evaluated configurations, the one thing
that would invalidate the cross-validation is a person or an AI looking at held-out results and
then "choosing". The rule must be: a predeclared selection function runs on the three training
groups, produces one choice per fold and arm, and is logged with its hash before the held-out
group's results are opened. Broad search inside a fold is statistically fine; human picking across
the held-out landscape is not.

**M3. Decide the P1 amendment before the P1 experiment controller is written.** The controller's
shape depends on it (shortlist-then-tune versus a cached-feature grid). The paper correctly says a
formal amendment would be needed. Building the narrow version first and widening later would mean
writing it twice.

### SHOULD

**S1. Drop the single-pass framing and paths C, D and G.** The accepted workflow already reads the
original twice (BAT line 58), and BestSource reads the whole file on first open to build its own
cache. Re-opening the original after indexing (path B) is therefore existing practice, not an
added cost. The dual-output and streaming paths solve a problem the project does not have, unless
the owner states a real requirement to process live or non-reopenable sources. Paths E and F are
already rightly rejected in the paper.

**S2. Park the MediaInfo preflight.** The exact frame count, geometry and coding state come from
the index, which the plugin must have anyway (D-24). MediaInfo adds provenance and an early
wrong-stream guard, nothing more. For MPEG program streams, MediaInfo normally does not parse the
whole file by default, so its `FrameCount` is likely to be derived from duration and frame rate
rather than counted; the paper's caution is right, but the feature has no consumer. Revisit only
if a concrete need appears.

**S3. Make "headroom" the gate for any assessor work, and sequence it after S2-I4.** Section 5
gives the measurement. Note the overlap: the real per-macroblock QP map tested in S2-I4 is already
a local, per-source severity signal. If real QP captures most of the per-source variation, an
assessor has little left to add. Deciding on an assessor before S2-I4 reports would be premature.

**S4. If an assessor is ever justified, treat it as a function, not a program.** Metadata
statistics over the whole recording can be computed by the plugin at start-up from the index it
already reads. A pixel pre-pass would be a sampled read of the source, which a VapourSynth script
or the plugin can also do. A separate `Mpeg2Assessor` executable adds a deployment artefact, a
sidecar format and a synchronisation problem, and needs its own justification beyond "it could".

**S5. Future (non-frozen) BATs should log FFmpeg's stderr in the piped command and check FFmpeg's
own success**, for example by writing its stderr to a separate log and validating the index frame
count against BestSource. The seven frozen TESTING BATs stay as they are.

**S6. Park spatial tiles.** The per-seam rules (R/P/K options with QP-scaled thresholds) are
already spatially adaptive at the finest useful scale. Tiles are a coarser version of the same
idea, with extra boundary and confidence machinery. Consider them only if the per-seam rules fail
in an identifiable, region-shaped way.

**S7. Define complementarity before testing "several different algorithms".** Two algorithms are
complementary only if (a) the per-source or per-region oracle choice between them beats the best
single algorithm by a stated margin, (b) the gain has the same sign in at least three of four
held-out groups, and (c) a predictor trained on the other groups recovers most of the oracle gain
out of group. (a) alone is an upper bound and is always positive by construction; it proves
nothing.

**S8. Restricted Media applies to caches.** Decoded luma caches and per-pixel feature caches are
derived visual media. They belong in a scratch folder outside the repository, are deleted after
the campaign (as BestSource caches already are), and never appear in results. Per-configuration
numeric summaries are ordinary text.

### OPTIONAL

**O1. Existing-filter yardstick.** The owner's concern is missing better approaches. The cheapest
check against that is to run one or two existing generic deblockers (for example an H.264-style or
pp7/spp-style VapourSynth filter) through the same metrics, as a **yardstick only**, never a
candidate. This reverses a recorded owner ruling (Stage 2 v0.7 section 3.7), so it is the owner's
call (section 7, question A).

**O2. Family C (K4) as a reference arm.** Its ratified status is "optional; must not delay Family
A". In an automated campaign it no longer costs calendar time to run, only implementation effort.
Worth including if implementation proves modest.

**O3. B1 as a separately labelled arm.** Adding the boundary-class option costs little CPU in a
cached grid, but B1 requires its own owner decision (S2-I3 v0.3 section 5). It must never be mixed
into the B0 results.

**O4. Indifference band and parsimony.** Many configurations will tie within measurement noise.
The selection function should pick the simplest configuration within a predeclared band of the
best training score, not the nominal top, which on four groups is mostly noise.

## 4. A bounded P1 amendment that uses the compute budget well

### 4.1 Why compute is not the constraint

Rough sizing, to be benchmarked first: 1,848 frames of 720x576 luma hold about 100,000 vertical and
horizontal block-boundary positions per frame, so about 190 million in the whole pool. The filters
under test are short-support and seam-local. That allows a two-level design:

1. **Once per source (expensive):** decode, validate against P0, and cache per-seam features (M1..M5,
   M4a, F1..F3, per field) plus the pixels within the correction support.
2. **Per configuration (cheap):** apply the decision rule and correction to the cached features
   only, then compute metrics from the corrected seam pixels and the changes.

On those assumptions a configuration might cost one to five seconds across all eight sources in
NumPy, against perhaps 30 to 60 seconds if each one re-filtered whole frames. So a one-to-two-day
unattended budget covers roughly **10,000 to 100,000 configuration evaluations** with the cached
design, but only a few thousand with the naive one. These are order-of-magnitude estimates; the
first step should be a small benchmark (section 6).

Two technical cautions:

- **Pass interaction.** Vertical-then-horizontal filtering reads pixels already changed near block
  corners, so a seam-local surrogate is not exactly the full-frame result. Use the surrogate for
  the search, re-run the Pareto set with an exact full-frame reference implementation, and report
  how well the surrogate's ranking agrees with the exact one (for example a rank correlation). If
  agreement is poor, the surrogate is not fit for selection.
- **A configuration's output depends only on the configuration and the source, not on the fold.**
  Compute each configuration once per source and reuse it in every fold and arm; only the
  *selection* differs by fold. This divides the cost by twelve (four folds, three arms).

### 4.2 What to evaluate

- **Structure:** every meaningful combination in the ratified inventory: M (6 options) x F (3) x R
  (4) x P (3) x K (K1-K3; K4 optional) x D (2), excluding combinations that are undefined (a rule
  that needs an input the chosen measure does not supply). Record each exclusion with its reason.
- **Continuous parameters:** thresholds and their QP scaling on a predeclared grid per structural
  combination (T1), plus T2 starting tables as a separate structural option.
- **Strength:** the ratified declared sweep, OFF included and checked bit-exact.
- **Metrics:** as S2-I3 v0.3 section 7, computed for every configuration and every source, plus a
  temporal-stability measure (frame-to-frame change of corrections in static regions).

### 4.3 How to select without fooling ourselves

1. **Predeclare** the selection function per arm: maximise seam-excess reduction on the training
   originals (2:1 weighted as ratified in arm J) **subject to** hard no-harm limits (off-seam change,
   edge damage, clamped pixels, flicker). A constrained rule is easier to defend than a weighted sum.
2. Apply the indifference band and parsimony rule (O4).
3. Run it mechanically per fold and arm; log the choice and its hash before opening held-out results
   (M2).
4. Report held-out results for the chosen configuration per fold. Also report the **rank stability**
   of the training top-50 on the held-out group; configurations that collapse out of group are
   flagged as overfitted.
5. **Interactions and outliers:** fit a simple main-effects plus two-way-interactions summary over
   the full factorial on training groups only. Claim an interaction only if it has the same sign in
   at least three of four groups. Flag any configuration whose held-out rank differs wildly from its
   training rank.
6. **Human stage:** the automated stage ends with a small Pareto set. **This is where "two or three"
   belongs:** the owner blind-views two to six Pareto points, not two or three survivors of a proxy
   screen.

Everything else in S2-I3 v0.3 stays: four leave-one-group-out folds, O/X/J arms with identical
budgets, fixed QP only, B0 only, no p-values, K0-J fitted on all eight after selection, protected
hold-outs locked until S2-I8.

### 4.4 Managing result volume

One machine-readable results table (one row per configuration x source x metric set) stays in the
scratch area. The committed outputs are generated summaries: per-factor effects, the Pareto set,
the selected configuration per fold and arm, rank-stability tables, flagged outliers, exclusions,
failures and reproducibility hashes. Nobody reads the raw table by eye.

## 5. The headroom test that decides the assessor question

From the same P1 runs, with no new tooling:

- **Per-source oracle headroom:** for each held-out source, compare the selected single
  configuration with the best configuration *for that source alone* (an oracle). If the oracle gain
  is small on all four groups, a per-recording assessor has nothing to win. Stop.
- **Per-GOP oracle headroom:** the same within each source, by native GOP. On 8-to-12-second clips
  this is weak evidence and only descriptive, but a large gap would be a signal worth pursuing on
  longer material.
- **Predictability:** if headroom exists, can simple whole-source statistics (QP histogram, transform
  mix, measured seam excess) predict the oracle's choice for a held-out group from the other three?
  With four groups this is close to anecdotal; treat it as a reason to gather long-form material, not
  as proof.

Then wait for S2-I4. If real per-macroblock QP closes most of the per-source headroom, the
assessor's job is already done by the index.

## 6. Answers to the paper's section 12 questions, in brief

1. **Pipe:** confirmed as described, with the error-capture gaps in section 2 and S5.
2. **Pixels:** the inspector sees only the compressed stream; no decoded pixels. Path B (re-open the
   original with BestSource) is existing practice; C, D and G are unnecessary (S1).
3. **MediaInfo:** low value; park it (S2).
4. **Sampling:** irrelevant on the current pool (M1). For later long-form work, re-open the original
   after indexing and use stratified temporal bins with jitter, using the exact index frame count.
   That is unbiased and simple; a one-pass reservoir design is not needed.
5. **Granularity:** whole-source and per-seam can be tested now; temporal ranges need long material;
   spatial tiles should be parked (S6).
6. **Filter policy:** the strength sweep is already ratified; continuous adaptation is R4; R3/K3 is
   already a two-mode switch. Test genuinely different algorithms only against the complementarity
   rule in S7.
7. **Automation:** section 4.
8. **Ratified changes needed (if adopted):** S2-I3 v0.3 section 5 (the shortlist paragraph and the
   "feature shortlist" wording in 4.2) and Stage 2 v0.7 section 8.4 ("choose a small declared
   shortlist"), as new versioned documents S2-I3 v0.4 and Stage 2 v0.8 under D-23. No change to
   D-07, D-13 or D-24 for the P1 amendment. O1 changes Stage 2 v0.7 section 3.7; O3 needs the B1
   owner decision. An eventual assessor or `auto` strength would need a new decision building on
   D-07.
9. **Recommendation:**

| Question | Assessment |
|---|---|
| Technical feasibility of an assessor | High. Offline Python over the index plus re-opened pixels is easy |
| Expected payoff | Unknown, probably small for per-recording choice given QP-scaled local rules; measurable via section 5 |
| Cost and complexity | Moderate as a function; high as a separate program with a sidecar format |
| Testability now | Per-source headroom only. Temporal ranges are untestable on the current pool |
| Timing | After P1 headroom and S2-I4. Not now |
| Do not build it | A legitimate outcome, and the current favourite |

**Suggested first step if the owner accepts the amendment:** a benchmark on one fold's training
material (feature cache build time, per-configuration time, memory, surrogate-versus-exact agreement
on a few configurations), then size the full grid from measured numbers rather than estimates.

## 7. Questions for the owner (only these need you)

- **A.** Revisit the no-yardstick ruling so one or two existing deblockers are measured alongside, as
  yardsticks only (O1)?
- **B.** Include B1 as a separately labelled arm (O3)?
- **C.** Include Family C (K4) if its implementation is modest (O2)?
- **D.** Is there long-form material that could be given a development role for later temporal
  questions? 6A/7A would need characterising and a design revision; the archive would need admission.

Everything else here can be settled between the two roles.

## 8. Agreement and disagreement with the paper

**Agree:** the pipe facts; the separation of expensive feature acquisition from cheap re-evaluation;
B0 and fixed QP for P1; fold discipline and arm parity; the staged granularity order; Python first,
C++ only on measured need; owner visual judgement as final; "do not build" as a legitimate outcome;
no change to Stage 1, the index or the frozen tests.

**Disagree, or would weight differently:** the paper's sampling and temporal sections do not fit
the pool (M1); the single-pass and dual-output paths (S1) and the MediaInfo preflight (S2) add work
with no consumer; a separate assessor program is the least likely useful form (S4); and the
assessor decision should wait for S2-I4 (S3).
