# Taucharts
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Flexible charting library based on D3 with grammar of graphics principles and facets.

## Official Resources
- **Website / Documentation:** [https://taucharts.com](https://taucharts.com)

## Installation & Setup
```bash
npm install taucharts
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/taucharts@2/dist/taucharts.min.js"></script>
```

## Starter / Hello World Example
```javascript
const chart = new Taucharts.Chart({
  data: [{x: 1, y: 2}, {x: 2, y: 4}],
  type: 'scatterplot',
  x: 'x',
  y: 'y'
});
chart.renderTo('#chart');
```
