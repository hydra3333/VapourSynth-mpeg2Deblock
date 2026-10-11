# Claude review - step 3 release workflow candidate v0.3 (ZIP-only, diff check)

File: Claude_REVIEW_OF_ChatGPT_Step3_Release_Workflow_Candidate_v0_3.md
Version / date: v0.1 / 2026-10-11
Author: Claude (migration chat, independent reviewer)
Reviewed: StageBPlus_Step3_RELEASE_ZIP_ONLY_CANDIDATE_FOR_CLAUDE_v0_3.zip (6 files plus PACKAGE_SHA256.txt), diffed against my reviewed v0.2.

## 1. Verdict

READY, WITH ONE SMALL ROBUSTNESS FIX (Z1) AND ONE DECISION FOR DAVE (Z2: licence files in the ZIP).

## 2. Checks

- SHA-256: 6/6 OK. The workflow is ASCII with CRLF and has 0 trailing-whitespace lines. The CSV is unchanged.
- The preimage equals my reviewed v0.2. The live file at `0c9bf90`, fetched read-only, also equals v0.2, so what is deployed is what I approved.
- The diff is additions only: the header (2 lines), one new packaging step and the reworked attach step. Everything proven is unchanged.

| Question | Result |
|---|---|
| ZIP contents | Both inputs must exist and be non-empty. Membership must be exactly the 2 root names, compared with `Compare-Object`, which outputs nothing when the sets are equal. Each entry is hashed after unpacking and compared with the verified build output. Streams and the SHA256 object are disposed in `finally`. Correct. |
| Fail-closed | Packaging is `if: success()`, so any earlier failure means no ZIP. Evidence upload is still `always()`. Attach still needs `success()` and `release`/`published`, and now also re-checks that the ZIP's name, size and SHA-256 match the manifest. A manual run can never attach. Correct. |
| Naming | `mpeg2Deblock-<tag>-win-x64.zip`, with characters outside `[A-Za-z0-9._-]` replaced by `_`. The packaging and attach steps compute the name the same way. Manual runs use `manual-<sha12>`, in the artifact only. Correct. |
| No second build path | Only already-verified files are copied and zipped. No flags, no rebuild. Correct. |
| PDBs | Kept in the Actions artifact (`Release_Binaries/`) and never in the ZIP. Correct, as Dave wanted. |

## 3. Fix

**Z1. Load the ZIP type explicitly.** Add `Add-Type -AssemblyName System.IO.Compression.FileSystem` before `[System.IO.Compression.ZipFile]::OpenRead`. Unverified: under PowerShell 7 this type is often available only because `Compress-Archive` loaded it first, which is an accidental dependency. The line is harmless if the type is already loaded. If it is missing, the step fails closed (no release asset), but it would block a release for a trivial reason.

## 4. Decision for Dave

**Z2. Put `LICENSE` and `NOTICE.md` in the ZIP (4 files, not 2).**
- The binaries are AGPL-3.0-or-later. Section 4, which Section 6 applies to object code, asks for a copy of the licence to be given to recipients along with the program. Both files exist in the repo root today: `LICENSE` is the AGPL text, and `NOTICE.md` covers the MPEG reference-decoder notices and the `VHSC_samples` exclusion.
- GitHub's automatic source archives already provide the Corresponding Source, but those are separate downloads.
- Adding the two text files is the usual and safest practice. The membership check would then expect 4 names.
- I am not a lawyer; this is the conventional reading. If Dave keeps the ZIP to EXE and DLL only, the repo LICENSE is still one click away, but the ZIP alone would then carry no licence.

## 5. Gate (as before, now for the ZIP)

1. Run manually on `main`. The artifact must contain:
   - `Release_Package/mpeg2Deblock-manual-<sha>-win-x64.zip`;
   - `release_distribution_zip_sha256.txt`;
   - the 4 binaries and PDBs in `Release_Binaries/`.
   There must be no attach.
2. With Dave's go: publish a new **pre-release** on a `main` commit. Pass criteria:
   - the ancestry PASS line appears;
   - all checks PASS;
   - exactly **one** ZIP is attached;
   - its SHA-256 equals the run's manifest;
   - its unpacked files equal the run's `Release_Binaries`.
3. I have not seen the evidence from the earlier `TESTONLYTOBEDELETED` v0.2 release run. The v0.3 runs above become the step 3 gate. Keeping or deleting the old test release is Dave's call.
