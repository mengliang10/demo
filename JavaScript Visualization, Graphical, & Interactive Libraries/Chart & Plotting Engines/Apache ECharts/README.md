# Apache ECharts
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Powerful charting and visualization library for enterprise applications with high rendering performance.

## Official Resources
- **Website / Documentation:** [https://echarts.apache.org](https://echarts.apache.org)

## Installation & Setup
```bash
npm install echarts
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
```

## Starter / Hello World Example
```javascript
const chart = echarts.init(document.getElementById('main'));
chart.setOption({
  xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] },
  yAxis: { type: 'value' },
  series: [{ data: [150, 230, 224, 218, 135], type: 'line' }]
});
```
