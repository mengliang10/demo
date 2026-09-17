# NGL Viewer
**Category:** [Math, Physics & Interactive Science](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
WebGL-based molecular viewer for large macromolecular structures, cryo-EM densities, and trajectories.

## Official Resources
- **Website / Documentation:** [https://nglviewer.org/ngl/](https://nglviewer.org/ngl/)

## Installation & Setup
```bash
npm install ngl
```

### CDN Embed:
```html
<script src="https://unpkg.com/ngl"></script>
```

## Starter / Hello World Example
```javascript
const stage = new NGL.Stage("viewport");
stage.loadFile("rcsb://1crn").then(function (o) {
  o.addRepresentation("cartoon");
  o.autoView();
});
```
