# zrender
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Lightweight 2D canvas rendering engine that powers Apache ECharts with rich graphic primitives.

## Official Resources
- **Website / Documentation:** [https://ecomfe.github.io/zrender-doc/public/](https://ecomfe.github.io/zrender-doc/public/)

## Installation & Setup
```bash
npm install zrender
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/zrender@5.5.0/dist/zrender.min.js"></script>
```

## Starter / Hello World Example
```javascript
const zr = zrender.init(document.getElementById('main'));
const circle = new zrender.Circle({
  shape: { cx: 150, cy: 50, r: 40 },
  style: { fill: 'none', stroke: '#F00' }
});
zr.add(circle);
```
