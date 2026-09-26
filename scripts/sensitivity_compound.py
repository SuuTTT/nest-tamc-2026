"""Sensitivity of NEST to its compound-search settings (Reviewer 3, item 2).

Reruns the deterministic NEST pool on the frozen 50-graph ablation subset
(seeds 0-9 per regime) under one-factor-at-a-time changes to the beam width
b, barrier beta, and compound-round cap R, and compares each setting with the
paper default (b=16, beta=0.05, R=8).  Writes
``results/nest_compound_sensitivity.json``.
"""
import json
import multiprocessing as mp
import os
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from run_nni_benchmark import hierarchical_sbm  # noqa: E402
from selib.htree import encoding_tree_nni_fast, hd_se  # noqa: E402

REGIMES = ["clean", "noisy", "imbalanced", "weighted", "weak-hierarchy"]
DEFAULT = {"beam_width": 16, "barrier_bits": 0.05, "compound_rounds": 8}
SETTINGS = [
    ("default", DEFAULT),
    ("b=4", {**DEFAULT, "beam_width": 4}),
    ("b=64", {**DEFAULT, "beam_width": 64}),
    ("beta=0.01", {**DEFAULT, "barrier_bits": 0.01}),
    ("beta=0.2", {**DEFAULT, "barrier_bits": 0.2}),
    ("R=2", {**DEFAULT, "compound_rounds": 2}),
    ("R=32", {**DEFAULT, "compound_rounds": 32}),
]


def run(job):
    regime, seed, name, params = job
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    graph, _, _, _ = hierarchical_sbm(regime, seed)
    root, _, _, vol = encoding_tree_nni_fast(graph, seed=seed, starts=4,
                                             compound=True, **params)
    return {"regime": regime, "seed": seed, "setting": name, "h": hd_se(root, vol)}


def main():
    jobs = [(r, s, name, params) for r in REGIMES for s in range(10)
            for name, params in SETTINGS]
    with mp.Pool(max(1, (os.cpu_count() or 2) - 2)) as pool:
        rows = pool.map(run, jobs, chunksize=2)
    base = {(r["regime"], r["seed"]): r["h"] for r in rows if r["setting"] == "default"}
    summary = {}
    for name, params in SETTINGS:
        diff = np.array([r["h"] - base[(r["regime"], r["seed"])]
                         for r in rows if r["setting"] == name])
        summary[name] = {
            "params": params,
            "mean_h": float(np.mean([r["h"] for r in rows if r["setting"] == name])),
            "mean_change_vs_default": float(diff.mean()),
            "max_abs_change": float(np.abs(diff).max()),
            "graphs_lower": int((diff < -1e-10).sum()),
            "graphs_higher": int((diff > 1e-10).sum()),
        }
    out = ROOT / "results" / "nest_compound_sensitivity.json"
    out.write_text(json.dumps({"summary": summary, "records": rows}, indent=1))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
