# S2-I2 Step B - exact proposed placement and disposition inventory

**Version:** 0.2, 2026-10-16  
**Status:** FOR CLAUDE REVIEW AND OWNER DECISION; **not an instruction to stage or commit yet**.  
**Working-tree basis:** the owner's two consecutive housekeeping reports, including the *post-unpack* state of `experiments/stage2/results/S2_I2_v0_1/`; the current Windows working tree was not available to this author for a fresh `git status`.  
**Code commit COMPLETED:** `190bd06ded88130ffddac7bb9adde4175d82f9f8` (parent `2286341`), pushed; Claude checked GitHub source ZIP, nine reviewed code hashes and six immutable accepted indexes. No re-commit.  
**Gating source:** Claude closure/commit review v0.1, Windows verification v0.2, and the owner-provided Claude closure-note-v0.2 review summary (M1/S1-S3).  

## 1. Proposed Step-B boundary

Only one documentation/evidence commit is proposed. No source-code modification, S2-I2 rerun, new `LP_blocky.idx` baseline, Stage 2 v0.6 edit, or S2-I3 implementation. Preserve the **nine accepted code files already committed** at `190bd06` exactly as tested; do not restage them under Step B.

With the recommended evidence-only `.gitattributes` pin, the maximal proposal is **40 additions, one modification and one deletion**: 12 already-moved docs, one conditional Copilot source after identity/NOTICE/quotation clearance, 25 evidence files, the gate report and status v0.6; modify existing root `.gitattributes`; remove status v0.5. If the research source is held back: **39 additions, one modification, one deletion**. These counts are *proposals*, not observed staged results. If the pin is declined, subtract the `.gitattributes` modification and use separate Git/GitHub evidence SHA values rather than Windows hashes.

**Blocking prerequisites before staging:** (i) Claude scans the Copilot research file for identity and material/rights issues; (ii) Claude reviews the revised closure note v0.2, converted to the installed filename after owner approval; (iii) draft Project Status v0.6 **from the ratified repository v0.5 file in the owner's actual HEAD**, not from the older v0.5 working draft in ChatGPT; (iv) record and verify the full code-commit SHA and code/evidence placement; (v) obtain owner ratification of the Step-B contents.

## 2. Files already moved to `docs/` - 12 exact proposed tracked paths

These are the twelve items counted in the owner's message, *not* twelve files to move a second time. Retain their current source bytes/filenames, stage each path explicitly after confirmation, and use `docs/` root (consistent with existing review-document precedent). They are historical/review/option records, not competing ratified repository authorities:

1. `docs/ChatGPT_S2_I2_Design_Plan_v0_4_FOR_CLAUDE_REVIEW.md`
2. `docs/Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_2_v0_1.md`
3. `docs/Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_3_v0_1.md`
4. `docs/Claude_REVIEW_OF_ChatGPT_S2_I2_Design_Plan_v0_4_v0_1.md`
5. `docs/Claude_REVIEW_OF_ChatGPT_S2_I2_Implementation_v0_1_v0_1.md`
6. `docs/Claude_REVIEW_OF_ChatGPT_S2_I2_Closure_Commit_and_S2_I3_Entry_v0_1_v0_1.md`
7. `docs/Claude_VERIFICATION_OF_S2_I2_Windows_Run_v0_2.md`
8. `docs/Claude_S2_Seam_Pixel_Test_Options_Table_v0_2.md`
9. `docs/ChatGPT_Review_of_Copilot_Grok_MPEG2_Block_Detection_v0_1_FOR_CLAUDE.md`
10. `docs/Claude_REVIEW_OF_ChatGPT_Copilot_Grok_Block_Detection_Assessment_v0_1.md`
11. `docs/S2_I2_v0_3_CHANGE_TRACEABILITY.md`
12. `docs/S2_I2_v0_4_CHANGE_TRACEABILITY.md`

**Scope note:** `ChatGPT_S2_I2_Design_Plan_v0_4_FOR_CLAUDE_REVIEW.md` is the historical text subsequently ratified by the owner; its filename need not be changed to assert that the text was ratified. `Claude_S2_Seam_Pixel_Test_Options_Table_v0_2.md` is the current review table, not an S2-I3 decision. When Claude later issues the v0.3 options table containing M4a, apply D-23 supersession rather than retaining both as competing current options. Do not silently insert M4a into v0.2.

## 3. Copilot research source - 13th `docs/` item, conditionally included

