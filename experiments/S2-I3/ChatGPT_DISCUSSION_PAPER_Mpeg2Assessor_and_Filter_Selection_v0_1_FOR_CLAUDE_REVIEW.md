# DISCUSSION PAPER - Offline MPEG-2 assessment, representative sampling and adaptive deblocking choices

**Working filename:** `ChatGPT_DISCUSSION_PAPER_Mpeg2Assessor_and_Filter_Selection_v0_1_FOR_CLAUDE_REVIEW.md`  
**Version:** v0.1, 2026-10-18  
**State:** EXPLORATION ONLY; NOT an authority, agreed architecture, amendment to Stage 2, P1 implementation plan, or permission to edit the repository.  
**Authors/review roles:** ChatGPT initial discussion draft; Claude to provide independent technical review; both roles to reconcile findings through the project owner.  
**Owner's premise:** Unattended PC computation of up to roughly one or two days is affordable if the methodology is informative, reproducible, and largely automated. Do not impose artificial early pruning merely to save modest runtime.

## 0. Purpose, current conclusion, and bounds

This paper asks whether a distinct *Mpeg2Assessor* (working name) could characterise MPEG-2 blocking risk and recommend a filter policy after seeing enough evidence, without forcing the VapourSynth deblocker to decide solely from the current frame. Choices to compare include assessment from coded metadata, decoded pixels or both; one whole-recording policy, policies over temporal ranges, and spatially local decisions; and a single filter with selectable strengths, multiple genuinely different filters, or a continuous parameterised method. It also asks whether systematic automated P1 screening should be broadened.

**Current answer: worth investigating, not established to be worthwhile.** The project already has indexed transform geometry, an experimental pixel measurement engine, and a Python/BestSource environment. The open question is whether an offline policy recommendation beats a simpler index-driven locally adaptive filter, sufficiently to justify extra work, latency, metadata and deployment complexity. A credible result could also be *do not build an assessor*.

Hard bounds unless separately ratified: Stage 1 inspector and the six reference indexes remain frozen; no new `.idx2` commitment; S2-I3 P1 presently uses B0 (indexed transform geometry and fixed QP only for algorithm fitting and filtering), with real per-MB QP comparison deferred to S2-I4 and extra B1 coding-context use requiring its own decision. The eight admitted development encodes remain XP/SP/LP/3A, each original + `_blocky`; keep EP/2A/4A and copies locked until S2-I8; the new 6A/7A home captures have no experimental role. P1 has been explicitly authorised to begin, but its implementation approach is under discussion; this exploration does not authorise assessor code or alteration of a ratified experimental design.

### 0.1 Questions to bring back to the owner

- Does richer automated testing materially reduce the risk of overlooking a better filter, at a tolerable engineering/CPU cost?
- Can indexed bitstream evidence plus representative decoded pixels predict the *best safe treatment*, not simply the presence of compression?
- Is a source-wide choice sufficient? If not, are temporal sections a worthwhile intermediate point before spatial regions?
- Does any meaningful benefit require more than one filtering algorithm, or is one adaptive algorithm enough?
- Which stage should assess, where should policy data live, and what proof is needed before changing the inspector/index?

## 1. Source reality: the existing FFmpeg -> inspector pipe

**Correction of an earlier ChatGPT answer.** The active accepted Windows Stage 1 testing BATs pipe the elementary stream straight from FFmpeg into the inspector. A temporary `.m2v` elementary stream is NOT part of that accepted path. The earlier answer erroneously promoted a historical Linux short-read observation into a description of the current Windows workflow.

Verified against all seven `TESTING/TEST_Mpeg2BlockInspector*.BAT` members in the supplied repository source ZIP: each has the same execution pattern (LP shown generically):

```bat
"%path_ffmpeg%" -v error -i "%mpg_file%" -c:v copy -an -f mpeg2video - | "%path_Mpeg2BlockInspector%" -b - -m "%mpg_index%" >>"%mpg_log%" 2>&1
```

`%mpg_index%.s1tmp` is the *temporary binary index being built*, not a disk copy of the elementary stream. Windows accepted tests gave valid indexed/decoded correspondence and frozen-index hashes; for LP, the accepted reference index SHA-256 is `849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011`. The inspector's stdin binary handling matters. Pipe exit/failure accounting must be independently audited: a Windows CMD pipeline's reported errorlevel may not reliably convey failures in both constituent processes without suitable explicit checks.

