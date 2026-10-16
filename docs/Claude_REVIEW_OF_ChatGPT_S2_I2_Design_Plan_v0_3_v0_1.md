# Claude Review of ChatGPT's S2-I2 Design Plan v0.3

**Filename:** `Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_3_v0_1.md`
**Version:** 0.1
**Date:** 2026-10-15
**Reviewed:** `ChatGPT_S2_I2_Design_Plan_v0_3_FOR_CLAUDE_REVIEW.md`, its review request and traceability
note (all US-ASCII, CRLF; zero identity hits)
**Status:** Design review. **Verdict: all v0.2 findings and owner additions are correctly
incorporated. One MUST (a threshold of Claude's own proposal that is too tight for the new row-phase
test), three SHOULDs. After those, suitable for owner ratification and bounded implementation.**

---

## 0. Method

The plan was read in full against Claude's v0.2 review, the owner's additions, options table v0.2,
Stage 2 v0.6 and the S2-I1 reader. The traceability note is accurate: every item maps to a v0.3
location.

Claude re-ran one informal check, because the new row-phase gate inherits a 10% margin that Claude
proposed in v0.2 for the column phase without testing it on the row phase. The check: LP and LP_blocky,
FFmpeg decode, row-phase margin under four sampling regions. Recordings and decoded frames were
deleted afterwards. (Disclosure as before: these are real values seen before the formal run.)

| Clip | Region | Row-phase margin min(q6,q7) over max(others) | Frames with q6 and q7 on top |
|---|---|---|---|
| LP | interior (16-px border excluded) | 11.5% | 92% |
| LP | interior (32-px border) | 11.1% | 92% |
| LP | central half | **9.7%** | 87% |
| LP | full width | 11.9% | 93% |
| LP_blocky | the same four regions | 20.7% - 26.1% | 72% - 81% |

## 1. Findings

### M1 - MUST - The 10% row-phase margin can fail a correctly aligned LP

On the correctly aligned LP, the row-phase margin is only 10-12%, and the central-half region gives
9.7%. Under v0.3 section 3.4 / gate J, a sampling-region choice alone could therefore return
INCONCLUSIVE and block S2-I2 when nothing is wrong. VHS's strong same-field vertical detail raises all
phases, so blocking stands out less vertically than horizontally (the column-phase margin on LP is
about 33%).

What actually detects misregistration in this test is the **rank**, not the margin: at +1 and +2 rows
the top two phases become {7,0} and {0,1}, so the test fails outright. The margin is only a guard
against ties and noise. Replace gate J's rule with:

```text
Row phase PASS iff, on the fixed interior region (frame minus a 16-pixel border; declared in the
manifest): q6 and q7 are the two largest aggregate means; AND
row_margin = (min(q6,q7) - max(other q)) / min(q6,q7) >= 0.05; AND q6 and q7 are the top two in at
least two thirds of eligible frames.
FAIL if any other phase ranks in the top two in aggregate. INCONCLUSIVE otherwise.
```

Keep the column-phase and 3x3 thresholds unchanged (10% and 2/3). They have large headroom (column
about 33%; 3x3 +28% / 93% on LP). This corrects Claude's own v0.2 S1 proposal, which applied 10% to "the
phase tests" without checking the row phase that Claude added in the same review.

### S1 - SHOULD - Fix the horizontal sampling pairs exactly (the review request asked for this)

The text is close but leaves the comparator pairs implicit. Proposed exact definitions, all
same-field, row indices relative to the MB top `b`, and the same for every class:

```text
Class                      cross-boundary pairs         comparator (in-block) pairs
FRAME internal (7|8)       (b+6,b+8), (b+7,b+9)         (b+4,b+6),(b+5,b+7) above; (b+8,b+10),(b+9,b+11) below
outer MB edge (b-1|b)      (b-2,b),   (b-1,b+1)         (b-4,b-2),(b-3,b-1) above; (b,b+2),(b+1,b+3) below
control (3|4)              (b+2,b+4), (b+3,b+5)         (b+0,b+2),(b+1,b+3) above; (b+4,b+6),(b+5,b+7) below
control (11|12)            (b+10,b+12),(b+11,b+13)      (b+8,b+10),(b+9,b+11) above; (b+12,b+14),(b+13,b+15) below
FIELD / NONE mid (7|8)     as FRAME internal            separate no-coded-seam classes, never standard controls
```

