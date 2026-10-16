# Claude Review of ChatGPT's S2-I2 Design Plan v0.2

**Filename:** `Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_2_v0_1.md`
**Version:** 0.1
**Date:** 2026-10-14
**Reviewed:** `S2_I2_Design_Plan_v0_2_FOR_CLAUDE_REVIEW.zip` (manifest OK; US-ASCII, CRLF; zero identity
hits; no media)
**Status:** Design review. **Verdict: sound design, one MUST (a demonstrated vertical blind spot),
four SHOULDs. Not yet ready for implementation.**

---

## 0. Method, including an informal feasibility probe

The plan was read in full against Stage 2 v0.6 (sections 3, 4, 6.2, 19), `06` v1.2 geometry,
`05` D-23/D-26, `NOTICE.md` and the committed S2-I1 v0.2 reader.

To test whether the proposed statistics actually work, Claude also ran a **small informal probe**. It
is **not** the S2-I2 implementation or result. The probe:
- used the authorised LP and LP_blocky recordings;
- decoded them with FFmpeg (the decoder BestSource wraps), not BestSource itself;
- read labels with the S2-I1 v0.2 reader;
- computed the plan's statistics exactly as written: D at same-field 6|8 and 7|9, the 3x3
  shifted-label contrast on the interior lattice, and the 8-phase column test.

It then **deliberately misregistered the pixels** relative to the index (offsets of 4, 8 and 16
columns, and 1, 2, 8 and 16 rows) to see which errors the planned gate catches. Recordings and decoded
frames were deleted afterwards. **Disclosure:** Claude has therefore seen real LP values before any
acceptance threshold was fixed (relevant to S1).

### 0.1 Probe results (numbers only)

| Case | LP shifted-label C(0,0) vs best other | LP (0,0) wins per frame | LP column phase | LP_blocky C(0,0) vs best other | LP_blocky column phase |
|---|---|---|---|---|---|
| aligned | 5.74 vs 4.13 (margin +28%) | 93% | phase 0 peak, 6.32 vs <=4.21 | 4.23 vs 2.64 (+38%) | phase 0 peak, 6.40 vs <=3.43 |
| +4 columns | margin +17% (passes) | 85% | **peak moves to 4 (caught)** | +25% (passes) | **peak 4 (caught)** |
| +8 columns | **peak (1,0), margin -2% (caught)** | 39% | phase 0 (blind, as expected) | **(1,0), -2% (caught)** | phase 0 (blind) |
| +16 columns | **peak (1,0) (caught)** | 2% | phase 0 (blind) | **caught** | blind |
| +8 rows | **caught** | 15% | blind | **caught** | blind |
| +16 rows | **peak (0,1) (caught)** | 1% | blind | **caught** | blind |
| **+1 row** | **margin +25% - PASSES (missed)** | 90% | blind | +34% - **PASSES (missed)** | blind |
| **+2 rows** | **margin +23% - PASSES (missed)** | 83% | blind | +22% - **PASSES (missed)** | blind |

Both clips register correctly at zero offset. LP_blocky's own index, generated with the frozen inspector
from a regular file:
- 204 records, 720x576, 45x36 MBs, all frame pictures;
- `progressive_frame` 0;
- I 19 / P 50 / B 135, starting with I, so **no leading B** and 204 eligible frames;
- FRAME 54292 / FIELD 33853 / NONE 242335;
- QP 62 everywhere;
- every frame's picture type matches FFmpeg;
- SHA-256 `b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238` (gcc build of the frozen
  sources, which reproduced all seven other indexes byte-for-byte).

**The owner's question:** yes, LP_blocky stands out more in the phase-type measurements:
- phase-0 step 1.87x the next phase (LP 1.50x);
- same-field row phase 1.35x (LP 1.14x, see M1);
- the normalised contrast (S2) is about twice LP's.

The raw FRAME-minus-FIELD contrast is not larger in absolute terms. These are probe values only.

## 1. Findings

### M1 - MUST (technical) - The planned gate cannot see a 1- or 2-row vertical misregistration

With pixels moved 1 or 2 rows (a field-parity swap, or a decoder that pads or crops a line), both
planned tests still PASS: the shifted-label test keeps its zero-shift peak with a 22-34% margin, and the
column-phase test only looks horizontally. A parity error is exactly what would break the same-field
access that Stage 2 depends on (D-09), so the "two-dimensional registration" gate must catch it.

Add an independent **same-field row-phase test** (the vertical counterpart of section 3.3):

```text
F(N,x,y) = abs(Y[N,y+2,x] - Y[N,y,x])      same-field pair (y, y+2); never adjacent lines
group by q = y mod 8, q = 0..7, over all included frames and interior columns;
expected: q = 6 and q = 7 are the two largest (pairs 6|8, 7|9, 14|16, 15|17 straddle the 8-row
transform boundaries in each field); report per-q counts and means, and the margin of min(q6,q7)
over max(other q)
```

In the probe this peaks at q = {6,7} for both clips when aligned and moves to {7,0} and {0,1} for 1-
and 2-row offsets, so it catches both. Gate it like the column-phase test (FAIL/INCONCLUSIVE stops
S2-I2). This adds a test beyond v0.6's text but serves its stated intent; record it in the next
Stage 2 revision.

