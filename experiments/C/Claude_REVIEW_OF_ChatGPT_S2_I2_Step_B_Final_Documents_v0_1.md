# Claude review of ChatGPT S2-I2 Step-B final documents (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: S2_I2_STEP_B_FINAL_DOCUMENTS_FOR_CLAUDE_REVIEW_v0_1.zip

## 1. Verdict

**CLEARED, with Claude's wording corrections applied** (one MUST, corrected in place). Step B is ready for the owner to run.

**Integrity.**

- All manifest hashes match. All files are US-ASCII CRLF with no identity text.
- The attached v0.5 source is the ratified repository file (CRLF `a5f19fa8...81da`).

**The gate report against closure v0.4.** Diffed line by line. Only the title and header, the decision wording in section 6, the wording in section 7.1, and the change log changed. Every result, threshold, limitation and evidence hash is identical.

**Status v0.6 against the ratified v0.5.** Diffed line by line. All the v0.5 text and every earlier change-log entry are preserved, and the new content is correct:

- the S2-I2 PASS table, the code commit `190bd06` and the commit chain;
- the LP_blocky S2-I2-only role and the row-phase addition;
- the stated limits;
- the two owner decisions, recorded as YES;
- S2-I3..I10 NOT AUTHORISED;
- the S2-I8 census wording;
- Stage 2 v0.6 unchanged.

## 2. MUST (corrected by Claude)

**M1. Both files describe their own installing commit as still pending.**

- **The problem.** Both files would be committed by Step B itself. Yet they still say:
  - "DRAFT FOR CLAUDE REVIEW - NOT YET RATIFIED OR INSTALLED";
  - "Step B is PENDING, not staged";
  - "not yet extracted";
  - "not yet applied or committed";
  - "(DRAFT; NOT YET RATIFIED)".
- **Why it matters.** Every one of those statements becomes false the moment the files are committed. This is the same class of problem as the earlier M1 about the code commit.
- **The precedent.** Ratified v0.5 states its own status as "RATIFIED 2026-10-14 ... The commit that installs v0.5 will follow it".
- **The correction.** Claude applied minimal wording edits so that both files are true as at their installing commit. The pattern is the same as Claude's direct correction of status v0.5.
  - **Gate report:**
    - the header's disposition line;
    - section 6 items 2, 3, 4 and 6;
    - the wording in section 7.1;
    - the first change-log entry.
  - **Status v0.6:**
    - the header Status line;
    - section 3's commit note;
    - the Step-B paragraph;
    - two layout rows;
    - the S2-I2 increment row;
    - the decision notes;
    - the v0.6 change-log heading and entries.
- **Nothing else changed:** no results, hashes, thresholds, decisions or history.
- The full diff is in `Claude_Step_B_install_wording_corrections_v0_1.diff`.

**Install copies (US-ASCII CRLF):**

```
5a5e89736a411b5c1c3f7885c37a6fcad8191687d5f5e7adfe00d025294879ae  S2_I2_Evidence_and_Gate_Report_v0_1.md
23197330b2d2bafb80e63df7a8812619f8c26177f844025bf7117ca1b2c1313e  00_PROJECT_STATUS_v0_6.md
```

The status header now reads "RATIFIED 2026-10-16 by the project owner". The owner's commit of these exact bytes is that ratification.

## 3. The Step-B procedure (`S2_I2_Step_B_stage_v0_1.py`)

The procedure is a Python script rather than a CMD block, because a pasted CMD block cannot stop at the first failure. It uses only the Python standard library and git.

**What it does**, in this order:

1. **Read-only checks:**
   - HEAD is exactly `190bd06`;
   - nothing is staged and no tracked file is modified;
   - v0.5 is the ratified file;
   - all 15 documents match the reviewed SHA-256 values (12 history files, the Copilot file, and the 2 install copies);
   - the ZIP SHA-256 is `0bce9022...34d6`;
   - neither the pin line nor the results folder exists yet.
2. **Extraction:** it extracts exactly the 25 evidence files, with the `.idx` never extracted, then re-verifies their sizes and hashes on disk and confirms that no other file is present.
3. **The rule:** it appends `experiments/stage2/results/** -text`, using the file's own line ending, then runs `git check-attr`. The result must be `unset` for the evidence and not unset for a document.
4. **Staging:** it stages the 41 paths by name and runs `git rm` on v0.5.
5. **Staged-set check:** it compares the exact staged set and statuses with the expected list (40 A / 1 M / 1 D).
6. **Final checks:**
   - `git diff --cached --check -- .gitattributes` must be clean;
   - each of the 25 **staged blobs** must be byte-identical to the Windows hashes.

It **never commits or pushes**. At any failure it prints STOP and exits with code 2.

**Rehearsal.** Claude ran it on a fresh `git clone` of the GitHub repository at `190bd06`, with `core.autocrlf=true` (reproducing the owner's CRLF v0.5 `a5f19fa8`). The replica contained the owner's documents, the evidence ZIP and an unrelated untracked decoy file.

- **The happy path ended READY TO COMMIT.**
- **The commit** gave exactly 40 added, 1 modified and 1 deleted. `git show`'s default rename detection displays the deletion as a rename of v0.5 to v0.6, which is cosmetic.
- **A GitHub-form archive** (`core.autocrlf=false`) had **0 of 25** evidence-hash mismatches, with v0.5 gone, v0.6 present and no `.idx`.
- **Negative tests:**
  - a missing document: STOP before any change;
  - a re-run after the commit: STOP on the HEAD check.
- The decoy and `Z/` stayed untracked.

## 4. For ChatGPT

No further drafting is needed. ChatGPT should note the M1 wording corrections and the two new hashes. The inventory v0.3 and pathlist v0.3 stand as cleared.
