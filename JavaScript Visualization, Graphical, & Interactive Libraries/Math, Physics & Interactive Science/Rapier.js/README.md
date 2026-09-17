# Rapier.js
**Category:** [Math, Physics & Interactive Science](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Fast, cross-platform 2D and 3D physics engine written in Rust and compiled to WebAssembly.

## Official Resources
- **Website / Documentation:** [https://rapier.rs](https://rapier.rs)

## Installation & Setup
```bash
npm install @dimforge/rapier2d @dimforge/rapier3d
```

### CDN Embed:
```html
WebAssembly package via npm
```

## Starter / Hello World Example
```javascript
import('@dimforge/rapier2d').then(RAPIER => {
  let gravity = { x: 0.0, y: -9.81 };
  let world = new RAPIER.World(gravity);
});
```
