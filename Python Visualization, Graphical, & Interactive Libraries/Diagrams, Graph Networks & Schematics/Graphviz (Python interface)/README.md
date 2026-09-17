# Graphviz (Python interface)
**Category:** [Diagrams, Graph Networks & Schematics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Python interface to the Graphviz graph layout engine with DOT language support.

## Official Resources
- **Website / Documentation:** [https://graphviz.readthedocs.io](https://graphviz.readthedocs.io)

## Installation & Setup
```bash
pip install graphviz
```

## Starter / Hello World Example
```python
import graphviz
dot = graphviz.Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.render('round_table', format='png', cleanup=True)
```