Historical caveat, **not a reason to discard the pipe**: a Linux FFmpeg -> legacy decoder/inspector short-read test once marked a truncated index complete. The correct response in this project was exact output validation and exercising the actual Windows pipeline, not adopting a large `.m2v` as default. Any future changes must preserve all frozen acceptance tests.

**Distinguish three objects:** (1) the original `.mpg` file; (2) the non-seekable, single-use *piped elementary stream*; (3) the completed frame-owned binary index. The pipe cannot be rewound. If the original `.mpg` remains stored on disk, a *separate* read of that original file is possible and does not require a temporary `.m2v`; but whether another read/decoding pass is acceptable in the workflow is a design and benchmark question, not an assumption. A truly live or deleted source is different.

## 2. Important asymmetry: indexing versus assessing decoded pixels

Mpeg2BlockInspector currently parses compressed MPEG-2 syntax and produces indexing metadata. It does not itself receive an already decoded BestSource frame through the pipe. Full-stream metadata histograms can be computed cheaply during parsing or later from the completed `.idx`, but **visible blocking and collateral picture damage require decoded pixel evidence**. Knowing total frame count or selecting frame numbers does not itself supply those pixels.

Therefore, a recommendation made **at end of stream** is straightforward for metadata accumulated as we index, but a decoded-pixel severity recommendation needs an explicit acquisition path. Possibilities are below; the selection should turn on reliability and benchmark results.

| Path | Indexed stream | Pixel evidence | Extra I/O / engineering | Present judgment |
|---|---|---|---|---|
| A. Use completed `.idx` only | Existing piped pass; index later read by Python | None; infer coding-risk proxies only | Low; metadata does not measure visible blocking | Important inexpensive baseline, not sufficient proof of severity |
| B. Post-index BestSource on original `.mpg` | Keep the existing pipe unchanged | Sample decoded frames by index/display ordinal | Reopen original, random-seek or decode dependencies; no `.m2v` needed | Cleanest prototype **if** reopening source is acceptable |
| C. Concurrent decoder/assessor from original `.mpg` | Keep existing inspector pipe | Separate FFmpeg/BestSource reader samples/decodes | Two readers of original; synchronization, CPU/cache | Useful if single workflow required, but not one read |
| D. One FFmpeg invocation with dual outputs | ES pipe to inspector; decoded frames to another consumer | Pixel stream while video is ingested | Windows pipe multiplexing/named pipe/blocked output risk, ordinal alignment | Feasible in principle; substantial reliability engineering |
| E. Extend inspector/parser to assess | Modified frozen path | Would need additional decoding or a new pixel interface | Frozen-stage change, high verification burden | Not a starting point |
| F. Write temporary `.m2v` | Replayable ES | Still must separately decode selected pixels | Disk and cleanup costs, contrary to current choice | Fallback **only** if supported by measured necessity |
| G. Streaming online estimator with bounded state | Single nonseekable input | Only if decoded samples also available under D/E | Needs buffer/reservoir or per-frame summary computations | Research option for truly non-repeatable inputs |

**Technical questions:** Could FFmpeg emit ES to stdout and decoded luma concurrently without fragile Windows pipe handling? What are the exact frame-count, B-picture reordering and timestamp mappings between output streams? Does the best tested setup need one or two full decodes? Is an extra read of a file cheap enough that single-pass complexity is pointless? Do not assert any path is tested yet.

## 3. Pre-pipe MediaInfo 26.10 feasibility and metadata inventory

The owner's VapourSynth environment installation BAT is configured for `MIv=26.10`. It downloads a 64-bit `MediaInfo.dll` and `MediaInfo.exe`, and ships/copies `MediaInfoDLL.py` plus `MediaInfoDLL3.py` into VapourSynth-related folders. **The installation script proves the intended layout, not that any specific target PC currently has the exact binaries**, and the present author has not executed the DLL on the owner's recordings.

Up-to-date official documentation supports a file-opening/field-access API (MediaInfoDLL3.py `MediaInfo.Open(...)`, `Get(...)`, `Count_Get(...)`, `Close()`, `Option(...)`), and fields such as video `FrameCount`, `FrameRate`, `Duration`, `Width`, `Height`, `BitRate`, `BitRate_Mode`, `ScanType`, `ScanOrder`, `Format`, `Format_Profile`, `ChromaSubsampling`, `BitDepth`, `DisplayAspectRatio`, video count/stream identification, and general file/duration/container fields. **Availability, precision and reliability depend on the actual MPEG-PS recordings; do not presume any requested field is present.** Audio metadata could be logged for provenance but is not relevant to luma deblocking unless a concrete need emerges.

