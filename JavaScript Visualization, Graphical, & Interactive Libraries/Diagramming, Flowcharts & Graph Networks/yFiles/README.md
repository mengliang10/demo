# yFiles
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
High-end commercial diagramming library with state-of-the-art automatic graph layouts (yWorks).

## Official Resources
- **Website / Documentation:** [https://www.yworks.com/products/yfiles](https://www.yworks.com/products/yfiles)

## Installation & Setup
```bash
npm install yfiles
```

### CDN Embed:
```html
Commercial evaluation / license bundle
```

## Starter / Hello World Example
```javascript
import { GraphComponent } from 'yfiles';
const graphComponent = new GraphComponent('#graphComponent');
const graph = graphComponent.graph;
const n1 = graph.createNodeAt([0, 0]);
const n2 = graph.createNodeAt([100, 100]);
graph.createEdge(n1, n2);
```
