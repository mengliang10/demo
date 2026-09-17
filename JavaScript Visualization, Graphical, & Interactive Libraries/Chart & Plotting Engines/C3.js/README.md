# C3.js
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
D3-based reusable chart library providing simple API wrappers for common charts.

## Official Resources
- **Website / Documentation:** [https://c3js.org](https://c3js.org)

## Installation & Setup
```bash
npm install c3
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/c3/0.7.20/c3.min.js"></script>
```

## Starter / Hello World Example
```javascript
var chart = c3.generate({
  bindto: '#chart',
  data: {
    columns: [
      ['data1', 30, 200, 100, 400, 150, 250],
      ['data2', 50, 20, 10, 40, 15, 25]
    ]
  }
});
```