Potentially useful preflight categories:

| Data | Why it might help | Safeguard |
|---|---|---|
| Video stream count/codec/format | Pick the intended MPEG-2 stream, reject unexpected media | Do not silently select the wrong program/stream |
| `FrameCount` | Plan representative frame positions early | Estimate only; may be absent/inferred; validate against completed index and BestSource |
| `Duration`, `FrameRate`, frame-rate mode | Fallback estimate `N ~= duration * fps`; time-domain distribution | Check units and whether timestamps are discontinuous |
| Width/height, interlace/scan order | CPU/memory prediction; strata and parity expectations | Inspector/decoder remain authoritative for actual eligibility |
| Bitrate, bitrate mode, profile | Descriptive coarse encoding-context covariates | They are *not* visible blockiness or safe-strength labels |
| Format, chroma, bit-depth, aspect ratio | Validation, provenance, unsupported-format guards | Missing or conflicting fields are reported, not coerced |
| GOP/timecode-related fields, when present | Potential pilot stratification | Do not assume per-GOP detail or exact frame ordinals from MediaInfo |

MediaInfo is not a substitute for index quantiser and transform-state records and does not provide a verified per-seam severity label. MediaInfo's full decoding, if any, and file-parsing cost need benchmark; the wrapper should not cause a second unbounded media scan unexpectedly. MediaInfo 26.10 support is confirmed by the official Windows download page as of this drafting date; verify the installed DLL's actual version at execution time.

### 3.1 Proposed small read-only Python preflight (NOT yet authorised or implemented)

Candidate working name: `mi_mpeg2_preflight_v0_1.py`. Python 3, no media writes, no Git changes. Before the FFmpeg pipe, open the original `.mpg` via the installed 64-bit MediaInfo DLL/wrapper, collect raw value plus source/error/missing status for each declared field, close the handle, and print a deterministic JSON result. Record resolved interpreter, wrapper/DLL versions and backend availability. Detect isolated Python (`python314._pth`/`-I`) import behaviour; do not rely on `PYTHONPATH` to find sibling modules. If a DLL location must be added to the Windows DLL search path, do it explicitly and minimally, verify it, and leave global PATH untouched.

Order-of-magnitude frame-count logic, as a **hypothesis for testing**:

1. If plausible `FrameCount` exists, use it as an **estimated** pre-index count with its origin recorded.
2. Otherwise, if `Duration` and `FrameRate` are valid, compute a separately flagged duration-based estimate; preserve raw values and units, do not force an integer certainty.
3. Otherwise use `N_unknown`, with a streaming sampling option or postpone sampling decisions until the finished index count is known.
4. After the existing pipe completes and the index validates, compare predicted count with the actual index record count and the BestSource decoded count; report errors and disagreements. A disagreement must not be automatically "fixed" by changing a frozen index.

Use original `.mpg` paths for local execution only; committed text/JSON should not expose the owner's local directory, personal identity, or any captured media. Probe only an owner-authorised collection. Suggested dry-run schema:

```json
{
  "preflight_version": "v0.1",
  "source_label": "LP",
  "media_info_version": "observed-at-runtime",
  "video_stream_count": null,
  "frame_count_reported": null,
  "frame_count_estimate": null,
  "estimate_method": "unknown",
  "frame_rate_reported": null,
  "duration_reported": null,
  "other_fields": {},
  "warnings": []
}
```

All `null` values here are placeholders, not measured results. An initial pilot would check selected already-admitted original/_blocky files (at least contrasting XP, LP, 3A, plus SP), and report missing-field rates, count error, elapsed time and repeated-run consistency. A secondary reference could use FFprobe metadata; `ffprobe -count_frames` is a full read and must be labelled as such, not a cheap peek. The preflight should **not** be inserted into existing BATs until independently tested and authorised.

### 3.2 Known source points for review

- Existing Windows BAT pipeline: the seven `TESTING/TEST_Mpeg2BlockInspector*.BAT` files from the supplied repository source ZIP; LP test line 63 (source member representation).
- MediaInfo Python wrapper: https://github.com/MediaArea/MediaInfoLib/blob/master/Source/MediaInfoDLL/MediaInfoDLL3.py
- MediaInfo field catalogue: https://mediaarea.net/en/MediaInfo/Support/Fields (published catalogue may lag release; test against installed 26.10)
- MediaInfo Windows download listings: https://mediaarea.net/en/MediaInfo/Download/Windows
- FFprobe `-count_frames`: https://www.ffmpeg.org/ffprobe.html

