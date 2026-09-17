# Vega
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Declarative format for creating, saving, and sharing interactive visualization designs.

## Official Resources
- **Website / Documentation:** [https://vega.github.io/vega/](https://vega.github.io/vega/)

## Installation & Setup
```bash
npm install vega
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
```

## Starter / Hello World Example
```javascript
const spec = { "$schema": "https://vega.github.io/schema/vega/v5.json", "width": 400, "height": 200 };
const view = new vega.View(vega.parse(spec), { renderer: 'canvas', container: '#view' }).run();
```
