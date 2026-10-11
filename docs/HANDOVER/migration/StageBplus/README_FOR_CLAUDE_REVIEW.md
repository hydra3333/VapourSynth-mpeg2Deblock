# Stage B+ migration Step 3 - release-workflow candidate v0.2 (single job)

**Status:** DRAFT for Claude independent DIFF review; NOT APPLIED.
**Date:** 2026-10-11. **Author:** ChatGPT migration coder.
**Source:** Claude review of Stage B+ Step 3 candidate v0.1, plus Dave's explicit decisions.

## Dave's decisions (supersede v0.1 reviewer recommendations)

- **R1 REJECTED:** Keep existing one-job workflow with `contents: write`; do not split permissions/jobs.
- **R2 ACCEPTED:** Correct the recorded CL versus LINK version numbers.
- **R3 REQUIRED BY NEW POLICY:** A published formal GitHub Release must tag a commit in `main` history. Enforce Git ancestry check on released tag commit.
- **Manual policy CHANGED:** Manual workflow dispatch must work for ANY branch (`refs/heads/*`). No manual run may attach assets to a GitHub Release, including from `main`.
- **R4 UNDECIDED:** No additional checksum Release asset is introduced. The SHA-256 evidence file remains included in the workflow-run artifact.

## Exactly one production file to replace after Claude reviews and Dave ratifies

`.github/workflows/prove-project-build-windows-x64.yml`

This candidate is a focused diff from reviewed v0.1, which itself is based on the previously successful Step 4 CI proving workflow (commit `3ccfa182`, run `38092449456`). No project, C++ source, `.slnx`, expected-switch CSV, or historical A3 CSV changes.

## Event mode contract

| Property | Published GitHub Release | Manual Actions run |
| --- | --- | --- |
| Trigger | `release.published` | `workflow_dispatch` |
| Ref | `refs/tags/<published release tag>` | `refs/heads/<any branch>` |
| Commit | Exact event SHA, additionally verified as ancestor of fetched main HEAD | Exact event SHA from selected branch |
| Build/strict tests | Debug + Release both projects; strict 10-key 256-token proof | Same |
| Artifacts in Actions run | Four binaries/PDBs, checksums, logs | Same |
| Attach four binaries/PDBs to GitHub Release | Yes, only after success | Never |

The tag ancestry test uses `git fetch --no-tags --unshallow origin main` for a shallow checkout, or normal `git fetch --no-tags origin main` when complete, then `git merge-base --is-ancestor $checkoutSha FETCH_HEAD`. This allows an older commit on `main`, not just the current `main` tip; it fails on a divergent branch commit. Check occurs after checkout event SHA verification and before the VS discovery/build. **No automatic tag or Release creation** occurs: someone must explicitly publish a GitHub Release to trigger this mode.

The single-job token has contents:write as Dave chose. `persist-credentials: false` remains. The token is explicitly provided to `gh` only by the Release-only upload step. Manual runs still upload a normal GitHub Actions artifact, never GitHub Release assets.

## Preserved limits and proofs

- Identical eight-step job structure and original embedded Python switch checker, including G5/G7.
- Original 256-token reference CSV is byte-for-byte unchanged; no new compiler/linker/resource options.
- Release security/import/export/version checks retained, and R81 local Stage B+ tests remain accepted separately; do not rerun six local indexes in CI.
- S4 four Release outputs, S6 Node24 action majors v7, SDK used and HostX64 proofs remain.
- Failure retains diagnostic artifacts but must not publish Release assets.
- R3 ancestry check verifies main *history*, not equality to latest main HEAD. If Dave intended HEAD-only publication, explicitly revisit the policy rather than silently tightening it.

## Offline checks / limits

`STATIC_VALIDATION.txt` documents the YAML/AST/layout/SHA checks. Git ancestry behaviour itself is well defined, but the new PowerShell code and GitHub Release event have not been exercised on a hosted Windows runner. There is no claim that release attachment currently passes.

## Items for Claude's v0.2 diff review

1. Is R1 properly absent, one job, with single-job token permissions unchanged?
2. Is the manual-any-branch guard correct and limited to `refs/heads/*` while excluding tag dispatch?
3. Does the shallow/nonshallow fetch and `git merge-base --is-ancestor` reliably reject Releases from outside main history, without making valid older-main Releases fail?
4. Does the release-only attach guard remain sufficient to guarantee no manual Release attachment?
5. Is the R2 correction accurate, and have all proven build/switch/security checks remained untouched?

**Do not apply, commit, or publish a real Release until reviewed/ratified.** After v0.2 acceptance: snapshot the workflow on main; manually prove main and optionally a non-main branch; publish a public pre-release only after Dave explicitly authorises that external action.
