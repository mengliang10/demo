"""
Builder for Geospatial & Mapping Tools (6 tools):
Folium, GeoPandas, Cartopy, Geoplotlib, Pydeck, Mapclassify
Each tool gets completely different map projections, Leaflet GIS layers, Deck.gl 3D hexbins, and statistical classifiers!
"""

import os
import json
from .common_frame import render_tool_page
from data_cat4_geospatial import TOOLS_CAT4

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(SCRIPT_DIR, "Python Visualization, Graphical, & Interactive Libraries", "Geospatial & Mapping")

def write_tool_output(tool_folder, html_content):
    target_dir = os.path.join(BASE_DIR, tool_folder)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    clean_name = tool_folder.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  [✓] {tool_folder:<35} -> Dedicated Interactive Studio Built ({len(html_content)/1024:.1f} KB)")

def build_geospatial_tools():
    tool_map = {t["folder"]: t for t in TOOLS_CAT4}

    build_folium(tool_map["Folium"])
    build_geopandas(tool_map["GeoPandas"])
    build_cartopy(tool_map["Cartopy"])
    build_geoplotlib(tool_map["Geoplotlib"])
    build_pydeck(tool_map["Pydeck (Deck.gl wrapper)"])
    build_mapclassify(tool_map["Mapclassify"])

