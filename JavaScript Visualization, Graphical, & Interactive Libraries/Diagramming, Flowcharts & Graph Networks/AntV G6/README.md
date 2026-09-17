# AntV G6
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Graph visualization engine for large relational data and knowledge graphs by Ant Group.

## Official Resources
- **Website / Documentation:** [https://g6.antv.antgroup.com](https://g6.antv.antgroup.com)

## Installation & Setup
```bash
npm install @antv/g6
```

### CDN Embed:
```html
<script src="https://unpkg.com/@antv/g6"></script>
```

## Starter / Hello World Example
```javascript
import { Graph } from '@antv/g6';
const graph = new Graph({
  container: 'container',
  width: 500,
  height: 500,
  data: { nodes: [{ id: 'node1' }, { id: 'node2' }], edges: [{ source: 'node1', target: 'node2' }] }
});
graph.render();
```
