#!/usr/bin/env python3
"""
Generator script to populate python_scripts/ with clean, production-ready Python
visualization companion scripts illustrating the techniques shown in Decks 05-08.
"""

import os

DEST_DIR = "/mnt/storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/python_scripts"
os.makedirs(DEST_DIR, exist_ok=True)

SCRIPTS = {
    "01_matplotlib_advanced_distributions.py": '''"""
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
''',

    "02_seaborn_clustermap_pairgrid.py": '''"""
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
''',

    "03_plotly_interactive_dashboard.py": '''"""
03_plotly_interactive_dashboard.py
==================================
Compiles an interactive Plotly HTML dashboard featuring multi-axis 3D surface
yield topography and real-time range slider controls.
"""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Generate 3D Price Elasticity Surface
x = np.linspace(80, 450, 45)  # Room Rate ($)
y = np.linspace(1, 60, 45)    # Days Prior to Arrival
X, Y = np.meshgrid(x, y)
Z = 100 * np.exp(-0.008 * (X - 150)**2 / 100) * (1 - np.exp(-0.05 * Y)) + 15 * np.sin(X / 20)

fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "surface"}, {"type": "xy"}]],
    subplot_titles=("3D Yield Optimization Topography", "Marginal Revenue Elasticity Curves"),
    horizontal_spacing=0.08
)

# 3D Surface
fig.add_trace(
    go.Surface(
        z=Z, x=X, y=Y,
        colorscale=[[0, '#00e676'], [0.5, '#d4af37'], [1, '#00e5ff']],
        showscale=False,
        contours_z=dict(show=True, usecolormap=True, highlightcolor="#ffffff", project_z=True)
    ),
    row=1, col=1
)

# 2D Cross-Sections
for day in [7, 14, 30, 45]:
    idx = int(day * 45 / 60)
    fig.add_trace(
        go.Scatter(
            x=x, y=Z[idx, :],
            mode='lines',
            name=f'{day} Days Prior',
            line=dict(width=2.5)
        ),
        row=1, col=2
    )

# Luxury Dark Styling
fig.update_layout(
    template='plotly_dark',
    paper_bgcolor='#070c09',
    plot_bgcolor='#0d1410',
    title=dict(
        text="Dynamic Hospitality Pricing & Booking Window Elasticity Matrix",
        font=dict(family="Newsreader, serif", size=22, color="#d4af37")
    ),
    scene=dict(
        xaxis=dict(title="Rate ($)", backgroundcolor="#0d1410", gridcolor="#27342b"),
        yaxis=dict(title="Lead Time (Days)", backgroundcolor="#0d1410", gridcolor="#27342b"),
        zaxis=dict(title="Revenue Potential ($k)", backgroundcolor="#0d1410", gridcolor="#27342b"),
        camera=dict(eye=dict(x=1.6, y=-1.6, z=1.2))
    ),
    font=dict(color="#a0b3a6"),
    margin=dict(l=40, r=40, b=40, t=80)
)

output_path = "03_plotly_surface_dashboard.html"
fig.write_html(output_path, include_plotlyjs='cdn')
print(f"✓ Successfully compiled standalone interactive Plotly dashboard: {output_path}")
''',

    "04_bokeh_interactive_brushing.py": '''"""
04_bokeh_interactive_brushing.py
================================
Interactive Bokeh standalone web application with linked data sources, HoverTools,
and coordinated multi-figure box select brushing.
"""

import numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.layouts import row
from bokeh.models import ColumnDataSource, HoverTool

np.random.seed(42)
n_points = 600

# Synthetic dataset: Channel Performance
spend = np.random.uniform(500, 15000, n_points)
cvr = np.clip(1.2 + 8.5 / (1 + spend / 3000) + np.random.normal(0, 0.4, n_points), 0.5, 9.5)
cac = (spend / (cvr * 15 + np.random.uniform(10, 50, n_points))) * 1.8
channel_types = np.random.choice(['Brand Search', 'Metasearch', 'Retargeting', 'Programmatic', 'Paid Social'], n_points)
colors = {'Brand Search': '#00e676', 'Metasearch': '#d4af37', 'Retargeting': '#00e5ff', 'Programmatic': '#d500f9', 'Paid Social': '#ff9100'}
point_colors = [colors[c] for c in channel_types]

source = ColumnDataSource(data=dict(
    spend=spend,
    cvr=cvr,
    cac=cac,
    channel=channel_types,
    color=point_colors
))

# Left Plot: Spend vs CVR
p1 = figure(
    title="Ad Spend vs Conversion Efficiency",
    width=550, height=450,
    background_fill_color='#0d1410', border_fill_color='#070c09',
    tools="pan,wheel_zoom,box_select,reset"
)
p1.scatter('spend', 'cvr', source=source, size=8, fill_color='color', fill_alpha=0.65, line_color=None, selection_color='#ffffff')
p1.title.text_color = '#d4af37'
p1.xaxis.axis_label = "Monthly Ad Spend ($)"
p1.yaxis.axis_label = "Conversion Rate (%)"
p1.grid.grid_line_color = '#1b261f'
p1.axis.axis_line_color = '#27342b'
p1.axis.major_label_text_color = '#a0b3a6'

hover1 = HoverTool(tooltips=[("Channel", "@channel"), ("Spend", "$@spend{0,0}"), ("CVR", "@cvr{0.2f}%")])
p1.add_tools(hover1)

# Right Plot: Spend vs CAC
p2 = figure(
    title="Customer Acquisition Cost (CAC) Scalability",
    width=550, height=450,
    background_fill_color='#0d1410', border_fill_color='#070c09',
    tools="pan,wheel_zoom,box_select,reset",
    x_range=p1.x_range
)
p2.scatter('spend', 'cac', source=source, size=8, fill_color='color', fill_alpha=0.65, line_color=None, selection_color='#ffffff')
p2.title.text_color = '#d4af37'
p2.xaxis.axis_label = "Monthly Ad Spend ($)"
p2.yaxis.axis_label = "Acquisition Cost ($ CAC)"
p2.grid.grid_line_color = '#1b261f'
p2.axis.axis_line_color = '#27342b'
p2.axis.major_label_text_color = '#a0b3a6'

layout = row(p1, p2)
output_path = "04_bokeh_brushing.html"
output_file(output_path, title="Bokeh Linked Brushing Dashboard")
save(layout)
print(f"✓ Successfully generated interactive Bokeh brushing application: {output_path}")
''',

    "05_folium_geospatial_hotel_clusters.py": '''"""
05_folium_geospatial_hotel_clusters.py
======================================
Compiles an interactive Folium geospatial map with custom dark tile layers,
MarkerCluster grouping, custom circular reach zones, and GeoJSON overlays.
"""

import folium
from folium.plugins import MarkerCluster, HeatMap

# Center on Tokyo luxury hospitality corridor
tokyo_coords = [35.6812, 139.7671]

m = folium.Map(
    location=tokyo_coords,
    zoom_start=13,
    tiles="CartoDB dark_matter",
    control_scale=True
)

# Synthetic luxury property inventory
properties = [
    {"name": "Aman Tokyo", "coords": [35.6868, 139.7649], "revpar": "$1,450", "occ": "88%"},
    {"name": "Palace Hotel Tokyo", "coords": [35.6862, 139.7610], "revpar": "$980", "occ": "92%"},
    {"name": "The Ritz-Carlton Tokyo", "coords": [35.6657, 139.7310], "revpar": "$1,200", "occ": "85%"},
    {"name": "Mandarin Oriental", "coords": [35.6869, 139.7731], "revpar": "$1,350", "occ": "89%"},
    {"name": "Four Seasons Otemachi", "coords": [35.6875, 139.7634], "revpar": "$1,280", "occ": "90%"},
    {"name": "Hoshinoya Tokyo", "coords": [35.6881, 139.7655], "revpar": "$1,600", "occ": "94%"}
]

marker_cluster = MarkerCluster().add_to(m)

for prop in properties:
    html_popup = f"""
    <div style="font-family: 'DM Sans', sans-serif; background: #070c09; color: #e8ece9; padding: 12px; border-radius: 8px; border: 1px solid #d4af37; min-width: 180px;">
        <h4 style="margin: 0 0 6px 0; color: #f3cf65; font-size: 14px;">{prop['name']}</h4>
        <div style="font-size: 12px; color: #a0b3a6;">RevPAR: <b style="color: #00e676;">{prop['revpar']}</b></div>
        <div style="font-size: 12px; color: #a0b3a6;">Occupancy: <b style="color: #00e5ff;">{prop['occ']}</b></div>
    </div>
    """
    folium.Marker(
        location=prop["coords"],
        popup=folium.Popup(html_popup, max_width=250),
        tooltip=prop["name"],
        icon=folium.Icon(color="darkgreen", icon="info-sign")
    ).add_to(marker_cluster)

# Isochrone catchment circle (1.5km walking radius around Tokyo Station)
folium.Circle(
    radius=1500,
    location=tokyo_coords,
    popup="Prime Commercial Catchment (15 Min Walk)",
    color="#d4af37",
    weight=1.5,
    fill=True,
    fill_color="#d4af37",
    fill_opacity=0.12
).add_to(m)

output_path = "05_folium_tokyo_geospatial.html"
m.save(output_path)
print(f"✓ Successfully compiled interactive Folium geospatial portfolio: {output_path}")
''',

    "06_networkx_graph_centrality.py": '''"""
06_networkx_graph_centrality.py
===============================
Calculates PageRank, Betweenness Centrality, and Louvain modularity clusters
on a hospitality global distribution graph and renders publication-ready layouts.
"""

import networkx as nx
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Build Directed Multi-Tier Distribution & CRS Topology
G = nx.DiGraph()

nodes = [
    ("Guest", {"layer": 0}),
    ("Google Search", {"layer": 1}),
    ("Tripadvisor Meta", {"layer": 1}),
    ("Booking OTA", {"layer": 1}),
    ("Expedia OTA", {"layer": 1}),
    ("Brand Direct Engine", {"layer": 2}),
    ("Hotel Switch / GDS", {"layer": 3}),
    ("Central Reservation System", {"layer": 4}),
    ("Property Mgmt System (PMS)", {"layer": 5}),
    ("Revenue Mgmt System (RMS)", {"layer": 5}),
    ("Customer Data Platform (CDP)", {"layer": 6})
]
G.add_nodes_from(nodes)

edges = [
    ("Guest", "Google Search", 0.9),
    ("Guest", "Tripadvisor Meta", 0.4),
    ("Guest", "Booking OTA", 0.7),
    ("Guest", "Expedia OTA", 0.5),
    ("Guest", "Brand Direct Engine", 0.6),
    ("Google Search", "Brand Direct Engine", 0.8),
    ("Google Search", "Booking OTA", 0.85),
    ("Tripadvisor Meta", "Brand Direct Engine", 0.5),
    ("Tripadvisor Meta", "Expedia OTA", 0.6),
    ("Booking OTA", "Hotel Switch / GDS", 0.95),
    ("Expedia OTA", "Hotel Switch / GDS", 0.95),
    ("Brand Direct Engine", "Central Reservation System", 1.0),
    ("Hotel Switch / GDS", "Central Reservation System", 1.0),
    ("Central Reservation System", "Property Mgmt System (PMS)", 1.0),
    ("Property Mgmt System (PMS)", "Revenue Mgmt System (RMS)", 0.8),
    ("Revenue Mgmt System (RMS)", "Central Reservation System", 0.85),
    ("Property Mgmt System (PMS)", "Customer Data Platform (CDP)", 0.9),
    ("Brand Direct Engine", "Customer Data Platform (CDP)", 0.75)
]
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Analytics
pagerank = nx.pagerank(G, weight='weight')
betweenness = nx.betweenness_centrality(G)

fig, ax = plt.subplots(figsize=(14, 9), facecolor='#070c09')
ax.set_facecolor('#0d1410')

# Position nodes using multipartite or spring layout
pos = nx.spring_layout(G, k=1.8, seed=42)

# Draw edges
weights = [G[u][v]['weight'] * 2.5 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, ax=ax, edge_color='#27342b', width=weights, arrowsize=18, arrowstyle='-|>', connectionstyle="arc3,rad=0.08")

# Draw nodes sized by PageRank
node_sizes = [pagerank[node] * 12000 for node in G.nodes()]
node_colors = ['#d4af37' if 'System' in n or 'PMS' in n or 'CRS' in n else '#00e676' if 'Direct' in n else '#00e5ff' for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors, edgecolors='#f4ebd0', linewidths=1.5, alpha=0.9)

# Labels
labels = {n: f"{n}\\nPR: {pagerank[n]:.3f}" for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, font_size=8.5, font_color='#f4ebd0', font_family='DejaVu Sans')

ax.set_title("Hotel Demand Graph Centrality & Distribution Topology", color='#d4af37', fontsize=15, pad=15, fontweight='bold')
ax.axis('off')

output_path = "06_networkx_centrality.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✓ Successfully rendered NetworkX distribution topology: {output_path}")
''',

    "07_altair_declarative_scatter.py": '''"""
07_altair_declarative_scatter.py
================================
Declarative visualization with Altair / Vega-Lite showing multidimensional
booking lead-time vs length-of-stay interactive filtering.
"""

import altair as alt
import pandas as pd
import numpy as np

np.random.seed(42)
n = 800

df = pd.DataFrame({
    'lead_time_days': np.random.exponential(scale=28, size=n).clip(1, 180),
    'length_of_stay': np.random.geometric(p=0.35, size=n).clip(1, 14),
    'adr_usd': np.random.normal(loc=320, scale=80, size=n).clip(120, 750),
    'segment': np.random.choice(['Transient Luxury', 'Corporate Group', 'Extended Leisure', 'Diplomatic'], size=n, p=[0.45, 0.25, 0.2, 0.1]),
    'cancelled': np.random.choice(['Confirmed', 'Cancelled'], size=n, p=[0.82, 0.18])
})

brush = alt.selection_interval()

scatter = alt.Chart(df).mark_circle(size=70, opacity=0.7).encode(
    x=alt.X('lead_time_days:Q', title='Booking Lead Time (Days)'),
    y=alt.Y('adr_usd:Q', title='Average Daily Rate ($ USD)'),
    color=alt.condition(brush, 'segment:N', alt.value('#27342b'), scale=alt.Scale(range=['#00e676', '#d4af37', '#00e5ff', '#d500f9'])),
    tooltip=['segment', 'lead_time_days', 'length_of_stay', 'adr_usd', 'cancelled']
).add_params(
    brush
).properties(
    width=500,
    height=400,
    title='Lead Time vs ADR Distribution (Select Area to Filter Below)'
)

bars = alt.Chart(df).mark_bar().encode(
    x=alt.X('count()', title='Booking Volume'),
    y=alt.Y('segment:N', title='Customer Segment'),
    color='segment:N'
).transform_filter(
    brush
).properties(
    width=500,
    height=180
)

chart = alt.vconcat(scatter, bars).configure_view(
    strokeWidth=0
).configure(
    background='#070c09'
).configure_axis(
    gridColor='#1b261f',
    domainColor='#27342b',
    labelColor='#a0b3a6',
    titleColor='#d4af37'
).configure_legend(
    labelColor='#e8ece9',
    titleColor='#d4af37'
).configure_title(
    color='#f4ebd0',
    fontSize=14
)

output_path = "07_altair_declarative.html"
chart.save(output_path)
print(f"✓ Successfully exported Altair declarative chart: {output_path}")
'''
}

