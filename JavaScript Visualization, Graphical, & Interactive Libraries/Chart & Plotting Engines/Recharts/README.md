# Recharts
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Redefined chart library built with React and D3 components for declarative composition.

## Official Resources
- **Website / Documentation:** [https://recharts.org](https://recharts.org)

## Installation & Setup
```bash
npm install recharts
```

### CDN Embed:
```html
Bundled via npm / Webpack / Vite in React
```

## Starter / Hello World Example
```javascript
import { BarChart, Bar, XAxis, YAxis, Tooltip } from 'recharts';
const App = () => (
  <BarChart width={400} height={250} data={[{name: 'A', uv: 400}, {name: 'B', uv: 700}]}>
    <XAxis dataKey="name" /><YAxis /><Tooltip /><Bar dataKey="uv" fill="#8884d8" />
  </BarChart>
);
```