## 4. Representative frame sampling - alternatives, not an adopted rule

**The actual pre-index count is unknown in general.** A stored MPEG-PS file's metadata may provide an estimate. A complete validated index later provides an exact number of output records. A streaming assessor may need to schedule samples before the last frame is known. A choice between these approaches belongs after pilot results.

| Sampling option | Benefits | Risks / questions |
|---|---|---|
| First 250 frames | Easy, cheap, immediate | Only ~10 seconds at 25 fps; unrepresentative of long recordings or changing quality |
| Every kth frame | Deterministic, easy online if count approximately known | Aliasing with GOP/scene/periodic structure; timing drift if estimated total wrong |
| Fixed percentage (1%, 5%, 10%) | Natural scaling with duration | Tiny clips under-sampled, very large clips over-sampled; unknown final count |
| Minimum/maximum capped temporal uniform sample | Bounds CPU; covers whole run | Need know/estimate duration ahead or sample after index/reopen |
| Stratified temporal bins with random jitter | Covers start/middle/end, avoids periodic alias | Bins based on estimated duration may leave late tail uncovered |
| Strata by index picture type / QP / transform mix | Includes rare coding regimes | Can oversample difficult cases; weight back to actual population; index may only be available after parse |
| Adaptive/anomaly-directed samples | Targets risky compression transitions | Not representative by themselves, cannot give unbiased source-wide prevalence |
| Online reservoir sampling | Uniform sample without knowing N | Requires retention of samples/compact features or an opportunity to revisit frames; storing full decoded frames may be costly |
| All frames / large sample | Strong calibration reference | Potentially large CPU; useful on short clips or limited pilot material |

A proposed, **not ratified**, reference comparison: full-frame or deliberately large-sample measurement on selected development sources; then 1%, 5%, 10% and capped/stratified strategies, all with fixed seeds and repeated draws. Judge *recommendation stability and consequential filter-output damage*, not merely agreement in average seam scores. Report I/P/B mix, frame/field state, scene diversity, time coverage, missing-tail problems, and confidence intervals reflecting temporal dependence. Ensure selection probabilities/weights are recorded and don't treat targeted extras as randomly sampled frames.

**One-pass difficulty:** an online sampler that has no decoded pixels cannot measure visible artifacts, however clever its choice of frame numbers. If a stream supplies decoded pixels and storage is bounded, compute compact frame-level seam-feature summaries for every frame and defer final classifier decisions until EOF; this may be cheap if feature extraction is vectorised but is no longer 'sampled frames only'. Alternative: keep a bounded random reservoir of actual frames (RAM/disk cost measured). If the original is reopenable, representative post-index sampling is simpler, not a rewind of the pipe.

## 5. What is being classified? Define the target before classifier design

"Better or worse than middling blocky" is a useful operational intuition, not yet a measurable definition. MPEG-2 QP, mode distribution and bitrate are **risk indicators**, not a direct measure of the visible seam artifact or the amount of safe filtering. Some severe QP is perceptually hidden by texture; some gentle compression shows strong bands on smooth regions. True source damage has no pristine reference for the LG originals; a flat edge may be real, not compression.

Candidate assessor outputs (no need for all):

- Estimated *visible coded-grid seam excess* relative to off-seam control, separated by horizontal/vertical seam geometry and FRAME/FIELD/NONE boundaries.
- Local activity/texture, edge preservation risk, noise level, oversmoothing susceptibility, spatial and temporal variability.
- Context strata (I/P/B, real/nominal QP, effective coded geometry, source mode), from existing index or MediaInfo where validated.
- Confidence and evidence coverage (how many independent temporal windows/sampled regions support recommendation, how stable across draws).
- **Recommended policy**, separately from the features and severity score; may be `OFF / unclassified` when evidence is weak.

A more useful learning target than a naked severity class may be **treatment utility**: for a given segment/source, which candidate achieves a worthwhile seam reduction at an acceptable local/no-harm and visual cost? That must be tested as an outcome; the initial score is not ground truth. Training a mapping using `_blocky` pairs alone would overfit artificial Q62 transcode artifacts. D-26 makes real recorder captures primary and `_blocky` paired-reference evidence secondary; no automatic numerical metric replaces blinded owner visual assessment.

