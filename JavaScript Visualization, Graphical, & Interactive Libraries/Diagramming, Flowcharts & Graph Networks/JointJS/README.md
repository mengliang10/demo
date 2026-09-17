# JointJS
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Modern diagramming library for interactive visual tools, statecharts, and workflow builders.

## Official Resources
- **Website / Documentation:** [https://www.jointjs.com](https://www.jointjs.com)

## Installation & Setup
```bash
npm install @joint/core
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jointjs/3.7.7/joint.min.js"></script>
```

## Starter / Hello World Example
```javascript
const graph = new joint.dia.Graph();
const paper = new joint.dia.Paper({ el: document.getElementById('paper'), model: graph, width: 600, height: 400 });
const rect = new joint.shapes.standard.Rectangle();
rect.position(100, 30);
rect.resize(100, 40);
rect.attr({ body: { fill: 'blue' }, label: { text: 'Hello', fill: 'white' } });
rect.addTo(graph);
```
