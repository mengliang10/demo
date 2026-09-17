# Altair
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Declarative statistical visualization library for Python, based on Vega and Vega-Lite grammar.

## Official Resources
- **Website / Documentation:** [https://altair-viz.github.io](https://altair-viz.github.io)

## Installation & Setup
```bash
pip install altair vega_datasets
```

## Starter / Hello World Example
```python
import altair as alt
from vega_datasets import data
cars = data.cars()
chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).interactive()
chart.save('altair_chart.html')
```
