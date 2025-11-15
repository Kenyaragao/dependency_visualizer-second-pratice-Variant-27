# Dependency Visualizer (Variant 27) — Stage 2

This is Stage 2 of the project.  
In this stage, the program is able to:

- Load a JSON configuration file
- Read direct dependencies of a Rust (Cargo) package
- Parse direct dependencies either from:
  - a real Git repository (cloned locally), or
  - a test file (when use_test_repo = true)

## Files

- `src/main.py` — main CLI integrating Stage 2
- `src/cargo_parser.py` — module that extracts dependencies
- `config.example.json` — example configuration
- `test_deps.txt` — simple test dependency file

## How to test

### 1. Test mode (local file)
