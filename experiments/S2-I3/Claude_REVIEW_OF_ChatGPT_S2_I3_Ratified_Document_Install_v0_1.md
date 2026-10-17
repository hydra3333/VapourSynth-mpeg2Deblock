# Claude review of the ratified S2-I3 / Stage 2 documentation install package (v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: S2_I3_RATIFIED_DOCUMENT_INSTALL_FOR_CLAUDE_v0_1.zip
Base HEAD: `6e7b5c53df1c65775524936fc945c449cc9fa100`.

## 1. Verdict

**CLEARED, with Claude's wording corrections applied** (one MUST, corrected in place). It is ready for named staging once the owner ratifies the status v0.7 content.

- **Integrity:** the manifest hashes match. The three install targets are US-ASCII CRLF with no identity text. The review-only `.diff` files are LF and must stay out of Git.
- **Stage 2 v0.7 and S2-I3 v0.3 against the cleared final wording:** only the header, status and authority wording and the change-log headings changed. No criterion, fold, threshold, role or history changed.
- **Status v0.7 source check** (review item 3):
  - the candidate was built from ChatGPT's pre-correction local v0.6 plus its diff;
  - compared directly with the committed v0.6 (`23197330...313e`, CRLF form, content-identical to GitHub), every difference is an intended v0.7 change;
  - the committed v0.6 change-log entry and all earlier history are present verbatim;
  - no corrected wording is reverted.
  - The transplant concern is therefore resolved, and no rebase is needed.

## 2. MUST (corrected by Claude)

**M1. Stale "proposed / not yet ratified" text would be false in the installed files.**

This is the same issue as the S2-I2 Step B M1. Corrected wording:

- **Stage 2 v0.7:**
  - **section 3.0:**
    - "These are **proposed v0.7 assignments** and take effect only after the owner ratifies this revision" becomes "ratified in v0.7 (2026-10-17)";
    - "sources proposed for reassignment" becomes "sources reassigned";
  - **section 3.2:** "v0.7 proposal" becomes "v0.7 development";
  - **section 6.2:** "the proposed eight-source S2-I3 scheme" loses "proposed";
  - **section 6.3 and section 8.4 headings:** "(PROPOSED v0.7)" becomes "(v0.7)";
  - **section 8.4:** "is proposed for replacement" becomes "is replaced";
  - **section 19:** "Proposed v0.7 order ... Stage 2 v0.6 is still binding until the owner ratifies this revision" becomes "Ratified v0.7 order (2026-10-17) ... v0.7 supersedes Stage 2 v0.6".
- **S2-I3 v0.3:**
  - the "Proposed role" column becomes "Role";
  - "Interpretation for this proposal" becomes "... this design";
  - in the section 9 disposition table, M3's "conditional alternate proof remains a review gate" becomes "exact P-skip identity admission (v0.3) closes the alternate-proof gate", and M4's "proposal" becomes "(ratified)".
- **Status v0.7:**
  - the header Status line is changed from candidate to ratified, installed by this documentation-only commit;
  - the Step-B paragraph's "this status v0.6" (which would be wrong inside v0.7) becomes "Project Status v0.6";
  - the change-log heading becomes "(RATIFIED)", and "proposes to install" becomes "installs".

The full diff is in `Claude_S2_I3_Install_Wording_Corrections_v0_1.diff`.

**Install copies (CRLF), for `docs/REPOSITORY/`:**

```
d754b94869a2c77ee148a41f1ca38e9998f3fdca698fd6090372a300a8bbb787  Stage2_Experiment_Design_v0_7.md
67893a9acde830079fa382c5f0c62d32fee7d5a13d3eae77930905aa1eaa81d8  S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_3.md
e7d2d422186f66bfe8b199291aa8e1f265c6f14e43f2556a6d8c5db53060f64d  00_PROJECT_STATUS_v0_7.md
```

The status header reads "RATIFIED 2026-10-17 by the project owner". The owner's commit of these exact bytes is that ratification, as for v0.6.

## 3. Rehearsal

Claude ran the rehearsal on a fresh sparse clone of GitHub at `6e7b5c53` with `core.autocrlf=true`:

- **Staging:** the three files placed and staged by name, plus `git rm` of the two v0.6 files, gave exactly `3 A / 2 D` in `--no-renames` form.
- **Whitespace:** `git diff --cached --check` was clean.
- **Archive:** after a test commit, the GitHub-style archive (LF), converted to CRLF, reproduced all three install hashes exactly.

## 4. Exclusions (unchanged)

- The seven development indexes are excluded.
- The six frozen Stage 1 indexes are untouched.
- The review `.diff` files, ZIPs and other untracked items are excluded.
- No code is included.
