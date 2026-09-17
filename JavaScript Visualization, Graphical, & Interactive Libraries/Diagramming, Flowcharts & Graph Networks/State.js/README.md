# State.js
**Category:** [Diagramming, Flowcharts & Graph Networks](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Hierarchical finite state machine (statechart) visualization and execution engine.

## Official Resources
- **Website / Documentation:** [https://github.com/steelbreeze/state](https://github.com/steelbreeze/state)

## Installation & Setup
```bash
npm install @steelbreeze/state
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/@steelbreeze/state"></script>
```

## Starter / Hello World Example
```javascript
import * as state from '@steelbreeze/state';
const model = new state.State('my_state_machine');
const initial = new state.PseudoState('initial', model, state.PseudoStateKind.Initial);
```
