# Mayavi
**Category:** [3D, High-Performance & Scientific Graphics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
3D scientific data visualization and plotting in Python powered by VTK and traits.

## Official Resources
- **Website / Documentation:** [https://docs.enthought.com/mayavi/mayavi/](https://docs.enthought.com/mayavi/mayavi/)

## Installation & Setup
```bash
pip install mayavi PyQt5
```

## Starter / Hello World Example
```python
from mayavi import mlab
import numpy as np
x, y = np.mgrid[-3:3:100j, -3:3:100j]
z = np.sin(x**2 + y**2)
mlab.surf(x, y, z)
mlab.savefig('mayavi_surface.png')
```
