# PixiJS
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Super fast 2D WebGL rendering engine with automatic Canvas fallback and rich sprite batching.

## Official Resources
- **Website / Documentation:** [https://pixijs.com](https://pixijs.com)

## Installation & Setup
```bash
npm install pixi.js
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/pixi.js/7.3.2/pixi.min.js"></script>
```

## Starter / Hello World Example
```javascript
const app = new PIXI.Application({ width: 640, height: 360 });
document.body.appendChild(app.view);
const graphics = new PIXI.Graphics();
graphics.beginFill(0xDE3249);
graphics.drawRect(50, 50, 100, 100);
graphics.endFill();
app.stage.addChild(graphics);
```