### S1 - SHOULD - Predeclare a margin and consistency rule; strict ranking alone is fragile

At an 8-column offset the zero-shift contrast is only about 2% below the winner. Noise could flip
that, and "C(0,0) > all eight" would then PASS a misregistered grid. Proposed rule, to be fixed by the
owner **before** the real run:

- **PASS:** C(0,0) is the strict maximum, **and** it exceeds every other C by at least 10% of
  C(0,0), **and** (0,0) is the maximum in at least two thirds of the frames that have both populations.
- **INCONCLUSIVE:** the maximum holds but either condition fails.
- **FAIL:** another shift is the maximum.
- Phase tests: the expected phase(s) must be the maximum with at least 10% margin over every other
  phase; otherwise INCONCLUSIVE or FAIL as above.

The probe's aligned values (+28%/93% LP, +38%/89% LP_blocky) and its misaligned values (at most
-2%/43%) sit far from these lines, so the rule is not tuned to pass. Because Claude has seen the
values, the owner should know the thresholds were proposed with that knowledge.

### S2 - SHOULD - Also report a content-normalised D

Raw D mixes the seam step with ordinary vertical detail, which correlates with the FRAME/FIELD choice.
Report alongside it (gate on raw D as declared, or on both):

```text
D_norm = D_seam(6|8, 7|9) - mean of same-field in-block steps (2|4, 3|5, 10|12, 11|13)
```

In the probe, D_norm gives the same verdicts on every offset, and on it LP_blocky's contrast is about
twice LP's (2.87 vs 1.29), whereas on raw D it is smaller (4.23 vs 5.74). It is
cheap and helps interpret confounding (plan section 3.2 "Confounding/limits").

### S3 - SHOULD - Built-in known-bad controls, and the LP_blocky expected identity

- **Known-bad controls.** Make the tool prove its own power on real data. In addition to the aligned
  run, re-run every test on the same frames with the pixels deliberately offset by +4/+8/+16 columns
  and +1/+2/+8/+16 rows (index unchanged, measured interior only). Each offset must be caught by at
  least one test (the probe shows which); the expected coverage table is section 0.1. A control that
  is not caught is a tool defect.
- **LP_blocky preflight.** Do not regenerate the 4A-blocky lesson: assert the expected identity now
  known (SHA-256 `b3f1d714...5238`, 204 records, 720x576, I/P/B 19/50/135, FRAME/FIELD/NONE
  54292/33853/242335, QP 62 x330480, no leading B), as S2-I1 did for 4A-blocky. Plan section 4.1.6
  ("no expected hash asserted") can change accordingly. The index is still non-baseline and
  uncommitted.

### S4 - SHOULD - Check NumPy in the VapourSynth Python before the run

The statistics need NumPy inside the Python that `vspipe` uses (the R81 install under `D:\TEST\...`).
That interpreter is not the one that ran S2-I1's plain-Python scripts. Add a preflight
(`import numpy` from that interpreter, printing its version) as the runner's first step; otherwise the
first owner run is likely to fail.

### O1 - OPTIONAL - State test coverage explicitly in the result file

Print which misregistrations each test can and cannot detect: the column phase is blind to 8/16-column
offsets, the shifted-label test to 4-column and 1/2-row offsets, and the row phase to 8/16-row offsets.
Together they cover all cases probed.

### O2 - OPTIONAL - Seam-map scope

The numeric coordinate CSV satisfies "seam-map diagnostics". A PNG is not required; if wanted, keep it
the separately selected Restricted Media option the plan describes.

## 2. Answers to the review questions

| # | Answer |
|---|---|
| 1, 8 Authority | No Stage 2 revision is needed before implementation. The owner's conversational assignment of LP_blocky to an S2-I2-only diagnostic role is consistent with the 2026-10-12 ruling ("nothing inferred until indexed and assigned"). LP_blocky is the development clip's own re-encode, so it exposes no hold-out content. Record the assignment in the implementation package and the next status file; fold it into Stage 2 at its next real revision, together with M1. |
| 2, 9 Index trap | Regular-file generation, independent analyzer, reader and BestSource checks, scratch-only output and "exit 0 is not enough" are all correct. Add the expected identity (S3). CMD lessons are carried; audit at implementation. |
| 3 Unknowns | Correctly not inherited. They are now measured (section 0.1): FRAME and FIELD both present, so the 3x3 test applies. |
| 4 Comparability | Same statistic, lattice and sign within each clip; no pooling: correct. |
| 5, 11 Gate integrity | The disposition matrix is correct; LP_blocky cannot rescue LP. With M1 and S1 the LP gate also becomes harder to pass wrongly. |
| 6 Software | Six files are acceptable. Explicit clip/index binding and separate scratch folders are right. Prefer one shared stats module so both clips use identical code. |
| 7 Inherited | D is suitable (keep it, add D_norm). The common lattice is fine: shifted contrasts stay positive through label autocorrelation, which is expected, and (0,0) still leads clearly. Ties are covered by S1. Parity pairs 6|8 and 7|9 and NONE's lack of internal seams match `06`. Seam maps: O2. |
| 10 Conditional contrast | Honest. NOT APPLICABLE (population absent) versus INCONCLUSIVE (present but weak) is clear. Moot for LP_blocky, which has both populations. |

## 3. Change log

### v0.1 - 2026-10-14

- First issue.
