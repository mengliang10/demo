# Babylon.js
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Complete, powerful, and accessible 3D game and WebGL/WebGPU rendering engine for the web.

## Official Resources
- **Website / Documentation:** [https://www.babylonjs.com](https://www.babylonjs.com)

## Installation & Setup
```bash
npm install @babylonjs/core
```

### CDN Embed:
```html
<script src="https://cdn.babylonjs.com/babylon.js"></script>
```

## Starter / Hello World Example
```javascript
const canvas = document.getElementById("renderCanvas");
const engine = new BABYLON.Engine(canvas, true);
const scene = new BABYLON.Scene(engine);
const camera = new BABYLON.FreeCamera("camera1", new BABYLON.Vector3(0, 5, -10), scene);
const sphere = BABYLON.MeshBuilder.CreateSphere("sphere", {diameter: 2}, scene);
engine.runRenderLoop(() => scene.render());
```
