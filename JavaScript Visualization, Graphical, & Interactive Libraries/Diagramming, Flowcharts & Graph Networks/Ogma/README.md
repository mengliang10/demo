# Ogma
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Commercial high-performance JavaScript library for large-scale graph visualization and cyber analytics.

## Official Resources
- **Website / Documentation:** [https://linkurio.us/ogma/](https://linkurio.us/ogma/)

## Installation & Setup
```bash
npm install @linkurious/ogma
```

### CDN Embed:
```html
Enterprise vendor distribution (Linkurious)
```

## Starter / Hello World Example
```javascript
const ogma = new Ogma({ container: 'graph-container' });
ogma.setGraph({ nodes: [{id: 1, text: 'A'}, {id: 2, text: 'B'}], edges: [{source: 1, target: 2}] });
```
