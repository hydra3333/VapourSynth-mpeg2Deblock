# Claude diff clearance: Route A install copies v0.2

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude, independent review role
Date: 2026-10-18
Packet reviewed: `Route_A_S2_I3_P0_INSTALL_COPY_DIFF_REVIEW_v0_2.zip`, six files
Against: the v0.1 candidates cleared in `Claude_REVIEW_OF_Route_A_Transfer_Packet_v0_1_v0_1.md`
Repository baseline re-verified: `8ffaa7d6d2500f842d5f841402a7b025ea4eda90`, still live HEAD

## 1. Verdict

**BOTH INSTALL COPIES CLEARED FOR INSTALLATION. No MUST remains. No SHOULD remains.**

Claude computed its own cold diff of each install copy against the previously cleared candidate rather
than reading the supplied patches. **Every one of the 41 changed lines maps to an agreed finding
(M1, M2, S1, S2, S3, O1). There is no unexplained change.**

Two conditions attach, both about *when and in what order* the files are committed rather than about
their content. Section 5.

Claude does **not** call these documents ratified. They carry future-effective ratification text by
design, correctly flagged as conditional in the packet's own guard note, and the owner's explicit
ratification of the installation wording is still required.

## 2. What was verified, and how

| Check | Method | Result |
|---|---|---|
| Install copies differ from cleared candidates only as agreed | Claude's own `diff` of LF-normalised texts, not the supplied patches | **Report: 26 changed lines, 7 hunks. Concept: 15 changed lines, 5 hunks. All accounted for** |
| No figure, hash, count or percentage altered | Extracted every 64-hex token, every decimal and every 3+ digit integer from both report versions and compared multisets | **Zero tokens removed.** Exactly four added: `610`, `96.72%`, `8,812` and `2026` twice - all from the M1 correction and the ratification dates |
| Eight index SHA-256 values unchanged | Per-hash occurrence counts, old versus new | **All eight identical** |
| K-03 / K-07 / K-08 rows unchanged | SHA-256 of each extracted table row | **All three byte-identical** |
| Concept section 3.1 body unchanged | SHA-256 of the block from "K-03: corroboration" to "establishes admission/correspondence" | **Byte-identical** (`d1ddbfa80ad0`) |
| M1 arithmetic | Recomputed from the evidence JSON | **Correct.** 8812 - 8202 = **610**; 8812 - 8523 = **289** |
| Supplied patches consistent with the install copies | Applied each patch to its candidate and compared the result | **Both reproduce their install copy exactly**, so ChatGPT's diff tooling agrees with Claude's |
| SHA-256 manifest | Recomputed all five listed digests | **All five OK** |
| Baseline still current | Fresh `ls-remote` | HEAD still `8ffaa7d6`, so no rebase needed |
| Identity text | Scanned all six packet files | **CLEAN** |
| Encoding of the two install copies | Byte census | **Pure US-ASCII**, 560 and 584 lines, no stray high bytes |

## 3. The changes, mapped to findings

### Evidence Report, 26 lines in 7 hunks

| Lines | Change | Finding |
|---|---|---|
| 3-4 | "Proposed repository path" to "Repository path"; version line to "RATIFIED by the project owner on 2026-10-18" | M2 |
| 10 | Authority line: "v1.2, pending a separately reviewed v1.3 candidate" to "v1.2 at the report drafting baseline; subsequent v1.3 is a separately reviewed and ratified update when installed" | M2, and durably phrased so it stays true after v1.3 lands |
| 32 | "this draft exists" to "this report exists"; **plus** the new sentence accounting for bridge sections 1, 9, 10 and 18 as process material, and pointing section 2's durable prohibition at section 13 item 5 | M2 + **S3** + **S2** |
| 34 | "outside this proposed Git commit" to "outside the report installation commit" | M2 |
| 57 | New sentence: the labels `3A` and `TEST 3A` denote the same admitted `TEST_3A_A002` source | **O1**, handled by one equivalence sentence rather than mass-editing copied annex provenance - the right call |
| 82 | **M1 fix:** "(289 blocks differed)" replaced by "with **610** blocks differing", plus a new sentence naming `previous_display` at 96.72% differing in only 289 of 8,812 | **M1**, exactly as proposed |
| 99 | "This explanatory interpretation is proposed for reviewer source-code verification" to a record that Claude verified it against the accepted source rule on 2026-10-18 | correct, and now true |
| 536 | "draft only, proposed current-tree addition after Claude review and owner ratification" to "ratified project record, installed in a separately bounded report-only commit" | M2 |
| 538 | Concept-authority paragraph rewritten; adds "At this report's initial installation, the preceding v1.2 remains authoritative until that separate v1.3 commit is installed" | M2, and it correctly encodes the two-commit ordering |
| 540 | Bridge-retention paragraph gains the sentence marking bridge section 10's operational snapshot historical and superseded | **S1** |
| 551 | Item 5 gains the prohibition on quoting the superseded v0.2 boundary and interior figures | **S2** |
| 555 | Change log heading to "(RATIFIED; initial report installation)" | M2 |

### Concept v1.3, 15 lines in 5 hunks

