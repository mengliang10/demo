# AntV G2
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
The grammar of graphics in JavaScript by Ant Financial / Alibaba.

## Official Resources
- **Website / Documentation:** [https://g2.antv.antgroup.com](https://g2.antv.antgroup.com)

## Installation & Setup
```bash
npm install @antv/g2
```

### CDN Embed:
```html
<script src="https://unpkg.com/@antv/g2"></script>
```

## Starter / Hello World Example
```javascript
import { Chart } from '@antv/g2';
const chart = new Chart({ container: 'container' });
chart.interval().data([{ genre: 'Sports', sold: 275 }, { genre: 'Strategy', sold: 115 }]).encode('x', 'genre').encode('y', 'sold');
chart.render();
```
