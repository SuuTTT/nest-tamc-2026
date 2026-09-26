"""Audit the one-NNI certificate on NEST's returned trees (Reviewer 3, items 1-3).

For every sealed 64-vertex graph this reruns the deterministic NEST pool
(``encoding_tree_nni_fast`` with the paper's settings) and records:

* which initializer produced the returned tree;
* whether the returned tree is binary, and how many multiway nodes it keeps;
* the most negative exact NNI delta left on any eligible binary edge
  (the certificate holds when it is >= -tol);
* whether that tree reproduces the sealed entropy.

Writes ``results/nest_certificate_audit.json``.
"""
import argparse
import json
import math
import multiprocessing as mp
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from run_nni_benchmark import hierarchical_sbm  # noqa: E402
from selib.htree import (  # noqa: E402
    _descendant_vertices, _nni_candidates, annotate, encoding_tree_nni_fast,
    hd_se, nni_delta,
)

TOL = 1e-10
REGIMES = {"clean": "clean", "noisy": "noisy", "imbalanced": "imbalanced",
           "weighted": "weighted", "weak-hierarchy": "weak"}


def tree_shape(root):
    internal = multiway = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node.is_leaf():
            continue
        internal += 1
        multiway += len(node.children) > 2
        stack.extend(node.children)
    return internal, multiway


def audit_one(job):
    regime, seed = job
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    graph, _, _, _ = hierarchical_sbm(regime, seed)
    root, deg, adj, vol, audit = encoding_tree_nni_fast(
        graph, seed=seed, starts=4, compound=True, return_trace=True
    )
    annotate(root, deg, adj, vol)
    leaves = _descendant_vertices(root)
    deltas = [nni_delta(root, p, c, adj, vol, leaves=leaves)
              for p, c in _nni_candidates(root)]
    deltas = [d for d in deltas if d is not None]
    internal, multiway = tree_shape(root)
    return {
        "regime": regime,
        "seed": seed,
        "entropy": hd_se(root, vol),
        "selected_initializer": audit["selected_initializer"],
        "internal_nodes": internal,
        "multiway_nodes": multiway,
        "binary": multiway == 0,
        "eligible_nni_moves": len(deltas),
        "min_nni_delta": min(deltas) if deltas else math.inf,
        "certified": (min(deltas) if deltas else 0.0) >= -TOL,
        "descent_moves": sum(s.get("kind", "descent") == "descent"
                             for s in audit["selected_trace"]),
        "compound_moves": sum(s.get("kind") == "compound"
                              for s in audit["selected_trace"]),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    parser.add_argument("--seeds", type=int, default=100)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "results" / "nest_certificate_audit.json")
    args = parser.parse_args()
    jobs = [(regime, seed) for regime in REGIMES
            for seed in range(1000, 1000 + args.seeds)]
    with mp.Pool(args.workers) as pool:
        rows = pool.map(audit_one, jobs, chunksize=4)

    sealed = {}
    for regime, stem in REGIMES.items():
        path = ROOT / "results" / "scale-audit-20260810" / f"n64-{stem}.json"
        for rec in json.loads(path.read_text())["records"]:
            if rec["method"] == "SE-NNI-fast" and rec.get("status") == "ok":
                sealed[(regime, rec["seed"])] = rec["raw_h"]
    for row in rows:
        row["matches_sealed"] = abs(row["entropy"] - sealed[(row["regime"], row["seed"])]) < 1e-9

    summary = {
        "graphs": len(rows),
        "certified": sum(r["certified"] for r in rows),
        "binary": sum(r["binary"] for r in rows),
        "matches_sealed": sum(r["matches_sealed"] for r in rows),
        "selected_initializer": {},
        "max_descent_moves_selected": max(r["descent_moves"] for r in rows),
        "max_compound_moves_selected": max(r["compound_moves"] for r in rows),
        "max_multiway_nodes": max(r["multiway_nodes"] for r in rows),
    }
    for row in rows:
        key = row["selected_initializer"]
        summary["selected_initializer"][key] = summary["selected_initializer"].get(key, 0) + 1
    args.output.write_text(json.dumps({"summary": summary, "records": rows}, indent=1))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
