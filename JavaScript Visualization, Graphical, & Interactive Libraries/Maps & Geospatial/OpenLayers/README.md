# OpenLayers
**Category:** [Maps & Geospatial](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
High-performance, feature-packed library for displaying dynamic map data from OGC, WMS, and GeoJSON.

## Official Resources
- **Website / Documentation:** [https://openlayers.org](https://openlayers.org)

## Installation & Setup
```bash
npm install ol
```

### CDN Embed:
```html
<script src="https://cdn.jsdelivr.net/npm/ol@v9.1.0/dist/ol.js"></script>
```

## Starter / Hello World Example
```javascript
import Map from 'ol/Map.js';
import View from 'ol/View.js';
import TileLayer from 'ol/layer/Tile.js';
import OSM from 'ol/source/OSM.js';
const map = new Map({
  target: 'map',
  layers: [new TileLayer({ source: new OSM() })],
  view: new View({ center: [0, 0], zoom: 2 })
});
```
