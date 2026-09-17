"""
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
