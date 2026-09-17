# GeoPandas
**Category:** [Geospatial & Mapping](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Extends pandas data types to allow spatial operations on geometric types using Shapely.

## Official Resources
- **Website / Documentation:** [https://geopandas.org](https://geopandas.org)

## Installation & Setup
```bash
pip install geopandas
```

## Starter / Hello World Example
```python
import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot(column='pop_est', legend=True, cmap='viridis')
plt.savefig('world_population.png')
```
