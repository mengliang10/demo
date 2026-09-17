# Bokeh
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Interactive visualization library targeting modern web browsers for presentation in Jupyter and web apps.

## Official Resources
- **Website / Documentation:** [https://bokeh.org](https://bokeh.org)

## Installation & Setup
```bash
pip install bokeh
```

## Starter / Hello World Example
```python
from bokeh.plotting import figure, show
p = figure(title="Bokeh Basic Line", x_axis_label='x', y_axis_label='y')
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2, color="navy")
show(p)
```
