# Cytoscape.js
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Graph theory / network library for analysis and visualization in bioinformatics and relational data.

## Official Resources
- **Website / Documentation:** [https://js.cytoscape.org](https://js.cytoscape.org)

## Installation & Setup
```bash
npm install cytoscape
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.28.1/cytoscape.min.js"></script>
```

## Starter / Hello World Example
```javascript
const cy = cytoscape({
  container: document.getElementById('cy'),
  elements: [
    { data: { id: 'a' } }, { data: { id: 'b' } },
    { data: { id: 'ab', source: 'a', target: 'b' } }
  ],
  style: [{ selector: 'node', style: { 'background-color': '#666', 'label': 'data(id)' } }],
  layout: { name: 'grid' }
});
```
