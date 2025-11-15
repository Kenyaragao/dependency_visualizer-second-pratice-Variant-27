# Dependency Visualizer (Variant 27) — Stage 4

This directory contains the implementation of **Stage 4**.

Stage 4 adds:
- Topological sorting of the dependency graph  
- Comparison with the real Cargo loading order  
- Display of differences  

## New Features

###  Topological Sort
A classical algorithm that ensures every dependency appears before the package that depends on it.

###  Comparison With Cargo
The program produces:
- Our calculated topological order
- Cargo's load order (simplified in this stage)
- A difference report

###  Test Mode
Works with the same `test_graph.txt` as Stage 3.

---

##  Project Structure (Stage 4)

dependency_visualizer_stage4/
├── README.md
├── .gitignore
├── config.example.json
├── test_graph.txt
└── src/
├── main.py
├── cargo_parser.py
├── graph_builder.py
└── topo_sort.py