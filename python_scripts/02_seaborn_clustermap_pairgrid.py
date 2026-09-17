"""
02_seaborn_clustermap_pairgrid.py
================================
Demonstration of Seaborn statistical clustering and hierarchical dendrograms
for hotel channel attribution and conversion dynamics.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('dark_background')
np.random.seed(101)

# Generate synthetic multi-channel attribution correlation matrix
channels = ['Google Ads', 'Meta Ads', 'Direct Web', 'Booking.com', 'Expedia', 'Corporate GDS', 'Email CRM', 'Influencer']
n_channels = len(channels)
data = np.random.rand(n_channels, n_channels)
# Make symmetric positive-definite covariance
corr = (data + data.T) / 2
np.fill_diagonal(corr, 1.0)
df_corr = pd.DataFrame(corr, index=channels, columns=channels)

# Custom color palette (emerald to gold to cyan)
cmap = sns.diverging_palette(145, 45, s=85, l=45, n=12, as_cmap=True)

# Build hierarchical clustermap
g = sns.clustermap(
    df_corr,
    annot=True,
    fmt=".2f",
    cmap=cmap,
    figsize=(11, 10),
    cbar_kws={'label': 'Pearson Cross-Channel Attribution Affinity'},
    linewidths=1.2,
    linecolor='#070c09'
)

g.figure.patch.set_facecolor('#070c09')
g.ax_heatmap.set_facecolor('#0d1410')
g.ax_heatmap.tick_params(colors='#e8ece9', labelsize=10)
g.ax_col_dendrogram.set_facecolor('#070c09')
g.ax_row_dendrogram.set_facecolor('#070c09')

output_path = "02_seaborn_clustermap.png"
g.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#070c09')
print(f"✓ Successfully generated Seaborn hierarchical clustermap: {output_path}")
