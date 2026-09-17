"""
01_matplotlib_advanced_distributions.py
======================================
Comprehensive Matplotlib production script showcasing multi-axis density estimation,
custom quantile annotations, and publication-ready dark theme aesthetics.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Set luxury dark aesthetics
plt.style.use('dark_background')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']
plt.rcParams['axes.edgecolor'] = '#27342b'
plt.rcParams['axes.linewidth'] = 0.8

np.random.seed(42)
n_samples = 2500

# Synthetic multi-segment distribution: Baseline, Campaign Lift, Outlier Demand
baseline = np.random.normal(loc=120, scale=18, size=n_samples)
campaign = np.random.exponential(scale=35, size=n_samples) + 85
blended = np.concatenate([baseline[:1500], campaign[:1000]])

fig = plt.figure(figsize=(14, 8), facecolor='#070c09')
gs = gridspec.GridSpec(2, 2, height_ratios=[1.2, 1], width_ratios=[1.5, 1], hspace=0.3, wspace=0.25)

# Subplot 1: Distribution Histogram & KDE
ax1 = fig.add_subplot(gs[0, :])
ax1.set_facecolor('#0d1410')
counts, bins, patches = ax1.hist(blended, bins=60, density=True, color='#00e676', alpha=0.35, edgecolor='#00e676', linewidth=0.5)

# Quantiles
q25, q50, q75 = np.percentile(blended, [25, 50, 75])
ax1.axvline(q50, color='#d4af37', linestyle='--', linewidth=1.5, label=f'Median: ${q50:.1f}')
ax1.axvline(q25, color='#00e5ff', linestyle=':', linewidth=1.2, label=f'Q1 (25%): ${q25:.1f}')
ax1.axvline(q75, color='#d500f9', linestyle=':', linewidth=1.2, label=f'Q3 (75%): ${q75:.1f}')

ax1.set_title("Luxury ADR & Booking Value Kernel Density Estimation", color='#f4ebd0', fontsize=14, pad=12, fontweight='bold')
ax1.set_xlabel("Net Room Rate ($ USD)", color='#a0b3a6', fontsize=11)
ax1.set_ylabel("Probability Density", color='#a0b3a6', fontsize=11)
ax1.tick_params(colors='#a0b3a6')
ax1.legend(facecolor='#0d1410', edgecolor='#27342b', labelcolor='#e8ece9')
ax1.grid(color='#142219', linestyle='--', alpha=0.6)

# Subplot 2: Violin & Box Plot
ax2 = fig.add_subplot(gs[1, 0])
ax2.set_facecolor('#0d1410')
parts = ax2.violinplot([baseline, campaign], showmeans=False, showmedians=True, showextrema=True)
for pc in parts['bodies']:
    pc.set_facecolor('#d4af37')
    pc.set_edgecolor('#f3cf65')
    pc.set_alpha(0.4)
parts['cmedians'].set_color('#00e676')
parts['cmaxes'].set_color('#27342b')
parts['cmins'].set_color('#27342b')
parts['cbars'].set_color('#27342b')

ax2.set_xticks([1, 2])
ax2.set_xticklabels(['Organic Baseline', 'Paid Campaign Cohort'], color='#a0b3a6')
ax2.set_title("Cohort Dispersion Comparison", color='#f4ebd0', fontsize=12, pad=10)
ax2.tick_params(colors='#a0b3a6')
ax2.grid(color='#142219', linestyle='--', alpha=0.6)

# Subplot 3: Cumulative Distribution
ax3 = fig.add_subplot(gs[1, 1])
ax3.set_facecolor('#0d1410')
sorted_data = np.sort(blended)
cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
ax3.plot(sorted_data, cdf, color='#00e5ff', linewidth=2, label='Empirical CDF')
ax3.axhline(0.8, color='#d500f9', linestyle='--', alpha=0.7, label='80th Percentile Target')
ax3.set_title("Cumulative Yield Trajectory", color='#f4ebd0', fontsize=12, pad=10)
ax3.set_xlabel("ADR ($ USD)", color='#a0b3a6', fontsize=10)
ax3.tick_params(colors='#a0b3a6')
ax3.legend(facecolor='#0d1410', edgecolor='#27342b', labelcolor='#e8ece9', fontsize=9)
ax3.grid(color='#142219', linestyle='--', alpha=0.6)

output_path = "01_matplotlib_distributions.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✓ Successfully rendered Matplotlib distribution suite: {output_path}")
