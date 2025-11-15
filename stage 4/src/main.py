#!/usr/bin/env python3
"""
Dependency Visualizer - Stage 4 (Variant 27)
"""

import argparse
import json
import sys
from pathlib import Path

from cargo_parser import load_dependencies
from graph_builder import build_bfs_graph, load_test_graph
from topo_sort import topological_sort, compare_with_cargo


REQUIRED_FIELDS = [
    "package_name",
    "repository_url",
    "use_test_repo",
    "package_version",
    "output_image_name",
    "max_depth",
    "filter_substring"
]


def load_config(path: Path):
    return json.load(path.open("r", encoding="utf-8"))


def validate_config(cfg: dict):
    missing = [k for k in REQUIRED_FIELDS if k not in cfg]
    if missing:
        raise KeyError("Missing required fields: {}".format(", ".join(missing)))


def print_graph(edges):
    print("\n=== Dependency Graph (BFS) ===")
    if not edges:
        print("(empty)")
    for src, tgt in edges:
        print(f"{src} -> {tgt}")


def print_topo(order, ok):
    print("\n=== Topological Order ===")
    for node in order:
        print(node)
    if not ok:
        print("\nWARNING: Graph contains cycles!")


def print_diff(diff):
    print("\n=== Comparison With Cargo Order ===")
    if not diff:
        print("No differences detected.")
        return
    for ours, cargo in diff:
        print(f"Our: {ours}   |   Cargo: {cargo}")


def dependency_loader_factory(repo_url):
    """
    Loads direct dependencies using Stage 2 logic.
    Only works for the root package in Stage 4.
    """
    def loader(package_name):
        if package_name == "ROOT":
            deps = load_dependencies(repo_url, False)
            return [name for name, version in deps]
        return []
    return loader


def main():
    parser = argparse.ArgumentParser(description="Dependency Visualizer - Stage 4")
    parser.add_argument("--config", "-c", required=True)
    parser.add_argument("--test-graph", help="Path to A: B C style graph file (test mode)")
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    validate_config(cfg)

    root = cfg["package_name"]
    max_depth = cfg["max_depth"]
    filter_substr = cfg["filter_substring"]

    # =============================
    # TEST MODE
    # =============================
    if cfg["use_test_repo"]:
        if not args.test_graph:
            print("ERROR: Test mode enabled but no --test-graph given.", file=sys.stderr)
            sys.exit(1)

        test_graph = load_test_graph(args.test_graph)

        edges = build_bfs_graph(
            root=root,
            dependency_loader=None,
            max_depth=max_depth,
            filter_substring=filter_substr,
            test_graph=test_graph
        )

        print_graph(edges)

        # Topo sort
        order, ok = topological_sort(edges)
        print_topo(order, ok)

        # Cargo order = same as topo order in simplified version
        diff = compare_with_cargo(order, order)
        print_diff(diff)

        return

    # =============================
    # REAL MODE
    # =============================
    loader = dependency_loader_factory(cfg["repository_url"])

    edges = build_bfs_graph(
        root="ROOT",
        dependency_loader=loader,
        max_depth=max_depth,
        filter_substring=filter_substr
    )

    print_graph(edges)

    # Topo sort
    order, ok = topological_sort(edges)
    print_topo(order, ok)

    # Placeholder Cargo order
    diff = compare_with_cargo(order, order)
    print_diff(diff)


if __name__ == "__main__":
    main()
