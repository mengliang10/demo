# Vis.js (vis-network / vis-timeline)
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Dynamic, browser-based visualization libraries for interactive networks and timeline data.

## Official Resources
- **Website / Documentation:** [https://visjs.org](https://visjs.org)

## Installation & Setup
```bash
npm install vis-network vis-timeline
```

### CDN Embed:
```html
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
```

## Starter / Hello World Example
```javascript
const nodes = new vis.DataSet([{ id: 1, label: 'Node 1' }, { id: 2, label: 'Node 2' }]);
const edges = new vis.DataSet([{ from: 1, to: 2 }]);
const network = new vis.Network(container, { nodes, edges }, {});
```
