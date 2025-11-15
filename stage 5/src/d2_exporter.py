from pathlib import Path

def export_to_d2(edges, output_path):
    lines = []
    for src, dst in edges:
        lines.append(f"{src}: {dst}")
    content = "\n".join(lines)
    p = Path(output_path)
    p.write_text(content, encoding="utf-8")
    return p
"""
d2_exporter.py - Stage 5 (Variant 27)

Exports the dependency graph to D2 format.
"""

from pathlib import Path

def export_to_d2(edges, output_path):
    """
    edges: list of (src, dst)
    output_path: path to .d2 file

    Writes D2 diagram format like:
    A: B
    B: C
    """
    lines = []
    for src, dst in edges:
        lines.append(f"{src}: {dst}")

    content = "\n".join(lines)

    p = Path(output_path)
    p.write_text(content, encoding="utf-8")

    return p
