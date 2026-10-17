# Claude verification of the S2-I3 P0 Windows run status v0.1

Project: VapourSynth-mpeg2Deblock (GitHub project owner: hydra3333)
Reviewer: Claude
Subject: `S2_I3_P0_WINDOWS_RUN_STATUS_AND_RESULTS_v0_1_FOR_CLAUDE_2026-10-17.md`
Repository HEAD at time of writing: `3f8f45a77a8bbdd9d6bbc42718e6e74a2abd5e21` (verified from GitHub)

## 1. Verdict

**CONTINUITY ACKNOWLEDGED. The handback faithfully captures the observed state. Proceed with
XP_blocky.**

Every value Claude can check independently is **correct**, and three of the checks are stronger than
the status document claims for itself (section 3). No MUST, no SHOULD. US-ASCII, no identity text.

One thing the status document does not know, because it was written before Claude re-checked GitHub:
**the snapshot cleanup is incomplete - four committed files still carry the owner's city and region.**
That is in `Claude_URGENT_Repository_Hygiene_Finding_3f8f45a_v0_1.md` and is **parallel to P0, not
blocking it.** Section 6.

## 2. P0B: all eight index identities verified against Claude's independent references

Claude compared every row of section 4's table against the allow-list it derived independently on
Linux from the frozen inspector, before any Windows run existed.

| Label | Frames | Dimensions | P-skips | SHA-256 prefix | Match |
|---|---:|---|---:|---|---|
| XP | 228 | 720x576 | 1619 | `4f3821b5086a` | **exact** |
| XP_blocky | 228 | 720x576 | 25635 | `8d0326b5975b` | **exact** |
| SP | 192 | 720x576 | 1764 | `40a97ce1a992` | **exact** |
| SP_blocky | 192 | 720x576 | 19010 | `7e19ca607807` | **exact** |
| LP | 204 | 720x576 | 1533 | `849b6a9c411a` | **exact** (frozen baseline) |
| LP_blocky | 204 | 720x576 | 20300 | `b3f1d71483bf` | **exact** |
| 3A | 300 | 704x576 | 8812 | `9a60a8d24a7e` | **exact** |
| 3A_blocky | 300 | 704x576 | 18190 | `e6f556dd4aae` | **exact** |

**All eight agree on all four quantities: full hash, frame count, dimensions and P-skip count.**

This is the cross-platform confirmation the design was built to obtain. Six indexes were produced on
Windows by the owner's MSVC-built frozen inspector and reproduce, byte for byte, what Claude produced
on Linux with a gcc build of the same frozen sources. That is strong evidence the inspector is
deterministic across toolchain and platform, and that the Stage 1 index format carries no
machine-dependent content - consistent with the earlier finding that the only readable text in an
index is the magic `S1MBIDX1`.

The status document's distinction is correct and worth preserving: **seven** indexes were actually
verified in P0B (six generated plus the LP_blocky byte copy), while **LP** is the pre-existing frozen
repository baseline and was not regenerated. Claude confirms LP's hash equals the immutable
`849b6a9c...0011`, so the frozen baseline is intact.

## 3. P0C XP: matches Claude's rehearsal exactly

| Quantity | Claude's Linux rehearsal | Owner's Windows run | |
|---|---|---|---|
| Status | REGISTERED | REGISTERED | match |
| Exact P-skips | 1619/1619 | 1619/1619 | match |
| **P pictures with qualified skips** | **54** | **54** | **match** |
| Frames | 228 | 228 | match |
| Geometry | 720x576 YUV420P8 | 720x576 YUV420P8 | match |

The P-picture count matching at 54 is the most informative of these. It is not a value either side
could have copied from the other: Claude never published it in the allow-list, which carries only
frame count, geometry and total skip count. It falls out of the display-order anchor derivation, so
agreement at 54 means the Windows run derived **the same anchor structure over the same pictures** as
the Linux rehearsal.

## 4. Runtime continuity: a check the status document did not claim

Claude compared the reported runtime against the **accepted, committed** S2-I2 `run_manifest.json`.

**The BestSource plugin binary is identical.** Reported DLL SHA-256
`fa5b9016ac55724843300e5a87d988c01a98eee87b679759d0e3f4ff3617f69c` **equals** the value recorded in
the accepted S2-I2 evidence, with the same `PluginVersion(major=22, minor=0)`. So the decoder that
produced today's admission is bit-identically the same binary that produced the accepted S2-I2
registration evidence. That matters for the P0D diagnostics step, where today's numbers will be
compared against the committed S2-I2 CSVs.

**One recorded difference, immaterial.** NumPy moved from **2.5.3** in the accepted S2-I2 evidence to
**2.5.4** today. Claude's rehearsal also used 2.5.3. This has no bearing on P0: the admission test is
an exact equality comparison on `uint8` arrays, and the pair rule uses integer-promoted absolute
differences, neither of which is sensitive to a NumPy patch release. It should simply be **recorded**
in the evidence so the P0D diagnostics comparison carries the correct runtime provenance, rather than
being discovered later as an unexplained difference.

