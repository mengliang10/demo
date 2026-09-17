# Pydeck (Deck.gl wrapper)
**Category:** [Geospatial & Mapping](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
High-scale spatial data visualization in Python powered by Deck.gl and WebGL2.

## Official Resources
- **Website / Documentation:** [https://deckgl.readthedocs.io](https://deckgl.readthedocs.io)

## Installation & Setup
```bash
pip install pydeck
```

## Starter / Hello World Example
```python
import pydeck as pdk
layer = pdk.Layer(
    "HexagonLayer",
    data="https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv",
    get_position="[lng, lat]",
    radius=1000,
    elevation_scale=50,
    extruded=True
)
view_state = pdk.ViewState(latitude=37.77, longitude=-122.4, zoom=11, pitch=50)
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.to_html("pydeck_hex.html")
```
