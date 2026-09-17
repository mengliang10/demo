# bqplot
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Interactive 2D plotting system for Jupyter Notebooks using ipywidgets and D3.js.

## Official Resources
- **Website / Documentation:** [https://github.com/bqplot/bqplot](https://github.com/bqplot/bqplot)

## Installation & Setup
```bash
pip install bqplot
```

## Starter / Hello World Example
```python
from bqplot import LinearScale, Lines, Figure, Axis
x_sc = LinearScale()
y_sc = LinearScale()
lines = Lines(x=[0, 1, 2, 3], y=[2, 4, 1, 5], scales={'x': x_sc, 'y': y_sc})
ax_x = Axis(scale=x_sc, label='Index')
ax_y = Axis(scale=y_sc, orientation='vertical', label='Value')
fig = Figure(marks=[lines], axes=[ax_x, ax_y], title='bqplot in Jupyter')
```
