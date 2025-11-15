# Dependency Visualizer (Variant 27) — Stage 3

This directory contains the implementation of **Stage 3** of the project.

Stage 3 introduces the **construction of a dependency graph** using **BFS**, with support for:

- Maximum depth limit  
- Substring-based dependency filtering  
- Cycle handling (via visited set)  
- Test mode using a simple text file describing the graph  
- Graph output as `source -> target` edges  

The program still reads the configuration file from Stage 1 and uses the dependency extraction from Stage 2 when running in real mode.

---

## 📌 Stage 3 Features

### ✔ BFS graph construction  
The graph is built from a root package, exploring dependencies level by level.

### ✔ Depth limit  
The BFS stops exploring deeper dependencies once the configured `max_depth` is reached.

### ✔ Filtering  
Dependencies whose names contain the substring defined in `filter_substring` are ignored.

### ✔ Cycle prevention  
A visited set is used to avoid infinite loops when the dependency graph contains cycles.

### ✔ Test graph mode  
When `"use_test_repo": true`, the program expects a file where each line describes dependencies:

