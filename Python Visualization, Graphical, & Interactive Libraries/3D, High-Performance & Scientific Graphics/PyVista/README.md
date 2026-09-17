# PyVista
**Category:** [3D, High-Performance & Scientific Graphics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
3D plotting and spatial mesh analysis through a streamlined, Pythonic interface to VTK.

## Official Resources
- **Website / Documentation:** [https://www.pyvista.org](https://www.pyvista.org)

## Installation & Setup
```bash
pip install pyvista
```

## Starter / Hello World Example
```python
import pyvista as pv
mesh = pv.Sphere()
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh, color='turquoise', show_edges=True)
plotter.screenshot('pyvista_sphere.png')
```
