# Claude independent review request - S2-I2 closure v0.3 / Step-B placement v0.2

**Date:** 2026-10-16
**Status:** Drafts only; do not install, stage, modify or delete project files until owner ratification.

## Input corrections from Claude closure-note v0.2 review

- MUST M1: accepted v0.1 nine-file code commit **DONE, PUSHED, VERIFIED**: `190bd06ded88130ffddac7bb9adde4175d82f9f8`, parent `2286341`. Check report sections 2, 6, 8. No candidate-ZIP-as-provenance reliance.
- SHOULD S1: owner `core.autocrlf=true`; the proposed single `.gitattributes` rule `experiments/stage2/results/** -text` preserves all 25 original Windows SHA-256s in working/Git/GitHub representations, per Claude's own rehearsal. Confirm scope and owner-decision treatment; no action taken.
- SHOULD S2: reader v0.2 SHA CRLF owner working `139f02c6...6f6` vs Git/GitHub LF `f9892039...fe21`, engine/adapter LF; label all representation claims.
- SHOULD S3: check 12 moved docs, the conditionally cleared Copilot research document, 25 evidence files, `.gitattributes` modification, installed gate report and ratified status v0.6 replacement; exclude process artifacts and scratch index.
- OPTIONAL O1/O2: cite code commit rather than candidate ZIP; document `core.autocrlf=true` implications of new checkouts.

## Requested gates

1. Independently compare v0.3 report with v0.2: ensure none of the ratified registration results, source/index identities, sample dispositions, thresholds, limitations, and 25 original Windows evidence hashes changed. Verify that the report accurately marks code commit as COMPLETE and Step B as pending.
2. Check the proposed `-text` attribute matches actual root `.gitattributes` syntax and has no side effects outside the evidence subtree. If the owner declines, the Windows-only-hashes fallback must be accurate. Check cross-platform hash representation labels.
3. Verify all 12 owner-moved docs names, conditional research gate, evidence path list (12 LP, 13 LP_blocky), no `.idx`, one installed gate report, one status addition and one status removal; verify exact staged-scope counts and identify any newly present/untracked review file.
4. Review Step-B disposition of three REVIEW_REQUESTs, four implementation-package documents (including the implementation review request), candidate manifest, closure ZIP(s), original `Z/` archive, and `research/`, without any implicit deletion.
5. **Status v0.6 not supplied in this package.** It cannot safely be drafted from the previously shared unratified v0.5 draft; require the ratified repo v0.5 and actual HEAD from owner's local repository before drafting/ratifying it. Do not treat absence as Stage 2 / S2-I3 authorisation.
6. Confirm Step-B remains uncommitted; review and owner ratification before any named-staging procedure. S2-I3 is NOT AUTHORISED.

## Proposed Step-B Git counts (with pin, after all required clearances)

- 40 additions: 12 previously moved docs, 1 conditional Copilot source, 25 evidence outputs, 1 report, 1 status v0.6.
- 1 modification: root `.gitattributes` (one appended scoped line only).
- 1 deletion: old Project Status v0.5.
- If Copilot research not cleared: 39 additions / 1 modification / 1 deletion.

**No command execution requested of owner now.**
