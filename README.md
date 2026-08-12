# NEST — TAMC 2026 paper package

This repository is the standalone, double-blind TAMC 2026 submission line for
**“NEST: Locally Certified Search for Structural-Entropy Hierarchies.”**

It is intentionally independent from the journal-extension repository.  Its
scope is the exact weighted rooted-NNI calculus, NEST, the finite exact audits,
and the sealed empirical evidence.  It must not absorb the later NEST-G graft
theory or journal-only claims.

## Status

- Upstream provenance: `SuuTTT/selib`, commit
  `7e93199e0093212f2098ad87fc5183e56d865376` (`Freeze submitted NEST TAMC 2026 paper`).
- Review artifact: `submission/TAMC2026_NEST/NEST_TAMC2026_anonymous_with_appendix.pdf`.
- Main source: `paper/se-hier-nni/main.tex`; the optional proof appendix is
  enabled by `paper/se-hier-nni/main-with-appendix.tex`.
- The official TAMC page currently lists 10 August 2026 as the extended paper
  deadline.  Do not assume the submission system accepts late uploads or submit
  anything without an author instruction.

## Evidence and governance

`docs/CLAIM_PROOF_LEDGER.md`, `docs/NOVELTY_AUDIT.md`,
`docs/PAPER_AUDIT_GATE.md`, and `docs/ARTIFACT_MANIFEST.md` define the claim
boundaries, prior-art record, audit status, and canonical hashes.  The raw
versioned results under `results/` are the source of truth for numeric claims.

Before modifying prose or evidence, read `PROJECT_CONTEXT.md`.  A change that
would overlap materially with the TCS/NEST-G manuscript requires an explicit
publication-policy decision; do not create concurrent overlapping submissions.

## Build

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error paper/se-hier-nni/main.tex
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error paper/se-hier-nni/main-with-appendix.tex
```

For code validation, install the project with the `dev` extra and run
`pytest -q`.  Re-run the hash and visual gates before replacing a canonical
artifact.

## Repository layout

- `paper/se-hier-nni/` — LNCS manuscript, tables, figures, and bibliography.
- `docs/` — proof ledger, novelty review, submission and artifact records.
- `results/` — sealed audit records.
- `scripts/`, `selib/`, `tests/` — reproducibility implementation and tests.
- `submission/` — chosen review artifact and its verification record.
