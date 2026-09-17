# Mapbox GL JS
**Category:** [Maps & Geospatial](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
WebGL-based vector tile mapping library for fast, high-resolution interactive geographic displays.

## Official Resources
- **Website / Documentation:** [https://docs.mapbox.com/mapbox-gl-js/](https://docs.mapbox.com/mapbox-gl-js/)

## Installation & Setup
```bash
npm install mapbox-gl
```

### CDN Embed:
```html
<script src="https://api.mapbox.com/mapbox-gl-js/v3.2.0/mapbox-gl.js"></script>
```

## Starter / Hello World Example
```javascript
mapboxgl.accessToken = 'YOUR_MAPBOX_ACCESS_TOKEN';
const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v12',
  center: [-74.5, 40],
  zoom: 9
});
```
