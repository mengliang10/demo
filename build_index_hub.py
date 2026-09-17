"""
Builder for index.html (Master Executive Portfolio Hub)
in /mnt/storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/
"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_index():
    decks = [
        {
            'series': '01',
            'file': '01-javascript-core-engines.html',
            'title': 'JavaScript Core Engines & General Visualization',
            'category': 'JavaScript Core Engines',
            'cat_slug': 'js-core',
            'desc': '20 distinct visual paradigms across low-level and high-level JavaScript charting libraries. Demonstrates hierarchical partitioning, algorithmic financials, multi-axis polar systems, and high-frequency vector flows.',
            'libs': ['D3.js v7', 'Apache ECharts 5.5', 'Chart.js v4', 'Plotly.js WebGL', 'ApexCharts', 'Vega-Lite', 'Observable Plot', 'Highcharts', 'amCharts 5', 'AntV G2'],
            'highlights': ['Zoomable Sunburst', 'Financial Candlestick + MACD', '3D Parametric Surface', 'Curved Sankey Flow', 'Voronoi Tessellation', '60-FPS Particle Sim']
        },
        {
            'series': '02',
            'file': '02-javascript-timelines-gantt.html',
            'title': 'JavaScript Timelines, Gantt & Temporal Data',
            'category': 'Timelines & Gantt',
            'cat_slug': 'js-temporal',
            'desc': '20 temporal visualization paradigms handling multi-scale time data from millennia down to milliseconds. Demonstrates critical path precedence, resource workload balancing, and rich media narratives.',
            'libs': ['Vis.js Timeline', 'Frappe Gantt', 'DHTMLX Gantt', 'TimelineJS', 'Timelines-Chart', 'AnyChart Gantt', 'CanvasJS', 'D3-Timeline'],
            'highlights': ['Critical Path CPM Gantt', 'Zoomable Multi-Track Axis', 'Circadian 24h Shift Dial', 'Resource Over-Allocation', 'Logarithmic Epoch Scaling', 'Space-Time Cube 3D']
        },
        {
            'series': '03',
            'file': '03-javascript-networks-graphs.html',
            'title': 'JavaScript Networks, Graphs & Node Diagrams',
            'category': 'Networks & Node Graphs',
            'cat_slug': 'js-networks',
            'desc': '20 graph topology paradigms mapping relational systems, knowledge bases, and complex dependencies. Demonstrates force simulations, large-scale WebGL node clusters, and protocol sequence handshakes.',
            'libs': ['Cytoscape.js', 'Sigma.js WebGL', 'Vis.js Network', 'AntV G6', 'Mermaid.js', 'JointJS BPMN', 'GoJS', 'VivaGraphJS'],
            'highlights': ['CoLA Physics Force Graph', '100k Node WebGL Shader', 'Concentric Radial Rings', 'Mermaid Sequence Handshake', 'Bipartite Affiliation', 'Hierarchical Edge Bundling']
        },
        {
            'series': '04',
            'file': '04-javascript-3d-maps-geospatial.html',
            'title': 'JavaScript 3D, Maps & Geospatial Visualization',
            'category': '3D & Geospatial',
            'cat_slug': 'js-geospatial',
            'desc': '20 spatial and 3D paradigms mapping geographic coordinates, extruded urban digital twins, and orbital earth globes. Demonstrates WebGL tile pipelines, isochrone travel contours, and photogrammetry.',
            'libs': ['Three.js r128', 'Deck.gl WebGL2', 'Leaflet.js v1.9', 'Mapbox GL JS', 'CesiumJS WGS84', 'OpenLayers', 'Kepler.gl', 'Turf.js'],
            'highlights': ['3D Earth Digital Globe', 'Extruded Hexagon Columns', '3D Urban Building Twins', 'Intercontinental Flight Arcs', 'Isochrone Travel Contours', '3D Exploded BIM Model']
        },
        {
            'series': '05',
            'file': '05-python-general-statistical.html',
            'title': 'Python General, Statistical & Declarative Visualization',
            'category': 'Python Statistical',
            'cat_slug': 'py-statistical',
            'desc': '20 analytical paradigms across Python statistical, grammar-based, and declarative libraries. Demonstrates bivariate density projections, financial waterfalls, horizon charts, and unsupervised cluster dendrograms.',
            'libs': ['Matplotlib', 'Seaborn', 'Plotly Py', 'Bokeh 3.4', 'Altair (Vega)', 'HoloViews', 'Pygal SVG', 'Chartify (Spotify)', 'Plotnine (ggplot2)', 'HVPlot'],
            'highlights': ['JointGrid Bivariate Marginals', 'Linked Brush SPLOM', 'Faceted Ridgeline Waves', 'Financial P&L Waterfall', 'Clustermap Dendrogram', 'Asymmetric Split Violins']
        },
        {
            'series': '06',
            'file': '06-python-scientific-3d.html',
            'title': 'Python Scientific, 3D & High-Performance Visualization',
            'category': 'Python Scientific & 3D',
            'cat_slug': 'py-scientific',
            'desc': '20 high-performance scientific paradigms handling multi-gigabyte datasets, real-time instrumentation, and volumetric scalar fields. Demonstrates out-of-core aggregation, GPU shaders, and tensor analysis.',
            'libs': ['Datashader (Numba)', 'Mayavi (VTK)', 'VisPy (OpenGL)', 'PyQtGraph (Qt6)', 'VTK C++/Python', 'Glumpy (GLSL)'],
            'highlights': ['10M Point HDR Density', '60-FPS Multi-Channel Scope', 'Marching Cubes Isosurface', 'DICOM Orthogonal Slices', 'Von Mises FEA Stress', 'Diffusion Tensor Ellipsoids']
        },
        {
            'series': '07',
            'file': '07-python-geospatial-mapping.html',
            'title': 'Python Geospatial & Mapping Visualization',
            'category': 'Python Geospatial',
            'cat_slug': 'py-geospatial',
            'desc': '20 spatial cartography paradigms across Python GIS and mapping packages. Demonstrates spatial joins, publication-grade projections, terrain heightmaps, and automated vector GeoJSON pipelines.',
            'libs': ['Folium (Leaflet)', 'GeoPandas (Shapely)', 'Cartopy (UK Met)', 'Geoplotlib (Pyglet)', 'Pydeck (Deck.gl)'],
            'highlights': ['GPU 3D Hexagon Layers', 'GeoPandas Spatial Joins', 'Robinson World Projection', 'Animated Time-Slider Heatmap', 'Value-by-Alpha Uncertainty', '3D DEM Terrain Shading']
        },
        {
            'series': '08',
            'file': '08-python-timelines-networks.html',
            'title': 'Python Timelines, Network & Specialized Visualization',
            'category': 'Python Networks & Timelines',
            'cat_slug': 'py-networks',
            'desc': '20 specialized graph theory and timeline paradigms in Python. Demonstrates physics-based network exploration, CPU concurrency tracking, spectral graph Laplacian embedding, and topological sorting.',
            'libs': ['NetworkX', 'PyVis', 'Matplotlib eventplot', 'Matplotlib broken_barh', 'PyCircos', 'Calplot', 'SciPy Community'],
            'highlights': ['Interactive Physics Graphs', 'Broken Barh Allocation Gantt', 'Bipartite Affiliations', 'Betweenness Centrality Chokepoints', 'Louvain Community Detection', 'Spectral Laplacian Embedding']
        }
    ]

    cards_html = []
    for d in decks:
        libs_pills = "".join([f'<span class="pill-badge">{lib}</span>' for lib in d['libs']])
        hl_items = "".join([f'<li>{h}</li>' for h in d['highlights']])
        
        card = f"""
        <article class="hub-deck-card" data-category="{d['cat_slug']}">
          <div class="card-top-strip">
            <span class="series-tag">Series #{d['series']}</span>
            <span class="cat-tag">{d['category']}</span>
          </div>
          <h2 class="card-title">{d['title']}</h2>
          <p class="card-desc">{d['desc']}</p>
          
          <div class="libs-wrapper">
            <span class="libs-label">Engines Featured:</span>
            <div class="pills-container">
              {libs_pills}
            </div>
          </div>
          
          <div class="highlights-box">
            <strong style="color:var(--viz-gold-bright); font-size:0.85rem; font-family:var(--font-mono); text-transform:uppercase; letter-spacing:0.05em; display:block; margin-bottom:6px;">Sample Visual Paradigms:</strong>
            <ul class="highlights-list">
              {hl_items}
            </ul>
          </div>
          
          <div class="card-footer">
            <span class="slide-badge">20 Master Slides</span>
            <a href="{d['file']}" class="launch-btn">Launch Deck &rarr;</a>
          </div>
        </article>
        """
        cards_html.append(card)

    cards_grid = "\n".join(cards_html)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visualization Software Masterclass Portfolio | Executive Hub</title>
  <meta name="description" content="Comprehensive Executive Demonstration of 50+ JavaScript and Python Data Visualization Software Libraries across 8 Masterclasses and 160 Unique Visual Paradigms.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --viz-bg-dark: #070c09;
      --viz-bg-surface: #0e1713;
      --viz-bg-card: rgba(16, 26, 22, 0.88);
      --viz-gold: #d4af37;
      --viz-gold-bright: #f3cf65;
      --viz-gold-border: rgba(212, 175, 55, 0.35);
      --viz-neon-emerald: #00e676;
      --viz-neon-cyan: #00e5ff;
      --viz-text-light: #fffefa;
      --viz-text-body: #e4ece7;
      --viz-text-muted: #9ba9a1;
      --font-heading: 'Newsreader', Georgia, serif;
      --font-body: 'DM Sans', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: radial-gradient(circle at 50% 10%, #13221b 0%, #070c09 100%);
      color: var(--viz-text-light);
      font-family: var(--font-body);
      line-height: 1.55;
      padding-bottom: 80px;
      min-height: 100vh;
    }}

    /* HEADER */
    .hub-header {{
      border-bottom: 1px solid var(--viz-gold-border);
      padding: 48px 36px 36px;
      background: rgba(11, 19, 15, 0.92);
      backdrop-filter: blur(14px);
    }}
    .hub-header-inner {{
      max-width: 1360px;
      margin: 0 auto;
    }}
    .brand-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      color: var(--viz-gold-bright);
      background: rgba(212, 175, 55, 0.14);
      border: 1px solid var(--viz-gold-border);
      padding: 5px 14px;
      border-radius: 50px;
      margin-bottom: 16px;
    }}
    .hub-title {{
      font-family: var(--font-heading);
      font-size: clamp(2.5rem, 4.5vw, 3.8rem);
      font-weight: 400;
      line-height: 1.1;
      color: #fffefa;
      margin-bottom: 14px;
    }}
    .hub-title span {{
      color: var(--viz-gold-bright);
      font-style: italic;
    }}
    .hub-subtitle {{
      font-size: 1.25rem;
      color: var(--viz-gold);
      font-family: var(--font-heading);
      font-style: italic;
      max-width: 980px;
      margin-bottom: 20px;
    }}
    .hub-desc {{
      font-size: 1.02rem;
      color: var(--viz-text-muted);
      max-width: 1050px;
      line-height: 1.65;
    }}

    /* STATS STRIP */
    .stats-strip {{
      max-width: 1360px;
      margin: 28px auto 0;
      padding: 0 36px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }}
    .stat-box {{
      background: rgba(16, 26, 22, 0.75);
      border: 1px solid var(--viz-gold-border);
      border-top: 2.5px solid var(--viz-gold);
      border-radius: 8px;
      padding: 16px 20px;
      text-align: center;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
    }}
    .stat-val {{
      font-family: var(--font-mono);
      font-size: 2.1rem;
      font-weight: 700;
      color: var(--viz-gold-bright);
      display: block;
      margin-bottom: 4px;
    }}
    .stat-lbl {{
      font-size: 0.85rem;
      color: var(--viz-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}

    /* CONTROLS BAR */
    .controls-bar {{
      max-width: 1360px;
      margin: 32px auto 0;
      padding: 0 36px;
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      justify-content: space-between;
      align-items: center;
    }}
    .search-input {{
      flex: 1;
      min-width: 300px;
      max-width: 480px;
      background: rgba(16, 26, 22, 0.95);
      border: 1px solid var(--viz-gold-border);
      color: #fffefa;
      padding: 12px 20px;
      border-radius: 8px;
      font-family: var(--font-body);
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}
    .search-input:focus {{
      border-color: var(--viz-gold-bright);
      box-shadow: 0 0 15px rgba(212, 175, 55, 0.25);
    }}
    .filter-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .pill-btn {{
      background: rgba(16, 26, 22, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--viz-text-muted);
      padding: 7px 16px;
      border-radius: 50px;
      font-size: 0.84rem;
      cursor: pointer;
      font-weight: 500;
      transition: all 0.2s ease;
    }}
    .pill-btn:hover, .pill-btn.active {{
      background: var(--viz-gold);
      color: #070c09;
      border-color: var(--viz-gold);
      font-weight: 600;
      box-shadow: 0 0 12px rgba(212, 175, 55, 0.35);
    }}

    /* DECK GRID */
    .deck-grid {{
      max-width: 1360px;
      margin: 36px auto 0;
      padding: 0 36px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
      gap: 28px;
    }}
    .hub-deck-card {{
      background: var(--viz-bg-card);
      border: 1px solid var(--viz-gold-border);
      border-top: 3px solid var(--viz-gold);
      border-radius: 12px;
      padding: 26px 28px;
      display: flex;
      flex-direction: column;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
      transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }}
    .hub-deck-card:hover {{
      transform: translateY(-4px);
      border-color: var(--viz-gold-bright);
      box-shadow: 0 22px 50px rgba(0, 0, 0, 0.65), 0 0 20px rgba(212, 175, 55, 0.15);
    }}
    .card-top-strip {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .series-tag {{
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--viz-gold-bright);
      background: rgba(212, 175, 55, 0.16);
      padding: 3px 10px;
      border-radius: 4px;
    }}
    .cat-tag {{
      font-size: 0.76rem;
      color: var(--viz-text-muted);
      background: rgba(255, 255, 255, 0.08);
      padding: 3px 12px;
      border-radius: 50px;
    }}
    .card-title {{
      font-family: var(--font-heading);
      font-size: 1.55rem;
      font-weight: 500;
      color: #fffefa;
      line-height: 1.25;
      margin-bottom: 12px;
    }}
    .card-desc {{
      font-size: 0.94rem;
      color: #cde4d8;
      line-height: 1.55;
      margin-bottom: 18px;
      flex-grow: 1;
    }}
    
    .libs-wrapper {{
      margin-bottom: 16px;
    }}
    .libs-label {{
      font-family: var(--font-mono);
      font-size: 0.76rem;
      text-transform: uppercase;
      color: var(--viz-gold-bright);
      letter-spacing: 0.06em;
      display: block;
      margin-bottom: 6px;
    }}
    .pills-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .pill-badge {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: var(--viz-text-body);
      font-family: var(--font-mono);
      font-size: 0.74rem;
      padding: 2px 8px;
      border-radius: 4px;
    }}

    .highlights-box {{
      background: rgba(7, 12, 9, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 6px;
      padding: 12px 16px;
      margin-bottom: 20px;
    }}
    .highlights-list {{
      padding-left: 18px;
      font-size: 0.86rem;
      color: var(--viz-text-muted);
      line-height: 1.5;
    }}
    .highlights-list li {{
      margin-bottom: 3px;
    }}

    .card-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .slide-badge {{
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--viz-neon-emerald);
      font-weight: 600;
    }}
    .launch-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(212, 175, 55, 0.18);
      border: 1px solid var(--viz-gold);
      color: #fffefa;
      padding: 9px 22px;
      border-radius: 50px;
      font-size: 0.88rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
    }}
    .launch-btn:hover {{
      background: var(--viz-gold);
      color: #070c09;
      box-shadow: 0 0 16px rgba(212, 175, 55, 0.4);
    }}

    /* MATRIX SECTION */
    .matrix-section {{
      max-width: 1360px;
      margin: 60px auto 0;
      padding: 0 36px;
    }}
    .section-title {{
      font-family: var(--font-heading);
      font-size: 2.2rem;
      color: #fffefa;
      margin-bottom: 8px;
    }}
    .section-title span {{
      color: var(--viz-gold-bright);
      font-style: italic;
    }}
    .section-desc {{
      font-size: 0.96rem;
      color: var(--viz-text-muted);
      margin-bottom: 24px;
    }}
    .matrix-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
      background: rgba(16, 26, 22, 0.8);
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--viz-gold-border);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
    }}
    .matrix-table th {{
      background: #14241c;
      color: var(--viz-gold-bright);
      padding: 14px 18px;
      text-align: left;
      font-family: var(--font-heading);
      font-size: 1.15rem;
      border-bottom: 1px solid var(--viz-gold-border);
    }}
    .matrix-table td {{
      padding: 12px 18px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      color: var(--viz-text-body);
    }}
    .matrix-table tr:nth-child(even) td {{
      background: rgba(11, 19, 15, 0.5);
    }}

    /* FOOTER */
    .hub-footer {{
      margin-top: 80px;
      text-align: center;
      font-size: 0.88rem;
      color: var(--viz-text-muted);
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      padding-top: 30px;
    }}
  </style>

  <script>
    function filterDecks() {{
      const query = document.getElementById('searchInput').value.toLowerCase();
      const cards = document.querySelectorAll('.hub-deck-card');
      cards.forEach(card => {{
        const text = card.innerText.toLowerCase();
        if (text.includes(query)) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    function filterCategory(catSlug, btn) {{
      document.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cards = document.querySelectorAll('.hub-deck-card');
      cards.forEach(card => {{
        if (catSlug === 'all' || card.getAttribute('data-category') === catSlug) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>
</head>
<body>

  <!-- HEADER -->
  <header class="hub-header">
    <div class="hub-header-inner">
      <span class="brand-badge">Demostration of Visualization Software &bull; Executive Suite</span>
      <h1 class="hub-title">Visualization Software <span>Masterclass Portfolio</span></h1>
      <p class="hub-subtitle">8 Specialized Masterclasses &bull; 160 Unique Visual Paradigms &bull; 50+ Modern JavaScript & Python Graphics Engines</p>
      <p class="hub-desc">
        A comprehensive, multi-disciplinary showcase designed for data engineers, commercial leaders, quantitative researchers, and software architects. Each presentation deck contains 20 fully-developed slides demonstrating distinct visual styles, algorithmic foundations, mathematical formulations, and live executable rendering engines.
      </p>
    </div>
  </header>

  <!-- STATS STRIP -->
  <section class="stats-strip">
    <div class="stat-box">
      <span class="stat-val">8 Decks</span>
      <span class="stat-lbl">Masterclasses</span>
    </div>
    <div class="stat-box">
      <span class="stat-val">160 Slides</span>
      <span class="stat-lbl">Unique Paradigms</span>
    </div>
    <div class="stat-box">
      <span class="stat-val">50+ Engines</span>
      <span class="stat-lbl">JS & Python Libs</span>
    </div>
    <div class="stat-box">
      <span class="stat-val">60 FPS WebGL</span>
      <span class="stat-lbl">Interactive Speed</span>
    </div>
  </section>

  <!-- CONTROLS -->
  <section class="controls-bar">
    <input type="text" id="searchInput" class="search-input" placeholder="Search 160 visual paradigms, libraries (D3, ECharts, Bokeh...)..." oninput="filterDecks()">
    <div class="filter-pills">
      <button class="pill-btn active" onclick="filterCategory('all', this)">All (8)</button>
      <button class="pill-btn" onclick="filterCategory('js-core', this)">JS Core Engines</button>
      <button class="pill-btn" onclick="filterCategory('js-temporal', this)">Timelines & Gantt</button>
      <button class="pill-btn" onclick="filterCategory('js-networks', this)">Networks & Graphs</button>
      <button class="pill-btn" onclick="filterCategory('js-geospatial', this)">3D & Geospatial</button>
      <button class="pill-btn" onclick="filterCategory('py-statistical', this)">Python Statistical</button>
      <button class="pill-btn" onclick="filterCategory('py-scientific', this)">Python Scientific</button>
      <button class="pill-btn" onclick="filterCategory('py-geospatial', this)">Python Geospatial</button>
      <button class="pill-btn" onclick="filterCategory('py-networks', this)">Python Networks</button>
    </div>
  </section>

  <!-- DECK GRID -->
  <main class="deck-grid" id="deckGrid">
{cards_grid}
  </main>

  <!-- SOFTWARE CAPABILITIES MATRIX -->
  <section class="matrix-section">
    <h3 class="section-title">Comprehensive <span>Software Capability Matrix</span></h3>
    <p class="section-desc">Technical breakdown across rendering backends, primary mathematical domains, and rendering performance.</p>
    <table class="matrix-table">
      <thead>
        <tr>
          <th>Category</th>
          <th>Representative Libraries</th>
          <th>Primary Rendering Backend</th>
          <th>Data Capacity</th>
          <th>Primary Analytical Domain</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:var(--viz-gold-bright);">JS Core Engines</strong></td>
          <td>D3.js, ECharts, Plotly, Chart.js, Vega, ApexCharts, amCharts</td>
          <td>Canvas 2D, SVG, WebGL</td>
          <td>1,000 to 100,000 Nodes</td>
          <td>Executive Dashboards, Financials, Sunbursts, Radars</td>
        </tr>
        <tr>
          <td><strong style="color:var(--viz-gold-bright);">Timelines & Temporal</strong></td>
          <td>Vis.js Timeline, Frappe, DHTMLX, TimelineJS, CanvasJS</td>
          <td>DOM Windowing, Canvas 2D, SVG</td>
          <td>Sub-ms to Millennia</td>
          <td>Project Gantt, Resource Leveling, Audit Logs, Flight Boards</td>
        </tr>
        <tr>
          <td><strong style="color:var(--viz-gold-bright);">Networks & Graphs</strong></td>
          <td>Cytoscape, Sigma.js, Vis.js Network, AntV G6, Mermaid</td>
          <td>WebGL Shaders, HTML5 Canvas</td>
          <td>10,000 to 500,000 Nodes</td>
          <td>Knowledge Graphs, Microservices, Cyber Attack Trees, MST</td>
        </tr>
        <tr>
          <td><strong style="color:var(--viz-gold-bright);">3D & Geospatial</strong></td>
          <td>Three.js, Deck.gl, Leaflet, Mapbox GL, CesiumJS, OpenLayers</td>
          <td>WebGL2, WGS84 Ellipsoid</td>
          <td>Millions of GPS Vertices</td>
          <td>3D Planetary Earth, Urban Twins, Isochrones, LiDAR Scans</td>
        </tr>
        <tr>
          <td><strong style="color:var(--viz-gold-bright);">Python Statistical</strong></td>
          <td>Matplotlib, Seaborn, Bokeh, Altair, HoloViews, Plotnine</td>
          <td>Matplotlib C++, BokehJS, Vega JSON</td>
          <td>Medium to Large DataFrames</td>
          <td>Bivariate KDE, P&L Waterfalls, Joyplots, Split Violins</td>
        </tr>
        <tr>
          <td><strong style="color:var(--viz-gold-bright);">Python Scientific & 3D</strong></td>
          <td>Datashader, Mayavi, VisPy, PyQtGraph, VTK, Glumpy</td>
          <td>Numba JIT, OpenGL ES, C++ VTK</td>
          <td>10M to 1B+ Points</td>
          <td>Medical DICOM, FEA Stress Tensors, 60 FPS Streams</td>
        </tr>
        <tr>
          <td><strong style="color:var(--viz-gold-bright);">Python Geospatial</strong></td>
          <td>Folium, GeoPandas, Cartopy, Geoplotlib, Pydeck</td>
          <td>GEOS C++, GDAL, Leaflet, Deck.gl</td>
          <td>Vector Shp, GeoJSON, Parquet</td>
          <td>Spatial Joins, Robinson Maps, Bivariate Chloropleths</td>
        </tr>
        <tr>
          <td><strong style="color:var(--viz-gold-bright);">Python Networks</strong></td>
          <td>NetworkX, PyVis, Matplotlib Eventplot, Calplot, PyCircos</td>
          <td>Graph C++, Vis.js Dynamic Engine</td>
          <td>Large Topology Graphs</td>
          <td>Betweenness Centrality, DAG Schedulers, Circos Chords</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- KEYBOARD SHORTCUTS GUIDE -->
  <section class="matrix-section" style="margin-top:40px;">
    <div style="background:rgba(16,26,22,0.85); border:1px solid var(--viz-gold-border); border-radius:8px; padding:24px 30px; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <h4 style="font-family:var(--font-heading); font-size:1.4rem; color:var(--viz-gold-bright); margin-bottom:6px;">Keyboard Presentation Shortcuts</h4>
        <p style="font-size:0.92rem; color:var(--viz-text-muted);">When viewing any of the 8 Reveal.js masterclasses:</p>
      </div>
      <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:0.85rem;">
        <div><strong style="color:#00e676;">[Space] / [&rarr;]</strong> Advance</div>
        <div><strong style="color:#00e676;">[&larr;]</strong> Back</div>
        <div><strong style="color:#f3cf65;">[F]</strong> Fullscreen</div>
        <div><strong style="color:#00e5ff;">[O] / [Esc]</strong> Slide Overview</div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="hub-footer">
    <p>Demostration of Visualization Software &bull; Executive Data Science & Graphic Systems Masterclasses</p>
    <p style="margin-top:6px; color:var(--viz-gold); font-family:var(--font-mono); font-size:0.8rem;">All 8 Presentations Built with Reveal.js &bull; 160 Unique Visual Paradigms</p>
  </footer>

</body>
</html>
"""
    out_path = os.path.join(SCRIPT_DIR, "index.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Built Master Hub: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    build_index()
