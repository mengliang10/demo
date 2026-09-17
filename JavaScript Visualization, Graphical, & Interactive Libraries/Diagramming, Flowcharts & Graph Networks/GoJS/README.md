# GoJS
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Feature-rich library for interactive diagrams, flowcharts, org charts, and BPMN systems.

## Official Resources
- **Website / Documentation:** [https://gojs.net](https://gojs.net)

## Installation & Setup
```bash
npm install gojs
```

### CDN Embed:
```html
<script src="https://unpkg.com/gojs/release/go.js"></script>
```

## Starter / Hello World Example
```javascript
const myDiagram = new go.Diagram("myDiagramDiv");
myDiagram.model = new go.GraphLinksModel(
  [{ key: "Alpha" }, { key: "Beta" }],
  [{ from: "Alpha", to: "Beta" }]
);
```
