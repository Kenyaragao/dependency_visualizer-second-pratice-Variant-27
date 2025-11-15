#!/usr/bin/env python3
"""
Dependency Visualizer - Stage 1 (Variant 27)

Simple CLI that reads JSON configuration and prints key = value pairs,
with validation and error handling.

All messages, variable names, and comments are in English as requested.
"""

import argparse
import json
import sys
from pathlib import Path

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
        raise FileNotFoundError("Configuration file not found: {}".format(path))
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON in configuration file: {}".format(e))
    return data

def validate_config(cfg: dict):
    missing = [k for k in REQUIRED_FIELDS if k not in cfg]
    if missing:
        raise KeyError("Missing required configuration fields: {}".format(", ".join(missing)))
    
    if not isinstance(cfg.get("use_test_repo"), bool):
        raise TypeError("'use_test_repo' must be a boolean")

    if not isinstance(cfg.get("max_depth"), int):
        raise TypeError("'max_depth' must be an integer")

    return True

def print_config(cfg: dict):
    for k, v in cfg.items():
        print("{} = {}".format(k, v))

def main():
    parser = argparse.ArgumentParser(description="Dependency Visualizer - Stage 1")
    parser.add_argument("--config", "-c", required=True, help="Path to JSON configuration file")
    args = parser.parse_args()

    cfg_path = Path(args.config)
    try:
        cfg = load_config(cfg_path)
    except Exception as e:
        print("ERROR: {}".format(e), file=sys.stderr)
        sys.exit(2)

    try:
        validate_config(cfg)
    except Exception as e:
        print("CONFIG ERROR: {}".format(e), file=sys.stderr)
        sys.exit(3)

    print_config(cfg)

if __name__ == "__main__":
    main()
