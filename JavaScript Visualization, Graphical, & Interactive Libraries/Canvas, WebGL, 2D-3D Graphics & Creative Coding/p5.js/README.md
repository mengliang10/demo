# p5.js
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Creative coding library inspired by Processing, making code accessible for generative art and education.

## Official Resources
- **Website / Documentation:** [https://p5js.org](https://p5js.org)

## Installation & Setup
```bash
npm install p5
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
```

## Starter / Hello World Example
```javascript
function setup() {
  createCanvas(400, 400);
}
function draw() {
  background(220);
  ellipse(mouseX, mouseY, 50, 50);
}
```
