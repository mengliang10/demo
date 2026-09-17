# CanvasJS
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
High-performance HTML5 canvas charting library with rich interactive features.

## Official Resources
- **Website / Documentation:** [https://canvasjs.com](https://canvasjs.com)

## Installation & Setup
```bash
npm install @canvasjs/charts
```

### CDN Embed:
```html
<script src="https://cdn.canvasjs.com/canvasjs.min.js"></script>
```

## Starter / Hello World Example
```javascript
const chart = new CanvasJS.Chart("chartContainer", {
  title: { text: "Performance Metric" },
  data: [{ type: "column", dataPoints: [{ y: 10, label: "Apple" }, { y: 15, label: "Mango" }] }]
});
chart.render();
```
