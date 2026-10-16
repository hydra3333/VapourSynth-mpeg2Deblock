# Claude review of ChatGPT S2-I2 closure, commit proposal and S2-I3 entry plan (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: S2_I2_CLOSURE_AND_S2_I3_ENTRY_v0_1_FOR_CLAUDE_REVIEW.zip

The package contains five files:

- the review request;
- the SHA-256 manifest;
- `S2_I2_Results_and_Closure_Note_v0_1_FOR_CLAUDE_REVIEW.md`;
- `S2_I2_Exact_Named_Staging_and_Commit_Proposal_v0_1.md`;
- `S2_I3_Entry_Plan_v0_1_FOR_DISCUSSION.md`.

Checked against:

- the owner's Windows evidence ZIP;
- the ratified Stage 2 v0.6;
- `05_DECISIONS_v1_2.md` (D-07, D-09, D-10, D-12, D-13, D-23, D-24, D-26);
- `NOTICE.md`;
- the `.gitattributes` file at `4221f7f`;
- Claude's two earlier S2-I2 documents.

## 1. Verdicts

| Item | Verdict |
|---|---|
| Package integrity | All 4 manifest hashes match. All files are US-ASCII CRLF. No identity text. |
| A. Nine-file code commit | **CLEARED.** Run it as written, adding the hash command in section 3.1. No MUST. |
| B. Closure note | **Accept with SHOULD edits as v0.2.** No MUST. It is not cleared for installation as v0.1. |
| C. S2-I3 entry plan | **Accurate against Stage 2 v0.6.** Two SHOULD items and one OPTIONAL item for the S2-I3 design. It authorises nothing, correctly. |
| M4a | **Correctly represented** as a proposal, not the ratified M4. |

There are no MUST findings anywhere. Step A can proceed now; it does not depend on B or C.

## 2. Correction to Claude's own verification document

`Claude_VERIFICATION_OF_S2_I2_Windows_Run_v0_1.md` section 3 says BestSource "delivered exactly the same luma as FFmpeg" for every eligible frame. That overstates the evidence.

- The eight identical CSVs are aggregates and per-frame summaries over nine offsets, at full floating-point precision.
- That is very strong evidence of identical luma, but it is not a pixel-by-pixel comparison.

Claude has issued `Claude_VERIFICATION_OF_S2_I2_Windows_Run_v0_2.md`, which changes only that wording. Use v0.2 wherever the verification is cited or installed; v0.1 was never committed. The closure note's section 4 repeats the same overstatement (see B-S1).

## 3. A. Nine-file named staging: audit and rehearsal

**Rehearsal.** Claude rehearsed the exact procedure in a scratch Git repository made from the 4221f7f tree, with the real `.gitattributes` and `core.autocrlf false`:

1. **The nine paths and hashes** in the proposal's table match the reviewed candidate exactly, all 64 hex digits.
2. **The nine named `git add -- "<path>"` commands** produced exactly nine `A` entries, and nothing else was staged.
3. **`git diff --cached --check`** produced no output, exit code 0. Nothing in the nine files trips the whitespace check.
4. **`git ls-files --eol`** after staging gave:
   - both BATs: `i/lf  w/crlf  attr/text eol=crlf`;
   - the seven `.py`/`.vpy` files: `i/lf  w/lf  attr/`.
