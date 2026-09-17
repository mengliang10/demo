# VisPy
**Category:** [3D, High-Performance & Scientific Graphics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
High-performance interactive 2D/3D data visualization library leveraging modern OpenGL shaders.

## Official Resources
- **Website / Documentation:** [https://vispy.org](https://vispy.org)

## Installation & Setup
```bash
pip install vispy
```

## Starter / Hello World Example
```python
from vispy import scene
import numpy as np

canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()
scatter = scene.visuals.Markers()
scatter.set_data(np.random.normal(size=(500, 3)), edge_color=None, face_color=(1, 1, 0, .5), size=5)
view.add(scatter)
view.camera = 'turntable'
```
