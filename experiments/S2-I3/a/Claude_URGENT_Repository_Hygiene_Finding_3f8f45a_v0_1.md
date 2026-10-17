# Claude URGENT finding: repository hygiene at commit `3f8f45a7`

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Author: Claude
Date: 2026-10-17
Trigger: Claude re-checked GitHub `main` while waiting for the incoming status document and found HEAD
had moved from `35cd543` to `3f8f45a7`.
Priority: **the identity findings in section 3 are time-sensitive on a public repository.**

## 1. Summary

**Good news first, because it answers the owner's actual concern.** Both role handovers are now
committed, and Claude verified they are **the exact bytes it cleared** (LF-normalised comparison
against the cleared candidates: both match). So today's knowledge **is** preserved in the repository.
The thing the owner asked to protect against is handled.

**But the snapshot commit swept in far more than the handovers, and some of it must come out.**

| # | Finding | Severity |
|---|---|---|
| 1 | **Four committed files carry the owner's city and region**, one of them as plain greppable text | **MUST, time-sensitive** |
| 2 | **D-23 v1.2 violated**: handover v0.7 and v0.9 were not deleted when v0.8 and v0.10 were added | **MUST** |
| 3 | 48 review-only artefacts committed, including **16 ZIPs**, a **54 MB copy of the repository inside itself**, and duplication of **49 MB of Restricted Media** | **MUST** |
| 4 | The four new recordings went in inside the snapshot rather than the agreed separate bounded commit | SHOULD, record only |

## 2. What happened

Two commits after `35cd543`:

| Commit | Time | Content |
|---|---|---|
| `6b7acc38168d0dea9278d1ba930bc09a174a50fe` | 17:55 | "SNAPSHOT after handovers updated" - **58 files added** |
| `3f8f45a77a8bbdd9d6bbc42718e6e74a2abd5e21` | 18:13 | "Remove handover review ZIP containing identity text" - 1 ZIP deleted |

The snapshot looks like a working-directory sweep (`git add -A` in effect). Tracked files went from
**181 to 239**; tracked bytes to **158.8 MB**.

The owner clearly spotted an identity problem himself and removed one ZIP at 18:13. **That removal was
correct but incomplete** - it caught
`ChatGPT_Handover_v0_8_CORRECTED_INSTALL_CANDIDATE_FOR_CLAUDE_DIFF_REVIEW.zip` and missed four other
carriers. The reason is instructive: a plain text search does not see inside ZIP members. This is
exactly the trap recorded in Claude's handover ("Every ZIP left in the tree needs its own scan: a
text-only scrub misses names inside ZIP members and member file names").

## 3. MUST 1 - four identity carriers in the current tree

Claude scanned every committed text file **and unpacked every committed ZIP**. Four carriers remain:

**(a) Plain text, directly searchable on GitHub - the worst of the four:**

```
experiments/S2-I3/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_1_FOR_CLAUDE_REVIEW.md
```

Line 5 is a date line with the city and region appended in parentheses. This is the S2-I3 design
v0.1 draft - the same header defect Claude raised as a MUST on that document, now committed in its
pre-correction form.

**(b) Inside committed ZIPs:**

```
experiments/S2-I3/S2_I3_v0_2_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip
    member: S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_2_FOR_CLAUDE_REVIEW.md

experiments/S2-I3/S2_I3_v0_3_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip
    member: S2_I3_v0_2_to_v0_3_Diff_FOR_CLAUDE.patch

experiments/S2-I3/ChatGPT_Handover_v0_8_FOR_CLAUDE_REVIEW.zip
    member: HANDOVER_CANDIDATE/docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md
```

Two of these were **specifically predicted**:

- `S2_I3_v0_2_to_v0_3_Diff_FOR_CLAUDE.patch` is the file Claude flagged as **O3** in
  `Claude_REVIEW_OF_ChatGPT_S2_I3_v0_3_and_Stage2_v0_7_rev_v0_1.md`: *"Do not commit the review patch
  files. `S2_I3_v0_2_to_v0_3_Diff_FOR_CLAUDE.patch` contains, as a removed line, the location text
  that M1 took out."* It is now committed, inside a ZIP.
- The v0.8 handover draft member is the **exact MUST M1** Claude raised at 17:43 today. The corrected
  install copy is clean and correctly committed; the uncorrected draft is in this ZIP.

This recurrence pattern - the same identity defect reappearing through review artefacts rather than
through the reviewed documents - is the strongest argument for keeping review material out of Git
entirely.

## 4. MUST 2 - D-23 v1.2 predecessor deletion was not done

`docs/HANDOVER/` at HEAD contains **both** versions of **both** handovers:

```
ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md   <- should have been deleted
ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md
Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md                         <- should have been deleted
Claude_HANDOVER_TO_Future_Claude_Chat_v0_10.md
ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT_FOR_BOTH_ROLES.md
```

D-23 v1.2: *"A revision is a new versioned file. The previous version is deleted from the current tree
in the same controlled change; Git history retains it until the Development Closure history scrub."*

Both clearance documents stated the expected shape as **1 A / 1 D** per handover. The adds happened;
the deletes did not. Beyond the rule, leaving both versions present is actively harmful in a handover:
a successor chat may read the superseded one.

## 5. MUST 3 - review artefacts, a repository inside itself, and duplicated media

