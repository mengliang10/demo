# Vega-Lite
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
High-level grammar of interactive graphics, generating concise JSON visual specifications.

## Official Resources
- **Website / Documentation:** [https://vega.github.io/vega-lite/](https://vega.github.io/vega-lite/)

## Installation & Setup
```bash
npm install vega-lite vega vega-embed
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
```

## Starter / Hello World Example
```javascript
vegaEmbed('#vis', {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"values": [{"a": "A","b": 28}, {"a": "B","b": 55}]},
  "mark": "bar",
  "encoding": {
    "x": {"field": "a", "type": "nominal"},
    "y": {"field": "b", "type": "quantitative"}
  }
});
```
