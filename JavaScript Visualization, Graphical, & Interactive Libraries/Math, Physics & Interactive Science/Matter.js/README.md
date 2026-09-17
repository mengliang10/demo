# Matter.js
**Category:** [Math, Physics & Interactive Science](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
2D rigid body physics engine for the web featuring collision detection, restitution, and constraints.

## Official Resources
- **Website / Documentation:** [https://brm.io/matter-js/](https://brm.io/matter-js/)

## Installation & Setup
```bash
npm install matter-js
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>
```

## Starter / Hello World Example
```javascript
const { Engine, Render, Runner, Bodies, Composite } = Matter;
const engine = Engine.create();
const render = Render.create({ element: document.body, engine: engine });
const box = Bodies.rectangle(400, 200, 80, 80);
const ground = Bodies.rectangle(400, 610, 810, 60, { isStatic: true });
Composite.add(engine.world, [box, ground]);
Render.run(render);
Runner.run(Runner.create(), engine);
```
