# FusionCharts
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Enterprise-grade JavaScript charts, maps, and dashboards for complex corporate systems.

## Official Resources
- **Website / Documentation:** [https://www.fusioncharts.com](https://www.fusioncharts.com)

## Installation & Setup
```bash
npm install fusioncharts
```

### CDN Embed:
```html
<script src="https://cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
```

## Starter / Hello World Example
```javascript
FusionCharts.ready(function(){
  var chart = new FusionCharts({
    type: 'column2d',
    renderAt: 'chart-container',
    width: '500',
    height: '300',
    dataSource: { chart: { caption: "Quarterly Revenue" }, data: [{ label: "Q1", value: "195000" }] }
  }).render();
});
```
