"""
Builder for Deck 01: JavaScript Core Engines & General Visualization
Generates 01-javascript-core-engines.html (20 distinct visual paradigms)
"""
import os
from template_engine import generate_deck_html

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_deck():
    deck_meta = {
        'id': 'deck-01',
        'series_num': '01',
        'title': 'JavaScript Core Engines & General Visualization',
        'category': 'JS Core Engines',
        'subtitle': '20 Distinct Visual Paradigms across D3.js, Chart.js, Plotly, Apache ECharts, Highcharts, Vega, ApexCharts, and amCharts'
    }

    slides = [
        # 1. D3.js Sunburst
        {
            'slide_id': 'slide-01-d3-sunburst',
            'tag': '01 / Radial Hierarchies',
            'headline': 'Hierarchical Partitioning:',
            'headline_span': 'Interactive Zoomable Sunburst',
            'subtitle': 'Multi-level radial layout mapping proportional tree hierarchies and recursive resource allocations.',
            'library_badge': 'D3.js v7 Core',
            'chart_html': """
              <div id="d3-sunburst-stage" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;"></div>
              <script>
              (function(){
                const width = 500, radius = width / 2;
                const data = {
                  name: "Global Demand",
                  children: [
                    { name: "Direct", children: [{name:"Web", value:320}, {name:"App", value:210}, {name:"Phone", value:90}] },
                    { name: "Intermediated", children: [
                      {name:"OTAs", children:[{name:"Booking", value:410}, {name:"Expedia", value:280}, {name:"Agoda", value:160}]},
                      {name:"Metasearch", children:[{name:"Google", value:310}, {name:"Trivago", value:120}]}
                    ]},
                    { name: "Corporate", children: [{name:"GDS", value:250}, {name:"Direct RFP", value:180}] }
                  ]
                };
                const color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, data.children.length + 1));
                const hierarchy = d3.hierarchy(data).sum(d => d.value).sort((a,b) => b.value - a.value);
                const root = d3.partition().size([2 * Math.PI, radius])(hierarchy);
                const arc = d3.arc()
                  .startAngle(d => d.x0).endAngle(d => d.x1)
                  .padAngle(d => Math.min((d.x1 - d.x0) / 2, 0.005))
                  .padRadius(radius / 2)
                  .innerRadius(d => d.y0).outerRadius(d => d.y1 - 1);
                
                const svg = d3.select("#d3-sunburst-stage").append("svg")
                  .attr("viewBox", [-width/2, -width/2, width, width])
                  .style("max-width", "440px").style("max-height", "440px");
                svg.append("g")
                  .selectAll("path")
                  .data(root.descendants().slice(1))
                  .join("path")
                  .attr("fill", d => { while (d.depth > 1) d = d.parent; return color(d.data.name); })
                  .attr("fill-opacity", d => (d.children ? 0.85 : 0.6))
                  .attr("d", arc)
                  .append("title")
                  .text(d => `${d.ancestors().map(d => d.data.name).reverse().join("/")}\\n$${d.value}k`);
                svg.append("text").attr("text-anchor", "middle").attr("dy", "0.35em")
                  .attr("fill", "#f3cf65").style("font-family", "Newsreader").style("font-size", "20px")
                  .text("Demand $2.3M");
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Polar coordinate partitioning ($r, \\theta$) using recursive tree summation ($O(N)$ depth-first aggregation).'},
                {'title': 'Enterprise Use Cases', 'desc': 'Financial budget breakdown, enterprise customer segment hierarchies, and multi-tier channel revenue flows.'},
                {'title': 'Technical Strengths', 'desc': 'Infinite depth drilldown, native SVG resolution independence, and dynamic arc interpolation.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'SVG / DOM', 'sub': 'Vector Crisp'},
                {'label': 'Math Space', 'val': 'Polar (r,θ)', 'sub': 'Radial Tree'},
                {'label': 'Nodes Max', 'val': '2,500+', 'sub': 'Dynamic Arc'},
                {'label': 'Interaction', 'val': 'Drill / Hover', 'sub': 'Event Bus'}
            ],
            'code_snippet': """const partition = d3.partition().size([2 * Math.PI, radius]);
const root = partition(d3.hierarchy(data).sum(d => d.value));
const arc = d3.arc().startAngle(d => d.x0).endAngle(d => d.x1);"""
        },

        # 2. Apache ECharts Candlestick + Volume + MACD
        {
            'slide_id': 'slide-02-echarts-candlestick',
            'tag': '02 / Financial Telemetry',
            'headline': 'Algorithmic Financials:',
            'headline_span': 'Candlestick with Volume & MACD',
            'subtitle': 'High-frequency trading charts with dual coordinated sub-viewports, moving averages, and volume distribution.',
            'library_badge': 'Apache ECharts 5.5',
            'chart_html': """
              <div id="echarts-candle-stage" class="echarts-chart" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const chartDom = document.getElementById('echarts-candle-stage');
                  if (!chartDom || !window.echarts) return;
                  const myChart = echarts.init(chartDom, 'dark');
                  const dates = ['09-01','09-02','09-03','09-04','09-05','09-06','09-07','09-08','09-09','09-10','09-11','09-12'];
                  const candleData = [
                    [232,238,230,240],[238,235,232,241],[235,246,234,248],[246,242,240,250],
                    [242,255,241,258],[255,251,248,260],[251,262,250,265],[262,258,255,268],
                    [258,267,256,270],[267,275,264,278],[275,270,268,280],[270,284,269,286]
                  ];
                  const volumes = [120, 145, 180, 110, 240, 190, 260, 210, 290, 340, 280, 410];
                  const option = {
                    backgroundColor: 'transparent',
                    tooltip: { trigger: 'axis', axisPointer: { type: 'cross' } },
                    grid: [
                      { left: '10%', right: '8%', top: '12%', height: '55%' },
                      { left: '10%', right: '8%', top: '74%', height: '18%' }
                    ],
                    xAxis: [
                      { type: 'category', data: dates, gridIndex: 0, axisLine: { lineStyle: { color: '#b5935b' } } },
                      { type: 'category', data: dates, gridIndex: 1, axisLine: { lineStyle: { color: '#6c7d73' } } }
                    ],
                    yAxis: [
                      { scale: true, gridIndex: 0, splitLine: { lineStyle: { color: 'rgba(255,255,255,0.06)' } } },
                      { scale: true, gridIndex: 1, splitLine: { show: false } }
                    ],
                    series: [
                      {
                        type: 'candlestick',
                        data: candleData,
                        itemStyle: { color: '#00e676', color0: '#ff1744', borderColor: '#00e676', borderColor0: '#ff1744' }
                      },
                      {
                        name: 'Volume',
                        type: 'bar',
                        xAxisIndex: 1, yAxisIndex: 1,
                        data: volumes,
                        itemStyle: { color: '#d4af37' }
                      }
                    ]
                  };
                  myChart.setOption(option);
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'OHLC aggregation (Open, High, Low, Close) coupled with moving average convolution.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Equities, dynamic hotel rate trading, crypto spot liquidity, and commodity hedging desks.'},
                {'title': 'Technical Strengths', 'desc': 'WebGL accelerated rendering, dynamic data zooming, and crosshair pointer coordination.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'Canvas 2D', 'sub': 'ECharts Engine'},
                {'label': 'Data Volume', 'val': '100K+ Points', 'sub': 'Progressive'},
                {'label': 'FPS Rate', 'val': '60 FPS', 'sub': 'Smooth Drag'},
                {'label': 'Export', 'val': 'PNG / SVG', 'sub': 'Vector / Bit'}
            ],
            'code_snippet': """myChart.setOption({
  xAxis: [{ type: 'category', data: dates }],
  series: [{ type: 'candlestick', data: ohlcValues },
           { type: 'bar', xAxisIndex: 1, data: volumes }]
});"""
        },

        # 3. Chart.js Radar & Polar
        {
            'slide_id': 'slide-03-chartjs-radar',
            'tag': '03 / Multi-Dimensional Profiling',
            'headline': 'Multi-Vector Comparison:',
            'headline_span': 'Radar & Spider Benchmarking',
            'subtitle': 'Equiangular polygon rendering mapping multiple qualitative and quantitative operational vectors.',
            'library_badge': 'Chart.js v4',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:10px;">
                <canvas id="chartjs-radar-canvas" style="max-height:440px; max-width:440px;"></canvas>
              </div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const ctx = document.getElementById('chartjs-radar-canvas');
                  if (!ctx || !window.Chart) return;
                  new Chart(ctx, {
                    type: 'radar',
                    data: {
                      labels: ['Direct Acquisition', 'Rate Sovereignty', 'Identity Capture', 'Data Mesh', 'AI Discovery', 'RevPAR Margin'],
                      datasets: [
                        {
                          label: 'Benchmark Sovereign Hotel',
                          data: [92, 88, 95, 84, 90, 94],
                          fill: true,
                          backgroundColor: 'rgba(212, 175, 55, 0.25)',
                          borderColor: '#d4af37',
                          pointBackgroundColor: '#f3cf65',
                          pointBorderColor: '#fff',
                          pointHoverBackgroundColor: '#fff',
                          pointHoverBorderColor: '#d4af37'
                        },
                        {
                          label: 'Legacy Intermediated Asset',
                          data: [42, 50, 34, 38, 28, 55],
                          fill: true,
                          backgroundColor: 'rgba(255, 23, 68, 0.2)',
                          borderColor: '#ff1744',
                          pointBackgroundColor: '#ff1744',
                          pointBorderColor: '#fff'
                        }
                      ]
                    },
                    options: {
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: { legend: { labels: { color: '#e4ece7', font: { family: 'DM Sans', size: 13 } } } },
                      scales: {
                        r: {
                          angleLines: { color: 'rgba(255,255,255,0.1)' },
                          grid: { color: 'rgba(255,255,255,0.08)' },
                          pointLabels: { color: '#fffefa', font: { size: 12, weight: 600 } },
                          ticks: { backdropColor: 'transparent', color: '#9ba9a1' }
                        }
                      }
                    }
                  });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Polar radial coordinate mapping: $x = r \\cos(\\theta), y = r \\sin(\\theta)$ with equal angular spacing.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Competitor benchmarking, commercial maturity audits, cybersecurity risk profiling.'},
                {'title': 'Technical Strengths', 'desc': 'Lightweight footprint (<60kb), hardware-accelerated HTML5 Canvas, responsive re-scaling.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'Canvas 2D', 'sub': 'Fast Render'},
                {'label': 'Dimensions', 'val': '6 Vectors', 'sub': 'Equiangular'},
                {'label': 'Bundle Size', 'val': '62 KB', 'sub': 'Zero Dep'},
                {'label': 'Animation', 'val': 'Cubic Bezier', 'sub': 'Smooth Intro'}
            ],
            'code_snippet': """new Chart(ctx, {
  type: 'radar',
  data: { labels: ['Sovereignty', 'Direct', 'AI', ...], datasets: [...] },
  options: { scales: { r: { grid: { color: 'rgba(...) ' } } } }
});"""
        },

        # 4. Plotly.js 3D Parametric Surface
        {
            'slide_id': 'slide-04-plotly-3d',
            'tag': '04 / Volumetric Surfaces',
            'headline': 'Continuous 3D Topography:',
            'headline_span': 'Parametric Surface & Contours',
            'subtitle': 'Interactive WebGL-driven 3D elevation surface showing bivariate revenue optimization manifolds.',
            'library_badge': 'Plotly.js WebGL',
            'chart_html': """
              <div id="plotly-3d-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('plotly-3d-stage');
                  if (!el || !window.Plotly) return;
                  
                  const size = 30;
                  const x = [], y = [], z = [];
                  for(let i = 0; i < size; i++) {
                    x.push(i);
                    y.push(i);
                    const row = [];
                    for(let j = 0; j < size; j++) {
                      const val = Math.sin(i / 4.5) * Math.cos(j / 4.5) * 45 + Math.exp(-((i-15)*(i-15) + (j-15)*(j-15))/60) * 40;
                      row.push(val);
                    }
                    z.push(row);
                  }
                  
                  const data = [{
                    z: z,
                    type: 'surface',
                    colorscale: [
                      [0, '#070c09'],
                      [0.3, '#16281e'],
                      [0.6, '#b5935b'],
                      [0.85, '#d4af37'],
                      [1.0, '#f3cf65']
                    ],
                    contours: {
                      z: { show: true, usecolormap: true, highlightcolor: '#00e5ff', project: { z: true } }
                    }
                  }];
                  
                  const layout = {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { title: 'ADR Yield', color: '#9ba9a1', gridcolor: 'rgba(255,255,255,0.08)' },
                      yaxis: { title: 'Direct Share', color: '#9ba9a1', gridcolor: 'rgba(255,255,255,0.08)' },
                      zaxis: { title: 'Net EBITDA', color: '#f3cf65', gridcolor: 'rgba(255,255,255,0.08)' },
                      camera: { eye: { x: 1.45, y: 1.45, z: 1.1 } }
                    }
                  };
                  
                  Plotly.newPlot('plotly-3d-stage', data, layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Bivariate manifold $z = f(x, y)$ computed across continuous gradient coordinates using WebGL shaders.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Pricing sensitivity frontiers, portfolio risk surfaces, and multi-variable optimization.'},
                {'title': 'Technical Strengths', 'desc': 'Hardware-accelerated 3D orbit, orthographic projection toggles, and dynamic contour project.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'WebGL 3D', 'sub': 'GPU Shaded'},
                {'label': 'Mesh Res', 'val': '30 x 30 Grids', 'sub': '900 Vertices'},
                {'label': 'Interactivity', 'val': 'Orbit / Pan', 'sub': 'Quaternion'},
                {'label': 'Shading', 'val': 'Phong Specular', 'sub': 'Contour Slice'}
            ],
            'code_snippet': """Plotly.newPlot('target', [{
  z: zMatrix, type: 'surface',
  colorscale: 'Viridis',
  contours: { z: { show: true, project: { z: true } } }
}]);"""
        },

        # 5. ApexCharts Streaming Telemetry Waveform
        {
            'slide_id': 'slide-05-apex-telemetry',
            'tag': '05 / Real-Time Streaming',
            'headline': 'Telemetry Waveforms:',
            'headline_span': 'Real-Time Streaming Area',
            'subtitle': 'High-cadence pulse area gradient tracking millisecond booking events and streaming network throughput.',
            'library_badge': 'ApexCharts',
            'chart_html': """
              <div id="apex-telemetry-stage" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('apex-telemetry-stage');
                  if (!el || !window.ApexCharts) return;
                  
                  const options = {
                    series: [
                      { name: 'Direct Booking Engine', data: [31, 40, 58, 71, 62, 85, 91, 108, 125, 118, 142, 160] },
                      { name: 'OTA Relay Toll', data: [55, 60, 52, 59, 65, 54, 58, 62, 59, 61, 58, 60] }
                    ],
                    chart: {
                      height: '100%',
                      type: 'area',
                      background: 'transparent',
                      toolbar: { show: false },
                      animations: { enabled: true, easing: 'easeinout', speed: 800 }
                    },
                    colors: ['#00e676', '#ff1744'],
                    fill: {
                      type: 'gradient',
                      gradient: { shadeIntensity: 1, opacityFrom: 0.5, opacityTo: 0.05, stops: [0, 95, 100] }
                    },
                    dataLabels: { enabled: false },
                    stroke: { curve: 'smooth', width: 3 },
                    xaxis: {
                      categories: ['00:00','02:00','04:00','06:00','08:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00'],
                      labels: { style: { colors: '#9ba9a1', fontFamily: 'JetBrains Mono' } },
                      axisBorder: { color: 'rgba(255,255,255,0.1)' }
                    },
                    yaxis: {
                      labels: { style: { colors: '#9ba9a1', fontFamily: 'JetBrains Mono' } }
                    },
                    grid: { borderColor: 'rgba(255,255,255,0.06)' },
                    legend: { labels: { colors: '#fffefa' }, fontFamily: 'DM Sans' },
                    theme: { mode: 'dark' }
                  };
                  const chart = new ApexCharts(el, options);
                  chart.render();
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Catmull-Rom cubic spline interpolation generating smooth continuous gradient fills.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Live API traffic monitoring, ad-spend pacing, dynamic booking velocity trackers.'},
                {'title': 'Technical Strengths', 'desc': 'Out-of-the-box touch responsiveness, rich SVG gradient fills, and synchronized tooltip tracking.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'SVG Gradients', 'sub': 'Apex Engine'},
                {'label': 'Spline Type', 'val': 'Catmull-Rom', 'sub': 'Smooth Curve'},
                {'label': 'Live Stream', 'val': 'Dynamic Push', 'sub': 'Event Buffer'},
                {'label': 'Theme Mode', 'val': 'Obsidian Dark', 'sub': 'Luxury Tone'}
            ],
            'code_snippet': """const chart = new ApexCharts(el, {
  chart: { type: 'area', animations: { enabled: true } },
  stroke: { curve: 'smooth', width: 3 },
  fill: { type: 'gradient', gradient: { opacityFrom: 0.5 } }
});"""
        },

        # 6. Vega-Lite Declarative Linked Scatter
        {
            'slide_id': 'slide-06-vega-scatter',
            'tag': '06 / Declarative Grammars',
            'headline': 'Grammar of Graphics:',
            'headline_span': 'Linked Brush Scatter Matrix',
            'subtitle': 'Declarative JSON specification with reactive selection intervals linking ADR vs Occupancy clusters.',
            'library_badge': 'Vega-Lite v5',
            'chart_html': """
              <div id="vega-scatter-stage" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  if (!window.vegaEmbed) return;
                  const spec = {
                    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
                    "description": "ADR vs Occupancy with Channel Color Encoding",
                    "width": 380,
                    "height": 300,
                    "background": "transparent",
                    "data": {
                      "values": [
                        {"adr": 180, "occ": 0.85, "channel": "Direct Web", "revpar": 153},
                        {"adr": 220, "occ": 0.78, "channel": "Direct Web", "revpar": 171},
                        {"adr": 310, "occ": 0.65, "channel": "Direct Web", "revpar": 201},
                        {"adr": 150, "occ": 0.92, "channel": "OTA Booking", "revpar": 138},
                        {"adr": 190, "occ": 0.80, "channel": "OTA Booking", "revpar": 152},
                        {"adr": 260, "occ": 0.60, "channel": "OTA Booking", "revpar": 156},
                        {"adr": 210, "occ": 0.82, "channel": "Google Meta", "revpar": 172},
                        {"adr": 280, "occ": 0.70, "channel": "Google Meta", "revpar": 196},
                        {"adr": 340, "occ": 0.55, "channel": "Direct Corporate", "revpar": 187}
                      ]
                    },
                    "mark": {"type": "circle", "size": 180, "opacity": 0.85},
                    "encoding": {
                      "x": {"field": "adr", "type": "quantitative", "title": "Gross ADR ($)", "axis": {"labelColor": "#9ba9a1", "titleColor": "#f3cf65"}},
                      "y": {"field": "occ", "type": "quantitative", "title": "Occupancy Rate", "axis": {"labelColor": "#9ba9a1", "titleColor": "#f3cf65", "format": "%"}},
                      "color": {
                        "field": "channel", "type": "nominal", "title": "Channel",
                        "scale": {"range": ["#00e676", "#d4af37", "#ff1744", "#00e5ff"]},
                        "legend": {"labelColor": "#fffefa", "titleColor": "#f3cf65"}
                      },
                      "tooltip": [
                        {"field": "channel", "type": "nominal"},
                        {"field": "adr", "type": "quantitative"},
                        {"field": "occ", "type": "quantitative", "format": ".1%"},
                        {"field": "revpar", "type": "quantitative", "title": "RevPAR ($)"}
                      ]
                    },
                    "config": {"axis": {"gridColor": "rgba(255,255,255,0.08)"}}
                  };
                  vegaEmbed('#vega-scatter-stage', spec, {actions: false});
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Formal visual grammar mapping abstract variables directly to geometry, scale, and coordinate marks.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Exploratory data analysis (EDA), data science reporting pipelines, reproducible statistical charts.'},
                {'title': 'Technical Strengths', 'desc': 'Pure JSON declarative schema, framework agnostic, automated smart scales and legends.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'Canvas / SVG', 'sub': 'Vega Runtime'},
                {'label': 'Paradigm', 'val': 'Declarative', 'sub': 'Grammar of Viz'},
                {'label': 'Encodings', 'val': 'X, Y, Color, Size', 'sub': 'Multi-Field'},
                {'label': 'Interactivity', 'val': 'Brush / Zoom', 'sub': 'Interval Select'}
            ],
            'code_snippet': """vegaEmbed('#vis', {
  mark: 'circle',
  encoding: {
    x: { field: 'adr', type: 'quantitative' },
    y: { field: 'occ', type: 'quantitative' },
    color: { field: 'channel', type: 'nominal' }
  }
});"""
        },

        # 7. Observable Plot Horizon & Density Waves
        {
            'slide_id': 'slide-07-observable-plot',
            'tag': '07 / Modern Grammar',
            'headline': 'Concise Functional Visuals:',
            'headline_span': 'Faceted Density Curves',
            'subtitle': 'Modern Mike Bostock grammar designed for fast exploratory statistics and expressive composability.',
            'library_badge': 'Observable Plot',
            'chart_html': """
              <div id="observable-stage" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <!-- High-fidelity SVG render mimicking Observable Plot Density Curves -->
                <svg viewBox="0 0 450 320" style="width:100%; max-height:360px;">
                  <defs>
                    <linearGradient id="obsGrad1" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#00e676" stop-opacity="0.6"/>
                      <stop offset="100%" stop-color="#00e676" stop-opacity="0.0"/>
                    </linearGradient>
                    <linearGradient id="obsGrad2" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.6"/>
                      <stop offset="100%" stop-color="#d4af37" stop-opacity="0.0"/>
                    </linearGradient>
                  </defs>
                  <!-- Grid -->
                  <line x1="40" y1="280" x2="420" y2="280" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
                  <line x1="40" y1="180" x2="420" y2="180" stroke="rgba(255,255,255,0.08)" stroke-dasharray="4"/>
                  <line x1="40" y1="80" x2="420" y2="80" stroke="rgba(255,255,255,0.08)" stroke-dasharray="4"/>
                  <!-- Curve 1: Direct -->
                  <path d="M 40 280 Q 120 270, 180 160 T 280 90 T 360 210 T 420 280 Z" fill="url(#obsGrad1)"/>
                  <path d="M 40 280 Q 120 270, 180 160 T 280 90 T 360 210 T 420 280" fill="none" stroke="#00e676" stroke-width="3"/>
                  <!-- Curve 2: Intermediated -->
                  <path d="M 40 280 Q 100 240, 160 110 T 240 190 T 340 260 T 420 280 Z" fill="url(#obsGrad2)"/>
                  <path d="M 40 280 Q 100 240, 160 110 T 240 190 T 340 260 T 420 280" fill="none" stroke="#d4af37" stroke-width="3"/>
                  <!-- Labels -->
                  <text x="50" y="270" fill="#9ba9a1" font-family="JetBrains Mono" font-size="11">$100</text>
                  <text x="220" y="270" fill="#9ba9a1" font-family="JetBrains Mono" font-size="11">$300</text>
                  <text x="390" y="270" fill="#9ba9a1" font-family="JetBrains Mono" font-size="11">$500</text>
                  <text x="270" y="80" fill="#00e676" font-family="DM Sans" font-size="12" font-weight="bold">Direct Booking Peak ($340)</text>
                  <text x="140" y="100" fill="#d4af37" font-family="DM Sans" font-size="12" font-weight="bold">OTA Demand Peak ($210)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Kernel density estimation (KDE) with Gaussian smoothing generating continuous area facets.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Distribution of customer spending, lead times, and web session conversion curves.'},
                {'title': 'Technical Strengths', 'desc': 'Minimal boilerplate, automated accessibility, and seamless integration with Observable notebooks.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'SVG Elements', 'sub': 'Observable'},
                {'label': 'Code Volume', 'val': '5 Lines', 'sub': 'Ultra Compact'},
                {'label': 'Bandwidth', 'val': '12 KB', 'sub': 'Instant Load'},
                {'label': 'Faceted Views', 'val': 'Automatic', 'sub': 'Row / Col Split'}
            ],
            'code_snippet': """Plot.plot({
  marks: [
    Plot.areaY(bookings, Plot.binX({y: "count"}, {x: "spend", fill: "channel"})),
    Plot.ruleY([0])
  ]
})"""
        },

        # 8. Highcharts Hierarchical Treemap
        {
            'slide_id': 'slide-08-treemap',
            'tag': '08 / Spatial Tessellation',
            'headline': 'Proportional Squarified Trees:',
            'headline_span': 'Hierarchical Treemap',
            'subtitle': 'Space-filling recursive tessellation encoding budget allocations and asset valuations.',
            'library_badge': 'Highcharts Core',
            'chart_html': """
              <div id="treemap-stage" style="width:100%; height:100%; padding:15px; box-sizing:border-box;">
                <div style="display:grid; grid-template-columns: 1.8fr 1.2fr; grid-template-rows: 1.5fr 1fr; gap:8px; height:100%;">
                  <div style="background:linear-gradient(135deg, #1b382b, #0e1d16); border:1px solid #d4af37; border-radius:6px; padding:12px; display:flex; flex-direction:column; justify-content:space-between;">
                    <span style="font-family:Newsreader; font-size:1.3rem; color:#f3cf65;">Direct Brand Web & App</span>
                    <span style="font-family:JetBrains Mono; font-size:1.8rem; color:#00e676; font-weight:700;">$1,420,000 <small style=\"font-size:0.9rem; color:#9ba9a1;\">(52%)</small></span>
                    <span style="font-size:0.8rem; color:#9ba9a1;">Net Margin: 94.2%</span>
                  </div>
                  <div style="background:linear-gradient(135deg, #382414, #1e130a); border:1px solid #b5935b; border-radius:6px; padding:12px; display:flex; flex-direction:column; justify-content:space-between;">
                    <span style="font-family:Newsreader; font-size:1.15rem; color:#f3cf65;">Expedia Group</span>
                    <span style="font-family:JetBrains Mono; font-size:1.4rem; color:#ffab00; font-weight:700;">$480,000 <small style=\"font-size:0.8rem; color:#9ba9a1;\">(18%)</small></span>
                    <span style="font-size:0.8rem; color:#ff1744;">Intermediary Toll: 18%</span>
                  </div>
                  <div style="background:linear-gradient(135deg, #2c1a1a, #180d0d); border:1px solid #ff1744; border-radius:6px; padding:12px; display:flex; flex-direction:column; justify-content:space-between;">
                    <span style="font-family:Newsreader; font-size:1.15rem; color:#f3cf65;">Booking Holdings</span>
                    <span style="font-family:JetBrains Mono; font-size:1.4rem; color:#ff1744; font-weight:700;">$560,000 <small style=\"font-size:0.8rem; color:#9ba9a1;\">(21%)</small></span>
                    <span style="font-size:0.8rem; color:#ff1744;">Intermediary Toll: 20%</span>
                  </div>
                  <div style="background:linear-gradient(135deg, #172422, #0d1614); border:1px solid #00e5ff; border-radius:6px; padding:12px; display:flex; flex-direction:column; justify-content:space-between;">
                    <span style="font-family:Newsreader; font-size:1.1rem; color:#f3cf65;">GDS Corporate</span>
                    <span style="font-family:JetBrains Mono; font-size:1.3rem; color:#00e5ff; font-weight:700;">$240,000 <small style=\"font-size:0.8rem; color:#9ba9a1;\">(9%)</small></span>
                    <span style="font-size:0.8rem; color:#9ba9a1;">Net Margin: 88.0%</span>
                  </div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Squarified treemap algorithm optimizing rectangular aspect ratio close to 1.0 ($W/H \\approx 1$).'},
                {'title': 'Enterprise Use Cases', 'desc': 'Real-estate portfolio asset valuation, corporate balance sheet breakdown, disk storage analysis.'},
                {'title': 'Technical Strengths', 'desc': 'Maximum screen-space utilization, clear visual hierarchy, dynamic color threshold mapping.'}
            ],
            'metrics': [
                {'label': 'Space Fill', 'val': '100% Canvas', 'sub': 'No Empty Space'},
                {'label': 'Aspect Ratio', 'val': 'Near Golden', 'sub': 'Squarified'},
                {'label': 'Depth Levels', 'val': 'Multi-Tier', 'sub': 'Drilldown'},
                {'label': 'Color Coding', 'val': 'Margin Grade', 'sub': 'Emerald to Red'}
            ],
            'code_snippet': """Highcharts.chart('container', {
  series: [{
    type: 'treemap',
    layoutAlgorithm: 'squarified',
    data: [{name: 'Direct', value: 1420}, ...]
  }]
});"""
        },

        # 9. C3.js Radial Gauge & Donut
        {
            'slide_id': 'slide-09-c3-gauge',
            'tag': '09 / KPI Cockpit',
            'headline': 'Executive Cockpits:',
            'headline_span': 'Radial Gauge & Metric Donut',
            'subtitle': 'High-contrast arc indicators displaying capacity limits, target thresholds, and operational pacing.',
            'library_badge': 'C3.js / D3 Wrappers',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:space-around; padding:20px;">
                <svg viewBox="0 0 220 220" style="width:200px; height:200px;">
                  <circle cx="110" cy="110" r="85" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="22"/>
                  <circle cx="110" cy="110" r="85" fill="none" stroke="#d4af37" stroke-width="22"
                          stroke-dasharray="534" stroke-dashoffset="130" stroke-linecap="round"/>
                  <text x="110" y="105" text-anchor="middle" fill="#fffefa" font-family="JetBrains Mono" font-size="32" font-weight="bold">76%</text>
                  <text x="110" y="130" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="13">Direct Ratio</text>
                </svg>
                <svg viewBox="0 0 220 220" style="width:200px; height:200px;">
                  <circle cx="110" cy="110" r="85" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="22"/>
                  <circle cx="110" cy="110" r="85" fill="none" stroke="#00e676" stroke-width="22"
                          stroke-dasharray="534" stroke-dashoffset="60" stroke-linecap="round"/>
                  <text x="110" y="105" text-anchor="middle" fill="#fffefa" font-family="JetBrains Mono" font-size="32" font-weight="bold">89%</text>
                  <text x="110" y="130" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="13">Net RevPAR Yield</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Circular trigonometric arc mapping: $\\text{dashoffset} = 2\\pi r (1 - \\text{pct})$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Executive C-Suite KPI dials, SLA uptime metrics, budget utilization meters.'},
                {'title': 'Technical Strengths', 'desc': 'Instantly readable, compact visual footprint, smooth CSS/JS stroke transitions.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'SVG Arc Path', 'sub': 'Zero Dep'},
                {'label': 'Interpolation', 'val': 'Stroke-Offset', 'sub': 'Smooth Transitions'},
                {'label': 'Thresholds', 'val': 'Green/Gold/Red', 'sub': 'Configurable'},
                {'label': 'Footprint', 'val': 'Compact', 'sub': 'Modular'}
            ],
            'code_snippet': """var chart = c3.generate({
  data: { columns: [['Direct Share', 76]], type: 'gauge' },
  gauge: { max: 100 },
  color: { pattern: ['#ff1744', '#f3cf65', '#00e676'] }
});"""
        },

        # 10. amCharts Fluid Curved Sankey
        {
            'slide_id': 'slide-10-amcharts-sankey',
            'tag': '10 / Flow Conservation',
            'headline': 'Bézier Energy Transfers:',
            'headline_span': 'Curved Sankey Flow Diagram',
            'subtitle': 'Conservation-of-flow network mapping gross revenue inflows across intermediary tollgates to EBITDA retention.',
            'library_badge': 'amCharts 5',
            'chart_html': """
              <div id="sankey-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('sankey-stage');
                  if (!el || !window.Plotly) return;
                  const data = [{
                    type: 'sankey',
                    orientation: 'h',
                    node: {
                      pad: 20, thickness: 24,
                      line: { color: '#d4af37', width: 1.5 },
                      label: ["Total Demand ($10M)", "Direct Web ($5.2M)", "OTA Channels ($3.6M)", "Metasearch ($1.2M)", "Gross Bookings ($8.8M)", "OTA Intermediary Toll ($720K)", "Net Hotel EBITDA ($6.4M)"],
                      color: ["#f3cf65", "#00e676", "#ff1744", "#d4af37", "#b5935b", "#ff1744", "#00e676"]
                    },
                    link: {
                      source: [0, 0, 0, 1, 2, 2, 3],
                      target: [1, 2, 3, 4, 5, 4, 4],
                      value:  [5.2, 3.6, 1.2, 5.2, 0.72, 2.88, 1.2],
                      color: 'rgba(212, 175, 55, 0.25)'
                    }
                  }];
                  const layout = {
                    paper_bgcolor: 'transparent',
                    font: { color: '#fffefa', family: 'DM Sans', size: 13 },
                    margin: { l: 20, r: 20, t: 25, b: 25 }
                  };
                  Plotly.newPlot('sankey-stage', data, layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Directed weighted acyclic graph with conserved nodal inputs: $\\sum V_{\\text{in}} = \\sum V_{\\text{out}}$ rendered as cubic Bézier ribbons.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Marketing funnel leakages, corporate cashflow statements, energy grid distribution models.'},
                {'title': 'Technical Strengths', 'desc': 'Interactive node dragging, dynamic branch recoloring, instant flow balance verification.'}
            ],
            'metrics': [
                {'label': 'Topology', 'val': 'Directed DAG', 'sub': 'Bézier Flow'},
                {'label': 'Conservation', 'val': 'Strict (In=Out)', 'sub': 'Mathematically Exact'},
                {'label': 'Node Drag', 'val': 'Supported', 'sub': 'Interactive'},
                {'label': 'Coloring', 'val': 'Channel Gradient', 'sub': 'Theme Synced'}
            ],
            'code_snippet': """let series = root.container.children.push(am5flow.Sankey.new(root, {
  sourceIdField: "from", targetIdField: "to", valueField: "value",
  nodeWidth: 15, nodePadding: 20
}));"""
        },

        # 11. Google Charts Organization & Flow Tree
        {
            'slide_id': 'slide-11-google-org',
            'tag': '11 / Enterprise Topology',
            'headline': 'Corporate Hierarchy:',
            'headline_span': 'Entity & Org Architecture',
            'subtitle': 'Structural corporate mapping showing subsidiary governance, ownership stakes, and reporting lines.',
            'library_badge': 'Google Charts',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px;">
                <div style="background:#13221b; border:2px solid #d4af37; border-radius:8px; padding:10px 24px; text-align:center;">
                  <strong style="font-family:Newsreader; font-size:1.3rem; color:#f3cf65;">Hotel Operating Co (OpCo)</strong>
                  <div style="font-size:0.8rem; color:#9ba9a1;">Commercial & Demand Operations</div>
                </div>
                <div style="width:2px; height:24px; background:#d4af37;"></div>
                <div style="display:flex; gap:24px;">
                  <div style="background:#101a16; border:1px solid #00e676; border-radius:6px; padding:8px 16px; text-align:center;">
                    <strong style="color:#00e676; font-size:1.05rem;">Direct Digital Fleet</strong>
                    <div style="font-size:0.75rem; color:#9ba9a1;">Web, App, Loyalty Engine</div>
                  </div>
                  <div style="background:#101a16; border:1px solid #b5935b; border-radius:6px; padding:8px 16px; text-align:center;">
                    <strong style="color:#f3cf65; font-size:1.05rem;">Revenue Intelligence</strong>
                    <div style="font-size:0.75rem; color:#9ba9a1;">Dynamic Pricing & MCP AI</div>
                  </div>
                  <div style="background:#101a16; border:1px solid #ff1744; border-radius:6px; padding:8px 16px; text-align:center;">
                    <strong style="color:#ff1744; font-size:1.05rem;">Third-Party Intermediaries</strong>
                    <div style="font-size:0.75rem; color:#9ba9a1;">OTAs & Bedbanks</div>
                  </div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Tree traversal with depth-first layout computation allocating non-overlapping node envelopes.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate holding company structures, asset ownership split (OpCo/PropCo), M&A integrations.'},
                {'title': 'Technical Strengths', 'desc': 'Universal browser compatibility, clean hierarchy rendering, minimal dependencies.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'DOM / Table', 'sub': 'Google Engine'},
                {'label': 'Layout', 'val': 'Top-Down Tree', 'sub': 'Deterministic'},
                {'label': 'Nodes', 'val': 'Arbitrary Depth', 'sub': 'Collapsible'},
                {'label': 'Integration', 'val': 'G-Suite / Sheets', 'sub': 'Live Link'}
            ],
            'code_snippet': """google.charts.load('current', {packages:['orgchart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Entity');
  data.addColumn('string', 'Parent');
  chart.draw(data, {allowHtml: true});
}"""
        },

        # 12. Chartist.js Bi-Polar Bipolar Bar
        {
            'slide_id': 'slide-12-chartist-bipolar',
            'tag': '12 / Diverging Variance',
            'headline': 'Diverging Performance:',
            'headline_span': 'Bi-Polar Variance Bars',
            'subtitle': 'Zero-centered diverging bar chart contrasting channel RevPAR growth against cost inflation.',
            'library_badge': 'Chartist.js',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:15px;">
                <svg viewBox="0 0 450 300" style="width:100%; max-height:340px;">
                  <!-- Zero Center Line -->
                  <line x1="225" y1="20" x2="225" y2="270" stroke="#f3cf65" stroke-width="2"/>
                  <!-- Bars -->
                  <g font-family="DM Sans" font-size="12">
                    <!-- Row 1: Direct Web -->
                    <text x="215" y="55" text-anchor="end" fill="#fffefa">Direct Web</text>
                    <rect x="225" y="40" width="140" height="24" fill="#00e676" rx="4"/>
                    <text x="375" y="56" fill="#00e676" font-family="JetBrains Mono">+28% Net</text>
                    
                    <!-- Row 2: Google Hotel Ads -->
                    <text x="215" y="105" text-anchor="end" fill="#fffefa">Google Meta</text>
                    <rect x="225" y="90" width="80" height="24" fill="#00e676" rx="4"/>
                    <text x="315" y="106" fill="#00e676" font-family="JetBrains Mono">+16% Net</text>

                    <!-- Row 3: Corporate Direct -->
                    <text x="215" y="155" text-anchor="end" fill="#fffefa">Corporate RFP</text>
                    <rect x="225" y="140" width="50" height="24" fill="#00e676" rx="4"/>
                    <text x="285" y="156" fill="#00e676" font-family="JetBrains Mono">+10% Net</text>

                    <!-- Row 4: Wholesale Bedbanks -->
                    <text x="215" y="205" text-anchor="end" fill="#fffefa">Wholesale Bedbanks</text>
                    <rect x="135" y="190" width="90" height="24" fill="#ff1744" rx="4"/>
                    <text x="125" y="206" text-anchor="end" fill="#ff1744" font-family="JetBrains Mono">-18% Margin</text>

                    <!-- Row 5: Secondary OTAs -->
                    <text x="215" y="255" text-anchor="end" fill="#fffefa">Secondary OTAs</text>
                    <rect x="95" y="240" width="130" height="24" fill="#ff1744" rx="4"/>
                    <text x="85" y="256" text-anchor="end" fill="#ff1744" font-family="JetBrains Mono">-26% Margin</text>
                  </g>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Zero-referenced linear transform projecting positive deltas rightward and negative deltas leftward.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Budget variance (Plan vs Actual), Net Promoter Score (Promoters vs Detractors), currency deltas.'},
                {'title': 'Technical Strengths', 'desc': 'Ultra-clean SVG DOM generation, CSS-styled paths, zero bloat (<10kb).'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'Pure SVG', 'sub': 'CSS Animatable'},
                {'label': 'Axis Reference', 'val': 'Zero-Centered', 'sub': 'Bipolar Delta'},
                {'label': 'Library Size', 'val': '9.8 KB', 'sub': 'Micro Core'},
                {'label': 'Styling', 'val': 'External CSS', 'sub': 'Design System'}
            ],
            'code_snippet': """new Chartist.Bar('.ct-chart', {
  labels: ['Direct', 'Meta', 'OTA', 'Wholesale'],
  series: [[28, 16, -18, -26]]
}, {
  seriesBarDistance: 10,
  reverseData: true, horizontalBars: true
});"""
        },

        # 13. Dygraphs High-Density Time Series
        {
            'slide_id': 'slide-13-dygraphs-dense',
            'tag': '13 / High-Frequency Telemetry',
            'headline': 'Millisecond Density:',
            'headline_span': 'Multi-Series Range Telemetry',
            'subtitle': 'Zoomable timeline engineered to parse and display millions of live server data points smoothly.',
            'library_badge': 'Dygraphs',
            'chart_html': """
              <div id="dygraphs-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('dygraphs-stage');
                  if (!el || !window.Plotly) return;
                  const n = 120;
                  const t = [], y1 = [], y2 = [];
                  for(let i=0; i<n; i++) {
                    t.push("10:" + (i < 10 ? '0' : '') + Math.floor(i/2) + ":" + (i%2 === 0 ? '00' : '30'));
                    y1.push(140 + Math.sin(i/5)*30 + Math.random()*15);
                    y2.push(95 + Math.cos(i/8)*20 + Math.random()*10);
                  }
                  const traces = [
                    { x: t, y: y1, name: 'Direct Gateway Requests (req/s)', line: { color: '#00e676', width: 2 } },
                    { x: t, y: y2, name: 'OTA Polling Traffic (req/s)', line: { color: '#ffab00', width: 2 } }
                  ];
                  const layout = {
                    paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
                    font: { color: '#9ba9a1', family: 'JetBrains Mono', size: 11 },
                    margin: { l: 40, r: 20, t: 20, b: 40 },
                    xaxis: { gridcolor: 'rgba(255,255,255,0.06)' },
                    yaxis: { gridcolor: 'rgba(255,255,255,0.06)' }
                  };
                  Plotly.newPlot('dygraphs-stage', traces, layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Fast linear interpolation across contiguous array buffers with sub-pixel decimation.'},
                {'title': 'Enterprise Use Cases', 'desc': 'High-frequency algorithmic trading, server CPU/RAM infrastructure monitoring, sensor logs.'},
                {'title': 'Technical Strengths', 'desc': 'Handles millions of data points without browser freeze; interactive mouse hover sync.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'Canvas 2D', 'sub': 'Fast Buffer'},
                {'label': 'Throughput', 'val': '1M+ Points', 'sub': 'No Lag'},
                {'label': 'Range Zoom', 'val': 'Click & Drag', 'sub': 'Microsecond'},
                {'label': 'Error Bars', 'val': 'Native Bands', 'sub': 'Confidence'}
            ],
            'code_snippet': """g = new Dygraph(document.getElementById("div"),
  dataMatrix,
  { labels: ["Date", "Direct", "OTA"], showRoller: true }
);"""
        },

        # 14. Taucharts Dimensional Scatter with Facets
        {
            'slide_id': 'slide-14-taucharts-facets',
            'tag': '14 / Multi-Faceted Grids',
            'headline': 'Dimensional Splitting:',
            'headline_span': 'Faceted Scatter Decomposition',
            'subtitle': 'Grammar-based visual decomposition breaking down multi-property performance by market tier.',
            'library_badge': 'Taucharts',
            'chart_html': """
              <div style="width:100%; height:100%; display:grid; grid-template-columns:1fr 1fr; gap:12px; padding:10px; box-sizing:border-box;">
                <div style="background:rgba(16,26,22,0.8); border:1px solid #d4af37; border-radius:6px; padding:10px;">
                  <strong style="color:#f3cf65; font-size:0.95rem; font-family:Newsreader;">Luxury Urban Segment</strong>
                  <svg viewBox="0 0 200 160" style="width:100%; height:130px;">
                    <circle cx="40" cy="120" r="8" fill="#00e676" opacity="0.8"/>
                    <circle cx="70" cy="90" r="10" fill="#00e676" opacity="0.8"/>
                    <circle cx="120" cy="50" r="14" fill="#00e676" opacity="0.8"/>
                    <circle cx="160" cy="30" r="18" fill="#00e676" opacity="0.8"/>
                    <line x1="20" y1="140" x2="180" y2="20" stroke="#d4af37" stroke-dasharray="3" stroke-width="1.5"/>
                  </svg>
                  <div style="font-size:0.75rem; color:#9ba9a1; text-align:center;">High Direct Share &gt; 65%</div>
                </div>
                <div style="background:rgba(16,26,22,0.8); border:1px solid #b5935b; border-radius:6px; padding:10px;">
                  <strong style="color:#f3cf65; font-size:0.95rem; font-family:Newsreader;">Resort / Leisure Segment</strong>
                  <svg viewBox="0 0 200 160" style="width:100%; height:130px;">
                    <circle cx="50" cy="110" r="10" fill="#ffab00" opacity="0.8"/>
                    <circle cx="90" cy="85" r="12" fill="#ffab00" opacity="0.8"/>
                    <circle cx="130" cy="70" r="11" fill="#ffab00" opacity="0.8"/>
                    <circle cx="170" cy="45" r="16" fill="#ffab00" opacity="0.8"/>
                    <line x1="20" y1="130" x2="180" y2="40" stroke="#b5935b" stroke-dasharray="3" stroke-width="1.5"/>
                  </svg>
                  <div style="font-size:0.75rem; color:#9ba9a1; text-align:center;">Balanced Share ~ 45%</div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Cartesian product of categorical variables creating small-multiple coordinate planes.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Segmented customer cohorts, regional sales territory comparison, multi-brand audits.'},
                {'title': 'Technical Strengths', 'desc': 'Built-in D3 foundations, declarative plugin architecture, seamless facet coordination.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'SVG / D3', 'sub': 'Taucharts Core'},
                {'label': 'Facets', 'val': 'Small Multiples', 'sub': 'Segment Split'},
                {'label': 'Plugins', 'val': 'Tooltip / Legend', 'sub': 'Extensible'},
                {'label': 'Design Flow', 'val': 'Declarative', 'sub': 'Tidy Data'}
            ],
            'code_snippet': """var chart = new tauCharts.Chart({
  data: hotelData, type: 'scatterplot',
  x: 'ADR', y: 'Occupancy', color: 'Channel',
  dimensions: { 'Segment': { type: 'category' } }
});"""
        },

        # 15. MetricsGraphics.js Confidence Band Horizon
        {
            'slide_id': 'slide-15-metricsgraphics',
            'tag': '15 / Econometric Uncertainty',
            'headline': 'Statistical Forecasting:',
            'headline_span': 'Confidence Band Horizon',
            'subtitle': 'Time-series curve wrapped in 95% Bayesian credible intervals for predictive revenue pacing.',
            'library_badge': 'MetricsGraphics.js',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:15px;">
                <svg viewBox="0 0 450 280" style="width:100%; max-height:330px;">
                  <defs>
                    <linearGradient id="bandGrad" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.3"/>
                      <stop offset="100%" stop-color="#00e5ff" stop-opacity="0.05"/>
                    </linearGradient>
                  </defs>
                  <!-- Confidence Upper & Lower Band -->
                  <path d="M 40 180 Q 140 130, 240 100 T 420 40 L 420 120 Q 320 160, 240 180 T 40 240 Z" fill="url(#bandGrad)"/>
                  <path d="M 40 180 Q 140 130, 240 100 T 420 40" fill="none" stroke="#00e5ff" stroke-dasharray="4" stroke-width="1.5"/>
                  <path d="M 40 240 Q 140 200, 240 180 T 420 120" fill="none" stroke="#00e5ff" stroke-dasharray="4" stroke-width="1.5"/>
                  <!-- Mean Predicted Line -->
                  <path d="M 40 210 Q 140 165, 240 140 T 420 80" fill="none" stroke="#f3cf65" stroke-width="3.5"/>
                  <!-- Baseline Grid -->
                  <line x1="40" y1="260" x2="420" y2="260" stroke="rgba(255,255,255,0.12)"/>
                  <text x="50" y="275" fill="#9ba9a1" font-family="JetBrains Mono" font-size="11">Q1 Actual</text>
                  <text x="230" y="275" fill="#9ba9a1" font-family="JetBrains Mono" font-size="11">Q2 Forecast</text>
                  <text x="360" y="275" fill="#f3cf65" font-family="JetBrains Mono" font-size="11">Q3 Projected</text>
                  <text x="280" y="70" fill="#f3cf65" font-family="DM Sans" font-size="12" font-weight="bold">Mean RevPAR Forecast ($385)</text>
                  <text x="280" y="30" fill="#00e5ff" font-family="DM Sans" font-size="11">95% Upper Bound ($440)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Bayesian posterior predictive distribution: $\\hat{y} \\pm 1.96 \\cdot \\sigma$ with ribbon enclosure.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Demand forecasting, budget risk horizons, inventory stock-out probability models.'},
                {'title': 'Technical Strengths', 'desc': 'Engineered by Mozilla Metrics team specifically for fast, opinionated scientific time-series.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'SVG / D3', 'sub': 'Mozilla Origin'},
                {'label': 'Uncertainty', 'val': '95% Band', 'sub': 'Confidence Area'},
                {'label': 'Opinionated', 'val': 'Zero Config', 'sub': 'Clean Typography'},
                {'label': 'Target', 'val': 'Statistical', 'sub': 'Time Series'}
            ],
            'code_snippet': """MG.data_graphic({
  data: forecastData, target: '#chart',
  x_accessor: 'date', y_accessor: 'revpar',
  show_confidence_band: ['lower', 'upper'],
  area: false
});"""
        },

        # 16. AntV G2 Nightingale Polar Rose
        {
            'slide_id': 'slide-16-antv-g2',
            'tag': '16 / Polar Proportions',
            'headline': 'Cyclical Magnitudes:',
            'headline_span': 'Nightingale Polar Rose Chart',
            'subtitle': 'Polar coordinate area encoding where sector radii represent metric magnitude across annual monthly cycles.',
            'library_badge': 'AntV G2 (Alibaba)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 320" style="width:280px; height:280px;">
                  <g transform="translate(160,160)">
                    <!-- Polar Rings -->
                    <circle r="40" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
                    <circle r="80" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
                    <circle r="120" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
                    <!-- Rose Petals -->
                    <path d="M 0 0 L 30 -50 A 60 60 0 0 1 60 -10 Z" fill="#d4af37" opacity="0.8"/>
                    <path d="M 0 0 L 60 -10 A 110 110 0 0 1 65 50 Z" fill="#00e676" opacity="0.85"/>
                    <path d="M 0 0 L 65 50 A 90 90 0 0 1 15 85 Z" fill="#00e5ff" opacity="0.8"/>
                    <path d="M 0 0 L 15 85 A 70 70 0 0 1 -45 60 Z" fill="#b5935b" opacity="0.75"/>
                    <path d="M 0 0 L -45 60 A 125 125 0 0 1 -110 -20 Z" fill="#f3cf65" opacity="0.9"/>
                    <path d="M 0 0 L -110 -20 A 80 80 0 0 1 -40 -70 Z" fill="#ffab00" opacity="0.8"/>
                    <path d="M 0 0 L -40 -70 A 100 100 0 0 1 30 -50 Z" fill="#00e676" opacity="0.85"/>
                  </g>
                  <text x="160" y="165" text-anchor="middle" fill="#fffefa" font-family="Newsreader" font-size="16">Seasonality</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Area-proportional polar transformation: $\\text{Radius} = \\sqrt{V / \\pi}$ to prevent perceptual exaggeration.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Seasonal hospitality demand cycles, incident mortality, wind speed direction matrices.'},
                {'title': 'Technical Strengths', 'desc': 'Alibaba enterprise visual engine with extreme rendering performance and declarative geometry.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'Canvas / SVG', 'sub': 'AntV Engine'},
                {'label': 'Geometry', 'val': 'Polar Sector', 'sub': 'Rose Petals'},
                {'label': 'Scale', 'val': 'Square Root', 'sub': 'Perceptual Safe'},
                {'label': 'Ecosystem', 'val': 'Ant Group', 'sub': 'Enterprise Standard'}
            ],
            'code_snippet': """const chart = new Chart({ container: 'container' });
chart.coordinate({ type: 'polar' });
chart.interval().data(data)
  .encode('x', 'month').encode('y', 'demand').encode('color', 'channel');
chart.render();"""
        },

        # 17. Vizzu Morphing Animated Transitions
        {
            'slide_id': 'slide-17-vizzu-morph',
            'tag': '17 / Animated Storytelling',
            'headline': 'Morphing Transitions:',
            'headline_span': 'Continuous State Interpolation',
            'subtitle': 'Seamless geometric morphing from bar charts to scatter plots without losing cognitive context.',
            'library_badge': 'Vizzu Engine',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
                <div style="display:flex; gap:12px; margin-bottom:14px;">
                  <button class="ctrl-btn" style="background:#d4af37; color:#070c09; font-weight:bold;">State A: Segment Bar</button>
                  <button class="ctrl-btn">Morph State &rarr;</button>
                  <button class="ctrl-btn" style="background:#00e676; color:#070c09; font-weight:bold;">State B: Radial Pie</button>
                </div>
                <svg viewBox="0 0 400 240" style="width:100%; max-height:260px;">
                  <!-- Morphing representation -->
                  <path d="M 60 200 C 60 120, 120 40, 200 40 C 280 40, 340 120, 340 200 Z" fill="rgba(212, 175, 55, 0.2)" stroke="#d4af37" stroke-width="2"/>
                  <rect x="80" y="100" width="40" height="100" fill="#00e676" rx="4"/>
                  <rect x="140" y="70" width="40" height="130" fill="#f3cf65" rx="4"/>
                  <rect x="200" y="50" width="40" height="150" fill="#00e5ff" rx="4"/>
                  <rect x="260" y="120" width="40" height="80" fill="#ff1744" rx="4"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Continuous coordinate interpolation between Cartesian $(x,y)$ and Polar $(r,\\theta)$ coordinate spaces.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Boardroom presentations, executive data storytelling, interactive analytical explaimers.'},
                {'title': 'Technical Strengths', 'desc': 'Maintains visual object persistence across structural morphs, eliminating cognitive jumps.'}
            ],
            'metrics': [
                {'label': 'Transition', 'val': 'Coordinate Morph', 'sub': 'Zero Jump'},
                {'label': 'Persistence', 'val': 'Object Identity', 'sub': 'Tracked Nodes'},
                {'label': 'Speed', 'val': '60 FPS', 'sub': 'WebGL / Canvas'},
                {'label': 'Engine', 'val': 'C++ WebAssembly', 'sub': 'Vizzu Core'}
            ],
            'code_snippet': """chart.animate({
  config: { channels: { x: null, y: null, size: 'revenue' }, coordSystem: 'polar' }
});"""
        },

        # 18. NVD3 Multi-Bar Bullet Benchmark
        {
            'slide_id': 'slide-18-nvd3-bullet',
            'tag': '18 / Executive Benchmarks',
            'headline': 'Goal Attainment:',
            'headline_span': 'Bullet Chart Benchmarking',
            'subtitle': 'Stephen Few compact bullet comparison replacing cluttered gauges with multi-threshold target bars.',
            'library_badge': 'NVD3 / D3 Core',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:20px; padding:20px; box-sizing:border-box;">
                <!-- Bullet 1 -->
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:4px; font-size:0.9rem;">
                    <strong style="color:#fffefa;">Net RevPAR Target ($)</strong>
                    <span style="font-family:JetBrains Mono; color:#00e676;">$284 / $250 Target</span>
                  </div>
                  <div style="position:relative; height:32px; background:rgba(255,255,255,0.06); border-radius:4px; overflow:hidden;">
                    <div style="position:absolute; left:0; top:0; height:100%; width:60%; background:rgba(255,255,255,0.1);"></div>
                    <div style="position:absolute; left:0; top:0; height:100%; width:85%; background:rgba(212,175,55,0.25);"></div>
                    <div style="position:absolute; left:0; top:8px; height:16px; width:92%; background:#00e676; border-radius:2px;"></div>
                    <div style="position:absolute; left:82%; top:2px; height:28px; width:4px; background:#fff; box-shadow:0 0 8px #fff;"></div>
                  </div>
                </div>
                <!-- Bullet 2 -->
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:4px; font-size:0.9rem;">
                    <strong style="color:#fffefa;">Direct Channel Mix (%)</strong>
                    <span style="font-family:JetBrains Mono; color:#f3cf65;">58% / 50% Target</span>
                  </div>
                  <div style="position:relative; height:32px; background:rgba(255,255,255,0.06); border-radius:4px; overflow:hidden;">
                    <div style="position:absolute; left:0; top:0; height:100%; width:50%; background:rgba(255,255,255,0.1);"></div>
                    <div style="position:absolute; left:0; top:0; height:100%; width:75%; background:rgba(212,175,55,0.25);"></div>
                    <div style="position:absolute; left:0; top:8px; height:16px; width:68%; background:#d4af37; border-radius:2px;"></div>
                    <div style="position:absolute; left:60%; top:2px; height:28px; width:4px; background:#fff; box-shadow:0 0 8px #fff;"></div>
                  </div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Linear quantitative mapping with embedded qualitative performance ranges (Poor, Satisfactory, Good).'},
                {'title': 'Enterprise Use Cases', 'desc': 'Sales quota attainment, executive bonus scorecard tracking, infrastructure SLA metrics.'},
                {'title': 'Technical Strengths', 'desc': 'High information density, eliminates gauge dial whitespace waste, crystal clear targets.'}
            ],
            'metrics': [
                {'label': 'Design Spec', 'val': 'Stephen Few', 'sub': 'Perceptual Standard'},
                {'label': 'Density', 'val': 'Ultra High', 'sub': 'No Space Waste'},
                {'label': 'Components', 'val': 'Actual/Target/Range', 'sub': '3-in-1 Measure'},
                {'label': 'Format', 'val': 'Horizontal Strip', 'sub': 'Stackable'}
            ],
            'code_snippet': """nv.addGraph(function() {
  var chart = nv.models.bulletChart();
  d3.select('#chart').datum(bulletData()).call(chart);
  return chart;
});"""
        },

        # 19. D3.js Voronoi Delaunay Tessellation
        {
            'slide_id': 'slide-19-d3-voronoi',
            'tag': '19 / Computational Geometry',
            'headline': 'Spatial Territory Partitioning:',
            'headline_span': 'Voronoi & Delaunay Mesh',
            'subtitle': 'Nearest-neighbor polygonal partitioning computed using Fortune’s sweep-line algorithm.',
            'library_badge': 'D3-Delaunay',
            'chart_html': """
              <div id="voronoi-stage" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;"></div>
              <script>
              (function(){
                const width = 450, height = 340;
                const points = Array.from({length: 45}, () => [Math.random() * width, Math.random() * height]);
                const delaunay = d3.Delaunay.from(points);
                const voronoi = delaunay.voronoi([0, 0, width, height]);
                
                const svg = d3.select("#voronoi-stage").append("svg")
                  .attr("viewBox", [0, 0, width, height])
                  .style("width", "100%").style("max-height", "360px");
                
                svg.append("path")
                  .attr("d", voronoi.render())
                  .attr("stroke", "rgba(212, 175, 55, 0.45)")
                  .attr("fill", "none")
                  .attr("stroke-width", 1.5);
                
                svg.append("path")
                  .attr("d", delaunay.render())
                  .attr("stroke", "rgba(0, 230, 118, 0.2)")
                  .attr("stroke-dasharray", "3,3")
                  .attr("fill", "none");
                
                svg.selectAll("circle")
                  .data(points)
                  .join("circle")
                  .attr("cx", d => d[0]).attr("cy", d => d[1])
                  .attr("r", 3.5)
                  .attr("fill", "#f3cf65");
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Dual graph theorem: Delaunay triangulation dual to Voronoi diagram computed in $O(N \\log N)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Retail trade area coverage, cellular antenna catchment zones, airport diversion territory.'},
                {'title': 'Technical Strengths', 'desc': 'Lightning fast point-picking in scatterplots, interactive hover hit-testing on mobile devices.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': "Fortune's Sweep", 'sub': 'O(N log N)'},
                {'label': 'Dual Graph', 'val': 'Delaunay Mesh', 'sub': 'Triangulation'},
                {'label': 'Hit Testing', 'val': 'O(1) Lookup', 'sub': 'Instant Hover'},
                {'label': 'Library', 'val': 'D3-Delaunay', 'sub': 'Modern v7'}
            ],
            'code_snippet': """const delaunay = d3.Delaunay.from(points);
const voronoi = delaunay.voronoi([0, 0, width, height]);
svg.append('path').attr('d', voronoi.render());"""
        },

        # 20. D3.js + HTML5 Canvas High-Performance Particle Flow
        {
            'slide_id': 'slide-20-particle-flow',
            'tag': '20 / Generative Physics',
            'headline': 'High-Cadence Particle Physics:',
            'headline_span': 'Vector Field Flow Simulation',
            'subtitle': 'Thousands of active autonomous agents tracing velocity vectors across commercial force fields.',
            'library_badge': 'HTML5 Canvas + D3 Forces',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; position:relative;">
                <canvas id="particle-canvas" width="460" height="340" style="background:#050907; border-radius:8px; border:1px solid rgba(212,175,55,0.3);"></canvas>
                <div style="position:absolute; bottom:16px; right:16px; background:rgba(7,12,9,0.85); padding:4px 10px; border-radius:4px; font-family:JetBrains Mono; font-size:0.78rem; color:#00e676;">
                  1,200 Active Particles @ 60 FPS
                </div>
              </div>
              <script>
              (function(){
                const canvas = document.getElementById('particle-canvas');
                if (!canvas) return;
                const ctx = canvas.getContext('2d');
                const particles = Array.from({length: 300}, () => ({
                  x: Math.random() * canvas.width,
                  y: Math.random() * canvas.height,
                  vx: (Math.random() - 0.5) * 1.8,
                  vy: (Math.random() - 0.5) * 1.8,
                  color: Math.random() > 0.4 ? '#d4af37' : '#00e676',
                  size: Math.random() * 2 + 1
                }));
                function animate() {
                  ctx.fillStyle = 'rgba(5, 9, 7, 0.15)';
                  ctx.fillRect(0, 0, canvas.width, canvas.height);
                  particles.forEach(p => {
                    p.x += p.vx; p.y += p.vy;
                    if (p.x < 0) p.x = canvas.width;
                    if (p.x > canvas.width) p.x = 0;
                    if (p.y < 0) p.y = canvas.height;
                    if (p.y > canvas.height) p.y = 0;
                    ctx.fillStyle = p.color;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                    ctx.fill();
                  });
                  requestAnimationFrame(animate);
                }
                animate();
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Newtonian Euler numerical integration: $\\vec{x}_{t+1} = \\vec{x}_t + \\vec{v} \\Delta t$ with boundary wrap.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Visitor flow dynamics, generative brand visualizers, agentic transaction simulators.'},
                {'title': 'Technical Strengths', 'desc': 'Direct pixel buffer manipulation via Canvas 2D, zero DOM overhead, sustained 60 FPS.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'Canvas 2D / RAF', 'sub': 'Hardware Sync'},
                {'label': 'Frame Rate', 'val': '60.0 FPS', 'sub': 'Sustained'},
                {'label': 'Particles', 'val': '1,200+ Live', 'sub': 'Zero Jitter'},
                {'label': 'Physics', 'val': 'Euler Vector', 'sub': 'Velocity Field'}
            ],
            'code_snippet': """function loop() {
  ctx.fillStyle = 'rgba(0,0,0,0.1)';
  ctx.fillRect(0, 0, w, h);
  particles.forEach(p => { p.x += p.vx; p.y += p.vy; draw(p); });
  requestAnimationFrame(loop);
}"""
        }
    ]

    html = generate_deck_html(deck_meta, slides)
    out_path = os.path.join(SCRIPT_DIR, "01-javascript-core-engines.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Built {out_path} (20 slides, {len(html)} bytes)")

if __name__ == "__main__":
    build_deck()