## 6. Granularity of decisions - explicit option ladder

| Scope of classification | Recommendation | Upside | Main complexity/failure risk |
|---|---|---|---|
| **Whole source** | One chosen treatment for all eligible seams/frames | Minimal sidecar; offline whole-run statistics; stable | Mis-treats sections that vary strongly |
| **Temporal ranges/windows** | One treatment per contiguous frame-ordinal interval; e.g., scenes or GOP-bounded windows | Captures changing capture/compression quality; assessor can decide after EOF | Boundary flicker, short ranges, scene-vs-GOP mismatch, too little sample evidence per range |
| **Frame-by-frame** | Policy can change each picture | More responsive | Flicker, over-reacts, B/P/I shifts; loses offline stability benefit unless smoothed |
| **Spatial coarse regions/tiles** | Policy per macroblock group or larger tile | Addresses strongly uneven blocking within frame | Region boundaries, moving scene content, support/confidence and memory overhead |
| **Per-edge/seam local adaptive** | Choose strength/algorithm at each indexed seam | Most targeted; existing pixel tests may naturally work this way | Hardest protection/transition problem; cannot infer simply from clip-wide sample |
| **Hybrid** | Whole-run or temporal default; seam-local guarded corrections | Potentially good quality/complexity compromise | More parameters, interactions, difficult to attribute gains |

**Staged test, not a mandate:** compare source-wide first, then temporal ranges, *then* spatial regions only if the earlier data show clear unmet need. But retain the existing native per-seam adaptive baseline for fair comparison at every stage. The *complexity of assessing* a classification region must match its evidence coverage: a 1% clip-wide sample cannot reliably characterise every moving spatial tile. Define minimum interval/region size, per-region sample minimum, smoothing/hysteresis, exception policy and fallbacks before claiming spatial benefits. A sample-informed temporal policy map might use frame-ordinal boundaries and switching hysteresis; a `scene` is not necessarily the same as a codec GOP.

A display-order frame ID must be reconciled with decoder/index orientation, especially for B-pictures and leading B frames. Offline maps cannot refer casually to byte positions or chronological decoding order if the consumer requests frames by display ordinal. Prefer a separate, versioned policy sidecar for prototypes so the frozen index stays unchanged.

## 7. Number and kind of selectable filters - separate experimental axis

Do **not** infer "five filtering algorithms" merely from five strength labels. Options to compare:

| Treatment family | Meaning | Evidence required |
|---|---|---|
| 0. OFF/no correction | Mandatory safety comparator and permitted local policy | Bit-exact output on OFF |
| 1. One fixed kernel and manually selected global strength | Ratified starting approach (D-07) | S2-I3 baseline and owner visual/no-harm |
| 2. Same kernel, 2 to 5 discrete strengths | Severity gates pick intensity, not algorithm | Consistent monotone benefits, avoid band transitions |
| 3. One continuously parameterised adaptive kernel | Local variables modulate a common safe filter | Stability, saturations and no-harm compared to discrete strengths |
| 4. 2 to 5 genuinely different kernels/algorithms | Selection changes correction mechanism | Demonstrated complementary wins on independent source regimes |
| 5. Hybrid: global/temporal algorithm plus per-seam local strength | Coarse guidance + local protection | Actual gains over a native locally adaptive filter |
| 6. Mixture/cascade of methods | Multiple filters might act sequentially | Interaction damage, difficult validation, significant extra scope |

Count 2/3/5 only as *candidate configurations*, not predetermined targets. The all-off fallback is essential. Test whether stronger classification means *more filtering is safe*; non-monotonic cases may demand an alternative kernel or OFF instead. Filter switching at temporal/spatial boundaries must not create seams, ghosting, field-parity cross-contamination, or temporal flicker. Algorithm differences can be worth the complexity only if they surpass a comparably optimised single adaptive kernel.

### 7.1 Combination matrix for the joint exploration

| Assess scope | One fixed filter | One filter with 2-5 strengths | 2-5 distinct algorithms | Hybrid adaptive filter |
|---|---|---|---|---|
| Whole source | Required baseline | Plausible first experiment | Plausible, test complementarity | Compare to native local rules |
| Temporal ranges | Same as whole source unless adaptive parameters | Strong candidate if quality varies by section | Larger search; avoid switching artifacts | Promising but added complexity |
| Spatial tiles/regions | Little extra value | Expensive confidence/transition machinery | Most difficult; may be premature | Compare to per-seam pixel adaptive rules |
| Per seam | Usually native fixed kernel with local guards | Adaptive strength as pixel rule | High policy variability | Natural end state if evidence supports it |

