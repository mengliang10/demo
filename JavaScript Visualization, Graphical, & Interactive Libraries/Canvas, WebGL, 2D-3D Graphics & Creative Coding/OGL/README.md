# OGL
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Minimal, high-performance WebGL library designed for creative coders who master GLSL shaders.

## Official Resources
- **Website / Documentation:** [https://github.com/oframe/ogl](https://github.com/oframe/ogl)

## Installation & Setup
```bash
npm install ogl
```

### CDN Embed:
```html
<script type="module">import { Renderer } from "https://unpkg.com/ogl";</script>
```

## Starter / Hello World Example
```javascript
import { Renderer, Camera, Transform, Program, Mesh, Box } from 'ogl';
const renderer = new Renderer();
document.body.appendChild(renderer.gl.canvas);
const scene = new Transform();
// Clean shader program setup...
```
