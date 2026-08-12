# TAMC project context

## Objective

Preserve a reproducible, submission-ready TAMC 2026 paper package while
keeping its claims at the scopes recorded in `docs/CLAIM_PROOF_LEDGER.md`.

## Non-negotiable boundaries

- The review PDF is double-blind; never add author names, affiliations,
  acknowledgements, or self-identifying wording to it.
- The main paper is limited to 12 LNCS A4 pages including references; proofs
  beyond that boundary belong only in the optional appendix.
- Finite exact-audit outcomes are not global-optimality or universal-performance
  guarantees.
- The NEST-G graft calculus, balanced-bisection complexity result, and frozen
  graft-confirmation experiment belong to the TCS extension, not this paper.
- Do not submit, withdraw, contact organizers, or make a public release
  without explicit author approval.

## Required checks before a new artifact

1. Re-run the relevant tests and deterministic result verifier.
2. Run the TAMC mechanical checker in double-blind mode.
3. Render and inspect every main and appendix page.
4. Record the Git commit, SHA-256, and artifact path in the manifest.

## Author-only decisions

The author list, EasyChair account metadata, corresponding author, competition
eligibility, and concurrent-submission attestation are human-owned facts.
