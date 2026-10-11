# Claude review - step 3 release workflow candidate v0.2 (diff check)

File: Claude_REVIEW_OF_ChatGPT_Step3_Release_Workflow_Candidate_v0_2.md
Version / date: v0.1 / 2026-10-11
Author: Claude (migration chat, independent reviewer)
Reviewed: StageBPlus_Step3_RELEASE_SINGLE_JOB_CANDIDATE_FOR_CLAUDE_v0_2.zip (7 files plus PACKAGE_SHA256.txt), diffed against my reviewed v0.1.

## 1. Verdict

READY FOR DAVE TO RATIFY AND APPLY, then the manual run and the release test as proposed in my v0.1 review, section 5.

## 2. Checks

- SHA-256: 7/7 OK. The workflow is ASCII with CRLF and has 0 trailing-whitespace lines. The preimage equals v0.1, and the CSV is unchanged.
- The diff against v0.1 touches only lines 1, 17 and 47, the event guard (lines 60-65) and the new ancestry block (lines 80-97). The tokeniser, switch checks, HostX64, PE checks, S4 and the attach step are unchanged.
- Dave's decisions are recorded and implemented as he made them.

| Item | Result |
|---|---|
| R1 rejected | Still one job with `contents: write`, unchanged. Dave's decision, and acceptable. As before, checkout does not persist credentials and only the attach step receives the token. |
| R2 | Header now reads "CL 19.51.36260.0, LINK 14.51.36260.0". Correct. |
| Manual on any branch (Q2) | `workflow_dispatch` requires `^refs/heads/.+$`, so tag dispatch is rejected. Correct. Note this replaces the earlier "main only" rule for **manual** runs; record it in Migration_Status. |
| R3, main ancestry (Q3) | This runs only for `release`, after the event-SHA check and before any build. A shallow checkout is fetched with `--unshallow origin main`; a full one with a plain fetch. Then `git merge-base --is-ancestor <tag commit> FETCH_HEAD`. This passes for the main tip or any older main commit, since `--is-ancestor` also succeeds when the two are equal, and fails for a commit only on another branch. It fails closed if the fetch fails. Correct. |
| No manual attach (Q4) | The attach step (line 558) still requires `success()`, `event_name == 'release'` and `action == 'published'`, and re-checks ID, tag and ref. A manual run cannot attach. Correct. |

## 3. Notes (no change needed)

- Optional: also write the "PASS: published Release commit ... belongs to main history" line into `event_identity.txt`, so it sits in the artifact as well as the console log.
- The fetch needs no credentials while the repo is public. If the repo ever becomes private, the ancestry check fails closed (no release assets) until that is addressed.

## 4. Gate (unchanged from my v0.1 review, section 5)

1. Commit on `main`, then run manually on `main`. Optionally also run once on another branch, which proves the any-branch rule and shows no attach.
2. With Dave's explicit go: publish one **pre-release** test (e.g. `v0.1.0-ci-test`, "CI test - scaffold, not for use") on a `main` commit. Pass criteria:
   - the ancestry PASS line appears;
   - all checks PASS;
   - the 4 assets are attached;
   - their SHA-256 values equal the run's `release_binary_hashes.txt`.
   Keeping or deleting it afterwards is Dave's call.
