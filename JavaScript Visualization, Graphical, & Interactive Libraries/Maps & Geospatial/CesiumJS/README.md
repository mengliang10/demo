# CesiumJS
**Category:** [Maps & Geospatial](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Open-source JavaScript platform for creating 3D globes and 2D maps with dynamic WGS84 terrain.

## Official Resources
- **Website / Documentation:** [https://cesium.com/platform/cesiumjs/](https://cesium.com/platform/cesiumjs/)

## Installation & Setup
```bash
npm install cesium
```

### CDN Embed:
```html
<script src="https://cesium.com/downloads/cesiumjs/releases/1.115/Build/Cesium/Cesium.js"></script>
```

## Starter / Hello World Example
```javascript
const viewer = new Cesium.Viewer('cesiumContainer', {
  terrainProvider: Cesium.createWorldTerrain()
});
```
