# Mapclassify
**Category:** [Geospatial & Mapping](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Classification schemes for choropleth mapping and spatial data analysis (Fisher-Jenks, Quantiles).

## Official Resources
- **Website / Documentation:** [https://pysal.org/mapclassify/](https://pysal.org/mapclassify/)

## Installation & Setup
```bash
pip install mapclassify
```

## Starter / Hello World Example
```python
import mapclassify
import numpy as np
data = np.random.exponential(scale=10, size=1000)
classifier = mapclassify.NaturalBreaks(data, k=5)
print(classifier)
```
