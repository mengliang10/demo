# Deck.gl
**Category:** [Maps & Geospatial](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
WebGL2-powered framework for large-scale visual exploratory data analysis over geographic layers.

## Official Resources
- **Website / Documentation:** [https://deck.gl](https://deck.gl)

## Installation & Setup
```bash
npm install deck.gl @deck.gl/layers
```

### CDN Embed:
```html
<script src="https://unpkg.com/deck.gl@latest/dist.min.js"></script>
```

## Starter / Hello World Example
```javascript
new deck.DeckGL({
  container: 'container',
  initialViewState: { longitude: -122.45, latitude: 37.8, zoom: 12 },
  controller: true,
  layers: [
    new deck.ScatterplotLayer({
      data: [{position: [-122.45, 37.8], size: 100}],
      getColor: [255, 0, 0],
      getRadius: d => d.size
    })
  ]
});
```
