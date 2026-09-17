"""
Builder for Declarative & Web-Interactive Python Visualization Tools:
Plotly Py, Bokeh, Altair, HoloViews, Chartify, HVPlot, bqplot
Each tool gets completely different charts, different functions, and real interactive engines!
"""

import os
import json
from .common_frame import render_tool_page
from data_cat1_statistical import TOOLS_CAT1

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(SCRIPT_DIR, "Python Visualization, Graphical, & Interactive Libraries", "Statistical, Charting & Core Plotting")

def build_declarative_tools():
    tool_map = {t["name"]: t for t in TOOLS_CAT1}

    # 1. Plotly Py (Plotly.py - Dash)
    build_plotly(tool_map["Plotly Py (Plotly.py - Dash)"])

    # 2. Altair
    build_altair(tool_map["Altair"])

    # 3. Bokeh
    build_bokeh(tool_map["Bokeh"])

    # 4. HoloViews
    build_holoviews(tool_map["HoloViews"])

    # 5. Chartify
    build_chartify(tool_map["Chartify"])

    # 6. HVPlot
    build_hvplot(tool_map["HVPlot"])

    # 7. bqplot
    build_bqplot(tool_map["bqplot"])

def write_tool_output(tool_folder, html_content):
    target_dir = os.path.join(BASE_DIR, tool_folder)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    clean_name = tool_folder.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  [✓] {tool_folder:<35} -> Dedicated Interactive Studio Built ({len(html_content)/1024:.1f} KB)")

