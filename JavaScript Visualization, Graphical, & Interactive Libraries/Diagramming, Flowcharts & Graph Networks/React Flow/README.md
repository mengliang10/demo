# React Flow
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Highly customizable React component for building node-based workflows and interactive graph UIs.

## Official Resources
- **Website / Documentation:** [https://reactflow.dev](https://reactflow.dev)

## Installation & Setup
```bash
npm install @xyflow/react
```

### CDN Embed:
```html
Bundled via npm in React
```

## Starter / Hello World Example
```javascript
import { ReactFlow } from '@xyflow/react';
const nodes = [{ id: '1', position: { x: 0, y: 0 }, data: { label: 'Node 1' } }];
const edges = [];
export default () => <div style={{ height: 400 }}><ReactFlow nodes={nodes} edges={edges} /></div>;
```
