"""
Builder for Deck 05: Python General, Statistical & Declarative Visualization
Generates 05-python-general-statistical.html (20 distinct visual paradigms)
"""
import os
from template_engine import generate_deck_html

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_deck():
    deck_meta = {
        'id': 'deck-05',
        'series_num': '05',
        'title': 'Python General, Statistical & Declarative Visualization',
        'category': 'Python Statistical & Declarative',
        'subtitle': '20 Analytical Paradigms across Matplotlib, Seaborn, Plotly Py, Bokeh, Altair, HoloViews, Pygal, Chartify, Plotnine, and HVPlot'
    }

    slides = [
        # 1. Seaborn JointGrid Bivariate KDE
        {
            'slide_id': 'slide-01-seaborn-jointgrid',
            'tag': '01 / Bivariate Density',
            'headline': 'Bivariate Probability Distributions:',
            'headline_span': 'Seaborn JointGrid with Marginals',
            'subtitle': 'Bivariate kernel density estimation with matched marginal univariate distribution histograms.',
            'library_badge': 'Seaborn / Matplotlib',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 300" style="width:100%; max-height:330px;">
                  <!-- Top Marginal Histogram (X) -->
                  <g fill="#00e676" opacity="0.6">
                    <rect x="70" y="25" width="20" height="15" rx="1"/>
                    <rect x="95" y="15" width="20" height="25" rx="1"/>
                    <rect x="120" y="8" width="20" height="32" rx="1"/>
                    <rect x="145" y="2" width="20" height="38" rx="1"/>
                    <rect x="170" y="12" width="20" height="28" rx="1"/>
                    <rect x="195" y="22" width="20" height="18" rx="1"/>
                  </g>
                  <!-- Right Marginal Histogram (Y) -->
                  <g fill="#d4af37" opacity="0.6">
                    <rect x="295" y="70" width="12" height="16" rx="1"/>
                    <rect x="295" y="90" width="26" height="16" rx="1"/>
                    <rect x="295" y="110" width="38" height="16" rx="1"/>
                    <rect x="295" y="130" width="30" height="16" rx="1"/>
                    <rect x="295" y="150" width="18" height="16" rx="1"/>
                  </g>
                  <!-- Central Contour Map -->
                  <rect x="60" y="45" width="230" height="180" fill="#0b1610" stroke="rgba(255,255,255,0.15)"/>
                  <ellipse cx="150" cy="130" rx="75" ry="50" fill="rgba(0,230,118,0.1)" stroke="#00e676" stroke-width="1.2"/>
                  <ellipse cx="150" cy="130" rx="50" ry="32" fill="rgba(212,175,55,0.18)" stroke="#d4af37" stroke-width="1.5"/>
                  <ellipse cx="150" cy="130" rx="25" ry="16" fill="rgba(243,207,101,0.3)" stroke="#f3cf65" stroke-width="2"/>
                  <circle cx="150" cy="130" r="4" fill="#fff"/>
                  <text x="150" y="125" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9">Peak Density Mode</text>
                  <!-- Labels -->
                  <text x="175" y="245" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Gross ADR ($)</text>
                  <text x="45" y="135" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="10" transform="rotate(-90, 45, 135)">Occupancy Rate (%)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': '2D Gaussian kernel density estimation: $\\hat{f}(x,y) = \\frac{1}{n} \\sum K_h(x - x_i, y - y_i)$ with 1D boundary projections.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Pricing elasticity vs occupancy tradeoffs, customer acquisition cost vs lifetime value.'},
                {'title': 'Technical Strengths', 'desc': 'Couples joint correlation structure with univariate distribution symmetry in one glance.'}
            ],
            'metrics': [
                {'label': 'Method', 'val': 'Bivariate KDE', 'sub': 'JointGrid'},
                {'label': 'Marginals', 'val': 'KDE + Hist', 'sub': 'Independent X, Y'},
                {'label': 'Python Lib', 'val': 'seaborn v0.13', 'sub': 'Matplotlib Base'},
                {'label': 'Bandwidth', 'val': "Scott's Rule", 'sub': 'Optimal h'}
            ],
            'code_snippet': """import seaborn as sns
g = sns.JointGrid(data=df, x="adr", y="occupancy")
g.plot_joint(sns.kdeplot, cmap="gold_d", fill=True)
g.plot_marginals(sns.histplot, kde=True, color="#00e676")"""
        },

        # 2. Altair Linked Interactive Scatter Matrix (SPLOM)
        {
            'slide_id': 'slide-02-altair-splom',
            'tag': '02 / Declarative Scatter Matrix',
            'headline': 'Exploratory Scatter Matrices:',
            'headline_span': 'Altair Linked Multi-Brush SPLOM',
            'subtitle': 'Declarative statistical grammar coordinating interval selections across all pairwise projections.',
            'library_badge': 'Altair (Vega-Lite Python)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 360 260" style="width:100%; max-height:280px;">
                  <!-- 2x2 Scatter Matrix -->
                  <g stroke="rgba(255,255,255,0.12)" stroke-width="1">
                    <rect x="40" y="30" width="135" height="95" fill="#0d1913"/>
                    <rect x="185" y="30" width="135" height="95" fill="#0d1913"/>
                    <rect x="40" y="135" width="135" height="95" fill="#0d1913"/>
                    <rect x="185" y="135" width="135" height="95" fill="#0d1913"/>
                  </g>
                  <!-- Scatter Points -->
                  <circle cx="70" cy="90" r="3.5" fill="#00e676"/>
                  <circle cx="110" cy="60" r="3.5" fill="#00e676"/>
                  <circle cx="140" cy="45" r="3.5" fill="#00e676"/>
                  <!-- Linked selection rectangle -->
                  <rect x="95" y="40" width="60" height="40" fill="rgba(212,175,55,0.2)" stroke="#d4af37" stroke-dasharray="2"/>
                  <!-- Other panes -->
                  <circle cx="210" cy="50" r="3.5" fill="#00e676"/>
                  <circle cx="260" cy="80" r="3.5" fill="#00e676"/>
                  <circle cx="300" cy="110" r="3.5" fill="#00e676"/>
                  <!-- Text labels -->
                  <text x="107" y="20" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">ADR ($)</text>
                  <text x="252" y="20" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">Net RevPAR ($)</text>
                  <text x="25" y="77" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="9" transform="rotate(-90, 25, 77)">Occ</text>
                  <text x="25" y="182" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="9" transform="rotate(-90, 25, 182)">TCA</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Pairwise Cartesian projection matrix: $\\mathbb{R}^k \\to \\binom{k}{2}$ coordinate planes with linked boolean predicates.'},
                {'title': 'Enterprise Use Cases', 'desc': 'High-dimensional feature space exploration, customer clustering, risk portfolio correlation.'},
                {'title': 'Technical Strengths', 'desc': 'Pure declarative Python code compiling directly to high-speed Vega-Lite JSON runtime.'}
            ],
            'metrics': [
                {'label': 'Syntax', 'val': 'Declarative Python', 'sub': 'alt.Chart(df)'},
                {'label': 'Selection', 'val': 'Interval Brush', 'sub': 'Bi-directional'},
                {'label': 'Backend', 'val': 'Vega-Lite JSON', 'sub': 'Zero JS Handcode'},
                {'label': 'Pairs', 'val': 'k x k Matrix', 'sub': 'All Dimensions'}
            ],
            'code_snippet': """brush = alt.selection_interval()
alt.Chart(df).mark_circle().encode(
    x=alt.X(alt.repeat("column"), type='quantitative'),
    y=alt.Y(alt.repeat("row"), type='quantitative'),
    color=alt.condition(brush, 'Channel:N', alt.value('grey'))
).repeat(row=['ADR', 'Occ'], column=['NetRevPAR', 'TCA']).add_params(brush)"""
        },

        # 3. Plotnine (ggplot2) Ridgeline / Joyplot Waves
        {
            'slide_id': 'slide-03-plotnine-ridges',
            'tag': '03 / Multi-Cohort Density',
            'headline': 'Ridgeline Joyplots:',
            'headline_span': 'Plotnine Staggered Density Waves',
            'subtitle': 'Staggered vertical density waves comparing booking lead-time distributions across seasonal months.',
            'library_badge': 'Plotnine (ggplot2 for Python)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 260" style="width:100%; max-height:280px;">
                  <!-- Wave 1: Jan -->
                  <path d="M 60 80 Q 140 30, 220 70 T 360 80 Z" fill="rgba(0,230,118,0.3)" stroke="#00e676" stroke-width="2"/>
                  <text x="50" y="80" text-anchor="end" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">Jan</text>
                  <!-- Wave 2: Apr -->
                  <path d="M 60 120 Q 180 60, 260 110 T 360 120 Z" fill="rgba(212,175,55,0.3)" stroke="#d4af37" stroke-width="2"/>
                  <text x="50" y="120" text-anchor="end" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">Apr</text>
                  <!-- Wave 3: Jul -->
                  <path d="M 60 160 Q 220 90, 300 150 T 360 160 Z" fill="rgba(243,207,101,0.35)" stroke="#f3cf65" stroke-width="2"/>
                  <text x="50" y="160" text-anchor="end" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">Jul</text>
                  <!-- Wave 4: Oct -->
                  <path d="M 60 200 Q 160 140, 240 190 T 360 200 Z" fill="rgba(0,229,255,0.3)" stroke="#00e5ff" stroke-width="2"/>
                  <text x="50" y="200" text-anchor="end" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">Oct</text>
                  <!-- X Axis -->
                  <line x1="60" y1="220" x2="360" y2="220" stroke="rgba(255,255,255,0.15)"/>
                  <text x="60" y="235" fill="#9ba9a1" font-family="JetBrains Mono" font-size="9">0 Days</text>
                  <text x="210" y="235" fill="#9ba9a1" font-family="JetBrains Mono" font-size="9">30 Days</text>
                  <text x="360" y="235" fill="#9ba9a1" font-family="JetBrains Mono" font-size="9">90 Days</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Overlapping 1D kernel density estimates displaced vertically by constant offset $\\Delta y$: $Y_i(x) = f_i(x) + i \\cdot \\delta$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Booking window compression, seasonal price sensitivity shifts, operational flight arrival delays.'},
                {'title': 'Technical Strengths', 'desc': 'Brings the legendary power and elegance of R\'s ggplot2 directly to Python data science workflows.'}
            ],
            'metrics': [
                {'label': 'Port Origin', 'val': 'R ggplot2', 'sub': 'Grammar of Graphics'},
                {'label': 'Density Type', 'val': 'Ridgeline Joyplot', 'sub': 'Overlapping Waves'},
                {'label': 'Aesthetics', 'val': 'aes(x, y, fill)', 'sub': 'Declarative'},
                {'label': 'Overlaps', 'val': 'Compact Stagger', 'sub': 'High Density'}
            ],
            'code_snippet': """from plotnine import *
(ggplot(df, aes(x='lead_time', y='month', fill='month'))
 + geom_density_ridges(alpha=0.6)
 + theme_dark())"""
        },

        # 4. Bokeh Multi-Line Hover Crossfilter
        {
            'slide_id': 'slide-04-bokeh-crossfilter',
            'tag': '04 / Web-Assembly & WebGL',
            'headline': 'High-Interaction Telemetry:',
            'headline_span': 'Bokeh Real-Time Hover Crossfilter',
            'subtitle': 'Fast Python server and standalone client-side JavaScript callback crossfilter dashboard.',
            'library_badge': 'Bokeh 3.4',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:15px; box-sizing:border-box;">
                <svg viewBox="0 0 450 250" style="width:100%; max-height:280px;">
                  <line x1="40" y1="210" x2="420" y2="210" stroke="rgba(255,255,255,0.15)"/>
                  <line x1="40" y1="40" x2="40" y2="210" stroke="rgba(255,255,255,0.15)"/>
                  <!-- Line 1: Direct -->
                  <path d="M 40 180 L 100 150 L 160 160 L 220 90 L 280 110 L 340 60 L 400 50" fill="none" stroke="#00e676" stroke-width="2.5"/>
                  <!-- Line 2: OTA -->
                  <path d="M 40 90 L 100 80 L 160 110 L 220 120 L 280 130 L 340 140 L 400 160" fill="none" stroke="#ff1744" stroke-width="2.5"/>
                  <!-- Hover Cursor Vertical Line -->
                  <line x1="220" y1="40" x2="220" y2="210" stroke="#f3cf65" stroke-dasharray="3" stroke-width="1.5"/>
                  <circle cx="220" cy="90" r="5" fill="#00e676" stroke="#fff" stroke-width="2"/>
                  <circle cx="220" cy="120" r="5" fill="#ff1744" stroke="#fff" stroke-width="2"/>
                  <!-- Hover Tooltip Box -->
                  <rect x="230" y="60" width="140" height="50" fill="#0e1713" stroke="#f3cf65" rx="4"/>
                  <text x="240" y="78" fill="#00e676" font-family="JetBrains Mono" font-size="10">Direct: $284 RevPAR</text>
                  <text x="240" y="96" fill="#ff1744" font-family="JetBrains Mono" font-size="10">OTA: $210 RevPAR</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Client-side ColumnDataSource data buffers communicating with BokehJS rendering engine.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Streaming financial trading desks, dynamic hotel revenue management controls, sensor arrays.'},
                {'title': 'Technical Strengths', 'desc': 'Enables Python data scientists to build complex interactive web apps without writing JavaScript.'}
            ],
            'metrics': [
                {'label': 'Architecture', 'val': 'Python -> BokehJS', 'sub': 'Zero JS Code'},
                {'label': 'Hover Tools', 'val': 'Sub-Pixel Hit', 'sub': 'Dynamic Tooltip'},
                {'label': 'Server Mode', 'val': 'Tornado WebSockets', 'sub': 'Bidirectional'},
                {'label': 'Performance', 'val': 'Canvas Accelerated', 'sub': 'Smooth Drag'}
            ],
            'code_snippet': """from bokeh.plotting import figure, show
p = figure(title="RevPAR Trajectory", hover_tool=True)
p.line(x='date', y='direct', source=source, color='#00e676', line_width=2)
p.line(x='date', y='ota', source=source, color='#ff1744', line_width=2)"""
        },

        # 5. Plotly Py Interactive Financial Waterfall
        {
            'slide_id': 'slide-05-plotly-waterfall',
            'tag': '05 / Financial Ledger Ledgers',
            'headline': 'Net Margin Reconciliations:',
            'headline_span': 'Plotly Py Financial Waterfall',
            'subtitle': 'Stepwise margin reconciliation tracing Gross Room Revenue minus intermediary deductions down to Net Cashflow.',
            'library_badge': 'plotly.graph_objects',
            'chart_html': """
              <div id="plotly-waterfall-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('plotly-waterfall-stage');
                  if (!el || !window.Plotly) return;
                  const data = [{
                    type: "waterfall",
                    orientation: "v",
                    measure: ["relative", "relative", "relative", "relative", "total"],
                    x: ["Gross RevPAR", "Brand PPC", "Meta Bid", "OTA Comm.", "Net RevPAR"],
                    textposition: "outside",
                    text: ["+$340", "-$18", "-$22", "-$54", "$246"],
                    y: [340, -18, -22, -54, 246],
                    connector: { line: { color: "rgba(212,175,55,0.6)", width: 1.5 } },
                    increasing: { marker: { color: "#00e676" } },
                    decreasing: { marker: { color: "#ff1744" } },
                    totals: { marker: { color: "#d4af37" } }
                  }];
                  const layout = {
                    paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
                    font: { color: '#fffefa', family: 'DM Sans', size: 12 },
                    margin: { l: 40, r: 20, t: 25, b: 35 },
                    yaxis: { gridcolor: 'rgba(255,255,255,0.06)' },
                    xaxis: { gridcolor: 'rgba(255,255,255,0.06)' }
                  };
                  Plotly.newPlot('plotly-waterfall-stage', data, layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Discrete cumulative step summation: $S_k = \\sum_{i=1}^k \\Delta y_i$ with directional floating bar geometry.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel P&L reconciliations, EBITDA variance bridges, gross-to-net commercial leakage audits.'},
                {'title': 'Technical Strengths', 'desc': 'Standard financial board reporting visual; native interactive tooltip and bar hovering.'}
            ],
            'metrics': [
                {'label': 'Chart Type', 'val': 'Financial Waterfall', 'sub': 'EBITDA Bridge'},
                {'label': 'Cumulative', 'val': 'Running Balance', 'sub': 'Auto-Totaled'},
                {'label': 'Coloring', 'val': 'Tri-Tone Logic', 'sub': 'Gain/Deduction'},
                {'label': 'Python Spec', 'val': 'go.Waterfall', 'sub': 'Plotly Py'}
            ],
            'code_snippet': """import plotly.graph_objects as go
fig = go.Figure(go.Waterfall(
    measure=["relative", "relative", "total"],
    x=["Gross Revenue", "Intermediation", "Net EBITDA"],
    y=[340, -94, 246]
))"""
        },

        # 6. Matplotlib 3D Parametric Mesh
        {
            'slide_id': 'slide-06-matplotlib-3d',
            'tag': '06 / Parametric Surfaces',
            'headline': 'Wireframe Surfaces:',
            'headline_span': 'Matplotlib mplot3d Parametric Mesh',
            'subtitle': 'Mathematical elevation manifold showing revenue yield optimization frontiers across ADR and Occupancy.',
            'library_badge': 'Matplotlib mplot3d',
            'chart_html': """
              <div id="mpl-3d-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('mpl-3d-stage');
                  if (!el || !window.Plotly) return;
                  const z = [];
                  for(let i=0; i<20; i++) {
                    const row = [];
                    for(let j=0; j<20; j++) {
                      row.push(Math.sin(i/3) * Math.cos(j/3) * 30 + 50);
                    }
                    z.push(row);
                  }
                  Plotly.newPlot('mpl-3d-stage', [{
                    z: z, type: 'surface',
                    colorscale: [[0, '#0e1713'], [0.5, '#b5935b'], [1, '#00e676']]
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
                {'title': 'Mathematical Engine', 'desc': 'Bivariate parametric mesh $(x(u,v), y(u,v), z(u,v))$ evaluated over structured 2D grid meshes.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Revenue management price-sensitivity manifolds, engineering stress surfaces, scientific simulations.'},
                {'title': 'Technical Strengths', 'desc': 'The venerable industry foundation of Python scientific plotting; pixel-perfect publication figures.'}
            ],
            'metrics': [
                {'label': 'Toolkit', 'val': 'mpl_toolkits.mplot3d', 'sub': 'Matplotlib Core'},
                {'label': 'Projection', 'val': 'Perspective 3D', 'sub': 'Azimuth/Elev'},
                {'label': 'Output', 'val': 'SVG / PDF / PNG', 'sub': 'Publication Std'},
                {'label': 'Precision', 'val': 'Vector Exact', 'sub': 'Arbitrary DPI'}
            ],
            'code_snippet': """from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, Z, cmap='viridis')"""
        },

        # 7. HoloViews Streamgraph
        {
            'slide_id': 'slide-07-holoviews-stream',
            'tag': '07 / Organic Temporal Flows',
            'headline': 'Fluid Continuous Shares:',
            'headline_span': 'HoloViews Organic Streamgraph',
            'subtitle': 'Zero-baseline centered stacked area stream tracking shifting channel volume proportions organically over time.',
            'library_badge': 'HoloViews / Bokeh',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 240" style="width:100%; max-height:270px;">
                  <!-- Stream Layers (Centered around Y=120) -->
                  <!-- Layer 1: Direct Web -->
                  <path d="M 40 120 C 120 70, 200 40, 280 60 C 340 70, 380 50, 400 60 L 400 130 C 360 120, 280 140, 200 130 C 120 125, 60 130, 40 120 Z" fill="#00e676" opacity="0.8"/>
                  <!-- Layer 2: Google Meta -->
                  <path d="M 40 120 C 60 130, 120 125, 200 130 C 280 140, 360 120, 400 130 L 400 180 C 360 170, 280 190, 200 180 C 120 170, 60 150, 40 120 Z" fill="#d4af37" opacity="0.85"/>
                  <!-- Layer 3: OTAs -->
                  <path d="M 40 120 C 60 150, 120 170, 200 180 C 280 190, 360 170, 400 180 L 400 210 C 340 205, 280 215, 200 205 C 120 195, 60 170, 40 120 Z" fill="#ff1744" opacity="0.75"/>
                  <!-- Text Labels inside stream -->
                  <text x="320" y="95" fill="#070c09" font-family="DM Sans" font-size="11" font-weight="bold">Direct (54%)</text>
                  <text x="320" y="155" fill="#070c09" font-family="DM Sans" font-size="11" font-weight="bold">Meta (28%)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Lee Byron / Martin Wattenberg silhouette baseline algorithm minimizing organic layer slope changes: $\\min \\sum (\\frac{dy}{dx})^2$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Topic trends over time in media, music genre listening share evolution, seasonal channel mix.'},
                {'title': 'Technical Strengths', 'desc': 'High aesthetic appeal, conveys organic ebb and flow without harsh rectilinear bar angles.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': 'Byron-Wattenberg', 'sub': 'Wiggle Min'},
                {'label': 'Baseline', 'val': 'Silhouette Center', 'sub': 'Zero Centered'},
                {'label': 'Ecosystem', 'val': 'PyData / HoloViz', 'sub': 'Composable'},
                {'label': 'Design Tone', 'val': 'Organic Fluid', 'sub': 'Editorial Standard'}
            ],
            'code_snippet': """import holoviews as hv
hv.extension('bokeh')
stream = hv.Area.stack(hv.Overlay([
    hv.Area((dates, shares[ch]), label=ch) for ch in channels
])).opts(baseline='wiggle')"""
        },

        # 8. Pygal Responsive Clean SVG Radar
        {
            'slide_id': 'slide-08-pygal-radar',
            'tag': '08 / Vector Scalability',
            'headline': 'Lightweight Vector Spiders:',
            'headline_span': 'Pygal Responsive SVG Radar',
            'subtitle': 'Zero-dependency standalone SVG generator engineered for clean web integration.',
            'library_badge': 'Pygal Python SVG',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 300 280" style="width:260px; height:240px;">
                  <!-- Hexagonal Grid Rings -->
                  <polygon points="150,30 240,80 240,180 150,230 60,180 60,80" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
                  <polygon points="150,70 205,100 205,160 150,190 95,160 95,100" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
                  <!-- Benchmark Polygon (Direct) -->
                  <polygon points="150,40 230,85 220,170 150,215 75,175 80,85" fill="rgba(0,230,118,0.25)" stroke="#00e676" stroke-width="2"/>
                  <!-- Secondary Polygon (OTA) -->
                  <polygon points="150,100 180,115 170,150 150,170 110,145 115,115" fill="rgba(255,23,68,0.2)" stroke="#ff1744" stroke-width="1.5"/>
                  <circle cx="150" cy="40" r="4" fill="#00e676"/>
                  <circle cx="230" cy="85" r="4" fill="#00e676"/>
                  <circle cx="220" cy="170" r="4" fill="#00e676"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Equiangular polar mapping compiled directly into clean, human-readable W3C SVG XML markup.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Automated PDF/email executive summary reporting, embedded web widgets with zero JavaScript dependencies.'},
                {'title': 'Technical Strengths', 'desc': 'Zero client-side JS needed; loads instantly in emails, print brochures, and responsive web pages.'}
            ],
            'metrics': [
                {'label': 'Format', 'val': 'Pure XML / SVG', 'sub': 'Zero JS Req.'},
                {'label': 'Styling', 'val': 'CSS Injected', 'sub': 'Theme Aware'},
                {'label': 'File Size', 'val': '< 8 KB Output', 'sub': 'Instant Transfer'},
                {'label': 'Email Ready', 'val': '100% Compatible', 'sub': 'Outlook / Gmail'}
            ],
            'code_snippet': """import pygal
radar = pygal.Radar(fill=True)
radar.x_labels = ['Direct', 'Rate Parity', 'CDP', 'AI Discovery']
radar.add('Sovereign Asset', [90, 85, 92, 88])
radar.render_to_file('report.svg')"""
        },

        # 9. Chartify Corporate Proportions with Callouts
        {
            'slide_id': 'slide-09-chartify-proportions',
            'tag': '09 / Spotify Data Viz',
            'headline': 'Corporate Editorial Clarity:',
            'headline_span': 'Chartify Proportional Stacked Bar',
            'subtitle': 'Spotify corporate data science framework designed for C-Suite clarity and executive presentation standards.',
            'library_badge': 'Chartify (Spotify Open Source)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:20px; box-sizing:border-box;">
                <div style="border-left:3px solid #00e676; padding-left:12px; margin-bottom:14px;">
                  <strong style="color:#fffefa; font-family:Newsreader; font-size:1.3rem;">FY26 Channel Contribution Share</strong>
                  <div style="font-size:0.85rem; color:#9ba9a1;">Key Finding: Direct Web surpassed OTAs by +14 percentage points.</div>
                </div>
                <!-- Stacked Bar -->
                <div style="height:36px; display:flex; border-radius:4px; overflow:hidden; border:1px solid #d4af37;">
                  <div style="width:54%; background:#00e676; display:flex; align-items:center; justify-content:center; color:#070c09; font-weight:bold; font-family:JetBrains Mono; font-size:0.85rem;">Direct 54%</div>
                  <div style="width:26%; background:#d4af37; display:flex; align-items:center; justify-content:center; color:#070c09; font-weight:bold; font-family:JetBrains Mono; font-size:0.85rem;">Meta 26%</div>
                  <div style="width:20%; background:#ff1744; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-family:JetBrains Mono; font-size:0.85rem;">OTA 20%</div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Normalized 100% proportional horizontal stacking with automated typography and label contrast calculations.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Annual investor letters, quarterly board slide decks, corporate strategic reviews.'},
                {'title': 'Technical Strengths', 'desc': 'Enforces corporate brand consistency and eliminates ugly default charting mistakes automatically.'}
            ],
            'metrics': [
                {'label': 'Origin', 'val': 'Spotify Lab', 'sub': 'Data Science Std'},
                {'label': 'Design Focus', 'val': 'Executive Board', 'sub': 'Publication Ready'},
                {'label': 'Under the Hood', 'val': 'Bokeh Core', 'sub': 'Interactive'},
                {'label': 'Callouts', 'val': 'Automatic', 'sub': 'Narrative Title'}
            ],
            'code_snippet': """import chartify
ch = chartify.Chart(blank_labels=True, x_axis_type='linear')
ch.set_title("FY26 Channel Contribution Share")
ch.plot.bar_stacked(data_frame=df, categorical_columns='year', numeric_column='share')"""
        },

        # 10. Seaborn Clustermap with Hierarchical Dendrogram Trees
        {
            'slide_id': 'slide-10-seaborn-clustermap',
            'tag': '10 / Hierarchical Clustering',
            'headline': 'Agglomerative Clustering:',
            'headline_span': 'Seaborn Clustermap with Trees',
            'subtitle': 'Unsupervised hierarchical clustering re-ordering hotel property rows and channels via Ward’s linkage distance.',
            'library_badge': 'Seaborn / SciPy Cluster',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 260" style="width:100%; max-height:280px;">
                  <!-- Top Dendrogram Tree -->
                  <g stroke="#d4af37" stroke-width="1.2" fill="none">
                    <line x1="120" y1="50" x2="120" y2="30"/>
                    <line x1="180" y1="50" x2="180" y2="30"/>
                    <line x1="120" y1="30" x2="180" y2="30"/>
                    <line x1="150" y1="30" x2="150" y2="15"/>
                    <line x1="240" y1="50" x2="240" y2="15"/>
                    <line x1="150" y1="15" x2="240" y2="15"/>
                  </g>
                  <!-- 3x3 Heatmap Cells -->
                  <g transform="translate(80, 60)">
                    <rect x="0" y="0" width="50" height="40" fill="#00e676"/>
                    <rect x="55" y="0" width="50" height="40" fill="#00e676" opacity="0.8"/>
                    <rect x="110" y="0" width="50" height="40" fill="#d4af37"/>
                    <rect x="0" y="45" width="50" height="40" fill="#00e676" opacity="0.7"/>
                    <rect x="55" y="45" width="50" height="40" fill="#d4af37"/>
                    <rect x="110" y="45" width="50" height="40" fill="#ff1744"/>
                    <rect x="0" y="90" width="50" height="40" fill="#d4af37"/>
                    <rect x="55" y="90" width="50" height="40" fill="#ff1744"/>
                    <rect x="110" y="90" width="50" height="40" fill="#ff1744" opacity="0.8"/>
                  </g>
                  <!-- Row Dendrogram (Left) -->
                  <g stroke="#00e676" stroke-width="1.2" fill="none">
                    <line x1="70" y1="80" x2="50" y2="80"/>
                    <line x1="70" y1="125" x2="50" y2="125"/>
                    <line x1="50" y1="80" x2="50" y2="125"/>
                    <line x1="50" y1="102" x2="30" y2="102"/>
                    <line x1="70" y1="170" x2="30" y2="170"/>
                    <line x1="30" y1="102" x2="30" y2="170"/>
                  </g>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Ward\'s minimum variance hierarchical agglomerative clustering: $d(u,v) = \\sqrt{\\frac{|u||v|}{|u|+|v|}} \\|\\bar{u} - \\bar{v}\\|_2$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel property portfolio segmentation, genomic expression profiling, customer RFM clustering.'},
                {'title': 'Technical Strengths', 'desc': 'Reorders rows and columns so similar behaving assets group together automatically.'}
            ],
            'metrics': [
                {'label': 'Clustering', 'val': "Ward's Linkage", 'sub': 'Min Variance'},
                {'label': 'Distance', 'val': 'Euclidean Metric', 'sub': 'Pairwise D'},
                {'label': 'Dendrogram', 'val': 'Dual Row/Col', 'sub': 'Biclustering'},
                {'label': 'Package', 'val': 'SciPy + Seaborn', 'sub': 'Agglomerative'}
            ],
            'code_snippet': """import seaborn as sns
sns.clustermap(matrix_df, method='ward', metric='euclidean',
              cmap='viridis', standard_scale=1)"""
        },

        # 11. Plotnine Violin Plot with Jitter & Quantiles
        {
            'slide_id': 'slide-11-plotnine-violin',
            'tag': '11 / Distribution Anatomy',
            'headline': 'Distribution Anatomy:',
            'headline_span': 'Violin Plots with Jitter & Boxplot',
            'subtitle': 'Full nonparametric kernel density combined with interquartile ranges and individual point observations.',
            'library_badge': 'Plotnine / Matplotlib',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Violin 1: Direct Web -->
                  <g transform="translate(100, 20)">
                    <path d="M 0 30 C 25 50, 30 80, 15 120 C 5 140, 20 160, 0 180 C -20 160, -5 140, -15 120 C -30 80, -25 50, 0 30 Z" fill="rgba(0,230,118,0.25)" stroke="#00e676" stroke-width="2"/>
                    <!-- Inner Boxplot -->
                    <line x1="0" y1="50" x2="0" y2="160" stroke="#fff" stroke-width="2"/>
                    <rect x="-6" y="80" width="12" height="50" fill="#13221b" stroke="#fff" stroke-width="1.5"/>
                    <circle cx="0" cy="105" r="3" fill="#f3cf65"/>
                    <text x="0" y="200" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="11">Direct Web</text>
                  </g>
                  <!-- Violin 2: OTA Intermediary -->
                  <g transform="translate(250, 20)">
                    <path d="M 0 50 C 18 70, 25 110, 10 140 C 5 155, 15 170, 0 180 C -15 170, -5 155, -10 140 C -25 110, -18 70, 0 50 Z" fill="rgba(255,23,68,0.25)" stroke="#ff1744" stroke-width="2"/>
                    <line x1="0" y1="70" x2="0" y2="160" stroke="#fff" stroke-width="2"/>
                    <rect x="-6" y="100" width="12" height="45" fill="#13221b" stroke="#fff" stroke-width="1.5"/>
                    <circle cx="0" cy="122" r="3" fill="#f3cf65"/>
                    <text x="0" y="200" text-anchor="middle" fill="#ff1744" font-family="DM Sans" font-size="11">OTA Channel</text>
                  </g>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Mirrored continuous kernel density estimate $\\pm \\hat{f}(y)$ with median, IQR, and whisker overlays.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Evaluating multi-modal revenue distributions that hide inside deceptive mean averages.'},
                {'title': 'Technical Strengths', 'desc': 'Exposes bi-modal and skewed distributions that standard boxplots completely conceal.'}
            ],
            'metrics': [
                {'label': 'Density', 'val': 'Mirrored KDE', 'sub': 'Symmetric Area'},
                {'label': 'Summary', 'val': 'Tukey Boxplot', 'sub': 'IQR + Median'},
                {'label': 'Outliers', 'val': 'Raw Jitter', 'sub': 'Scatter Overlay'},
                {'label': 'Multi-Modal', 'val': 'Exposed', 'sub': 'Hidden Peaks'}
            ],
            'code_snippet': """(ggplot(df, aes(x='channel', y='net_adr', fill='channel'))
 + geom_violin(alpha=0.4)
 + geom_boxplot(width=0.1, fill='black')
 + geom_jitter(width=0.05, alpha=0.3))"""
        },

        # 12. Matplotlib Polar Wind Rose
        {
            'slide_id': 'slide-012-wind-rose',
            'tag': '12 / Directional Binning',
            'headline': 'Directional Frequency:',
            'headline_span': 'Matplotlib Polar Wind Rose',
            'subtitle': 'Directional circular histogram sorting geographic arrival origins and booking velocity by vector.',
            'library_badge': 'Matplotlib Polar',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 280 280" style="width:250px; height:250px;">
                  <circle cx="140" cy="140" r="100" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
                  <circle cx="140" cy="140" r="60" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
                  <!-- Polar Spokes -->
                  <line x1="140" y1="40" x2="140" y2="240" stroke="rgba(255,255,255,0.1)"/>
                  <line x1="40" y1="140" x2="240" y2="140" stroke="rgba(255,255,255,0.1)"/>
                  <!-- Stacked Polar Bins -->
                  <path d="M 140 140 L 150 50 A 90 90 0 0 0 130 50 Z" fill="#00e676"/>
                  <path d="M 140 140 L 220 120 A 85 85 0 0 0 220 160 Z" fill="#d4af37"/>
                  <path d="M 140 140 L 125 210 A 70 70 0 0 0 155 210 Z" fill="#ffab00"/>
                  <path d="M 140 140 L 65 155 A 80 80 0 0 0 65 125 Z" fill="#00e5ff"/>
                  <!-- Cardinal Labels -->
                  <text x="140" y="32" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="10">N (Europe)</text>
                  <text x="255" y="144" fill="#f3cf65" font-family="JetBrains Mono" font-size="10">E (APAC)</text>
                  <text x="140" y="258" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="10">S (ANZ)</text>
                  <text x="25" y="144" text-anchor="end" fill="#f3cf65" font-family="JetBrains Mono" font-size="10">W (US)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': '2D circular binning: partitioning vector angles $\\theta \\in [0, 2\\pi)$ and metric speeds into stacked radial sectors.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Atmospheric wind energy farm placement, maritime port navigation, seasonal international flight arrivals.'},
                {'title': 'Technical Strengths', 'desc': 'Native Matplotlib polar projection (`projection=\'polar\'`) with full bar stacking capabilities.'}
            ],
            'metrics': [
                {'label': 'Projection', 'val': 'Polar Theta-R', 'sub': 'Cyclical 360°'},
                {'label': 'Binning', 'val': '16 Compass Points', 'sub': 'Stacked Bar'},
                {'label': 'Radius', 'val': 'Proportional', 'sub': 'Frequency'},
                {'label': 'Colors', 'val': 'Speed Quantiles', 'sub': 'Multicolor Stack'}
            ],
            'code_snippet': """ax = plt.subplot(111, polar=True)
ax.bar(theta, radii, width=width, bottom=0.0, color='#00e676')"""
        },

        # 13. Altair Horizon Chart for Multi-Subject Compact Time-Series
        {
            'slide_id': 'slide-13-altair-horizon',
            'tag': '13 / High-Density Time Series',
            'headline': 'Extreme Vertical Density:',
            'headline_span': 'Altair Folded Horizon Chart',
            'subtitle': 'Folds high-amplitude time series into banded color density strips, conserving 85% vertical screen space.',
            'library_badge': 'Altair Horizon',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:8px; padding:20px; box-sizing:border-box;">
                <!-- Strip 1 -->
                <div style="height:26px; background:#101a16; border:1px solid #d4af37; border-radius:3px; position:relative; overflow:hidden;">
                  <div style="position:absolute; left:20%; width:30%; height:100%; background:#00e676; opacity:0.4;"></div>
                  <div style="position:absolute; left:28%; width:15%; height:100%; background:#00e676; opacity:0.8;"></div>
                  <span style="position:absolute; left:8px; top:5px; font-family:JetBrains Mono; font-size:0.75rem; color:#fff;">Asset SG-01 (Peak: +42%)</span>
                </div>
                <!-- Strip 2 -->
                <div style="height:26px; background:#101a16; border:1px solid #d4af37; border-radius:3px; position:relative; overflow:hidden;">
                  <div style="position:absolute; left:45%; width:40%; height:100%; background:#f3cf65; opacity:0.4;"></div>
                  <div style="position:absolute; left:60%; width:20%; height:100%; background:#f3cf65; opacity:0.8;"></div>
                  <span style="position:absolute; left:8px; top:5px; font-family:JetBrains Mono; font-size:0.75rem; color:#fff;">Asset UK-04 (Peak: +28%)</span>
                </div>
                <!-- Strip 3 -->
                <div style="height:26px; background:#101a16; border:1px solid #d4af37; border-radius:3px; position:relative; overflow:hidden;">
                  <div style="position:absolute; left:10%; width:50%; height:100%; background:#ff1744; opacity:0.4;"></div>
                  <div style="position:absolute; left:20%; width:25%; height:100%; background:#ff1744; opacity:0.8;"></div>
                  <span style="position:absolute; left:8px; top:5px; font-family:JetBrains Mono; font-size:0.75rem; color:#fff;">Asset JP-02 (Lag: -18%)</span>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Modulo-height folding: values exceeding threshold $H$ wrap to bottom with intensified color saturation.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Monitoring 100+ hotel properties simultaneously on a single executive dashboard display.'},
                {'title': 'Technical Strengths', 'desc': 'Permits dense vertical stacking of 50 time-series in the space normally required for 3 line charts.'}
            ],
            'metrics': [
                {'label': 'Space Saving', 'val': '85% Vertical', 'sub': 'Folded Bands'},
                {'label': 'Bands', 'val': '3-4 Color Steps', 'sub': 'Value = Saturation'},
                {'label': 'Scalability', 'val': '100+ Assets', 'sub': 'Single Screen'},
                {'label': 'Resolution', 'val': 'Preserved', 'sub': 'Zero Downsample'}
            ],
            'code_snippet': """alt.Chart(df).mark_area().encode(
    x='date:T', y='y_folded:Q',
    color=alt.Color('band:O', scale=alt.Scale(scheme='goldgreen'))
)"""
        },

        # 14. Seaborn PairGrid with Custom Diagonal Histograms
        {
            'slide_id': 'slide-14-seaborn-pairgrid',
            'tag': '14 / Matrix Diagnostics',
            'headline': 'Faceted Multi-Variables:',
            'headline_span': 'Seaborn PairGrid Diagnostics',
            'subtitle': 'Subplot grid pairing univariate kernel histograms on diagonal with bivariate linear regressions off-diagonal.',
            'library_badge': 'Seaborn PairGrid',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 240" style="width:100%; max-height:260px;">
                  <!-- 2x2 Diagnostics Grid -->
                  <!-- Top-Left: Hist 1 -->
                  <rect x="30" y="20" width="110" height="90" fill="#0e1713" stroke="rgba(255,255,255,0.1)"/>
                  <path d="M 40 100 Q 85 40, 130 100 Z" fill="#00e676" opacity="0.6"/>
                  <!-- Top-Right: Scatter + Regress -->
                  <rect x="160" y="20" width="110" height="90" fill="#0e1713" stroke="rgba(255,255,255,0.1)"/>
                  <circle cx="180" cy="85" r="3" fill="#f3cf65"/>
                  <circle cx="210" cy="65" r="3" fill="#f3cf65"/>
                  <circle cx="240" cy="45" r="3" fill="#f3cf65"/>
                  <line x1="170" y1="95" x2="260" y2="35" stroke="#d4af37" stroke-width="1.5"/>
                  <!-- Bottom-Left: KDE Contours -->
                  <rect x="30" y="125" width="110" height="90" fill="#0e1713" stroke="rgba(255,255,255,0.1)"/>
                  <ellipse cx="85" cy="170" rx="35" ry="20" fill="none" stroke="#00e5ff" stroke-width="1.5"/>
                  <!-- Bottom-Right: Hist 2 -->
                  <rect x="160" y="125" width="110" height="90" fill="#0e1713" stroke="rgba(255,255,255,0.1)"/>
                  <path d="M 170 205 Q 215 150, 260 205 Z" fill="#d4af37" opacity="0.6"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Subplot dispatch mapping: $M_{i,j} = \\text{regplot}$ when $i \\neq j$ and $M_{i,i} = \\text{histplot}$ along main diagonal.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Econometric multicollinearity audits, regression residual analysis, marketing mix modeling (MMM).'},
                {'title': 'Technical Strengths', 'desc': 'Custom callback functions can be mapped to upper, lower, and diagonal triangles independently.'}
            ],
            'metrics': [
                {'label': 'Dispatch', 'val': 'Tri-Partite', 'sub': 'Diag / Upper / Lower'},
                {'label': 'Regressions', 'val': 'OLS Fitted', 'sub': 'Confidence Shaded'},
                {'label': 'Hue Mapping', 'val': 'Categorical', 'sub': 'Color Coded'},
                {'label': 'Library', 'val': 'Seaborn Engine', 'sub': 'Matplotlib Grid'}
            ],
            'code_snippet': """g = sns.PairGrid(df, hue="segment")
g.map_diag(sns.histplot, kde=True)
g.map_offdiag(sns.regplot, scatter_kws={'alpha':0.4})"""
        },

        # 15. Plotly Py Interactive Polar Sunburst
        {
            'slide_id': 'slide-15-plotly-sunburst',
            'tag': '15 / Multi-Tier Proportions',
            'headline': 'Nested Multi-Tiers:',
            'headline_span': 'Plotly Py Interactive Sunburst',
            'subtitle': 'Clickable multi-level radial partition expanding market demand segments into localized room tiers.',
            'library_badge': 'plotly.express.sunburst',
            'chart_html': """
              <div id="plotly-py-sunburst-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('plotly-py-sunburst-stage');
                  if (!el || !window.Plotly) return;
                  const data = [{
                    type: "sunburst",
                    labels: ["Portfolio", "Direct", "OTA", "Meta", "Web", "App", "Booking", "Expedia", "Google HPA"],
                    parents: ["", "Portfolio", "Portfolio", "Portfolio", "Direct", "Direct", "OTA", "OTA", "Meta"],
                    values:  [100, 54, 28, 18, 36, 18, 18, 10, 18],
                    marker: { colors: ["#070c09", "#00e676", "#ff1744", "#d4af37", "#2d5a44", "#6a7952", "#b84a39", "#d9534f", "#f3cf65"] },
                    branchvalues: 'total'
                  }];
                  Plotly.newPlot('plotly-py-sunburst-stage', data, {
                    paper_bgcolor: 'transparent',
                    font: { color: '#fffefa', family: 'DM Sans', size: 12 },
                    margin: { l: 0, r: 0, b: 0, t: 0 }
                  }, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Proportional angular allocation $\\Delta \\theta_i = 2\\pi (V_i / \\sum V)$ nested across concentric hierarchical radii.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Enterprise software cost attribution, global hotel company brand portfolio breakdown.'},
                {'title': 'Technical Strengths', 'desc': 'Native animated click-to-zoom drilldown in modern browsers with zero external plugin overhead.'}
            ],
            'metrics': [
                {'label': 'Python API', 'val': 'px.sunburst', 'sub': 'One-Liner Call'},
                {'label': 'Drilldown', 'val': 'Animated Zoom', 'sub': 'Native Click'},
                {'label': 'Data Format', 'val': 'Parent-Child / Path', 'sub': 'Tidy DataFrame'},
                {'label': 'Engine', 'val': 'Plotly Py WebGL', 'sub': 'Hardware Smooth'}
            ],
            'code_snippet': """import plotly.express as px
fig = px.sunburst(df, path=['market', 'brand', 'room_type'],
                  values='revenue', color='margin',
                  color_continuous_scale='RdYlGn')"""
        },

        # 16. Bokeh Interactive Candlestick with VWAP
        {
            'slide_id': 'slide-16-bokeh-candlestick',
            'tag': '16 / Trading Diagnostics',
            'headline': 'Algorithmic Financials in Python:',
            'headline_span': 'Bokeh Candlestick with VWAP',
            'subtitle': 'Interactive trading chart combining OHLC candlesticks with volume-weighted average price (VWAP) overlays.',
            'library_badge': 'Bokeh Financial',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 240" style="width:100%; max-height:260px;">
                  <!-- Candlesticks -->
                  <!-- Bar 1 Green -->
                  <line x1="80" y1="60" x2="80" y2="180" stroke="#00e676" stroke-width="1.5"/>
                  <rect x="72" y="80" width="16" height="70" fill="#00e676" rx="2"/>
                  <!-- Bar 2 Red -->
                  <line x1="140" y1="80" x2="140" y2="200" stroke="#ff1744" stroke-width="1.5"/>
                  <rect x="132" y="100" width="16" height="60" fill="#ff1744" rx="2"/>
                  <!-- Bar 3 Green -->
                  <line x1="200" y1="50" x2="200" y2="170" stroke="#00e676" stroke-width="1.5"/>
                  <rect x="192" y="70" width="16" height="80" fill="#00e676" rx="2"/>
                  <!-- Bar 4 Green High -->
                  <line x1="260" y1="30" x2="260" y2="150" stroke="#00e676" stroke-width="1.5"/>
                  <rect x="252" y="50" width="16" height="70" fill="#00e676" rx="2"/>
                  <!-- VWAP Yellow Curve -->
                  <path d="M 60 140 Q 140 130, 200 110 T 320 80" fill="none" stroke="#f3cf65" stroke-width="2.5" stroke-dasharray="3"/>
                  <text x="330" y="85" fill="#f3cf65" font-family="JetBrains Mono" font-size="10">VWAP</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'OHLC glyph rendering with continuous VWAP benchmark: $\\text{VWAP} = \\frac{\\sum P_i Q_i}{\\sum Q_i}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Algorithmic rate yield trading, real-time demand auction bidding, liquidity evaluation.'},
                {'title': 'Technical Strengths', 'desc': 'Wheel zoom, pan, and box select tools rendered directly via HTML5 Canvas.'}
            ],
            'metrics': [
                {'label': 'Glyphs', 'val': 'Segment + VBar', 'sub': 'OHLC Geometry'},
                {'label': 'Indicators', 'val': 'VWAP / EMA', 'sub': 'Moving Average'},
                {'label': 'Interactivity', 'val': 'Wheel / Pan', 'sub': 'Interactive Pan'},
                {'label': 'Language', 'val': 'Pure Python', 'sub': 'Bokeh Core'}
            ],
            'code_snippet': """p = figure(x_axis_type="datetime")
p.segment(df.date, df.high, df.date, df.low, color="#fff")
p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#00e676")
p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#ff1744")"""
        },

        # 17. Matplotlib Vector Streamplot
        {
            'slide_id': 'slide-17-mpl-streamplot',
            'tag': '17 / Vector Fields',
            'headline': 'Continuous Vector Fields:',
            'headline_span': 'Matplotlib 2D Streamplot',
            'subtitle': 'Eulerian vector streamlines illustrating velocity flow vectors and gradient forces in commercial optimization.',
            'library_badge': 'Matplotlib streamplot',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Smooth streamline curves -->
                  <g fill="none" stroke-width="2">
                    <path d="M 40 40 Q 140 80, 200 140 T 320 200" stroke="#00e676"/>
                    <path d="M 40 80 Q 140 120, 200 160 T 320 220" stroke="#00e676" opacity="0.8"/>
                    <path d="M 40 120 Q 140 160, 220 180 T 320 230" stroke="#d4af37" opacity="0.7"/>
                    <!-- Recirculation vortex -->
                    <path d="M 220 60 Q 280 40, 280 90 T 220 110 Z" stroke="#00e5ff" stroke-width="1.5"/>
                    <!-- Arrows -->
                    <polygon points="200,140 190,135 195,145" fill="#00e676"/>
                    <polygon points="260,175 250,170 255,180" fill="#00e676"/>
                  </g>
                  <text x="175" y="235" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Gradient Flow: Direct Velocity Stream</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Runge-Kutta 4th order (RK4) numerical trajectory integration tracing tangent curves to vector field $(u(x,y), v(x,y))$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Gradient descent optimization trajectory, aerodynamics fluid flow, geomagnetic fields.'},
                {'title': 'Technical Strengths', 'desc': 'Adaptive streamline density control avoiding artificial trajectory clustering.'}
            ],
            'metrics': [
                {'label': 'Integrator', 'val': 'RK4 Numerical', 'sub': 'Tangent Exact'},
                {'label': 'Speed Encode', 'val': 'Line Color/Width', 'sub': 'Dual Vector'},
                {'label': 'Grid Base', 'val': 'NumPy 2D Mesh', 'sub': 'Vectorized'},
                {'label': 'Output', 'val': 'Vector SVG/PDF', 'sub': 'Lossless Scale'}
            ],
            'code_snippet': """import matplotlib.pyplot as plt
fig, ax = plt.subplots()
speed = np.sqrt(u**2 + v**2)
ax.streamplot(X, Y, u, v, color=speed, cmap='autumn', density=1.2)"""
        },

        # 18. HVPlot Linked Brush Time Series
        {
            'slide_id': 'slide-18-hvplot-timeseries',
            'tag': '18 / High-Level PyData',
            'headline': 'Pandas One-Line Elegance:',
            'headline_span': 'HVPlot Linked Datetime Brushing',
            'subtitle': 'Seamless high-level Pandas .hvplot() API binding HoloViews and Bokeh with zero boilerplate.',
            'library_badge': 'hvPlot (HoloViz)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:15px; box-sizing:border-box;">
                <svg viewBox="0 0 450 240" style="width:100%; max-height:260px;">
                  <line x1="40" y1="200" x2="420" y2="200" stroke="rgba(255,255,255,0.15)"/>
                  <!-- Top Main Plot -->
                  <path d="M 40 140 Q 120 70, 200 110 T 320 60 T 420 80" fill="none" stroke="#00e676" stroke-width="2.5"/>
                  <!-- Mini Range Slider Plot Below -->
                  <rect x="40" y="210" width="380" height="24" fill="#0e1713" stroke="rgba(255,255,255,0.1)"/>
                  <rect x="140" y="210" width="160" height="24" fill="rgba(212,175,55,0.25)" stroke="#d4af37"/>
                  <text x="220" y="226" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">Active Range Selection Window</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Wraps HoloViews composable primitives around Pandas and XArray data structures with automatic BokehJS bindings.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Rapid exploratory data analysis on multi-gigabyte financial time-series and sensor telemetry.'},
                {'title': 'Technical Strengths', 'desc': 'Transforms standard static Pandas `.plot()` calls into rich interactive WebGL dashboards.'}
            ],
            'metrics': [
                {'label': 'API Style', 'val': 'df.hvplot()', 'sub': 'Pandas Native'},
                {'label': 'Backend', 'val': 'Bokeh / Plotly', 'sub': 'Interchangeable'},
                {'label': 'Brushing', 'val': 'RangeTool Link', 'sub': 'Subplot Sync'},
                {'label': 'Big Data', 'val': 'Datashader Plug', 'sub': 'Billion Pts'}
            ],
            'code_snippet': """import hvplot.pandas
df.hvplot(x='date', y=['direct_revpar', 'ota_revpar'],
          responsive=True, grid=True, line_width=2)"""
        },

        # 19. Seaborn Split Violin Plot
        {
            'slide_id': 'slide-19-split-violin',
            'tag': '19 / Counterfactual Contrasts',
            'headline': 'Asymmetric Treatment Contrasts:',
            'headline_span': 'Seaborn Split Hue Violin',
            'subtitle': 'Splits each kernel violin into left (Pre-Intervention) and right (Post-Intervention) halves for direct contrast.',
            'library_badge': 'Seaborn split=True',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Split Violin Center Axis at X=175 -->
                  <!-- Left Half: Pre-Strategy (Red) -->
                  <path d="M 175 40 C 130 60, 120 100, 145 140 C 160 160, 150 180, 175 200 Z" fill="rgba(255,23,68,0.3)" stroke="#ff1744" stroke-width="2"/>
                  <!-- Right Half: Post-Strategy (Green) -->
                  <path d="M 175 40 C 220 50, 235 80, 210 120 C 195 150, 215 180, 175 200 Z" fill="rgba(0,230,118,0.3)" stroke="#00e676" stroke-width="2"/>
                  <!-- Divider Line -->
                  <line x1="175" y1="30" x2="175" y2="210" stroke="#fff" stroke-width="1.5"/>
                  <text x="120" y="125" text-anchor="middle" fill="#ff1744" font-family="DM Sans" font-size="11" font-weight="bold">Pre-Audit (42%)</text>
                  <text x="235" y="125" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="11" font-weight="bold">Post-Audit (68%)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Split bilateral density estimation: left half evaluates $f(y \\mid \\text{Control})$, right half evaluates $f(y \\mid \\text{Treatment})$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'A/B testing conversions, hotel rate restructuring impact, executive salary equity audits.'},
                {'title': 'Technical Strengths', 'desc': 'Eliminates horizontal side-by-side gap; enables instant perceptual subtraction between two states.'}
            ],
            'metrics': [
                {'label': 'Feature', 'val': 'split=True', 'sub': 'Bilateral Split'},
                {'label': 'Contrast', 'val': 'Zero Spatial Gap', 'sub': 'Instant Diff'},
                {'label': 'Density', 'val': 'KDE Normalized', 'sub': 'Fair Area'},
                {'label': 'Use Case', 'val': 'A/B Experiment', 'sub': 'Causal Lift'}
            ],
            'code_snippet': """sns.violinplot(data=df, x="asset_tier", y="net_revpar",
               hue="intervention", split=True, palette=["#ff1744", "#00e676"])"""
        },

        # 20. Matplotlib Triangulated Contour Plot (tricontourf)
        {
            'slide_id': 'slide-20-mpl-tricontour',
            'tag': '20 / Unstructured Meshes',
            'headline': 'Unstructured Spatial Contours:',
            'headline_span': 'Matplotlib tricontourf Interpolation',
            'subtitle': 'Interpolates scattered, non-gridded sensor points into continuous smooth isobaric revenue surfaces.',
            'library_badge': 'Matplotlib tricontourf',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Contour Bands -->
                  <circle cx="175" cy="120" r="90" fill="rgba(14,23,19,0.9)" stroke="#d4af37" stroke-width="1"/>
                  <circle cx="175" cy="120" r="65" fill="rgba(45,90,68,0.5)" stroke="#00e676" stroke-width="1.5"/>
                  <circle cx="175" cy="120" r="40" fill="rgba(0,230,118,0.4)" stroke="#00e676" stroke-width="2"/>
                  <circle cx="175" cy="120" r="20" fill="rgba(243,207,101,0.6)" stroke="#f3cf65" stroke-width="2"/>
                  <!-- Raw Unstructured Points -->
                  <circle cx="140" cy="90" r="3" fill="#fff"/>
                  <circle cx="210" cy="100" r="3" fill="#fff"/>
                  <circle cx="160" cy="150" r="3" fill="#fff"/>
                  <circle cx="190" cy="130" r="3" fill="#fff"/>
                  <text x="175" y="124" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="9" font-weight="bold">$380 Peak</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Delaunay triangulation with natural neighbor bivariate cubic interpolation across non-gridded coordinates.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Geological ore reserve estimation, weather station precipitation contouring, real-estate land value surfaces.'},
                {'title': 'Technical Strengths', 'desc': 'Zero requirement for regular rectilinear grids; operates directly on messy real-world observation pings.'}
            ],
            'metrics': [
                {'label': 'Interpolation', 'val': 'Delaunay Cubic', 'sub': 'Natural Neighbor'},
                {'label': 'Data Input', 'val': 'Irregular (x,y,z)', 'sub': 'Non-Gridded'},
                {'label': 'Contours', 'val': 'Filled Isobars', 'sub': 'tricontourf'},
                {'label': 'Output', 'val': 'High-Res Vector', 'sub': 'Matplotlib Engine'}
            ],
            'code_snippet': """import matplotlib.tri as tri
triang = tri.Triangulation(x, y)
plt.tricontourf(triang, z, levels=14, cmap='viridis')
plt.plot(x, y, 'ko', ms=3)"""
        }
    ]

    html = generate_deck_html(deck_meta, slides)
    out_path = os.path.join(SCRIPT_DIR, "05-python-general-statistical.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Built {out_path} (20 slides, {len(html)} bytes)")

if __name__ == "__main__":
    build_deck()
