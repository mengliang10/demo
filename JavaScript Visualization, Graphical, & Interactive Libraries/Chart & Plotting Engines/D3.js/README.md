# D3.js
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Data-Driven Documents: low-level, powerful SVG/Canvas/HTML data-binding and visualization library.

## Official Resources
- **Website / Documentation:** [https://d3js.org](https://d3js.org)

## Installation & Setup
```bash
npm install d3
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
```

## Starter / Hello World Example
```javascript
const svg = d3.select("body").append("svg").attr("width", 400).attr("height", 200);
svg.selectAll("rect")
  .data([10, 35, 22, 55, 40])
  .join("rect")
  .attr("x", (d, i) => i * 60 + 20)
  .attr("y", d => 180 - d * 2.5)
  .attr("width", 45)
  .attr("height", d => d * 2.5)
  .attr("fill", "#00e676");
```
