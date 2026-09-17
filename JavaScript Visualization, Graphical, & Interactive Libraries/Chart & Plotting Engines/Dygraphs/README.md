# Dygraphs
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Fast, flexible open-source JavaScript chart library optimized for huge, dense time-series datasets.

## Official Resources
- **Website / Documentation:** [https://dygraphs.com](https://dygraphs.com)

## Installation & Setup
```bash
npm install dygraphs
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/dygraph/2.2.1/dygraph.min.js"></script>
```

## Starter / Hello World Example
```javascript
new Dygraph(document.getElementById("div_g"),
  "Date,Temperature\n2008-05-07,75\n2008-05-08,70\n2008-05-09,80\n", {});
```
