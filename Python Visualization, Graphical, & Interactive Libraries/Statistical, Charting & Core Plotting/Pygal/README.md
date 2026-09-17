# Pygal
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Sexy, pythonic SVG chart generator producing lightweight, resolution-independent vector graphics.

## Official Resources
- **Website / Documentation:** [https://www.pygal.org](https://www.pygal.org)

## Installation & Setup
```bash
pip install pygal
```

## Starter / Hello World Example
```python
import pygal
bar_chart = pygal.Bar()
bar_chart.title = 'Quarterly Gross Revenue'
bar_chart.add('2023', [12, 19, 15, 25])
bar_chart.add('2024', [18, 24, 22, 31])
bar_chart.render_to_file('chart.svg')
```