This is a **conceptual design space**, not authority to implement each cell. The initial priority is to establish whether any offline assessment policy improves over the no-assessor baseline.

## 8. Comprehensive automation without unsound pruning

The owner welcomes long but unattended `.bat`/Python runs. That justifies broader experiments and suggests separating expensive feature acquisition from cheap candidate re-evaluation:

1. **Decode/index registration gate and immutable dataset manifest** (reuse accepted P0 guarantees, no hold-outs). Cache only permitted numeric features and bounded temporary working data.
2. **Feature pass:** every eligible individual M1..M5 plus M4a; F1..F3 and other candidate measures, across the complete training content in each fold; record separate strata. Do not equate seam-vs-off-seam discrimination with final benefit.
3. **Filter pass:** predeclared broad crossing of representative detection/protection/kernel/strength families, not solely top-ranked individual detectors. Include alternatives that may have interactions or source-specific advantages. Record which families were not exhaustively combined and why.
4. **Evaluation pass:** actual filtered outputs, seam reduction, collateral change, no-harm, edge/texture and field-parity damage, per-source and per-GOP/frame statistics, plus paired-reference movement for aligned `_blocky` pairs (not pristine ground truth).
5. **Grouped refit/assessment:** four leave-one-content-group-out folds, all O/X/J fitting arms with identical candidate budgets and exact train/test separation. Early elimination only where mechanically invalid or supported by relevant filtering evidence; preserve Pareto-incomparable variants.
6. **Possible assessor pass:** compare policy predictors from bitstream-only, pixel-only (at indexed seams) and combined features; source-wide vs temporal; one algorithm vs multiple. Use *out-of-training-content* policy comparisons, and keep S2-I8 locked.
7. **Human visual stage:** reproducible blinded/anonymous comparisons chosen by declared stratified sampling; owner assesses genuine edges/noise/motion/flat scenes/field parity. Automated score is not the ultimate arbiter.
8. **Report generator:** Python writes fixed-schema CSV/JSON and compact numeric summaries, including failed cases, candidate exclusions, confidence and reproducibility hashes. Derived visual media never inadvertently enters Git.

Potential engineering method: deterministic cache keys from media/index/config/code identities; stage checkpoints, serial `.bat` wrappers that verify paths/exit status and print useful progress; resumable independent jobs with explicit `.complete` markers written only after validation; no silent skip after errors. First benchmark a small reproducible workload to estimate total duration, RAM, scratch I/O and thermal throttling. Offline CPU cost is acceptable up to the owner's day-or-two preference, but systematic software QA cost and interpretability are still constraints.

**Current ratified limitation requiring explicit discussion:** S2-I3 v0.3 section 5 directs diagnostic screening and a shortlist of two or three combinations. A much broader expensive filter-search process, or adding offline adaptive assessment to P1, is **not already ratified**. A formal bounded design amendment would be needed if the joint review recommends changing that execution scope. Do not quietly treat the owner's exploratory interest as permission to redesign K0 or open S2-I8.

## 9. Data leakage, validity, and controls

- Preserve each original and `_blocky` encoding within one content group and hold the whole group out together, never leak pair pixels into fold tuning.
- For every O/X/J fold, the assessment features, candidate selection, thresholds, policy bands and recommendation-to-filter mapping must be learned on the three training content groups only. Apply frozen choices to the omitted fourth group. A retrospective winner picked using omitted-group results is optimistic.
- Predeclare comparison budgets/seeds/fold membership, all-source balance (four independent content groups; in J, 2:1 original:blocky within group), significance of real-recorder no-harm, and stable reporting. No p-values with four independent groups.
- MediaInfo metadata measured for a held-out clip is allowed at *deployment inference* if the procedure is explicitly designed to read such metadata, but its held-out quality outcomes must never tune the assessor in that fold. Raw bitstream acquisition is not the same as knowing the desired filter answer.
- Exact indexed seam geometry remains authoritative (D-24); pixel evidence may measure severity, **not replace it with a pixel-only grid detector**.
- Preserve luma/interlaced field-parity discipline; FRAME-DCT is not permission to mix temporally distinct fields. Current Stage 2 source material is mainly 576i; choma is out of S2-I3 P1 filtering scope.
- Stable source policy vs shifting: compare per-source global parameter choice, temporal switching with minimum segment length and hysteresis, and existing per-edge local guards. Measure both framewise quality and temporal flicker.
- Missing/ambiguous evidence should lead to a safe baseline/OFF or explicit INCONCLUSIVE, not arbitrary selection of the strongest filter.
- Do not generalise the 4 groups to the owner's entire archive: independently protected S2-I8 is the first later external-content check; extrapolation beyond that still requires more real-world diversity.
- Maintain provenance around QP > 62 and `q_scale_type`; table selector recovery is unconfirmed and not available as a new feature by assumption.

