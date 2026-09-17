# HVPlot
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
High-level plotting API for pandas, dask, xarray, and polars built on top of HoloViews.

## Official Resources
- **Website / Documentation:** [https://hvplot.holoviz.org](https://hvplot.holoviz.org)

## Installation & Setup
```bash
pip install hvplot
```

## Starter / Hello World Example
```python
import pandas as pd
import hvplot.pandas
df = pd.DataFrame({'x': range(10), 'y': [i**2 for i in range(10)]})
plot = df.hvplot.line(x='x', y='y', title='hvPlot Line')
# Interactively renders in browser or notebook
```
