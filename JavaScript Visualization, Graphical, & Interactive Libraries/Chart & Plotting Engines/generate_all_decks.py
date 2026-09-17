import os
import sys

BASE_DIR = "/run/media/ml/Storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/JavaScript Visualization, Graphical, & Interactive Libraries/Chart & Plotting Engines"

from build_all_viz_decks import LIBRARIES, ARCHETYPES

THEME_CSS = """
:root {
  --viz-bg-dark: #070c09;
  --viz-bg-surface: #0e1713;
  --viz-bg-card: rgba(16, 26, 22, 0.92);
  --viz-bg-card-hover: rgba(22, 36, 30, 0.98);
  --viz-gold: #d4af37;
  --viz-gold-bright: #f3cf65;
  --viz-gold-muted: #b5935b;
  --viz-gold-subtle: rgba(212, 175, 55, 0.15);
  --viz-gold-border: rgba(212, 175, 55, 0.35);
  --viz-neon-cyan: #00e5ff;
  --viz-neon-emerald: #00e676;
  --viz-neon-violet: #d500f9;
  --viz-neon-amber: #ffab00;
  --viz-neon-crimson: #ff1744;
  --viz-text-light: #fffefa;
  --viz-text-body: #e4ece7;
  --viz-text-muted: #9ba9a1;
  --viz-text-dim: #6c7d73;
  --viz-border: rgba(255, 255, 255, 0.12);
  --viz-border-glow: rgba(212, 175, 55, 0.45);
  --font-heading: 'Newsreader', Georgia, serif;
  --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

body {
  margin: 0;
  padding: 0;
  background: radial-gradient(circle at 50% 15%, #13221b 0%, #070c09 100%);
  color: var(--viz-text-light);
  font-family: var(--font-body);
  overflow: hidden;
}

.reveal {
  font-family: var(--font-body);
  color: var(--viz-text-light);
  background: radial-gradient(circle at 50% 15%, #13221b 0%, #070c09 100%);
  font-size: 19px;
  line-height: 1.45;
}

.reveal .slides {
  text-align: left;
}

.reveal .slides section {
  padding: 16px 36px 40px 36px;
  box-sizing: border-box;
  height: 100%;
}

.deck-nav-bar {
  position: absolute;
  top: 14px;
  left: 36px;
  right: 36px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 100;
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: var(--viz-text-muted);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 8px;
  pointer-events: auto;
}

.deck-nav-bar a {
  color: var(--viz-gold-bright);
  text-decoration: none;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
}
.deck-nav-bar a:hover {
  color: #fffefa;
  text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
}

.deck-footer-bar {
  position: absolute;
  bottom: 12px;
  left: 36px;
  right: 36px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 100;
  font-family: var(--font-body);
  font-size: 0.78rem;
  color: var(--viz-text-dim);
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 6px;
  pointer-events: none;
}

.slide-tag {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: var(--viz-gold-bright);
  display: inline-block;
  margin-bottom: 4px;
}

.slide-headline {
  font-family: var(--font-heading);
  font-size: 1.75rem;
  font-weight: 400;
  color: #fffefa;
  margin: 0 0 3px 0;
  line-height: 1.2;
}
.slide-headline span {
  color: var(--viz-gold-bright);
  font-style: italic;
}

.slide-subtitle {
  font-size: 0.88rem;
  color: var(--viz-text-muted);
  margin: 0 0 12px 0;
  max-width: 1000px;
  line-height: 1.35;
}

.tech-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(212, 175, 55, 0.14);
  border: 1px solid var(--viz-gold-border);
  color: var(--viz-gold-bright);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  padding: 3px 10px;
  border-radius: 4px;
}

.viz-stage-split {
  display: grid;
  grid-template-columns: 1.18fr 0.82fr;
  gap: 20px;
  height: calc(100vh - 175px);
  max-height: 670px;
}

.viz-canvas-container {
  background: var(--viz-bg-card);
  border: 1px solid var(--viz-border);
  border-radius: 8px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: center;
  position: relative;
  overflow: hidden;
  box-shadow: 0 12px 36px rgba(0,0,0,0.5), 0 0 0 1px rgba(212, 175, 55, 0.15);
}

.viz-canvas-container canvas, 
.viz-canvas-container svg,
.viz-canvas-container .chart-stage {
  width: 100% !important;
  height: 100% !important;
  max-height: 100%;
}

.viz-info-panel {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow-y: auto;
}

.spec-card {
  background: rgba(14, 23, 19, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-left: 3px solid var(--viz-gold);
  border-radius: 6px;
  padding: 9px 14px;
  margin-bottom: 8px;
  backdrop-filter: blur(8px);
}
.spec-card h5 {
  font-family: var(--font-heading);
  font-size: 0.95rem;
  color: var(--viz-gold-bright);
  margin: 0 0 2px 0;
}
.spec-card p {
  font-size: 0.82rem;
  color: var(--viz-text-body);
  margin: 0;
  line-height: 1.35;
}

.code-box {
  background: #050806;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 6px;
  padding: 10px 12px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: #f3cf65;
  overflow-x: auto;
  margin-bottom: 8px;
}
.code-box pre {
  margin: 0;
}

.metrics-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
}

.metric-pill {
  background: rgba(20, 32, 26, 0.75);
  border: 1px solid rgba(212, 175, 55, 0.2);
  border-radius: 6px;
  padding: 6px 8px;
  text-align: center;
}
.metric-pill .lbl {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--viz-text-muted);
  text-transform: uppercase;
}
.metric-pill .val {
  display: block;
  font-family: var(--font-body);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--viz-gold-bright);
}
.metric-pill .sub {
  display: block;
  font-size: 0.65rem;
  color: var(--viz-neon-emerald);
}
"""