## 10. Implementation-language options (not predetermined)

**Python first:** a read-only MediaInfo preflight, experiment controller, deterministic sampling, NumPy seam feature extraction, candidate scoring, and CSV/JSON reports are suitable Python work. The owner already has VapourSynth R81/BestSource and relevant Python modules, though library/runtime availability must be tested on the current machine. The interpreter is isolated in some invocations: explicit local-module paths matter. Native VapourSynth plugin implementation is not required for this exploratory assessor.

**C++ only if evidence supports it:** if profiling shows per-pixel feature extraction or deployment time is materially costly, port narrowly measured kernels/feature code to C++ (potentially AVX2), retaining Python orchestration and reference outputs. A pure C++ assessor may simplify native packaging but increases development/verification cost. Runtime speed alone is not a reason to rewrite reliable Python that completes in an acceptable offline interval.

**Inspector integration later, if ever:** Stage 1 is frozen. A new executable called `Mpeg2Assessor` should initially be a *logical role* or Python module, not a second modified decoder. If the experiment succeeds, compare (i) standalone Python, (ii) Python + small native library, (iii) C++ executable consuming the existing index and/or original MPG, and (iv) a future change in production index layout. File naming, delivery and index metadata are Stage 3 decisions with their own ratification gates.

## 11. Proposed short research/pilot sequence - needs later owner authorisation

**R0 - review this paper only.** Claude verifies the actual pipe semantics, the ratified constraints and the MediaInfo 26.10 API; challenges assumptions and proposes the smallest useful tests. ChatGPT responds; the owner receives joint assessment, including disagreements. No code needed for R0.

**R1 - preflight pilot, if later authorised.** Run a tiny read-only MediaInfo/FFprobe metadata collection script against representative already permitted MPEG-2 MPG files. Compare count/geometry/field signals with accepted index and BestSource; measure runtime and missing fields. No destructive edits, no new `.m2v`.

**R2 - frame/pixel access and cost pilot, if later authorised.** For the actual Windows pipe plus original file, benchmark: after-index BestSource sampling without `.m2v`; separate concurrent decode; and, only if justified, a one-process dual-output design. Prove identical frame ordinal/luma against accepted P0, record time/I/O/memory/failure modes. Do not change Stage 1 or existing BATs.

**R3 - measurement stability pilot, if later authorised.** On a small, representative development subset and with correct fold restrictions, compare 1/5/10% sampling and capped/stratified plans to a high-coverage reference; determine what results are stable enough to guide filter choice. No new policy claims until output harm is tested.

**R4 - full adaptive-method evaluation, if warranted.** Compare one global kernel, several strengths, genuinely different kernels, per-source selection and temporal sections, plus the no-assessor locally adaptive baseline. Only then consider spatial regions or inspector/index integration. Any overlap with P1 candidate-search design requires amendment approval first.

*Stop criteria include: no robust superiority to baseline, instability between sampled draws, consistently wrong decisions on one original group, visible artifacts at policy transitions, unjustified index changes, or disproportionate engineering complexity. Positive evidence requires per-group and owner visual improvement, not only more sophisticated scoring.*

## 12. Requests for Claude's independent review (please address concretely)

