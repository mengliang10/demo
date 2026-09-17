# Observable Plot
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Concise, expressive library for exploratory data visualization on the web.

## Official Resources
- **Website / Documentation:** [https://observablehq.com/plot](https://observablehq.com/plot)

## Installation & Setup
```bash
npm install @observablehq/plot
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6"></script>
```

## Starter / Hello World Example
```javascript
const plot = Plot.rectY([1, 2, 3, 4, 5], {x: d => d, y: d => d * 2}).plot();
document.body.append(plot);
```
