"""
Builder for Deck 07: Python Geospatial & Mapping Visualization
Generates 07-python-geospatial-mapping.html (20 distinct visual paradigms)
"""
import os
from template_engine import generate_deck_html

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_deck():
    deck_meta = {
        'id': 'deck-07',
        'series_num': '07',
        'title': 'Python Geospatial & Mapping Visualization',
        'category': 'Python Geospatial & Maps',
        'subtitle': '20 Spatial Cartographic Paradigms across Folium, GeoPandas, Cartopy, Geoplotlib, and Pydeck'
    }

    slides = [
        # 1. Pydeck 3D Hexagon Layer
        {
            'slide_id': 'slide-01-pydeck-hex',
            'tag': '01 / GPU Spatial Columns',
            'headline': 'GPU 3D Hexagon Extrusion:',
            'headline_span': 'Pydeck HexagonLayer with Pitch',
            'subtitle': 'Deck.gl Python wrapper rendering 3D spatial column density with dynamic camera pitch and lighting.',
            'library_badge': 'Pydeck (Deck.gl Python)',
            'chart_html': """
              <div id="pydeck-hex-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('pydeck-hex-stage');
                  if (!el || !window.Plotly) return;
                  const x = [1, 2, 3, 2, 3, 4, 3, 4, 5];
                  const y = [1, 1, 1, 2, 2, 2, 3, 3, 3];
                  const z = [180, 320, 510, 420, 850, 610, 340, 560, 380];
                  Plotly.newPlot('pydeck-hex-stage', [{
                    type: 'scatter3d', mode: 'markers',
                    x: x, y: y, z: z,
                    marker: { size: 16, color: z, colorscale: 'YlGnBu', symbol: 'square' }
                  }], {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { color: '#9ba9a1' }, yaxis: { color: '#9ba9a1' }, zaxis: { color: '#f3cf65' },
                      camera: { eye: { x: 1.4, y: 1.4, z: 1.1 } }
                    }
                  }, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Spatial quantization into Uber H3 discrete global hexagonal grid cells with GPU-driven elevation extrusion.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Urban rideshare demand density, multi-property guest pickup aggregation, mobile app telemetry.'},
                {'title': 'Technical Strengths', 'desc': 'Seamlessly handles millions of rows directly from Pandas/Polars DataFrames without browser lag.'}
            ],
            'metrics': [
                {'label': 'Engine', 'val': 'Deck.gl WebGL2', 'sub': 'Pydeck Wrapper'},
                {'label': 'Data Binding', 'val': 'Pandas / Polars', 'sub': 'Zero Copy Arrow'},
                {'label': 'Camera', 'val': 'Pitch & Bearing', 'sub': '3D Oblique'},
                {'label': 'Throughput', 'val': '5M+ Points', 'sub': 'GPU Instanced'}
            ],
            'code_snippet': """import pydeck as pdk
layer = pdk.Layer(
    "HexagonLayer", data=df, get_position='[lon, lat]',
    auto_highlight=True, elevation_scale=50, pickable=True,
    elevation_range=[0, 3000], extruded=True
)
r = pdk.Deck(layers=[layer], initial_view_state=view_state)"""
        },

        # 2. Folium Interactive Choropleth with GeoJSON Tooltips
        {
            'slide_id': 'slide-02-folium-choropleth',
            'tag': '02 / Interactive Leaflet Python',
            'headline': 'Interactive Leaflet Wrappers:',
            'headline_span': 'Folium Choropleth with Tooltips',
            'subtitle': 'Pythonic Leaflet wrapper binding GeoJSON country boundaries to Pandas metrics with dynamic color scales.',
            'library_badge': 'Folium / Leaflet.js',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 380 240" style="width:100%; max-height:260px;">
                  <polygon points="50,40 140,30 180,90 120,150 40,110" fill="#00e676" stroke="#fff" stroke-width="1"/>
                  <polygon points="140,30 260,20 290,100 180,90" fill="#d4af37" stroke="#fff" stroke-width="1"/>
                  <polygon points="120,150 180,90 270,160 210,210 100,200" fill="#f3cf65" stroke="#fff" stroke-width="1"/>
                  <polygon points="180,90 290,100 330,170 270,160" fill="#ff1744" stroke="#fff" stroke-width="1"/>
                  <!-- Tooltip popup simulation -->
                  <rect x="190" y="45" width="130" height="34" fill="#070c09" stroke="#f3cf65" rx="4"/>
                  <text x="200" y="60" fill="#fffefa" font-family="DM Sans" font-size="10" font-weight="bold">Region Beta: 68% Direct</text>
                  <text x="200" y="72" fill="#00e676" font-family="JetBrains Mono" font-size="9">RevPAR: $284.50</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Choropleth scalar normalization mapping Pandas Series $x$ to discrete ColorBrewer quintile intervals.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Regional market share reporting, state sales tax distribution, international hotel demand penetration.'},
                {'title': 'Technical Strengths', 'desc': 'Exports directly to standalone self-contained HTML files or embeds smoothly in Jupyter notebooks.'}
            ],
            'metrics': [
                {'label': 'Python Core', 'val': 'folium.Choropleth', 'sub': 'Leaflet Engine'},
                {'label': 'Data Format', 'val': 'GeoJSON + Pandas', 'sub': 'Key-On ID'},
                {'label': 'Color Maps', 'val': 'ColorBrewer', 'sub': 'Perceptual Quintiles'},
                {'label': 'Tooltips', 'val': 'GeoJsonTooltip', 'sub': 'HTML Rich'}
            ],
            'code_snippet': """import folium
m = folium.Map(location=[1.35, 103.82], zoom_start=11)
folium.Choropleth(
    geo_data=geojson_data, data=df,
    columns=['Region', 'RevPAR'], key_on='feature.properties.name',
    fill_color='YlGn', legend_name='Direct RevPAR ($)'
).add_to(m)"""
        },

        # 3. GeoPandas Spatial Join & Geometry Intersection Buffers
        {
            'slide_id': 'slide-03-geopandas-sjoin',
            'tag': '03 / Vector Spatial Algebra',
            'headline': 'Vector Geometric Operations:',
            'headline_span': 'GeoPandas Spatial Join (sjoin)',
            'subtitle': 'R-tree spatial indexing executing fast point-in-polygon queries and geometric buffer intersections.',
            'library_badge': 'GeoPandas / Shapely',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Buffer Polygon 1 -->
                  <circle cx="140" cy="120" r="70" fill="rgba(0,230,118,0.25)" stroke="#00e676" stroke-width="2"/>
                  <!-- Buffer Polygon 2 -->
                  <circle cx="210" cy="120" r="70" fill="rgba(212,175,55,0.25)" stroke="#d4af37" stroke-width="2"/>
                  <!-- Intersection Lens (Bright Gold) -->
                  <path d="M 175 62 A 70 70 0 0 1 175 178 A 70 70 0 0 1 175 62 Z" fill="rgba(243,207,101,0.6)"/>
                  <text x="175" y="124" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="9" font-weight="bold">Intersection</text>
                  <!-- Seed Center Points -->
                  <circle cx="140" cy="120" r="4" fill="#fff"/>
                  <circle cx="210" cy="120" r="4" fill="#fff"/>
                  <text x="175" y="215" text-anchor="middle" fill="#fffefa" font-family="DM Sans" font-size="10">Spatial Join: Buffer(A) ∩ Buffer(B)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Dimensionally Extended 9-Intersection Model (DE-9IM) evaluated via GEOS C++ library backend.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Retail cannibalization between sibling properties, catchment area overlap, environmental buffer zones.'},
                {'title': 'Technical Strengths', 'desc': 'Treats spatial geometries as standard Pandas DataFrame columns with full vectorization.'}
            ],
            'metrics': [
                {'label': 'Data Model', 'val': 'GeoDataFrame', 'sub': 'Shapely Geometry'},
                {'label': 'Index Struct', 'val': 'R-Tree Spatial', 'sub': 'O(log N) Lookup'},
                {'label': 'Backend C++', 'val': 'GEOS / GDAL', 'sub': 'Industry Core'},
                {'label': 'Operations', 'val': 'Union / Intersect', 'sub': 'DE-9IM Topology'}
            ],
            'code_snippet': """import geopandas as gpd
hotels_gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))
buffers = hotels_gdf.buffer(distance=5000) # 5km
joined = gpd.sjoin(points_gdf, buffers, predicate='intersects')"""
        },

        # 4. Cartopy Robinson Projection with Shaded Relief
        {
            'slide_id': 'slide-04-cartopy-robinson',
            'tag': '04 / Publication Cartography',
            'headline': 'Global Equal-Area Balance:',
            'headline_span': 'Cartopy Robinson World Projection',
            'subtitle': 'Pseudocylindrical map projection balancing shape and area distortions for global publication maps.',
            'library_badge': 'Cartopy (SciTools UK Met)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 240" style="width:100%; max-height:260px;">
                  <!-- Curved Robinson Boundary Outline -->
                  <path d="M 60 40 Q 200 25, 340 40 C 370 120, 370 120, 340 200 Q 200 215, 60 200 C 30 120, 30 120, 60 40 Z" fill="#0a140f" stroke="#d4af37" stroke-width="2"/>
                  <!-- Graticule Lines -->
                  <path d="M 45 120 Q 200 120, 355 120" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
                  <path d="M 200 30 Q 200 120, 200 210" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
                  <!-- Continents Schematic -->
                  <ellipse cx="140" cy="90" rx="35" ry="25" fill="#1b382b"/>
                  <ellipse cx="270" cy="90" rx="45" ry="30" fill="#1b382b"/>
                  <ellipse cx="285" cy="160" rx="25" ry="20" fill="#1b382b"/>
                  <ellipse cx="160" cy="155" rx="20" ry="30" fill="#1b382b"/>
                  <!-- Property Hub Pins -->
                  <circle cx="280" cy="115" r="5" fill="#00e676"/>
                  <circle cx="130" cy="85" r="4" fill="#f3cf65"/>
                  <circle cx="240" cy="80" r="4" fill="#f3cf65"/>
                  <text x="200" y="230" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Robinson Projection &bull; Minimal Polar Distortion</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Arthur H. Robinson pseudocylindrical compromise projection using tabular interpolation of latitude offsets.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Annual sustainability ESG global footprint reports, international supply chain maps, academic atlases.'},
                {'title': 'Technical Strengths', 'desc': 'Deep PROJ.4 integration allowing seamless coordinate transformation between any two global projections.'}
            ],
            'metrics': [
                {'label': 'Projection', 'val': 'Robinson World', 'sub': 'Compromise'},
                {'label': 'Institution', 'val': 'SciTools UK Met', 'sub': 'Atmospheric Std'},
                {'label': 'Distortion', 'val': 'Visually Pleasing', 'sub': 'Balanced'},
                {'label': 'Natural Earth', 'val': 'Built-In Vectors', 'sub': 'Coastlines/Borders'}
            ],
            'code_snippet': """import cartopy.crs as ccrs
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
ax.stock_img()
ax.coastlines(color='#d4af37')"""
        },

        # 5. Geoplotlib Voronoi Tessellation & Dot Density
        {
            'slide_id': 'slide-05-geoplotlib-voronoi',
            'tag': '05 / Real-Time Spatial GPU',
            'headline': 'High-Cadence Dot Density:',
            'headline_span': 'Geoplotlib Hardware Tessellation',
            'subtitle': 'Pyglet/OpenGL accelerated spatial visualization rendering live point distributions and dynamic Voronoi cells.',
            'library_badge': 'Geoplotlib (Pyglet/OpenGL)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Voronoi Polygon Mosaic -->
                  <g fill="none" stroke="#00e676" stroke-width="1.2">
                    <polygon points="60,50 140,30 180,90 90,110" fill="rgba(0,230,118,0.15)"/>
                    <polygon points="140,30 240,40 270,110 180,90" fill="rgba(212,175,55,0.15)"/>
                    <polygon points="90,110 180,90 200,180 110,190" fill="rgba(0,229,255,0.15)"/>
                    <polygon points="180,90 270,110 290,180 200,180" fill="rgba(243,207,101,0.15)"/>
                  </g>
                  <!-- High density points inside -->
                  <circle cx="110" cy="70" r="2" fill="#fff"/>
                  <circle cx="120" cy="75" r="2" fill="#fff"/>
                  <circle cx="115" cy="80" r="2" fill="#fff"/>
                  <circle cx="210" cy="75" r="2" fill="#fff"/>
                  <text x="175" y="225" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="10">OpenGL Real-Time Dot Density</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Delaunay triangulation and Voronoi diagram computation compiled directly into OpenGL display lists.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Crime incident dot mapping, voter turnout precinct clustering, delivery driver density.'},
                {'title': 'Technical Strengths', 'desc': 'Hardware-accelerated pan and zoom with sub-pixel dot antialiasing.'}
            ],
            'metrics': [
                {'label': 'Graphics Engine', 'val': 'Pyglet / OpenGL', 'sub': 'Direct Draw'},
                {'label': 'Density Type', 'val': 'Dot Density + Voronoi', 'sub': 'Dual Display'},
                {'label': 'Speed', 'val': 'Interactive 60 FPS', 'sub': 'Hardware Sync'},
                {'label': 'License', 'val': 'Open Source', 'sub': 'Python Native'}
            ],
            'code_snippet': """import geoplotlib
