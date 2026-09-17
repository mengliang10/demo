# Tangram
**Category:** [Maps & Geospatial](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Flexible 2D/3D map engine designed for real-time rendering of OpenStreetMap vector data with OpenGL.

## Official Resources
- **Website / Documentation:** [https://github.com/tangrams/tangram](https://github.com/tangrams/tangram)

## Installation & Setup
```bash
npm install tangram
```

### CDN Embed:
```html
<script src="https://unpkg.com/tangram/dist/tangram.min.js"></script>
```

## Starter / Hello World Example
```javascript
const map = L.map('map');
const layer = Tangram.leafletLayer({ scene: 'scene.yaml' });
layer.addTo(map);
```
