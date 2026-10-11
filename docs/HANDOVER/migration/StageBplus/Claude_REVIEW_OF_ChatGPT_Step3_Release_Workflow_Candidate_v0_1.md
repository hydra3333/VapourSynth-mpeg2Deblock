# Claude review - step 3 release workflow candidate v0.1

File: Claude_REVIEW_OF_ChatGPT_Step3_Release_Workflow_Candidate_v0_1.md
Version / date: v0.1 / 2026-10-11
Author: Claude (migration chat, independent reviewer)
Reviewed: StageBPlus_Step3_RELEASE_CANDIDATE_FOR_CLAUDE_v0_1.zip (6 files plus PACKAGE_SHA256.txt). The candidate was diffed against the proven step 4 workflow, which is the version run 38092449456 used.

## 1. Verdict

GOOD, AND CLOSE. The changes are all ones we agreed, and the protections the step 4 run proved are untouched. One should-fix needs Dave's choice (R1). There is also one small correction (R2) and one optional item (R3). After that: a manual proof run, then a real-release test (section 5).

## 2. Verified

- SHA-256: 6/6 OK. The header line is text, which is why sha256sum warns about one line. The workflow is ASCII with CRLF and has 0 trailing-whitespace lines.
- The baseline file equals my reviewed step 4 v0.2, which is what ran. The reference CSV equals the committed CSV.
- Diff scope: header and G7 block, triggers, permissions, event/ref/SHA guard, CSV-driven counts, the `$matches` rename, S4 binary preservation, artifact v7, and release attach. Nothing else changed: discovery, isolation guards, tokeniser, HostX64 classifier, PE checks, the F1 version check and the F2 SDK record are all as proven.
- **S6, action versions.** I checked with `git ls-remote` and the action metadata:
  - `actions/checkout` tags run up to v7.0.1, and v7 `action.yml` has `using: node24`;
  - `actions/upload-artifact` tags run up to v7.0.2, and v7 has `using: 'node24'`.
  Both exist and both are Node 24. VERIFIED.
- **G7 (Q3).** All 10 reference lines equal `' '.join(CSV tokens)` for their key, checked by script. They are comments only, clearly labelled with placeholders, so they are not a second build route. Good.
- **G5 (Q4).** The fixed 10-key inventory stays in code. Counts now come from the CSV. Missing or extra tokens are still fatal, and LINK still ignores case. The disposition allow-list (blank or the B6 string) is adequate: the CSV is the reviewed authority, and any change to it is a reviewed commit. Correct.
- **Event logic (Q1).**
  - Manual runs must be on `main`.
  - A release must be `published`, with `GITHUB_REF == refs/tags/<tag>`.
  - Checkout HEAD is compared with `GITHUB_SHA`, and the identity is recorded.
  - The attach step re-checks ID, tag and ref through `gh api`.
  Correct. Note: for a `release` event, GitHub runs the workflow file **from the tagged commit**. A tag on a commit older than this workflow does nothing, which is fail-safe.
- **S4.** The four files are always preserved with size and SHA-256, and an empty file fails. Attaching is gated on `success()`, so a failed check never publishes. No `--clobber`, so duplicates fail rather than overwrite. Correct (Q5).

## 3. Should fix (Dave's choice)

**R1. Least privilege: two jobs in the same one workflow file.** Today `contents: write` applies to the whole job, including the manual runs and the step that builds repository code with MSBuild. Risk is low, because the repo is Dave's own, checkout does not persist credentials, and the token is passed only to the attach step. But the cost of splitting is small, and it still meets G3 ("all in one place": one file):
- job `build-and-prove`: `permissions: contents: read`. Everything as now, including the artifact upload.
- job `attach-release-assets`: `needs: build-and-prove`, `if: github.event_name == 'release' && github.event.action == 'published'`, `permissions: contents: write`. Steps: `actions/download-artifact@v8` (the current major; I checked that v7 and v8 both run on node24), then the same identity checks and `gh release upload`, with no checkout at all.

Manual runs would then never hold write access. I recommend the split; if Dave prefers one job, the current design is acceptable.

## 4. Small items

- **R2. Header comment.** It says "CL/LINK file version 19.51.36260.0". CL is 19.51.36260.0 and LINK is 14.51.36260.0. Fix the wording.
- **R3. Optional.** For a release, also check that the tagged commit is on `main`: `git fetch --no-tags origin main` (a public repo needs no credentials), then `git merge-base --is-ancestor $env:GITHUB_SHA FETCH_HEAD`. This enforces "main is the only branch" at release time. Optional.
- **R4. Optional.** Also attach `release_binary_hashes.txt` as a fifth asset (SHA256 sums), so users can check their downloads. Optional.

## 5. Proposed step 3 gate (Q6)

1. **A manual run on `main`** after applying. It must show:
   - checkout and upload-artifact v7 working;
   - all checks PASS;
   - `Release_Binaries/` with 4 files and `release_binary_hashes.txt`;
   - `event_identity.txt`;
   - no attach job or step running.
2. **One real release test.** This is public and needs Dave's explicit go.
   - Dave publishes a GitHub Release marked **pre-release**, e.g. tag `v0.1.0-ci-test`, titled "CI test - scaffold, not for use", on the current `main` commit.
   - Pass criteria:
     - the workflow runs for the tag;
     - all checks PASS;
     - the 4 assets (5 with R4) are attached;
     - the attached SHA-256 values equal `release_binary_hashes.txt` in that run's artifact.
   - Afterwards, Dave decides whether to keep the pre-release or delete it. Deleting a release or tag is destructive, so it is his explicit call and never automatic.
   - Expect the release page to be visible without assets for a few minutes while the build runs.
3. Re-publishing the same tag should fail on duplicate assets, by design. There is no need to test that.

## 6. Next

1. ChatGPT makes v0.2 with R1 (if Dave agrees) and R2, plus R3 and R4 if Dave wants them.
2. I check it as a diff.
3. Dave applies it and does the manual run, then the release test.
4. I review both runs. Step 3 closes, then step 4, the handback.