5. **Round trip.** After committing, `git archive --format=zip HEAD` (the mechanism behind GitHub's source ZIP) returned all nine files with exactly the reviewed SHA-256, including the CRLF BATs.

**SHOULD A-S1. The proposed blob check proves less than it claims.**

- The proposal suggests comparing `git hash-object` with `git rev-parse :path` "to ensure Git is storing exact working bytes". `git hash-object` applies the same attribute filters as `git add`, so the two always agree.
- For the BATs, Git deliberately does **not** store the working bytes. `.gitattributes` (`*.bat text eol=crlf`) stores them LF and restores CRLF on checkout and archive, exactly as for the S2-I1 BATs already in the repository.
- The meaningful guarantee is the round trip. Claude verifies it after the push by checking the SHA-256 of the nine files in the GitHub ZIP against the table.
- Replace the blob-check paragraph with the `git ls-files --eol` check and its expected output above. Neither check is a reason to stop the commit.

**OPTIONAL A-O1.** One read-only command hashes all nine files at once, instead of nine separate certutil commands (section 3.1). Staging stays strictly named, with no wildcards.

### 3.1 Owner command sequence for A (one block at a time)

```
cd /d "E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock"
```

```
git branch --show-current
```

```
git log -1 --format="%H %s"
```

```
git diff --cached --name-status --no-renames
```

The output must be empty. If anything is already staged, stop.

```
for %F in (experiments\stage2\S2_I2_*_v0_1.bat experiments\stage2\stage2_*_v0_1.py experiments\stage2\stage2_*_v0_1.vpy) do @certutil -hashfile "%F" SHA256 | findstr /v /c:"CertUtil"
```

Expect exactly nine hashes, each equal to the proposal's table. On any mismatch, stop.

The nine `git add` commands follow, one per block:

```
git add -- "experiments/stage2/S2_I2_prepare_LP_blocky_index_v0_1.bat"
```

```
git add -- "experiments/stage2/S2_I2_run_registration_v0_1.bat"
```

```
git add -- "experiments/stage2/stage2_check_result_v0_1.py"
```

```
git add -- "experiments/stage2/stage2_ffmpeg_rehearsal_v0_1.py"
```

```
git add -- "experiments/stage2/stage2_registration_clip_v0_1.vpy"
```

```
git add -- "experiments/stage2/stage2_registration_stats_v0_1.py"
```

```
git add -- "experiments/stage2/stage2_registration_tests_v0_1.py"
```

```
git add -- "experiments/stage2/stage2_validate_lp_blocky_v0_1.py"
```

```
git add -- "experiments/stage2/stage2_vspipe_env_preflight_v0_1.vpy"
```

Then check what is staged:

```
git diff --cached --name-status --no-renames
```

Expect exactly nine lines, all `A`.

```
git diff --cached --check
```

Expect no output.

```
git ls-files --eol -- experiments/stage2/S2_I2_*_v0_1.bat experiments/stage2/stage2_*_v0_1.py experiments/stage2/stage2_*_v0_1.vpy
```

Expect the BATs as `i/lf w/crlf attr/text eol=crlf` and the other seven as `i/lf w/lf attr/`.

Commit, check the result, then push:

```
git commit -m "Add accepted S2-I2 spatial registration diagnostics v0.1"
```

```
git show --format="%H %s" --name-status --no-renames HEAD
```

Expect exactly nine `A` lines.

```
git push
```

Then send the push output and the new GitHub source ZIP. Claude will check the nine file hashes and that the six frozen indexes are unchanged.

## 4. B. Closure note: findings

The closure note does several things correctly:

- it distinguishes the owner-ratified gate from the uncommitted code;
- it closes S2-I2, not Stage 2;
- it states that S2-I3 is NOT AUTHORISED;
- it keeps the scratch LP_blocky index non-baseline and out of Git;
- it records the limits faithfully, including the temporal-slip and field-swap cases;
- it carries O5 as withdrawn.

Claude rechecked the figures in its tables and they are correct:

- the 3x3 margins: 27.74% (LP) and 35.59% (LP_blocky);
- the frame fractions: 92.86% / 88.78% for 3x3, and 92.08% / 77.94% for the row phase;
- every SHA-256;
- the runtime versions.

**SHOULD B-S1. Soften the decoder-equivalence claim in section 4.**

- "This demonstrates corresponding decoded luma for every eligible frame" should become: "byte-identical aggregate and per-frame statistics across nine offsets are strong evidence that BestSource and FFmpeg delivered identical luma for every eligible frame; no pixel-by-pixel comparison was made".
- This is the same correction as section 2.

**SHOULD B-S2. Make the evidence durable.**

- The note's only evidence pointer for the numerical results is the `%TEMP%` folder and ZIP, which is neither permanent nor reviewable from GitHub.
- The run outputs are purely numerical and textual (logs, JSON, CSV, text), so under `NOTICE.md` lines 29-30 and Stage 2 v0.6 section 5 they are **not** Restricted Media. They total about 772 KB, excluding the `.idx`.
- **Recommendation:** in the separate document commit (step B), install them unchanged in a new folder, `experiments/stage2/results/S2_I2_v0_1/LP/` and `.../LP_blocky/`, with every file **except** `LG_576i_3_LP_blocky.idx`. List the SHA-256 values from Appendix A in the closure note.
- The LP_blocky logs and manifest contain the Windows temporary path `C:\Users\u\...`. "u" is not a name or a location, so this does not breach D-23; it is noted only for completeness.
- If the owner prefers not to track them, the closure note must instead say where the ZIP is retained outside `%TEMP%`.

**SHOULD B-S3. Placement and filename.**

- The Stage 1 precedent is `docs/REPOSITORY/Stage1_Evidence_and_Gate_Report_v0_3.md`.
- Use `docs/REPOSITORY/S2_I2_Evidence_and_Gate_Report_v0_1.md` (ratified content, renumbered v0.1 on installation), rather than "Results_and_Gate_Report". This keeps the gate-report family recognisable.
- The owner may choose otherwise; whatever is chosen, use it consistently in the status file.

**OPTIONAL B-O1.** In section 3, say that the "additional independent reviewer mutations" were run in Claude's Linux FFmpeg rehearsal, not in the Windows path.

**OPTIONAL B-O2.** In section 2, record that GitHub stores the BATs as LF and that checkout and archive restore CRLF (`.gitattributes`). The "exact bytes" claim refers to the checked-out and archived form.

**Placement of status and documents (step B).**

- One bounded document commit:
  - adds the ratified gate report;
  - adds the evidence folder;
  - adds Claude's two S2-I2 documents (the implementation review v0.1 and the verification v0.2) under `docs/`, next to the other review documents;
  - adds `00_PROJECT_STATUS_v0_6.md`, and removes `00_PROJECT_STATUS_v0_5.md` in the same commit (D-23).
- The status update should record:
  - the S2-I2 PASS and its ratification date;
  - the code commit SHA, once verified;
  - the LP_blocky S2-I2-only role and the row-phase test addition;
  - that S2-I3 is NOT AUTHORISED.
- Stage 2 v0.6 is **not** revised merely for this, as the note says. The row-phase test, LP_blocky's S2-I2 role and the S2-I8 census wording (C-S2) wait for its next substantive revision.
- The review packages, design drafts and ZIPs now untracked under `experiments/` are owner housekeeping, for a separate decision. Nothing should be deleted without the owner's direction.

## 5. C. S2-I3 entry plan: findings

Claude checked the plan against Stage 2 v0.6 sections 3.3, 8.4, 9.1 and 19, and D-07, D-09, D-10, D-12, D-13 and D-24. The following are all stated correctly:

- **GOP split:** the even/odd usable-GOP split, with GOPs as display-order runs from I to before the next I, numbered 0 from the first I after the leading-B exclusion.
- **Fixed QP:** median QP 18.
- **K0:** freeze K0 before S2-I4, with no retuning between variants.
- **Hold-outs:** EP, 4A original and 2A original stay locked.
- **LP_blocky:** no S2-I3 role by default.
- **B1:** coding-context boundary strength needs an owner decision beyond D-13, with B0 as the default.
- **Strength:** one manual strength (D-07).
- **Exclusions:** no Family B (D-24), and Family C optional and non-blocking (D-12).
- **Media:** Restricted Media handling.
- **Options:** the no-silent-deletion rule for options.

Claude computed the following from the frozen LP index:

| Population | Median QP |
|---|---:|
| All 204 frames, all macroblocks | 18 |
| Eligible frames only | 18 |
| Even usable GOPs only | 18 |
| Coded macroblocks only (FRAME/FIELD, NONE excluded) | **16** |

The GOP structure: 17 usable GOPs, each 12 frames except GOP 16 (10 frames). That gives 9 even GOPs (106 frames) and 8 odd GOPs (96 frames).

**SHOULD C-S1. Pin the Q_fixed population in the S2-I3 design.**

- Stage 2 v0.6 section 9.1 defines `Q_fixed` as the median effective per-macroblock QP of the clip. Its value of 18 comes from Stage 1 over all macroblocks, including NONE, whose QP is carried over and has no residual meaning.
- A coded-only reading gives 16 instead.
- The S2-I3 design should state the population explicitly: all macroblocks of the clip, per section 9.1, giving 18.
- It should also forbid re-deriving the value from a subset after results have been seen.

**SHOULD C-S2. Correct the S2-I8 wording (section 4F).**

- Stage 2 v0.6 defines S2-I8 as "locked hold-out generalisation / no-harm".
- The owner-requested all-16-source census was agreed in the review chats and the options table; it is not yet in v0.6.
- Suggested wording: "S2-I8 (locked hold-out generalisation / no-harm, Stage 2 v0.6) is also where the owner-requested all-16-source census is planned, after kernel and thresholds are frozen; record this in the next Stage 2 revision."

**OPTIONAL C-O1.** Put the GOP facts above (17 GOPs; even 9 / 106 frames; odd 8 / 96 frames) in the S2-I3 split manifest. The S2-I2 `frame_gop_uncertainty.csv` already carries the same GOP numbering and can serve as an independent cross-check of the split.

**M4a.**

- The plan defines M4a as "M4 numerator using adjacent slopes, denominator retaining the ratified in-block comparators". That matches Claude's variant exactly (per-field ratio, all macroblock columns: LP 47.0% / AUC 0.812, against ratified M4 23.79% / 0.754).
- The plan labels it a proposal and keeps the proxy-truth caveat.
- **Minimal revision:** Claude issues `Claude_S2_Seam_Pixel_Test_Options_Table_v0_3.md`. It is v0.2 with only an M4a row and a change-log entry added; nothing is removed.
  - v0.2 and v0.1 are currently untracked working files, not repository files. The owner decides whether the table belongs in `docs/` at step B. If it is installed, v0.3 replaces v0.2 under D-23.
  - Claude can draft v0.3 whenever the owner asks.

## 6. Recommended owner sequence

1. **Step A now:** run section 3.1, then send the push output and the GitHub ZIP for Claude to verify.
2. **ChatGPT revises the closure note to v0.2** (B-S1, B-S2, B-S3, plus the OPTIONAL items it accepts) and drafts `00_PROJECT_STATUS_v0_6.md`. Claude reviews both, the owner ratifies, and step B is one bounded document commit.
3. **S2-I3 stays NOT AUTHORISED** until the owner separately authorises the design only, deciding the LP_blocky role (default no) and B1 (default B0). C-S1 and C-S2 are folded into that design.

## Appendix A. Windows evidence hashes (as received, Windows bytes)

SHA-256 and size in bytes, for each file in the owner's `%TEMP%\VapourSynth-mpeg2Deblock_S2_I2` ZIP. The scratch `.idx` is excluded (its SHA-256 is b3f1d714...5238).

```
LP/S2_I2_LP.log                           6586  adc7b08696c569e18bb3117d9eea5319df760b9fc386e5d9129026800cf7481f
LP/S2_I2_LP_result.txt                     198  1dad6614ee86152d3c0c5614a17cfa16c3e447eacfb2c1e60f6d3ecb893d1818
LP/boundary_detectability.csv           116695  b602ffad8a69da3f656fcbca4471e87be4c959a74ba13449af65ccd1aaa84366
LP/column_phase.csv                       4016  87e07eef3c138eabefb6f877c649964a281b8ce503033ededdd1b176e8a9ac25
LP/frame_gop_uncertainty.csv             31211  301d0b12d5e35cdebc8a773bd6deada144a3d2b9dc0dfa8e9c1fb49f65e4a82e
LP/known_bad_offsets.csv                   233  60a48edba14dc7ac930dfed0e9dec9df6c1d833b55254622477c7f37dde20005
LP/outer_mb_edge_diagnostics.csv        428181  49a6da6a96d24aecda05e81492547b2f5807a82b4aacfcfde3ee3d7eba532f93
LP/row_phase.csv                          4905  764aac98903a0a34bd7bfb04f9b4a2042a2af683153c8558228d4a4fb3365864
LP/run_manifest.json                      6833  1c5def218fece7f6e774fdce45c7aa3001414d8fb3e4c693c0f4528895ce9673
LP/seam_counts.csv                         807  f189120e34680ff9cb7f93b69078bb30c93c6b5b0fa77bbf2cb97516b752f5c2
LP/shifted_label_contrast.csv             6234  b6ecd3c0e50b125861d1117f40e5014e8e95672acec0dd8301db86abc3ff14a5
LP/source_index_sha256.txt                 245  60d98ae84d1abb7bb7b34612fdf204dd7b0e4f8851e16156626987db3847b240
LP_blocky/S2_I2_LP_blocky.log             6736  b05306a640ec3ac1fd8e6a5edabc8538a698ecc818b72260d563a570faf998b1
LP_blocky/S2_I2_LP_blocky_result.txt       198  1dad6614ee86152d3c0c5614a17cfa16c3e447eacfb2c1e60f6d3ecb893d1818
LP_blocky/boundary_detectability.csv     46779  e7b562fe85b99f65c9c68135a7bbeaf4816c05736c0a883a03a281a5baf4410c
LP_blocky/column_phase.csv                5017  94da210a16f9869ce6dee19cfc8e4ac37c76247a15feda8ddd87884c2f442101
LP_blocky/frame_gop_uncertainty.csv      31451  246cee9d33292c058fa3e7958ab1595f76daae18fe602b4097eb87aa3066dd30
LP_blocky/index_preflight.log             2689  203c6062f73d5ab85cb1c8ad954023a91e58acf0663cb4f58cbee5be70f05c6c
LP_blocky/known_bad_offsets.csv            249  631e71ae7dc5e408bf8365aa08eb5aaf1d326ee632a16445bbf3e22254c855c6
LP_blocky/outer_mb_edge_diagnostics.csv  10190  e47c0da7b84e61950156c55405d12845da24bf35c43c82930cdd52dc73952666
LP_blocky/row_phase.csv                   4935  07f705f0dc4b8c1246736a144673ea17b9cfbf7f62b4c9961fc220e5551b08b2
LP_blocky/run_manifest.json               6823  d789d40277799ceb0328310edeaea63e597c06e131b0d3cb199d0d1d5c8d85c3
LP_blocky/seam_counts.csv                  809  12089e7f8345d72cd81997ba123586e3f4fa7066290fe7f06b2ba29a3bcdfadc
LP_blocky/shifted_label_contrast.csv      6145  64d8676fb0af06d9b7f73d4a5f56605ef56c65d47130fa4068913a6cf9e928ee
LP_blocky/source_index_sha256.txt          231  f9232c0315c4ed7a2bb93695a8aeac631f10e01ff07cc96e6b6f6a9759ee5e79
```

Git may store and archive these files with different line endings, depending on `core.autocrlf`; per D-23, hashes refer to the representation named. The CSV files are CRLF as written by Python on both platforms.
