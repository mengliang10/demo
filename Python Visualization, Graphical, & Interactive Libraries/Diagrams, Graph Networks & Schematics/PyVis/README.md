# PyVis
**Category:** [Diagrams, Graph Networks & Schematics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Python library for quick, interactive network graph visualizations using Vis.js under the hood.

## Official Resources
- **Website / Documentation:** [https://pyvis.readthedocs.io](https://pyvis.readthedocs.io)

## Installation & Setup
```bash
pip install pyvis
```

## Starter / Hello World Example
```python
from pyvis.network import Network
net = Network(notebook=False)
net.add_node(1, label="Node 1")
net.add_node(2, label="Node 2")
net.add_edge(1, 2)
net.save_graph("pyvis_network.html")
```
