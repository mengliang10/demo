# Sigma.js
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
WebGL-powered JavaScript library dedicated to drawing massive network graphs.

## Official Resources
- **Website / Documentation:** [https://www.sigmajs.org](https://www.sigmajs.org)

## Installation & Setup
```bash
npm install sigma graphology
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/sigma.js/2.4.0/sigma.min.js"></script>
```

## Starter / Hello World Example
```javascript
import Graph from 'graphology';
import Sigma from 'sigma';
const graph = new Graph();
graph.addNode("1", { label: "Node 1", x: 0, y: 0, size: 10, color: "blue" });
graph.addNode("2", { label: "Node 2", x: 1, y: 1, size: 10, color: "red" });
graph.addEdge("1", "2");
const renderer = new Sigma(graph, document.getElementById("container"));
```
