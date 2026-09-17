# Victory
**Category:** [Chart & Plotting Engines](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Modular React components for building interactive charts and data visualizations.

## Official Resources
- **Website / Documentation:** [https://commerce.nearform.com/open-source/victory/](https://commerce.nearform.com/open-source/victory/)

## Installation & Setup
```bash
npm install victory
```

### CDN Embed:
```html
Bundled via npm in React
```

## Starter / Hello World Example
```javascript
import { VictoryBar, VictoryChart, VictoryTheme } from 'victory';
const App = () => (
  <VictoryChart theme={VictoryTheme.material} domainPadding={20}>
    <VictoryBar data={[{x: 1, y: 2}, {x: 2, y: 3}, {x: 3, y: 5}]} />
  </VictoryChart>
);
```
