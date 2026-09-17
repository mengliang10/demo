# mxGraph
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Battle-tested diagramming library powering enterprise tools like draw.io / diagrams.net.

## Official Resources
- **Website / Documentation:** [https://github.com/jgraph/mxgraph](https://github.com/jgraph/mxgraph)

## Installation & Setup
```bash
npm install mxgraph
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/mxgraph@4.2.2/javascript/mxClient.js"></script>
```

## Starter / Hello World Example
```javascript
const container = document.getElementById('graphContainer');
const graph = new mxGraph(container);
const parent = graph.getDefaultParent();
graph.getModel().beginUpdate();
try {
  const v1 = graph.insertVertex(parent, null, 'Hello,', 20, 20, 80, 30);
  const v2 = graph.insertVertex(parent, null, 'World!', 200, 150, 80, 30);
  graph.insertEdge(parent, null, '', v1, v2);
} finally { graph.getModel().endUpdate(); }
```
