# NEST: Locally Certified Search for Structural-Entropy Hierarchies

Code, sealed results, and LaTeX source for the TAMC 2026 paper by Dingli Su,
Yicheng Pan, and Angsheng Li (Beihang University), to appear in Springer LNCS.

NEST refines hierarchies for structural entropy with rooted nearest-neighbor
interchange (NNI). It scores every rotation with an exact weighted identity,
certifies one-NNI local optimality, and escapes shallow traps with a bounded
two-move search. An exact O(3^n) subset dynamic program audits optimality on
small graphs.

## Paper

- Camera-ready: `submission/TAMC2026_NEST_camera_ready/NEST_TAMC2026_camera_ready.pdf`
  (12 pages), with proofs and extra evidence in `..._with_appendix.pdf`.
- Source: `paper/se-hier-nni/main.tex` (main) and `main-with-appendix.tex`.

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error paper/se-hier-nni/main.tex
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error paper/se-hier-nni/main-with-appendix.tex
```

## Reproducing the results

```bash
python -m venv .venv && .venv/bin/pip install -e '.[dev,extra]' seaborn
.venv/bin/pytest -q
git clone https://github.com/Hardict/HCSE external/HCSE && git -C external/HCSE checkout ccf832e
```

The official HCSE/BBM implementation must sit at `external/HCSE` (commit
`ccf832e`). Every paper number comes from a file in `results/`:

| Paper element | Result file | Generator / verifier |
|---|---|---|
| Table 1, Fig. 2, Table 2, Table 3, macros | `results/scale-audit-20260810/`, `results/nni_restart_fairness.json` | `scripts/make_nni_scale_submission_artifacts.py`, `scripts/verify_nni_scale_audit.py` |
| Q3 purity | same | `scripts/make_purity_macros.py` |
| Certificate, binary trees, parameters | `results/nest_certificate_audit.json`, `results/nest_compound_sensitivity.json` | `scripts/audit_nest_certificate.py`, `scripts/sensitivity_compound.py`, `scripts/make_review3_macros.py` |
| Fresh rerun check | `results/camera-ready-repro-20260926/` | `scripts/compare_camera_ready_repro.py` |
| Appendix basin and ablation tables | `results/nni_basin_*.json`, `results/nni_ablation.json` | `scripts/verify_nni_basin_audit.py`, `scripts/verify_nni_supplements.py` |

Rerun a main-benchmark block or an exact-audit block with, for example:

```bash
.venv/bin/python scripts/run_nni_benchmark.py --seed-start 1000 --seeds 100 --regimes clean --output out.json
.venv/bin/python scripts/run_nni_restart_fairness.py --seed-start 160 --seeds 50 --budget 32 --campaign-seed 20260810 --max-nodes 12 --output exact12.json
```

NEST, HCSE, Paris, and the SE constructors reproduce bit-for-bit. BBM's
internal clustering is unseeded and varies by up to about 0.1 bits between runs.

## Layout

- `selib/` — structural-entropy library, including the NNI refinement (`selib/htree.py`)
  and the exact dynamic program (`selib/optimality.py`).
- `scripts/` — experiment runners, verifiers, and table/figure generators.
- `results/` — sealed per-graph records with SHA-256 seals.
- `paper/se-hier-nni/` — LNCS manuscript, generated tables, and figures.
- `docs/` — claim ledger, novelty audit, and artifact manifest.
- `submission/` — the anonymous review PDF and the camera-ready PDFs.

## License

MIT (see `LICENSE`).
