"""Compare the 2026-09-26 fresh reruns with the sealed August records.

Deterministic methods must match to floating-point noise; BBM's internal
clustering is unseeded, so its drift is reported against the smallest sealed
winning margin of NEST over the better of HCSE and BBM.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
NEW = ROOT / "results" / "camera-ready-repro-20260926"
SEALED = ROOT / "results" / "scale-audit-20260810"
REGIMES = {"clean": "clean", "noisy": "noisy", "imbalanced": "imbalanced",
           "weighted": "weighted", "weak-hierarchy": "weak"}
DETERMINISTIC = {"SE-NNI-fast", "HCSE", "Paris", "SE-agglomerative", "se_hier"}


def records(path):
    return json.loads(path.read_text())["records"]


def main():
    drift, graphs = {}, set()
    for new_name, old_name in REGIMES.items():
        sealed = {(r["seed"], r["method"]): r for r in records(SEALED / f"n64-{old_name}.json")}
        for rec in records(NEW / f"n64-{new_name}.json"):
            graphs.add((new_name, rec["seed"]))
            old = sealed[(rec["seed"], rec["method"])]
            d = abs(rec["nni2_h"] - old["nni2_h"]) if rec["method"] == "SE-NNI-fast" else abs(rec["raw_h"] - old["raw_h"])
            drift[rec["method"]] = max(drift.get(rec["method"], 0.0), d)
    min_margin = float("inf")
    for old_name in REGIMES.values():
        by = {}
        for r in records(SEALED / f"n64-{old_name}.json"):
            by.setdefault(r["seed"], {})[r["method"]] = r
        for m in by.values():
            margin = min(m["HCSE"]["raw_h"], m["BBM"]["raw_h"]) - m["SE-NNI-fast"]["nni2_h"]
            min_margin = min(min_margin, margin)
    exact_bad = exact_n = 0
    for new_name, old_path in [("exact12_paper.json", ROOT / "results" / "nni_restart_fairness.json"),
                               ("exact14.json", SEALED / "exact14.json")]:
        sealed = {(r["regime"], r["graph_seed"]): r for r in records(old_path)}
        for rec in records(NEW / new_name):
            old = sealed[(rec["regime"], rec["graph_seed"])]
            exact_n += 1
            same = abs(rec["global_optimum_bits"] - old["global_optimum_bits"]) < 1e-12
            for m in ("NEST-R32", "NEST-coalescent-B32"):
                same &= rec["outcomes"][m]["globally_optimal"] == old["outcomes"][m]["globally_optimal"]
                same &= abs(rec["outcomes"][m]["entropy_bits"] - old["outcomes"][m]["entropy_bits"]) < 1e-9
            exact_bad += not same
    for m, d in sorted(drift.items()):
        print(f"{m:18s} max |dH| = {d:.2e}")
    print(f"n64 graphs rerun: {len(graphs)}; smallest sealed winning margin: {min_margin:.4f} bits")
    print(f"exact graphs rerun: {exact_n}; H* or NEST outcome mismatches: {exact_bad}")
    assert all(drift[m] < 1e-9 for m in DETERMINISTIC), drift
    assert drift["BBM"] < min_margin and exact_bad == 0
    print("PASS")


if __name__ == "__main__":
    main()
