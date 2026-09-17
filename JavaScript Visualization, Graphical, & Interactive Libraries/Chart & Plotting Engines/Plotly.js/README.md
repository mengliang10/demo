# Plotly.js
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
High-level, declarative charting library built on D3 and WebGL with over 40 chart types.

## Official Resources
- **Website / Documentation:** [https://plotly.com/javascript/](https://plotly.com/javascript/)

## Installation & Setup
```bash
npm install plotly.js-dist-min
```

### CDN Embed:
```html
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
```

## Starter / Hello World Example
```javascript
Plotly.newPlot('myDiv', [{
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  mode: 'markers+lines',
  type: 'scatter'
}], { title: 'Basic Plotly Chart' });
```
