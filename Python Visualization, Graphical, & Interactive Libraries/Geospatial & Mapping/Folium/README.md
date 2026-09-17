# Folium
**Category:** [Geospatial & Mapping](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Python library for visualizing geospatial data on interactive Leaflet maps with marker clusters.

## Official Resources
- **Website / Documentation:** [https://python-visualization.github.io/folium/](https://python-visualization.github.io/folium/)

## Installation & Setup
```bash
pip install folium
```

## Starter / Hello World Example
```python
import folium
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
folium.Marker([45.5236, -122.6750], popup="Portland").addTo(m)
m.save("folium_map.html")
```
