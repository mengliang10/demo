# Matplotlib
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Comprehensive library for creating static, animated, and interactive visualizations in Python.

## Official Resources
- **Website / Documentation:** [https://matplotlib.org](https://matplotlib.org)

## Installation & Setup
```bash
pip install matplotlib
```

## Starter / Hello World Example
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.figure(figsize=(8, 4))
plt.plot(x, np.sin(x), label='Sine Wave', color='#00e676')
plt.title('Matplotlib Starter')
plt.legend()
plt.savefig('plot.png')
plt.show()
```