- Proposed: `docs/COPILOT-MPEG2_Deblocking_VHS_DVD_Research.md`.
- **Status: HOLD**, pending Claude's identity scan and review for NOTICE/Restricted Media and source-quotation/rights concerns. A scan result must come **before** any `git add` for this file; its current untracked presence in `docs/` is not itself an approval.
- If it fails or is not yet cleared, leave it untracked and make an explicit note in the Step-B commit review. Do not scrub, rewrite, remove or commit it without owner instruction.

## 4. Persistent numerical evidence - exact proposed paths

Evidence root: `experiments/stage2/results/S2_I2_v0_1/`. The user has **already** unpacked it there from `Z/`; do not extract a duplicate overlay. The evidence ZIP SHA-256 independently checked here is:

`0bce902275a2e7533fb0685788bcbf3ef2c0a173b344866ed4a0f757d02c34d6`

All **25** listed payload files were independently checked byte-for-byte against that ZIP and Claude's Appendix A (file sizes and full hashes). The ZIP contains one *additional* `LP_blocky.idx`, correctly **excluded** from this installation. **Important:** with owner `core.autocrlf=true`, Claude reports 25/25 GitHub-form evidence hashes mismatch their original Windows hashes without a new `.gitattributes` pin; some logs mix LF/CRLF and cannot be reconstructed after conversion. Its rehearsal with the scoped `experiments/stage2/results/** -text` pin had 0/25 mismatches. Verify current working-tree hashes and post-push GitHub hashes; the pin requires owner approval.

| Relative path beneath evidence root | Bytes | SHA-256 (original Windows bytes) |
|---|---:|---|
| `LP/S2_I2_LP.log` | 6,586 | `adc7b08696c569e18bb3117d9eea5319df760b9fc386e5d9129026800cf7481f` |
| `LP/S2_I2_LP_result.txt` | 198 | `1dad6614ee86152d3c0c5614a17cfa16c3e447eacfb2c1e60f6d3ecb893d1818` |
| `LP/boundary_detectability.csv` | 116,695 | `b602ffad8a69da3f656fcbca4471e87be4c959a74ba13449af65ccd1aaa84366` |
| `LP/column_phase.csv` | 4,016 | `87e07eef3c138eabefb6f877c649964a281b8ce503033ededdd1b176e8a9ac25` |
| `LP/frame_gop_uncertainty.csv` | 31,211 | `301d0b12d5e35cdebc8a773bd6deada144a3d2b9dc0dfa8e9c1fb49f65e4a82e` |
| `LP/known_bad_offsets.csv` | 233 | `60a48edba14dc7ac930dfed0e9dec9df6c1d833b55254622477c7f37dde20005` |
| `LP/outer_mb_edge_diagnostics.csv` | 428,181 | `49a6da6a96d24aecda05e81492547b2f5807a82b4aacfcfde3ee3d7eba532f93` |
| `LP/row_phase.csv` | 4,905 | `764aac98903a0a34bd7bfb04f9b4a2042a2af683153c8558228d4a4fb3365864` |
| `LP/run_manifest.json` | 6,833 | `1c5def218fece7f6e774fdce45c7aa3001414d8fb3e4c693c0f4528895ce9673` |
| `LP/seam_counts.csv` | 807 | `f189120e34680ff9cb7f93b69078bb30c93c6b5b0fa77bbf2cb97516b752f5c2` |
| `LP/shifted_label_contrast.csv` | 6,234 | `b6ecd3c0e50b125861d1117f40e5014e8e95672acec0dd8301db86abc3ff14a5` |
| `LP/source_index_sha256.txt` | 245 | `60d98ae84d1abb7bb7b34612fdf204dd7b0e4f8851e16156626987db3847b240` |
| `LP_blocky/S2_I2_LP_blocky.log` | 6,736 | `b05306a640ec3ac1fd8e6a5edabc8538a698ecc818b72260d563a570faf998b1` |
| `LP_blocky/S2_I2_LP_blocky_result.txt` | 198 | `1dad6614ee86152d3c0c5614a17cfa16c3e447eacfb2c1e60f6d3ecb893d1818` |
| `LP_blocky/boundary_detectability.csv` | 46,779 | `e7b562fe85b99f65c9c68135a7bbeaf4816c05736c0a883a03a281a5baf4410c` |
| `LP_blocky/column_phase.csv` | 5,017 | `94da210a16f9869ce6dee19cfc8e4ac37c76247a15feda8ddd87884c2f442101` |
| `LP_blocky/frame_gop_uncertainty.csv` | 31,451 | `246cee9d33292c058fa3e7958ab1595f76daae18fe602b4097eb87aa3066dd30` |
| `LP_blocky/index_preflight.log` | 2,689 | `203c6062f73d5ab85cb1c8ad954023a91e58acf0663cb4f58cbee5be70f05c6c` |
| `LP_blocky/known_bad_offsets.csv` | 249 | `631e71ae7dc5e408bf8365aa08eb5aaf1d326ee632a16445bbf3e22254c855c6` |
| `LP_blocky/outer_mb_edge_diagnostics.csv` | 10,190 | `e47c0da7b84e61950156c55405d12845da24bf35c43c82930cdd52dc73952666` |
| `LP_blocky/row_phase.csv` | 4,935 | `07f705f0dc4b8c1246736a144673ea17b9cfbf7f62b4c9961fc220e5551b08b2` |
| `LP_blocky/run_manifest.json` | 6,823 | `d789d40277799ceb0328310edeaea63e597c06e131b0d3cb199d0d1d5c8d85c3` |
| `LP_blocky/seam_counts.csv` | 809 | `12089e7f8345d72cd81997ba123586e3f4fa7066290fe7f06b2ba29a3bcdfadc` |
| `LP_blocky/shifted_label_contrast.csv` | 6,145 | `64d8676fb0af06d9b7f73d4a5f56605ef56c65d47130fa4068913a6cf9e928ee` |
| `LP_blocky/source_index_sha256.txt` | 231 | `f9232c0315c4ed7a2bb93695a8aeac631f10e01ff07cc96e6b6f6a9759ee5e79` |

