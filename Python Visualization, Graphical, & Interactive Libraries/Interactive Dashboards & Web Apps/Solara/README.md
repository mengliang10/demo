# Solara
**Category:** [Interactive Dashboards & Web Apps](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Pure Python, reactive web framework for data apps built on ipywidgets and React-like hooks.

## Official Resources
- **Website / Documentation:** [https://solara.dev](https://solara.dev)

## Installation & Setup
```bash
pip install solara
```

## Starter / Hello World Example
```python
import solara

@solara.component
def Page():
    count, set_count = solara.use_state(0)
    solara.Button(label=f"Clicks: {count}", on_click=lambda: set_count(count + 1))
```
