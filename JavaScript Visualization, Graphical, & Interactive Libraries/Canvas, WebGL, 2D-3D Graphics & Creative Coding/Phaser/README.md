# Phaser
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Fast, fun, and free 2D game framework for desktop and mobile HTML5 web applications.

## Official Resources
- **Website / Documentation:** [https://phaser.io](https://phaser.io)

## Installation & Setup
```bash
npm install phaser
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/phaser@3.80.1/dist/phaser.min.js"></script>
```

## Starter / Hello World Example
```javascript
const config = { type: Phaser.AUTO, width: 800, height: 600, scene: { preload, create } };
const game = new Phaser.Game(config);
function preload() {}
function create() { this.add.text(100, 100, 'Hello Phaser!', { fill: '#0f0' }); }
```
