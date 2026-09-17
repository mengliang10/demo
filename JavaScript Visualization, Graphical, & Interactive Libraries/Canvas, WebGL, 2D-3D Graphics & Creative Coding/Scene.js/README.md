# Scene.js
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
JavaScript timeline-based animation library for creating complex choreographed web scenes.

## Official Resources
- **Website / Documentation:** [https://daybrush.com/scenejs/](https://daybrush.com/scenejs/)

## Installation & Setup
```bash
npm install scenejs
```

### CDN Embed:
```html
<script src="https://daybrush.com/scenejs/release/latest/dist/scene.min.js"></script>
```

## Starter / Hello World Example
```javascript
const scene = new Scene({
  ".circle": {
    0: { transform: "scale(0)" },
    1: { transform: "scale(1)" }
  }
}, { duration: 1 }).play();
```
