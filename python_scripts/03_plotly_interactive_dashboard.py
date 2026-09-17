"""
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
