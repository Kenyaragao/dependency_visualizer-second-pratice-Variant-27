"""
topo_sort.py - Stage 4 (Variant 27)

Implements:
- Topological sorting of the dependency graph
- Comparison between our order and the real Cargo order
"""

from collections import defaultdict, deque

def topological_sort(edges):
    """
    edges: list of (src, dst)
    returns: list of nodes in topologically sorted order
    """

    graph = defaultdict(list)
    indegree = defaultdict(int)

    nodes = set()

    for src, dst in edges:
        graph[src].append(dst)
        indegree[dst] += 1
        nodes.add(src)
        nodes.add(dst)

    # Queue of all nodes with no incoming edges
    queue = deque([n for n in nodes if indegree[n] == 0])

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neigh in graph[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)

    if len(order) != len(nodes):
        # Graph contains cycles or unresolved edges
        return order, False

    return order, True


def compare_with_cargo(our_order, cargo_order):
    """
    Compare two lists and return elements that differ.
    Returns a dict with results.
    """

    differences = []

    for i, node in enumerate(our_order):
        if i >= len(cargo_order):
            differences.append((node, None))
            continue
        if node != cargo_order[i]:
            differences.append((node, cargo_order[i]))

    return differences
