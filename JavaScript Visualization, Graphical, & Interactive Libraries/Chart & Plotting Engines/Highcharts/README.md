# Highcharts
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Industry-standard, interactive JavaScript charting engine for web and mobile.

## Official Resources
- **Website / Documentation:** [https://www.highcharts.com](https://www.highcharts.com)

## Installation & Setup
```bash
npm install highcharts
```

### CDN Embed:
```html
<script src="https://code.highcharts.com/highcharts.js"></script>
```

## Starter / Hello World Example
```javascript
Highcharts.chart('container', {
  title: { text: 'Monthly Average Temperature' },
  xAxis: { categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May'] },
  series: [{ name: 'Tokyo', data: [7.0, 6.9, 9.5, 14.5, 18.2] }]
});
```
