# Claude diff-only clearance: ChatGPT role handover v0.8 install candidate (v0.1)

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: `ChatGPT_Handover_v0_8_CORRECTED_INSTALL_CANDIDATE_FOR_CLAUDE_DIFF_REVIEW.zip`
Input review: `Claude_REVIEW_OF_ChatGPT_Handover_v0_8_v0_1.md` (SHA-256 `7bbfe851...09cf`, unchanged)
Baseline: `35cd543b459a5856688f7c3795f73226e72311f8`
Scope: diff-only. **Not a review of the P0 S4 candidate**, which remains unseen and uncleared.

## 1. Verdict

**CLEARED FOR INSTALLATION.** No MUST, no SHOULD. Every finding from the continuity review is applied
correctly and nothing else of substance changed.

- **Both MUSTs fixed** (M1 identity, M2 the V1-V4 pointer), M2 using the suggested replacement sentence.
- **All five SHOULDs applied** (S1 install-true status, S2 the false parenthetical, S3 the
  `--check` caveat, S4 the six durable operational rules, S5 Claude v0.10).
- **OPTIONAL O1 applied.**
- **One addition beyond the review, and it is a genuine improvement:** the agreed common
  continuity-purpose text, quoted and **verified verbatim** against its owning file.
- **No technical content changed.** All S2-I3 and P0 figures, tables, hashes, scope statements and
  gate descriptions are byte-identical to the version Claude verified in detail.

## 2. Mechanical verification

| Check | Result |
|---|---|
| Manifest | 3 entries, **all 3 hashes match** |
| Install candidate | US-ASCII, 511/511 CRLF, zero trailing whitespace, zero tabs |
| Identity text in the install candidate | **none** (section 3.1) |
| Change scope | 10 hunks, 52 lines added, 16 removed, in one file |
| ChatGPT's supplied patch versus Claude's independent diff | **exactly identical change-set**: 52 added and 16 removed on both sides, zero lines in one and not the other |
| Technical figures | spot-checked and unchanged: `1619/1619`, `25635/25635`, pair `140/228` and `268/300`, index hashes `4f3821b5...`, `e6f556dd...`, transform mix `70.9/12.1/17.0`, seam excess `+19.5%`, NONE `1.9-9.4%`, harm `2.244` |
| Files proposed for installation | exactly one, `docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md` |
| `REVIEW_ONLY/` | correctly outside the install tree; **must stay untracked** (section 3.2) |

## 3. Finding-by-finding confirmation

### 3.1 M1 - identity, fixed

The date line is now bare (`**Date:** 2026-10-17`). A scan of the whole package for the owner's name,
the location string, the e-mail and a UTC-offset pattern returns **no hit in the install candidate**.

**One note, not a finding.** The single package-wide hit is inside
`REVIEW_ONLY/CHATGPT_HANDOVER_v0_8_REVIEW_TO_INSTALL_DIFF.patch`, which necessarily quotes the removed
line as a deletion. That is correct and unavoidable for a patch that documents the fix, and
`REVIEW_ONLY/` is already excluded from Git. It is worth stating explicitly only because this is the
same category as the earlier S2-I3 review patch that carried removed location text: **the patch must
never be committed.** Claude's own review redacted the string for the same reason.

### 3.2 M2 - the V1-V4 pointer, fixed

The dangling reference to the about-to-be-deleted v0.7 is replaced with the suggested sentence,
pointing at ratified authority: V1 in K-03, V2 in K-04, V3 in K-10, V4 in K-11 of
`06_DEBLOCK_CONCEPT.md`, with the Claude handover named as a second live home for the source line
references. Claude confirmed those four K items do carry the corresponding `CDR V1`-`V4` and `RR ... V4`
source citations, so the pointer is live and will survive the install.

### 3.3 SHOULD items, all applied

- **S1.** The Status line now reads "CURRENT CHATGPT ROLE HANDOVER on installation under D-23 v1.2; a
  continuity record, **not** technical or design authority", and "Supersedes when accepted" became
  "Supersedes in the current tree". Both are **true at the installing commit**, which closes the
  install-time wording class for this document. The v0.7 change-log entry and the supersession table
  were updated to match, so the document is internally consistent about its own status.
- **S2.** The incorrect "(review-file suffix added to this candidate only)" parenthetical is removed.
  The candidate filename equals the intended installed filename, and the ZIP isolates it under
  `HANDOVER_INSTALL_CANDIDATE/`. Naming is now unambiguous.
