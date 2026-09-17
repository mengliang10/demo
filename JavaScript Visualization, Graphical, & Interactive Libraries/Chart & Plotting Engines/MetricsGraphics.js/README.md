# MetricsGraphics.js
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
D3-based library optimized for visualizing time-series and scatter data cleanly.

## Official Resources
- **Website / Documentation:** [https://metricsgraphicsjs.org](https://metricsgraphicsjs.org)

## Installation & Setup
```bash
npm install metricsgraphics
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/metrics-graphics/2.15.6/metricsgraphics.min.js"></script>
```

## Starter / Hello World Example
```javascript
MG.data_graphic({
  title: "Line Chart",
  data: [{date: new Date('2020-01-01'), value: 10}, {date: new Date('2020-01-02'), value: 20}],
  width: 450,
  height: 200,
  target: '#chart',
  x_accessor: 'date',
  y_accessor: 'value'
});
```
