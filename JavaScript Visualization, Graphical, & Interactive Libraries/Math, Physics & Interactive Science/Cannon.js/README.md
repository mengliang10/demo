# Cannon.js
**Category:** [Math, Physics & Interactive Science](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Lightweight 3D physics engine for JavaScript, frequently paired with Three.js.

## Official Resources
- **Website / Documentation:** [https://pmndrs.github.io/cannon-es/](https://pmndrs.github.io/cannon-es/)

## Installation & Setup
```bash
npm install cannon-es
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/cannon-es/dist/cannon-es.js"></script>
```

## Starter / Hello World Example
```javascript
import * as CANNON from 'cannon-es';
const world = new CANNON.World({ gravity: new CANNON.Vec3(0, -9.82, 0) });
const body = new CANNON.Body({ mass: 5, shape: new CANNON.Sphere(1) });
world.addBody(body);
```
