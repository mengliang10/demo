# Turf.js
**Category:** [Maps & Geospatial](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Advanced geospatial analysis engine for browsers and Node.js implementing GeoJSON algorithms.

## Official Resources
- **Website / Documentation:** [https://turfjs.org](https://turfjs.org)

## Installation & Setup
```bash
npm install @turf/turf
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/@turf/turf@6/turf.min.js"></script>
```

## Starter / Hello World Example
```javascript
const pt1 = turf.point([-75.343, 39.984]);
const pt2 = turf.point([-75.534, 39.123]);
const distance = turf.distance(pt1, pt2, { units: 'miles' });
console.log(`Distance: ${distance} miles`);
```
