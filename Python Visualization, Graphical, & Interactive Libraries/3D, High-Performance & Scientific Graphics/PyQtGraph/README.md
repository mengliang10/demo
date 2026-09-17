# PyQtGraph
**Category:** [3D, High-Performance & Scientific Graphics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Fast data visualization and GUI library tailored for high-speed scientific and engineering instrumentation.

## Official Resources
- **Website / Documentation:** [https://www.pyqtgraph.org](https://www.pyqtgraph.org)

## Installation & Setup
```bash
pip install pyqtgraph PyQt6
```

## Starter / Hello World Example
```python
import pyqtgraph as pg
import numpy as np

app = pg.mkQApp("Plotting App")
win = pg.plot()
win.setWindowTitle('High-Speed Oscilloscope')
data = np.random.normal(size=10000)
win.plot(data, pen='g')
pg.exec()
```