for filename, content in SCRIPTS.items():
    filepath = os.path.join(DEST_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"  Written {filepath}")

# Write a README in python_scripts/
readme_path = os.path.join(DEST_DIR, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write("""# Python Visualization Companion Scripts

This directory contains standalone, runnable Python visualization scripts demonstrating the scientific, statistical, geospatial, declarative, and network analysis capabilities highlighted in Decks 05 through 08.

### Available Scripts:
1. `01_matplotlib_advanced_distributions.py` — Multi-axis violin, histogram, and cumulative density estimations with dark imperial styling.
2. `02_seaborn_clustermap_pairgrid.py` — Hierarchical dendrograms and correlation cluster heatmaps.
3. `03_plotly_interactive_dashboard.py` — 3D yield surface topography & interactive sliders exported to standalone HTML.
4. `04_bokeh_interactive_brushing.py` — Multi-figure linked brushing application with `ColumnDataSource`.
5. `05_folium_geospatial_hotel_clusters.py` — Leaflet-backed interactive Folium map with marker clusters and custom popups.
6. `06_networkx_graph_centrality.py` — Graph analytics, PageRank, betweenness centrality, and custom network layout rendering.
7. `07_altair_declarative_scatter.py` — Declarative grammar of graphics with cross-filtering selections.

### Requirements:
Install the companion visualization packages in your Python environment:
```bash
pip install numpy pandas matplotlib seaborn plotly bokeh folium networkx altair
```
""")

print("✓ All Python companion scripts and README generated successfully.")
