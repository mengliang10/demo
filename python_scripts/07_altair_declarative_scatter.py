"""
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
