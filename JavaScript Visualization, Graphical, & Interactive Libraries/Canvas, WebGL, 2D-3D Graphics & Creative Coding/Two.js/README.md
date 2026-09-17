# Two.js
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Two-dimensional drawing API agnostic to SVG, Canvas, or WebGL renderers.

## Official Resources
- **Website / Documentation:** [https://two.js.org](https://two.js.org)

## Installation & Setup
```bash
npm install two.js
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/two.js/0.8.10/two.min.js"></script>
```

## Starter / Hello World Example
```javascript
const two = new Two({ width: 285, height: 200 }).appendTo(document.body);
const circle = two.makeCircle(72, 100, 50);
circle.fill = '#FF8000';
two.update();
```
