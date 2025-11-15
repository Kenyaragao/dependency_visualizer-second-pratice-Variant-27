# 2-pratice — Variant 27  
Configuration Management Practice Work  

## Project Goal

The project demonstrates practical skills in:

- Configuration management  
- Version control practices  
- Incremental software development  
- Dependency analysis  
- Graph construction  
- Visualization using D2  
- Comparison between custom and Cargo dependency resolution  

The tool loads dependencies, builds a graph, performs topological sorting, compares with Cargo, and exports a dependency diagram.

## Repository Structure

.
├── README.md # Main project documentation
├── stage1/ # Stage 1 implementation
│ ├── src/
│ ├── config.example.json
│ ├── .gitignore
│ └── README.md
├── stage2/ # Stage 2 implementation
├── stage3/ # Stage 3 implementation
├── stage4/ # Stage 4 implementation
└── stage5/ # Stage 5 (+ final D2 export)

Each stage contains:

- `src/` — Python files for that stage  
- `config.example.json` — configuration format  
- `test_graph.txt` — sample input graph  
- `README.md` — stage-specific documentation  

#  Stage Descriptions

## **Stage 1 — Base Project Setup**
- Created project structure  
- Implemented configuration loader  
- Added example config file  
- Setup `.gitignore`

## **Stage 2 — Cargo Direct Dependency Parser**
- Implemented a parser that reads dependency names from a simple graph file  
- Introduced `cargo_parser.py`  
- Printed direct dependency relationships

## **Stage 3 — BFS Graph Builder**
- Implemented dependency graph construction using **Breadth-First Search**  
- Added depth-limit support  
- Added test mode using a text file  
- Output a readable dependency list

## **Stage 4 — Topological Sorting + Cargo Comparison**
- Implemented topological sorting  
- Detected cycles  
- Compared calculated order with Cargo’s order  
- Displayed differences

## **Stage 5 — D2 Export (Final Visualization)**
- Exported the dependency graph to D2 format  
- Generated `.d2` and `.svg` output  
- Final graphical representation of the dependency graph

#  Running the Project (Test Mode)

Each stage can be executed separately.  
Example for Stage 5:

python src/main.py --config config.example.json --test-graph test_graph.txt

markdown
Копировать код

This will:

- Parse the graph  
- Build dependencies  
- Compute topological order  
- Compare with Cargo  
- Export the D2 diagram  
- Save `deps.d2` and `deps.svg`

This repository follows the required commit structure:

- **Stage 1 commit**
- **Stage 2 commit**
- **Stage 3 commit**
- **Stage 4 commit**
- **Stage 5 commit**
- Additional fixes if necessary (correct submodule removal, etc.)

Each stage commit contains only the files that belong to that stage.