geoplotlib.voronoi(data, cmap='hot')
geoplotlib.dot(data, color=[0, 230, 118, 255])
geoplotlib.show()"""
        },

        # 6. Pydeck Great Circle Flight Path ArcLayer
        {
            'slide_id': 'slide-06-pydeck-arcs',
            'tag': '06 / Great-Circle Flight Arcs',
            'headline': 'Flight Network Telemetry:',
            'headline_span': 'Pydeck Great Circle ArcLayer',
            'subtitle': 'Bézier flight trajectories elevating international airline transit flows above dark base satellite tiles.',
            'library_badge': 'Pydeck ArcLayer',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 240" style="width:100%; max-height:260px;">
                  <!-- Base Map Grid -->
                  <rect x="30" y="30" width="340" height="180" fill="#08100c" stroke="rgba(255,255,255,0.12)" rx="6"/>
                  <!-- Parabolic Arcs -->
                  <path d="M 70 150 Q 180 30, 310 140" fill="none" stroke="#00e676" stroke-width="3" stroke-linecap="round"/>
                  <path d="M 70 150 Q 150 50, 240 160" fill="none" stroke="#f3cf65" stroke-width="2.5" stroke-linecap="round"/>
                  <!-- Nodes -->
                  <circle cx="70" cy="150" r="7" fill="#00e676"/>
                  <circle cx="310" cy="140" r="6" fill="#f3cf65"/>
                  <circle cx="240" cy="160" r="6" fill="#f3cf65"/>
                  <text x="70" y="175" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="9">SIN Hub</text>
                  <text x="310" y="165" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">LHR</text>
                  <text x="240" y="185" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">DXB</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Spherical linear interpolation (SLERP) computing geodesic shortest-distance flight curves.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Aviation fleet routes, inter-hotel guest origin tracking, international cargo logistics.'},
                {'title': 'Technical Strengths', 'desc': 'Direct GPU vertex shader elevation calculation with animated pulse particles along the arcs.'}
            ],
            'metrics': [
                {'label': 'Arc Curve', 'val': 'SLERP Geodesic', 'sub': 'True Shortest'},
                {'label': 'GPU Shaders', 'val': 'Instanced Draw', 'sub': '100k Arcs'},
                {'label': 'Animation', 'val': 'Pulse Particles', 'sub': 'Trip Duration'},
                {'label': 'Ecosystem', 'val': 'Deck.gl Python', 'sub': 'Uber Tech'}
            ],
            'code_snippet': """arc_layer = pdk.Layer(
    "ArcLayer", data=flights_df,
    get_source_position='[origin_lon, origin_lat]',
    get_target_position='[dest_lon, dest_lat]',
    get_source_color=[0, 230, 118], get_target_color=[243, 207, 101]
)"""
        },

        # 7. Folium HeatMapWithTime Animated Temporal Slider
        {
            'slide_id': 'slide-07-folium-heat-time',
            'tag': '07 / Spatiotemporal Heatmaps',
            'headline': 'Temporal Heatwave Evolution:',
            'headline_span': 'Folium HeatMapWithTime Slider',
            'subtitle': 'Playback controls animating hourly tourist foot traffic migration across city districts over 24-hour cycles.',
            'library_badge': 'Folium.plugins',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; padding:15px; box-sizing:border-box;">
                <svg viewBox="0 0 350 180" style="width:100%; max-height:190px;">
                  <rect x="20" y="20" width="310" height="140" fill="#08100c" stroke="rgba(255,255,255,0.15)" rx="6"/>
                  <circle cx="150" cy="80" r="45" fill="rgba(0,230,118,0.4)" filter="blur(6px)"/>
                  <circle cx="150" cy="80" r="20" fill="rgba(255,23,68,0.7)" filter="blur(4px)"/>
                  <circle cx="230" cy="100" r="30" fill="rgba(212,175,55,0.4)" filter="blur(5px)"/>
                </svg>
                <!-- Playback Slider Bar -->
                <div style="width:80%; display:flex; align-items:center; gap:10px; margin-top:8px;">
                  <button class="ctrl-btn" style="background:#00e676; color:#070c09; font-weight:bold;">&#9658; Play</button>
                  <div style="flex:1; height:6px; background:rgba(255,255,255,0.15); border-radius:3px; position:relative;">
                    <div style="position:absolute; left:0; width:65%; height:100%; background:#00e676; border-radius:3px;"></div>
                  </div>
                  <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#fffefa;">18:00 Peak</span>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Temporal slice indexing: $H_t(x, y) = \\text{KDE}(P_t)$ sequenced across continuous time frames.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Tourist footfall migration across nightlife districts, peak taxi demand times, epidemic spread tracking.'},
                {'title': 'Technical Strengths', 'desc': 'Interactive play/pause slider widget embedded directly into standalone HTML outputs.'}
            ],
            'metrics': [
                {'label': 'Playback', 'val': 'Animated Slider', 'sub': 'Play/Pause'},
                {'label': 'Slices', 'val': '24-Hour Cadence', 'sub': 'Hourly Steps'},
                {'label': 'Smoothing', 'val': 'Gaussian Blur', 'sub': 'Dynamic Radius'},
                {'label': 'Output', 'val': 'Standalone HTML', 'sub': 'Zero Server'}
            ],
            'code_snippet': """from folium.plugins import HeatMapWithTime
