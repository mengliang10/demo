# Plotnine (ggplot2 implementation)
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Grammar of graphics implementation for Python based closely on R's ggplot2.

## Official Resources
- **Website / Documentation:** [https://plotnine.org](https://plotnine.org)

## Installation & Setup
```bash
pip install plotnine
```

## Starter / Hello World Example
```python
from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars
p = (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm')
 + facet_wrap('~gear'))
p.save('plotnine_figure.png')
```
