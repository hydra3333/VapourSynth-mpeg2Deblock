# Claude review of ChatGPT S2-I2 closure v0.4 and Step-B v0.3 (review v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: S2_I2_CLOSURE_v0_4_STEP_B_v0_3_FOR_CLAUDE_REVIEW.zip

The package contains six files:

- the closure note v0.4;
- the placement inventory v0.3;
- the pathlist v0.3;
- the status-v0.6 requirements note;
- the review request;
- the manifest.

## 1. Verdict

**Closure v0.4 content: CLEARED. Inventory v0.3 and pathlist v0.3: CLEARED.** There are no MUST findings.

- **Package integrity:** all manifest hashes match, and every file is US-ASCII CRLF with no identity text.
- **The previous findings are all correctly applied:**
  - M1: the evidence is now stated as ZIP-only and not yet unpacked;
  - S1: the `.gitattributes` check is the only whitespace STOP;
  - S2: the ASCII exception is narrow, proposed and not yet ratified;
  - S3: status v0.6 is to be drafted from the ratified v0.5 only;
  - O1 and O2 are applied.
- **Results are unchanged.** Claude diffed v0.3 against v0.4: only sections 6, 7.1 and the change log changed. Every result, threshold, limitation and sample disposition is unchanged.
- **All 25 evidence hashes** appear unchanged in both the closure note and the inventory.
- **Counts:** 40 A / 1 M / 1 D with the pin and both exceptions, or 38 A / 1 M / 1 D with neither. These agree with the pathlist.
- **The exception wording** keeps Claude's identity/NOTICE clearance separate from the owner's waiver, and limits the waiver to the two named verbatim records.

Step B is still **not executable**. Three items remain: section 2, item 1, and the two owner decisions in section 3.

## 2. Remaining before the Step-B command block

**1. Project Status v0.6 (full draft).**

- The requirements note is correct. It also correctly refuses to draft from ChatGPT's older local v0.5.
- The owner should attach `docs\REPOSITORY\00_PROJECT_STATUS_v0_5.md` from the working tree. With `core.autocrlf=true`, that copy should be the CRLF form, `a5f19fa8...81da`. ChatGPT can check it against that value or against the Git LF form, `ee0d41ea...9131`.

**2. Install-ready gate report (SHOULD).**

- The file to install as `docs/REPOSITORY/S2_I2_Evidence_and_Gate_Report_v0_1.md` must be a finished file, not the review draft renamed. The draft still says "REVISED DRAFT for Claude review", "working review draft is v0.4", and so on.
- ChatGPT should supply the exact install-ready file (US-ASCII CRLF) with:
  - the version set to 0.1;
  - the status changed to ratified on the owner's ratification date;
  - "proposed" wording resolved for decisions the owner has actually taken, such as the pin and the exceptions;
  - a short change log noting that it derives from review drafts v0.1 to v0.4.
- Claude will diff it against v0.4 so that only header, status and decision wording change, and then hash it for the command block. The same applies to status v0.6.

**3. Document hashes (OPTIONAL).** Inventory v0.3 refers to Claude's review section 5 for the 12 document hashes, rather than listing them. That is acceptable. Claude's command block will check all 13 documents: the 12 hashes from that section, plus the Copilot file `9ea0462a...8986`.

## 3. Owner decisions needed (no command yet)

1. **Evidence pin:** append `experiments/stage2/results/** -text` to `.gitattributes`. Claude recommends YES.
2. **D-23 US-ASCII exception** for exactly these two verbatim records:
   - `docs/ChatGPT_Review_of_Copilot_Grok_MPEG2_Block_Detection_v0_1_FOR_CLAUDE.md`;
   - `docs/COPILOT-MPEG2_Deblocking_VHS_DVD_Research.md`.

   Claude recommends YES. Declining either decision is also safe; the counts would then change as the inventory describes.

## 4. Sequence from here

1. The owner decides both items in section 3 and attaches the repository's v0.5 to ChatGPT.
2. ChatGPT delivers:
   - the full status v0.6;
   - the install-ready `S2_I2_Evidence_and_Gate_Report_v0_1.md` (both US-ASCII CRLF);
   - their hashes.
3. Claude reviews both against the ratified v0.5 and closure v0.4, then issues the single Step-B CMD block. The block will:
   1. verify the ZIP;
   2. extract the evidence and hash all 25 files;
   3. append the pin and check it with `git check-attr`;
   4. hash the 13 documents and the 2 authority files;
   5. stage by name;
   6. confirm the expected counts;
   7. run `--check -- .gitattributes`;
   8. commit and push.
4. Claude verifies the result from GitHub.
