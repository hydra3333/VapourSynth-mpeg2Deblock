# Claude Review of ChatGPT's S2-I2 Design Plan v0.4

**Filename:** `Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_4_v0_1.md`
**Version:** 0.1
**Date:** 2026-10-15
**Reviewed:** `ChatGPT_S2_I2_Design_Plan_v0_4_FOR_CLAUDE_REVIEW.md`, its review request and traceability
note (US-ASCII, CRLF; zero identity hits)
**Status:** Design review. **Verdict: no MUST. Suitable for owner ratification.** The two SHOULDs below
are implementation details. They can be carried into the implementation package as stated, so no
further design round is needed.

---

## 0. Method

- The v0.3-to-v0.4 diff was read line by line. Every change maps to Claude's v0.3 findings, and nothing
  else was removed.
- The full v0.4 text was read against the v0.2 and v0.3 reviews, Stage 2 v0.6 and the S2-I1 reader.

## 1. Confirmations (the review questions)

| # | Result |
|---|---|
| 1 Gate J | Correct. Fixed 16-pixel interior; q6/q7 aggregate top two; row_margin >= 5%; q6/q7 top two in >= 2/3 of eligible frames; any outside phase in the aggregate top two (including a tie) = FAIL; otherwise INCONCLUSIVE. The probe showed +1/+2 rows move the top two to {7,0}/{0,1}, so FAIL. The 3x3 (10%, 2/3) and column (10%) gates are unchanged. |
| 2 Pairs | The horizontal table matches Claude's v0.3 S1 exactly. Signs (lower-upper, right-left), the in-block/no-crossing rule, outer-edge `b` from the MB below, 2 parities x 2 chunks equal weighting and the vertical transpose with two 8-row field populations are unambiguous. The plain and robust formulas are correct, with the absolute value taken per subpopulation before averaging. |
| 3 Preflight | Right intent. Two practical details in S1. |
| 4 Engine | Correct: NumPy arrays plus reader records, no VapourSynth import, thin `.vpy` adapter, streaming within about 1 GB. Claude can run the actual engine on FFmpeg-decoded frames. |
| 5 Offsets | Correct. `Y_shift(x,y) = Y_original(x-cx, y-ry)`, index unchanged, a common 16-pixel interior and no wrap. The largest offset (16) exactly uses the border, so every target reads inside the frame. |
| 6 Carry-forward | Intact: raw-D gate with D_norm reported, LP_blocky identity, CSV seam map, both-orientation M2/M4, 5% FA/AUC, frame/GOP uncertainty. No tuning, kernel choice, denoising, hold-outs or pixel seam-finding. |
| 7 Disposition | Ready for owner ratification. Implementation is a separate step. |

## 2. Findings

### S1 - SHOULD (carry into the implementation) - Two vspipe preflight practicalities

1. `vspipe --info` fails if the script defines no output. Like the S2-I1 `.vpy`, the preflight script
   must end by setting an output (for example a 1-frame `core.std.BlankClip(...).set_output()`),
   otherwise it fails for the wrong reason.
2. BestSource may not expose a version query. Fail closed only on **import or plugin-load failure**
   (NumPy, `vapoursynth`, `core.bs`). For the BestSource identity, record the plugin's file path and its
   SHA-256 (available from VapourSynth's plugin listing) plus a version if one is exposed. A missing
   version string must not block the run.

### S2 - SHOULD (carry into the implementation) - Frame access and output folder

- Obtain the luma plane as a read-only NumPy view of plane 0 (stride handled by the VapourSynth Python
  API), and copy it to `int16` before differencing.
- Pass the output folder into the `.vpy` via `--arg`, as S2-I1 does for `src` and `idx`, rather than
  deriving it inside the script.
- Claude will verify both when the code arrives.

### O1 - OPTIONAL (owner request, 2026-10-15) - Split NONE by how it was copied, descriptive only

The owner asked for this to be added. The index already records the coding state, so the descriptive
report can split the NONE class at no extra cost:

```text
NONE-SKIPPED in P pictures   zero-motion copy by MPEG-2 definition: inherited edges on the grid,
                             not softened
NONE-SKIPPED in B pictures   reuses the previous MB's motion; may be averaged from two references
NONE-INTER with CBP 0        own motion vector; inherited edges may be off-grid and softened
```

Report each as its own descriptive class: the internal x=8 and mid-height positions, and the outer
edges by neighbour pairing. This is reporting only. It does not choose a NONE policy, which stays with
S2-I6, and it does not consume metadata for filtering (D-13 is unaffected). It gives S2-I6 the first
evidence on whether skipped-P blocks behave differently.

## 3. For the owner to ratify

**Before the formal run:** these thresholds are now final in the design:
- 3x3 contrast: >= 10% margin and a win in >= 2/3 of frames;
- column phase: >= 10% margin;
- row phase: q6/q7 top two, >= 5% margin and >= 2/3 of frames.

Ratify them together with the design.

## 4. Change log

### v0.1 - 2026-10-15

- First issue.