**Do not stage** `experiments/stage2/results/S2_I2_v0_1/LP_blocky/LG_576i_3_LP_blocky.idx`, even if a later unpack accidentally introduces it. It remains a scratch, non-baseline index only under `%TEMP%` or another expressly authorised scratch location.


## 4A. Proposed root `.gitattributes` modification - owner decision required

Recommend appending **only** the following line to the currently tracked root `.gitattributes` *before staging any evidence*:

```gitattributes
experiments/stage2/results/** -text
```

Purpose: disable Git line-ending normalisation for the **numerical evidence** subtree alone. The owner reports `core.autocrlf=true`. Claude independently rehearsed the unpinned case (**25/25** GitHub files differ from Windows hashes) and pinned case (**0/25** differ), using the real attributes and configuration. Existing `.gitattributes` rules for BAT and other source files must remain unchanged. This is a tracked `M .gitattributes` in Step B, not an untracked addition. Do not apply this without owner ratification.

With the pin, and subject to post-push verification, section 4 SHA-256 values apply identically to original Windows working files, Git objects and GitHub source ZIP. Without the pin, they apply to the original Windows files only; separately record the Git-archived representation SHA-256 rather than equating it to Windows bytes. Do **not** normalise or rewrite the evidence files to fit Git.

## 5. Two authority-document paths in `docs/REPOSITORY/`

- **ADD** `docs/REPOSITORY/S2_I2_Evidence_and_Gate_Report_v0_1.md`: installed and owner-ratified form of `S2_I2_Results_and_Closure_Note_v0_3_FOR_CLAUDE_REVIEW.md`. Review must check that the contents: (a) use *strong evidence*, not pixel-by-pixel equality, for the BestSource/FFmpeg comparisons; (b) cite the 25 durable evidence paths with full hashes; (c) record both accepted gates, seven known-bad controls, and spatial-only/field-order limitations; (d) retain S2-I3 NOT AUTHORISED; (e) refer to code commit full SHA and current actual status where appropriate. **Do not install the FOR_CLAUDE_REVIEW filename as a second gate report.**
- **ADD** `docs/REPOSITORY/00_PROJECT_STATUS_v0_6.md`; **REMOVE** `docs/REPOSITORY/00_PROJECT_STATUS_v0_5.md` in the *same commit* per D-23. Start from the ratified `v0_5` checked out at current HEAD, not the earlier unratified local draft. Record S2-I2 COMPLETE/PASS and owner ratification date 2026-10-16, independently reviewed code commit, LP_blocky S2-I2-only scope, row-phase addition, and S2-I3 NOT AUTHORISED. Do not modify `Stage2_Experiment_Design_v0_6.md` just for this commit.

## 6. Existing untracked items - decision and timing