# ==============================================================================
# 1. FOLIUM
# ==============================================================================
def build_folium(tool):
    extra_cdn = """
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    """
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">FOLIUM LEAFLET.JS SLIPPY MAP</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="toggleFoliumCircles()" id="btn-fol-cir" style="font-size:0.7rem; padding:3px 8px;">Toggle Hubs</button>
        <button class="btn-action" onclick="centerFoliumMap()" style="font-size:0.7rem; padding:3px 8px;">Recenter</button>
      </div>
    </div>
    <div class="canvas-body" id="folium-map" style="width:100%; height:100%; min-height:480px; z-index:10;">
      <!-- Leaflet map container -->
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>m = folium.Map(location=[1.3521, 103.8198], zoom_start=12, tiles='CartoDB dark_matter')</span>
      <span>Leaflet.js DOM Layer Binding · EPSG:3857 Web Mercator Projection</span>
    </div>
    """

    custom_js = """
    let foliumMap, circleGroup;
    let circlesVisible = true;

    function initFolium() {
      const container = document.getElementById('folium-map');
      if (!container || typeof L === 'undefined') return;

      foliumMap = L.map('folium-map', {
        center: [1.3521, 103.8198],
        zoom: 12,
        zoomControl: true
      });

      // CartoDB Dark Matter tiles
      L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
        subdomains: 'abcd',
        maxZoom: 19
      }).addTo(foliumMap);

      circleGroup = L.layerGroup().addTo(foliumMap);

      const hubs = [
        { name: 'Marina Bay Financial Hub', lat: 1.2800, lon: 103.8540, radius: 900, color: '#00e676' },
        { name: 'One-North Bio-Tech Park', lat: 1.2980, lon: 103.7870, radius: 1200, color: '#00e5ff' },
        { name: 'Changi Aviation Logistics', lat: 1.3644, lon: 103.9915, radius: 1600, color: '#f3cf65' },
        { name: 'Jurong Innovation District', lat: 1.3480, lon: 103.6880, radius: 1400, color: '#ff1744' }
      ];

      hubs.forEach(h => {
        const circle = L.circle([h.lat, h.lon], {
          color: h.color,
          fillColor: h.color,
          fillOpacity: 0.35,
          radius: h.radius
        }).bindPopup(`<strong>${h.name}</strong><br>Status: Operational Cluster<br>Radius: ${h.radius}m`);
        circleGroup.addLayer(circle);

        L.marker([h.lat, h.lon]).addTo(circleGroup).bindPopup(h.name);
      });
    }

    function toggleFoliumCircles() {
      circlesVisible = !circlesVisible;
      if (circlesVisible) foliumMap.addLayer(circleGroup);
      else foliumMap.removeLayer(circleGroup);
      document.getElementById('btn-fol-cir').innerText = circlesVisible ? 'Hide Hubs' : 'Show Hubs';
    }

    function centerFoliumMap() {
      if (foliumMap) foliumMap.setView([1.3521, 103.8198], 12);
    }

    window.addEventListener('load', () => { setTimeout(initFolium, 100); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 2. GEOPANDAS
# ==============================================================================
def build_geopandas(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">GEOPANDAS VECTOR SPATIAL ANALYSIS</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Buffer Radius:</label>
        <input type="range" id="gpd-buffer" min="10" max="60" step="5" value="25" oninput="drawGeoPandas()" style="width:80px;">
        <button class="btn-action" onclick="toggleGpdVoronoi()" id="btn-gpd-vor" style="font-size:0.7rem; padding:3px 8px;">Toggle Voronoi Cells</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="gpd-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>gdf['buffer'] = gdf.geometry.buffer(distance=5000); sjoin = gpd.sjoin(gdf, census, how='inner')</span>
      <span>GEOS C++ Topological Operations · Shapely MultiPolygon Geometric Algebra</span>
    </div>
    """

    custom_js = """
    let showVoronoi = true;
    const transitStations = [
      { name: 'Station Alpha', x: 220, y: 180, zone: 'Central' },
      { name: 'Station Beta', x: 380, y: 150, zone: 'North' },
      { name: 'Station Gamma', x: 490, y: 260, zone: 'East' },
      { name: 'Station Delta', x: 310, y: 320, zone: 'South' },
      { name: 'Station Epsilon', x: 180, y: 300, zone: 'West' }
    ];

    function toggleGpdVoronoi() {
      showVoronoi = !showVoronoi;
      document.getElementById('btn-gpd-vor').innerText = showVoronoi ? 'Hide Voronoi' : 'Show Voronoi';
      drawGeoPandas();
    }

    function drawGeoPandas() {
      const c = document.getElementById('gpd-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const bufRadius = parseInt(document.getElementById('gpd-buffer').value);

      // Draw simulated Voronoi tessellation partitions
      if (showVoronoi) {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
        ctx.lineWidth = 1;
        ctx.setLineDash([3, 3]);
        // Delimiter chords
        ctx.beginPath(); ctx.moveTo(W*0.5, 0); ctx.lineTo(W*0.5, H); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(0, H*0.5); ctx.lineTo(W, H*0.5); ctx.stroke();
        ctx.setLineDash([]);
      }

      // Buffer circles around transit stations
      transitStations.forEach((st, idx) => {
        // Buffer polygon fill
        ctx.fillStyle = 'rgba(0, 230, 118, 0.12)';
        ctx.strokeStyle = '#00e676';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(st.x, st.y, bufRadius * 2, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        // Station Point (Centroid)
        ctx.fillStyle = '#f3cf65';
        ctx.beginPath();
        ctx.arc(st.x, st.y, 5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#040705';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Label
        ctx.fillStyle = '#fff';
        ctx.font = '10px JetBrains Mono';
        ctx.fillText(st.name, st.x + 8, st.y - 8);
      });

      // Spatial Join overlay legend
      ctx.fillStyle = 'rgba(10, 18, 14, 0.9)';
      ctx.fillRect(20, 20, 260, 65);
      ctx.strokeStyle = 'rgba(255,255,255,0.15)';
      ctx.strokeRect(20, 20, 260, 65);

      ctx.fillStyle = '#00e676';
      ctx.font = '10px JetBrains Mono';
      ctx.fillText(`● Shapely Buffer = ${(bufRadius * 0.2).toFixed(1)} km`, 32, 40);
      ctx.fillStyle = '#f3cf65';
      ctx.fillText(`● Point Centroid Nodes (n=${transitStations.length})`, 32, 58);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`CRS: EPSG:4326 (WGS 84)`, 32, 74);
    }

    window.addEventListener('load', () => { drawGeoPandas(); });
    window.addEventListener('resize', drawGeoPandas);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 3. CARTOPY
# ==============================================================================
def build_cartopy(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">CARTOPY GEODETIC PROJECTION ENGINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="setCartopyProj('ortho')" id="btn-cp-ortho" style="font-size:0.7rem; padding:3px 8px;">Orthographic Globe</button>
        <button class="btn-action" onclick="setCartopyProj('robinson')" id="btn-cp-robin" style="font-size:0.7rem; padding:3px 8px;">Robinson Equal-Area</button>
        <button class="btn-action" onclick="toggleCartopyGraticule()" style="font-size:0.7rem; padding:3px 8px;">Graticule Lines</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="cartopy-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>ax = fig.add_subplot(projection=ccrs.Orthographic(central_longitude=100)); ax.gridlines()</span>
      <span>PROJ C++ Library Coordinate Transformation · Geodesic Great Circle Arc Calculation</span>
    </div>
    """

    custom_js = """
    let cartopyProj = 'ortho';
    let showGraticules = true;
    let globeRot = 0;

    function setCartopyProj(p) {
      cartopyProj = p;
      drawCartopy();
    }
    function toggleCartopyGraticule() {
      showGraticules = !showGraticules;
      drawCartopy();
    }

    function drawCartopy() {
      const c = document.getElementById('cartopy-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      if (cartopyProj === 'ortho') {
        // Orthographic 3D Sphere Globe
        const cx = W / 2; const cy = H / 2; const R = 170;

        // Space glow
        const grad = ctx.createRadialGradient(cx, cy, R * 0.8, cx, cy, R * 1.1);
        grad.addColorStop(0, 'rgba(0, 230, 118, 0.08)');
        grad.addColorStop(1, 'transparent');
        ctx.fillStyle = grad;
        ctx.beginPath(); ctx.arc(cx, cy, R * 1.1, 0, 2*Math.PI); ctx.fill();

        // Globe sphere
        ctx.fillStyle = '#08140e';
        ctx.beginPath(); ctx.arc(cx, cy, R, 0, 2*Math.PI); ctx.fill();
        ctx.strokeStyle = '#00e676';
        ctx.lineWidth = 1.8;
        ctx.stroke();

        // Graticules (Parallels & Meridians)
        if (showGraticules) {
          ctx.strokeStyle = 'rgba(255,255,255,0.1)';
          ctx.lineWidth = 1;
          for (let lat = -60; lat <= 60; lat += 30) {
            const yOffset = cy - Math.sin((lat * Math.PI) / 180) * R;
            const rLat = Math.cos((lat * Math.PI) / 180) * R;
            ctx.beginPath();
            ctx.ellipse(cx, yOffset, rLat, rLat * 0.25, 0, 0, 2*Math.PI);
            ctx.stroke();
          }
        }

        // Great Circle Geodesic Arc (Singapore to London)
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(cx + 60, cy - 20); // Singapore
        ctx.bezierCurveTo(cx + 20, cy - 120, cx - 60, cy - 110, cx - 80, cy - 80); // London
        ctx.stroke();

        ctx.fillStyle = '#f3cf65';
        ctx.fillText('Geodesic: SIN ✈ LHR (10,880 km)', cx - 100, cy + R + 25);
      } else {
        // Robinson projection pseudocylindrical
        const rx = 80; const ry = 80; const rw = W - 160; const rh = H - 160;
        ctx.strokeStyle = '#00e5ff';
        ctx.lineWidth = 1.5;
        ctx.strokeRect(rx, ry, rw, rh);

        if (showGraticules) {
          ctx.strokeStyle = 'rgba(255,255,255,0.08)';
          for (let x = rx; x <= rx + rw; x += rw / 6) { ctx.beginPath(); ctx.moveTo(x, ry); ctx.lineTo(x, ry + rh); ctx.stroke(); }
          for (let y = ry; y <= ry + rh; y += rh / 6) { ctx.beginPath(); ctx.moveTo(rx, y); ctx.lineTo(rx + rw, y); ctx.stroke(); }
        }

        ctx.fillStyle = '#00e5ff';
        ctx.font = '12px DM Sans';
        ctx.fillText('ccrs.Robinson() Global Equal-Area Planar Grid', rx + 15, ry + 25);
      }
    }

    window.addEventListener('load', () => { drawCartopy(); });
    window.addEventListener('resize', drawCartopy);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 4. GEOPLOTLIB
# ==============================================================================
def build_geoplotlib(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676; box-shadow:0 0 10px #00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">GEOPLOTLIB REALTIME FLIGHT TRAILS</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--cyan-neon);">Active Flights: <strong>60</strong></span>
        <button class="btn-action" onclick="toggleGeoplotPause()" id="btn-gpl-run" style="font-size:0.7rem; padding:3px 8px;">Pause</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#020403; display:flex; align-items:center; justify-content:center;">
      <canvas id="geoplot-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>import geoplotlib; geoplotlib.graph(data, src_lat='lat1', src_lon='lon1', dest_lat='lat2')</span>
      <span>Hardware OpenGL Spatial Particles · High-Throughput Track Animation</span>
    </div>
    """

    custom_js = """
    let gplRunning = true;
    let gplParticles = [];

    const hubs = [
      { id: 'LHR', x: 280, y: 150 },
      { id: 'JFK', x: 180, y: 170 },
      { id: 'SIN', x: 480, y: 260 },
      { id: 'HND', x: 530, y: 180 },
      { id: 'DXB', x: 380, y: 210 },
      { id: 'SYD', x: 540, y: 340 }
    ];

    function initGeoplotParticles() {
      gplParticles = [];
      for (let i = 0; i < 60; i++) {
        const src = hubs[Math.floor(Math.random() * hubs.length)];
        let dst = hubs[Math.floor(Math.random() * hubs.length)];
        while (dst === src) dst = hubs[Math.floor(Math.random() * hubs.length)];

        gplParticles.push({
          src: src, dst: dst,
          progress: Math.random(),
          speed: 0.003 + Math.random() * 0.004,
          color: (i % 2 === 0) ? '#00e676' : '#00e5ff'
        });
      }
    }
    initGeoplotParticles();

    function toggleGeoplotPause() {
      gplRunning = !gplRunning;
      document.getElementById('btn-gpl-run').innerText = gplRunning ? 'Pause' : 'Resume';
      if (gplRunning) requestAnimationFrame(geoplotLoop);
    }

    function geoplotLoop() {
      if (!gplRunning) return;

      const c = document.getElementById('geoplot-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      // Motion blur fade
      ctx.fillStyle = 'rgba(2, 4, 3, 0.15)';
      ctx.fillRect(0, 0, W, H);

      // Draw Hubs
      hubs.forEach(h => {
        ctx.fillStyle = '#f3cf65';
        ctx.beginPath(); ctx.arc(h.x, h.y, 4, 0, 2*Math.PI); ctx.fill();
        ctx.fillStyle = '#94a3b8';
        ctx.font = '10px JetBrains Mono';
        ctx.fillText(h.id, h.x - 8, h.y - 8);
      });

      // Draw Flight Particles
      gplParticles.forEach(p => {
        p.progress += p.speed;
        if (p.progress >= 1.0) p.progress = 0;

        // Quadratic Bezier arc
        const midX = (p.src.x + p.dst.x) / 2;
        const midY = (p.src.y + p.dst.y) / 2 - 40;

        const t = p.progress;
        const curX = (1-t)*(1-t)*p.src.x + 2*(1-t)*t*midX + t*t*p.dst.x;
        const curY = (1-t)*(1-t)*p.src.y + 2*(1-t)*t*midY + t*t*p.dst.y;

        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(curX, curY, 2.5, 0, 2*Math.PI);
        ctx.fill();
      });

      requestAnimationFrame(geoplotLoop);
    }

    window.addEventListener('load', () => { requestAnimationFrame(geoplotLoop); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 5. PYDECK
# ==============================================================================
def build_pydeck(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9; box-shadow:0 0 10px #d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">PYDECK (DECK.GL) 3D HEXAGON ELEVATION</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Pitch:</label>
        <input type="range" id="deck-pitch" min="0" max="60" step="5" value="45" oninput="drawPydeck()" style="width:70px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); margin-left:6px;">Extrusion Scale:</label>
        <input type="range" id="deck-elev" min="0.5" max="2.5" step="0.1" value="1.2" oninput="drawPydeck()" style="width:70px;">
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="deck-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>pdk.Layer('HexagonLayer', data=df, get_position='[lon, lat]', elevation_scale=50, extruded=True)</span>
      <span>GPU WebGL Hexbin Aggregation · 60 FPS Perspective Pitch & Bearing</span>
    </div>
    """

    custom_js = """
    function drawPydeck() {
      const c = document.getElementById('deck-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const pitch = parseInt(document.getElementById('deck-pitch').value);
      const elevScale = parseFloat(document.getElementById('deck-elev').value);

      const pitchFactor = 1.0 - (pitch / 90) * 0.55;

      // Draw 3D isometric extruded hexagon grid
      const hexes = [
        { q: 0, r: 0, height: 140 },
        { q: 1, r: -1, height: 110 },
        { q: 1, r: 0, height: 180 },
        { q: 0, r: 1, height: 95 },
        { q: -1, r: 1, height: 130 },
        { q: -1, r: 0, height: 160 },
        { q: 0, r: -1, height: 75 },
        { q: 2, r: -1, height: 125 },
        { q: 2, r: 0, height: 195 },
        { q: 1, r: 1, height: 85 }
      ];

      const cx = W / 2; const cy = H / 2 + 30;
      const hexRad = 36;

      hexes.sort((a, b) => (a.r - b.r));

      hexes.forEach(h => {
        const x = cx + hexRad * (Math.sqrt(3) * h.q + Math.sqrt(3)/2 * h.r);
        const y = cy + hexRad * (3/2 * h.r) * pitchFactor;
        const extrusion = h.height * elevScale * (pitch / 45);

        // Extruded vertical pillar
        const grad = ctx.createLinearGradient(0, y - extrusion, 0, y);
        grad.addColorStop(0, '#00e676');
        grad.addColorStop(1, '#0a2e1d');

        ctx.fillStyle = grad;
        ctx.fillRect(x - hexRad * 0.8, y - extrusion, hexRad * 1.6, extrusion);

        // Hexagon top face
        ctx.fillStyle = '#00e5ff';
        ctx.beginPath();
        for (let i = 0; i < 6; i++) {
          const angle = (Math.PI / 3) * i;
          const px = x + hexRad * 0.85 * Math.cos(angle);
          const py = (y - extrusion) + hexRad * 0.85 * Math.sin(angle) * pitchFactor;
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.closePath();
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1;
        ctx.stroke();
      });

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px JetBrains Mono';
      ctx.fillText(`deck.gl Pitch: ${pitch}° | Elevation Multiplier: ${elevScale}x`, 25, 30);
    }

    window.addEventListener('load', () => { drawPydeck(); });
    window.addEventListener('resize', drawPydeck);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 6. MAPCLASSIFY
# ==============================================================================
def build_mapclassify(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">MAPCLASSIFY CHOROPLETH CLASSIFICATION BENCHMARK</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Algorithm:</label>
        <select id="mc-algo" onchange="drawMapclassify()" style="background:#070d09; color:#fff; border:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; padding:2px 6px; border-radius:4px;">
          <option value="fisher_jenks" selected>NaturalBreaks (Fisher-Jenks)</option>
          <option value="quantiles">Quantiles (Equal Frequency)</option>
          <option value="equal_interval">EqualInterval</option>
          <option value="std_mean">StdMean (Standard Deviation)</option>
        </select>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; flex-direction:column; gap:12px;">
      <div style="flex:1; width:100%; position:relative;">
        <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--gold-bright); margin-bottom:4px;">Histogram Distribution & Classification Cut-Points (k=5)</div>
        <canvas id="mc-canvas-hist" style="width:100%; height:calc(100% - 20px); min-height:220px;"></canvas>
      </div>
      <div style="height:150px; width:100%; position:relative;">
        <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--cyan-neon); margin-bottom:4px;">Choropleth Color Palette Bin Intervals</div>
        <canvas id="mc-canvas-bins" style="width:100%; height:calc(100% - 20px);"></canvas>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>classifier = mapclassify.NaturalBreaks(values, k=5); print(classifier.bins)</span>
      <span>1D Optimal K-Means Variance Minimization · Goodness of Variance Fit (GVF)</span>
    </div>
    """

    custom_js = """
    function drawMapclassify() {
      const algo = document.getElementById('mc-algo').value;

      // Precomputed cut points for skewed income dataset
      const cuts = {
        fisher_jenks: [18, 38, 65, 95, 160],
        quantiles: [22, 34, 48, 68, 160],
        equal_interval: [32, 64, 96, 128, 160],
        std_mean: [25, 45, 65, 85, 160]
      }[algo];

      drawHist(cuts);
      drawBins(cuts);
    }

    function drawHist(cuts) {
      const c = document.getElementById('mc-canvas-hist');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070f0b';
      ctx.fillRect(0, 0, W, H);

      // Draw skewed distribution bars
      const nBins = 40;
      const maxVal = 160;
      const barW = (W - 60) / nBins;

      for (let i = 0; i < nBins; i++) {
        const xVal = (i / nBins) * maxVal;
        // Chi-square like right-skewed distribution
        const freq = Math.pow(xVal, 1.8) * Math.exp(-xVal / 18) * 0.08;
        const bH = freq * (H - 40);
        const bx = 40 + i * barW;
        const by = H - 25 - bH;

        ctx.fillStyle = '#334155';
        ctx.fillRect(bx, by, barW - 1, bH);
      }

      // Draw Vertical Cut-Off Lines
      const colors = ['#00e676', '#00e5ff', '#f3cf65', '#ff1744', '#d500f9'];
      cuts.forEach((cut, idx) => {
        const cx = 40 + (cut / maxVal) * (W - 60);
        ctx.strokeStyle = colors[idx];
        ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(cx, 15); ctx.lineTo(cx, H - 25); ctx.stroke();

        ctx.fillStyle = colors[idx];
        ctx.font = '10px JetBrains Mono';
        ctx.fillText(`${cut}`, cx - 8, 12);
      });
    }

    function drawBins(cuts) {
      const c = document.getElementById('mc-canvas-bins');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070f0b';
      ctx.fillRect(0, 0, W, H);

      const colors = ['#0a2e1d', '#00a854', '#00e676', '#f3cf65', '#ff1744'];
      const binW = (W - 60) / 5;

      let prev = 0;
      for (let i = 0; i < 5; i++) {
        const bx = 30 + i * binW;
        ctx.fillStyle = colors[i];
        ctx.fillRect(bx, 20, binW - 8, 45);

        ctx.fillStyle = '#fff';
        ctx.font = '10px JetBrains Mono';
        ctx.fillText(`[${prev}, ${cuts[i]})`, bx + 10, 45);
        prev = cuts[i];
      }
    }

    window.addEventListener('load', () => { drawMapclassify(); });
    window.addEventListener('resize', drawMapclassify);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)