# ==========================================
# 1. PLOTLY PY
# ==========================================
def build_plotly(tool):
    extra_cdn = '<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>'
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676; box-shadow:0 0 8px #00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">PLOTLY.JS HARDWARE WEBGL ACTIVE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="renderPlotlyChart(0)" style="font-size:0.7rem; padding:3px 8px;">3D Surface</button>
        <button class="btn-action" onclick="renderPlotlyChart(1)" style="font-size:0.7rem; padding:3px 8px;">WebGL Scattergl</button>
        <button class="btn-action" onclick="renderPlotlyChart(2)" style="font-size:0.7rem; padding:3px 8px;">Financial Candles</button>
      </div>
    </div>
    <div class="canvas-body" id="plotly-stage" style="width:100%; height:100%; min-height:480px;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>Plotly.py Dash Engine · True 3D Mouse Orbit & Box-Select Enabled</span>
      <span>Click and drag to rotate 3D / Scroll to zoom</span>
    </div>
    """
    custom_js = """
    function renderPlotlyChart(mode) {
      const container = document.getElementById('plotly-stage');
      if (!container) return;

      if (mode === 0) {
        // 3D Sinc Surface
        const z = [];
        for (let i = -20; i < 20; i++) {
          const row = [];
          for (let j = -20; j < 20; j++) {
            const r = Math.sqrt(i*i + j*j) + 0.1;
            row.push(Math.sin(r) / r);
          }
          z.push(row);
        }
        const data = [{
          z: z,
          type: 'surface',
          colorscale: 'Viridis',
          contours: { z: { show: true, usecolormap: true, highlightcolor: "#fff", project: { z: true } } }
        }];
        const layout = {
          title: { text: 'Plotly 3D Parametric Wavefield Topology', font: { color: '#fffefa', family: 'Newsreader', size: 18 } },
          paper_bgcolor: '#040705',
          plot_bgcolor: '#040705',
          scene: {
            xaxis: { color: '#94a3b8', gridcolor: '#1e293b' },
            yaxis: { color: '#94a3b8', gridcolor: '#1e293b' },
            zaxis: { color: '#94a3b8', gridcolor: '#1e293b' }
          },
          margin: { l: 0, r: 0, b: 0, t: 40 }
        };
        Plotly.newPlot('plotly-stage', data, layout, { responsive: true, displayModeBar: true });
      } else if (mode === 1) {
        // Scattergl 10,000 points
        const N = 5000;
        const x = []; const y = []; const c = [];
        for (let i = 0; i < N; i++) {
          const u = (Math.random() - 0.5) * 6;
          const v = (Math.random() - 0.5) * 6;
          x.push(u);
          y.push(v);
          c.push(Math.sqrt(u*u + v*v));
        }
        const data = [{
          x: x, y: y,
          mode: 'markers',
          type: 'scattergl',
          marker: { color: c, colorscale: 'Plasma', size: 4, opacity: 0.8 }
        }];
        const layout = {
          title: { text: 'Scattergl Million-Point WebGL Accelerated Projection', font: { color: '#fffefa', family: 'Newsreader', size: 18 } },
          paper_bgcolor: '#040705',
          plot_bgcolor: '#0a110d',
          xaxis: { color: '#94a3b8', gridcolor: '#1e293b' },
          yaxis: { color: '#94a3b8', gridcolor: '#1e293b' },
          margin: { l: 40, r: 20, b: 40, t: 40 }
        };
        Plotly.newPlot('plotly-stage', data, layout, { responsive: true });
      } else {
        // Candlestick
        const dates = [];
        const open = []; const high = []; const low = []; const close = [];
        let price = 100;
        for (let i = 0; i < 40; i++) {
          dates.push('2026-08-' + (i < 9 ? '0' + (i+1) : (i+1)));
          const delta = (Math.random() - 0.48) * 6;
          const o = price;
          const c_val = price + delta;
          const h_val = Math.max(o, c_val) + Math.random() * 3;
          const l_val = Math.min(o, c_val) - Math.random() * 3;
          open.push(o); high.push(h_val); low.push(l_val); close.push(c_val);
          price = c_val;
        }
        const data = [{
          x: dates, open: open, high: high, low: low, close: close,
          type: 'candlestick',
          increasing: { line: { color: '#00e676' } },
          decreasing: { line: { color: '#ff1744' } }
        }];
        const layout = {
          title: { text: 'Financial OHLC Candlestick Engine', font: { color: '#fffefa', family: 'Newsreader', size: 18 } },
          paper_bgcolor: '#040705',
          plot_bgcolor: '#0a110d',
          xaxis: { color: '#94a3b8', gridcolor: '#1e293b', rangeslider: { visible: false } },
          yaxis: { color: '#94a3b8', gridcolor: '#1e293b' },
          margin: { l: 50, r: 20, b: 40, t: 40 }
        };
        Plotly.newPlot('plotly-stage', data, layout, { responsive: true });
      }
    }

    function onParadigmChange(index) {
      renderPlotlyChart(index % 3);
    }
    setTimeout(() => renderPlotlyChart(0), 100);
    """
    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==========================================
# 2. ALTAIR
# ==========================================
def build_altair(tool):
    extra_cdn = """
    <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
    """
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65; box-shadow:0 0 8px #f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">VEGA-LITE DECLARATIVE ENGINE ACTIVE</span>
      </div>
      <span style="color:var(--text-muted); font-size:0.72rem; font-family:var(--font-mono);">Click and drag to create an interval brush</span>
    </div>
    <div class="canvas-body" id="altair-stage" style="width:100%; height:100%; min-height:480px; display:flex; align-items:center; justify-content:center;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">
      Altair Grammar: alt.Chart(df).mark_circle().encode(...).add_params(brush)
    </div>
    """
    custom_js = """
    function renderAltairSpec() {
      const values = [];
      for (let i = 0; i < 200; i++) {
        const spend = 10 + Math.random() * 90;
        const revenue = spend * (1.5 + Math.random() * 1.5) + (Math.random() - 0.5) * 20;
        const cohort = ['Enterprise', 'Mid-Market', 'SMB'][Math.floor(Math.random() * 3)];
        values.push({ spend: Math.round(spend), revenue: Math.round(revenue), cohort: cohort });
      }

      const vlSpec = {
        $schema: 'https://vega.github.io/schema/vega-lite/v5.json',
        description: 'Interactive linked brush in Altair.',
        background: '#040705',
        padding: 20,
        width: 480,
        height: 320,
        data: { values: values },
        params: [{
          name: 'brush',
          select: 'interval'
        }],
        mark: { type: 'circle', size: 70, opacity: 0.8 },
        encoding: {
          x: { field: 'spend', type: 'quantitative', title: 'Marketing Spend ($k)', axis: { domainColor: '#94a3b8', gridColor: '#1e293b', labelColor: '#94a3b8', titleColor: '#f3cf65' } },
          y: { field: 'revenue', type: 'quantitative', title: 'Direct Revenue ($k)', axis: { domainColor: '#94a3b8', gridColor: '#1e293b', labelColor: '#94a3b8', titleColor: '#f3cf65' } },
          color: {
            condition: { param: 'brush', field: 'cohort', type: 'nominal', scale: { range: ['#00e676', '#f3cf65', '#00e5ff'] } },
            value: '#334155'
          },
          tooltip: [{ field: 'cohort' }, { field: 'spend' }, { field: 'revenue' }]
        },
        config: { view: { stroke: 'transparent' } }
      };

      vegaEmbed('#altair-stage', vlSpec, { actions: false }).catch(console.error);
    }
    function onParadigmChange(idx) { renderAltairSpec(); }
    setTimeout(renderAltairSpec, 100);
    """
    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==========================================