HeatMapWithTime(data_by_hour, radius=25, auto_play=True,
                max_opacity=0.8).add_to(m)"""
        },

        # 8. Cartopy Polar Stereographic Arctic Sea Ice Contours
        {
            'slide_id': 'slide-08-cartopy-polar',
            'tag': '08 / Climatological Projections',
            'headline': 'High-Latitude Sea Ice:',
            'headline_span': 'Cartopy Polar Stereographic Contours',
            'subtitle': 'True polar projection mapping multi-year Arctic ice concentration contours and navigation corridors.',
            'library_badge': 'Cartopy NorthPolarStereo',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 280 280" style="width:250px; height:250px;">
                  <circle cx="140" cy="140" r="110" fill="#070d09" stroke="#d4af37" stroke-width="2"/>
                  <!-- Polar Graticules -->
                  <circle cx="140" cy="140" r="80" fill="none" stroke="rgba(255,255,255,0.12)" stroke-dasharray="3"/>
                  <circle cx="140" cy="140" r="50" fill="none" stroke="rgba(255,255,255,0.12)" stroke-dasharray="3"/>
                  <!-- Arctic Ice Extent Area -->
                  <path d="M 140 70 Q 190 90, 190 140 T 130 190 T 90 130 Z" fill="rgba(0,229,255,0.3)" stroke="#00e5ff" stroke-width="1.5"/>
                  <circle cx="140" cy="140" r="4" fill="#fff"/>
                  <text x="140" y="130" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9">North Pole</text>
                  <text x="140" y="225" text-anchor="middle" fill="#00e5ff" font-family="JetBrains Mono" font-size="9">Sea Ice Concentration &gt; 85%</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Conformal stereographic azimuthal projection centered at $90^\\circ\\text{N}$ with true scale at $71^\\circ\\text{N}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Arctic maritime Northwest Passage transit planning, global climate sea-ice monitoring, polar aviation.'},
                {'title': 'Technical Strengths', 'desc': 'Eliminates boundary wrapping tears inherent in Mercator projections around the poles.'}
            ],
            'metrics': [
                {'label': 'Projection', 'val': 'NorthPolarStereo', 'sub': 'Conformal'},
                {'label': 'Scale Lat', 'val': '71°N True Scale', 'sub': 'NSIDC Standard'},
                {'label': 'Contours', 'val': 'Ice Concentration', 'sub': 'Filled Isobars'},
                {'label': 'Science', 'val': 'Cryosphere GIS', 'sub': 'IPCC Standard'}
            ],
            'code_snippet': """ax = plt.subplot(111, projection=ccrs.NorthPolarStereo())
