"""
cargo_parser.py - Stage 2 (Variant 27)

Extracts direct dependencies from Cargo.toml or from a test file.
"""

import re
import subprocess
import tempfile
import shutil
from pathlib import Path


def clone_repository(repo_url: str) -> Path:
    """Clone a git repo into a temp directory."""
    temp_dir = Path(tempfile.mkdtemp(prefix="cargo_repo_"))
    try:
        subprocess.run(
            ["git", "clone", "--depth=1", repo_url, str(temp_dir)],
            check=True,
            capture_output=True
        )
    except subprocess.CalledProcessError as e:
        shutil.rmtree(temp_dir)
        raise RuntimeError("Failed to clone repository: {}".format(e.stderr.decode()))
    return temp_dir


def find_cargo_files(root: Path) -> Path:
    """Return Cargo.toml if found."""
    toml = root / "Cargo.toml"
    if toml.exists():
        return toml
    raise FileNotFoundError("Cargo.toml not found in repository.")


def parse_cargo_toml(path: Path):
    """Extract dependencies from [dependencies] section in Cargo.toml."""
    content = path.read_text(encoding="utf-8")

    match = re.search(r"\[dependencies\]([\s\S]*?)(\n\[|$)", content)
    if not match:
        return []

    block = match.group(1)
    dependencies = []

    pattern = r"^\s*([A-Za-z0-9_\-]+)\s*=\s*(.+)$"

    for line in block.splitlines():
        m = re.match(pattern, line.strip())
        if m:
            name = m.group(1)
            version = m.group(2)
            dependencies.append((name, version))

    return dependencies


def load_dependencies(repository_url: str, use_test_repo: bool, test_file: str = None):
    """Load direct dependencies from a test file or a real repository."""
    if use_test_repo:
        if test_file is None:
            raise ValueError("Test mode enabled but no test file provided.")
        p = Path(test_file)
        if not p.exists():
            raise FileNotFoundError("Test file not found.")
        deps = []
        for line in p.read_text().splitlines():
            if "=" in line:
                name, ver = line.split("=", 1)
                deps.append((name.strip(), ver.strip()))
        return deps

    # Real repository
    repo_dir = clone_repository(repository_url)
    cargo_toml = find_cargo_files(repo_dir)
    deps = parse_cargo_toml(cargo_toml)

    shutil.rmtree(repo_dir, ignore_errors=True)
    return deps
