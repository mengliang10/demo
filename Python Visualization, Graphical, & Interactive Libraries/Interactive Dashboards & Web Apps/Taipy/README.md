# Taipy
**Category:** [Interactive Dashboards & Web Apps](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Enterprise-ready Python application framework for interactive GUIs and complex data pipelines.

## Official Resources
- **Website / Documentation:** [https://www.taipy.io](https://www.taipy.io)

## Installation & Setup
```bash
pip install taipy
```

## Starter / Hello World Example
```python
from taipy.gui import Gui
page = """
# Taipy Interactive Dashboard
<|{value}|slider|min=0|max=100|>
<|{value}|text|>
"""
value = 50
Gui(page=page).run(dark_mode=True)
```
