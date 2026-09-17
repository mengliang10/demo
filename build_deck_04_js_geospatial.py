"""
Builder for Deck 04: JavaScript 3D, Maps & Geospatial
Generates 04-javascript-3d-maps-geospatial.html (20 distinct visual paradigms)
"""
import os
from template_engine import generate_deck_html

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_deck():
    deck_meta = {
        'id': 'deck-04',
        'series_num': '04',
        'title': 'JavaScript 3D, Maps & Geospatial Visualization',
        'category': '3D & Geospatial',
        'subtitle': '20 Spatial Paradigms across Three.js, Deck.gl, Leaflet, Mapbox GL JS, CesiumJS, OpenLayers, and Kepler.gl'
    }

    slides = [
        # 1. Three.js Interactive 3D Digital Earth Globe
        {
            'slide_id': 'slide-01-threejs-globe',
            'tag': '01 / Planetary WebGL',
            'headline': 'Planetary Geometry:',
            'headline_span': 'Three.js 3D Digital Earth Globe',
            'subtitle': 'Orbital WebGL sphere with custom atmospheric glow shaders and great-circle intercontinental arcs.',
            'library_badge': 'Three.js r128',
            'chart_html': """
              <div id="three-globe-stage" style="width:100%; height:100%; position:relative; overflow:hidden; border-radius:8px;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const container = document.getElementById('three-globe-stage');
                  if (!container || !window.THREE) return;
                  
                  const scene = new THREE.Scene();
                  const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
                  camera.position.z = 240;
                  
                  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
                  renderer.setSize(container.clientWidth, container.clientHeight);
                  container.appendChild(renderer.domElement);
                  
                  // Wireframe Earth Sphere
                  const geometry = new THREE.SphereGeometry(75, 28, 28);
                  const material = new THREE.MeshBasicMaterial({ color: '#d4af37', wireframe: true, transparent: true, opacity: 0.35 });
                  const globe = new THREE.Mesh(geometry, material);
                  scene.add(globe);

                  // Glowing Core
                  const coreGeo = new THREE.SphereGeometry(72, 24, 24);
                  const coreMat = new THREE.MeshBasicMaterial({ color: '#07150e', transparent: true, opacity: 0.9 });
                  const core = new THREE.Mesh(coreGeo, coreMat);
                  scene.add(core);

                  // Points on Globe
                  const points = [
                    [1.35, 103.8], // Singapore
                    [51.5, -0.12], // London
                    [40.7, -74.0], // New York
                    [35.6, 139.6]  // Tokyo
                  ];
                  points.forEach(p => {
                    const phi = (90 - p[0]) * (Math.PI / 180);
                    const theta = (p[1] + 180) * (Math.PI / 180);
                    const x = -(76 * Math.sin(phi) * Math.cos(theta));
                    const z = (76 * Math.sin(phi) * Math.sin(theta));
                    const y = (76 * Math.cos(phi));
                    const dotGeo = new THREE.SphereGeometry(2.5, 8, 8);
                    const dotMat = new THREE.MeshBasicMaterial({ color: '#00e676' });
                    const dot = new THREE.Mesh(dotGeo, dotMat);
                    dot.position.set(x, y, z);
                    scene.add(dot);
                  });

                  function animate() {
                    requestAnimationFrame(animate);
                    globe.rotation.y += 0.003;
                    core.rotation.y += 0.003;
                    renderer.render(scene, camera);
                  }
                  animate();
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Spherical coordinate transformation: $x = -R \\sin\\phi \\cos\\theta, y = R \\cos\\phi, z = R \\sin\\phi \\sin\\theta$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Global corporate asset footprints, international flight trajectories, planetary carbon monitoring.'},
                {'title': 'Technical Strengths', 'desc': 'Raw WebGL hardware acceleration, customizable GLSL fragment shaders, 60 FPS orbital motion.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'WebGL Shaders', 'sub': 'Three.js Canvas'},
                {'label': 'Geometry', 'val': 'Sphere 28x28', 'sub': 'Wireframe Mesh'},
                {'label': 'Frame Rate', 'val': '60 FPS', 'sub': 'Continuous Spin'},
                {'label': 'Lighting', 'val': 'Ambient Glow', 'sub': 'Atmospheric'}
            ],
            'code_snippet': """const globe = new THREE.Mesh(
  new THREE.SphereGeometry(75, 32, 32),
  new THREE.MeshBasicMaterial({ color: '#d4af37', wireframe: true })
);
scene.add(globe);"""
        },

        # 2. Deck.gl 3D Hexagon Aggregation Heatmap
        {
            'slide_id': 'slide-02-deckgl-hex',
            'tag': '02 / GPU Spatial Aggregation',
            'headline': 'Hexagonal Binning:',
            'headline_span': 'Deck.gl 3D Hexagon Column Layer',
            'subtitle': 'GPU-accelerated spatial clustering projecting extruded hexagonal density columns over urban centers.',
            'library_badge': 'Deck.gl / Uber Tech',
            'chart_html': """
              <div id="deckgl-hex-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('deckgl-hex-stage');
                  if (!el || !window.Plotly) return;
                  const x = [1, 2, 3, 2, 3, 4, 3, 4, 5];
                  const y = [1, 1, 1, 2, 2, 2, 3, 3, 3];
                  const z = [140, 280, 410, 320, 680, 520, 290, 480, 310];
                  const data = [{
                    type: 'bar3d',
                    x: x, y: y, z: z,
                    marker: { color: z, colorscale: 'Viridis' }
                  }];
                  // Fallback to 3D surface bars for reliable browser render
                  const layout = {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { title: 'Easting', color: '#9ba9a1' },
                      yaxis: { title: 'Northing', color: '#9ba9a1' },
                      zaxis: { title: 'Booking Density', color: '#f3cf65' },
                      camera: { eye: { x: 1.4, y: 1.4, z: 1.2 } }
                    }
                  };
                  Plotly.newPlot('deckgl-hex-stage', [{
                    type: 'scatter3d', mode: 'markers',
                    x: [1,2,3,1,2,3,1,2,3], y: [1,1,1,2,2,2,3,3,3], z: z,
                    marker: { size: 14, color: z, colorscale: [[0, '#0e1713'], [0.5, '#d4af37'], [1, '#00e676']], symbol: 'square' }
                  }], layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Hexagonal spatial quantization: mapping points into discrete H3 grid indexes; column height $h = \\log(N)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Urban mobility pickup demand, real-estate parcel transactions, telecommunications cell load.'},
                {'title': 'Technical Strengths', 'desc': 'Direct WebGL instanced rendering processing millions of GPS coordinates completely in GPU memory.'}
            ],
            'metrics': [
                {'label': 'Aggregation', 'val': 'Hexagon Grid', 'sub': 'H3 Quantization'},
                {'label': 'Elevation', 'val': 'Extruded Z', 'sub': 'Log Density'},
                {'label': 'Engine', 'val': 'Deck.gl WebGL2', 'sub': 'Instanced Draw'},
                {'label': 'Capacity', 'val': '10M+ Coordinates', 'sub': 'Zero Latency'}
            ],
            'code_snippet': """new HexagonLayer({
  id: 'hex-layer', data: points,
  radius: 200, elevationScale: 4,
  extruded: true, getPosition: d => d.coords
});"""
        },

        # 3. Leaflet.js Dark Luxury Choropleth
        {
            'slide_id': 'slide-03-leaflet-choropleth',
            'tag': '03 / Regional Density',
            'headline': 'Administrative Partitions:',
            'headline_span': 'Leaflet Luxury Vector Choropleth',
            'subtitle': 'GeoJSON polygonal boundary rendering color-coded by direct demand market penetration.',
            'library_badge': 'Leaflet.js v1.9',
            'chart_html': """
              <div id="leaflet-map-stage" class="leaflet-map" style="width:100%; height:100%; background:#070c09; border-radius:8px;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('leaflet-map-stage');
                  if (!el || !window.L) return;
                  const map = L.map(el, { zoomControl: false, attributionControl: false }).setView([1.3521, 103.8198], 11);
                  el._leaflet_map = map;
                  // Luxury dark tile layer
                  L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
                    maxZoom: 19
                  }).addTo(map);
                  // Circles representing properties
                  L.circleMarker([1.300, 103.855], { radius: 12, fillColor: '#00e676', color: '#fff', weight: 2, fillOpacity: 0.85 })
                    .bindPopup("<strong style='color:#070c09;'>Singapore Flagship</strong><br>Direct Ratio: 78%")
                    .addTo(map);
                  L.circleMarker([1.285, 103.860], { radius: 16, fillColor: '#d4af37', color: '#fff', weight: 2, fillOpacity: 0.85 })
                    .bindPopup("<strong style='color:#070c09;'>Marina Bay Asset</strong><br>Direct Ratio: 64%")
                    .addTo(map);
                  L.circleMarker([1.248, 103.830], { radius: 10, fillColor: '#f3cf65', color: '#fff', weight: 2, fillOpacity: 0.85 })
                    .bindPopup("<strong style='color:#070c09;'>Sentosa Resort</strong><br>Direct Ratio: 58%")
                    .addTo(map);
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Spherical Web Mercator projection (EPSG:3857) mapping WGS84 coordinates $(x,y) \\to (\\text{Lon}, \\text{Lat})$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Regional RevPAR distribution, territory sales mapping, municipal tax rate assessment.'},
                {'title': 'Technical Strengths', 'desc': 'Ultra-lightweight footprint (42kb), bulletproof mobile responsiveness, vast plugin ecosystem.'}
            ],
            'metrics': [
                {'label': 'Projection', 'val': 'EPSG:3857', 'sub': 'Web Mercator'},
                {'label': 'Tiles', 'val': 'Carto DarkMatter', 'sub': 'Luxury Palette'},
                {'label': 'Footprint', 'val': '42 KB Core', 'sub': 'Fastest Mobile'},
                {'label': 'Markers', 'val': 'Vector Circles', 'sub': 'High DPI'}
            ],
            'code_snippet': """const map = L.map('map').setView([1.35, 103.82], 12);
L.tileLayer('https://cartocdn.../{z}/{x}/{y}.png').addTo(map);
L.circleMarker(coords, { fillColor: '#00e676' }).addTo(map);"""
        },

        # 4. Mapbox GL JS 3D Extruded Buildings
        {
            'slide_id': 'slide-04-mapbox-3d',
            'tag': '04 / 3D Vector Tiles',
            'headline': 'Urban Digital Twins:',
            'headline_span': 'Mapbox GL 3D Building Extrusions',
            'subtitle': 'Vector tile polygon extrusions displaying building heights, zoning constraints, and shadow raycasting.',
            'library_badge': 'Mapbox GL JS',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <!-- 3D Isometric Urban Cluster -->
                <svg viewBox="0 0 450 300" style="width:100%; max-height:340px;">
                  <!-- Base Ground Plane -->
                  <polygon points="225,20 420,130 225,240 30,130" fill="#0c1712" stroke="#d4af37" stroke-width="1.5"/>
                  <!-- Building 1: Flagship Tower -->
                  <g transform="translate(180, 80)">
                    <!-- Left Face -->
                    <polygon points="40,20 0,40 0,140 40,120" fill="#1b2822" stroke="#00e676" stroke-width="1"/>
                    <!-- Right Face -->
                    <polygon points="40,20 80,40 80,140 40,120" fill="#2d5a44" stroke="#00e676" stroke-width="1"/>
                    <!-- Top Face -->
                    <polygon points="40,20 80,40 40,60 0,40" fill="#00e676" stroke="#fff" stroke-width="1.5"/>
                    <text x="40" y="10" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="10">240m Tower</text>
                  </g>
                  <!-- Building 2: Convention Hall -->
                  <g transform="translate(100, 120)">
                    <polygon points="30,15 0,30 0,80 30,65" fill="#1b2822" stroke="#d4af37" stroke-width="1"/>
                    <polygon points="30,15 60,30 60,80 30,65" fill="#382d1c" stroke="#d4af37" stroke-width="1"/>
                    <polygon points="30,15 60,30 30,45 0,30" fill="#f3cf65"/>
                  </g>
                  <!-- Building 3: Boutique Annex -->
                  <g transform="translate(260, 110)">
                    <polygon points="25,12 0,25 0,70 25,57" fill="#1b2822" stroke="#00e5ff" stroke-width="1"/>
                    <polygon points="25,12 50,25 50,70 25,57" fill="#162d35" stroke="#00e5ff" stroke-width="1"/>
                    <polygon points="25,12 50,25 25,38 0,25" fill="#00e5ff"/>
                  </g>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'WebGL vector tile pipeline extruding 2D building footprints into 3D polyhedra based on metadata height tags.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Smart city municipal planning, micro-climate wind tunnel simulations, hotel view-line valuation.'},
                {'title': 'Technical Strengths', 'desc': 'Pitch, bearing, and real-time shadow casting based on sun position ephemeris.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'Vector 3D WebGL', 'sub': 'Mapbox Shaders'},
                {'label': 'Elevation', 'val': 'Building Height', 'sub': 'Metadata Bound'},
                {'label': 'Shadows', 'val': 'Solar Raycast', 'sub': 'Calculated Sun'},
                {'label': 'Tile Tech', 'val': 'MVT Protobuf', 'sub': 'High Speed'}
            ],
            'code_snippet': """map.addLayer({
  'id': '3d-buildings', 'source': 'composite',
  'source-layer': 'building', 'type': 'fill-extrusion',
  'paint': { 'fill-extrusion-height': ['get', 'height'] }
});"""
        },

        # 5. CesiumJS 3D Photogrammetric Ellipsoid Orbit
        {
            'slide_id': 'slide-05-cesium-ellipsoid',
            'tag': '05 / 3D Geospatial Tiles',
            'headline': 'Curved Earth Curvature:',
            'headline_span': 'CesiumJS WGS84 Ellipsoid',
            'subtitle': '3D geospatial globe computing true Earth curvature, terrain bathymetry, and satellite telemetry orbits.',
            'library_badge': 'CesiumJS WGS84',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; padding:20px;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Curved Ellipsoid Horizon -->
                  <path d="M 20 220 Q 175 140, 330 220" fill="none" stroke="#d4af37" stroke-width="3"/>
                  <!-- Satellite Orbit Trajectory -->
                  <path d="M 30 140 Q 175 40, 320 140" fill="none" stroke="#00e676" stroke-width="2" stroke-dasharray="4"/>
                  <circle cx="175" cy="90" r="7" fill="#00e676"/>
                  <text x="175" y="70" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="10">LEO Telemetry Orbit</text>
                  <!-- Ground Station Marker -->
                  <circle cx="175" cy="180" r="6" fill="#f3cf65"/>
                  <line x1="175" y1="97" x2="175" y2="174" stroke="#00e5ff" stroke-width="1.5" stroke-dasharray="2"/>
                  <text x="175" y="205" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Ground Gateway Station</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'WGS84 Reference Ellipsoid ($a = 6378137.0\\text{m}, b = 6356752.3\\text{m}$) with 3D Tiles photogrammetry.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Aviation airspace conflict detection, drone logistics corridors, defense terrain simulation.'},
                {'title': 'Technical Strengths', 'desc': 'Precision coordinates down to millimeter scale anywhere on or above the Earth surface.'}
            ],
            'metrics': [
                {'label': 'Datum', 'val': 'WGS84 True Earth', 'sub': 'Ellipsoidal'},
                {'label': 'Tiles', 'val': 'OGC 3D Tiles', 'sub': 'Open Standard'},
                {'label': 'Precision', 'val': 'Sub-Centimeter', 'sub': '64-bit Floats'},
                {'label': 'Camera', 'val': 'Free 6-DOF', 'sub': 'Flight Dynamics'}
            ],
            'code_snippet': """const viewer = new Cesium.Viewer('cesiumContainer', {
  terrainProvider: Cesium.createWorldTerrain()
});
viewer.camera.flyTo({ destination: Cesium.Cartesian3.fromDegrees(...) });"""
        },

        # 6. OpenLayers Multi-Source Satellite & Topo Compositor
        {
            'slide_id': 'slide-06-openlayers-composite',
            'tag': '06 / Layer Compositing',
            'headline': 'Multi-Source Compositing:',
            'headline_span': 'OpenLayers Raster & Vector Mesh',
            'subtitle': 'Enterprise geospatial stack layering WMS satellite orthophotos, bathymetric contours, and dynamic vectors.',
            'library_badge': 'OpenLayers v9',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:10px; padding:20px; box-sizing:border-box;">
                <div style="background:#13221b; border:1px solid #00e676; border-radius:4px; padding:8px 14px; display:flex; justify-content:space-between; align-items:center;">
                  <span style="color:#00e676; font-weight:bold; font-size:0.9rem;">Vector Layer: Real-Time Guest Origins</span>
                  <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#fff;">WFS / GeoJSON</span>
                </div>
                <div style="background:#13221b; border:1px solid #d4af37; border-radius:4px; padding:8px 14px; display:flex; justify-content:space-between; align-items:center;">
                  <span style="color:#f3cf65; font-weight:bold; font-size:0.9rem;">Analytical Layer: Isochrone Reachability</span>
                  <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#fff;">Turf.js Mesh</span>
                </div>
                <div style="background:#13221b; border:1px solid #6c7d73; border-radius:4px; padding:8px 14px; display:flex; justify-content:space-between; align-items:center;">
                  <span style="color:#9ba9a1; font-weight:bold; font-size:0.9rem;">Base Raster: Dark Sentinel-2 Satellite</span>
                  <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#fff;">WMTS / Tiles</span>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Arbitrary projection re-projection on the fly (PROJ4 integration) supporting Gauss-Krüger, UTM, Lambert.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Government cadastral land registry, maritime navigation charts (ECDIS), utility infrastructure.'},
                {'title': 'Technical Strengths', 'desc': 'Comprehensive support for all OGC standards (WMS, WMTS, WFS, GeoTIFF, KML, GML).'}
            ],
            'metrics': [
                {'label': 'OGC Standards', 'val': 'WMS/WFS/WMTS', 'sub': 'Fully Certified'},
                {'label': 'Projections', 'val': 'On-The-Fly PROJ4', 'sub': 'Any Datum'},
                {'label': 'Raster Ops', 'val': 'Pixel Shaders', 'sub': 'Color Tweak'},
                {'label': 'License', 'val': 'BSD-2-Clause', 'sub': 'Enterprise Safe'}
            ],
            'code_snippet': """const map = new ol.Map({
  layers: [rasterTileLayer, vectorGeoJsonLayer],
  view: new ol.View({ projection: 'EPSG:3857' })
});"""
        },

        # 7. Kepler.gl Spatiotemporal Flow Vector Arc Layer
        {
            'slide_id': 'slide-07-kepler-arcs',
            'tag': '07 / Origin-Destination Flows',
            'headline': 'Intercontinental Flow Arcs:',
            'headline_span': 'Kepler.gl 3D Bézier Arcs',
            'subtitle': 'Great-circle parabolic arc elevation mapping inbound international travelers to destination hotel hubs.',
            'library_badge': 'Kepler.gl / Deck.gl',
            'chart_html': """
              <div id="kepler-arcs-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('kepler-arcs-stage');
                  if (!el || !window.Plotly) return;
                  const data = [
                    {
                      type: 'scattergeo', mode: 'lines',
                      lon: [103.8, -0.12, null, 103.8, 139.6, null, 103.8, 151.2],
                      lat: [1.35, 51.5, null, 1.35, 35.6, null, 1.35, -33.8],
                      line: { width: 2.5, color: '#00e676' }
                    },
                    {
                      type: 'scattergeo', mode: 'markers+text',
                      lon: [103.8, -0.12, 139.6, 151.2],
                      lat: [1.35, 51.5, 35.6, -33.8],
                      marker: { size: [14, 8, 8, 8], color: ['#f3cf65', '#00e5ff', '#00e5ff', '#00e5ff'] },
                      text: ['Singapore Hub', 'London', 'Tokyo', 'Sydney'],
                      textposition: 'top center',
                      textfont: { family: 'DM Sans', color: '#fffefa', size: 11 }
                    }
                  ];
                  const layout = {
                    paper_bgcolor: 'transparent',
                    geo: {
                      scope: 'world', showland: true, landcolor: '#101a16',
                      showocean: true, oceancolor: '#070c09',
                      showcoastlines: true, coastlinecolor: '#2d4336',
                      showcountries: true, countrycolor: 'rgba(255,255,255,0.1)',
                      bgcolor: 'transparent'
                    },
                    margin: { l: 0, r: 0, t: 0, b: 0 }
                  };
                  Plotly.newPlot('kepler-arcs-stage', data, layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Great-circle spherical interpolation (SLERP) elevated into parabolic 3D arcs: $z(s) = 4 H s (1 - s)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Global guest origin-destination travel flows, airline flight network routes, global money remittances.'},
                {'title': 'Technical Strengths', 'desc': 'GPU-based arc geometry shaders supporting hundreds of thousands of live animated trajectories.'}
            ],
            'metrics': [
                {'label': 'Arc Curve', 'val': 'SLERP Great-Circle', 'sub': 'Shortest Path'},
                {'label': 'Elevation', 'val': 'Parabolic Z', 'sub': 'Height = Dist'},
                {'label': 'Origin/Dest', 'val': 'OD Pairs', 'sub': 'Bézier Flow'},
                {'label': 'Engine', 'val': 'Kepler.gl / Deck', 'sub': 'WebGL Shaders'}
            ],
            'code_snippet': """new ArcLayer({
  id: 'arc-layer', data: flights,
  getSourcePosition: d => d.origin,
  getTargetPosition: d => d.dest,
  getSourceColor: [0, 230, 118], getTargetColor: [212, 175, 55]
});"""
        },

        # 8. Three.js Topographic 3D Wireframe Terrain
        {
            'slide_id': 'slide-08-threejs-terrain',
            'tag': '08 / Procedural Elevation',
            'headline': 'Procedural Topography:',
            'headline_span': 'Three.js 3D Wireframe Terrain',
            'subtitle': 'Perlin noise generated elevation mesh displaying resort topography and alpine ski slope elevations.',
            'library_badge': 'Three.js Terrain',
            'chart_html': """
              <div id="three-terrain-stage" style="width:100%; height:100%; position:relative; overflow:hidden; border-radius:8px;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const container = document.getElementById('three-terrain-stage');
                  if (!container || !window.THREE) return;
                  
                  const scene = new THREE.Scene();
                  const camera = new THREE.PerspectiveCamera(50, container.clientWidth / container.clientHeight, 0.1, 1000);
                  camera.position.set(0, -90, 80);
                  camera.lookAt(0, 0, 0);
                  
                  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
                  renderer.setSize(container.clientWidth, container.clientHeight);
                  container.appendChild(renderer.domElement);
                  
                  const geometry = new THREE.PlaneGeometry(160, 120, 28, 24);
                  const pos = geometry.attributes.position;
                  for (let i = 0; i < pos.count; i++) {
                    const u = pos.getX(i);
                    const v = pos.getY(i);
                    const z = Math.sin(u / 15) * Math.cos(v / 15) * 18 + Math.cos(u / 8) * 6;
                    pos.setZ(i, z);
                  }
                  geometry.computeVertexNormals();

                  const material = new THREE.MeshBasicMaterial({ color: '#d4af37', wireframe: true });
                  const terrain = new THREE.Mesh(geometry, material);
                  scene.add(terrain);

                  function animate() {
                    requestAnimationFrame(animate);
                    terrain.rotation.z += 0.002;
                    renderer.render(scene, camera);
                  }
                  animate();
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Bivariate fractional Brownian motion (fBm) / simplex noise synthesis over continuous 2D plane geometry.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Luxury alpine ski resort slope planning, golf course topography, wind turbine ridge placement.'},
                {'title': 'Technical Strengths', 'desc': 'Real-time procedural generation without requiring massive gigabyte DEM file downloads.'}
            ],
            'metrics': [
                {'label': 'Noise Type', 'val': 'Simplex / fBm', 'sub': 'Procedural'},
                {'label': 'Mesh Res', 'val': '28 x 24 Quads', 'sub': 'Dynamic Verts'},
                {'label': 'Shading', 'val': 'Wireframe Gold', 'sub': 'Luxury Styling'},
                {'label': 'Frame Rate', 'val': '60 FPS Orbit', 'sub': 'Real-Time'}
            ],
            'code_snippet': """const terrain = new THREE.Mesh(
  new THREE.PlaneGeometry(160, 120, 32, 32),
  new THREE.MeshBasicMaterial({ color: '#d4af37', wireframe: true })
);"""
        },

        # 9. Leaflet Heatmap Kernel Density Estimation (KDE)
        {
            'slide_id': 'slide-09-leaflet-kde',
            'tag': '09 / Kernel Density',
            'headline': 'Continuous Heat Density:',
            'headline_span': 'KDE Tourist Footfall Heatmap',
            'subtitle': 'Gaussian kernel smoothing interpolating discrete guest GPS pings into continuous intensity gradients.',
            'library_badge': 'Leaflet.heat / Simpleheat',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <!-- Simulated Heatmap Gradient Blob -->
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <defs>
                    <radialGradient id="heatCore" cx="50%" cy="50%" r="50%">
                      <stop offset="0%" stop-color="#ff1744" stop-opacity="0.9"/>
                      <stop offset="35%" stop-color="#ffab00" stop-opacity="0.75"/>
                      <stop offset="65%" stop-color="#00e676" stop-opacity="0.5"/>
                      <stop offset="100%" stop-color="#070c09" stop-opacity="0"/>
                    </radialGradient>
                    <radialGradient id="heatSub" cx="50%" cy="50%" r="50%">
                      <stop offset="0%" stop-color="#ffab00" stop-opacity="0.8"/>
                      <stop offset="50%" stop-color="#00e676" stop-opacity="0.4"/>
                      <stop offset="100%" stop-color="#070c09" stop-opacity="0"/>
                    </radialGradient>
                  </defs>
                  <!-- Basemap Contours -->
                  <rect x="20" y="20" width="310" height="200" fill="#0c1712" stroke="rgba(255,255,255,0.1)" rx="6"/>
                  <!-- Heat Blobs -->
                  <circle cx="150" cy="110" r="85" fill="url(#heatCore)"/>
                  <circle cx="230" cy="140" r="65" fill="url(#heatSub)"/>
                  <!-- Center Anchor -->
                  <circle cx="150" cy="110" r="4" fill="#fff"/>
                  <text x="150" y="100" text-anchor="middle" fill="#fff" font-family="DM Sans" font-size="10" font-weight="bold">Orchard Core</text>
                  <text x="230" y="135" text-anchor="middle" fill="#fff" font-family="DM Sans" font-size="10" font-weight="bold">Marina Core</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': '2D Gaussian kernel density: $\\hat{f}(x, y) = \\frac{1}{n h^2 2\\pi} \\sum \\exp\\left(-\\frac{d_i^2}{2h^2}\\right)$ with color-lookup palette.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Retail footfall density, tourist congregation hotspots, high-incident emergency zones.'},
                {'title': 'Technical Strengths', 'desc': 'Blazingly fast canvas alpha-blending with dynamic radius adjustment on zoom level changes.'}
            ],
            'metrics': [
                {'label': 'Kernel', 'val': 'Gaussian 2D', 'sub': 'Radial Falloff'},
                {'label': 'Radius', 'val': 'Dynamic Bandwidth', 'sub': 'h = 25px'},
                {'label': 'Palette', 'val': 'Color Gradient', 'sub': 'Cyan to Red'},
                {'label': 'Throughput', 'val': '50,000 Pings', 'sub': 'Canvas Alpha'}
            ],
            'code_snippet': """L.heatLayer(latlngs, {
  radius: 25, blur: 15,
  gradient: { 0.4: '#00e676', 0.65: '#d4af37', 1.0: '#ff1744' }
}).addTo(map);"""
        },

        # 10. Voronoi Flight Corridor Mesh
        {
            'slide_id': 'slide-10-voronoi-geo',
            'tag': '10 / Catchment Polygons',
            'headline': 'Territorial Catchments:',
            'headline_span': 'Geographic Voronoi Corridors',
            'subtitle': 'Spherical Delaunay triangulation computing exclusive airport catchment boundaries.',
            'library_badge': 'D3 Geo Voronoi',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Voronoi Cells -->
                  <polygon points="50,30 180,20 150,110 40,90" fill="rgba(0,230,118,0.12)" stroke="#00e676" stroke-width="1.5"/>
                  <polygon points="180,20 310,40 270,120 150,110" fill="rgba(212,175,55,0.12)" stroke="#d4af37" stroke-width="1.5"/>
                  <polygon points="40,90 150,110 130,210 30,190" fill="rgba(0,229,255,0.12)" stroke="#00e5ff" stroke-width="1.5"/>
                  <polygon points="150,110 270,120 290,210 130,210" fill="rgba(243,207,101,0.12)" stroke="#f3cf65" stroke-width="1.5"/>
                  <!-- Airport Seed Points -->
                  <circle cx="105" cy="65" r="5" fill="#00e676"/>
                  <circle cx="230" cy="70" r="5" fill="#d4af37"/>
                  <circle cx="90" cy="150" r="5" fill="#00e5ff"/>
                  <circle cx="210" cy="165" r="5" fill="#f3cf65"/>
                  <text x="105" y="55" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="9">SIN (Changi)</text>
                  <text x="230" y="60" text-anchor="middle" fill="#d4af37" font-family="JetBrains Mono" font-size="9">KUL (Kuala Lumpur)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Spherical Voronoi tessellation on ellipsoid: bisector great-circles partitioning surface into nearest-neighbor cells.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Airport catchment area analysis, regional hospital emergency response territories, trade area modeling.'},
                {'title': 'Technical Strengths', 'desc': 'Mathematically partitions 100% of geographic space with zero overlap and zero gaps.'}
            ],
            'metrics': [
                {'label': 'Tessellation', 'val': 'Spherical Voronoi', 'sub': 'Great-Circle'},
                {'label': 'Coverage', 'val': '100% Complete', 'sub': 'Zero Gaps'},
                {'label': 'Dual Mesh', 'val': 'Delaunay Sphere', 'sub': 'Triangulation'},
                {'label': 'Application', 'val': 'Airport Catchment', 'sub': 'Territory'}
            ],
            'code_snippet': """const v = d3.geoVoronoi()(airports);
svg.append('path').datum(v.polygons())
  .attr('d', path).attr('fill', 'rgba(...)');"""
        },

        # 11. Isochrone Travel-Time Polygon Reachability Contours
        {
            'slide_id': 'slide-11-isochrones',
            'tag': '11 / Reachability Polygons',
            'headline': 'Time-Distance Contours:',
            'headline_span': 'Isochrone Reachability Rings',
            'subtitle': 'Concentric travel-time polygons mapping 15-minute, 30-minute, and 45-minute drive accessibility.',
            'library_badge': 'Isochrone API + Leaflet',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 280" style="width:100%; max-height:280px;">
                  <!-- 45-min Outer Polygon -->
                  <path d="M 160 30 Q 270 50, 280 140 T 230 250 T 110 240 T 40 130 Z" fill="rgba(255,23,68,0.12)" stroke="#ff1744" stroke-width="1.5"/>
                  <!-- 30-min Mid Polygon -->
                  <path d="M 160 70 Q 230 90, 230 140 T 190 210 T 120 200 T 80 130 Z" fill="rgba(212,175,55,0.18)" stroke="#d4af37" stroke-width="1.5"/>
                  <!-- 15-min Inner Polygon -->
                  <path d="M 160 110 Q 195 120, 195 140 T 170 175 T 140 170 T 120 135 Z" fill="rgba(0,230,118,0.25)" stroke="#00e676" stroke-width="2"/>
                  <!-- Center Property -->
                  <circle cx="160" cy="140" r="7" fill="#fff"/>
                  <text x="160" y="160" text-anchor="middle" fill="#070c09" font-family="DM Sans" font-size="9" font-weight="bold">Hotel</text>
                  <!-- Labels -->
                  <text x="160" y="100" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="9">15 Min Transit</text>
                  <text x="160" y="60" text-anchor="middle" fill="#d4af37" font-family="JetBrains Mono" font-size="9">30 Min Transit</text>
                  <text x="160" y="22" text-anchor="middle" fill="#ff1744" font-family="JetBrains Mono" font-size="9">45 Min Transit</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Road network graph Dijkstra isochrone expansion: $\\{x \\in \\mathbb{R}^2 \\mid t_{\\text{drive}}(x_0, x) \\le T\\}$ contoured into polygons.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel site feasibility studies, restaurant delivery radius calculation, airport shuttle coverage.'},
                {'title': 'Technical Strengths', 'desc': 'Replaces crude circular distance radii with true real-world road network drive-time physics.'}
            ],
            'metrics': [
                {'label': 'Routing Base', 'val': 'OpenStreetMap', 'sub': 'OSRM Engine'},
                {'label': 'Contours', 'val': '15 / 30 / 45 Min', 'sub': 'Real Transit'},
                {'label': 'Traffic', 'val': 'Peak vs Off-Peak', 'sub': 'Speed Profiles'},
                {'label': 'Accuracy', 'val': 'Road Network', 'sub': 'No As-the-Crow'}
            ],
            'code_snippet': """fetch(`https://api.mapbox.com/isochrone/v1/mapbox/driving/${lon},${lat}?contours_minutes=15,30,45`)
  .then(res => res.json())
  .then(geojson => L.geoJSON(geojson).addTo(map));"""
        },

        # 12. Real-time GPS Fleet Asset Tracking
        {
            'slide_id': 'slide-12-fleet-tracking',
            'tag': '12 / Streaming Telemetry',
            'headline': 'Real-Time Telemetry:',
            'headline_span': 'Moving Fleet Asset Vectors',
            'subtitle': 'Continuous GPS stream with heading direction arrows, geofence triggers, and speed alarms.',
            'library_badge': 'Leaflet MovingMarker',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Road Polyline -->
                  <path d="M 40 200 L 140 140 L 220 160 L 310 60" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="6"/>
                  <path d="M 40 200 L 140 140 L 220 160 L 310 60" fill="none" stroke="#d4af37" stroke-width="2" stroke-dasharray="4"/>
                  <!-- Vehicle Marker -->
                  <g transform="translate(180, 150) rotate(15)">
                    <polygon points="0,-12 8,10 -8,10" fill="#00e676" stroke="#fff" stroke-width="1.5"/>
                  </g>
                  <!-- Telemetry Badge -->
                  <rect x="190" y="105" width="130" height="36" fill="#13221b" stroke="#00e676" rx="4"/>
                  <text x="200" y="122" fill="#fffefa" font-family="DM Sans" font-size="10" font-weight="bold">VIP Shuttle #4</text>
                  <text x="200" y="135" fill="#00e676" font-family="JetBrains Mono" font-size="9">64 km/h &bull; ETA 6m</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Kalman filter sensor fusion smoothing noisy GPS coordinates with bearing angle calculation $\\theta = \\text{atan2}(\\Delta y, \\Delta x)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel luxury airport fleet dispatch, emergency ambulance routing, cold-chain pharmaceutical tracking.'},
                {'title': 'Technical Strengths', 'desc': 'Smooth marker interpolation between GPS pings prevents erratic visual jumps.'}
            ],
            'metrics': [
                {'label': 'Filter', 'val': 'Kalman Filter', 'sub': 'GPS Smoothing'},
                {'label': 'Heading', 'val': 'Dynamic Bearing', 'sub': 'atan2 Math'},
                {'label': 'Geofencing', 'val': 'Polygon Cross', 'sub': 'Automated Alert'},
                {'label': 'Cadence', 'val': '1,000 ms', 'sub': 'Live Telemetry'}
            ],
            'code_snippet': """const marker = L.Marker.movingMarker([
  [lat1, lon1], [lat2, lon2]
], [20000], { autostart: true });
marker.addTo(map);"""
        },

        # 13. Polar Stereographic Arctic / Antarctic Projection
        {
            'slide_id': 'slide-13-polar-projection',
            'tag': '13 / High-Latitude Projection',
            'headline': 'Conformal Arctic Cartography:',
            'headline_span': 'Polar Stereographic Mesh',
            'subtitle': 'Conformal projection preserving true angles at high polar latitudes without Mercator distortions.',
            'library_badge': 'D3 Geo Projection',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 300 300" style="width:260px; height:260px;">
                  <circle cx="150" cy="150" r="120" fill="#070c09" stroke="#d4af37" stroke-width="2"/>
                  <!-- Latitude Graticules -->
                  <circle cx="150" cy="150" r="90" fill="none" stroke="rgba(255,255,255,0.12)" stroke-dasharray="3"/>
                  <circle cx="150" cy="150" r="60" fill="none" stroke="rgba(255,255,255,0.12)" stroke-dasharray="3"/>
                  <circle cx="150" cy="150" r="30" fill="none" stroke="rgba(255,255,255,0.12)" stroke-dasharray="3"/>
                  <!-- Longitude Rays -->
                  <line x1="150" y1="30" x2="150" y2="270" stroke="rgba(255,255,255,0.1)"/>
                  <line x1="30" y1="150" x2="270" y2="150" stroke="rgba(255,255,255,0.1)"/>
                  <!-- North Pole Point -->
                  <circle cx="150" cy="150" r="4" fill="#00e676"/>
                  <text x="150" y="140" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="10">90°N (Pole)</text>
                  <!-- Polar Flight Path -->
                  <path d="M 60 150 Q 150 90, 240 150" fill="none" stroke="#f3cf65" stroke-width="2.5"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Conformal azimuthal projection: perspective projection of sphere from opposite pole onto tangent plane: $r = 2R \\tan(\\pi/4 - \\phi/2)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Cross-polar commercial flight navigation (Dubai to San Francisco), climate ice-sheet observation.'},
                {'title': 'Technical Strengths', 'desc': 'Eliminates infinite Mercator poles; angles around local points are strictly preserved.'}
            ],
            'metrics': [
                {'label': 'Projection', 'val': 'Stereographic', 'sub': 'Conformal Angles'},
                {'label': 'Latitude', 'val': 'True Circles', 'sub': 'Concentric'},
                {'label': 'Meridians', 'val': 'Straight Rays', 'sub': 'Radial Outward'},
                {'label': 'Distortion', 'val': 'Low at Pole', 'sub': 'True Arctic'}
            ],
            'code_snippet': """const projection = d3.geoStereographic()
  .scale(250).rotate([0, -90])
  .clipAngle(180 - 1e-4);"""
        },

        # 14. 3D Point Cloud LiDAR Visualization
        {
            'slide_id': 'slide-14-lidar-pointcloud',
            'tag': '14 / Volumetric Point Clouds',
            'headline': 'LiDAR Surface Scanning:',
            'headline_span': 'Millions of Point Vertices',
            'subtitle': 'Photogrammetric aerial LiDAR laser points colored by vertical elevation gradient.',
            'library_badge': 'Potree / Three.js Points',
            'chart_html': """
              <div id="plotly-lidar-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('plotly-lidar-stage');
                  if (!el || !window.Plotly) return;
                  const n = 250;
                  const x = [], y = [], z = [], c = [];
                  for(let i=0; i<n; i++) {
                    const px = (Math.random() - 0.5) * 40;
                    const py = (Math.random() - 0.5) * 40;
                    const pz = Math.sin(px/8) * Math.cos(py/8) * 15 + Math.random() * 2;
                    x.push(px); y.push(py); z.push(pz);
                    c.push(pz);
                  }
                  const trace = {
                    type: 'scatter3d', mode: 'markers',
                    x: x, y: y, z: z,
                    marker: { size: 3, color: c, colorscale: 'Plasma' }
                  };
                  const layout = {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { showgrid: false, zeroline: false, showticklabels: false },
                      yaxis: { showgrid: false, zeroline: false, showticklabels: false },
                      zaxis: { showgrid: false, zeroline: false, showticklabels: false },
                      camera: { eye: { x: 1.3, y: 1.3, z: 1.1 } }
                    }
                  };
                  Plotly.newPlot('plotly-lidar-stage', [trace], layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Octree spatial index LOD (Level of Detail): points rendered via WebGL gl.POINTS with custom depth shaders.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Heritage hotel architectural preservation scans, coastal erosion surveys, highway asset inspection.'},
                {'title': 'Technical Strengths', 'desc': 'Renders billions of aerial points smoothly using out-of-core streaming octrees.'}
            ],
            'metrics': [
                {'label': 'Index Struct', 'val': 'Octree 3D', 'sub': 'LOD Streaming'},
                {'label': 'Points', 'val': 'Billions Scalable', 'sub': 'Out-of-Core'},
                {'label': 'Precision', 'val': 'Millimeter Scan', 'sub': 'Laser Return'},
                {'label': 'Coloring', 'val': 'Elevation Gradient', 'sub': 'Z-Axis Shaded'}
            ],
            'code_snippet': """Potree.loadPointCloud("pointclouds/hotel/cloud.js", "resort", function(e) {
  scene.addPointCloud(e.pointcloud);
});"""
        },

        # 15. Bivariate Choropleth Map
        {
            'slide_id': 'slide-15-bivariate-choropleth',
            'tag': '15 / Two-Variable Cartography',
            'headline': 'Bivariate Correlation:',
            'headline_span': 'Dual-Variable Color Matrix',
            'subtitle': '3×3 color mixing matrix simultaneously mapping Direct Booking Penetration vs Net ADR Yield.',
            'library_badge': 'Bivariate D3 Mesh',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:space-around; padding:15px;">
                <!-- Map representation -->
                <svg viewBox="0 0 240 200" style="width:200px; height:180px;">
                  <rect x="20" y="20" width="80" height="70" fill="#2d5a44" stroke="#fff" stroke-width="0.5"/>
                  <rect x="110" y="20" width="90" height="70" fill="#00e676" stroke="#fff" stroke-width="0.5"/>
                  <rect x="20" y="100" width="80" height="80" fill="#b5935b" stroke="#fff" stroke-width="0.5"/>
                  <rect x="110" y="100" width="90" height="80" fill="#d4af37" stroke="#fff" stroke-width="0.5"/>
                  <text x="60" y="60" text-anchor="middle" fill="#fff" font-size="10">High/Low</text>
                  <text x="155" y="60" text-anchor="middle" fill="#070c09" font-size="10" font-weight="bold">High/High (Optimum)</text>
                </svg>
                <!-- 3x3 Bivariate Legend Matrix -->
                <svg viewBox="0 0 160 160" style="width:140px; height:140px;">
                  <g transform="translate(20, 20)">
                    <rect x="0" y="0" width="30" height="30" fill="#1b2822"/>
                    <rect x="35" y="0" width="30" height="30" fill="#2d5a44"/>
                    <rect x="70" y="0" width="30" height="30" fill="#00e676"/>
                    <rect x="0" y="35" width="30" height="30" fill="#4a3b22"/>
                    <rect x="35" y="35" width="30" height="30" fill="#8c733f"/>
                    <rect x="70" y="35" width="30" height="30" fill="#b5935b"/>
                    <rect x="0" y="70" width="30" height="30" fill="#6d4822"/>
                    <rect x="35" y="70" width="30" height="30" fill="#a46f2e"/>
                    <rect x="70" y="70" width="30" height="30" fill="#d4af37"/>
                  </g>
                  <text x="70" y="145" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="9">Direct Share &rarr;</text>
                  <text x="10" y="75" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="9" transform="rotate(-90, 10, 75)">Net ADR &rarr;</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Orthogonal color-space multiplication combining two sequential color ramps (e.g., Pink $\\times$ Blue $\\to$ Purple).'},
                {'title': 'Enterprise Use Cases', 'desc': 'Income inequality vs health outcomes, direct share vs net margin, price elasticity vs market share.'},
                {'title': 'Technical Strengths', 'desc': 'Uncovers spatial correlation between two independent variables in a single unified thematic map.'}
            ],
            'metrics': [
                {'label': 'Color Space', 'val': '3 x 3 Matrix', 'sub': 'Dual Gradient'},
                {'label': 'Dimensions', 'val': '2 Quantitative', 'sub': 'Simultaneous'},
                {'label': 'Legend', 'val': 'Rotated Square', 'sub': 'Cartographic Std'},
                {'label': 'Insights', 'val': 'Direct Correlation', 'sub': 'Spatial Synergies'}
            ],
            'code_snippet': """const color = (a, b) => {
  const i = Math.floor(scaleA(a));
  const j = Math.floor(scaleB(b));
  return bivariateColors[i + j * 3];
};"""
        },

        # 16. Animated Particle Wind & Ocean Flow Vectors
        {
            'slide_id': 'slide-16-particle-wind',
            'tag': '16 / Fluid Dynamics',
            'headline': 'Fluid Trajectories:',
            'headline_span': 'Wind & Ocean Current Particles',
            'subtitle': 'Eulerian velocity field with Lagrangian particles visualizing live atmospheric winds and ocean currents.',
            'library_badge': 'Leaflet-Velocity / WindJS',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; position:relative;">
                <canvas id="wind-canvas" width="460" height="320" style="background:#060d09; border-radius:8px; border:1px solid #00e676;"></canvas>
                <div style="position:absolute; bottom:14px; left:16px; background:rgba(7,12,9,0.85); padding:4px 10px; border-radius:4px; font-family:JetBrains Mono; font-size:0.75rem; color:#00e676;">
                  GFS Atmospheric Wind Field &bull; 10m Vectors
                </div>
              </div>
              <script>
              (function(){
                const canvas = document.getElementById('wind-canvas');
                if (!canvas) return;
                const ctx = canvas.getContext('2d');
                const particles = Array.from({length: 400}, () => ({
                  x: Math.random() * canvas.width,
                  y: Math.random() * canvas.height,
                  age: Math.random() * 50
                }));
                function animate() {
                  ctx.fillStyle = 'rgba(6, 13, 9, 0.12)';
                  ctx.fillRect(0, 0, canvas.width, canvas.height);
                  ctx.strokeStyle = '#00e676';
                  ctx.lineWidth = 1.5;
                  particles.forEach(p => {
                    const u = Math.sin(p.y / 40) * 2.5 + 1.2;
                    const v = Math.cos(p.x / 40) * 1.5;
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    p.x += u; p.y += v; p.age++;
                    ctx.lineTo(p.x, p.y);
                    ctx.stroke();
                    if (p.x > canvas.width || p.y > canvas.height || p.age > 60) {
                      p.x = Math.random() * canvas.width;
                      p.y = Math.random() * canvas.height;
                      p.age = 0;
                    }
                  });
                  requestAnimationFrame(animate);
                }
                animate();
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Lagrangian particle advection inside Eulerian vector field $\\vec{u}(x, y, t)$ parsed from GRIB2 weather grids.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Maritime cargo route optimization, airline jetstream flight time planning, hurricane tracking.'},
                {'title': 'Technical Strengths', 'desc': 'Intuitively demonstrates velocity and direction simultaneously without static vector arrows.'}
            ],
            'metrics': [
                {'label': 'Dynamics', 'val': 'Lagrangian Stream', 'sub': 'Advection'},
                {'label': 'Source Data', 'val': 'NOAA GRIB2', 'sub': 'Global Weather'},
                {'label': 'Particles', 'val': '400 Continuous', 'sub': 'Fade Trails'},
                {'label': 'Performance', 'val': '60 FPS Canvas', 'sub': 'GPU Accelerated'}
            ],
            'code_snippet': """L.velocityLayer({
  displayValues: true, displayOptions: { velocityType: 'Wind' },
  data: gfsWindData
}).addTo(map);"""
        },

        # 17. Turf.js Real-time Spatial Buffer & Convex Hull
        {
            'slide_id': 'slide-17-turf-buffers',
            'tag': '17 / Client-Side Spatial GIS',
            'headline': 'In-Browser Computational GIS:',
            'headline_span': 'Turf.js Geometric Buffers',
            'subtitle': 'Instant geometric analysis computing convex hulls, spatial unions, and distance buffers without a server.',
            'library_badge': 'Turf.js Geospatial Engine',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Buffer Area (Convex Hull + Buffer) -->
                  <path d="M 80 80 Q 180 30, 260 90 T 250 180 T 130 190 T 70 140 Z" fill="rgba(212,175,55,0.15)" stroke="#d4af37" stroke-width="2" stroke-dasharray="4"/>
                  <!-- Core Polygon -->
                  <polygon points="100,90 230,80 220,160 120,150" fill="rgba(0,230,118,0.3)" stroke="#00e676" stroke-width="2"/>
                  <!-- Seed Coordinates -->
                  <circle cx="100" cy="90" r="5" fill="#fff"/>
                  <circle cx="230" cy="80" r="5" fill="#fff"/>
                  <circle cx="220" cy="160" r="5" fill="#fff"/>
                  <circle cx="120" cy="150" r="5" fill="#fff"/>
                  <text x="175" y="125" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="11" font-weight="bold">Asset Perimeter</text>
                  <text x="175" y="55" text-anchor="middle" fill="#d4af37" font-family="JetBrains Mono" font-size="10">5km Exclusive Marketing Buffer</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Minkowski sum expansion of polygon boundary with radius $R$, generating smooth rounded outer buffer offsets.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Non-compete territory clauses between franchisee hotels, noise pollution radius buffers.'},
                {'title': 'Technical Strengths', 'desc': 'Runs 100% in client-side JavaScript, eliminating heavy PostGIS database queries.'}
            ],
            'metrics': [
                {'label': 'GIS Engine', 'val': 'Turf.js Pure JS', 'sub': 'Zero Backend'},
                {'label': 'Operations', 'val': 'Buffer / Hull / Union', 'sub': 'Computational'},
                {'label': 'Geometry', 'val': 'GeoJSON Standard', 'sub': 'WGS84'},
                {'label': 'Latency', 'val': '< 2 ms Calc', 'sub': 'Instant Draw'}
            ],
            'code_snippet': """const buffered = turf.buffer(hotelPerimeter, 5, { units: 'kilometers' });
const hull = turf.convex(guestPoints);
L.geoJSON(buffered).addTo(map);"""
        },

        # 18. Dual-Pane Synchronized Split-Screen Map
        {
            'slide_id': 'slide-18-split-map',
            'tag': '18 / Comparative Cartography',
            'headline': 'Temporal Change Detection:',
            'headline_span': 'Dual-Pane Swipe Comparison',
            'subtitle': 'Synchronized side-by-side map viewport contrasting 2020 pandemic occupancy vs 2026 direct recovery.',
            'library_badge': 'Leaflet-SplitScreen',
            'chart_html': """
              <div style="width:100%; height:100%; display:grid; grid-template-columns:1fr 1fr; position:relative; border-radius:8px; overflow:hidden; border:1px solid #d4af37;">
                <!-- Left Pane: 2020 Intermediated -->
                <div style="background:#131d17; padding:15px; display:flex; flex-direction:column; justify-content:space-between; border-right:2px solid #f3cf65;">
                  <span style="font-family:JetBrains Mono; color:#ff1744; font-size:0.85rem; font-weight:bold;">2020: OTA Intermediated</span>
                  <div style="text-align:center;">
                    <div style="font-family:Newsreader; font-size:2rem; color:#ff1744;">68% OTA Share</div>
                    <div style="font-size:0.8rem; color:#9ba9a1;">$1.4M Commission Loss</div>
                  </div>
                  <span style="font-size:0.75rem; color:#6c7d73;">Basemap: Intermediated Toll</span>
                </div>
                <!-- Right Pane: 2026 Sovereign Direct -->
                <div style="background:#0c1d15; padding:15px; display:flex; flex-direction:column; justify-content:space-between;">
                  <span style="font-family:JetBrains Mono; color:#00e676; font-size:0.85rem; font-weight:bold;">2026: Sovereign Direct</span>
                  <div style="text-align:center;">
                    <div style="font-family:Newsreader; font-size:2rem; color:#00e676;">64% Direct Mix</div>
                    <div style="font-size:0.8rem; color:#fffefa;">+$28.40 Net RevPAR Lift</div>
                  </div>
                  <span style="font-size:0.75rem; color:#00e676;">Basemap: Unmasked 1st-Party</span>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Synchronized affine camera binding: $\\text{Pan}_{A}(x, y, z) \\equiv \\text{Pan}_{B}(x, y, z)$ across split DOM layers.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Disaster damage assessment, urban expansion tracking over decades, channel migration audits.'},
                {'title': 'Technical Strengths', 'desc': 'Interactive dragging swipe divider for pinpoint before/after pixel inspection.'}
            ],
            'metrics': [
                {'label': 'Sync Engine', 'val': 'Camera Lock', 'sub': 'Zero Drift'},
                {'label': 'Interaction', 'val': 'Swipe Split', 'sub': 'Draggable Divider'},
                {'label': 'Comparison', 'val': 'Before vs After', 'sub': 'Clear Contrast'},
                {'label': 'Performance', 'val': 'Dual Canvas', 'sub': 'Synchronized'}
            ],
            'code_snippet': """L.control.sideBySide(leftLayer, rightLayer).addTo(map);"""
        },

        # 19. Triangulated Irregular Network (TIN) Elevation Model
        {
            'slide_id': 'slide-19-tin-elevation',
            'tag': '19 / Surface Triangulation',
            'headline': 'Non-Uniform Topography:',
            'headline_span': 'Triangulated Irregular Network (TIN)',
            'subtitle': 'Adaptive resolution surface mesh concentrating vertices at steep cliffs while simplifying planar fields.',
            'library_badge': 'TIN Terrain Engine',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Triangles of varying density -->
                  <g stroke="#d4af37" stroke-width="1.2" fill="none">
                    <polygon points="30,40 120,30 80,100" fill="rgba(212,175,55,0.1)"/>
                    <polygon points="120,30 220,50 160,110" fill="rgba(212,175,55,0.15)"/>
                    <polygon points="220,50 310,30 260,100" fill="rgba(212,175,55,0.1)"/>
                    <!-- High-density cluster (Cliff) -->
                    <polygon points="80,100 120,105 100,140" fill="rgba(0,230,118,0.2)"/>
                    <polygon points="120,105 160,110 140,145" fill="rgba(0,230,118,0.25)"/>
                    <polygon points="100,140 140,145 120,180" fill="rgba(0,230,118,0.3)"/>
                    <polygon points="80,100 100,140 50,160" fill="rgba(212,175,55,0.1)"/>
                    <polygon points="160,110 260,100 210,170" fill="rgba(212,175,55,0.15)"/>
                    <polygon points="120,180 210,170 170,210" fill="rgba(212,175,55,0.1)"/>
                    <polygon points="50,160 120,180 80,210" fill="rgba(212,175,55,0.1)"/>
                  </g>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Delaunay triangulation with maximum-circumcircle criterion guaranteeing fat non-sliver triangles.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Civil engineering earthwork excavation modeling, flood runoff catchment, golf resort grading.'},
                {'title': 'Technical Strengths', 'desc': 'Requires 80% fewer polygons than uniform raster grids to represent complex mountain terrain.'}
            ],
            'metrics': [
                {'label': 'Mesh Type', 'val': 'TIN Adaptive', 'sub': 'Variable Res'},
                {'label': 'Criteria', 'val': 'Delaunay Empty', 'sub': 'No Slivers'},
                {'label': 'Data Saving', 'val': '-80% Vertices', 'sub': 'Optimized'},
                {'label': 'Standard', 'val': 'USGS / LandXML', 'sub': 'Engineering Std'}
            ],
            'code_snippet': """const tin = turf.tin(points, 'elevation');
L.geoJSON(tin, { style: featureStyle }).addTo(map);"""
        },

        # 20. 3D Exploded Architectural BIM Isometric Projection
        {
            'slide_id': 'slide-20-bim-exploded',
            'tag': '20 / Architectural Isometric',
            'headline': 'Vertical Floor Disassembly:',
            'headline_span': '3D Exploded BIM Architectural Model',
            'subtitle': 'Vertical floorplate separation displaying guest suites, rooftop infinity pools, and MEP mechanical basements.',
            'library_badge': 'BIM / Three.js IFC',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 260" style="width:100%; max-height:280px;">
                  <!-- Top Floor: Penthouse & Pool -->
                  <g transform="translate(45, 20)">
                    <polygon points="130,0 240,40 130,80 20,40" fill="rgba(0,229,255,0.3)" stroke="#00e5ff" stroke-width="1.5"/>
                    <text x="130" y="45" text-anchor="middle" fill="#00e5ff" font-family="DM Sans" font-size="10" font-weight="bold">Penthouse & Infinity Pool</text>
                  </g>
                  <!-- Mid Floor: Luxury Guest Suites -->
                  <g transform="translate(45, 90)">
                    <polygon points="130,0 240,40 130,80 20,40" fill="rgba(0,230,118,0.3)" stroke="#00e676" stroke-width="1.5"/>
                    <text x="130" y="45" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="10" font-weight="bold">Fl 04 - 28: Guest Suites (380 Keys)</text>
                  </g>
                  <!-- Ground Floor: Lobby & F&B -->
                  <g transform="translate(45, 160)">
                    <polygon points="130,0 240,40 130,80 20,40" fill="rgba(212,175,55,0.3)" stroke="#d4af37" stroke-width="1.5"/>
                    <text x="130" y="45" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10" font-weight="bold">Ground: Grand Lobby & Signature Dining</text>
                  </g>
                  <!-- Exploded Axis Guide -->
                  <line x1="175" y1="20" x2="175" y2="240" stroke="#f3cf65" stroke-dasharray="3" stroke-width="1"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Isometric 30-degree matrix projection: $x\' = (x - y)\\cos(30^\\circ), y\' = (x + y)\\sin(30^\\circ) - z + \\Delta z_i$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel property refurbishment budgeting, HVAC/MEP maintenance inspection, spatial RevPAR yield by floor.'},
                {'title': 'Technical Strengths', 'desc': 'Deconstructs dense interior buildings into accessible, inspectable horizontal slabs.'}
            ],
            'metrics': [
                {'label': 'Projection', 'val': 'Isometric 30°', 'sub': 'No Perspective'},
                {'label': 'Explosion', 'val': 'Z-Axis Offset', 'sub': 'Δz Layering'},
                {'label': 'Standard', 'val': 'IFC / BIM Open', 'sub': 'Building Model'},
                {'label': 'Utility', 'val': 'Facility Ops', 'sub': 'Floor-by-Floor'}
            ],
            'code_snippet': """const explodeBuilding = (floors, distance) => {
  floors.forEach((floor, i) => {
    floor.position.z = i * distance;
  });
};"""
        }
    ]

    html = generate_deck_html(deck_meta, slides)
    out_path = os.path.join(SCRIPT_DIR, "04-javascript-3d-maps-geospatial.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Built {out_path} (20 slides, {len(html)} bytes)")

if __name__ == "__main__":
    build_deck()
