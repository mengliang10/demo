# VivaGraphJS
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Graph drawing library designed for high performance with WebGL, SVG, and force-directed algorithms.

## Official Resources
- **Website / Documentation:** [https://github.com/anvaka/VivaGraphJS](https://github.com/anvaka/VivaGraphJS)

## Installation & Setup
```bash
npm install vivagraphjs
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/vivagraphjs@0.12.0/dist/vivagraph.min.js"></script>
```

## Starter / Hello World Example
```javascript
const graph = Viva.Graph.graph();
graph.addLink(1, 2);
const renderer = Viva.Graph.View.renderer(graph, { container: document.getElementById('graph1') });
renderer.run();
```
