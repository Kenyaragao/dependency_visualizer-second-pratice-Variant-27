#!/usr/bin/env python3
"""
Dependency Visualizer - Stage 3 (Variant 27)
"""

import argparse
import json
import sys
from pathlib import Path
from cargo_parser import load_dependencies
from graph_builder import build_bfs_graph, load_test_graph


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
        print("{} -> {}".format(src, tgt))


def dependency_loader_factory(repo_url, test_mode, test_file):
    """
    Creates a function that loads dependencies for a given package name.
    For Stage 3, we reuse Stage 2's loader for the root only.
    For other nodes, return empty (Stage 3 does not resolve sub-crates).
    """
    def loader(package_name):
        if test_mode:
            return []  # test mode handled separately
        if package_name == "ROOT":
            deps = load_dependencies(repo_url, False)
            return [name for name, version in deps]
        return []  # no real recursive Cargo resolution yet (will improve in Stage 4+)

    return loader


def main():
    parser = argparse.ArgumentParser(description="Dependency Visualizer - Stage 3")
    parser.add_argument("--config", "-c", required=True)
    parser.add_argument("--test-graph", help="Path to A: B C style graph file (test mode)")
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    validate_config(cfg)

    root = cfg["package_name"]
    max_depth = cfg["max_depth"]
    filter_substr = cfg["filter_substring"]

    # TEST MODE
    if cfg["use_test_repo"]:
        if not args.test_graph:
            print("ERROR: Test mode enabled but no --test-graph given.", file=sys.stderr)
            sys.exit(1)

        graph = load_test_graph(args.test_graph)
        edges = build_bfs_graph(
            root=root,
            dependency_loader=None,
            max_depth=max_depth,
            filter_substring=filter_substr,
            test_graph=graph
        )
        print_graph(edges)
        return

    # REAL MODE (only direct deps for now)
    loader = dependency_loader_factory(
        repo_url=cfg["repository_url"],
        test_mode=False,
        test_file=None
    )

    edges = build_bfs_graph(
        root="ROOT",
        dependency_loader=loader,
        max_depth=max_depth,
        filter_substring=filter_substr
    )

    print_graph(edges)


if __name__ == "__main__":
    main()
