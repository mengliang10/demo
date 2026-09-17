# NVD3
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Reusable charts and chart components built on top of D3.js.

## Official Resources
- **Website / Documentation:** [https://nvd3.org](https://nvd3.org)

## Installation & Setup
```bash
npm install nvd3
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.6/nv.d3.min.js"></script>
```

## Starter / Hello World Example
```javascript
nv.addGraph(function() {
  const chart = nv.models.lineChart().useInteractiveGuideline(true);
  d3.select('#chart svg').datum(myData).call(chart);
  return chart;
});
```
