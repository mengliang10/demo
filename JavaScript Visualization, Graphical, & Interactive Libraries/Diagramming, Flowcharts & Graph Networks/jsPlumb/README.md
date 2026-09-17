# jsPlumb
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Visual connectivity library for wiring DOM elements together with lines, anchors, and arrows.

## Official Resources
- **Website / Documentation:** [https://jsplumbtoolkit.com](https://jsplumbtoolkit.com)

## Installation & Setup
```bash
npm install @jsplumb/core
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jsPlumb/2.15.6/js/jsplumb.min.js"></script>
```

## Starter / Hello World Example
```javascript
jsPlumb.ready(function() {
  jsPlumb.connect({
    source: "item1",
    target: "item2",
    endpoint: "Dot"
  });
});
```
