# Claude verification of the S2-I2 v0.1 Windows acceptance run (v0.2)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: the owner's Windows run of the S2-I2 implementation candidate v0.1, cleared in `Claude_REVIEW_OF_ChatGPT_S2_I2_Implementation_v0_1_v0_1.md`
Evidence received: the console transcript, `git status --short`, and a ZIP of `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2` (no media; the `.m2v` had been deleted before zipping)

## 1. Verdict

**S2-I2 REGISTRATION GATE: PASS on both clips.** The windows run supports closing the S2-I2 gate.

| Clip | Gate | 3x3 / column / row | Seven known-bad offsets caught |
|---|---|---|---|
| LP (primary) | PASS | PASS / PASS / PASS | 7/7 |
| LP_blocky | PASS | PASS / PASS / PASS | 7/7 |

There are no findings against the run itself.

## 2. Was what ran what was reviewed?

Every identity below was checked:

| Item | SHA-256 recorded by the run | Matches |
|---|---|---|
| `stage2_registration_stats_v0_1.py` | 2f640f17ad600c9866455d73db17142dea6bd7025cd1e99a5fcb28e4679beb1c | the reviewed overlay |
| `stage2_registration_clip_v0_1.vpy` | 8a85aadc85ce6941c3467d444a1cb80c6c775ba2674c857fc659d687ed9e1e6b | the reviewed overlay |
| `stage2_index_reader_v0_2.py` | 139f02c64bbb86f21f62f06029db1fb976914f65e7a2cf20d49fce7515c126f6 | the committed S2-I1 file |
| `LG_576i_3_LP.mpg` | 521f43a2dac5257b2bce600956281f138033f358e558d6310f1f0916d808c7aa | the committed recording |
| `LG_576i_3_LP_blocky.mpg` | 6882d9001fa7cc187fe657cb5e22eedc243630f01f74af9f52cce652a6efd9f1 | the committed recording |
| `LG_576i_3_LP.idx` | 849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011 | the frozen baseline (certutil and the manifest agree) |
| `LG_576i_3_LP_blocky.idx` (scratch) | b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238 | the expected value; Claude re-hashed the returned file |

Runtime recorded by the vspipe preflight:

- VapourSynth R81 and Python 3.14.8 in the vspipe environment;
- NumPy 2.5.3;
- BestSource `PluginVersion(major=22, minor=0)`;
- BestSource plugin `libbestsource.dll`, SHA-256 fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c.

Note: the plugin exposes its version, so review finding O5 is withdrawn.

## 3. BestSource against Claude's FFmpeg rehearsal

The rehearsal ran the same statistics engine on FFmpeg-decoded frames. All eight CSV reports from the BestSource run are **byte-identical** to the rehearsal's, for both clips:

- `shifted_label_contrast.csv`
- `column_phase.csv`
- `row_phase.csv`
- `known_bad_offsets.csv`
- `seam_counts.csv`
- `boundary_detectability.csv`
- `frame_gop_uncertainty.csv`
- `outer_mb_edge_diagnostics.csv`

The `*_result.txt` files differ only in line endings (CRLF on Windows).

These byte-identical aggregate and per-frame statistics, across nine offsets and at full floating-point precision, are strong evidence that BestSource delivered the same luma as FFmpeg's rawvideo decode for every eligible frame of both clips. They are not a pixel-by-pixel comparison. They also indicate that the adapter's handling of plane 0 (native stride view, copy to int16) neither adds nor loses anything.

Every figure in sections 3 and 10 of the implementation review is therefore also the BestSource figure.

## 4. Structural checks in the logs

**LP_blocky preparation (`index_preflight.log`):**

- the index was built from a regular `.m2v` file, not a pipe, and the inspector exited with code 0;
- the reader confirmed the identity and the SHA-256;
- the frozen analyzer passed with `count_gate=PASS` and 204 frames;
- the totals are FIELD 33853, FRAME 54292, NONE 242335, with QP 62 throughout;
- the BestSource picture-type correspondence passed.

**Both runs:**

- the six-index S2-I1 regression passed;
- the vspipe preflight ran the 15 synthetic tests and all passed;
- the BestSource correspondence check passed;
- the eligible frame counts are 202 for LP (leading B frames 0 and 1 excluded) and 204 for LP_blocky.

## 5. Repository state

`git status --short` shows untracked files only. No tracked file was modified, and no BestSource cache file appears in the repository.

The untracked list mixes four kinds of item:

- the nine S2-I2 code files;
- review and design documents;
- package ZIPs;
- the `experiments/stage2/REPO_OVERLAY/` and `experiments/stage2/research/` folders.

The commit must therefore use **named staging** (`git add` with each file named), never `git add -A` or `git add experiments`. The file list is the owner's decision, to be settled with ChatGPT.

## 6. Carried forward (unchanged from the implementation review)

- **SHOULD S1-S4 and OPTIONAL O1-O4 and O6** go into the next versioned files. O5 is withdrawn (section 2).
- **Commit the v0.1 bytes exactly as run.** Do not convert their line endings before committing, because the run recorded their SHA-256 values.
- **Record the gate's limits in the S2-I2 results note:** the gate checks the spatial grid only; temporal correspondence comes from the picture-type checks; a field swap cannot be detected.
- **Leave the scratch LP_blocky index out of the repository.** It stays a non-baseline scratch file, and its SHA-256 is recorded above.

## 7. Change log

- v0.2 (2026-10-16): section 3 wording corrected. The identical statistics are strong evidence of identical luma, not a pixel-by-pixel proof. No other change.
- v0.1 (2026-10-15): initial verification.