| Item(s) | Step-B handling | After Step-B push is independently verified |
|---|---|---|
| Two design review requests: `experiments/Claude_REVIEW_REQUEST_ChatGPT_S2_I2_Design_Plan_v0_3.md`, `...v0_4.md` | **EXCLUDE** from Step B; retain untracked until the owner chooses archive or deletion. Reviewed design/reviews themselves are preserved in `docs/`. | Owner may remove as redundant process artifacts **only by explicit instruction**. |
| Implementation review request `experiments/stage2/CLAUDE_REVIEW_REQUEST_S2_I2_IMPLEMENTATION_v0_1.md` | **EXCLUDE**. This is the third known REVIEW_REQUEST, also one member of the implementation-package working documents. | Owner chooses retention/archive/deletion. |
| Other implementation-package documents in `experiments/stage2/`: `S2_I2_IMPLEMENTATION_REHEARSAL_EVIDENCE_v0_1.md`, `S2_I2_IMPLEMENTATION_v0_1_README_FOR_CLAUDE.md`, `S2_I2_IMPLEMENTATION_v0_1_TRACEABILITY.md` | **EXCLUDE** from Step B. Taken together with the implementation review request above, these are the four known implementation-package process documents; preserve untracked for an explicit separate decision. | Owner decides whether any are worth relocating to `docs/` or discarding as superseded working material. |
| `experiments/stage2/SHA256_MANIFEST_S2_I2_CANDIDATE_v0_1.md` | **EXCLUDE**; the accepted candidate identity is durably in the report/manifests and code commit, but the original manifest stays untracked pending owner decision. | Owner decides archive/delete, not automatic. |
| S2-I2 closure ZIP, wherever currently untracked (e.g. `experiments/stage2/...` or `experiments/...`) | **EXCLUDE** (never stage a complete duplicated evidence bundle). Keep until the report and individual evidence files are committed, pushed and hashes checked. | Owner may then delete its working-tree copy, or retain a separate offline archive. |
| `experiments/stage2/Z/` (the originally supplied Windows evidence ZIP) | **EXCLUDE**. Retain untracked through Step B as the reference against which installed evidence can be compared; its archive SHA above is known. | With owner permission, delete `Z/` after independent verification of the pushed evidence; it is not a tracked deliverable. |
| `experiments/stage2/research/` | Owner reports its sole Copilot research file moved to `docs/`. Confirm the original folder is empty before any deletion. | Do not stage the folder; remove empty folder only with owner direction. |
| Any S2-I3 entry-plan discussion draft in the working tree | **EXCLUDE**. S2-I3 planning is not authorised implementation and need not be bound into S2-I2 closure. | Retain for future S2-I3 design review. |
| Any newly discovered path not listed in this document | **EXCLUDE**, flag it for Claude/owner review. | No blanket staging or deletion. |

**No `git add -A`, `git add docs`, or `git add experiments`**. For Step B, stage only the paths in the companion pathlist, individually by exact name after the review gates above; handle the v0.5 status deletion by exact name. Check `git diff --cached --name-status --no-renames`, `git diff --cached --check` and the number and identity of changes **before** committing. No deletion of untracked items is part of the Step-B commit.

## 7. Changes to incorporate in the next Claude review

1. Confirm the owner's *actual current* `docs/` filenames and `git status` against this proposed list, including duplicates/collisions with tracked entries; the full code commit and its independent verification are now confirmed by Claude's GitHub-source ZIP inspection; the current live HEAD, proposed `.gitattributes` line, identity-reviewed research source, and status-v0.6 draft still require the user's live-tree check and ratification.
2. Check Copilot source research identity/rights/NOTICE separately before allowing it into the public repository.
3. Confirm all 25 evidence files have original Windows byte hashes above; ensure absence of `.idx` under `results/`.
4. Review and ratify the installed closure report and Project Status v0.6 drafted from repository authority.
5. After exact staged-scope verification, commit and push Step B; Claude reviews the post-push tree and evidence SHA-256. Leave the old untracked artifacts alone until owner authorises housekeeping.

## 8. Change record

- v0.2 (2026-10-16): recorded completed GitHub-verified commit 190bd06; recommended owner-ratified evidence `-text` pin in `.gitattributes` for `core.autocrlf=true`; updated Step-B counts, closure v0.3, no re-commit of accepted code and Windows-vs-Git hash representation distinction.
- v0.1 (2026-10-16): reflects user's two-stage cleanup, the already-present durable evidence subtree, the 12 docs plus research, current closure report v0.2 draft and ratified status v0.5 -> proposed v0.6.