- **Plain:** mean |cross| minus mean |comparator|.
- **Robust (per parity):** |signed mean cross step minus mean signed comparator slope| /
  (mean |comparator| + 1), over each 8-column chunk (columns 0-7 and 8-15 of the MB). Take the
  equal-weight mean of the 2 parities x 2 chunks.
- **Vertical** is the transpose: per 8-row field population, pairs (x-1,x), comparators (x-3,x-2) and
  (x+1,x+2).

Each comparator lies inside one block and one field, and never crosses the boundary being measured.

### S2 - SHOULD - Detect the NumPy interpreter through vspipe itself

S4's intent is right, but "detect or require explicit configuration" leaves path-guessing open. The
robust method is a tiny preflight `.vpy`, run with the **same** `vspipe --info` as the real run. It
imports NumPy and writes `sys.executable`, `sys.version`, `numpy.__version__` and the VapourSynth and
BestSource versions to stderr, and fails if the import fails. This is by construction the interpreter
the real run uses; no hardcoded Python path is needed.

### S3 - SHOULD - Keep the statistics runnable outside VapourSynth

Make `stage2_registration_stats` take plain NumPy luma arrays plus reader records, with no VapourSynth
import. The `.vpy` only fetches BestSource frames and passes them in. Claude can then execute the
**actual** statistics code on FFmpeg-decoded frames before the owner runs anything. Without this, the
execute-before-owner duty covers only the synthetic tests. Also stream frame by frame (or bound memory
to about 1 GB): seven offset controls times full-clip arrays would otherwise be large.

### O1 - OPTIONAL - Small corrections

- The status v0.5 commit is `2286341` (pushed after `4221f7f`); it can now be cited (section header,
  section 0).
- State the offset sign once in the manifest: "pixels moved right/down by k; index unchanged". That is
  the convention Claude's probe used (the 8-column offset then peaked at dx = +1).

## 2. Answers to the review questions

| # | Answer |
|---|---|
| 1 | The row-phase equation and expected {6,7} are right and close the +1/+2 gap. The margin needs to be 5% plus frame consistency (M1). Region: declare the fixed interior, 16-pixel border. |
| 2 | 3x3 and column gates: specified well enough to freeze. FAIL versus INCONCLUSIVE are clear. The disclosure is adequate. |
| 3 | D_norm as a descriptive companion with raw D gating: agreed. The pairs 2|4, 3|5, 10|12, 11|13 are faithful. |
| 4 | Seven offsets, common interior, "at least one test non-PASS" per offset, and LP_blocky identity: confirmed. The probe shows each offset caught: +4 columns by the column phase; +8/+16 columns and +8/+16 rows by the 3x3; +1/+2 rows by the row phase. |
| 5 | Use the vspipe-run preflight (S2). |
| 6 | Section 3.6 reproduces plain M2 and robust M4, both orientations, the controls, NONE kept separate, a fixed 5% FA per clip/orientation/metric, AUC and frame/GOP uncertainty, without selecting a detector. Horizontal pairs: S1. |
| 7 | Confirmed: the report is completeness-only, not a gate; options table v0.2 is preserved in full; B1 deferred; G1/G2 optional; no hold-out leakage. |
| 8 | Clip roles confirmed. |
| 9 | Six files plus one small report helper is fine, with S3's separation. |
| 10 | Confirmed: no v0.6 revision before implementation. Record the row-phase test and LP_blocky's role at the next real Stage 2/status revision. CSV suffices as the seam map; no default PNG. |

## 3. Change log

### v0.1 - 2026-10-15

- First issue.
