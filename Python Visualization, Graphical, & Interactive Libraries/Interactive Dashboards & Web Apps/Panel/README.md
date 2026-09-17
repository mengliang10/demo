# Panel
**Category:** [Interactive Dashboards & Web Apps](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Powerful data exploration and dashboarding toolkit for Python connecting to any plotting ecosystem.

## Official Resources
- **Website / Documentation:** [https://panel.holoviz.org](https://panel.holoviz.org)

## Installation & Setup
```bash
pip install panel
```

## Starter / Hello World Example
```python
import panel as pn
pn.extension()
slider = pn.widgets.IntSlider(name='Select', start=0, end=100)
pane = pn.pane.Markdown(slider.param.value)
pn.Row(slider, pane).servable()
```