48 further paths were added that are review correspondence, not repository content: 16 ZIPs, review
requests, `.diff` and `.patch` files, and new ad-hoc folders `experiments/S2-I3/` and `experiments/C/`.
`experiments/stage2/`, which holds **accepted code**, also gained five review artefacts
(`CLAUDE_REVIEW_REQUEST_...`, `S2_I2_IMPLEMENTATION_REHEARSAL_EVIDENCE_...`, `..._README_FOR_CLAUDE`,
`..._TRACEABILITY`, `SHA256_MANIFEST_...`), so accepted code and review scratch now sit side by side.

Two items deserve singling out:

- **`experiments/S2-I3/VapourSynth-mpeg2Deblock-main.zip` is 54.1 MB: a complete copy of the
  repository committed inside the repository.** It holds 204 members including **16 `.mpg` files
  totalling 49 MB** and the six frozen Stage 1 indexes. So all the Restricted Media now exists twice
  in the tree, once loose and once zipped. Under `NOTICE.md` that doubles what Development Closure
  must remove, and it inflates every clone.
- The remaining candidate and evidence ZIPs duplicate material that is already committed in its
  accepted form, which is precisely the "second current-tree archive merely to duplicate Git history"
  that D-23 v1.2 rules out.

The standing rule, stated in both role handovers and in several Claude reviews, is that review ZIPs
and patches stay out of the repository, and that **`git add -A` is not a safe routine default**.

## 6. SHOULD - the media commit shape

The four new recordings are committed:

```
VHSC_samples/TEST_6A_home_576i.mpg        VHSC_samples/TEST_6A_home_576i_blocky.mpg
VHSC_samples/TEST_7A_home_576i.mpg        VHSC_samples/TEST_7A_home_576i_blocky.mpg
```

The owner **authorised this**, so it is not a policy breach, and Claude recommends keeping them. But
the agreed shape was a *separate bounded commit of exactly four named paths, expecting 4 A / 0 M / 0
D*, reviewable on its own. Instead they arrived inside a 58-file sweep. Record it and move on; the
point matters only because it removes the clean audit boundary around the media decision, which is
the one the owner still has to make about history.

## 7. The limit of any fix now

Deleting these paths removes them from the **current tree**, so they leave the default GitHub view
and future source archives. **It does not remove them from history.** The identity text stays in
commit `6b7acc38` unless history is rewritten.

This is the same caveat Claude gave about the home media a few hours ago, now applying to identity
text. Two routes:

1. **Tree removal now, history purge at Development Closure.** This is already project policy: D-23
   v1.2 states that the Development Closure history scrub *"also removes owner-identifying text from
   historical commits"*. Proportionate, and nothing new needs deciding.
2. **Rewrite history now.** The owner has done this before (`11f4742`). Heavier, and it invalidates
   every existing clone.

**Claude recommends route 1**, with the Development Closure scrub explicitly noted as now carrying
these four paths. Route 2 is only worth it if the owner judges the public exposure window
unacceptable.

One small observation: the commit message "Remove handover review ZIP containing identity text" is
itself a public signpost that identity text was committed. Not worth rewriting for, but worth knowing.

## 8. Recommended remediation: three bounded commits

Keep: both handovers (cleared bytes, verified), the four authorised recordings, and everything that
was already at `35cd543`.

**Commit A - identity removal. Do this first.** Four paths, expect `0 A / 0 M / 4 D`:

```
experiments/S2-I3/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_1_FOR_CLAUDE_REVIEW.md
experiments/S2-I3/S2_I3_v0_2_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip
experiments/S2-I3/S2_I3_v0_3_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip
experiments/S2-I3/ChatGPT_Handover_v0_8_FOR_CLAUDE_REVIEW.zip
```

**Commit B - D-23 correction.** Two paths, expect `0 A / 0 M / 2 D`:

```
docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_7.md
docs/HANDOVER/Claude_HANDOVER_TO_Future_Claude_Chat_v0_9.md
```

**Commit C - review-artefact cleanup.** The remaining 44 paths added by the snapshot, after the owner
and ChatGPT agree the list. `VapourSynth-mpeg2Deblock-main.zip` should be in it on size and
Restricted-Media grounds alone. Claude will supply and check the exact path list for this one rather
than have it done by wildcard, since `experiments/stage2/` must keep its accepted code.

Claude will verify each commit from GitHub, as for every previous commit.

**Afterwards:** add a `.gitignore` rule or an agreed convention so review ZIPs cannot be swept in
again. A single `*.zip` ignore under `experiments/` would have prevented all of today's identity
recurrences.

## 9. Process lesson

Every individual document in this chain was reviewed and corrected. The leaks came in through
**review artefacts about those documents** - a superseded draft, a diff showing a removed line, and a
pre-correction candidate inside a ZIP. The corrected forms are all clean and correctly committed.

So the lesson is not "review harder". It is: **review material must not enter the repository at all**,
because a corrected document and its correction history have opposite identity properties. A diff that
removes identity text contains identity text, permanently.

For the handover lesson lists, in both roles:

> Review ZIPs, patches and superseded drafts carry identity text precisely because the corrections
> removed it. Never commit review correspondence. A snapshot commit (`git add -A`) over a working
> directory that holds review material will commit identity text that every individual document
> review has already removed. Scan inside ZIP members, not only text files, before any commit that
> touches untracked paths.