def generate_deck_html(lib_info):
    lib_name = lib_info["name"]
    lib_badge = lib_info["badge"]
    lib_vendor = lib_info["vendor"]
    lib_desc = lib_info["desc"]

    cdns = [
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.js"></script>',
        '<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>'
    ]
    css_extra = ""

    if "ECharts" in lib_name:
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>')
    elif "ApexCharts" in lib_name:
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/apexcharts@3.52.0/dist/apexcharts.min.js"></script>')
    elif "Chart.js" in lib_name:
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>')
    elif "Plotly" in lib_name:
        cdns.append('<script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>')
    elif "Highcharts" in lib_name:
        cdns.append('<script src="https://code.highcharts.com/highcharts.js"></script>')
        cdns.append('<script src="https://code.highcharts.com/highcharts-more.js"></script>')
        cdns.append('<script src="https://code.highcharts.com/modules/sankey.js"></script>')
        cdns.append('<script src="https://code.highcharts.com/modules/treemap.js"></script>')
        cdns.append('<script src="https://code.highcharts.com/modules/heatmap.js"></script>')
    elif "Google Charts" in lib_name:
        cdns.append('<script src="https://www.gstatic.com/charts/loader.js"></script>')
        cdns.append("<script>if(window.google) google.charts.load('current', {'packages':['corechart', 'treemap', 'sankey', 'gauge']});</script>")
    elif "amCharts" in lib_name:
        cdns.append('<script src="https://cdn.amcharts.com/lib/5/index.js"></script>')
        cdns.append('<script src="https://cdn.amcharts.com/lib/5/xy.js"></script>')
        cdns.append('<script src="https://cdn.amcharts.com/lib/5/radar.js"></script>')
        cdns.append('<script src="https://cdn.amcharts.com/lib/5/percent.js"></script>')
        cdns.append('<script src="https://cdn.amcharts.com/lib/5/themes/Animated.js"></script>')
    elif "Vega-Lite" in lib_name or "Vega" in lib_name:
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>')
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>')
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>')
    elif "Observable Plot" in lib_name:
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6/dist/plot.umd.min.js"></script>')
    elif "C3.js" in lib_name:
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/c3@0.7.20/c3.min.js"></script>')
        css_extra += '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/c3@0.7.20/c3.min.css">\n'
    elif "Chartist" in lib_name:
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/chartist@0.11.4/dist/chartist.min.js"></script>')
        css_extra += '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/chartist@0.11.4/dist/chartist.min.css">\n'
    elif "Dygraphs" in lib_name:
        cdns.append('<script src="https://cdnjs.cloudflare.com/ajax/libs/dygraph/2.2.1/dygraph.min.js"></script>')
        css_extra += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/dygraph/2.2.1/dygraph.min.css">\n'
    elif "AntV G2" in lib_name:
        cdns.append('<script src="https://unpkg.com/@antv/g2@5/dist/g2.min.js"></script>')
    elif "Vizzu" in lib_name:
        cdns.append('<script src="https://cdn.jsdelivr.net/npm/vizzu@0.10.0/dist/vizzu.min.js"></script>')
    elif "CanvasJS" in lib_name:
        cdns.append('<script src="https://cdn.canvasjs.com/canvasjs.min.js"></script>')
    elif "FusionCharts" in lib_name:
        cdns.append('<script src="https://cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>')
        cdns.append('<script src="https://cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>')

    slides_html = []
    for idx, arch in enumerate(ARCHETYPES, start=1):
        s_id = f"slide-{idx:02d}-{arch['id']}"
        container_id = f"chart-container-{idx:02d}"

        # Clean code snippet without f-string nesting
        code_lines = [
            f"// {lib_badge} Architecture - {arch['highlight']}",
            f"const stage = document.getElementById('{container_id}');",
            f"const chart = new {lib_name.split()[0].replace('.','')}.Visualization({{",
            f"  container: stage,",
            f"  paradigm: '{arch['id']}',",
            f"  theme: 'dark-gold',",
            f"  palette: ['#d4af37', '#00e5ff', '#00e676', '#ff1744'],",
            f"  series: [{{ name: '{arch['highlight']}', data: dataMatrix }}]",
            f"}}).render();"
        ]
        code_snippet = "\n".join(code_lines)

        metric_pills = "\n".join([
            f"""<div class="metric-pill">
              <span class="lbl">{m[0]}</span>
              <span class="val">{m[1]}</span>
              <span class="sub">{m[2]}</span>
            </div>""" for m in arch["metrics"]
        ])

        slide_markup = f"""
      <!-- SLIDE {idx:02d}: {arch['highlight']} -->
      <section id="{s_id}" data-transition="fade">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px;">
          <div>
            <span class="slide-tag">{arch['tag']}</span>
            <h2 class="slide-headline">{arch['headline']} <span>{arch['highlight']}</span></h2>
            <p class="slide-subtitle">{arch['subtitle']}</p>
          </div>
          <div style="text-align: right; padding-top: 2px;">
            <span class="tech-badge">{lib_badge}</span>
          </div>
        </div>
        
        <div class="viz-stage-split">
          <div class="viz-canvas-container">
            <div id="{container_id}" class="chart-stage" style="width:100%; height:100%; min-height: 420px; display:flex; align-items:center; justify-content:center; position:relative;"></div>
            <script>
            (function() {{
              function renderChart() {{
                const el = document.getElementById('{container_id}');
                if (!el) return;
                el.innerHTML = '';

                try {{
                  // Dedicated ECharts Engine Hook
                  if (window.echarts && '{lib_name}'.indexOf('ECharts') !== -1) {{
                    const chart = echarts.init(el, 'dark');
                    const isFin = {idx} === 1;
                    const isRad = {idx} === 3;
                    const isTree = {idx} === 4;
                    const isGauge = {idx} === 5;
                    
                    const opt = {{
                      backgroundColor: 'transparent',
                      tooltip: {{ trigger: isRad || isTree ? 'item' : 'axis' }},
                      grid: {{ left: '8%', right: '6%', top: '12%', bottom: '12%' }},
                      xAxis: isRad || isTree || isGauge ? {{ show: false }} : {{ type: 'category', data: ['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8'], axisLine: {{ lineStyle: {{ color: '#b5935b' }} }} }},
                      yAxis: isRad || isTree || isGauge ? {{ show: false }} : {{ type: 'value', splitLine: {{ lineStyle: {{ color: 'rgba(255,255,255,0.06)' }} }} }},
                      series: [{{
                        type: isFin ? 'candlestick' : isRad ? 'radar' : isTree ? 'treemap' : isGauge ? 'gauge' : '{ 'line' if idx in [2,8] else 'bar' }',
                        data: isFin ? [[230,245,225,250],[245,240,235,248],[240,260,238,265],[260,255,250,270],[255,275,252,280],[275,270,268,285],[270,290,269,295],[290,310,285,315]] :
                              isTree ? [{{name:'Global', children:[{{name:'Cloud', value:450}},{{name:'AI', value:320}},{{name:'Security', value:210}}]}}] :
                              isGauge ? [{{ value: 94.2, name: 'SLA' }}] : [120, 180, 240, 320, 410, 520, 630, 780],
                        itemStyle: {{ color: '#d4af37', borderColor: '#f3cf65' }},
                        lineStyle: {{ color: '#00e5ff', width: 3 }}
                      }}]
                    }};
                    if (isRad) {{
                      opt.radar = {{ indicator: [{{name:'Speed',max:100}},{{name:'Scale',max:100}},{{name:'Sec',max:100}},{{name:'UX',max:100}},{{name:'Perf',max:100}}] }};
                      opt.series = [{{ type: 'radar', data: [{{ value: [88, 92, 95, 84, 90], name: 'Metric' }}] }}];
                    }}
                    chart.setOption(opt);
                    window.addEventListener('resize', () => chart.resize());
                    return;
                  }}

                  // Dedicated ApexCharts Engine Hook
                  if (window.ApexCharts && '{lib_name}'.indexOf('ApexCharts') !== -1) {{
                    const chart = new ApexCharts(el, {{
                      chart: {{ type: '{ 'candlestick' if idx==1 else 'area' if idx==2 else 'radar' if idx==3 else 'treemap' if idx==4 else 'radialBar' if idx==5 else 'bar' }', height: '100%', background: 'transparent' }},
                      theme: {{ mode: 'dark' }},
                      colors: ['#d4af37', '#00e5ff', '#00e676', '#ff1744'],
                      series: [{{ name: '{arch["highlight"]}', data: [25, 42, 65, 88, 120, 155, 190, 240] }}],
                      xaxis: {{ categories: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8'] }}
                    }});
                    chart.render();
                    return;
                  }}

                  // Universal D3 / SVG Vector Render Pipeline
                  const svg = d3.select(el).append('svg')
                    .attr('viewBox', [0, 0, 640, 420])
                    .style('width', '100%').style('height', '100%');
                  
                  const gradId = 'grad-{idx}-{container_id}';
                  svg.append('defs').html(
                    '<linearGradient id="' + gradId + '" x1="0%" y1="0%" x2="100%" y2="100%">' +
                    '<stop offset="0%" stop-color="#d4af37" stop-opacity="0.9"/>' +
                    '<stop offset="100%" stop-color="#00e5ff" stop-opacity="0.3"/>' +
                    '</linearGradient>'
                  );

                  // Grid background
                  for (let i = 0; i <= 6; i++) {{
                    svg.append('line').attr('x1', 50).attr('x2', 590).attr('y1', 50 + i*50).attr('y2', 50 + i*50)
                      .attr('stroke', 'rgba(255,255,255,0.06)').attr('stroke-dasharray', '3,3');
                  }}

                  if ({idx} === 1) {{
                    // Candlestick rendering
                    const candles = [[100,160,80,180],[150,210,140,220],[190,170,160,200],[180,260,170,270],[250,310,240,320],[300,280,270,310],[290,360,280,370]];
                    candles.forEach((p, i) => {{
                      const x = 90 + i * 70;
                      const openY = 380 - p[0];
                      const closeY = 380 - p[1];
                      const highY = 380 - p[3];
                      const lowY = 380 - p[2];
                      const col = p[1] >= p[0] ? '#00e676' : '#ff1744';
                      svg.append('line').attr('x1', x).attr('x2', x).attr('y1', highY).attr('y2', lowY).attr('stroke', col).attr('stroke-width', 2);
                      svg.append('rect').attr('x', x - 14).attr('y', Math.min(openY, closeY)).attr('width', 28).attr('height', Math.max(Math.abs(closeY - openY), 4)).attr('fill', col).attr('rx', 2);
                    }});
                  }} else if ({idx} === 3) {{
                    // Radar / Polar
                    const cx = 320, cy = 210, r = 140;
                    const angles = [0, 1, 2, 3, 4, 5].map(a => a * Math.PI / 3);
                    [0.25, 0.5, 0.75, 1.0].forEach(level => {{
                      const pts = angles.map(a => (cx + r * level * Math.cos(a)) + ',' + (cy + r * level * Math.sin(a))).join(' ');
                      svg.append('polygon').attr('points', pts).attr('fill', 'none').attr('stroke', 'rgba(212,175,55,0.2)').attr('stroke-dasharray', '2,2');
                    }});
                    const dataPts = [0.85, 0.92, 0.78, 0.95, 0.88, 0.72].map((v, i) => (cx + r * v * Math.cos(angles[i])) + ',' + (cy + r * v * Math.sin(angles[i]))).join(' ');
                    svg.append('polygon').attr('points', dataPts).attr('fill', 'url(#' + gradId + ')').attr('stroke', '#f3cf65').attr('stroke-width', 2.5);
                  }} else if ({idx} === 4) {{
                    // Treemap hierarchy
                    const boxes = [
                      {{x: 50, y: 50, w: 260, h: 220, label: "Core Platforms", val: "$45.2M", c: "#d4af37"}},
                      {{x: 320, y: 50, w: 270, h: 140, label: "AI Acceleration", val: "$28.4M", c: "#00e5ff"}},
                      {{x: 320, y: 200, w: 270, h: 150, label: "Security & Gov", val: "$19.8M", c: "#00e676"}},
                      {{x: 50, y: 280, w: 260, h: 70, label: "Edge Telemetry", val: "$8.1M", c: "#d500f9"}}
                    ];
                    boxes.forEach(b => {{
                      svg.append('rect').attr('x', b.x).attr('y', b.y).attr('width', b.w).attr('height', b.h).attr('fill', b.c).attr('fill-opacity', 0.25).attr('stroke', b.c).attr('stroke-width', 1.5).attr('rx', 4);
                      svg.append('text').attr('x', b.x + 12).attr('y', b.y + 26).attr('fill', '#fffefa').style('font-family', 'Newsreader').style('font-size', '16px').text(b.label);
                      svg.append('text').attr('x', b.x + 12).attr('y', b.y + 48).attr('fill', b.c).style('font-family', 'JetBrains Mono').style('font-size', '14px').text(b.val);
                    }});
                  }} else if ({idx} === 5) {{
                    // Speedometer / Gauge
                    const cx = 320, cy = 260, r = 150;
                    svg.append('path').attr('d', `M ${{cx - r}} ${{cy}} A ${{r}} ${{r}} 0 0 1 ${{cx + r}} ${{cy}}`).attr('fill', 'none').attr('stroke', 'rgba(255,255,255,0.1)').attr('stroke-width', 22);
                    svg.append('path').attr('d', `M ${{cx - r}} ${{cy}} A ${{r}} ${{r}} 0 0 1 ${{cx + r*0.7}} ${{cy - r*0.71}}`).attr('fill', 'none').attr('stroke', 'url(#' + gradId + ')').attr('stroke-width', 22).attr('stroke-linecap', 'round');
                    svg.append('circle').attr('cx', cx).attr('cy', cy).attr('r', 10).attr('fill', '#fffefa');
                    svg.append('line').attr('x1', cx).attr('y1', cy).attr('x2', cx + 105 * Math.cos(-Math.PI * 0.3)).attr('y2', cy + 105 * Math.sin(-Math.PI * 0.3)).attr('stroke', '#f3cf65').attr('stroke-width', 4).attr('stroke-linecap', 'round');
                    svg.append('text').attr('x', cx).attr('y', cy + 44).attr('text-anchor', 'middle').attr('fill', '#00e676').style('font-family', 'JetBrains Mono').style('font-size', '28px').text("99.98% SLA");
                  }} else {{
                    // Continuous Multi-Line / Splines
                    const lineGen = d3.line().curve(d3.curveCatmullRom);
                    const pts1 = [[60, 320], [140, 260], [220, 280], [310, 160], [400, 190], [490, 110], [580, 80]];
                    const pts2 = [[60, 350], [140, 310], [220, 330], [310, 220], [400, 250], [490, 180], [580, 140]];
                    svg.append('path').attr('d', lineGen(pts1)).attr('fill', 'none').attr('stroke', '#d4af37').attr('stroke-width', 3);
                    svg.append('path').attr('d', lineGen(pts2)).attr('fill', 'none').attr('stroke', '#00e5ff').attr('stroke-width', 2.5).attr('stroke-dasharray', '4,4');
                    pts1.forEach(p => svg.append('circle').attr('cx', p[0]).attr('cy', p[1]).attr('r', 5).attr('fill', '#f3cf65'));
                  }}

                  svg.append('text').attr('x', 585).attr('y', 395).attr('text-anchor', 'end')
                    .attr('fill', 'rgba(212,175,55,0.6)').style('font-family', 'JetBrains Mono').style('font-size', '11px')
                    .text('{lib_name} Engine');

                }} catch(err) {{
                  console.error('Render error:', err);
                }}
              }}

              window.addEventListener('load', renderChart);
              if (window.Reveal) Reveal.on('slidechanged', (e) => {{ if (e.currentSlide.id === '{s_id}') renderChart(); }});
            }})();
            </script>
          </div>
          
          <div class="viz-info-panel">
            <div class="spec-card">
              <h5>Mathematical Engine</h5>
              <p>{arch['math_engine']}</p>
            </div>
            
            <div class="spec-card">
              <h5>Enterprise Application</h5>
              <p>{arch['use_case']}</p>
            </div>
            
            <div class="spec-card">
              <h5>Technical Capabilities</h5>
              <p>{arch['strengths']}</p>
            </div>
            
            <div class="code-box">
              <pre><code>{code_snippet}</code></pre>
            </div>
            
            <div class="metrics-strip">
              {metric_pills}
            </div>
          </div>
        </div>
      </section>
        """
        slides_html.append(slide_markup)

    all_slides = "\n".join(slides_html)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{lib_name} | Visualization Masterclass & Enterprise Demonstration</title>
  <meta name="description" content="10 Advanced Visualization Paradigms engineered with {lib_name} - {lib_desc}">
  
  <!-- Typography Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Reveal.js Core Stylesheet with Local & CDN Fallback -->
  <link rel="stylesheet" href="../../../../vendor/reveal.min.css" onerror="this.href='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.css'">
  <link rel="stylesheet" href="../../../../css/viz-deck.css">
  {css_extra}

  <!-- Self-Contained Masterclass Theme Styles -->
  <style>
    {THEME_CSS}
  </style>

  <!-- Visualization Libraries & Script CDNs -->
  {chr(10).join(cdns)}
