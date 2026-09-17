"""
Shared template engine for generating 20-slide Reveal.js masterclass decks.
"""

def generate_deck_html(deck_meta, slides, extra_head_scripts=""):
    """
    deck_meta: {
        'id': 'deck-01',
        'series_num': '01',
        'title': '...',
        'category': '...',
        'subtitle': '...',
        'prev_deck': '...',
        'next_deck': '...'
    }
    slides: list of 20 dicts:
        {
            'slide_id': 'slide-01',
            'tag': '01 / Sunburst Flow',
            'headline': '...',
            'headline_span': '...',
            'subtitle': '...',
            'library_badge': 'D3.js v7',
            'chart_html': '...', # HTML element or container with live JS
            'specs': [
                {'title': 'Mathematical Engine', 'desc': '...'},
                {'title': 'Enterprise Use Cases', 'desc': '...'},
                {'title': 'Technical Strengths', 'desc': '...'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'SVG / DOM', 'sub': 'Vector Scale'},
                {'label': 'Max Nodes', 'val': '10,000+', 'sub': '60 FPS Target'},
                {'label': 'Interaction', 'val': 'Zoom / Drill', 'sub': 'Event Driven'},
                {'label': 'License', 'val': 'ISC / Open', 'sub': 'Enterprise Safe'}
            ],
            'code_snippet': '...' # optional python/JS snippet
        }
    """
    
    slides_html = []
    
    for s in slides:
        specs_html = "".join([f"""
          <div class="spec-card">
            <h5>{spec['title']}</h5>
            <p>{spec['desc']}</p>
          </div>
        """ for spec in s.get('specs', [])])
        
        metrics_html = "".join([f"""
          <div class="metric-pill">
            <span class="lbl">{m['label']}</span>
            <span class="val">{m['val']}</span>
            <span class="sub">{m['sub']}</span>
          </div>
        """ for m in s.get('metrics', [])])
        
        code_box_html = ""
        if s.get('code_snippet'):
            code_box_html = f"""
          <div class="code-box" style="margin-top: 10px;">
            <pre style="margin: 0;"><code>{s['code_snippet']}</code></pre>
          </div>
            """
            
        slide_markup = f"""
      <section id="{s['slide_id']}" data-transition="fade">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
          <div>
            <span class="slide-tag">{s['tag']}</span>
            <h2 class="slide-headline">{s['headline']} <span>{s['headline_span']}</span></h2>
            <p class="slide-subtitle">{s['subtitle']}</p>
          </div>
          <div style="text-align: right; padding-top: 4px;">
            <span class="tech-badge">{s['library_badge']}</span>
          </div>
        </div>
        
        <div class="viz-stage-split">
          <div class="viz-canvas-container" id="container-{s['slide_id']}">
            {s['chart_html']}
          </div>
          <div class="viz-info-panel">
            {specs_html}
            {code_box_html}
            <div class="metrics-strip">
              {metrics_html}
            </div>
          </div>
        </div>
      </section>
        """
        slides_html.append(slide_markup)
        
    all_slides_content = "\n".join(slides_html)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{deck_meta['title']} | Visualization Masterclass</title>
  <meta name="description" content="{deck_meta['subtitle']}">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Reveal.js Core CSS -->
  <link rel="stylesheet" href="vendor/reveal.min.css" onerror="this.href='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.css'">
  <link rel="stylesheet" href="css/viz-deck.css">
  
  <!-- Visualization Engines -->
  <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
  <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.28.1/cytoscape.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
  {extra_head_scripts}
  
  <script>
    if (window.mermaid) {{
      mermaid.initialize({{
        startOnLoad: true,
        theme: 'dark',
        themeVariables: {{
          darkMode: true,
          background: '#070c09',
          primaryColor: '#13221b',
          primaryTextColor: '#fffefa',
          primaryBorderColor: '#d4af37',
          lineColor: '#f3cf65',
          fontFamily: 'DM Sans',
          fontSize: '15px'
        }}
      }});
    }}
  </script>
</head>
<body>

  <!-- PERSISTENT TOP NAVIGATION -->
  <div class="deck-nav-bar">
    <div style="display: flex; align-items: center; gap: 16px;">
      <a href="index.html">
        <span aria-hidden="true">&larr;</span> <strong>Visualization Portfolio Hub</strong>
      </a>
      <span style="opacity: 0.4;">|</span>
      <span style="font-family: var(--font-mono); font-size: 0.88rem; color: var(--viz-gold-bright);">Series #{deck_meta['series_num']}</span>
      <span style="opacity: 0.4;">|</span>
      <span style="color: #fffefa; font-weight: 500; font-family: var(--font-heading); font-size: 1.2rem;">{deck_meta['title']}</span>
    </div>
    <div style="display: flex; align-items: center; gap: 12px;">
      <span class="tech-badge">{deck_meta['category']}</span>
      <span style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--viz-text-muted);">20 Master Slides</span>
    </div>
  </div>

  <!-- PERSISTENT FOOTER BAR -->
  <div class="deck-footer-bar">
    <span><strong>Demostration of Visualization Software</strong> &bull; Executive Data Science & Graphic Systems</span>
    <span>Use <strong>Space / Arrows</strong> to Navigate &bull; Press <strong>F</strong> for Fullscreen &bull; <strong>O</strong> for Overview</span>
  </div>

  <div class="reveal">
    <div class="slides">
{all_slides_content}
    </div>
  </div>

  <!-- Reveal.js & Dynamic Resize Engine -->
  <script src="vendor/reveal.min.js" onerror="this.src='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.js'"></script>
  <script>
    Reveal.initialize({{
      hash: true,
      slideNumber: 'c/t',
      controls: true,
      progress: true,
      center: false,
      overview: true,
      width: 1400,
      height: 860,
      margin: 0.03,
      minScale: 0.2,
      maxScale: 2.0,
      transition: 'fade',
      backgroundTransition: 'fade'
    }});

    // Universal auto-resize hook for Plotly, ECharts, Leaflet, Three.js, etc.
    Reveal.on('slidechanged', event => {{
      const current = event.currentSlide;
      
      // Plotly resize
      const plotlyGraphs = current.querySelectorAll('.plotly-graph');
      plotlyGraphs.forEach(graph => {{
        if (window.Plotly && graph._fullLayout) {{
          Plotly.Plots.resize(graph);
        }}
      }});
      
      // ECharts resize
      const echartsContainers = current.querySelectorAll('.echarts-chart');
      echartsContainers.forEach(container => {{
        if (window.echarts) {{
          const inst = echarts.getInstanceByDom(container);
          if (inst) inst.resize();
        }}
      }});

      // Leaflet resize
      const leafletMaps = current.querySelectorAll('.leaflet-map');
      leafletMaps.forEach(mapContainer => {{
        if (mapContainer._leaflet_map) {{
          mapContainer._leaflet_map.invalidateSize();
        }}
      }});

      // Re-trigger Mermaid if present
      if (window.mermaid) {{
        const mermaids = current.querySelectorAll('.mermaid');
        if (mermaids.length > 0) {{
          mermaid.run({{ nodes: mermaids }});
        }}
      }}
    }});
  </script>
</body>
</html>
"""
    return html
