# HoloViews
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
High-level visualization library designed to make data analysis immediate, composable, and reproducible.

## Official Resources
- **Website / Documentation:** [https://holoviews.org](https://holoviews.org)

## Installation & Setup
```bash
pip install holoviews
```

## Starter / Hello World Example
```python
import numpy as np
import holoviews as hv
hv.extension('bokeh')
xs = np.linspace(0, np.pi*4, 100)
curve = hv.Curve((xs, np.sin(xs)), 'Time', 'Amplitude')
hv.save(curve, 'holoviews_curve.html')
```
