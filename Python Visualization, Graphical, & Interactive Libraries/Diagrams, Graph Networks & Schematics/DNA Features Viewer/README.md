# DNA Features Viewer
**Category:** [Diagrams, Graph Networks & Schematics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Python library to visualize DNA features and genomic sequence annotations clearly.

## Official Resources
- **Website / Documentation:** [https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer](https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer)

## Installation & Setup
```bash
pip install dna_features_viewer
```

## Starter / Hello World Example
```python
from dna_features_viewer import GraphicFeature, GraphicRecord
record = GraphicRecord(sequence_length=1000, features=[
    GraphicFeature(start=20, end=500, strand=+1, color="#ffd700", label="Gene A"),
    GraphicFeature(start=400, end=700, strand=-1, color="#ffcccc", label="Gene B")
])
ax, _ = record.plot(figure_width=5)
ax.figure.savefig("dna_features.png")
```