ax.set_extent([-180, 180, 60, 90], ccrs.PlateCarree())
ax.contourf(lons, lats, ice_conc, transform=ccrs.PlateCarree())"""
        },

        # 9. GeoPandas Value-by-Alpha / Bivariate Cartographic Map
        {
            'slide_id': 'slide-09-geopandas-alpha',
            'tag': '09 / Value-by-Alpha Mapping',
            'headline': 'Bivariate Uncertainty Mapping:',
            'headline_span': 'GeoPandas Value-by-Alpha',
            'subtitle': 'Color hue encodes metric performance while alpha transparency reflects statistical sample confidence.',
            'library_badge': 'GeoPandas Cartography',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- High Sample Confidence (High Alpha) -->
                  <polygon points="50,40 150,30 170,110 60,120" fill="#00e676" opacity="0.95" stroke="#fff" stroke-width="1"/>
                  <text x="105" y="80" text-anchor="middle" fill="#070c09" font-family="DM Sans" font-size="10" font-weight="bold">High N (α=0.95)</text>
                  <!-- Low Sample Confidence (Low Alpha) -->
                  <polygon points="150,30 270,40 280,120 170,110" fill="#00e676" opacity="0.2" stroke="#fff" stroke-width="1" stroke-dasharray="3"/>
                  <text x="215" y="80" text-anchor="middle" fill="#fff" font-family="DM Sans" font-size="10">Low N (α=0.20)</text>
                  <polygon points="60,120 170,110 160,190 70,180" fill="#ff1744" opacity="0.9" stroke="#fff" stroke-width="1"/>
                  <polygon points="170,110 280,120 270,190 160,190" fill="#ff1744" opacity="0.25" stroke="#fff" stroke-width="1" stroke-dasharray="3"/>
                  <text x="175" y="225" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Color = Net RevPAR Delta &bull; Alpha = Sample Size</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Dual-channel encoding: $\\text{Color} = f(\\text{Metric})$, $\\alpha = g(\\text{Confidence})$, where $\\alpha \\propto \\sqrt{N}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Preventing executive over-reaction to small-sample regional anomalies, election polling maps.'},
                {'title': 'Technical Strengths', 'desc': 'Suppresses noisy rural regions with tiny sample sizes while emphasizing statistically robust metro hubs.'}
            ],
            'metrics': [
                {'label': 'Color Hue', 'val': 'Performance Yield', 'sub': 'Green / Red'},
                {'label': 'Alpha Channel', 'val': 'Sample Weight (N)', 'sub': 'Opacity Shading'},
                {'label': 'Cognitive', 'val': 'Suppresses Noise', 'sub': 'De-biasing'},
                {'label': 'Framework', 'val': 'GeoPandas Plot', 'sub': 'RGBA Mapping'}
            ],
            'code_snippet': """colors = [to_rgba(c, alpha=a) for c, a in zip(metric_colors, sample_weights)]
