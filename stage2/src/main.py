#!/usr/bin/env python3
"""
Dependency Visualizer - Stage 2 (Variant 27)
"""

import argparse
import json
import sys
from pathlib import Path
from cargo_parser import load_dependencies

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
    if not path.exists():
        raise FileNotFoundError("Configuration file not found.")
    return json.load(path.open("r", encoding="utf-8"))

def validate_config(cfg: dict):
    missing = [k for k in REQUIRED_FIELDS if k not in cfg]
    if missing:
        raise KeyError("Missing required fields: {}".format(", ".join(missing)))

def print_dependencies(dep_list):
    print("\n=== Direct Dependencies ===")
    for name, version in dep_list:
        print("{} = {}".format(name, version))

def main():
    parser = argparse.ArgumentParser(description="Dependency Visualizer - Stage 2")
    parser.add_argument("--config", "-c", required=True)
    parser.add_argument("--test-file")
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    validate_config(cfg)

    deps = load_dependencies(
        repository_url=cfg["repository_url"],
        use_test_repo=cfg["use_test_repo"],
        test_file=args.test_file
    )

    print_dependencies(deps)

if __name__ == "__main__":
    main()
