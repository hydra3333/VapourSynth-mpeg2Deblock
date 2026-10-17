# Claude analysis: paired original/blocky reference metric, and the new 17/10/2026 samples (v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Author: Claude
Prompted by: the project owner's query of 17/10/2026
Baseline: `35cd543b459a5856688f7c3795f73226e72311f8`

## 1. Summary

Two separate matters.

**A. The paired original/blocky reference.** Yes, and it is already the ratified basis: the whole purpose of the P0 pair-correspondence proof is to make exactly this legitimate. Claude has now measured it on all four development pairs, and the measurement changes what the metric should be:

- **global MAE toward the original is a weak objective.** Only about 9% of the blocky-versus-original error sits at block boundaries. The rest is detail destroyed by quantisation, which no deblocker can restore. The best crude edge-constrained filter Claude tried gained 1-2%.
- **a no-reference blockiness index is a strong objective.** Boundary discontinuity excess separates original from blocky by roughly 1.4x to 2x on every pair.
- **recommended pairing:** drive the blockiness index toward the original's own level, with paired MAE to the original as a do-no-harm fidelity guard that must not worsen. Details in section 3.

**B. The new samples.** One MUST finding.

- **Four of the six new pairs are not new content.** TEST_1A, TEST_8A, TEST_9A and TEST_10A are byte-size-identical to existing XP, MLS, EP and LP, and their filenames embed those stems. Admitting them as sources would leak the EP hold-out and the MLS control into development, and would double-count XP and LP in the cross-validation folds.
- **Two of the six are genuinely new:** TEST_6A_home_576i and TEST_7A_home_576i. These are valuable, being different in provenance from the LG and TEST_nA sets. They need Stage-1 characterisation, a privacy decision, and a bounded design revision before use.

**C. Sequencing recommendation.** Run P0 on the ratified eight sources as already cleared, once M1 from the P0 review is fixed. Handle the new material as a separate increment afterwards. P0 is fail-closed against the new filenames, so there is no risk in proceeding (section 6).

## 2. MUST

**M1. Four of the six new pairs appear to be copies of existing samples, two of them protected.**

Every one of the eight files matches an existing sample's size exactly, and the name contains the original stem:

| New file | Bytes | Identical size to |
|---|---|---|
| TEST_1A_LG_576i_1_XP.mpg | 3,575,808 | LG_576i_1_XP.mpg |
| TEST_1A_LG_576i_1_XP_blocky.mpg | 1,556,480 | LG_576i_1_XP_blocky.mpg |
| TEST_8A_LG_576i_5_MLS.mpg | 1,751,040 | LG_576i_5_MLS.mpg |
| TEST_8A_LG_576i_5_MLS_blocky.mpg | 1,292,288 | LG_576i_5_MLS_blocky.mpg |
| TEST_9A_LG_576i_4_EP.mpg | 2,191,360 | LG_576i_4_EP.mpg |
| TEST_9A_LG_576i_4_EP_blocky.mpg | 1,124,352 | LG_576i_4_EP_blocky.mpg |
| TEST_10A_LG_576i_3_LP.mpg | 2,932,736 | LG_576i_3_LP.mpg |
| TEST_10A_LG_576i_3_LP_blocky.mpg | 1,509,376 | LG_576i_3_LP_blocky.mpg |

Only TEST_6A_home_576i and TEST_7A_home_576i, with their `_blocky` copies, have sizes matching nothing in the existing set.

**Why this matters.** Protection and fold membership follow the *content*, not the filename.

- **TEST_9A is EP.** EP is a hold-out, locked until S2-I8. Admitting TEST_9A as a development source would destroy the hold-out, and no later analysis could undo that.
- **TEST_8A is MLS.** MLS is a designated control pair, not a development source.
- **TEST_1A is XP and TEST_10A is LP.** Both are already development sources. Admitting them again under new names would place the same content in two different content groups, so leave-one-content-group-out cross-validation would train and test on the same material. That is precisely the selection optimism the ratified design guards against.

**Required action.** Confirm by hash before anything else, with the single command block in section 7. Then, depending on the result:

- **If they are exact copies, which Claude expects:** treat them as aliases, not sources. The clean resolution is to pick one naming scheme and *rename*, rather than keep two names for one clip. The hold-out and control status must travel with the content: whatever EP is called, it stays locked until S2-I8, and whatever MLS is called, it stays a control.
- **If any hash differs:** that pair is new content and needs the same treatment as TEST_6A and TEST_7A.

**Observation on the naming scheme.** The numbering suggests a unified `TEST_nA_` scheme over the whole sample set: 1A=XP, 2A, 3A, 4A, 6A and 7A new, 8A=MLS, 9A=EP, 10A=LP. **5A is missing, and LG_576i_2_SP has no TEST_nA_ counterpart.** If a complete renaming is intended, SP is the gap.

## 3. The paired original/blocky reference

### 3.1 It is already the design basis

