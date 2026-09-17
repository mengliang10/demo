# Cartopy
**Category:** [Geospatial & Mapping](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Python package designed for geospatial data processing and cartographic map projections.

## Official Resources
- **Website / Documentation:** [https://scitools.org.uk/cartopy/docs/latest/](https://scitools.org.uk/cartopy/docs/latest/)

## Installation & Setup
```bash
pip install cartopy
```

## Starter / Hello World Example
```python
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()
plt.savefig('cartopy_globe.png')
```
