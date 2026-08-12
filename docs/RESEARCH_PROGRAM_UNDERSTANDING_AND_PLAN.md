# Research program understanding and acceleration plan

Last reviewed: 2026-08-12 (Asia/Shanghai)

## Program map

The program has three deliberately separate layers.

1. **Research Portal** is the private operations and evidence index.  It is a
   static, Git/JSON-backed renderer that reads project cards and safely probes
   status.  It is not a project-code repository or a control plane.  The
   public service on port 8899 must stay read-only and free of unpublished
   material, credentials, pane output, and terminal input.
2. **NEST / `selib`** is the reusable structural-entropy implementation and
   evidence base.  It owns algorithms, tests, validators, exact-audit records,
   and reproducible experiment scripts.
3. **The publications are two different scientific products.**  The TAMC paper
   is an anonymous, compact theory/algorithm paper about exact weighted NNI
   search and finite sealed audits.  The TCS article is a material extension:
   a constrained complexity boundary, exact subtree-graft calculus,
   neighborhood containment and certificate, NEST-G, and a disjoint frozen
   confirmation.  The TCS story must not be presented as extra prose or seeds
   for the TAMC result.

## Current truth

### Portal

- The mobile-notifier/terminal work is committed on
  `codex/portal-handoff-mobile-ops`; the local handoff documents specify
  notifier dry-run, a loopback-only authenticated PWA, and a separate private
  terminal plane.
- Production is intentionally unchanged.  Initial notification channel,
  allowed identity, deployment topology, real delivery, terminal access, DNS,
  and external publishing are human approval gates.
- The next engineering sequence is security-first: baseline tests and
  threat-model decision, dry-run events, one approved delivery adapter,
  authenticated read-only pane view, then a separate allow-listed terminal
  gateway.

### TAMC

- The chosen anonymous LNCS review package has passed the mechanical and
  scientific gates in its handoff record.  The source is frozen at upstream
  `selib` commit `7e93199e0093212f2098ad87fc5183e56d865376`.
- The TAMC 2026 site currently lists an extended deadline of **10 August 2026**;
  it requires original work, double-blind review, LNCS formatting, and at most
  12 pages including references (optional appendix excluded).
- Upload remains an author action: author metadata, conflict/overlap
  attestations, the exact uploaded file, and receipt must be resolved by the
  human owner.  Do not make the TCS extension simultaneous with an overlapping
  TAMC submission without a policy decision.

### TCS

- The current 19-page Elsevier draft has a valid journal-level architecture and
  passed its current mechanical package checks.  Its upstream source is pinned
  at `85bef2ce785e703288d5adde2232f87e7549c085`.
- The key remaining scientific gate is a frozen 100-graph exact confirmation
  of NEST-G against the rotation-only baseline.  The current protocol fixes
  graphs, seeds, starts, endpoints, and its falsifier.
- `scripts/run_tcs_graft_confirmation.py` and `selib/htree.py` are frozen for
  v1.  Their expected SHA-256 values are enforced by the runner.  A null or
  negative outcome narrows the empirical claim; it does not invalidate the
  scoped theory or license retuning.
- Human-only metadata (authors, affiliation, corresponding author, funding,
  conflicts, archival/overlap status, and approval of the AI declaration) is
  unresolved and must not be invented.

## Acceleration plan

### 0. Keep lanes independent

- Use one repository and one evidence ledger per paper; cite provenance across
  them instead of copying claims informally.
- Keep all experiment output, source hashes, analysis reports, manuscript
  edits, and package hashes on the same branch/revision chain.
- Create a portal card only after an exact project commit and durable report
  exist; status pages should link, not duplicate implementation content.

### 1. Start TCS empirical execution safely

1. Verify repository head/dirty state and the two frozen hashes.
2. In an isolated Linux CPU environment, run `tests/test_nni.py` and a one-graph
   smoke run to a separate temporary output.
3. If the smoke is clean, run one resumable process for the 100-record v1
   artifact.  Do not alter parameters or inspect partial outcomes to tune.
4. Independently validate record count, regime/seed coverage, hashes,
   certificates, exact-hit tolerances, numeric finiteness, and artifact SHA.
5. Produce paired statistics and an explicit positive/null/negative decision.
6. Update manuscript, claim ledger, journal-delta record, and gap report
   together; then rebuild, visually inspect, and hash the same revision.

### 2. Make the TCS theorem spine submission-safe

- Perform an independent proof audit of the cubic Minimum Bisection source,
  NP membership/threshold representation, balanced affine identity,
  changed-incidence cancellation, NNI-as-graft mapping, and natural termination
  versus a round cap.
- Keep all restricted quantifiers in the abstract and introduction.  Do not
  claim unrestricted TREE-SE hardness, a general approximation ratio, global
  optimum, or population-level NEST-G gains without matching proof/evidence.

### 3. Preserve and close the TAMC lane

- Treat its package as a release candidate, not a drafting sandbox.
- Before any upload, re-check the current official EasyChair instructions,
  perform the double-blind artifact gate against the exact PDF, and obtain the
  author-owned attestations.
- After an outcome, record the exact submission/decision and retain the TCS
  extension disclosure and overlap analysis.

### 4. Advance portal engineering with explicit security choices

- Run the existing tests and capture a production baseline before any rollout.
- Keep notifier delivery in dry-run mode until the owner chooses one channel.
- Default mobile PWA deployment to authenticated Tailscale HTTPS; keep port
  8899 static and public-read-only.  Add phone terminal access only through a
  separate allow-listed, audited, private gateway.
- Stage on a separate checkout/port; test redaction, cooldown/deduplication,
  proxy identity, origin checks, revocation, background reconnect, and rollback
  before any production action.

## Standalone repositories created locally

- `nest-tamc-2026` — commit `ce4303e`; independent TAMC source, evidence,
  tests, submission artifact, and double-blind scope rules.
- `nest-tcs-journal` — commits `d3b1eff` and `383409a`; independent TCS source,
  frozen protocol, results, tests, and extension-specific governance.  The
  frozen hashes match the protocol in this copy.

Neither repository has a remote or has been published.  Publishing, remote
creation, merge, submission, or deployment remains a separate approval.