1. **PIPE:** Inspect the actual accepted Windows BATs. Confirm the piped `-f mpeg2video - | ... -b -` path and distinguish `.s1tmp` index staging from temporary `.m2v`; audit CMD pipeline error detection and late EOF/truncation conditions.
2. **PIXEL AVAILABILITY:** Is any decoded-pixel evidence available from the current inspector parse at all? If not, which of paths B/C/D/G is practical on Windows x64 without materialising ES? Explain ordinal/parity and backpressure proof needs, rather than proposing an architecture without a data flow.
3. **MEDIAINFO:** Inspect the installed-wrapper source/API and 26.10 support. Which individual fields are likely in MPEG-PS vs ES, especially `FrameCount`, and which are merely duration-derived? Recommend exact read-only pilot fields, units, library load/isolated Python semantics, version logging, and fallback to FFprobe.
4. **SAMPLING:** Recommend a variable-length uniform/stratified sampling design with reliable handling of unknown estimated frame count. Can it work in one pass without retaining decoded frames, and when is a two-pass original-file read simpler? Compare statistical bias and compute costs.
5. **GRANULARITY:** Compare whole-source, temporal ranges/scenes, per-frame, spatial tiles and per-seam selection. What minimum sample evidence and temporal/hysteresis safeguards would make each defensible?
6. **FILTER POLICY:** Compare single filter with multiple discrete strengths, continuous adaptive filter, 2-5 truly different algorithms, and OFF/hybrid defaults. What data show complementarity rather than superficial apparent gains? How prevent overfitting?
7. **AUTOMATION:** How to run all eligible individual measures and a substantially broader candidate set reproducibly within a day-or-two target without screening away interactions? Suggest cached features, validation and status reports rather than new production code now.
8. **RATIFIED CONSTRAINTS:** Identify exact changes required to Stage 2 v0.7 / S2-I3 v0.3 / D-07, D-13, D-24 if any exploration becomes implementation. Do not silently amend them.
9. **RECOMMENDATION:** State separate assessments for technical feasibility, expected payoff, cost/complexity, testability and timing, including the explicit viable outcome of *do not build Mpeg2Assessor*. Mark agreement/disagreement with ChatGPT; do not escalate routine QA differences needlessly.

## 13. Areas where evidence is presently absent

- No measurements yet of MediaInfo 26.10 on the owner's actual full original MPG recordings in this session; `FrameCount` correctness cannot be asserted.
- No Windows benchmark comparing reopened original MPG versus concurrent or dual-output decode; no demonstration of a reliable decoded-pixel tee into the accepted inspector pipeline.
- No evidence yet that representative sampling at 1%, 5% or 10% is enough to choose a safe filter across long real-world sources, or that local temporal ranges improve quality.
- No demonstrated superiority of automatic severity classification over a manually set and locally guarded index-driven filter.
- No empirical proof that 2-5 distinct kernels outperform one well-tuned adaptive kernel; choice depends on the P1 filtering outcomes.
- No measured acceptable region size or switching hysteresis, especially for interlaced, moving, noisy home recordings.
- No permission from this paper to change the inspector, stream pipeline, binary index, frozen tests, development pool, or protected hold-outs.

## 14. Controlled conclusion and possible owner decisions later

Recommended **now**: commission R0 joint technical review; consider narrowly bounded MediaInfo + sampling feasibility pilots *after* the two roles agree on valid test methods and the owner authorises them. Keep existing direct Windows FFmpeg pipe intact. Retain both a simple no-assessor locally adaptive filter and an OFF baseline, with concrete opportunities for a negative feasibility outcome. Judge any multi-filter selection against *actual filtered-output quality and preservation*, not only severity-prediction scores.

**NO DECISION REQUESTED YET** on assessor implementation, extra scans, sample percentage, policy granularity, filter count, algorithm list, C++ conversion or index fields. This paper is a structured starting point for independent Claude review and subsequent ChatGPT/Claude reconciliation. The project owner makes any later ratification.

### Source pointers (document provenance, not superseding authority)

- Ratified `docs/REPOSITORY/Stage2_Experiment_Design_v0_7.md`: indexed geometry, K0, fixed-QP P1, full eight-source grouped development, sections 8.1-8.4, D-26 hierarchy.
- Ratified `docs/REPOSITORY/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md`: sections 4-8, especially four-fold grouped O/X/J, the 2:1 weighting in arm J, option inventory and B0-only initial rule.
- Ratified `docs/REPOSITORY/05_DECISIONS_v1_2.md`: D-07 strength evolution; D-09 field-owned; D-13 coding-metadata scope; D-23 versioned documents; D-24 index-driven seam geometry; D-26 evidence hierarchy.
- Source: `TESTING/TEST_Mpeg2BlockInspector_LP_2.BAT` and six peer BATs in the supplied repository source ZIP, independently pattern-checked for the direct ES pipe.
- Official MediaInfo and FFprobe links: section 3.2 above.
