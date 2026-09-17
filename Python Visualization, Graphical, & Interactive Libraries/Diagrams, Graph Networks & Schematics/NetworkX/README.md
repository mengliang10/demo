# NetworkX
**Category:** [Diagrams, Graph Networks & Schematics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Comprehensive Python package for the creation, manipulation, and study of complex network structures.

## Official Resources
- **Website / Documentation:** [https://networkx.org](https://networkx.org)

## Installation & Setup
```bash
pip install networkx
```

## Starter / Hello World Example
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(n=30, p=0.15, seed=42)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, node_color='#00e676', edge_color='#444', with_labels=True)
plt.savefig('networkx_graph.png')
```
