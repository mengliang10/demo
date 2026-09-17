# Datashader
**Category:** [3D, High-Performance & Scientific Graphics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Graphics pipeline system for synthesizing meaningful representations from billions of raw data points.

## Official Resources
- **Website / Documentation:** [https://datashader.org](https://datashader.org)

## Installation & Setup
```bash
pip install datashader
```

## Starter / Hello World Example
```python
import datashader as ds
import pandas as pd
import numpy as np

df = pd.DataFrame({'x': np.random.normal(size=1000000), 'y': np.random.normal(size=1000000)})
cvs = ds.Canvas(plot_width=400, plot_height=400)
agg = cvs.points(df, 'x', 'y')
img = ds.transfer_functions.shade(agg)
img.to_pil().save('datashader_output.png')
```
