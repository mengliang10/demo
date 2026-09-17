# Manim (Mathematical Animation Engine)
**Category:** [3D, High-Performance & Scientific Graphics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Animation engine for explanatory math and science videos created by Grant Sanderson (3Blue1Brown).

## Official Resources
- **Website / Documentation:** [https://www.manim.community](https://www.manim.community)

## Installation & Setup
```bash
pip install manim
```

## Starter / Hello World Example
```python
from manim import *
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```