gdf.plot(color=colors, edgecolor='black', linewidth=0.5)"""
        },

        # 10. Pydeck ScreenGridLayer Dynamic Cell Density
        {
            'slide_id': 'slide-10-pydeck-screengrid',
            'tag': '10 / Screen-Space Clustering',
            'headline': 'Screen-Space Aggregations:',
            'headline_span': 'Pydeck ScreenGridLayer Density',
            'subtitle': 'Aggregates points into fixed-pixel screen-space grid cells dynamically on the GPU during panning.',
            'library_badge': 'Pydeck ScreenGridLayer',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Screen Grid Matrix -->
                  <g fill="#00e676" stroke="#070c09" stroke-width="1.5">
                    <rect x="70" y="50" width="30" height="30" fill="#070c09"/>
                    <rect x="105" y="50" width="30" height="30" fill="#1b382b"/>
                    <rect x="140" y="50" width="30" height="30" fill="#00e676" opacity="0.8"/>
                    <rect x="175" y="50" width="30" height="30" fill="#f3cf65"/>
                    <rect x="70" y="85" width="30" height="30" fill="#1b382b"/>
                    <rect x="105" y="85" width="30" height="30" fill="#00e676"/>
                    <rect x="140" y="85" width="30" height="30" fill="#fffefa"/>
                    <rect x="175" y="85" width="30" height="30" fill="#00e676"/>
                    <rect x="70" y="120" width="30" height="30" fill="#070c09"/>
                    <rect x="105" y="120" width="30" height="30" fill="#1b382b"/>
                    <rect x="140" y="120" width="30" height="30" fill="#00e676" opacity="0.6"/>
                    <rect x="175" y="120" width="30" height="30" fill="#1b382b"/>
                  </g>
                  <text x="175" y="195" text-anchor="middle" fill="#fffefa" font-family="JetBrains Mono" font-size="10">Pixel Cell Size: 30px &bull; GPU Binning</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Screen-space binning: points mapped into fixed $W \\times H$ pixel buckets directly in fragment shader.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Emergency 911 incident dispatch density, nationwide cellular handover drops, taxi hailing hotspots.'},
                {'title': 'Technical Strengths', 'desc': 'Cell size remains invariant to map zoom level, providing consistent screen legibility.'}
            ],
            'metrics': [
                {'label': 'Coordinate', 'val': 'Screen Pixels', 'sub': 'Viewport Fixed'},
                {'label': 'Aggregation', 'val': 'GPU Fragment', 'sub': 'Ultra Fast'},
                {'label': 'Zoom Stability', 'val': 'Constant Size', 'sub': 'No Flickering'},
                {'label': 'Capacity', 'val': '10M Points', 'sub': 'Zero Lag'}
            ],
            'code_snippet': """pdk.Layer(
    "ScreenGridLayer", data=df,
    get_position='[lon, lat]', cell_size_pixels=30,
    color_range=[[0, 230, 118], [243, 207, 101], [255, 23, 68]]
)"""
        },

        # 11. Folium MarkerCluster with Luxury HTML Popups
        {
            'slide_id': 'slide-11-folium-cluster',
            'tag': '11 / Dynamic Pin Clustering',
            'headline': 'Dynamic Spatial Clustering:',
            'headline_span': 'Folium MarkerCluster with HTML Popups',
            'subtitle': 'Hierarchical distance-based marker clustering expanding into custom luxury HTML card summaries upon click.',
            'library_badge': 'Folium MarkerCluster',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Cluster Circle Core -->
                  <circle cx="120" cy="110" r="32" fill="#1b2822" stroke="#d4af37" stroke-width="2.5" filter="drop-shadow(0 0 10px #d4af37)"/>
                  <text x="120" y="115" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="14" font-weight="bold">18</text>
                  <!-- Popup Card on Right -->
                  <rect x="180" y="60" width="150" height="95" fill="#101a16" stroke="#00e676" rx="6"/>
                  <text x="190" y="80" fill="#fffefa" font-family="DM Sans" font-size="11" font-weight="bold">Orchard Flagship</text>
                  <text x="190" y="96" fill="#00e676" font-family="JetBrains Mono" font-size="9">Direct RevPAR: $340</text>
                  <text x="190" y="110" fill="#d4af37" font-family="JetBrains Mono" font-size="9">Occupancy: 84.5%</text>
                  <text x="190" y="135" fill="#9ba9a1" font-family="DM Sans" font-size="8">Managed by OpCo Asia</text>
                  <!-- Connector Line -->
                  <line x1="152" y1="110" x2="180" y2="105" stroke="#00e676" stroke-width="1.5" stroke-dasharray="2"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'K-d tree hierarchical spatial clustering grouping coordinates whose pixel distance $< D_{\\text{thresh}}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel chain global property directories, real estate listings portals, store locator search engines.'},
                {'title': 'Technical Strengths', 'desc': 'Prevents visual marker collision when viewing thousands of properties at national zoom levels.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': 'Distance Clustering', 'sub': 'Pixel Radius'},
                {'label': 'Popup', 'val': 'Rich HTML5 Card', 'sub': 'Bootstrap/CSS'},
                {'label': 'Spiderfy', 'val': 'Overlapping Points', 'sub': 'Spiral Fanout'},
                {'label': 'Performance', 'val': '10,000 Pins', 'sub': 'Fast Cluster'}
            ],
            'code_snippet': """from folium.plugins import MarkerCluster
mc = MarkerCluster().add_to(m)
for _, row in df.iterrows():
    html = f"<b>{row.name}</b><br>RevPAR: ${row.revpar}"
    folium.Marker([row.lat, row.lon], popup=html).add_to(mc)"""
        },

        # 12. Cartopy Orthographic Satellite with Solar Terminator
        {
            'slide_id': 'slide-12-cartopy-ortho',
            'tag': '12 / Celestial Cartography',
            'headline': 'Day / Night Solar Boundary:',
            'headline_span': 'Cartopy Orthographic Terminator',
            'subtitle': 'True orthographic Earth view showing real-time solar declination and astronomical day/night shadow boundaries.',
            'library_badge': 'Cartopy Nightshade',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 280 280" style="width:250px; height:250px;">
                  <defs>
                    <clipPath id="earthClip">
                      <circle cx="140" cy="140" r="110"/>
                    </clipPath>
                  </defs>
                  <!-- Base Earth Circle -->
                  <circle cx="140" cy="140" r="110" fill="#0d281a" stroke="#d4af37" stroke-width="2"/>
                  <!-- Night Shade Half -->
                  <path d="M 140 30 Q 180 140, 140 250 A 110 110 0 0 1 140 30 Z" fill="#040806" opacity="0.85" clip-path="url(#earthClip)"/>
                  <!-- Sun Position -->
                  <circle cx="90" cy="120" r="6" fill="#f3cf65" filter="drop-shadow(0 0 10px #f3cf65)"/>
                  <text x="90" y="105" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">Solar Zenith</text>
                  <!-- Terminator Line -->
                  <path d="M 140 30 Q 180 140, 140 250" fill="none" stroke="#d4af37" stroke-width="1.5" stroke-dasharray="3"/>
                  <text x="140" y="265" text-anchor="middle" fill="#fffefa" font-family="DM Sans" font-size="10">Solar Terminator Night Boundary</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Astronomical ephemeris solar position calculation $(\\delta, \\alpha)$ projecting great-circle night shadow boundary.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Global 24/7 call center staffing handover, international market opening hours, satellite solar panel tracking.'},
                {'title': 'Technical Strengths', 'desc': 'Simulates authentic orbital view of Earth as seen from deep space with precise solar illumination.'}
            ],
            'metrics': [
                {'label': 'Projection', 'val': 'Orthographic', 'sub': 'Infinite Viewpoint'},
                {'label': 'Ephemeris', 'val': 'Solar Declination', 'sub': 'Astronomical'},
                {'label': 'Shadow', 'val': 'Nightshade Polygon', 'sub': 'Day/Night Split'},
                {'label': 'Precision', 'val': 'Sub-Minute', 'sub': 'UTC Synced'}
            ],
            'code_snippet': """from cartopy.feature.nightshade import Nightshade
