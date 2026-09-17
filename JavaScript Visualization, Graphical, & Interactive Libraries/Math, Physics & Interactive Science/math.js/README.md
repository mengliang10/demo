# math.js
**Category:** [Math, Physics & Interactive Science](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Extensive math library for JavaScript and Node.js with symbolic computation, matrices, and unit parsing.

## Official Resources
- **Website / Documentation:** [https://mathjs.org](https://mathjs.org)

## Installation & Setup
```bash
npm install mathjs
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/12.4.0/math.js"></script>
```

## Starter / Hello World Example
```javascript
const ans = math.evaluate('12 / (2.3 + 0.7)');
const d = math.derivative('x^2 + x', 'x');
console.log(d.toString()); // 2 * x + 1
```
