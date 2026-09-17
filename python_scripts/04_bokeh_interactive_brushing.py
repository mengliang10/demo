"""
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