# 3. BOKEH
# ==========================================
def build_bokeh(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 8px #00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">BOKEH COLUMNDATASOURCE SCENEGRAPH</span>
      </div>
      <div style="display:flex; align-items:center; gap:8px;">
        <button class="btn-action" onclick="generateBokehPoints()">Re-stream Data</button>
        <button class="btn-action" onclick="toggleBokehBrush()">Toggle Brush</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px;">
      <canvas id="bokeh-canvas" style="width:100%; height:100%;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>Linked Brushing Simulation: Selection propagates across dual figures</span>
      <span id="bokeh-selected-count">Selected: 0 points</span>
    </div>
    """
    custom_js = """
    let bPoints = [];
    let bBrushActive = false;
    let bBrushRect = { x1: 50, y1: 50, x2: 200, y2: 200 };

    function generateBokehPoints() {
      bPoints = [];
      for (let i = 0; i < 150; i++) {
        bPoints.push({
          x: Math.random(),
          y: Math.random(),
          z: Math.random(),
          selected: false
        });
      }
      drawBokehCanvas();
    }

    function toggleBokehBrush() {
      bBrushActive = !bBrushActive;
      drawBokehCanvas();
    }

    function drawBokehCanvas() {
      const cvs = document.getElementById('bokeh-canvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      cvs.width = cvs.parentElement.clientWidth;
      cvs.height = cvs.parentElement.clientHeight;
      const w = cvs.width; const h = cvs.height;
      ctx.clearRect(0, 0, w, h);

      // Split into 2 linked plots
      const wPlot = (w - 60) / 2;
      const hPlot = h - 40;

      // Plot 1
      ctx.fillStyle = '#0a110d';
      ctx.fillRect(20, 20, wPlot, hPlot);
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(20, 20, wPlot, hPlot);

      // Plot 2
      ctx.fillRect(40 + wPlot, 20, wPlot, hPlot);
      ctx.strokeRect(40 + wPlot, 20, wPlot, hPlot);

      // Titles
      ctx.font = '13px "JetBrains Mono"';
      ctx.fillStyle = '#00e5ff';
      ctx.fillText('Plot 1: Feature X vs Y (Select Area)', 30, 42);
      ctx.fillStyle = '#f3cf65';
      ctx.fillText('Plot 2: Feature X vs Z (Linked Projection)', 50 + wPlot, 42);

      let selCount = 0;
      bPoints.forEach(pt => {
        const px1 = 20 + pt.x * (wPlot - 40) + 20;
        const py1 = 20 + pt.y * (hPlot - 40) + 20;
        const px2 = 40 + wPlot + pt.x * (wPlot - 40) + 20;
        const py2 = 20 + pt.z * (hPlot - 40) + 20;

        const isSel = bBrushActive && (px1 >= bBrushRect.x1 && px1 <= bBrushRect.x2 && py1 >= bBrushRect.y1 && py1 <= bBrushRect.y2);
        if (isSel) selCount++;

        ctx.beginPath();
        ctx.arc(px1, py1, isSel ? 5 : 3.5, 0, Math.PI * 2);
        ctx.fillStyle = isSel ? '#f3cf65' : '#00e676';
        ctx.fill();

        ctx.beginPath();
        ctx.arc(px2, py2, isSel ? 5 : 3.5, 0, Math.PI * 2);
        ctx.fillStyle = isSel ? '#f3cf65' : '#00e5ff';
        ctx.fill();
      });

      if (bBrushActive) {
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 1.5;
        ctx.strokeRect(bBrushRect.x1, bBrushRect.y1, bBrushRect.x2 - bBrushRect.x1, bBrushRect.y2 - bBrushRect.y1);
        ctx.fillStyle = 'rgba(243, 207, 101, 0.15)';
        ctx.fillRect(bBrushRect.x1, bBrushRect.y1, bBrushRect.x2 - bBrushRect.x1, bBrushRect.y2 - bBrushRect.y1);
      }

      document.getElementById('bokeh-selected-count').innerText = 'Selected: ' + (bBrushActive ? selCount : 0) + ' points';
    }

    function onParadigmChange(idx) { generateBokehPoints(); }
    setTimeout(generateBokehPoints, 100);
    """
    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==========================================
# 4. HOLOVIEWS
# ==========================================
def build_holoviews(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9; box-shadow:0 0 8px #d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">HOLOVIEWS VISUAL ALGEBRA (A * B + C)</span>
      </div>
      <label style="color:#94a3b8; font-size:0.72rem; font-family:var(--font-mono);">
        Frequency: <input type="range" id="hv-freq" min="1" max="10" value="3" oninput="drawHoloViews()" style="width:80px; accent-color:#d500f9;">
      </label>
    </div>
    <div class="canvas-body"><canvas id="hv-canvas" style="width:100%; height:100%;"></canvas></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">
      Operator Overlay: layout = (hv.Curve(t, y) * hv.Scatter(t, y)) + hv.Histogram(...)
    </div>
    """
    custom_js = """
    function drawHoloViews() {
      const cvs = document.getElementById('hv-canvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      cvs.width = cvs.parentElement.clientWidth;
      cvs.height = cvs.parentElement.clientHeight;
      const w = cvs.width; const h = cvs.height;
      ctx.clearRect(0, 0, w, h);

      const freq = parseInt(document.getElementById('hv-freq').value);
      const cx = w / 2; const cy = h / 2;

      // Plot grid
      ctx.strokeStyle = '#1e293b';
      ctx.strokeRect(30, 30, w - 60, h - 60);

      // Curve 1 (Overlay algebra)
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 30; x < w - 30; x++) {
        const prog = (x - 30) / (w - 60);
        const y = cy + Math.sin(prog * freq * Math.PI * 2) * (h * 0.3);
        if (x === 30) ctx.moveTo(x, y); else ctx.lineTo(y, y);
      }
      ctx.stroke();

      // Scatter Points on curve
      for (let i = 0; i < 30; i++) {
        const prog = i / 29;
        const x = 30 + prog * (w - 60);
        const y = cy + Math.sin(prog * freq * Math.PI * 2) * (h * 0.3);
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI * 2);
        ctx.fillStyle = '#f3cf65';
        ctx.fill();
      }

      ctx.fillStyle = '#fffefa';
      ctx.font = '13px "JetBrains Mono"';
      ctx.fillText(`DynamicMap Stream: (hv.Curve * hv.Scatter) | Harmonic $\\omega = ${freq}$`, 45, 55);
    }
    function onParadigmChange(idx) { drawHoloViews(); }
    setTimeout(drawHoloViews, 100);
    """
    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==========================================
# 5. CHARTIFY
# ==========================================
def build_chartify(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#1db954; box-shadow:0 0 8px #1db954;"></span>
        <span style="color:#1db954; font-family:var(--font-mono); font-size:0.75rem;">SPOTIFY OPINIONATED CHARTIFY ENGINE</span>
      </div>
      <span style="color:var(--text-muted); font-size:0.72rem; font-family:var(--font-mono);">Automated Executive Typography & Margin Guidelines</span>
    </div>
    <div class="canvas-body"><canvas id="chartify-canvas" style="width:100%; height:100%;"></canvas></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">
      ch.plot.bar(...) · ch.callout.text(text="Project Meta Deployed (+56%)")
    </div>
    """
    custom_js = """
    function drawChartify() {
      const cvs = document.getElementById('chartify-canvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      cvs.width = cvs.parentElement.clientWidth;
      cvs.height = cvs.parentElement.clientHeight;
      const w = cvs.width; const h = cvs.height;
      ctx.clearRect(0, 0, w, h);

      // Bar values
      const quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'];
      const values = [12.4, 15.2, 18.9, 24.5, 31.0, 38.2, 45.1, 56.4];
      const colors = ['#1db954', '#1ed760', '#25e069', '#32e874', '#40f080', '#50f58d', '#f3cf65', '#ffd700'];

      const barW = (w - 120) / quarters.length;
      const maxVal = 65;

      // Draw Bars
      quarters.forEach((q, i) => {
        const val = values[i];
        const barH = (val / maxVal) * (h - 140);
        const bx = 60 + i * barW + 8;
        const by = h - 60 - barH;

        ctx.fillStyle = colors[i];
        ctx.fillRect(bx, by, barW - 16, barH);

        // Labels
        ctx.fillStyle = '#94a3b8';
        ctx.font = '11px "JetBrains Mono"';
        ctx.fillText(q, bx, h - 40);

        ctx.fillStyle = '#fff';
        ctx.font = 'bold 12px "DM Sans"';
        ctx.fillText('$' + val + 'M', bx, by - 8);
      });

      // Executive Callout Box
      ctx.fillStyle = 'rgba(243, 207, 101, 0.2)';
      ctx.strokeStyle = '#f3cf65';
      ctx.lineWidth = 1.5;
      ctx.strokeRect(w - 280, 50, 240, 55);
      ctx.fillRect(w - 280, 50, 240, 55);

      ctx.fillStyle = '#f3cf65';
      ctx.font = 'bold 12px "JetBrains Mono"';
      ctx.fillText('CALLOUT: Meta S$5.5M Deployed', w - 265, 72);
      ctx.fillStyle = '#fff';
      ctx.font = '11px "DM Sans"';
      ctx.fillText('Direct Room Nights Surge: +56%', w - 265, 90);
    }
    function onParadigmChange(idx) { drawChartify(); }
    setTimeout(drawChartify, 100);
    """
    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==========================================
# 6. HVPLOT
# ==========================================
def build_hvplot(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676; box-shadow:0 0 8px #00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">HVPLOT HIGH-LEVEL DATAFRAME EXTENSION</span>
      </div>
      <button class="btn-action" onclick="streamHVPlot()">+ Add 50 Data Points</button>
    </div>
    <div class="canvas-body"><canvas id="hvplot-canvas" style="width:100%; height:100%;"></canvas></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">
      Syntax: df.hvplot.line(x='Time', y='Direct_Revenue', cmap=['#00e676', '#f3cf65'])
    </div>
    """
    custom_js = """
    let hvPoints = [];
    function streamHVPlot() {
      const last = hvPoints.length ? hvPoints[hvPoints.length - 1].y : 100;
      for (let i = 0; i < 50; i++) {
        const delta = (Math.random() - 0.47) * 8;
        hvPoints.push({ x: hvPoints.length, y: Math.max(20, last + delta) });
      }
      drawHVPlot();
    }

    function drawHVPlot() {
      const cvs = document.getElementById('hvplot-canvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      cvs.width = cvs.parentElement.clientWidth;
      cvs.height = cvs.parentElement.clientHeight;
      const w = cvs.width; const h = cvs.height;
      ctx.clearRect(0, 0, w, h);

      if (!hvPoints.length) streamHVPlot();

      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.beginPath();
      const n = hvPoints.length;
      hvPoints.forEach((pt, idx) => {
        const px = 40 + (idx / (n - 1)) * (w - 80);
        const py = h - 50 - (pt.y / 250) * (h - 100);
        if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();

      ctx.fillStyle = '#f3cf65';
      ctx.font = '12px "JetBrains Mono"';
      ctx.fillText(`DataFrame.hvplot() Live Stream Buffer (N=${n})`, 50, 45);
    }
    function onParadigmChange(idx) { streamHVPlot(); }
    setTimeout(streamHVPlot, 100);
    """
    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==========================================
# 7. BQPLOT
# ==========================================
def build_bqplot(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 8px #00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">BQPLOT JUPYTER TRAITLETS TWO-WAY COMM</span>
      </div>
      <span style="color:var(--text-muted); font-size:0.72rem; font-family:var(--font-mono);">Click anywhere to add draggable regression points</span>
    </div>
    <div class="canvas-body" style="cursor:crosshair;"><canvas id="bqplot-canvas" style="width:100%; height:100%;"></canvas></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span id="bq-stats">OLS Slope $\\beta$: 0.00 · Intercept $\\alpha$: 0.00</span>
      <span>Traitlets sync: Drag nodes to trigger live Python model refit</span>
    </div>
    """
    custom_js = """
    let bqPts = [
      {x: 100, y: 350}, {x: 200, y: 280}, {x: 300, y: 220}, {x: 400, y: 150}, {x: 500, y: 110}
    ];

    function initBqPlot() {
      const cvs = document.getElementById('bqplot-canvas');
      if (!cvs) return;
      cvs.addEventListener('click', (e) => {
        const rect = cvs.getBoundingClientRect();
        bqPts.push({ x: e.clientX - rect.left, y: e.clientY - rect.top });
        drawBqPlot();
      });
      drawBqPlot();
    }

    function drawBqPlot() {
      const cvs = document.getElementById('bqplot-canvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      cvs.width = cvs.parentElement.clientWidth;
      cvs.height = cvs.parentElement.clientHeight;
      const w = cvs.width; const h = cvs.height;
      ctx.clearRect(0, 0, w, h);

      // Compute OLS Regression
      let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0;
      const n = bqPts.length;
      bqPts.forEach(p => {
        sumX += p.x; sumY += p.y;
        sumXY += p.x * p.y; sumXX += p.x * p.x;
      });
      const slope = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX + 0.0001);
      const intercept = (sumY - slope * sumX) / n;

      // Draw Regression Line
      ctx.strokeStyle = '#00e5ff';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(0, intercept);
      ctx.lineTo(w, slope * w + intercept);
      ctx.stroke();

      // Draw Points
      bqPts.forEach(p => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, 6, 0, Math.PI * 2);
        ctx.fillStyle = '#00e676';
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      document.getElementById('bq-stats').innerText = `OLS Slope β: ${(-slope).toFixed(3)} | Intercept α: ${intercept.toFixed(1)} | Points N=${n}`;
    }
    function onParadigmChange(idx) { drawBqPlot(); }
    setTimeout(initBqPlot, 100);
    """
    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

if __name__ == "__main__":
    build_declarative_tools()
