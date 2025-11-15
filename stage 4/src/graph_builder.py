"""
graph_builder.py - Stage 3 (Variant 27)

Builds a dependency graph using BFS.
Supports:
- max depth limit
- cycle detection
- substring filtering
- test mode (graph described in a simple text file)
"""

from collections import deque
from pathlib import Path


def load_test_graph(path: str):
    """
    Loads a simple A: B C style graph from a file.
    Returns a dict: {"A": ["B", "C"], ...}
    """
    graph = {}
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError("Test graph file not found.")

    for line in p.read_text().splitlines():
        if ":" not in line:
            continue
        src, deps = line.split(":", 1)
        src = src.strip()
        deps = [d.strip() for d in deps.split() if d.strip()]
        graph[src] = deps

    return graph


def build_bfs_graph(root: str, dependency_loader, max_depth: int,
                    filter_substring: str, test_graph: dict = None):
    """
    Builds a dependency graph using BFS.

    Parameters:
    - root: name of the root package
    - dependency_loader: function(name) -> list of dependency names
    - max_depth: maximum BFS depth
    - filter_substring: exclude dependencies containing this substring
    - test_graph: optional dict used in test mode

    Returns:
    - edges: list of (source, target)
    """
    visited = set()
    queue = deque([(root, 0)])
    edges = []

    while queue:
        current, depth = queue.popleft()

        if depth >= max_depth:
            continue

        if current in visited:
            continue

        visited.add(current)

        # Load dependencies (real or test mode)
        if test_graph is not None:
            deps = test_graph.get(current, [])
        else:
            deps = dependency_loader(current)

        for dep in deps:
            # Apply substring filter
            if filter_substring and filter_substring in dep:
                continue

            edges.append((current, dep))

            if dep not in visited:
                queue.append((dep, depth + 1))

    return edges
