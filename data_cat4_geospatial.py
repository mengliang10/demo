"""
Category 4: Geospatial & Mapping (6 tools)
Contains authentic paradigms, production Python scripts, mathematical specs, and metrics.
"""

PEERS_CAT4 = [
    {"name": "Folium", "paradigm": "Leaflet.js Interactive Web Maps", "engine": "Leaflet JS / HTML5 DOM", "scale": "50K Markers / GeoJSON", "interactivity": "Tile Pan / Zoom / Tooltips", "learning_curve": "Low"},
    {"name": "GeoPandas", "paradigm": "Spatial Tabular Geometry Engine", "engine": "Shapely / GEOS / PyPROJ", "scale": "1M+ Polygons", "interactivity": "Static Matplotlib / Interactive Explorer", "learning_curve": "Low - Moderate"},
    {"name": "Cartopy", "paradigm": "Cartographic Projection Systems", "engine": "PROJ C++ / Matplotlib", "scale": "Global Satellite Rasters", "interactivity": "Scientific Vector Graticules", "learning_curve": "Moderate - High"},
    {"name": "Geoplotlib", "paradigm": "Hardware-Accelerated Spatial Pygame", "engine": "OpenGL / Pygame", "scale": "2M Points / Flight Tracks", "interactivity": "Real-time Particle Flow", "learning_curve": "Moderate"},
    {"name": "Pydeck (Deck.gl wrapper)", "paradigm": "GPU-Powered 3D Spatial Layers", "engine": "Deck.gl / WebGL Shaders", "scale": "1M+ 3D Hexagons / Arcs", "interactivity": "Smooth 60 FPS 3D Pitch/Bearing", "learning_curve": "Low - Moderate"},
    {"name": "Mapclassify", "paradigm": "Choropleth Statistical Classifiers", "engine": "NumPy / SciPy Optimizers", "scale": "Any Attribute Vector", "interactivity": "Histogram & Interval Binning", "learning_curve": "Low"}
]

