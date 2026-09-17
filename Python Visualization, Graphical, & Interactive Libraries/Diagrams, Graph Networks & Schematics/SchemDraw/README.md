# SchemDraw
**Category:** [Diagrams, Graph Networks & Schematics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Python package for producing publication-quality electrical circuit diagrams and schematics.

## Official Resources
- **Website / Documentation:** [https://schemdraw.readthedocs.io](https://schemdraw.readthedocs.io)

## Installation & Setup
```bash
pip install schemdraw
```

## Starter / Hello World Example
```python
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(file='schematic.png') as d:
    d += elm.Battery().up().label('10V')
    d += elm.Resistor().right().label('100kΩ')
    d += elm.Capacitor().down().label('0.1µF')
    d += elm.Line().left()
```
