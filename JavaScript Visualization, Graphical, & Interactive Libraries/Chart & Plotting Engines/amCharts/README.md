# amCharts
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Fast, flexible data visualization library with advanced animations and Canvas engine (amCharts 5).

## Official Resources
- **Website / Documentation:** [https://www.amcharts.com](https://www.amcharts.com)

## Installation & Setup
```bash
npm install @amcharts/amcharts5
```

### CDN Embed:
```html
<script src="https://cdn.amcharts.com/lib/5/index.js"></script>
```

## Starter / Hello World Example
```javascript
const root = am5.Root.new("chartdiv");
const chart = root.container.children.push(am5xy.XYChart.new(root, {}));
// configure axes and series...
```
