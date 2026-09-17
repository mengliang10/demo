# Leaflet.js
**Category:** [Maps & Geospatial](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
The leading open-source JavaScript library for mobile-friendly interactive mapping.

## Official Resources
- **Website / Documentation:** [https://leafletjs.com](https://leafletjs.com)

## Installation & Setup
```bash
npm install leaflet
```

### CDN Embed:
```html
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" /><script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
```

## Starter / Hello World Example
```javascript
const map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
L.marker([51.5, -0.09]).addTo(map).bindPopup('A pretty CSS popup.').openPopup();
```
