# Chart.js
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Simple yet flexible JavaScript charting for designers & developers using HTML5 Canvas.

## Official Resources
- **Website / Documentation:** [https://www.chartjs.org](https://www.chartjs.org)

## Installation & Setup
```bash
npm install chart.js
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

## Starter / Hello World Example
```javascript
const ctx = document.getElementById('myChart');
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple'],
    datasets: [{ label: 'Votes', data: [12, 19, 3, 5, 2], borderWidth: 1 }]
  }
});
```
