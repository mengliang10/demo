# GR Framework
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Universal visualization framework with ultra-fast rendering engines supporting real-time data feeds.

## Official Resources
- **Website / Documentation:** [https://gr-framework.org](https://gr-framework.org)

## Installation & Setup
```bash
pip install gr
```

## Starter / Hello World Example
```python
from gr.pygr import plot
import numpy as np
x = np.linspace(-2, 2, 40)
plot(x, x**3 - x)
```
