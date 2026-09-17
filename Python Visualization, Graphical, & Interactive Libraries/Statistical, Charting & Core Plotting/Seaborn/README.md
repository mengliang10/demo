# Seaborn
**Category:** [Statistical, Charting & Core Plotting](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Statistical data visualization based on Matplotlib providing high-level statistical chart themes.

## Official Resources
- **Website / Documentation:** [https://seaborn.pydata.org](https://seaborn.pydata.org)

## Installation & Setup
```bash
pip install seaborn
```

## Starter / Hello World Example
```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set2")
plt.title("Seaborn Statistical Boxplot")
plt.show()
```