ax = plt.subplot(111, projection=ccrs.Orthographic(central_longitude=100))
ax.add_feature(Nightshade(datetime.now(), alpha=0.5))"""
        },

        # 13. Geoplotlib Spatial Graph with Edge Aggregation
        {
            'slide_id': 'slide-13-geoplotlib-graph',
            'tag': '13 / Spatial Network Routing',
            'headline': 'Geographic Network Flows:',
            'headline_span': 'Geoplotlib Spatial Graph Aggregation',
            'subtitle': 'Fast OpenGL graph layer drawing weighted trade and communication routes between geographic nodes.',
            'library_badge': 'Geoplotlib Graph',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <g stroke="#00e676" stroke-linecap="round">
                    <line x1="80" y1="130" x2="175" y2="90" stroke-width="4"/>
                    <line x1="175" y1="90" x2="280" y2="110" stroke-width="3"/>
                    <line x1="80" y1="130" x2="200" y2="180" stroke-width="2" stroke-opacity="0.6"/>
                    <line x1="175" y1="90" x2="200" y2="180" stroke-width="2.5" stroke-opacity="0.7"/>
                  </g>
                  <circle cx="80" cy="130" r="10" fill="#00e676"/>
                  <circle cx="175" cy="90" r="14" fill="#f3cf65"/>
                  <circle cx="280" cy="110" r="9" fill="#00e5ff"/>
                  <circle cx="200" cy="180" r="8" fill="#d4af37"/>
                  <text x="175" y="70" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="10">Hub Node (Volume: $42M)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Spatial network $G = (V, E)$ where nodes possess fixed geographic $(x, y)$ coordinates and edge width $w \\propto \\text{Flow}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Inter-branch financial cash logistics, global cloud data replication routes, maritime freight flows.'},
                {'title': 'Technical Strengths', 'desc': 'Renders tens of thousands of geographic edges smoothly using compiled OpenGL vertex arrays.'}
            ],
            'metrics': [
                {'label': 'Network Type', 'val': 'Spatial Graph', 'sub': 'Fixed Coordinates'},
                {'label': 'Edge Weight', 'val': 'Width = Volume', 'sub': 'Proportional'},
                {'label': 'Render Backend', 'val': 'PyOpenSSL / GL', 'sub': 'Desktop Hardware'},
                {'label': 'Throughput', 'val': '50,000 Links', 'sub': 'Zero Lag'}
            ],
            'code_snippet': """import geoplotlib
geoplotlib.graph(network_data, src_lat='lat1', src_lon='lon1',
                 dest_lat='lat2', dest_lon='lon2', color=[0, 230, 118, 200])
geoplotlib.show()"""
        },

        # 14. GeoPandas Cartogram Transforming Area by GDP
        {
            'slide_id': 'slide-14-geopandas-cartogram',
            'tag': '14 / Non-Contiguous Cartograms',
            'headline': 'Value-Distorted Geographies:',
            'headline_span': 'GeoPandas Value-Distorted Cartogram',
            'subtitle': 'Rescales polygon surface areas strictly proportional to direct booking revenue rather than physical landmass.',
            'library_badge': 'GeoPandas Cartogram',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Distorted Region Squares -->
                  <rect x="50" y="40" width="110" height="110" fill="#00e676" stroke="#fff" stroke-width="1.5" rx="4"/>
                  <text x="105" y="95" text-anchor="middle" fill="#070c09" font-family="DM Sans" font-size="11" font-weight="bold">Singapore (Small Land)</text>
                  <text x="105" y="112" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="10">$48M Direct Rev</text>
                  
                  <rect x="180" y="60" width="130" height="70" fill="#d4af37" stroke="#fff" stroke-width="1.5" rx="4"/>
                  <text x="245" y="95" text-anchor="middle" fill="#070c09" font-family="DM Sans" font-size="11" font-weight="bold">London Annex</text>
                  <text x="245" y="112" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="10">$32M Direct Rev</text>

                  <rect x="110" y="165" width="60" height="45" fill="#6c7d73" stroke="#fff" stroke-width="1" rx="4"/>
                  <text x="140" y="192" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="8">Regional Asset</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Gastner-Newman diffusion-based cartogram algorithm: warping geographic coordinates so density $\\rho(x,y) = \\text{const}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Revenue-weighted territory balance, electoral vote representation, regional hotel EBITDA contribution.'},
                {'title': 'Technical Strengths', 'desc': 'Eliminates landmass bias where huge geographic territories with low population dominate visual charts.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': 'Gastner-Newman', 'sub': 'Diffusion Flow'},
                {'label': 'Area Meaning', 'val': 'Proportional to $', 'sub': 'Revenue-Scaled'},
                {'label': 'Bias Elimination', 'val': 'Landmass Neutral', 'sub': 'True Weight'},
                {'label': 'Topology', 'val': 'Preserved Contiguity', 'sub': 'Border Shared'}
            ],
            'code_snippet': """import geocartogram
