# VTK (Python bindings)
**Category:** [3D, High-Performance & Scientific Graphics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Visualization Toolkit: world-renowned C++/Python engine for 3D graphics, volumetric processing, and CAD.

## Official Resources
- **Website / Documentation:** [https://vtk.org](https://vtk.org)

## Installation & Setup
```bash
pip install vtk
```

## Starter / Hello World Example
```python
import vtk
cylinder = vtk.vtkCylinderSource()
cylinder.SetResolution(8)
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cylinder.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
```