| Lines | Change | Finding |
|---|---|---|
| 4 | Version to "1.3 (RATIFIED 2026-10-18)" | M2 |
| 6-7 | Drafted-by records the Claude review and owner ratification; status line now describes v1.3 as the ratified current revision superseding v1.2 without changing ratified K mechanisms | M2 |
| 30 | "Version 1.3 is proposed solely to annotate" to "Version 1.3 annotates ... solely" | M2, a stale temporal phrase Claude had not itemised; correct to fix |
| 134 | Section 3.1 heading loses "(v1.3 DRAFT; ...)" | M2 |
| 504, 513-514 | Change log heading to "(RATIFIED)"; the "requires Claude's review and the owner's ratification" bullet replaced by a record that both occurred | M2 |

**Nothing else in the concept changed.** The K-table rows, section 3.1's body, every figure, and all
open O-items are byte-identical to the cleared candidate.

## 4. False-at-install sweep

Claude swept both install copies for any remaining present-tense draft, candidate, proposed, pending or
awaiting language that would become false at the installing commit. **None remains.** The hits the sweep
returned are all legitimate and must stay:

- technical uses of "candidate": candidate seams, candidate temporal offsets `k=-2..+2`, candidate
  boundary locations, the frozen initial candidate kernel, candidate analytical measures;
- durable statements of fact: that ChatGPT did not execute P0 or read the 137 files; that v0.5
  supersedes v0.1-v0.4; that no `.idx2` or Stage 1 expansion is proposed; the record of the owner's
  P0 ratification;
- the concept's section 0.2 general policy sentence that drafts awaiting ratification show their
  evidence level explicitly - a statement about the labelling convention, not about this document;
- historical change-log entries for concept v0.1 and v0.2 marked "(DRAFT, PROPOSED)", which were
  accurate at the time and are correct to preserve as history.

The two specific places the packet asked Claude to check are both correct: concept section 0.1 now
reads "Version 1.3 annotates K-03/K-07/K-08 solely with empirical Stage 2 evidence", and the report's
section 12 cross-document lifetime sentence correctly states that v1.2 remains authoritative at the
report's installation until the separate v1.3 commit lands.

## 5. Two conditions on installation

Neither is a content defect. Both arise because the install copies deliberately carry future-effective
text, which is the right solution to the install-time wording problem but makes two circumstances
load-bearing.

### Condition 1 - the date. Install on 2026-10-18 or update every date field.

Both documents assert **RATIFIED 2026-10-18**. If the owner ratifies and installs on a later date,
those statements are false on arrival - the exact defect M2 existed to remove. The packet's own guard
note says this; Claude confirms it and makes it a condition. If the date slips, update every
ratification and date field in both documents and send the revised copies for a short re-diff; Claude
will check only the changed lines.

### Condition 2 - the order is now load-bearing, not merely preferred.

The concept's status line says v1.3 is "separately installed **after** the S2-I3 P0 Evidence and Gate
Report". **If the concept were installed first, that sentence would be false.** So the previously
recommended order is now a correctness requirement:

| Step | Commit | Expected staged shape |
|---|---|---|
| 1 | `docs/REPOSITORY/S2_I3_P0_Evidence_and_Gate_Report_v0_1.md` from the report install copy | **`1 A / 0 M / 0 D`** |
| 2 | `docs/REPOSITORY/06_DEBLOCK_CONCEPT.md` in place from the concept install copy, after the owner's separate approval | **`0 A / 1 M / 0 D`** |

Never stage both in one commit. Run `git diff --cached --name-status --no-renames` before each and
confirm the shape exactly; three commits earlier today swept unintended files and that check is what
stopped the fourth.

**Install-copy digests for the owner to confirm after staging** (LF-normalised, which is what Git will
store given `core.autocrlf=true`):

```
253cc418e3408e9a...  S2_I3_P0_Evidence_and_Gate_Report_v0_1.md
820c15f4149c9acc...  06_DEBLOCK_CONCEPT.md
```

Nothing else from this packet enters the repository: not the two review-only patches, not the manifest,
not the diff-review request, not the ZIP. The seven indexes are already installed at `35923a5` and must
not be staged again.

## 6. Unchanged

P0 is ratified PASSED; **P1 remains unauthorised and needs a separate explicit owner decision.** No
filtering has been run or evaluated. The six frozen Stage 1 indexes and the seven newly tracked indexes
are untouched. EP, TEST 2A and TEST 4A with every `_blocky` copy stay locked until S2-I8 under any
filename or alias. TEST 6A and 7A remain outside the allow-list with no assigned role. No change to
`02`, `05`, Stage 2 v0.7, S2-I3 v0.3, any open O-item, or any D-item. No new K item. Git history has not
been scrubbed and that remains a Development Closure obligation.

**The interim bridge stays tracked.** Retirement still needs all four conditions from the Route A
review: both documents installed and ratified, both role handovers revised to carry bridge sections 15
and 16 deliberately, and the transfer matrix updated with the actual commit IDs. Claude's handover v0.12
already carries that material; **the ChatGPT handover v0.9 still needs its own pass**, as the packet
itself states.