- **S3.** Section 8 now states "**Do NOT use `git diff --cached --check` as a STOP gate**", with the
  reason (legitimate CRLF evidence under `experiments/stage2/results/` and Markdown two-space hard
  breaks) and the provenance (established in S2-I2 Step B). The command is also removed from the list
  of routine discipline commands, which is the right treatment.
- **S4.** A new section 3.4 carries all six items, accurately:
  - the six-index local regression trigger, with the `.filters` exemption and the infrastructure-only
    LP smoke run, and correctly marked as **not** CI checks;
  - the destructive `TESTING` BAT side effect, with the `git add -A` warning and the correct note that
    the S2-I3 scratch procedure must never write into `VHSC_samples`;
  - `core.autocrlf=true` and the dual-hash representation rule, including the exact worked example
    (`139f02c6` working-tree CRLF versus `f9892039` Git-stored LF) and the `results/** -text` pin;
  - the `git ls-files --eol` check showing `-text`, with the expected `7 A / 0 M / 0 D`;
  - the `plugin_version.h` bump and the `merge-base --is-ancestor` release guard;
  - AVX2 with no runtime detection and no fallback.
- **S5.** Both places are corrected. Section 2.2 now says v0.9 was the installed companion at
  `35cd543` and that Claude **delivered v0.10 on 2026-10-17** at the same baseline as an owner-review
  draft, to be checked for subsequent installation. The supersession table row matches. The
  uncommitted status of v0.10 is correctly distinguished from the committed v0.9.
- **O1.** The four omitted commits are restored to the abbreviated history, with `bfaed24` correctly
  annotated as the commit that installed Claude handover v0.9. Claude verified all four from the live
  repository: `eac5526`, `bfb6cc2`, `bfaed24`, `10956a1`, in the right order.

### 3.4 The addition: common continuity-purpose text

ChatGPT added the agreed shared purpose text, which the earlier v0.8 lacked. Claude verified it
**verbatim** against `docs/HANDOVER/ROLE_HANDOVER_CONTINUITY_PURPOSE_TEXT_FOR_BOTH_ROLES.md` after
whitespace normalisation: the 1,501-character quotation is an exact substring of the owning file.

This is the right addition. That file's own instruction is to keep the text "in every future version
of both" role handovers, and v0.7 carried it while the first v0.8 draft had dropped it. Claude
confirmed its own v0.10 carries the same text verbatim, so **the two handovers now agree exactly** on
this block.

## 4. OPTIONAL (no action needed)

**O1. The supplied patch is documentation, not machine-applicable.** Its headers are descriptive
labels (`--- v0.8_FOR_CLAUDE_REVIEW (original)` / `+++ v0.8_INSTALL_CANDIDATE (corrections)`) rather
than paths, so `patch -p0` and `-p1` both refuse it. This cost nothing here, because Claude produced
its own diff independently and the two change-sets proved identical. For future packages, real
relative paths in the headers would let the reviewer apply and verify in one step.

**O2. The owner's own purpose statement is not carried.** Claude's handover quotes the owner's
2026-10-12 verbatim statement of what the handover is for, marked "keep it in every future version".
That instruction was given for the Claude handover, and the shared text is the part required in both,
so this is not a gap. ChatGPT may wish to carry it anyway, since it is the clearest statement of the
owner's expectation.

**O3. Header formatting changed incidentally.** The header switched from trailing-two-space Markdown
hard breaks to blank-line separated lines. That accounts for part of the line-count growth and has the
small side benefit of removing trailing whitespace from the header, which is consistent with S3's
subject matter. No action.

## 5. Install path

1. The owner ratifies this corrected candidate.
2. A separate bounded documentation commit **adds**
   `docs/HANDOVER/ChatGPT_Handover_To_Future_ChatGPT_MPEG2_Deblocking_Project_v0_8.md` and **deletes**
   `..._v0_7.md`, under D-23 v1.2. Expect **1 A / 1 D** from
   `git diff --cached --name-status --no-renames`.
3. Stage by exact name. Do not copy `REVIEW_ONLY/` anywhere near the repository, and do not use
   `git diff --cached --check` as a gate - the document now says so itself.
4. Claude verifies the pushed commit from GitHub, as for every previous commit. Expected installed
   SHA-256, in the LF form Git will store, can be confirmed after the push; the CRLF working-copy form
   of the candidate is `1ce5d3313270b8148ac48f11d9a1cb728e3bb7db9894bdc07052db7c3d8f94eb`.

**Claude still recommends two separate commits** for the two handovers, so each is verified on its
own. Claude's v0.10 remains a draft awaiting the owner's read, so the ChatGPT v0.8 commit need not
wait for it.

**Nothing here touches P0.** The revised P0 candidate remains cleared, and the S4 one-file variant has
still not been supplied to Claude.
