# Curtains.js
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Lightweight WebGL library that converts HTML DOM elements into interactive 3D textured planes.

## Official Resources
- **Website / Documentation:** [https://www.curtainsjs.com](https://www.curtainsjs.com)

## Installation & Setup
```bash
npm install curtainsjs
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/curtainsjs/8.1.5/curtains.min.js"></script>
```

## Starter / Hello World Example
```javascript
const curtains = new Curtains({ container: "canvas" });
const planeElement = document.getElementsByClassName("plane")[0];
const plane = new Plane(curtains, planeElement);
```