cartogram_gdf = geocartogram.transform(gdf, value='direct_revenue')
cartogram_gdf.plot(color='#00e676', edgecolor='white')"""
        },

        # 15. Pydeck 3D TerrainLayer with Digital Elevation Model (DEM)
        {
            'slide_id': 'slide-15-pydeck-terrain',
            'tag': '15 / 3D DEM Raster Shaders',
            'headline': '3D Satellite Shading:',
            'headline_span': 'Pydeck TerrainLayer with DEM Tiles',
            'subtitle': 'GPU-accelerated heightmap elevation decoding rendering real-world mountain topography.',
            'library_badge': 'Pydeck TerrainLayer',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Mountain Peak Shaded Contours -->
                  <polygon points="175,30 280,180 70,180" fill="url(#peakGrad)" stroke="#d4af37" stroke-width="1.5"/>
                  <polygon points="175,30 240,180 175,180" fill="#00e676" opacity="0.3"/>
                  <polygon points="175,30 110,180 175,180" fill="#d4af37" opacity="0.4"/>
                  <!-- Base elevation wire -->
                  <line x1="40" y1="180" x2="310" y2="180" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
                  <text x="175" y="215" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="10">Alpine Resort &bull; 2,850m Summit DEM</text>
                  <defs>
                    <linearGradient id="peakGrad" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#fffefa"/>
                      <stop offset="40%" stop-color="#00e676"/>
                      <stop offset="100%" stop-color="#08100c"/>
                    </linearGradient>
                  </defs>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'RGB-encoded elevation decoding: $\\text{Elevation} = -10000 + (R \\cdot 256^2 + G \\cdot 256 + B) \\cdot 0.1$ evaluated in vertex shaders.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Ski resort slope planning, view-line shadow analysis for high-rise luxury penthouses, telecom line-of-sight.'},
                {'title': 'Technical Strengths', 'desc': 'Streams standard Mapbox/Terrarium elevation tiles with sub-second mesh reconstruction.'}
            ],
            'metrics': [
                {'label': 'Tile Protocol', 'val': 'Mapbox Terrain-RGB', 'sub': 'Normal Map'},
                {'label': 'Decoding', 'val': 'Hardware Shader', 'sub': 'GPU Vertex'},
                {'label': 'Lighting', 'val': 'Hillshade Normal', 'sub': 'Sun Angle'},
                {'label': 'Framerate', 'val': '60 FPS 3D', 'sub': 'Orbit / Pitch'}
            ],
            'code_snippet': """pdk.Layer(
    "TerrainLayer", elevation_decoder={"rScaler": 6553.6, "gScaler": 25.6, "bScaler": 0.1, "offset": -10000},
    elevation_data='https://.../terrain-rgb/{z}/{x}/{y}.png',
    texture='https://.../satellite/{z}/{x}/{y}.png'
)"""
        },

        # 16. Folium DualMap Synchronized Side-by-Side
        {
            'slide_id': 'slide-16-folium-dualmap',
            'tag': '16 / Synchronized Split Maps',
            'headline': 'Dual-Pane Cartographic Locks:',
            'headline_span': 'Folium DualMap Synchronized View',
            'subtitle': 'Twin coordinated map viewports locking pan, zoom, and pitch across comparative marketing datasets.',
            'library_badge': 'Folium DualMap Plugin',
            'chart_html': """
              <div style="width:100%; height:100%; display:grid; grid-template-columns:1fr 1fr; gap:8px; padding:15px; box-sizing:border-box;">
                <div style="background:#09120e; border:1px solid #00e676; border-radius:6px; padding:10px; display:flex; flex-direction:column; justify-content:space-between;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#00e676;">Layer A: Direct Bookings</span>
                  <div style="text-align:center; font-family:Newsreader; font-size:1.8rem; color:#00e676;">74% Net Share</div>
                  <span style="font-size:0.75rem; color:#9ba9a1;">Zero Intermediary Leak</span>
                </div>
                <div style="background:#09120e; border:1px solid #ff1744; border-radius:6px; padding:10px; display:flex; flex-direction:column; justify-content:space-between;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#ff1744;">Layer B: OTA Commissions</span>
                  <div style="text-align:center; font-family:Newsreader; font-size:1.8rem; color:#ff1744;">$920k Intermediary Toll</div>
                  <span style="font-size:0.75rem; color:#9ba9a1;">Masked Relay Emails</span>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Synchronized event listeners binding Map A center $(\\phi_A, \\lambda_A)$ and zoom $z_A$ directly to Map B.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Side-by-side competitor rate monitoring, demographic income vs direct booking propensity.'},
                {'title': 'Technical Strengths', 'desc': 'Pre-built Python plugin with zero complex JavaScript event synchronization required.'}
            ],
            'metrics': [
                {'label': 'Python Plugin', 'val': 'plugins.DualMap', 'sub': 'Folium Extended'},
                {'label': 'Sync Lock', 'val': 'Pan + Zoom', 'sub': 'Zero Lag'},
                {'label': 'Layers', 'val': 'Independent Tiles', 'sub': 'Dual Datasets'},
                {'label': 'Export', 'val': 'Self-Contained HTML', 'sub': 'Single File'}
            ],
            'code_snippet': """from folium.plugins import DualMap
m = DualMap(location=[1.35, 103.82], zoom_start=12)
folium.TileLayer('cartodbpositron').add_to(m.m1)
folium.TileLayer('cartodbdark_matter').add_to(m.m2)"""
        },

        # 17. Cartopy Interrupted Goode Homolosine Equal-Area Projection
        {
            'slide_id': 'slide-17-cartopy-homolosine',
            'tag': '17 / Equal-Area Interruption',
            'headline': 'Zero Land Distortion:',
            'headline_span': 'Goode Homolosine Interrupted World',
            'subtitle': 'Composite equal-area pseudocylindrical projection slicing ocean basins to present continents with true relative sizes.',
            'library_badge': 'Cartopy GoodeHomolosine',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 380 220" style="width:100%; max-height:240px;">
                  <!-- Interrupted lobes schematic -->
                  <g fill="#13221b" stroke="#d4af37" stroke-width="1.5">
                    <!-- Americas Lobe -->
                    <path d="M 50 180 Q 90 40, 130 180 Z"/>
                    <!-- Europe/Africa Lobe -->
                    <path d="M 140 180 Q 180 30, 220 180 Z"/>
                    <!-- Asia/Australia Lobe -->
                    <path d="M 230 180 Q 290 30, 350 180 Z"/>
                  </g>
                  <text x="190" y="210" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Goode Homolosine: Strictly Equal-Area Worldwide</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Piecewise combination: Sinusoidal projection between latitudes $0^\\circ - 44^\\circ$ and Mollweide projection above $44^\\circ$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Accurately representing true global market shares without inflating Greenland and Antarctica.'},
                {'title': 'Technical Strengths', 'desc': 'Preserves true areal proportions across all continents simultaneously without shape squashing.'}
            ],
            'metrics': [
                {'label': 'Projection Type', 'val': 'Equal-Area (Homolographic)', 'sub': 'True Land Area'},
                {'label': 'Interruption', 'val': 'Multi-Lobed Oceans', 'sub': 'Min Distort'},
                {'label': 'Standard', 'val': 'USGS / Academic', 'sub': 'True Area Std'},
                {'label': 'Implementation', 'val': 'Cartopy PROJ', 'sub': 'SciTools'}
            ],
            'code_snippet': """import cartopy.crs as ccrs
ax = plt.subplot(111, projection=ccrs.InterruptedGoodeHomolosine())
ax.coastlines(color='#00e676')"""
        },

        # 18. GeoPandas Spatially Weighted Centroid Dispersion Ellipses
        {
            'slide_id': 'slide-18-geopandas-ellipses',
            'tag': '18 / Spatial Statistics',
            'headline': 'Directional Spatial Drift:',
            'headline_span': 'Standard Deviational Ellipse (SDE)',
            'subtitle': 'Calculates the central geographic mean, spatial dispersion dispersion, and directional trend of guest origins.',
            'library_badge': 'PySAL / GeoPandas',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Standard Deviational Ellipse rotated 35 degrees -->
                  <g transform="translate(175, 120) rotate(35)">
                    <ellipse cx="0" cy="0" rx="95" ry="45" fill="rgba(0,230,118,0.2)" stroke="#00e676" stroke-width="2"/>
                    <!-- Major Axis -->
                    <line x1="-95" y1="0" x2="95" y2="0" stroke="#f3cf65" stroke-width="1.5" stroke-dasharray="3"/>
                    <!-- Minor Axis -->
                    <line x1="0" y1="-45" x2="0" y2="45" stroke="#f3cf65" stroke-width="1.5" stroke-dasharray="3"/>
                    <!-- Mean Center -->
                    <circle cx="0" cy="0" r="5" fill="#fff"/>
                  </g>
                  <text x="175" y="220" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="10">Directional Trend: Northeast Corridor (θ=35°)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Standard deviational ellipse principal axis calculation from spatial covariance matrix: $\\tan 2\\theta = \\frac{2\\sum \\tilde{x}_i \\tilde{y}_i}{\\sum \\tilde{x}_i^2 - \\sum \\tilde{y}_i^2}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Evaluating geographic directional drift in hotel guest source markets over multi-year cycles.'},
                {'title': 'Technical Strengths', 'desc': 'Summarizes thousands of scattered customer GPS points into a concise, rigorous 1-sigma ellipse.'}
            ],
            'metrics': [
                {'label': 'Statistics', 'val': '1-Sigma SDE', 'sub': '68% Coordinates'},
                {'label': 'Direction', 'val': 'Eigenvector Angle', 'sub': 'Major Axis θ'},
                {'label': 'Dispersion', 'val': 'Standard Deviation', 'sub': 'σx and σy'},
                {'label': 'Library', 'val': 'PySAL / Pointpats', 'sub': 'Spatial Stats'}
            ],
            'code_snippet': """from pointpats import PointPattern
pp = PointPattern(coords)
sde_center, major_len, minor_len, angle = pp.sde"""
        },

        # 19. Pydeck PointCloudLayer 3D Urban Forest Canopy
        {
            'slide_id': 'slide-19-pydeck-pointcloud',
            'tag': '19 / GPU LiDAR Point Clouds',
            'headline': 'GPU Urban Canopy Scans:',
            'headline_span': 'Pydeck PointCloudLayer Slices',
            'subtitle': 'Direct GPU vertex rendering of millions of urban 3D laser coordinates with height-based RGB coloring.',
            'library_badge': 'Pydeck PointCloudLayer',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <g fill="#00e676" opacity="0.8">
                    <circle cx="90" cy="180" r="3"/> <circle cx="120" cy="170" r="3"/> <circle cx="150" cy="165" r="3"/>
                    <circle cx="100" cy="150" r="3"/> <circle cx="140" cy="140" r="3"/> <circle cx="180" cy="130" r="3"/>
                  </g>
                  <g fill="#d4af37" opacity="0.9">
                    <circle cx="160" cy="90" r="4"/> <circle cx="170" cy="75" r="4.5"/> <circle cx="185" cy="80" r="5"/>
                  </g>
                  <text x="175" y="225" text-anchor="middle" fill="#fffefa" font-family="JetBrains Mono" font-size="10">Pydeck PointCloudLayer &bull; Sub-Centimeter WebGL</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'GPU instanced point primitives rendered via Deck.gl PointCloudLayer with custom point size and lighting attenuation.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Architectural façade laser scans, urban tree canopy biomass calculation, heritage asset digital twins.'},
                {'title': 'Technical Strengths', 'desc': 'Streams binary LAS/LAZ files directly into browser WebGL buffers through Python.'}
            ],
            'metrics': [
                {'label': 'Primitive', 'val': 'gl.POINTS WebGL', 'sub': 'Hardware Point'},
                {'label': 'LAS Support', 'val': 'Direct Stream', 'sub': 'Binary LAS/LAZ'},
                {'label': 'Attenuation', 'val': 'Perspective Sizing', 'sub': 'Distance Scaling'},
                {'label': 'Language', 'val': 'Python + Deck.gl', 'sub': 'Modern GPU'}
            ],
            'code_snippet': """pdk.Layer(
    "PointCloudLayer", data=point_df,
    get_position='[x, y, z]', get_color='[r, g, b]',
    point_size=3
)"""
        },

        # 20. Folium Real-Time GeoJSON Vector Tile Pipeline
        {
            'slide_id': 'slide-20-folium-vt',
            'tag': '20 / Real-Time Vector Pipelines',
            'headline': 'Production Vector Pipelines:',
            'headline_span': 'Folium Dynamic GeoJSON Vector Pipeline',
            'subtitle': 'End-to-end Python pipeline streaming live hotel rate parity and availability GeoJSON polygons.',
            'library_badge': 'Folium GeoJSON Pipeline',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:15px; box-sizing:border-box;">
                <table class="viz-table">
                  <thead>
                    <tr>
                      <th>Property Asset</th>
                      <th>Country</th>
                      <th>Direct Share</th>
                      <th>Rate Parity Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td style="color:#00e676; font-weight:bold;">Singapore Urban Luxury</td>
                      <td>Singapore (SIN)</td>
                      <td style="font-family:JetBrains Mono;">64%</td>
                      <td><span style="color:#00e676; font-weight:bold;">100% PARITY LOCK</span></td>
                    </tr>
                    <tr>
                      <td style="color:#f3cf65; font-weight:bold;">London Heritage Flagship</td>
                      <td>United Kingdom (UK)</td>
                      <td style="font-family:JetBrains Mono;">52%</td>
                      <td><span style="color:#00e676; font-weight:bold;">100% PARITY LOCK</span></td>
                    </tr>
                    <tr>
                      <td style="color:#ffab00; font-weight:bold;">Tokyo Ginza Suites</td>
                      <td>Japan (JP)</td>
                      <td style="font-family:JetBrains Mono;">48%</td>
                      <td><span style="color:#ffab00; font-weight:bold;">MINOR OTA LEAK (-4%)</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Event-driven spatial dictionary ingestion: feature collections serialized into compact GeoJSON buffers.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Automated daily commercial executive dashboard distribution, real-time rate leakage mapping.'},
                {'title': 'Technical Strengths', 'desc': 'Requires zero external map server infrastructure; generates self-contained interactive files.'}
            ],
            'metrics': [
                {'label': 'Data Format', 'val': 'GeoJSON Feature', 'sub': 'W3C Standard'},
                {'label': 'Automation', 'val': 'Nightly Cron', 'sub': 'Python Script'},
                {'label': 'Security', 'val': 'Self-Contained', 'sub': 'No Leaked APIs'},
                {'label': 'Client Engine', 'val': 'Leaflet v1.9', 'sub': 'Fastest Mobile'}
            ],
            'code_snippet': """folium.GeoJson(
    geojson_data, style_function=lambda x: {
        'fillColor': '#00e676' if x['properties']['parity'] else '#ff1744',
        'color': '#ffffff', 'weight': 1.5, 'fillOpacity': 0.7
    }
).add_to(m)"""
        }
    ]

    html = generate_deck_html(deck_meta, slides)
    out_path = os.path.join(SCRIPT_DIR, "07-python-geospatial-mapping.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Built {out_path} (20 slides, {len(html)} bytes)")

if __name__ == "__main__":
    build_deck()
