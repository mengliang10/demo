# Fabric.js
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Powerful HTML5 canvas library with interactive object model, SVG parsing, and serialized states.

## Official Resources
- **Website / Documentation:** [http://fabricjs.com](http://fabricjs.com)

## Installation & Setup
```bash
npm install fabric
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"></script>
```

## Starter / Hello World Example
```javascript
const canvas = new fabric.Canvas('c');
const rect = new fabric.Rect({ top: 100, left: 100, width: 60, height: 70, fill: 'red' });
canvas.add(rect);
```