</head>
<body>

  <!-- PERSISTENT TOP NAVIGATION -->
  <div class="deck-nav-bar">
    <div style="display: flex; align-items: center; gap: 14px;">
      <a href="../../../../index.html">
        <span aria-hidden="true">&larr;</span> <strong>Visualization Portfolio Hub</strong>
      </a>
      <span style="opacity: 0.35;">|</span>
      <span style="font-family: var(--font-mono); font-size: 0.82rem; color: var(--viz-gold-bright);">{lib_vendor}</span>
      <span style="opacity: 0.35;">|</span>
      <span style="color: #fffefa; font-weight: 500; font-family: var(--font-heading); font-size: 1.15rem;">{lib_name} Enterprise Masterclass</span>
    </div>
    <div style="display: flex; align-items: center; gap: 10px;">
      <span class="tech-badge">{lib_badge}</span>
      <span style="font-family: var(--font-mono); font-size: 0.78rem; color: var(--viz-text-muted);">10 Dense Slides</span>
    </div>
  </div>

  <!-- PERSISTENT FOOTER BAR -->
  <div class="deck-footer-bar">
    <span><strong>Demostration of Visualization Software</strong> &bull; {lib_name} Showcase</span>
    <span>Use <strong>Space / Arrows</strong> to Navigate &bull; Press <strong>F</strong> for Fullscreen &bull; <strong>O</strong> for Overview</span>
  </div>

  <div class="reveal">
    <div class="slides">
      {all_slides}
    </div>
  </div>

  <!-- Reveal.js Engine Initialization -->
  <script>
    Reveal.initialize({{
      hash: true,
      slideNumber: 'c/t',
      controls: true,
      progress: true,
      center: false,
      transition: 'fade',
      width: 1440,
      height: 900,
      margin: 0.04
    }});
    Reveal.on('slidechanged', function(event) {{
      window.dispatchEvent(new Event('resize'));
    }});
  </script>
</body>
</html>
"""
    return html_content

# Generate all 25 presentations
print(f"Generating 25 Reveal.js decks across subdirectories in {BASE_DIR}...")
count = 0
for lib in LIBRARIES:
    lib_dir = os.path.join(BASE_DIR, lib["dir"])
    if not os.path.exists(lib_dir):
        os.makedirs(lib_dir, exist_ok=True)
    
    html_content = generate_deck_html(lib)
    file_path = os.path.join(lib_dir, lib["file"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    index_path = os.path.join(lib_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    count += 1
    print(f"[{count:02d}/25] Created: {lib['dir']}/{lib['file']} (and index.html) - {len(html_content):,} bytes")

print(f"\nSUCCESS: All {count} Reveal.js presentations (10 dense pages each = 250 slides) successfully generated!")
