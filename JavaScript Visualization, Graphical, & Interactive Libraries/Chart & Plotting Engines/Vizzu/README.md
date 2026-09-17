# Vizzu
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Library for animated data stories and seamless morphing chart-to-chart transitions.

## Official Resources
- **Website / Documentation:** [https://vizzuhq.com](https://vizzuhq.com)

## Installation & Setup
```bash
npm install vizzu
```

### CDN Embed:
```html
<script type="module" src="https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js"></script>
```

## Starter / Hello World Example
```javascript
import Vizzu from 'https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js';
const chart = new Vizzu('myVizzu');
chart.initializing.then(chart => chart.animate({
  data: { series: [{ name: 'Foo', values: ['Alice', 'Bob'] }, { name: 'Bar', values: [15, 32] }] },
  config: { x: 'Foo', y: 'Bar', geometry: 'rectangle' }
}));
```
