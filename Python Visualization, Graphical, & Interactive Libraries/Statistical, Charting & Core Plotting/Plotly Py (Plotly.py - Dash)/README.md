# Plotly Py (Plotly.py / Dash)
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Interactive graphing library and framework for analytical web applications in pure Python.

## Official Resources
- **Website / Documentation:** [https://plotly.com/python/](https://plotly.com/python/)

## Installation & Setup
```bash
pip install plotly dash
```

## Starter / Hello World Example
```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size='petal_length')
fig.write_html("plotly_scatter.html")
fig.show()
```