The pair-correspondence proof in P0 exists so that paired-reference metrics are defensible. Stage 2 v0.7 section 15 already provides for them, and the four pairs all PASS, with zero decisive-frame violations. So frame N of the blocky encode is now proven to correspond to frame N of the original. The reference is sound.

### 3.2 What Claude measured

All four development pairs, all frames, FFmpeg/BestSource on Linux, luma plane, media deleted afterwards.

**Baseline error, and where it sits.** "Boundary" means pixels adjacent to an 8-pixel DCT block edge; "interior" is the rest.

| Pair | MAE all | MAE boundary | MAE interior |
|---|---|---|---|
| XP | 3.567 | 3.745 | 3.428 |
| SP | 3.266 | 3.436 | 3.134 |
| LP | 4.355 | 4.588 | 4.173 |
| 3A | 5.512 | 5.748 | 5.329 |

Boundary error exceeds interior error by only **7 to 10%**. The overwhelming majority of the blocky-versus-original difference is not blocking at all: it is detail the Q62 encode discarded, and a deblocker cannot put it back.

**Consequence.** Global MAE or PSNR toward the original is dominated by irrecoverable error. Using it as the optimisation target means chasing a signal diluted roughly ten to one.

**What crude filters achieve** (change in global MAE against the blocky baseline, and the damage the same filter does to the *clean* original):

| Pair | h-blur at vertical edges | field v-blur at within-field edges | both | naive FRAME v-blur | harm to original, naive |
|---|---|---|---|---|---|
| XP | +1.2% | -1.2% | -0.2% | -12.3% | 1.092 |
| SP | +1.3% | -0.3% | +0.8% | -26.8% | 1.557 |
| LP | -0.2% | -3.8% | -4.1% | -7.5% | 1.051 |
| 3A | +2.3% | -4.7% | -2.9% | -20.3% | 2.244 |

Two things follow.

- **The metric is not easily gamed.** A blur does not quietly improve it; mostly it makes things worse. That is reassuring for the metric's integrity.
- **But the usable range is tiny.** The best crude result is +2.3%. Distinguishing a good filter from a mediocre one on this measure will be hard.

**The blockiness index, by contrast, separates cleanly.** This is a no-reference measure: the mean absolute pixel step across 8-pixel block edges, minus the mean step away from them, computed field-aware in the vertical direction.

| Pair | H excess, original | H excess, blocky | V excess, original | V excess, blocky |
|---|---|---|---|---|
| XP | 1.614 | 2.313 | 1.011 | 2.145 |
| SP | 1.950 | 2.816 | 1.472 | 2.879 |
| LP | 2.319 | 3.169 | 1.189 | 2.221 |
| 3A | 1.726 | 3.352 | 3.715 | 6.197 |

Every pair separates, vertically by roughly a factor of two. **This is the strong signal.**

### 3.3 Recommended metric set

**Primary objective.** Move the blocky clip's blockiness excess toward the original clip's own value, measured separately for horizontal and vertical, and field-aware vertically. The original's value is the realistic target: the original is itself an MPEG-2 encode at Q 14-18, so it has its own mild blocking. Zero is not the goal, and "100% recovery" is not a meaningful claim.

**Fidelity guard, must not worsen.** Paired MAE to the original, reported globally and split boundary versus interior. A filter that improves the blockiness index while worsening interior MAE is destroying detail, and the split makes that visible.

**Do-no-harm arm.** Run the filter on the *original* clip and measure the damage against itself. This is already the ratified O arm, and the table above shows why it matters: the naive frame blur damages a clean clip by up to 2.244 MAE, which is comparable to a large part of the entire blocky-versus-original baseline.

**Use the difference form, not the ratio.** Claude also computed the boundary-to-interior *ratio*. It is unusable: on LP_blocky it is infinite, because at Q62 the block interiors are perfectly flat, so the denominator is zero. Other blocky clips gave 69.0 and 10.9. The difference (excess) form is stable; the ratio must not be used as a gate.

### 3.4 Interlace is the dominant trap

This is the clearest result of the whole exercise. The naive frame-based vertical blur loses 7.5% to 26.8% of MAE and damages the clean original badly, because on 576i content adjacent frame lines belong to *different fields*, that is to different moments in time. Any vertical filtering must be constrained within a field, or driven by the per-macroblock FRAME versus FIELD transform flag.

That flag is exactly what the index records, which is the project's whole premise. The measurement is independent confirmation that the index-driven approach is addressing the real problem, and that a naive spatial deblocker would be actively harmful here.

### 3.5 A breadth gap worth raising

**Every `_blocky` encode in the pool is Q62.** That is a single, extreme operating point, and the index-interior flatness confirms how extreme: on LP_blocky the block interiors are perfectly flat. Real-world VHS captures will show far milder blocking.

A filter fitted only at Q62 may not transfer. Consistent with the stated preference not to develop against one kind of input, consider adding intermediate-QP encodes, perhaps around Q 25 to 40, of the existing content. This is cheap, since it reuses source material already in hand, and it would give the fit a QP range rather than one point. S2-I4's two QP estimands are the natural home for this.

This is a suggestion for ChatGPT and the owner to weigh, not a finding against the current design.

