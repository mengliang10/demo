# Glumpy
**Category:** [3D, High-Performance & Scientific Graphics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Scientific visualization library based on OpenGL and NumPy for fast shader-driven rendering.

## Official Resources
- **Website / Documentation:** [https://glumpy.github.io](https://glumpy.github.io)

## Installation & Setup
```bash
pip install glumpy
```

## Starter / Hello World Example
```python
from glumpy import app, gloo, gl
vertex = """attribute vec2 position; void main() { gl_Position = vec4(position, 0.0, 1.0); }"""
fragment = """void main() { gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); }"""
window = app.Window()
program = gloo.Program(vertex, fragment, count=4)
# Run glumpy event loop...
```
