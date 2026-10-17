# Claude clearance: S2-I3 v0.3 and Stage 2 v0.7 final wording (v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: S2_I3_v0_3_STAGE2_v0_7_FINAL_WORDING_FOR_CLAUDE_REVIEW.zip

## Verdict

**CLEAR FOR OWNER RATIFICATION.**

Claude diffed both documents against the versions reviewed in `Claude_REVIEW_OF_ChatGPT_S2_I3_v0_3_and_Stage2_v0_7_rev_v0_1.md`. The only changes are the requested edits.

**Stage 2 v0.7:**

- **S2:** the qualifying-block definition is added.
- **S3:** the reference is now "the immediately preceding I or P picture in display order, which is also the most recently decoded anchor", and the controls say "next/previous picture in display order".
- **S4:** the shifted-window sentence is added (same offset in both windows; only windows wholly in-bounds counted).
- **S1:** the disposition now treats a control reaching 100% as INCONCLUSIVE - QUALITY BLOCKED. FAIL is kept only for a structural failure or a true-position mismatch.
- **O1:** the duplicate rule is removed.

**S2-I3 v0.3:** section 3.1 mirrors S1 and S3.

Nothing else changed:

- the S2-I2 diagnostic thresholds;
- the folds and source assignments;
- Q_fixed;
- hold-out protection;
- the v0.6 history;
- the authority status;
- the seven non-baseline indexes;
- the fixed-QP-only boundary.

Integrity: the manifest hashes match, the files are US-ASCII and consistently CRLF, and there is no identity text.

## Notes for the installation step

**1. Install-ready copies.**

- The ratified files must not be installed with draft headers. Today they read "DRAFT FOR CLAUDE REVIEW; NOT RATIFIED".
- Before the documentation commit, ChatGPT should supply install copies with:
  - final filenames (no `_FOR_CLAUDE_REVIEW` suffix);
  - the status changed to ratified on the owner's ratification date;
  - text that is true at its own installing commit (the same lesson as S2-I2 Step B).
- Claude then diff-checks that only the header and status lines changed, and hashes the files for the command block.

**2. Commit content.**

- Stage 2 v0.7 is added and v0.6 removed in the same commit (D-23). Placement of the S2-I3 design follows the owner's choice; `docs/REPOSITORY/` is Claude's recommendation, matching other authority documents.
- A status update (Project Status v0.7) is expected in the same bounded commit if the owner wants the status file to record the ratification.
- The two review `.diff` files are excluded.
- The seven development indexes are **not** part of this commit.

**3. Guided procedure.** ChatGPT's step-by-step Windows guidance should:

- stage by name;
- check the exact counts (expect A/M/D as listed in its plan);
- run `git diff --cached --check -- <the new .md files>` informationally;
- verify the result after the push, as Claude has done for every previous commit.

Claude will verify the pushed commit from GitHub.