Python itself is the embeddable **3.14.8**, which is the interpreter whose isolation behaviour caused
the P0A failure and which the corrected BAT now accommodates.

## 5. The status document's own accuracy

Claude checked the claims it could verify and found the epistemics careful throughout:

- the seven-verified versus eighth-frozen distinction is drawn correctly, in the table legend and in
  section 1;
- `EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent` is correctly called expected, and
  correctly **not** treated as permission to generate a hold-out index;
- console `REGISTERED` is correctly described as a successful run and **not** a substitute for
  examining the JSON evidence, which has not yet been supplied;
- the P0A root cause is stated correctly, including that isolated mode ignores `PYTHONPATH` - which
  Claude verified independently;
- that Claude's original S4 Linux launch test was insufficient, and that prior `python3 -I` failures
  had already exposed the issue, is recorded accurately and without softening;
- hold-out protection "regardless of filename" is correctly stated;
- `READY_FOR_P1` is correctly described as numerical only;
- the two new commits, and the fact that the removed ZIP survives in history at `6b7acc3`, are stated
  correctly.

The commit identities and the HEAD are correct; Claude re-verified them from GitHub.

## 6. The one gap: snapshot cleanup is incomplete

The status document records the snapshot and the single ZIP removal accurately, and correctly defers
cleanup. But it was written without knowledge of the following, which Claude found by unpacking every
committed ZIP:

**Four committed paths still carry the owner's city and region**, one of them as plain greppable text:

```
experiments/S2-I3/S2_I3_Full_Data_Multi_Source_Experimental_Design_v0_1_FOR_CLAUDE_REVIEW.md   (plain text, line 5)
experiments/S2-I3/S2_I3_v0_2_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip                                 (member: the v0.2 design draft)
experiments/S2-I3/S2_I3_v0_3_STAGE2_v0_7_FOR_CLAUDE_REVIEW.zip                                 (member: S2_I3_v0_2_to_v0_3_Diff_FOR_CLAUDE.patch)
experiments/S2-I3/ChatGPT_Handover_v0_8_FOR_CLAUDE_REVIEW.zip                                  (member: the uncorrected v0.8 draft)
```

Also outstanding: **D-23 v1.2 predecessor deletion was not performed** - handover v0.7 and v0.9 are
still in `docs/HANDOVER/` alongside v0.8 and v0.10, so a successor chat could read a superseded one.

Full detail, exact paths and a three-commit remediation are in
`Claude_URGENT_Repository_Hygiene_Finding_3f8f45a_v0_1.md`.

**This does not block P0.** The installed overlay is correct, the scratch evidence is intact, and the
cleanup touches only `experiments/S2-I3/` review artefacts and `docs/HANDOVER/` predecessors - none of
which P0 reads. Claude recommends continuing the admissions and doing the cleanup in parallel, since
the identity exposure is public and time-sensitive while P0 is not.

## 7. Proceed: expected values for the remaining seven admissions

One source per invocation, stopping on any FAIL or INCONCLUSIVE:

| Order | Label | Expect exact P-skips | Expect P pictures | Frames |
|---:|---|---:|---:|---:|
| 1 | XP_blocky | 25635/25635 | 55 | 228 |
| 2 | SP | 1764/1764 | 46 | 192 |
| 3 | SP_blocky | 19010/19010 | 46 | 192 |
| 4 | LP | 1533/1533 | 46 | 204 |
| 5 | LP_blocky | 20300/20300 | 50 | 204 |
| 6 | 3A | 8812/8812 | 133 | 300 |
| 7 | 3A_blocky | 18190/18190 | 73 | 300 |

The **P-picture** column is Claude's rehearsal value and was not previously published. It is a free
extra check at no cost: if exact identity passes but the P-picture count differs from the above, the
anchor derivation has diverged and that is worth stopping for even though the gate would pass.

LP must use the frozen repository index; LP_blocky must use its verified copied scratch index. Every
admission must report REGISTERED with exact identity and `ERRORLEVEL=0`.

**On evidence delivery.** Console output per source is sufficient to proceed - no need to send the
JSON files one at a time. Claude will do the full evidence examination once all eight admissions, the
eight diagnostics, the four pair tests and the summary are complete, which is the natural point for it
and avoids eight review rounds. Send the complete `results\` tree contents then. If any single source
reports anything other than REGISTERED, stop and send that source's JSON immediately.

## 8. Unchanged

No filtering. `READY_FOR_P1` is a numerical report, not authorisation. EP, TEST_2A and TEST_4A with
all their `_blocky` copies stay locked until S2-I8 under any filename. The 6A/7A recordings are
outside the allow-list and carry no role. The seven-index tracking commit is separate and follows
owner and Claude acceptance of the P0 evidence. The six frozen Stage 1 indexes must never be
rewritten, and `VHSC_samples\LG_576i_3_LP.idx` must remain unmodified.
