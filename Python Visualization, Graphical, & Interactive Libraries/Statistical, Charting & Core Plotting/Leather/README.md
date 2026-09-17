# Leather
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Python charting library designed for zero friction, fast SVG generation with no heavy dependencies.

## Official Resources
- **Website / Documentation:** [https://leather.readthedocs.io](https://leather.readthedocs.io)

## Installation & Setup
```bash
pip install leather
```

## Starter / Hello World Example
```python
import leather
chart = leather.Chart('Simple Dots')
chart.add_dots([(1, 2), (2, 4), (3, 6)])
chart.to_svg('dots.svg')
```
