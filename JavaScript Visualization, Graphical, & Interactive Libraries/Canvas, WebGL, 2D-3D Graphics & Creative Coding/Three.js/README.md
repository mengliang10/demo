# Three.js
**Category:** [Canvas, WebGL, 2D-3D Graphics & Creative Coding](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
The premier 3D WebGL library for creating rich 3D computer graphics directly in the browser.

## Official Resources
- **Website / Documentation:** [https://threejs.org](https://threejs.org)

## Installation & Setup
```bash
npm install three
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```

## Starter / Hello World Example
```javascript
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
const cube = new THREE.Mesh(new THREE.BoxGeometry(), new THREE.MeshBasicMaterial({ color: 0x00ff00 }));
scene.add(cube);
camera.position.z = 5;
renderer.render(scene, camera);
```
