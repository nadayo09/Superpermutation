# Superpermutation

An independent research project investigating greedy heuristics and hybrid search methods for constructing superpermutations.

## Overview

This project explores several algorithms for constructing superpermutations and compares their performance through experimental benchmarking.

## Algorithms

- Baseline Greedy
- Greedy + Lookahead
- Beam Search
- Random Restart
- Depth-Limited DFS

## Files

| File | Description |
|------|-------------|
| common.py | Shared utility functions |
| baseline_greedy.py | Baseline greedy algorithm |
| lookahead.py | Greedy with lookahead search |
| beam_search.py | Beam Search implementation |
| beam_search_1_20.py | Beam width parameter sweep |
| random_restart.py | Random restart heuristic |
| dfs_limited.py | Depth-limited DFS |
| dfs_limited100.py | DFS benchmark (100 runs) |
| run_all.py | Runs all benchmarks |

## Experimental Results (n = 5)

| Algorithm | Avg Length | Avg Time |
|-----------|-----------:|---------:|
| Baseline Greedy | **153** | **8.60 ms** |
| Beam Search | 161 | 136.58 ms |
| Lookahead | 184 | 630.58 ms |
| DFS | **153** | 100.26 ms |
| Random Restart | 162.18 | 9.79 ms |

## Research Paper

The complete research paper is included as **paper.pdf**.

## Author

Brian Oh
