# Dependency Visualizer (Variant 27) — Stage 5

This directory contains the implementation of **Stage 5**, the final stage.

Stage 5 adds:
- Export of the dependency graph to D2 format  
- Ability to generate diagrams using D2  
- Final integration of all previous stages  

---

## New Features

### ✔ D2 Export
The program now produces a `.d2` file from the dependency graph.

Example output:
A: B
A: C
B: D
C: D
C: E
├── README.md
├── .gitignore
├── config.example.json
├── test_graph.txt
└── src/
├── main.py
├── cargo_parser.py
├── graph_builder.py
├── topo_sort.py
└── d2_exporter.py

Produces:

- BFS graph  
- Topological order  
- Cargo comparison  
- D2 diagram file (`deps.d2`, for example)
