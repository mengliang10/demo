# Nomnoml
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Sassy UML diagram renderer based on pure text syntax rendered to HTML5 Canvas.

## Official Resources
- **Website / Documentation:** [https://nomnoml.com](https://nomnoml.com)

## Installation & Setup
```bash
npm install nomnoml
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/nomnoml/dist/nomnoml.min.js"></script>
```

## Starter / Hello World Example
```javascript
const canvas = document.getElementById('target-canvas');
const source = '[Pirate]->[Car] [Car]->[Fuel]';
nomnoml.draw(canvas, source);
```