## 4. The two genuinely new pairs

TEST_6A_home_576i and TEST_7A_home_576i are the valuable additions. They are also much longer than anything in the pool: 20.5 MB and 12.4 MB against roughly 3 MB, so expect several times the frame count.

**Before they can be used:**

1. **A privacy decision, and it comes first.** The name indicates personal home footage. The existing `VHSC_samples/*.mpg` files are tracked in the public GitHub repository. Committing personal home recordings to a public repository is a different proposition from committing test captures: faces, interiors, voices and incidental speech can all identify people, which cuts directly against the standing instruction that nothing uploaded to GitHub identifies the owner. **Claude's recommendation is not to commit the `.mpg` files.** The `.idx` files are a different matter and are safe: they hold macroblock metadata only, with no pixel data and no paths, and the only readable text is the magic `S1MBIDX1`. So the indexes can be tracked even if the media is not.
2. **Stage-1 characterisation.** Generate indexes with the frozen inspector, then run the analyzer summary: frame count, dimensions, macroblock grid alignment, picture structure, chroma format, and the Q histogram for Q_fixed as the all-macroblock median. Watch for the MLS_blocky trap, where the blocky copy turned out to be 352x288 with `progressive_frame=0`. Verify that each new pair's two encodes agree in frame count and geometry before anything else.
3. **Independent verification, which needs a decision.** For the committed samples Claude can regenerate an index from the repository media and check the hash independently. For media that is never committed, Claude cannot. To keep the project's independent-verification standard, the clean path is to attach the four files here when we reach that step, under the existing development-period AI media authorisation, so Claude can verify and then delete them, as with every previous rehearsal. The alternative is to record those index hashes as owner-attested only, with the gap noted in the evidence.
4. **A bounded design revision.** Adding development sources changes the folds, so it is a Stage 2 v0.8 and S2-I3 v0.4 matter, not something to slip into P0. The questions for that revision are whether the new groups join development, which would take the leave-one-content-group-out scheme from four groups to six, or serve as additional evaluation-only sources; and how the 2:1 original-to-blocky weighting applies to much longer clips, since a clip several times longer would otherwise dominate a per-frame fit. Claude's recommendation, given the stated preference for breadth, is full development groups, subject to characterisation, with per-group weighting normalised by frame count so that length does not become influence.

**Extending the code is cheap.** The admission allow-list in `stage2_i3_preflight_verdict_v0_1.py` is pure data: a label, stem, index SHA, frame count, geometry and reference skip count per source. Adding sources is a v0_2 of that one file plus new hashes. No logic changes.

## 5. What this does not change

- The P0 review verdict stands: one MUST, the one-line BAT fix in `S2_I3_P0D_diagnostics_v0_1.bat` line 37, plus S1 to S3.
- No ratified criterion, threshold, fold or hold-out changes as a result of this analysis. Section 3 recommends a metric set for S2-I4 and later; it does not alter S2-I3, which is registration and admission only.
- EP, 2A and 4A, with their `_blocky` copies, stay locked until S2-I8 under whatever name they appear.

## 6. P0 is fail-closed against the new filenames

Claude verified this directly. The admission allow-list contains only the eight ratified labels, `argparse` rejects any other label, and both the admission and diagnostic scripts require the source basename to equal the allow-listed stem exactly. Attempts to pass `EP` or `4A_blocky` are refused with a non-zero exit. A stray `TEST_9A_LG_576i_4_EP.mpg` in `VHSC_samples/` therefore cannot be admitted by accident, and P0 will not read it.

So the new files do not block the P0 run. They do need resolving before any of them is used, and before the seven-index tracking commit, so that no duplicate content enters the repository under a second name.

## 7. Verification command for the owner

One block. It writes nothing, and prints one line per distinct content hash, listing every filename that shares it. Any line containing `==` is a duplicate-content group.

```
cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"
```

```
powershell -NoProfile -Command "Get-ChildItem 'VHSC_samples\*.mpg' | Get-FileHash -Algorithm SHA256 | Group-Object Hash | ForEach-Object { $_.Name.Substring(0,16) + '  ' + (($_.Group | ForEach-Object { Split-Path $_.Path -Leaf }) -join '  ==  ') }"
```

Paste the output back. Claude will confirm the duplicate set and, for TEST_6A and TEST_7A, record the hashes as the starting point for characterisation.

## 8. Recommended order

1. Run the hash check in section 7, and settle the duplicate and naming question.
2. ChatGPT fixes P0 M1, plus S1 to S3. Claude diff-checks.
3. The owner runs P0 on the ratified eight. Claude reviews the evidence.
4. The seven-index tracking commit, with the naming question already settled so no duplicate content is tracked.
5. Separately: the privacy decision on the home media, then characterisation of TEST_6A and TEST_7A, then a Stage 2 v0.8 and S2-I3 v0.4 revision covering the new groups, the metric set in section 3, and the intermediate-QP suggestion in section 3.5.

Steps 2 to 4 and step 5 are independent. Neither needs to wait for the other, beyond step 1.
