# Nivo
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Rich set of data visualization components built on top of React and D3 with SVG, Canvas, and SSR.

## Official Resources
- **Website / Documentation:** [https://nivo.rocks](https://nivo.rocks)

## Installation & Setup
```bash
npm install @nivo/core @nivo/bar
```

### CDN Embed:
```html
Bundled via npm in React
```

## Starter / Hello World Example
```javascript
import { ResponsiveBar } from '@nivo/bar';
const MyBar = ({ data }) => (
  <ResponsiveBar data={data} keys={['hot dog', 'burger']} indexBy="country" margin={{ top: 50, right: 130, bottom: 50, left: 60 }} />
);
```
