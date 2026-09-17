# Veusz
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
GUI and Python scientific plotting package designed for producing publication-ready EPS and PDF figures.

## Official Resources
- **Website / Documentation:** [https://veusz.github.io](https://veusz.github.io)

## Installation & Setup
```bash
pip install veusz
```

## Starter / Hello World Example
```python
import veusz.embed as veusz
embed = veusz.Embedded('window')
embed.To(embed.Root.Add('page'))
embed.To(embed.Current.Add('graph'))
# Add xy plots with scientific error bars...
```
