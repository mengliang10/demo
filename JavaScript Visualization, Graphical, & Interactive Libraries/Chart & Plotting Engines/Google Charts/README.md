# Google Charts
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Free visualization service with interactive charts and comprehensive cross-browser compatibility.

## Official Resources
- **Website / Documentation:** [https://developers.google.com/chart](https://developers.google.com/chart)

## Installation & Setup
```bash
npm install google-charts
```

### CDN Embed:
```html
<script src="https://www.gstatic.com/charts/loader.js"></script>
```

## Starter / Hello World Example
```javascript
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(() => {
  const data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'], ['Work', 8], ['Eat', 2], ['Sleep', 7]
  ]);
  const chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, { title: 'Daily Activities' });
});
```