TOOLS_CAT4 = [
    {
        "name": "Folium",
        "category": "Geospatial & Mapping",
        "folder": "Folium",
        "pip": "pip install folium pandas",
        "docs": "https://python-visualization.github.io/folium",
        "license": "MIT License",
        "tagline": "Python wrapper for Leaflet.js: renders interactive slippy maps directly into standalone HTML.",
        "peers": PEERS_CAT4,
        "paradigms": [
            {
                "tag": "01 / CHOROPLETH SPATIO-TEMPORAL",
                "title": "Interactive Choropleth with HeatMapWithTime Dynamic Tracking",
                "subtitle": "Binds GeoJSON administrative boundary geometries with tabular pandas metrics and animated time sliders.",
                "math_desc": "Web Mercator coordinate projection: EPSG:3857 mapping spherical latitude/longitude to 2D planar coordinates: $x = R \\lambda, y = R \\ln\\left[\\tan\\left(\\frac{\\pi}{4} + \\frac{\\phi}{2}\\right)\\right]$.",
                "math_formula": "x = \\frac{128}{\\pi} 2^{\\text{zoom}} (\\lambda + \\pi), \\quad y = \\frac{128}{\\pi} 2^{\\text{zoom}} \\left(\\pi - \\ln\\left[\\tan\\left(\\frac{\\pi}{4} + \\frac{\\phi}{2}\\right)\\right]\\right)",
                "time_complexity": "O(N) tile bounding box quadkey query",
                "space_complexity": "O(V) GeoJSON vertex list",
                "enterprise_use": "Nationwide hotel portfolio occupancy rates, municipal disease vector spread monitoring.",
                "strengths": "Instant browser-native interactive maps; zero web server setup; outputs self-contained HTML.",
                "tradeoffs": "Client-side Leaflet DOM struggles with GeoJSON files exceeding ~15MB.",
                "metrics": [
                    {"label": "Engine", "val": "Leaflet.js v1.9", "sub": "HTML5 Slippy Map"},
                    {"label": "Projection", "val": "EPSG:3857", "sub": "Web Mercator"},
                    {"label": "Plugins", "val": "HeatMapWithTime", "sub": "Time Slider"},
                    {"label": "Tiles", "val": "OSM / CartoDB", "sub": "Dark Matter"}
                ],
                "code": """import folium
from folium.plugins import HeatMap
import numpy as np

# Center on Singapore
m = folium.Map(location=[1.3521, 103.8198], zoom_start=12, tiles="CartoDB dark_matter")

# Generate synthetic customer trip locations
lats = 1.3521 + np.random.normal(0, 0.05, n_samples)
lons = 103.8198 + np.random.normal(0, 0.05, n_samples)
heat_data = [[lat, lon, 1.0] for lat, lon in zip(lats, lons)]

HeatMap(heat_data, radius=15, blur=10, min_opacity=0.4).add_to(m)
m.save("folium_map.html")"""
            }
        ]
    },
    {
        "name": "GeoPandas",
        "category": "Geospatial & Mapping",
        "folder": "GeoPandas",
        "pip": "pip install geopandas shapely pyproj",
        "docs": "https://geopandas.org",
        "license": "BSD 3-Clause",
        "tagline": "Extends the datatypes used by pandas to allow spatial operations on geometric types.",
        "peers": PEERS_CAT4,
        "paradigms": [
            {
                "tag": "01 / SPATIAL JOINS & BUFFERING",
                "title": "Vector Spatial Joins & Multi-Ring Buffer Intersections",
                "subtitle": "GEOS-accelerated point-in-polygon queries, Voronoi tessellations, and CRS reprojection.",
                "math_desc": "Ray-casting point-in-polygon Jordan Curve Theorem: point $P$ is interior if an arbitrary ray intersects polygon edges an odd number of times.",
                "math_formula": "\\mathcal{J}(P, \\mathcal{P}) = \\left( \\sum_{e \\in \\mathcal{P}} \\mathbb{I}(\\text{Ray}(P) \\cap e) \\right) \\pmod 2 \\equiv 1",
                "time_complexity": "O(N \\log M) with R-tree spatial index",
                "space_complexity": "O(N) Shapely C-pointer geometry array",
                "enterprise_use": "Catchment area customer demographic profiling, urban zoning flood risk spatial joins.",
                "strengths": "Combines full power of pandas DataFrame manipulation with spatial C-geometry algorithms.",
                "tradeoffs": "Requires GEOS, GDAL, and PROJ system libraries.",
                "metrics": [
                    {"label": "Engine", "val": "GEOS C++ / Shapely", "sub": "Hardware Spatial"},
                    {"label": "Indexing", "val": "R-tree / STRtree", "sub": "Sub-millisecond Join"},
                    {"label": "CRS", "val": "PyPROJ 4.x", "sub": "EPSG Transformations"},
                    {"label": "API", "val": "GeoDataFrame", "sub": "Pandas Integrated"}
                ],
                "code": """import geopandas as gpd
from shapely.geometry import Point
import numpy as np

# Create GeoDataFrame of hotel property coordinates
lats = np.random.uniform(1.25, 1.45, n_samples)
lons = np.random.uniform(103.7, 103.95, n_samples)
geometry = [Point(xy) for xy in zip(lons, lats)]

gdf = gpd.GeoDataFrame({'Hotel_ID': range(n_samples), 'ADR': np.random.normal(250, 40, n_samples)},
                        geometry=geometry, crs="EPSG:4326")

# Re-project to UTM Zone 48N (meters) and create 1km buffer
gdf_utm = gdf.to_crs(epsg=32648)
gdf_utm['Buffer_1km'] = gdf_utm.buffer(1000)

print(f"Computed spatial buffers for {len(gdf)} properties.")"""
            }
        ]
    },
    {
        "name": "Cartopy",
        "category": "Geospatial & Mapping",
        "folder": "Cartopy",
        "pip": "pip install cartopy matplotlib",
        "docs": "https://scitools.org.uk/cartopy",
        "license": "LGPL 3.0",
        "tagline": "Geospatial data processing library designed for map generation and cartographic analysis in Matplotlib.",
        "peers": PEERS_CAT4,
        "paradigms": [
            {
                "tag": "01 / CARTOGRAPHIC PROJECTIONS",
                "title": "Global Cartographic Projections with Geodetic Great Circles",
                "subtitle": "Transforms global coordinate systems across Orthographic, Robinson, and Lambert Conformal Conic projections.",
                "math_desc": "Geodesic shortest path on an oblate spheroid (WGS84) computed via Vincenty inverse problem formulation.",
                "math_formula": "\\tan\\sigma = \\frac{\\sqrt{(\\cos U_2 \\sin\\lambda)^2 + (\\cos U_1 \\sin U_2 - \\sin U_1 \\cos U_2 \\cos\\lambda)^2}}{\\sin U_1 \\sin U_2 + \\cos U_1 \\cos U_2 \\cos\\lambda}",
                "time_complexity": "O(N) PROJ coordinate projection passes",
                "space_complexity": "O(N) coastline polygon vertices",
                "enterprise_use": "International airline route flight-path optimization, IPCC climate warming simulation grids.",
                "strengths": "True cartographic transformations with accurate land boundary and graticule clipping.",
                "tradeoffs": "High computational overhead when reprojecting large raster arrays.",
                "metrics": [
                    {"label": "Library", "val": "UK Met Office", "sub": "Climatology Standard"},
                    {"label": "Projections", "val": "60+ Carto CRSs", "sub": "PROJ Backend"},
                    {"label": "Geodesics", "val": "Great Circle Paths", "sub": "Curved Arcs"},
                    {"label": "Features", "val": "Natural Earth", "sub": "Coastlines & Borders"}
                ],
                "code": """import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6), facecolor='#050806')
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
ax.set_facecolor('#0a110d')

ax.add_feature(cfeature.LAND, facecolor='#122119')
ax.add_feature(cfeature.OCEAN, facecolor='#050806')
ax.add_feature(cfeature.COASTLINE, edgecolor='#00e676', linewidth=0.8)
ax.gridlines(color='#94a3b8', alpha=0.3, linestyle='--')

# Plot geodesic flight path: Singapore to Seoul
ax.plot([103.8198, 126.9780], [1.3521, 37.5665], color='#f3cf65', linewidth=2,
        transform=ccrs.Geodetic(), label='SIN - ICN Flight Path')

ax.set_title('Global Great Circle Geodesic Routing', color='#fffefa')
plt.savefig('cartopy_map.png')"""
            }
        ]
    },
    {
        "name": "Geoplotlib",
        "category": "Geospatial & Mapping",
        "folder": "Geoplotlib",
        "pip": "pip install geoplotlib pyopengl",
        "docs": "https://github.com/andrea-cuttone/geoplotlib",
        "license": "GPL 3.0",
        "tagline": "Hardware-accelerated Python toolbox for visualizing geographical data and flow animations.",
        "peers": PEERS_CAT4,
        "paradigms": [
            {
                "tag": "01 / GPU HARDWARE FLIGHT TRACKS",
                "title": "Hardware-Accelerated Flight Tracks & Particle Flows",
                "subtitle": "Renders millions of geographic coordinate vectors at 60 FPS using raw Pygame and OpenGL buffers.",
                "math_desc": "Temporal particle advection: $\\mathbf{x}_{t+\\Delta t} = \\mathbf{x}_t + \\mathbf{v}(\\mathbf{x}_t) \\Delta t$ rendered with trail decay transparency.",
                "math_formula": "I_{\\text{trail}}(t) = I_0 \\cdot e^{-\\lambda (t - t_0)}",
                "time_complexity": "O(N) hardware particle rendering",
                "space_complexity": "O(N) vertex coordinate array",
                "enterprise_use": "Global maritime shipping AIS vessel tracking, airline fleet real-time positioning.",
                "strengths": "Incredible raw performance for animated particle movements and high-density spatial trails.",
                "tradeoffs": "Desktop Pygame window; requires desktop display environment.",
                "metrics": [
                    {"label": "Engine", "val": "Pygame / OpenGL", "sub": "Hardware 60 FPS"},
                    {"label": "Particles", "val": "2,000,000 Pts", "sub": "Realtime Advection"},
                    {"label": "Animation", "val": "Trail Alpha Decay", "sub": "Motion Blur"},
                    {"label": "License", "val": "GPL 3.0", "sub": "Open Source"}
                ],
                "code": """import geoplotlib
import pandas as pd
import numpy as np

# Generate sample origin-destination pairs
data = pd.DataFrame({
    'lat1': [1.3521, 22.3193, 35.6762],
    'lon1': [103.8198, 114.1694, 139.6503],
    'lat2': [37.5665, 1.3521, 1.3521],
    'lon2': [126.9780, 103.8198, 103.8198]
})

geoplotlib.graph(data, src_lat='lat1', src_lon='lon1', dest_lat='lat2', dest_lon='lon2',
                 color=[0, 230, 118, 200], linewidth=2)
geoplotlib.show()"""
            }
        ]
    },
    {
        "name": "Pydeck (Deck.gl wrapper)",
        "category": "Geospatial & Mapping",
        "folder": "Pydeck (Deck.gl wrapper)",
        "pip": "pip install pydeck pandas",
        "docs": "https://deckgl.readthedocs.io",
        "license": "Apache 2.0",
        "tagline": "High-scale WebGL-powered 3D geospatial data analysis in Python using Uber's Deck.gl.",
        "peers": PEERS_CAT4,
        "paradigms": [
            {
                "tag": "01 / 3D HEXAGON SPATIAL AGGREGATION",
                "title": "3D HexagonLayer & Great-Circle ArcLayer WebGL",
                "subtitle": "Dynamically aggregates hundreds of thousands of GPS coordinates into 3D hexagonal prisms with elevation extrusion.",
                "math_desc": "Hexagonal spatial binning: $H(q, r) = \\lfloor \\mathbf{M}_{\\text{axial}} \\cdot (x, y)^T \\rceil$ with extruded 3D height proportional to bin density.",
                "math_formula": "h_{\\text{elevation}} = \\alpha \\cdot \\log(1 + \\text{Count}_{\\text{hex}}), \\quad \\text{Pitch} = 45^\\circ",
                "time_complexity": "O(N) GPU instanced draw call",
                "space_complexity": "O(K) aggregated hexagon mesh",
                "enterprise_use": "Ride-sharing dynamic surge pricing demand surfaces (Uber), urban mobility foot-traffic heatmaps.",
                "strengths": "Stunning 3D perspective pitch and bearing; handles 1,000,000+ points smoothly in browser WebGL.",
                "tradeoffs": "Requires Mapbox token or Carto basemap tiles for underlying satellite imagery.",
                "metrics": [
                    {"label": "WebGL Engine", "val": "Deck.gl v8.9", "sub": "Hardware Shaders"},
                    {"label": "Layer Types", "val": "Hexagon, Arc, Grid", "sub": "3D Extrusions"},
                    {"label": "Points", "val": "1,000,000+ Pts", "sub": "Smooth 60 FPS"},
                    {"label": "Camera", "val": "Pitch, Bearing, Zoom", "sub": "3D Perspective"}
                ],
                "code": """import pydeck as pdk
import pandas as pd
import numpy as np

# Generate 100,000 coordinates across Singapore
df = pd.DataFrame({
    'lat': 1.3521 + np.random.normal(0, 0.04, n_samples * 100),
    'lon': 103.8198 + np.random.normal(0, 0.04, n_samples * 100)
})

layer = pdk.Layer(
    "HexagonLayer",
    df,
    get_position=["lon", "lat"],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1
)

view_state = pdk.ViewState(longitude=103.8198, latitude=1.3521, zoom=11, min_zoom=5, max_zoom=15, pitch=45, bearing=15)
r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style="dark")
r.to_html("pydeck_3d_hex.html")"""
            }
        ]
    },
    {
        "name": "Mapclassify",
        "category": "Geospatial & Mapping",
        "folder": "Mapclassify",
        "pip": "pip install mapclassify pandas",
        "docs": "https://pysal.org/mapclassify",
        "license": "BSD 3-Clause",
        "tagline": "Classification schemes for choropleth mapping from the Python Spatial Analysis Library (PySAL).",
        "peers": PEERS_CAT4,
        "paradigms": [
            {
                "tag": "01 / STATISTICAL CHOROPLETH BINNING",
                "title": "Fisher-Jenks Optimal Natural Breaks Classification",
                "subtitle": "Minimizes within-class variance and maximizes between-class variance across choropleth attributes.",
                "math_desc": "Fisher-Jenks dynamic programming algorithm minimizing Goodness of Variance Fit (GVF).",
                "math_formula": "\\text{GVF} = 1 - \\frac{\\sum_{j=1}^k \\sum_{i \\in C_j} (x_i - \\bar{x}_j)^2}{\\sum_{i=1}^N (x_i - \\bar{x})^2}",
                "time_complexity": "O(k N^2) dynamic programming solver",
                "space_complexity": "O(k N) classification matrix",
                "enterprise_use": "Government census poverty demographic mapping, property tax assessment district zoning.",
                "strengths": "Statistically rigorous binning preventing misleading cartographic visual distortion.",
                "tradeoffs": "Computationally intensive on huge arrays; requires subsampling for $N > 100,000$.",
                "metrics": [
                    {"label": "Algorithm", "val": "Fisher-Jenks", "sub": "Optimal Breaks"},
                    {"label": "Goodness of Fit", "val": "GVF Optimization", "sub": "Max Variance Exp"},
                    {"label": "Alternatives", "val": "Quantiles, Equal, Box", "sub": "12 Schemes"},
                    {"label": "Part of", "val": "PySAL Ecosystem", "sub": "Spatial Analysis"}
                ],
                "code": """import mapclassify
import numpy as np

# Generate skewed wealth distribution
data = np.random.lognormal(mean=10, sigma=1.2, size=n_samples)

# Compute Fisher-Jenks Natural Breaks into 5 classes
fj = mapclassify.FisherJenks(data, k=5)
print(f"Computed Fisher-Jenks Bins: {fj.bins}")
print(f"Goodness of Variance Fit (GVF): {fj.adcm}")"""
            }
        ]
    }
]
