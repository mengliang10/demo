# Konva.js
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
2D canvas framework for desktop and mobile with high-performance layer compositing and event handling.

## Official Resources
- **Website / Documentation:** [https://konvajs.org](https://konvajs.org)

## Installation & Setup
```bash
npm install konva
```

### CDN Embed:
```html
<script src="https://unpkg.com/konva@9/konva.min.js"></script>
```

## Starter / Hello World Example
```javascript
const stage = new Konva.Stage({ container: 'container', width: 500, height: 500 });
const layer = new Konva.Layer();
const circle = new Konva.Circle({ x: stage.width() / 2, y: stage.height() / 2, radius: 70, fill: 'red' });
layer.add(circle);
stage.add(layer);
```
