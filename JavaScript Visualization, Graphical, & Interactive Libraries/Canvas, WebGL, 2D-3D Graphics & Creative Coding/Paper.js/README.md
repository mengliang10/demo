# Paper.js
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Vector graphics scripting framework running on top of the HTML5 Canvas with clean Bézier math.

## Official Resources
- **Website / Documentation:** [http://paperjs.org](http://paperjs.org)

## Installation & Setup
```bash
npm install paper
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/paper.js/0.12.17/paper-full.min.js"></script>
```

## Starter / Hello World Example
```javascript
paper.setup(document.getElementById('myCanvas'));
const path = new paper.Path();
path.strokeColor = 'black';
path.moveTo(new paper.Point(20, 20));
path.lineTo(new paper.Point(100, 100));
paper.view.draw();
```
