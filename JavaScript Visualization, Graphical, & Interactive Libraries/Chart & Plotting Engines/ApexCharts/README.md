# ApexCharts
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Modern SVG charting library for reactive applications with elegant dark mode and animations.

## Official Resources
- **Website / Documentation:** [https://apexcharts.com](https://apexcharts.com)

## Installation & Setup
```bash
npm install apexcharts
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
```

## Starter / Hello World Example
```javascript
const options = {
  chart: { type: 'area', height: 350 },
  series: [{ name: 'Series 1', data: [30, 40, 45, 50, 49, 60, 70] }],
  xaxis: { categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997] }
};
const chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
```
