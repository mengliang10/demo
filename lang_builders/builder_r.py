"""
Builder for R Visualization Libraries:
ggplot2, plotly, leaflet, visNetwork, shiny, ggiraph, dygraphs, corrplot
"""
import os
from .common_frame import render_lang_page

BASE_DIR = "/run/media/ml/Storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/R Visualization"

def write_tool(folder_name, html):
    target_dir = os.path.join(BASE_DIR, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    clean_name = folder_name.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [✓] R :: {folder_name:<30} -> Studio Built ({len(html)/1024:.1f} KB)")

def build_r_all():
    build_ggplot2()
    build_plotly_r()
    build_leaflet_r()
    build_visnetwork()
    build_shiny()
    build_ggiraph()
    build_dygraphs()
    build_corrplot()

# 1. GGPLOT2
def build_ggplot2():
    paradigms = [{
        "tag": "01 / GRAMMAR OF GRAPHICS",
        "title": "Layered Aesthetic Mapping & Violin-Boxplot Density",
        "subtitle": "Wilkinson's Grammar of Graphics decoupling data, aesthetic mappings (aes), geometric objects (geom), and statistical transformations (stat).",
        "math_desc": "Kernel density estimator: $\\hat{f}_h(x) = \\frac{1}{nh} \\sum_{i=1}^n K\\left(\\frac{x - X_i}{h}\\right)$ with Gaussian kernel $K(u) = \\frac{1}{\\sqrt{2\\pi}} e^{-u^2/2}$.",
        "math_formula": "\\text{Plot} = \\text{Data} + \\text{Aesthetics} + \\sum \\text{Geom}_k(\\text{Stat}_k(\\text{Position})) + \\text{Coord} + \\text{Facet}",
        "time_complexity": "O(N log N) sorting and density estimation",
        "space_complexity": "O(N) grid grob scenegraph tree",
        "enterprise_use": "Clinical trial drug efficacy distributions, econometric wage inequality decile decomposition.",
        "strengths": "Unmatched declarative compositionality; publication-standard aesthetic defaults; massive extension ecosystem.",
        "tradeoffs": "Static vector/raster output requiring downstream wrappers (plotly/ggiraph) for web interactivity.",
        "metrics": [
            {"label": "Engine", "val": "grid graphics", "sub": "Native R C-Core"},
            {"label": "Data Model", "val": "Tidy tibble/df", "sub": "Long-Format"},
            {"label": "Rendering", "val": "Cairo / quartz", "sub": "Vector Target"},
            {"label": "License", "val": "MIT / GPL-2", "sub": "Open Standard"}
        ],
        "code": """library(ggplot2)
library(dplyr)

# Layered statistical exploration: Violin + Boxplot + Jitter
p <- ggplot(diamonds, aes(x = cut, y = price, fill = cut)) +
  geom_violin(alpha = 0.4, trim = FALSE, adjust = 1.2) +
  geom_boxplot(width = 0.18, color = "#fffefa", outlier.shape = NA, alpha = 0.8) +
  stat_summary(fun = "median", geom = "point", shape = 23, size = 3, fill = "#f3cf65") +
  scale_fill_viridis_d(option = "mako") +
  scale_y_continuous(labels = scales::dollar_format()) +
  labs(title = "Diamond Price Stratification Across Gemological Cuts",
       subtitle = "Kernel density contours overlaid with interquartile ranges and median markers",
       x = "Diamond Proportional Cut Quality", y = "Transaction Price (USD)") +
  theme_dark() +
  theme(
    plot.background = element_rect(fill = "#050806", color = NA),
    panel.background = element_rect(fill = "#0a110d", color = "#1e293b"),
    text = element_text(color = "#cbd5e1", family = "DM Sans"),
    legend.position = "none"
  )

ggsave("diamond_stratification.pdf", plot = p, width = 10, height = 6, device = cairo_pdf)"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">GGPLOT2 LAYERED GRAMMAR RENDERER</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="toggleGgJitter()" id="btn-gg-jit" style="font-size:0.7rem; padding:3px 8px;">Toggle Points</button>
        <button class="btn-action" onclick="toggleGgViolin()" id="btn-gg-vln" style="font-size:0.7rem; padding:3px 8px;">Toggle Density</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="gg-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>ggplot(df, aes(x, y, fill)) + geom_violin() + geom_boxplot() + stat_summary()</span>
      <span>grid graphics grob tree architecture · Cairo sub-pixel antialiased raster</span>
    </div>
    """

    custom_js = """
    let showJitter = true;
    let showViolin = true;

    function toggleGgJitter() { showJitter = !showJitter; drawGgplot(); }
    function toggleGgViolin() { showViolin = !showViolin; drawGgplot(); }

    function drawGgplot() {
      const c = document.getElementById('gg-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const margin = { top: 40, right: 30, bottom: 60, left: 70 };
      const pw = W - margin.left - margin.right;
      const ph = H - margin.top - margin.bottom;

      // Draw panel background
      ctx.fillStyle = '#0a110d';
      ctx.fillRect(margin.left, margin.top, pw, ph);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(margin.left, margin.top, pw, ph);

      // Grid
      ctx.strokeStyle = 'rgba(255,255,255,0.05)';
      for (let y = margin.top; y <= margin.top + ph; y += ph/5) {
        ctx.beginPath(); ctx.moveTo(margin.left, y); ctx.lineTo(margin.left + pw, y); ctx.stroke();
      }

      const cuts = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'];
      const medians = [4350, 3800, 3980, 4600, 3450];
      const q25 = [2100, 1900, 1850, 2200, 1600];
      const q75 = [6200, 5600, 5800, 6800, 5100];
      const colors = ['#2e1e3b', '#3b4371', '#407088', '#49a09d', '#00e676'];

      const slotW = pw / cuts.length;

      cuts.forEach((cut, i) => {
        const cx = margin.left + slotW * (i + 0.5);

        // 1. Violin density curve
        if (showViolin) {
          ctx.fillStyle = colors[i] + '55';
          ctx.strokeStyle = colors[i];
          ctx.lineWidth = 1.5;
          ctx.beginPath();

          const nPoints = 30;
          const leftHalf = [];
          const rightHalf = [];

          for (let step = 0; step <= nPoints; step++) {
            const frac = step / nPoints;
            const priceVal = frac * 12000;
            const py = margin.top + ph - (priceVal / 12000) * ph;
            const meanP = medians[i];
            const density = Math.exp(-Math.pow(priceVal - meanP, 2) / (2 * 1800 * 1800)) * (slotW * 0.35);

            leftHalf.push({ x: cx - density, y: py });
            rightHalf.push({ x: cx + density, y: py });
          }

          ctx.moveTo(leftHalf[0].x, leftHalf[0].y);
          leftHalf.forEach(pt => ctx.lineTo(pt.x, pt.y));
          rightHalf.reverse().forEach(pt => ctx.lineTo(pt.x, pt.y));
          ctx.closePath();
          ctx.fill();
          ctx.stroke();
        }

        // 2. Jittered scatter points
        if (showJitter) {
          ctx.fillStyle = 'rgba(243, 207, 101, 0.4)';
          for (let j = 0; j < 35; j++) {
            const jx = cx + (Math.random() - 0.5) * (slotW * 0.3);
            const jy = margin.top + ph - (Math.random() * 0.8 + 0.1) * ph;
            ctx.beginPath(); ctx.arc(jx, jy, 2, 0, 2*Math.PI); ctx.fill();
          }
        }

        // 3. Boxplot
        const yMed = margin.top + ph - (medians[i] / 12000) * ph;
        const yQ25 = margin.top + ph - (q25[i] / 12000) * ph;
        const yQ75 = margin.top + ph - (q75[i] / 12000) * ph;

        // Whiskers
        ctx.strokeStyle = '#fffefa';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(cx, yQ25); ctx.lineTo(cx, yQ25 + 25);
        ctx.moveTo(cx, yQ75); ctx.lineTo(cx, yQ75 - 25);
        ctx.stroke();

        // Box
        ctx.fillStyle = 'rgba(14, 23, 18, 0.9)';
        ctx.fillRect(cx - 14, yQ75, 28, yQ25 - yQ75);
        ctx.strokeRect(cx - 14, yQ75, 28, yQ25 - yQ75);

        // Median line
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(cx - 14, yMed); ctx.lineTo(cx + 14, yMed); ctx.stroke();

        // X Axis label
        ctx.fillStyle = '#cbd5e1';
        ctx.font = '11px DM Sans';
        ctx.textAlign = 'center';
        ctx.fillText(cut, cx, H - 25);
      });

      // Y Axis ticks
      ctx.fillStyle = '#64748b';
      ctx.font = '10px JetBrains Mono';
      ctx.textAlign = 'right';
      for (let p = 0; p <= 12000; p += 3000) {
        const y = margin.top + ph - (p / 12000) * ph;
        ctx.fillText('$' + p.toLocaleString(), margin.left - 10, y + 3);
      }
    }

    window.addEventListener('load', () => { drawGgplot(); });
    window.addEventListener('resize', drawGgplot);
    """

    html = render_lang_page("R", "ggplot2", "R Visualization", 'install.packages("ggplot2")',
                            "https://ggplot2.tidyverse.org",
                            "The gold standard layered grammar of graphics implementation in R.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("ggplot2", html)

# 2. PLOTLY (R)
def build_plotly_r():
    extra_cdn = '<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>'
    paradigms = [{
        "tag": "01 / WEBGL 3D SURFACE & VOLCANO",
        "title": "WebGL Hardware-Accelerated 3D Topographic Mesh",
        "subtitle": "Translates R matrix objects directly into interactive JSON schemas executed by the client-side Plotly.js WebGL shader pipeline.",
        "math_desc": "Parametric surface equation: $z = f(x,y) = 100 \\left(\\frac{\\sin\\sqrt{x^2+y^2}}{\\sqrt{x^2+y^2} + 0.1}\\right)$ with marching cubes normal lighting vectors.",
        "math_formula": "\\mathbf{N}(x,y) = \\nabla (z - f(x,y)) = \\left( -\\frac{\\partial f}{\\partial x}, -\\frac{\\partial f}{\\partial y}, 1 \\right)^T",
        "time_complexity": "O(N) hardware GPU geometry render",
        "space_complexity": "O(N) float32 vertex buffer in VRAM",
        "enterprise_use": "Petroleum reservoir seismic depth modeling, financial volatility surface arbitrage scanning.",
        "strengths": "Direct translation of R ggplot2 objects via ggplotly(); instant 3D camera pan, zoom, and mouse tilt.",
        "tradeoffs": "JSON payload size increases exponentially for dense matrices (>1000x1000).",
        "metrics": [
            {"label": "Bridge", "val": "htmlwidgets", "sub": "R to JS JSON"},
            {"label": "Renderer", "val": "WebGL 2.0", "sub": "Hardware Shader"},
            {"label": "Scale", "val": "100K Vertices", "sub": "Smooth 60 FPS"},
            {"label": "License", "val": "MIT Open", "sub": "Enterprise Safe"}
        ],
        "code": """library(plotly)

# Mount Eden volcano topographic dataset in R
data(volcano)

fig <- plot_ly(z = ~volcano) %>%
  add_surface(
    contours = list(
      z = list(show = TRUE, usecolormap = TRUE, highlightcolor = "#ffffff", project = list(z = TRUE))
    ),
    colorscale = "Viridis"
  ) %>%
  layout(
    title = list(text = "Maunga Whau Volcano Topographic Elevation (Plotly R)", font = list(color = "#fffefa")),
    scene = list(
      xaxis = list(title = "Easting (m)", color = "#94a3b8", gridcolor = "#1e293b"),
      yaxis = list(title = "Northing (m)", color = "#94a3b8", gridcolor = "#1e293b"),
      zaxis = list(title = "Elevation (m)", color = "#94a3b8", gridcolor = "#1e293b"),
      bgcolor = "#040705"
    ),
    paper_bgcolor = "#040705"
  )

htmlwidgets::saveWidget(fig, "plotly_volcano.html", selfcontained = TRUE)"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 10px #00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">PLOTLY R HARDWARE WEBGL ACTIVE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="renderRPlotlySurface()" style="font-size:0.7rem; padding:3px 8px;">Volcano Mesh</button>
        <button class="btn-action" onclick="renderRPlotlyScatter()" style="font-size:0.7rem; padding:3px 8px;">3D Scatter Gl</button>
      </div>
    </div>
    <div class="canvas-body" id="plotly-r-stage" style="width:100%; height:100%; min-height:480px;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>plot_ly(z = ~volcano) %>% add_surface(); ggplotly(p)</span>
      <span>htmlwidgets Serialization · Hardware Accelerated 3D Camera Orbit</span>
    </div>
    """

    custom_js = """
    function renderRPlotlySurface() {
      const z = [];
      for (let i = -20; i < 20; i++) {
        const row = [];
        for (let j = -20; j < 20; j++) {
          const r = Math.sqrt(i*i + j*j) + 0.1;
          row.push((Math.sin(r) / r) * 60 + Math.cos(i*0.2)*10);
        }
        z.push(row);
      }
      const data = [{
        z: z,
        type: 'surface',
        colorscale: 'Viridis',
        contours: { z: { show: true, usecolormap: true, project: { z: true } } }
      }];
      const layout = {
        title: { text: 'Plotly R: 3D Topographic Elevation Surface', font: { color: '#fffefa', family: 'Newsreader', size: 17 } },
        paper_bgcolor: '#040705',
        plot_bgcolor: '#040705',
        scene: {
          xaxis: { color: '#94a3b8', gridcolor: '#1e293b' },
          yaxis: { color: '#94a3b8', gridcolor: '#1e293b' },
          zaxis: { color: '#94a3b8', gridcolor: '#1e293b' }
        },
        margin: { l: 0, r: 0, b: 0, t: 40 }
      };
      Plotly.newPlot('plotly-r-stage', data, layout, { responsive: true });
    }

    function renderRPlotlyScatter() {
      const N = 600;
      const x = []; const y = []; const z = []; const color = [];
      for (let i = 0; i < N; i++) {
        const t = i * 0.1;
        x.push(Math.sin(t) * (10 + t*0.1));
        y.push(Math.cos(t) * (10 + t*0.1));
        z.push(t);
        color.push(t);
      }
      const data = [{
        x: x, y: y, z: z,
        mode: 'markers',
        type: 'scatter3d',
        marker: { size: 3.5, color: color, colorscale: 'Plasma', opacity: 0.85 }
      }];
      const layout = {
        title: { text: 'Plotly R: 3D Parametric Trajectory Point Cloud', font: { color: '#fffefa', family: 'Newsreader', size: 17 } },
        paper_bgcolor: '#040705',
        scene: {
          xaxis: { color: '#94a3b8', gridcolor: '#1e293b' },
          yaxis: { color: '#94a3b8', gridcolor: '#1e293b' },
          zaxis: { color: '#94a3b8', gridcolor: '#1e293b' }
        },
        margin: { l: 0, r: 0, b: 0, t: 40 }
      };
      Plotly.newPlot('plotly-r-stage', data, layout, { responsive: true });
    }

    window.addEventListener('load', () => { setTimeout(renderRPlotlySurface, 100); });
    """

    html = render_lang_page("R", "plotly (R)", "R Visualization", 'install.packages("plotly")',
                            "https://plotly.com/r/",
                            "Interactive WebGL 3D surfaces and ggplot2 conversion via htmlwidgets.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("plotly", html)

# 3. LEAFLET (R)
def build_leaflet_r():
    extra_cdn = """
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    """
    paradigms = [{
        "tag": "01 / SPATIAL SLIPPY MAPS",
        "title": "Interactive Leaflet GeoJSON Binding in R",
        "subtitle": "Binds spatial SpatialPolygonsDataFrame and sf (Simple Features) objects to reactive Leaflet slippy map tiles.",
        "math_desc": "Haversine great-circle distance metric: $d = 2r \\arcsin\\sqrt{\\sin^2\\left(\\frac{\\Delta\\phi}{2}\\right) + \\cos\\phi_1 \\cos\\phi_2 \\sin^2\\left(\\frac{\\Delta\\lambda}{2}\\right)}$.",
        "math_formula": "S(p) = \\sum_{i=1}^k w_i \\cdot \\text{Kernel}\\left(\\frac{\\text{dist}(p, x_i)}{b}\\right)",
        "time_complexity": "O(N) quadtree tile bounding box lookups",
        "space_complexity": "O(V) GeoJSON spatial vertex tree",
        "enterprise_use": "Nationwide supply chain distribution hubs, property portfolio valuation heatmaps.",
        "strengths": "Tightly integrates with R's `sf` package; rich plugin library (MarkerClusters, Heatmaps, MiniMap).",
        "tradeoffs": "Browser DOM struggles with large polygons exceeding 20 MB without Vector Tiles (Mapbox/Pmtiles).",
        "metrics": [
            {"label": "GIS Engine", "val": "sf / GEOS", "sub": "Simple Features"},
            {"label": "Projection", "val": "EPSG:3857", "sub": "Web Mercator"},
            {"label": "Output", "val": "HTML5 Canvas", "sub": "Tile-Based"},
            {"label": "License", "val": "GPL-3", "sub": "Open Standard"}
        ],
        "code": """library(leaflet)
library(sf)

# Initialize Leaflet map with dark carto tiles
m <- leaflet() %>%
  addProviderTiles(providers$CartoDB.DarkMatter) %>%
  setView(lng = 103.8198, lat = 1.3521, zoom = 12) %>%
  addCircles(
    lng = c(103.8540, 103.7870, 103.9915),
    lat = c(1.2800, 1.2980, 1.3644),
    radius = c(1200, 1500, 2000),
    color = "#00e676",
    fillColor = "#00e676",
    fillOpacity = 0.4,
    popup = c("Marina Bay HQ", "One-North R&D Enclave", "Changi Aviation Hub")
  )

htmlwidgets::saveWidget(m, "singapore_hubs.html")"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">LEAFLET R SPATIAL ENGINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="recenterLeafletR()" style="font-size:0.7rem; padding:3px 8px;">Recenter</button>
      </div>
    </div>
    <div class="canvas-body" id="leaflet-r-map" style="width:100%; height:100%; min-height:480px; z-index:10;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>leaflet() %>% addProviderTiles(CartoDB.DarkMatter) %>% addCircles()</span>
      <span>R Simple Features (sf) Integration · EPSG:3857 Web Mercator Projections</span>
    </div>
    """

    custom_js = """
    let rLeafletMap;
    function initRLeaflet() {
      const el = document.getElementById('leaflet-r-map');
      if (!el || typeof L === 'undefined') return;

      rLeafletMap = L.map('leaflet-r-map', { center: [1.3521, 103.8198], zoom: 12 });
      L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; OpenStreetMap contributors &copy; CARTO'
      }).addTo(rLeafletMap);

      const hubs = [
        { name: "Marina Bay Financial District", lat: 1.2800, lon: 103.8540, r: 1000, col: "#00e676" },
        { name: "One-North Bio-Tech Park", lat: 1.2980, lon: 103.7870, r: 1400, col: "#00e5ff" },
        { name: "Changi Logistics Hub", lat: 1.3644, lon: 103.9915, r: 1800, col: "#f3cf65" }
      ];

      hubs.forEach(h => {
        L.circle([h.lat, h.lon], {
          color: h.col, fillColor: h.col, fillOpacity: 0.35, radius: h.r
        }).bindPopup(`<strong>${h.name}</strong><br>Radius: ${h.r}m<br>Status: Operational`).addTo(rLeafletMap);
      });
    }

    function recenterLeafletR() {
      if (rLeafletMap) rLeafletMap.setView([1.3521, 103.8198], 12);
    }

    window.addEventListener('load', () => { setTimeout(initRLeaflet, 100); });
    """

    html = render_lang_page("R", "leaflet (R)", "R Visualization", 'install.packages("leaflet")',
                            "https://rstudio.github.io/leaflet/",
                            "Interactive geospatial slippy maps and sf simple features integration.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("leaflet", html)

# 4. VISNETWORK
def build_visnetwork():
    extra_cdn = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" rel="stylesheet" />
    """
    paradigms = [{
        "tag": "01 / HIERARCHICAL PHYSICS",
        "title": "Interactive Network & Dependency Physics in R",
        "subtitle": "R wrapper for vis.js force-directed physics, enabling exploration of complex graph networks directly in HTML.",
        "math_desc": "Spring electrical model: $F_{ij} = -k (d_{ij} - L) \\hat{r}_{ij} + \\frac{C}{d_{ij}^2} \\hat{r}_{ij}$ balancing Hooke's elasticity with Coulomb repulsion.",
        "math_formula": "E = \\sum_{(i,j) \\in E} \\frac{k_{ij}}{2} (\\|x_i - x_j\\| - l_{ij})^2 + \\sum_{i \\ne j} \\frac{q_i q_j}{\\|x_i - x_j\\|}",
        "time_complexity": "O(V^2) or O(V log V) Barnes-Hut quadtree",
        "space_complexity": "O(V + E) adjacency graph representation",
        "enterprise_use": "Corporate ownership control trees, banking systemic transaction fraud detection.",
        "strengths": "Interactive draggable nodes; hierarchical tree visualization; custom HTML tooltips.",
        "tradeoffs": "Client CPU struggles with graphs exceeding 5,000 nodes without WebGL acceleration.",
        "metrics": [
            {"label": "Physics", "val": "Barnes-Hut", "sub": "Quadtree Gravity"},
            {"label": "Scale", "val": "2,500 Nodes", "sub": "Browser Cap"},
            {"label": "Format", "val": "igraph / tidygraph", "sub": "Native R Bind"},
            {"label": "License", "val": "MIT", "sub": "htmlwidgets"}
        ],
        "code": """library(visNetwork)

nodes <- data.frame(
  id = 1:6,
  label = c("Holding Co", "Retail Bank", "Asset Mgmt", "FinTech SPV", "Digital Pay", "Custody Trust"),
  group = c("HoldCo", "Bank", "Funds", "Tech", "Tech", "Bank"),
  value = c(30, 20, 18, 15, 14, 16)
)

edges <- data.frame(
  from = c(1, 1, 1, 2, 4, 3),
  to = c(2, 3, 4, 5, 5, 6),
  arrows = "to",
  smooth = TRUE
)

visNetwork(nodes, edges, width = "100%", height = "500px") %>%
  visOptions(highlightNearest = TRUE, nodesIdSelection = TRUE) %>%
  visPhysics(solver = "forceAtlas2Based", forceAtlas2Based = list(gravitationalConstant = -50))"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">VISNETWORK R PHYSICS GRAPH</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="stabilizeVisNetwork()" style="font-size:0.7rem; padding:3px 8px;">Freeze</button>
        <button class="btn-action" onclick="fitVisNetwork()" style="font-size:0.7rem; padding:3px 8px;">Fit View</button>
      </div>
    </div>
    <div class="canvas-body" id="visnet-stage" style="width:100%; height:100%; min-height:480px; background:#040705;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>visNetwork(nodes, edges) %>% visPhysics(solver='forceAtlas2Based')</span>
      <span>ForceAtlas2 Gravitational Equilibrium · Interactive Node Draggable Physics</span>
    </div>
    """

    custom_js = """
    let visNetInstance;
    function initVisNetwork() {
      const container = document.getElementById('visnet-stage');
      if (!container || typeof vis === 'undefined') return;

      const nodes = new vis.DataSet([
        { id: 1, label: 'Holding Co (HQ)', color: '#f3cf65', size: 26, shape: 'dot' },
        { id: 2, label: 'Retail Banking Core', color: '#00e676', size: 20, shape: 'dot' },
        { id: 3, label: 'Asset Management', color: '#00e5ff', size: 18, shape: 'dot' },
        { id: 4, label: 'FinTech SPV Alpha', color: '#ff1744', size: 16, shape: 'dot' },
        { id: 5, label: 'Digital Payments Rail', color: '#d500f9', size: 16, shape: 'dot' },
        { id: 6, label: 'Global Custody Trust', color: '#00e676', size: 17, shape: 'dot' }
      ]);

      const edges = new vis.DataSet([
        { from: 1, to: 2, arrows: 'to', color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 1, to: 3, arrows: 'to', color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 1, to: 4, arrows: 'to', color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 2, to: 5, arrows: 'to', color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 4, to: 5, arrows: 'to', color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 3, to: 6, arrows: 'to', color: { color: 'rgba(255,255,255,0.3)' } }
      ]);

      const data = { nodes: nodes, edges: edges };
      const options = {
        physics: {
          forceAtlas2Based: { gravitationalConstant: -60, springLength: 100, damping: 0.4 },
          solver: 'forceAtlas2Based'
        },
        nodes: { font: { color: '#fff', face: 'JetBrains Mono', size: 12 } }
      };

      visNetInstance = new vis.Network(container, data, options);
    }

    function stabilizeVisNetwork() {
      if (visNetInstance) visNetInstance.setOptions({ physics: { enabled: false } });
    }

    function fitVisNetwork() {
      if (visNetInstance) visNetInstance.fit({ animation: true });
    }

    window.addEventListener('load', () => { setTimeout(initVisNetwork, 100); });
    """

    html = render_lang_page("R", "visNetwork", "R Visualization", 'install.packages("visNetwork")',
                            "https://datastorm-open.github.io/visNetwork/",
                            "Interactive force-directed and hierarchical graph networks in R.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("visNetwork", html)

# 5. SHINY
def build_shiny():
    paradigms = [{
        "tag": "01 / REACTIVE COMPUTATION GRAPH",
        "title": "Reactive Programming & Shinylive Wasm Architecture",
        "subtitle": "Declarative dependency graph connecting UI input elements to server reactive expressions and outputs.",
        "math_desc": "Directed Acyclic Reactive Graph: updates propagate topologically: $O_k = f(I_1, \\dots, I_m)$ where only invalidated nodes are re-evaluated.",
        "math_formula": "\\mathcal{G} = (V, E), \\quad v \\in V_{\\text{react}} \\implies \\text{Invalidate}(\\text{Descendants}(v))",
        "time_complexity": "O(k) where k is number of dirty dependent nodes",
        "space_complexity": "O(N) reactive state dependency graph",
        "enterprise_use": "FDA regulatory drug submission dossiers, executive macro financial stress-testing dashboards.",
        "strengths": "Pure R code creates full reactive web apps; Shinylive allows running client-side in WebAssembly without R server.",
        "tradeoffs": "Standard Shiny requires an active persistent R process (single-threaded event loop).",
        "metrics": [
            {"label": "Reactivity", "val": "Topological DAG", "sub": "Lazy Invalidation"},
            {"label": "Wasm Mode", "val": "Shinylive", "sub": "Zero-Server WebR"},
            {"label": "Protocol", "val": "WebSocket JSON", "sub": "Binary Packs"},
            {"label": "License", "val": "GPL-3", "sub": "Posit Enterprise"}
        ],
        "code": """library(shiny)
library(bslib)
library(ggplot2)

ui <- page_sidebar(
  theme = bs_theme(bg = "#050806", fg = "#cbd5e1", primary = "#00e676"),
  title = "Commercial Portfolio Allocation Simulator",
  sidebar = sidebar(
    sliderInput("n_alloc", "Direct Channel Budget Share (%)", min = 10, max = 90, value = 65),
    selectInput("market", "Target Geographical Region", choices = c("APAC", "EMEA", "Americas"))
  ),
  card(
    card_header("Projected Direct Incremental Revenue"),
    plotOutput("revPlot")
  )
)

server <- function(input, output, session) {
  simData <- reactive({
    days <- 1:90
    rate <- input$n_alloc / 100
    data.frame(day = days, rev = cumsum(rnorm(90, mean = 2000 * rate, sd = 150)))
  })

  output$revPlot <- renderPlot({
    ggplot(simData(), aes(x = day, y = rev)) +
      geom_line(color = "#00e676", linewidth = 1.2) +
      theme_dark()
  })
}

shinyApp(ui, server)"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">SHINY REACTIVE RUNTIME SIMULATION</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">Shinylive WebR Core</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:0; background:#070b09; display:flex; height:100%; min-height:480px;">
      <!-- Shiny Sidebar -->
      <div style="width:230px; background:#0e1712; border-right:1px solid rgba(255,255,255,0.08); padding:16px; display:flex; flex-direction:column; gap:14px;">
        <div style="font-family:var(--font-mono); font-size:0.7rem; color:#f3cf65;">sidebar() Inputs</div>
        <div>
          <label style="font-size:0.72rem; color:#cbd5e1; display:block; margin-bottom:4px;">Direct Channel Share (%)</label>
          <input type="range" id="sh-slider" min="20" max="90" value="65" oninput="updateShinySim()" style="width:100%;">
          <div style="font-family:var(--font-mono); font-size:0.7rem; color:#00e676; text-align:right;" id="sh-slider-lbl">65%</div>
        </div>
        <div>
          <label style="font-size:0.72rem; color:#cbd5e1; display:block; margin-bottom:4px;">Market Selection</label>
          <select id="sh-market" onchange="updateShinySim()" style="width:100%; background:#040705; color:#fff; border:1px solid rgba(255,255,255,0.15); font-size:0.75rem; padding:4px;">
            <option value="apac">APAC Hospitality</option>
            <option value="emea">EMEA Commercial</option>
          </select>
        </div>
      </div>

      <!-- Shiny Main Panel -->
      <div style="flex:1; padding:16px; display:flex; flex-direction:column; gap:12px;">
        <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:10px;">
          <div style="background:#0e1712; border:1px solid rgba(255,255,255,0.08); padding:10px; border-radius:6px;">
            <div style="font-size:0.7rem; color:#94a3b8;">Reactive Projected Net</div>
            <div style="font-size:1.3rem; font-weight:700; color:#00e676;" id="sh-kpi-net">$1.42M</div>
          </div>
          <div style="background:#0e1712; border:1px solid rgba(255,255,255,0.08); padding:10px; border-radius:6px;">
            <div style="font-size:0.7rem; color:#94a3b8;">OTA Commission Recaptured</div>
            <div style="font-size:1.3rem; font-weight:700; color:#f3cf65;" id="sh-kpi-comm">$340K</div>
          </div>
        </div>

        <div style="background:#0e1712; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:10px; flex:1; display:flex; flex-direction:column;">
          <div style="font-family:var(--font-mono); font-size:0.68rem; color:#00e5ff; margin-bottom:4px;">renderPlot(ggplot(simData, aes(x, y)))</div>
          <canvas id="sh-plot-canvas" style="width:100%; flex:1;"></canvas>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>shinyApp(ui, server) · Shinylive WebAssembly Execution</span>
      <span>Topological Reactive Graph Invalidation · Client-Side Zero-Server Deployment</span>
    </div>
    """

    custom_js = """
    function updateShinySim() {
      const share = parseInt(document.getElementById('sh-slider').value);
      document.getElementById('sh-slider-lbl').innerText = `${share}%`;
      document.getElementById('sh-kpi-net').innerText = `$${(share * 0.022).toFixed(2)}M`;
      document.getElementById('sh-kpi-comm').innerText = `$${Math.round(share * 5.2)}K`;

      drawShinyPlot(share);
    }

    function drawShinyPlot(share) {
      const c = document.getElementById('sh-plot-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070b09';
      ctx.fillRect(0, 0, W, H);

      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2.2;
      ctx.beginPath();
      const nDays = 60;
      for (let d = 0; d < nDays; d++) {
        const x = (d / nDays) * W;
        const trend = (d / nDays) * (share * 2.8);
        const y = H - 20 - (trend / 280) * (H - 40);
        if (d === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }

    window.addEventListener('load', () => { setTimeout(updateShinySim, 100); });
    window.addEventListener('resize', updateShinySim);
    """

    html = render_lang_page("R", "shiny", "R Visualization", 'install.packages("shiny")',
                            "https://shiny.posit.co",
                            "Reactive full-stack web applications and Shinylive WebR client execution.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("shiny", html)

# 6. GGIRAPH
def build_ggiraph():
    paradigms = [{
        "tag": "01 / DYNAMIC SVG GGPLOT",
        "title": "Interactive SVG Elements & Tooltip Callbacks",
        "subtitle": "Replaces standard ggplot2 geoms with interactive geoms (`geom_point_interactive`, `geom_bar_interactive`) producing web-native SVG with hover effects.",
        "math_desc": "Affine coordinate translation of R grob viewports into SVG `<g>` nodes decorated with data-id attributes and CSS hover pseudoclasses.",
        "math_formula": "\\text{SVGNode}(p_i) = \\langle \\text{circle}, \\{cx, cy, r, \\text{data-id}=\\text{id}_i, \\text{tooltip}=\\text{str}_i\\} \\rangle",
        "time_complexity": "O(N) XML SVG node generation",
        "space_complexity": "O(N) DOM node memory",
        "enterprise_use": "Executive boardroom interactive presentations, biopharmaceutical genomic mutation browsers.",
        "strengths": "Retains 100% of ggplot2 syntax and styling; adds zero-lag hardware-accelerated CSS hovers.",
        "tradeoffs": "Large datasets (>50k points) produce bulky SVG DOM documents.",
        "metrics": [
            {"label": "Standard", "val": "W3C SVG 1.1", "sub": "DOM Accessible"},
            {"label": "Events", "val": "Hover / OnClick", "sub": "Shiny Inputs"},
            {"label": "Syntax", "val": "100% ggplot2", "sub": "Drop-in Geoms"},
            {"label": "License", "val": "GPL-3", "sub": "CRAN Verified"}
        ],
        "code": """library(ggiraph)
library(ggplot2)

p <- ggplot(mpg, aes(x = displ, y = hwy, color = class, tooltip = paste("Model:", model, "<br>HWY:", hwy), data_id = model)) +
  geom_point_interactive(size = 3.5, alpha = 0.8) +
  scale_color_viridis_d(option = "plasma") +
  theme_dark() +
  labs(title = "Interactive Vehicle Fuel Economy Breakdown", x = "Displacement (L)", y = "Highway MPG")

girafe(ggobj = p, width_svg = 8, height_svg = 5,
       options = list(opts_hover(css = "fill:#f3cf65;stroke:#ffffff;cursor:pointer;")))"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">GGIRAPH INTERACTIVE SVG DOM</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--gold-bright);" id="ggiraph-hover-lbl">Hover points to inspect</span>
      </div>
    </div>
    <div class="canvas-body" id="ggiraph-container" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <!-- Dynamic SVG -->
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>geom_point_interactive(aes(tooltip=model, data_id=model)); girafe(ggobj=p)</span>
      <span>W3C Vector DOM Element Injection · Native CSS Hover Transitions</span>
    </div>
    """

    custom_js = """
    function renderGgiraphSvg() {
      const el = document.getElementById('ggiraph-container');
      if (!el) return;

      const pts = [
        { model: 'Audi A4', x: 120, y: 140, col: '#00e676', mpg: 31 },
        { model: 'BMW 328i', x: 220, y: 180, col: '#00e5ff', mpg: 28 },
        { model: 'Ford Mustang', x: 380, y: 280, col: '#ff1744', mpg: 19 },
        { model: 'Chevy Corvette', x: 490, y: 320, col: '#f3cf65', mpg: 16 },
        { model: 'Toyota Prius', x: 90, y: 90, col: '#00e676', mpg: 48 },
        { model: 'Tesla Model 3', x: 140, y: 80, col: '#00e5ff', mpg: 52 }
      ];

      let svgContent = `
        <svg viewBox="0 0 640 420" style="width:100%; max-width:640px; height:auto;">
          <line x1="60" y1="360" x2="600" y2="360" stroke="#334155" stroke-width="1.5"/>
          <line x1="60" y1="40" x2="60" y2="360" stroke="#334155" stroke-width="1.5"/>
          <text x="330" y="395" fill="#94a3b8" font-family="DM Sans" font-size="12" text-anchor="middle">Engine Displacement (Liters)</text>
          <text x="25" y="200" fill="#94a3b8" font-family="DM Sans" font-size="12" transform="rotate(-90, 25, 200)" text-anchor="middle">Highway MPG</text>
      `;

      pts.forEach(p => {
        svgContent += `
          <circle cx="${p.x}" cy="${p.y}" r="8" fill="${p.col}" opacity="0.85" style="cursor:pointer; transition:all 0.2s;"
                  onmouseover="onPointHover('${p.model}', ${p.mpg})" onmouseout="onPointLeave(this)"
                  class="ggiraph-dot"/>
        `;
      });
      svgContent += `</svg>`;
      el.innerHTML = svgContent;
    }

    function onPointHover(model, mpg) {
      document.getElementById('ggiraph-hover-lbl').innerText = `Active Model: ${model} (${mpg} Highway MPG)`;
    }
    function onPointLeave(el) {
      document.getElementById('ggiraph-hover-lbl').innerText = 'Hover points to inspect';
    }

    window.addEventListener('load', () => { setTimeout(renderGgiraphSvg, 100); });
    """

    html = render_lang_page("R", "ggiraph", "R Visualization", 'install.packages("ggiraph")',
                            "https://davidgohel.github.io/ggiraph/",
                            "Interactive dynamic SVG extension for the ggplot2 grammar.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("ggiraph", html)

# 7. DYGRAPHS
def build_dygraphs():
    paradigms = [{
        "tag": "01 / HIGH-DENSITY TIME SERIES",
        "title": "Interactive Dense Financial Time-Series with Range Selector",
        "subtitle": "R wrapper for dygraphs JavaScript library engineered specifically for handling millions of time series data points smoothly.",
        "math_desc": "Exponential moving average: $S_t = \\alpha Y_t + (1 - \\alpha) S_{t-1}$ with dynamically rescaled zooming windows and level-of-detail decimation.",
        "math_formula": "\\text{LOD}(T) = \\left\\{ \\text{avg}(Y_k) \\mid k \\in [t_i, t_{i+\\Delta}] \\right\\}",
        "time_complexity": "O(N) pan/zoom resampling",
        "space_complexity": "O(N) continuous float array buffer",
        "enterprise_use": "Algorithmic trading microsecond tick recording, industrial sensor power telemetry.",
        "strengths": "Fastest browser charting engine for massive time-series; synchronized crosshairs across multiple plots.",
        "tradeoffs": "Strictly optimized for 1D/2D time series only; cannot render arbitrary non-temporal geometries.",
        "metrics": [
            {"label": "Scale", "val": "500,000 Pts", "sub": "Smooth Canvas"},
            {"label": "Zoom", "val": "RangeSelector", "sub": "Interactive Brush"},
            {"label": "Data Format", "val": "xts / zoo", "sub": "R Time Series"},
            {"label": "License", "val": "MIT", "sub": "Open Source"}
        ],
        "code": """library(dygraphs)
library(xts)

# Generate synthetic high-density asset price history
dates <- seq(as.Date("2024-01-01"), as.Date("2026-09-15"), by = "days")
returns <- rnorm(length(dates), mean = 0.0005, sd = 0.015)
prices <- 100 * cumprod(1 + returns)

stock_xts <- xts(prices, order.by = dates)
colnames(stock_xts) <- "Portfolio_NAV"

dygraph(stock_xts, main = "High-Density Asset Portfolio NAV Trajectory") %>%
  dyRangeSelector(height = 30) %>%
  dySeries("Portfolio_NAV", color = "#00e676", strokeWidth = 2) %>%
  dyHighlight(highlightCircleSize = 5, highlightSeriesBackgroundAlpha = 0.2)"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">DYGRAPHS R HIGH-DENSITY ENGINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="toggleDySMA()" id="btn-dy-sma" style="font-size:0.7rem; padding:3px 8px;">Toggle SMA Ribbon</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; flex-direction:column; gap:10px;">
      <div style="flex:1; position:relative;">
        <canvas id="dy-main-canvas" style="width:100%; height:100%; min-height:280px;"></canvas>
      </div>
      <div style="height:50px; background:#0e1712; border:1px solid rgba(255,255,255,0.08); border-radius:4px; padding:4px;">
        <canvas id="dy-mini-canvas" style="width:100%; height:100%;"></canvas>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>dygraph(xts_data) %>% dyRangeSelector() %>% dyHighlight()</span>
      <span>HTML5 Canvas Resampling · Sub-millisecond Interactive Range Scrubbing</span>
    </div>
    """

    custom_js = """
    let showSMA = true;
    function toggleDySMA() { showSMA = !showSMA; drawDygraphs(); }

    function drawDygraphs() {
      const c = document.getElementById('dy-main-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      // Grid
      ctx.strokeStyle = 'rgba(255,255,255,0.06)';
      for (let y = 0; y < H; y += 35) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      // Generate 250 points
      const n = 250;
      let price = 100;
      const pts = [];
      for (let i = 0; i < n; i++) {
        price += (Math.sin(i * 0.1) * 2) + (Math.random() - 0.48) * 3;
        pts.push(price);
      }

      // Draw Main Price Series
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      for (let i = 0; i < n; i++) {
        const x = (i / n) * W;
        const y = H * 0.7 - ((pts[i] - 70) / 100) * (H * 0.6);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Draw SMA 20
      if (showSMA) {
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        for (let i = 20; i < n; i++) {
          let sum = 0;
          for (let j = 0; j < 20; j++) sum += pts[i - j];
          const sma = sum / 20;
          const x = (i / n) * W;
          const y = H * 0.7 - ((sma - 70) / 100) * (H * 0.6);
          if (i === 20) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }
    }

    window.addEventListener('load', () => { setTimeout(drawDygraphs, 100); });
    window.addEventListener('resize', drawDygraphs);
    """

    html = render_lang_page("R", "dygraphs (R)", "R Visualization", 'install.packages("dygraphs")',
                            "https://rstudio.github.io/dygraphs/",
                            "High-density financial time series with interactive range selectors.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("dygraphs", html)

# 8. CORRPLOT
def build_corrplot():
    paradigms = [{
        "tag": "01 / MULTIVARIATE CORRELATION MATRIX",
        "title": "Hierarchical Dendrogram Clustering & Elliptical Covariance",
        "subtitle": "Visual exploration of high-dimensional correlation matrices with confidence ellipses and hclust sorting.",
        "math_desc": "Pearson correlation coefficient: $r_{xy} = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sqrt{\\sum (x_i - \\bar{x})^2 \\sum (y_i - \\bar{y})^2}}$ encoded as ellipse eccentricity.",
        "math_formula": "\\text{Eccentricity } e = \\sqrt{1 - \\lambda_2 / \\lambda_1}, \\quad \\lambda_{1,2} = 1 \\pm |r_{xy}|",
        "time_complexity": "O(P^3) for P-variable hierarchical clustering",
        "space_complexity": "O(P^2) covariance storage",
        "enterprise_use": "Credit default swap risk factor cross-correlation, multi-factor quantitative equity portfolio risk.",
        "strengths": "Fastest visual diagnostic for collinearity; intuitive elliptical orientation (45 deg positive, -45 deg negative).",
        "tradeoffs": "Static visual matrix; requires interactive wrapper for drill-down tooltips.",
        "metrics": [
            {"label": "Method", "val": "Ellipse / Circle", "sub": "Eigen Eccentricity"},
            {"label": "Clustering", "val": "hclust (Ward)", "sub": "Dendrogram Order"},
            {"label": "Significance", "val": "p-value crosses", "sub": "alpha = 0.05"},
            {"label": "License", "val": "GPL-2", "sub": "Standard R"}
        ],
        "code": """library(corrplot)

# Multi-factor correlation matrix on mtcars
M <- cor(mtcars)
res1 <- cor.mtest(mtcars, conf.level = 0.95)

# Render publication matrix with hierarchical clustering
corrplot(M, method = "ellipse", type = "upper", order = "hclust",
         tl.col = "#cbd5e1", tl.srt = 45,
         col = colorRampPalette(c("#ff1744", "#050806", "#00e676"))(200),
         p.mat = res1$p, sig.level = 0.05, insig = "blank")"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">CORRPLOT ELLIPSE MATRIX</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="toggleCorrMethod('circle')" style="font-size:0.7rem; padding:3px 8px;">Circle</button>
        <button class="btn-action" onclick="toggleCorrMethod('ellipse')" style="font-size:0.7rem; padding:3px 8px;">Ellipse</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="corr-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>corrplot(M, method='ellipse', order='hclust', type='upper')</span>
      <span>Pearson Covariance Eigen-Decomposition · Bivariate Confidence Ellipse Geometry</span>
    </div>
    """

    custom_js = """
    let corrMethod = 'ellipse';
    function toggleCorrMethod(m) { corrMethod = m; drawCorrplot(); }

    function drawCorrplot() {
      const c = document.getElementById('corr-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const vars = ['Price', 'Volume', 'Beta', 'Volat', 'PE', 'DivYield'];
      const P = vars.length;
      const matrix = [
        [ 1.00,  0.72,  0.45, -0.62,  0.81, -0.34],
        [ 0.72,  1.00,  0.58, -0.41,  0.64, -0.22],
        [ 0.45,  0.58,  1.00, -0.15,  0.32, -0.05],
        [-0.62, -0.41, -0.15,  1.00, -0.55,  0.42],
        [ 0.81,  0.64,  0.32, -0.55,  1.00, -0.28],
        [-0.34, -0.22, -0.05,  0.42, -0.28,  1.00]
      ];

      const size = Math.min(W, H) - 100;
      const ox = (W - size) / 2 + 40;
      const oy = (H - size) / 2 + 40;
      const cell = size / P;

      for (let r = 0; r < P; r++) {
        for (let cl = 0; cl < P; cl++) {
          const val = matrix[r][cl];
          const cx = ox + cl * cell + cell/2;
          const cy = oy + r * cell + cell/2;

          ctx.strokeStyle = 'rgba(255,255,255,0.06)';
          ctx.strokeRect(ox + cl*cell, oy + r*cell, cell, cell);

          if (corrMethod === 'ellipse') {
            ctx.save();
            ctx.translate(cx, cy);
            ctx.rotate(val > 0 ? -Math.PI/4 : Math.PI/4);
            ctx.fillStyle = val > 0 ? '#00e676' : '#ff1744';
            ctx.beginPath();
            ctx.ellipse(0, 0, (cell * 0.4), (cell * 0.4) * (1 - Math.abs(val)), 0, 0, 2*Math.PI);
            ctx.fill();
            ctx.restore();
          } else {
            ctx.fillStyle = val > 0 ? '#00e676' : '#ff1744';
            ctx.beginPath();
            ctx.arc(cx, cy, (cell * 0.4) * Math.abs(val), 0, 2*Math.PI);
            ctx.fill();
          }
        }
      }

      // Labels
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '11px JetBrains Mono';
      for (let i = 0; i < P; i++) {
        ctx.textAlign = 'right';
        ctx.fillText(vars[i], ox - 8, oy + i*cell + cell/2 + 4);
        ctx.textAlign = 'center';
        ctx.fillText(vars[i], ox + i*cell + cell/2, oy - 10);
      }
    }

    window.addEventListener('load', () => { setTimeout(drawCorrplot, 100); });
    window.addEventListener('resize', drawCorrplot);
    """

    html = render_lang_page("R", "corrplot", "R Visualization", 'install.packages("corrplot")',
                            "https://cran.r-project.org/web/packages/corrplot/",
                            "Correlation matrix visual diagnostics and hierarchical clustering.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("corrplot", html)

if __name__ == "__main__":
    build_r_all()
