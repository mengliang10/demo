# 3Dmol.js
**Category:** [Math, Physics & Interactive Science](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Object-oriented, WebGL-based molecular visualization library for proteins and chemical structures.

## Official Resources
- **Website / Documentation:** [https://3dmol.csb.pitt.edu](https://3dmol.csb.pitt.edu)

## Installation & Setup
```bash
npm install 3dmol
```

### CDN Embed:
```html
<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
```

## Starter / Hello World Example
```javascript
let viewer = $3Dmol.createViewer("gldiv", {});
viewer.addModel("ATOM      1  N   ASP A   1      27.282  15.225  37.994  1.00 24.97           N", "pdb");
viewer.setStyle({}, {stick: {}});
viewer.render();
```
