"""
Builder for Statistical, Charting & Core Plotting Tools (Remaining 9 tools):
Matplotlib, Seaborn, Pygal, Plotnine, Leather, Veusz, GR Framework, Visvis, Chaco
Each tool gets completely different charts, different functions, and real interactive engines!
"""

import os
import json
from .common_frame import render_tool_page
from data_cat1_statistical import TOOLS_CAT1

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(SCRIPT_DIR, "Python Visualization, Graphical, & Interactive Libraries", "Statistical, Charting & Core Plotting")

def write_tool_output(tool_folder, html_content):
    target_dir = os.path.join(BASE_DIR, tool_folder)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    clean_name = tool_folder.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  [✓] {tool_folder:<35} -> Dedicated Interactive Studio Built ({len(html_content)/1024:.1f} KB)")

def build_statistical_tools():
    tool_map = {t["folder"]: t for t in TOOLS_CAT1}

    build_matplotlib(tool_map["Matplotlib"])
    build_seaborn(tool_map["Seaborn"])
    build_pygal(tool_map["Pygal"])
    build_plotnine(tool_map["Plotnine (ggplot2 implementation)"])
    build_leather(tool_map["Leather"])
    build_veusz(tool_map["Veusz"])
    build_gr(tool_map["GR Framework"])
    build_visvis(tool_map["Visvis"])
    build_chaco(tool_map["Chaco"])

# ==============================================================================
# 1. MATPLOTLIB
# ==============================================================================
def build_matplotlib(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">MATPLOTLIB ARTIST PIPELINE ACTIVE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Freq: <span id="mpl-freq-val">2.5</span> Hz</label>
        <input type="range" id="mpl-freq" min="0.5" max="8.0" step="0.1" value="2.5" oninput="updateMatplotlib()" style="width:90px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); margin-left:6px;">Noise:</label>
        <input type="range" id="mpl-noise" min="0.0" max="0.8" step="0.05" value="0.2" oninput="updateMatplotlib()" style="width:70px;">
        <button class="btn-action" onclick="toggleMplGrid()" style="font-size:0.7rem; padding:3px 8px;">Toggle Grid</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#030504; display:flex; flex-direction:column; gap:8px; width:100%;">
      <div style="display:grid; grid-template-columns: 1.4fr 1fr; gap:10px; width:100%; height:55%;">
        <div style="background:#070d09; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:8px; position:relative;">
          <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--gold-bright); margin-bottom:4px;">ax1: ax.plot(t, signal) & Envelope</div>
          <canvas id="mpl-canvas-signal" style="width:100%; height:calc(100% - 20px);"></canvas>
        </div>
        <div style="background:#070d09; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:8px; position:relative;">
          <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--cyan-neon); margin-bottom:4px;">ax2: np.fft.rfft Power Spectrum (dB)</div>
          <canvas id="mpl-canvas-fft" style="width:100%; height:calc(100% - 20px);"></canvas>
        </div>
      </div>
      <div style="background:#070d09; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:8px; width:100%; height:45%;">
        <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--emerald-neon); margin-bottom:4px;">ax3: ax.streamplot(X, Y, U, V) Vector Field Streamlines</div>
        <canvas id="mpl-canvas-stream" style="width:100%; height:calc(100% - 20px);"></canvas>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>Figure(figsize=(10, 7), dpi=300) · GridSpec(2, 2, height_ratios=[1.2, 1.0])</span>
      <span>Agg Backend Transform Pipeline</span>
    </div>
    """

    custom_js = """
    let showGrid = true;
    function toggleMplGrid() {
      showGrid = !showGrid;
      updateMatplotlib();
    }

    function updateMatplotlib() {
      const freq = parseFloat(document.getElementById('mpl-freq').value);
      const noise = parseFloat(document.getElementById('mpl-noise').value);
      document.getElementById('mpl-freq-val').innerText = freq.toFixed(1);

      drawSignalCanvas(freq, noise);
      drawFftCanvas(freq, noise);
      drawStreamCanvas(freq);
    }

    function drawSignalCanvas(freq, noise) {
      const c = document.getElementById('mpl-canvas-signal');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070d09';
      ctx.fillRect(0, 0, W, H);

      if (showGrid) {
        ctx.strokeStyle = 'rgba(255,255,255,0.06)';
        ctx.lineWidth = 1;
        for (let x = 0; x < W; x += 30) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
        for (let y = 0; y < H; y += 25) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }
      }

      // Zero axis
      ctx.strokeStyle = 'rgba(255,255,255,0.2)';
      ctx.beginPath(); ctx.moveTo(0, H/2); ctx.lineTo(W, H/2); ctx.stroke();

      // Plot Signal
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      const nPts = 200;
      for (let i = 0; i < nPts; i++) {
        const t = (i / nPts) * 4 * Math.PI;
        const s = Math.sin(freq * t) + (Math.sin(freq * 2.3 * t) * 0.4) + (Math.random() - 0.5) * noise * 2;
        const px = (i / nPts) * W;
        const py = H/2 - (s * (H * 0.35));
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Envelope
      ctx.strokeStyle = 'rgba(243, 207, 101, 0.6)';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (let i = 0; i < nPts; i++) {
        const t = (i / nPts) * 4 * Math.PI;
        const env = 1.4 + (Math.random() - 0.5) * noise * 0.5;
        const px = (i / nPts) * W;
        const py = H/2 - (env * (H * 0.35));
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);
    }

    function drawFftCanvas(freq, noise) {
      const c = document.getElementById('mpl-canvas-fft');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070d09';
      ctx.fillRect(0, 0, W, H);

      const nBins = 32;
      const barW = (W - 40) / nBins;
      const peakBin = Math.min(Math.floor(freq * 3.5), nBins - 2);

      for (let i = 0; i < nBins; i++) {
        let mag = Math.random() * noise * 0.4 + 0.05;
        if (i === peakBin) mag += 0.85;
        if (i === Math.floor(peakBin * 2.3) && i < nBins) mag += 0.35;

        const bH = mag * (H - 30);
        const bx = 25 + i * barW;
        const by = H - 20 - bH;

        const grad = ctx.createLinearGradient(0, by, 0, H - 20);
        grad.addColorStop(0, '#00e5ff');
        grad.addColorStop(1, 'rgba(0, 229, 255, 0.1)');
        ctx.fillStyle = grad;
        ctx.fillRect(bx, by, barW - 2, bH);
      }

      // X axis
      ctx.strokeStyle = 'rgba(255,255,255,0.2)';
      ctx.beginPath(); ctx.moveTo(20, H - 20); ctx.lineTo(W - 10, H - 20); ctx.stroke();
      ctx.fillStyle = '#64748b';
      ctx.font = '9px JetBrains Mono';
      ctx.fillText('0 Hz', 25, H - 6);
      ctx.fillText('Nyquist (Fs/2)', W - 70, H - 6);
    }

    function drawStreamCanvas(freq) {
      const c = document.getElementById('mpl-canvas-stream');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070d09';
      ctx.fillRect(0, 0, W, H);

      const rows = 6; const cols = 16;
      const dx = W / cols; const dy = H / rows;

      for (let r = 0; r < rows; r++) {
        for (let cl = 0; cl < cols; cl++) {
          const x = (cl + 0.5) * dx;
          const y = (r + 0.5) * dy;
          const u = -Math.sin((y / H) * Math.PI * (freq * 0.4));
          const v = Math.cos((x / W) * Math.PI * (freq * 0.4));
          const angle = Math.atan2(v, u);
          const len = 14;

          ctx.strokeStyle = `hsl(${(cl * 15 + r * 20) % 360}, 80%, 60%)`;
          ctx.lineWidth = 1.4;
          ctx.beginPath();
          ctx.moveTo(x - Math.cos(angle)*len*0.5, y - Math.sin(angle)*len*0.5);
          ctx.lineTo(x + Math.cos(angle)*len*0.5, y + Math.sin(angle)*len*0.5);
          ctx.stroke();

          // Arrow head
          ctx.fillStyle = ctx.strokeStyle;
          ctx.beginPath();
          ctx.arc(x + Math.cos(angle)*len*0.5, y + Math.sin(angle)*len*0.5, 2, 0, 2*Math.PI);
          ctx.fill();
        }
      }
    }

    window.addEventListener('load', () => { setTimeout(updateMatplotlib, 100); });
    window.addEventListener('resize', updateMatplotlib);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 2. SEABORN
# ==============================================================================
def build_seaborn(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">SEABORN STATISTICAL JOINTGRID</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Palette:</label>
        <select id="sns-palette" onchange="drawSeaborn()" style="background:#070d09; color:#fff; border:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; padding:2px 6px; border-radius:4px;">
          <option value="viridis">viridis</option>
          <option value="mako" selected>mako</option>
          <option value="rocket">rocket</option>
          <option value="crest">crest</option>
        </select>
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); margin-left:6px;">KDE Bandwidth:</label>
        <input type="range" id="sns-bw" min="0.3" max="2.0" step="0.1" value="1.0" oninput="drawSeaborn()" style="width:80px;">
        <button class="btn-action" onclick="resampleSeaborn()" style="font-size:0.7rem; padding:3px 8px;">Re-sample</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#040705;">
      <canvas id="sns-stage" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>sns.jointplot(x='petal_length', y='sepal_width', kind='kde', fill=True, marginal_kws=dict(fill=True))</span>
      <span>Bivariate Gaussian Kernel Density Estimation</span>
    </div>
    """

    custom_js = """
    let snsPoints = [];
    function initSnsPoints() {
      snsPoints = [];
      const N = 180;
      // Cluster 1 (Setosa)
      for (let i = 0; i < N/2; i++) {
        snsPoints.push({
          x: 1.5 + (Math.random() - 0.5) * 0.8 + (Math.random() - 0.5) * 0.4,
          y: 3.5 + (Math.random() - 0.5) * 0.7 + (Math.random() - 0.5) * 0.3,
          species: 0
        });
      }
      // Cluster 2 (Versicolor/Virginica)
      for (let i = 0; i < N/2; i++) {
        snsPoints.push({
          x: 4.5 + (Math.random() - 0.5) * 1.5 + (Math.random() - 0.5) * 0.6,
          y: 2.8 + (Math.random() - 0.5) * 0.8 + (Math.random() - 0.5) * 0.4,
          species: 1
        });
      }
    }
    initSnsPoints();

    function resampleSeaborn() {
      initSnsPoints();
      drawSeaborn();
    }

    function drawSeaborn() {
      const c = document.getElementById('sns-stage');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const margin = { top: 60, right: 60, bottom: 50, left: 60 };
      const mainW = W - margin.left - margin.right;
      const mainH = H - margin.top - margin.bottom;

      // Draw Joint Bivariate KDE Contours
      const pal = document.getElementById('sns-palette').value;
      const bw = parseFloat(document.getElementById('sns-bw').value);

      // Render 2D density contours
      const colors = {
        mako: ['#2e1e3b', '#3b4371', '#407088', '#49a09d', '#5fd068'],
        viridis: ['#440154', '#3b528b', '#21908d', '#5dc863', '#fde725'],
        rocket: ['#1f1424', '#541c44', '#932649', '#dd513a', '#fca50a'],
        crest: ['#1b3b42', '#28636a', '#3f8f8b', '#68baa3', '#9fe0b5']
      }[pal];

      // Draw contour ellipses for cluster 1
      drawKdeContours(ctx, margin.left + mainW * 0.22, margin.top + mainH * 0.25, 45 * bw, 32 * bw, -0.3, colors);
      // Draw contour ellipses for cluster 2
      drawKdeContours(ctx, margin.left + mainW * 0.68, margin.top + mainH * 0.60, 75 * bw, 45 * bw, 0.4, colors);

      // Scatter Points overlay
      for (const p of snsPoints) {
        const px = margin.left + ((p.x - 0.8) / 5.5) * mainW;
        const py = margin.top + mainH - ((p.y - 1.8) / 2.8) * mainH;
        ctx.fillStyle = p.species === 0 ? 'rgba(0, 229, 255, 0.7)' : 'rgba(243, 207, 101, 0.7)';
        ctx.beginPath();
        ctx.arc(px, py, 3.5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = 'rgba(0,0,0,0.5)';
        ctx.stroke();
      }

      // Regression Trendline for Cluster 2
      ctx.strokeStyle = '#f3cf65';
      ctx.lineWidth = 2;
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(margin.left + mainW * 0.45, margin.top + mainH * 0.85);
      ctx.lineTo(margin.left + mainW * 0.92, margin.top + mainH * 0.35);
      ctx.stroke();
      ctx.setLineDash([]);

      // Marginal Top Histogram
      drawMarginalTop(ctx, margin.left, margin.top - 45, mainW, 40, colors[3]);
      // Marginal Right Histogram
      drawMarginalRight(ctx, margin.left + mainW + 5, margin.top, 45, mainH, colors[3]);

      // Axes Frame
      ctx.strokeStyle = 'rgba(255,255,255,0.2)';
      ctx.strokeRect(margin.left, margin.top, mainW, mainH);

      // Axis Labels
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px DM Sans';
      ctx.textAlign = 'center';
      ctx.fillText('petal_length (cm) - Bivariate Joint Density', margin.left + mainW/2, H - 15);
      ctx.save();
      ctx.translate(20, margin.top + mainH/2);
      ctx.rotate(-Math.PI/2);
      ctx.fillText('sepal_width (cm)', 0, 0);
      ctx.restore();
    }

    function drawKdeContours(ctx, cx, cy, rx, ry, rot, colors) {
      for (let lvl = 0; lvl < 5; lvl++) {
        const factor = (5 - lvl) / 5;
        ctx.save();
        ctx.translate(cx, cy);
        ctx.rotate(rot);
        ctx.fillStyle = colors[lvl] + '33';
        ctx.strokeStyle = colors[lvl] + 'bb';
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        ctx.ellipse(0, 0, rx * factor, ry * factor, 0, 0, 2*Math.PI);
        ctx.fill();
        ctx.stroke();
        ctx.restore();
      }
    }

    function drawMarginalTop(ctx, x, y, w, h, col) {
      ctx.fillStyle = col + '55';
      ctx.strokeStyle = col;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(x, y + h);
      const nBins = 30;
      for (let i = 0; i <= nBins; i++) {
        const u = i / nBins;
        // Bimodal distribution
        const d1 = Math.exp(-Math.pow(u - 0.22, 2) / 0.015);
        const d2 = Math.exp(-Math.pow(u - 0.68, 2) / 0.035) * 1.3;
        const val = (d1 + d2) * 0.45;
        ctx.lineTo(x + u * w, y + h - val * h);
      }
      ctx.lineTo(x + w, y + h);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();
    }

    function drawMarginalRight(ctx, x, y, w, h, col) {
      ctx.fillStyle = col + '55';
      ctx.strokeStyle = col;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(x, y + h);
      const nBins = 30;
      for (let i = 0; i <= nBins; i++) {
        const u = i / nBins;
        const d = Math.exp(-Math.pow(u - 0.5, 2) / 0.04);
        ctx.lineTo(x + d * (w * 0.8), y + h - u * h);
      }
      ctx.lineTo(x, y);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();
    }

    window.addEventListener('load', () => { setTimeout(drawSeaborn, 100); });
    window.addEventListener('resize', drawSeaborn);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 3. PYGAL
# ==============================================================================
def build_pygal(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">PYGAL RESOLUTION-INDEPENDENT SVG ENGINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="setPygalMode('radar')" id="btn-pygal-radar" style="font-size:0.7rem; padding:3px 8px;">Radar Spider</button>
        <button class="btn-action" onclick="setPygalMode('gauge')" id="btn-pygal-gauge" style="font-size:0.7rem; padding:3px 8px;">SolidGauge</button>
        <button class="btn-action" onclick="toggleSeriesB()" style="font-size:0.7rem; padding:3px 8px;">Toggle Series B</button>
      </div>
    </div>
    <div class="canvas-body" id="pygal-svg-container" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <!-- Dynamic SVG injected here -->
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>chart = pygal.Radar(fill=True, stroke_style={'width': 2}); chart.render_to_file()</span>
      <span>Pure XML/SVG DOM Nodes with CSS Transition Tooltips</span>
    </div>
    """

    custom_js = """
    let pygalMode = 'radar';
    let showSeriesB = true;

    function setPygalMode(mode) {
      pygalMode = mode;
      renderPygal();
    }
    function toggleSeriesB() {
      showSeriesB = !showSeriesB;
      renderPygal();
    }

    function renderPygal() {
      const container = document.getElementById('pygal-svg-container');
      if (!container) return;

      if (pygalMode === 'radar') {
        const axes = ['Latency (ms)', 'Throughput (k/s)', 'GPU Efficiency', 'Accuracy (%)', 'Memory Footprint', 'Reliability'];
        const valsA = [88, 76, 92, 95, 82, 90];
        const valsB = [65, 94, 80, 89, 70, 96];

        const cx = 320; const cy = 250; const R = 180;
        let concentric = '';
        for (let r = 1; r <= 5; r++) {
          const rad = (R / 5) * r;
          let polyPts = [];
          for (let i = 0; i < 6; i++) {
            const angle = (Math.PI * 2 / 6) * i - Math.PI / 2;
            polyPts.push(`${cx + rad * Math.cos(angle)},${cy + rad * Math.sin(angle)}`);
          }
          concentric += `<polygon points="${polyPts.join(' ')}" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>`;
          concentric += `<text x="${cx + 4}" y="${cy - rad + 10}" fill="#64748b" font-family="JetBrains Mono" font-size="10">${r*20}%</text>`;
        }

        let spokes = '';
        let labels = '';
        for (let i = 0; i < 6; i++) {
          const angle = (Math.PI * 2 / 6) * i - Math.PI / 2;
          const x2 = cx + R * Math.cos(angle);
          const y2 = cy + R * Math.sin(angle);
          spokes += `<line x1="${cx}" y1="${cy}" x2="${x2}" y2="${y2}" stroke="rgba(255,255,255,0.15)" stroke-width="1.2"/>`;
          const lx = cx + (R + 25) * Math.cos(angle);
          const ly = cy + (R + 25) * Math.sin(angle);
          labels += `<text x="${lx}" y="${ly}" fill="#f3cf65" font-family="DM Sans" font-size="12" font-weight="600" text-anchor="middle" dominant-baseline="middle">${axes[i]}</text>`;
        }

        // Polygon A
        let ptsA = [];
        for (let i = 0; i < 6; i++) {
          const angle = (Math.PI * 2 / 6) * i - Math.PI / 2;
          const dist = (valsA[i] / 100) * R;
          ptsA.push(`${cx + dist * Math.cos(angle)},${cy + dist * Math.sin(angle)}`);
        }

        // Polygon B
        let ptsB = [];
        for (let i = 0; i < 6; i++) {
          const angle = (Math.PI * 2 / 6) * i - Math.PI / 2;
          const dist = (valsB[i] / 100) * R;
          ptsB.push(`${cx + dist * Math.cos(angle)},${cy + dist * Math.sin(angle)}`);
        }

        container.innerHTML = `
          <svg viewBox="0 0 640 500" style="width:100%; max-width:640px; height:auto; overflow:visible;">
            <defs>
              <linearGradient id="gradA" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#00e676" stop-opacity="0.4"/>
                <stop offset="100%" stop-color="#00e5ff" stop-opacity="0.1"/>
              </linearGradient>
              <linearGradient id="gradB" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ff1744" stop-opacity="0.3"/>
                <stop offset="100%" stop-color="#d500f9" stop-opacity="0.1"/>
              </linearGradient>
            </defs>
            ${concentric}
            ${spokes}
            ${labels}
            <polygon points="${ptsA.join(' ')}" fill="url(#gradA)" stroke="#00e676" stroke-width="2.5"/>
            ${ptsA.map((pt, idx) => `<circle cx="${pt.split(',')[0]}" cy="${pt.split(',')[1]}" r="4" fill="#00e676"><title>Cluster Alpha: ${axes[idx]} = ${valsA[idx]}%</title></circle>`).join('')}

            ${showSeriesB ? `
              <polygon points="${ptsB.join(' ')}" fill="url(#gradB)" stroke="#ff1744" stroke-width="2" stroke-dasharray="4,4"/>
              ${ptsB.map((pt, idx) => `<circle cx="${pt.split(',')[0]}" cy="${pt.split(',')[1]}" r="3.5" fill="#ff1744"><title>Cluster Beta: ${axes[idx]} = ${valsB[idx]}%</title></circle>`).join('')}
            ` : ''}

            <!-- Legend -->
            <rect x="20" y="20" width="14" height="14" fill="#00e676" rx="3"/>
            <text x="42" y="32" fill="#fff" font-family="JetBrains Mono" font-size="11">Alpha Cluster (v3.2)</text>
            ${showSeriesB ? `
              <rect x="20" y="44" width="14" height="14" fill="#ff1744" rx="3"/>
              <text x="42" y="56" fill="#fff" font-family="JetBrains Mono" font-size="11">Beta Baseline (v2.8)</text>
            ` : ''}
          </svg>
        `;
      } else {
        // SolidGauge
        container.innerHTML = `
          <svg viewBox="0 0 640 460" style="width:100%; max-width:640px; height:auto;">
            <g transform="translate(180, 230)">
              <circle r="120" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="24"/>
              <circle r="120" fill="none" stroke="#00e676" stroke-width="24" stroke-dasharray="753" stroke-dashoffset="180" transform="rotate(-90)"/>
              <text x="0" y="10" fill="#fff" font-family="Newsreader" font-size="36" font-weight="600" text-anchor="middle">76.4%</text>
              <text x="0" y="38" fill="#00e676" font-family="JetBrains Mono" font-size="12" text-anchor="middle">GPU UTILIZATION</text>
            </g>
            <g transform="translate(460, 230)">
              <circle r="120" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="24"/>
              <circle r="120" fill="none" stroke="#f3cf65" stroke-width="24" stroke-dasharray="753" stroke-dashoffset="310" transform="rotate(-90)"/>
              <text x="0" y="10" fill="#fff" font-family="Newsreader" font-size="36" font-weight="600" text-anchor="middle">58.9%</text>
              <text x="0" y="38" fill="#f3cf65" font-family="JetBrains Mono" font-size="12" text-anchor="middle">SLA HEADROOM</text>
            </g>
          </svg>
        `;
      }
    }

    window.addEventListener('load', () => { setTimeout(renderPygal, 100); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 4. PLOTNINE (ggplot2)
# ==============================================================================
def build_plotnine(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">PLOTNINE GRAMMAR OF GRAPHICS (GGPLOT2)</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Facet By:</label>
        <select id="p9-facet" onchange="drawPlotnine()" style="background:#070d09; color:#fff; border:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; padding:2px 6px; border-radius:4px;">
          <option value="dept_4">facet_wrap(~department, ncol=2)</option>
          <option value="dept_2">facet_grid(tier ~ region)</option>
        </select>
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); margin-left:6px;">geom_smooth:</label>
        <select id="p9-smooth" onchange="drawPlotnine()" style="background:#070d09; color:#fff; border:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; padding:2px 6px; border-radius:4px;">
          <option value="lm">method='lm' (Linear)</option>
          <option value="loess">method='loess' (Local Polynomial)</option>
        </select>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#040705;">
      <canvas id="p9-stage" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>ggplot(df, aes(x='spend', y='revenue', color='cohort')) + geom_point() + stat_smooth(method='loess') + facet_wrap('~region')</span>
      <span>Wilkinson's Grammar of Graphics Affine Mapping</span>
    </div>
    """

    custom_js = """
    function drawPlotnine() {
      const c = document.getElementById('p9-stage');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const facetType = document.getElementById('p9-facet').value;
      const smoothType = document.getElementById('p9-smooth').value;

      const panels = [
        { name: "Region: North America (NA)", color: "#00e676", slope: 2.2, intercept: 20 },
        { name: "Region: EMEA (Europe)", color: "#00e5ff", slope: 1.7, intercept: 35 },
        { name: "Region: APAC (Asia-Pac)", color: "#f3cf65", slope: 3.1, intercept: 15 },
        { name: "Region: LATAM (Latin Am)", color: "#ff1744", slope: 1.4, intercept: 10 }
      ];

      const pw = (W - 30) / 2;
      const ph = (H - 30) / 2;

      panels.forEach((p, idx) => {
        const col = idx % 2;
        const row = Math.floor(idx / 2);
        const ox = 10 + col * (pw + 10);
        const oy = 10 + row * (ph + 10);

        // Panel header strip (ggplot2 facet strip)
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(ox, oy, pw, 22);
        ctx.fillStyle = '#f8fafc';
        ctx.font = '10px JetBrains Mono';
        ctx.fillText(p.name, ox + 10, oy + 15);

        // Panel plot body
        ctx.fillStyle = '#0b130e';
        ctx.fillRect(ox, oy + 22, pw, ph - 22);
        ctx.strokeStyle = 'rgba(255,255,255,0.08)';
        ctx.strokeRect(ox, oy + 22, pw, ph - 22);

        // Grid lines
        ctx.strokeStyle = 'rgba(255,255,255,0.04)';
        for (let gx = ox + 30; gx < ox + pw; gx += 40) { ctx.beginPath(); ctx.moveTo(gx, oy + 22); ctx.lineTo(gx, oy + ph); ctx.stroke(); }
        for (let gy = oy + 45; gy < oy + ph; gy += 30) { ctx.beginPath(); ctx.moveTo(ox, gy); ctx.lineTo(ox + pw, gy); ctx.stroke(); }

        // Data points
        const nPoints = 35;
        const pts = [];
        for (let i = 0; i < nPoints; i++) {
          const xVal = 10 + (i / nPoints) * 80;
          const noise = (Math.sin(i * 1.7) + Math.cos(i * 0.9)) * 12;
          const yVal = p.intercept + xVal * (p.slope * 0.8) + noise;
          const px = ox + (xVal / 100) * (pw - 20) + 10;
          const py = oy + ph - (yVal / 180) * (ph - 35) - 10;
          pts.push({ x: px, y: py, rawX: xVal });

          ctx.fillStyle = p.color + 'aa';
          ctx.beginPath();
          ctx.arc(px, py, 3, 0, 2*Math.PI);
          ctx.fill();
        }

        // Regression Smooth line
        ctx.strokeStyle = '#fffefa';
        ctx.lineWidth = 2;
        ctx.beginPath();
        if (smoothType === 'lm') {
          const startX = ox + 10;
          const startY = oy + ph - (p.intercept / 180) * (ph - 35) - 10;
          const endX = ox + pw - 10;
          const endY = oy + ph - ((p.intercept + 100 * (p.slope * 0.8)) / 180) * (ph - 35) - 10;
          ctx.moveTo(startX, startY);
          ctx.lineTo(endX, endY);
        } else {
          // Loess smooth curve
          pts.sort((a, b) => a.x - b.x);
          for (let i = 0; i < pts.length; i++) {
            const smoothY = pts[i].y + Math.sin(i * 0.4) * 8;
            if (i === 0) ctx.moveTo(pts[i].x, smoothY);
            else ctx.lineTo(pts[i].x, smoothY);
          }
        }
        ctx.stroke();

        // 95% Confidence Interval Ribbon
        ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.beginPath();
        ctx.moveTo(ox + 10, oy + ph - 25);
        ctx.lineTo(ox + pw - 10, oy + 35);
        ctx.lineTo(ox + pw - 10, oy + 55);
        ctx.lineTo(ox + 10, oy + ph - 15);
        ctx.closePath();
        ctx.fill();
      });
    }

    window.addEventListener('load', () => { setTimeout(drawPlotnine, 100); });
    window.addEventListener('resize', drawPlotnine);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 5. LEATHER
# ==============================================================================
def build_leather(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#b5935b;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">LEATHER ZERO-DEPENDENCY MINIMALIST ENGINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="setLeatherMode('dots')" style="font-size:0.7rem; padding:3px 8px;">Dots & Scales</button>
        <button class="btn-action" onclick="setLeatherMode('step')" style="font-size:0.7rem; padding:3px 8px;">Step Functions</button>
        <button class="btn-action" onclick="setLeatherMode('bars')" style="font-size:0.7rem; padding:3px 8px;">Clean Columns</button>
      </div>
    </div>
    <div class="canvas-body" id="leather-canvas-wrap" style="padding:24px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <!-- Minimalist Leather chart generated dynamically -->
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>chart = leather.Chart('Quarterly Net'); chart.add_dots(data); chart.to_svg('out.svg')</span>
      <span>Zero NumPy/Pandas dependency · Pure Python Typographic Scalability</span>
    </div>
    """

    custom_js = """
    let leatherMode = 'dots';
    function setLeatherMode(mode) {
      leatherMode = mode;
      renderLeather();
    }

    function renderLeather() {
      const wrap = document.getElementById('leather-canvas-wrap');
      if (!wrap) return;

      if (leatherMode === 'dots') {
        wrap.innerHTML = `
          <svg viewBox="0 0 680 440" style="width:100%; max-width:680px; height:auto;">
            <!-- Typographic Header -->
            <text x="40" y="45" fill="#f3cf65" font-family="Newsreader" font-size="24" font-weight="500">Global Micro-Transaction Latency Distribution</text>
            <text x="40" y="68" fill="#94a3b8" font-family="DM Sans" font-size="12">Sampling 48 edge servers across 4 tier-1 transit backbones</text>

            <!-- Grid Axes -->
            <line x1="60" y1="360" x2="640" y2="360" stroke="#334155" stroke-width="1"/>
            <line x1="60" y1="100" x2="60" y2="360" stroke="#334155" stroke-width="1"/>

            ${[100, 165, 230, 295, 360].map((y, i) => `
              <line x1="55" y1="${y}" x2="640" y2="${y}" stroke="rgba(255,255,255,0.05)" stroke-dasharray="2,4"/>
              <text x="45" y="${y+4}" fill="#64748b" font-family="JetBrains Mono" font-size="10" text-anchor="end">${100 - i*25}ms</text>
            `).join('')}

            ${[60, 176, 292, 408, 524, 640].map((x, i) => `
              <text x="${x}" y="380" fill="#64748b" font-family="JetBrains Mono" font-size="10" text-anchor="middle">T+${i*4}h</text>
            `).join('')}

            <!-- Data Dots -->
            ${Array.from({length: 45}).map((_, idx) => {
              const x = 80 + (idx / 45) * 530 + (Math.sin(idx) * 8);
              const y = 330 - Math.pow(idx / 45, 0.7) * 200 + (Math.cos(idx * 2) * 25);
              const r = 3.5 + Math.random() * 2.5;
              return `<circle cx="${x}" cy="${y}" r="${r}" fill="#00e676" opacity="0.85"><title>Ping: ${Math.round(400 - y)}ms</title></circle>`;
            }).join('')}

            <!-- Trend Step Line -->
            <path d="M 80 320 L 160 300 L 260 270 L 380 210 L 490 160 L 610 135" fill="none" stroke="#f3cf65" stroke-width="2.5"/>
          </svg>
        `;
      } else if (leatherMode === 'step') {
        wrap.innerHTML = `
          <svg viewBox="0 0 680 440" style="width:100%; max-width:680px; height:auto;">
            <text x="40" y="45" fill="#f3cf65" font-family="Newsreader" font-size="24" font-weight="500">Autonomous Auto-Scaler Replica Step Function</text>
            <line x1="60" y1="360" x2="640" y2="360" stroke="#334155" stroke-width="1"/>
            <path d="M 60 340 H 140 V 300 H 220 V 250 H 320 V 180 H 420 V 140 H 520 V 220 H 620" fill="none" stroke="#00e5ff" stroke-width="3"/>
            ${[340, 300, 250, 180, 140, 220].map((y, idx) => `
              <circle cx="${140 + idx*80}" cy="${y}" r="5" fill="#f3cf65"/>
            `).join('')}
          </svg>
        `;
      } else {
        wrap.innerHTML = `
          <svg viewBox="0 0 680 440" style="width:100%; max-width:680px; height:auto;">
            <text x="40" y="45" fill="#f3cf65" font-family="Newsreader" font-size="24" font-weight="500">Quarterly Pipeline Throughput (Terabytes)</text>
            <line x1="60" y1="360" x2="640" y2="360" stroke="#334155" stroke-width="1"/>
            ${[45, 82, 115, 160, 210, 280].map((val, idx) => {
              const h = (val / 300) * 260;
              const x = 90 + idx * 90;
              const y = 360 - h;
              return `
                <rect x="${x}" y="${y}" width="48" height="${h}" fill="#00e676" rx="2" opacity="0.9"/>
                <text x="${x + 24}" y="${y - 8}" fill="#fff" font-family="JetBrains Mono" font-size="11" text-anchor="middle">${val}TB</text>
                <text x="${x + 24}" y="380" fill="#94a3b8" font-family="DM Sans" font-size="12" text-anchor="middle">Q${idx+1}</text>
              `;
            }).join('')}
          </svg>
        `;
      }
    }

    window.addEventListener('load', () => { setTimeout(renderLeather, 100); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 6. VEUSZ
# ==============================================================================
def build_veusz(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#ff1744;"></span>
        <span style="color:#ff1744; font-family:var(--font-mono); font-size:0.75rem;">VEUSZ SCIENTIFIC PUBLICATION CANVAS</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Fit Model:</label>
        <button class="btn-action" onclick="toggleVeuszFit()" id="btn-vsz-fit" style="font-size:0.7rem; padding:3px 8px;">Toggle Gaussian Fit</button>
        <button class="btn-action" onclick="toggleErrorBars()" style="font-size:0.7rem; padding:3px 8px;">Toggle Asymmetric Error</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#040705;">
      <canvas id="veusz-stage" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>import veusz.embed as veusz; g = veusz.Embedded('window'); g.To('/plot1')</span>
      <span>Sub-Millimeter High Precision Vector Node Tree Architecture</span>
    </div>
    """

    custom_js = """
    let showVeuszFit = true;
    let showErrorBars = true;

    function toggleVeuszFit() { showVeuszFit = !showVeuszFit; drawVeusz(); }
    function toggleErrorBars() { showErrorBars = !showErrorBars; drawVeusz(); }

    function drawVeusz() {
      const c = document.getElementById('veusz-stage');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const margin = { top: 40, right: 60, bottom: 60, left: 70 };
      const pw = W - margin.left - margin.right;
      const ph = H - margin.top - margin.bottom;

      // Inner plot box with crisp double stroke
      ctx.strokeStyle = '#e2e8f0';
      ctx.lineWidth = 1.5;
      ctx.strokeRect(margin.left, margin.top, pw, ph);

      // Major and minor ticks
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '10px JetBrains Mono';
      for (let i = 0; i <= 10; i++) {
        const x = margin.left + (pw / 10) * i;
        ctx.beginPath(); ctx.moveTo(x, margin.top + ph); ctx.lineTo(x, margin.top + ph - (i % 2 === 0 ? 8 : 4)); ctx.stroke();
        if (i % 2 === 0) {
          ctx.textAlign = 'center';
          ctx.fillText((200 + i * 20) + ' nm', x, margin.top + ph + 16);
        }
      }

      for (let i = 0; i <= 8; i++) {
        const y = margin.top + (ph / 8) * i;
        ctx.beginPath(); ctx.moveTo(margin.left, y); ctx.lineTo(margin.left + (i % 2 === 0 ? 8 : 4), y); ctx.stroke();
        if (i % 2 === 0) {
          ctx.textAlign = 'right';
          ctx.fillText((80 - i * 10) + ' a.u.', margin.left - 10, y + 4);
        }
      }

      // Generate Spectroscopy Data with Asymmetric Errors
      const nSamples = 28;
      const pts = [];
      for (let i = 0; i < nSamples; i++) {
        const lambda = 200 + (i / nSamples) * 200;
        const peak = 72 * Math.exp(-Math.pow(lambda - 295, 2) / (2 * 28 * 28));
        const noise = (Math.sin(i * 1.5) + (Math.random() - 0.5)) * 3;
        const yVal = peak + 10 + noise;
        const errPlus = 2 + Math.random() * 4;
        const errMinus = 1.5 + Math.random() * 3;
        pts.push({
          x: margin.left + ((lambda - 200) / 200) * pw,
          y: margin.top + ph - (yVal / 90) * ph,
          errP: (errPlus / 90) * ph,
          errM: (errMinus / 90) * ph
        });
      }

      // Draw Data points and Asymmetric Error Bars
      pts.forEach(p => {
        if (showErrorBars) {
          ctx.strokeStyle = 'rgba(243, 207, 101, 0.7)';
          ctx.lineWidth = 1.2;
          ctx.beginPath();
          ctx.moveTo(p.x, p.y - p.errP);
          ctx.lineTo(p.x, p.y + p.errM);
          ctx.stroke();
          // Caps
          ctx.beginPath();
          ctx.moveTo(p.x - 3, p.y - p.errP); ctx.lineTo(p.x + 3, p.y - p.errP);
          ctx.moveTo(p.x - 3, p.y + p.errM); ctx.lineTo(p.x + 3, p.y + p.errM);
          ctx.stroke();
        }

        // Diamond marker
        ctx.fillStyle = '#00e676';
        ctx.strokeStyle = '#050806';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(p.x, p.y - 4);
        ctx.lineTo(p.x + 4, p.y);
        ctx.lineTo(p.x, p.y + 4);
        ctx.lineTo(p.x - 4, p.y);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
      });

      // Fitted Gaussian Curve
      if (showVeuszFit) {
        ctx.strokeStyle = '#ff1744';
        ctx.lineWidth = 2.2;
        ctx.beginPath();
        for (let xPix = 0; xPix <= pw; xPix += 2) {
          const lambda = 200 + (xPix / pw) * 200;
          const fitY = 72 * Math.exp(-Math.pow(lambda - 295, 2) / (2 * 28 * 28)) + 10;
          const yPix = margin.top + ph - (fitY / 90) * ph;
          if (xPix === 0) ctx.moveTo(margin.left + xPix, yPix);
          else ctx.lineTo(margin.left + xPix, yPix);
        }
        ctx.stroke();

        // Fit info banner
        ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
        ctx.strokeStyle = 'rgba(255,255,255,0.15)';
        ctx.strokeRect(margin.left + pw - 220, margin.top + 20, 200, 60);
        ctx.fillRect(margin.left + pw - 220, margin.top + 20, 200, 60);

        ctx.fillStyle = '#ff1744';
        ctx.font = '11px JetBrains Mono';
        ctx.textAlign = 'left';
        ctx.fillText('Gauss Fit: R² = 0.9942', margin.left + pw - 210, margin.top + 38);
        ctx.fillStyle = '#94a3b8';
        ctx.fillText('μ = 295.1 nm | σ = 28.3 nm', margin.left + pw - 210, margin.top + 55);
        ctx.fillText('χ² / DoF = 1.08', margin.left + pw - 210, margin.top + 70);
      }

      // X/Y Axis Labels
      ctx.fillStyle = '#f8fafc';
      ctx.font = '12px DM Sans';
      ctx.textAlign = 'center';
      ctx.fillText('Absorption Wavelength λ (nm)', margin.left + pw/2, H - 20);

      ctx.save();
      ctx.translate(22, margin.top + ph/2);
      ctx.rotate(-Math.PI/2);
      ctx.fillText('Optical Density Extinction ε (a.u.)', 0, 0);
      ctx.restore();
    }

    window.addEventListener('load', () => { setTimeout(drawVeusz, 100); });
    window.addEventListener('resize', drawVeusz);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 7. GR FRAMEWORK
# ==============================================================================
def build_gr(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676; box-shadow:0 0 10px #00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">GR C-ACCELERATED RUNTIME (120 FPS CAPABLE)</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--gold-bright);">FPS: <strong id="gr-fps">120</strong></span>
        <button class="btn-action" onclick="toggleGrRunning()" id="btn-gr-run" style="font-size:0.7rem; padding:3px 8px;">Pause Stream</button>
        <button class="btn-action" onclick="stepGrSignal()" style="font-size:0.7rem; padding:3px 8px;">Modulate Freq</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#020403; display:flex; flex-direction:column; gap:8px;">
      <div style="flex:1; width:100%; position:relative;">
        <canvas id="gr-canvas-wave" style="width:100%; height:100%; min-height:260px;"></canvas>
      </div>
      <div style="height:160px; width:100%; position:relative;">
        <canvas id="gr-canvas-waterfall" style="width:100%; height:100%;"></canvas>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>import gr; gr.plot(x, y); gr.heatmap(spectral_grid)</span>
      <span>Microsecond Native C Kernel Rendering Pipeline</span>
    </div>
    """

    custom_js = """
    let grRunning = true;
    let grPhase = 0;
    let grCarrier = 3.0;
    let grLastTime = performance.now();
    let grFrameCount = 0;
    const waterfallHistory = [];

    function toggleGrRunning() {
      grRunning = !grRunning;
      document.getElementById('btn-gr-run').innerText = grRunning ? 'Pause Stream' : 'Resume Stream';
      if (grRunning) requestAnimationFrame(grLoop);
    }

    function stepGrSignal() {
      grCarrier = grCarrier === 3.0 ? 6.5 : 3.0;
    }

    function grLoop(timestamp) {
      if (!grRunning) return;

      grFrameCount++;
      if (timestamp - grLastTime >= 1000) {
        document.getElementById('gr-fps').innerText = Math.round((grFrameCount * 1000) / (timestamp - grLastTime));
        grFrameCount = 0;
        grLastTime = timestamp;
      }

      grPhase += 0.08;
      drawGrWave();
      drawGrWaterfall();

      requestAnimationFrame(grLoop);
    }

    function drawGrWave() {
      const c = document.getElementById('gr-canvas-wave');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#020403';
      ctx.fillRect(0, 0, W, H);

      // CRT Phosphor grid
      ctx.strokeStyle = 'rgba(0, 230, 118, 0.08)';
      ctx.lineWidth = 1;
      for (let x = 0; x < W; x += 25) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
      for (let y = 0; y < H; y += 20) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      // Oscilloscope High-Speed Waveform
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.shadowColor = '#00e676';
      ctx.shadowBlur = 8;
      ctx.beginPath();

      const nPts = 400;
      const currRow = [];
      for (let i = 0; i < nPts; i++) {
        const t = (i / nPts) * 6 * Math.PI;
        // Modulated wave packet
        const env = Math.exp(-Math.pow(t - 3*Math.PI + Math.sin(grPhase)*2, 2) / 12);
        const yVal = Math.sin(grCarrier * t + grPhase) * env * (H * 0.42);
        const px = (i / nPts) * W;
        const py = H/2 - yVal;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);

        if (i % 8 === 0) currRow.push(Math.abs(yVal) / (H * 0.42));
      }
      ctx.stroke();
      ctx.shadowBlur = 0;

      waterfallHistory.unshift(currRow);
      if (waterfallHistory.length > 50) waterfallHistory.pop();
    }

    function drawGrWaterfall() {
      const c = document.getElementById('gr-canvas-waterfall');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#020403';
      ctx.fillRect(0, 0, W, H);

      const rows = waterfallHistory.length;
      if (rows === 0) return;
      const cols = waterfallHistory[0].length;
      const cellW = W / cols;
      const cellH = H / rows;

      for (let r = 0; r < rows; r++) {
        for (let cl = 0; cl < cols; cl++) {
          const val = waterfallHistory[r][cl] || 0;
          // Inferno palette
          const hue = 180 + val * 160;
          ctx.fillStyle = `hsla(${hue}, 90%, ${val * 60}%, ${1.0 - (r/rows)*0.8})`;
          ctx.fillRect(cl * cellW, r * cellH, cellW + 0.5, cellH + 0.5);
        }
      }
    }

    window.addEventListener('load', () => { requestAnimationFrame(grLoop); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 8. VISVIS
# ==============================================================================
def build_visvis(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">VISVIS 3D VOLUMETRIC MIP RECONSTRUCTION</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Orthogonal Plane:</label>
        <button class="btn-action" onclick="setVisvisPlane('axial')" id="btn-vv-ax" style="font-size:0.7rem; padding:3px 8px;">Axial (Z)</button>
        <button class="btn-action" onclick="setVisvisPlane('coronal')" id="btn-vv-co" style="font-size:0.7rem; padding:3px 8px;">Coronal (Y)</button>
        <button class="btn-action" onclick="setVisvisPlane('sagittal')" id="btn-vv-sa" style="font-size:0.7rem; padding:3px 8px;">Sagittal (X)</button>
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); margin-left:6px;">Slice:</label>
        <input type="range" id="vv-slice" min="0" max="63" value="32" oninput="drawVisvis()" style="width:70px;">
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center; gap:16px;">
      <div style="background:#000; border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:6px; text-align:center;">
        <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--gold-bright); margin-bottom:4px;" id="vv-plane-lbl">Multi-Planar Slice (32/64)</div>
        <canvas id="vv-slice-canvas" width="280" height="280" style="border:1px solid #1e293b; image-rendering:pixelated;"></canvas>
      </div>
      <div style="background:#000; border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:6px; text-align:center;">
        <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--cyan-neon); margin-bottom:4px;">3D Volumetric MIP Raycast Ray-March</div>
        <canvas id="vv-mip-canvas" width="280" height="280" style="border:1px solid #1e293b;"></canvas>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>import visvis as vv; vol = vv.volread('stent.v3d'); vv.volshow(vol, renderStyle='mip')</span>
      <span>OpenGL 3D Texture Memory Multi-Planar Orthogonal Pipeline</span>
    </div>
    """

    custom_js = """
    let visvisPlane = 'axial';
    const volSize = 48;
    // Generate synthetic 3D scalar volume (ellipsoid core + toroidal vessels)
    const volumeData = new Float32Array(volSize * volSize * volSize);
    for (let z = 0; z < volSize; z++) {
      for (let y = 0; y < volSize; y++) {
        for (let x = 0; x < volSize; x++) {
          const idx = z * volSize * volSize + y * volSize + x;
          const nx = (x - volSize/2) / (volSize/2);
          const ny = (y - volSize/2) / (volSize/2);
          const nz = (z - volSize/2) / (volSize/2);

          // Sphere
          const r = Math.sqrt(nx*nx + ny*ny + nz*nz);
          let val = 0;
          if (r < 0.7) val = (0.7 - r) * 1.5;

          // Torus
          const rTor = Math.sqrt(nx*nx + ny*ny);
          const distTor = Math.sqrt(Math.pow(rTor - 0.5, 2) + nz*nz);
          if (distTor < 0.15) val = Math.max(val, 0.9);

          volumeData[idx] = val;
        }
      }
    }

    function setVisvisPlane(plane) {
      visvisPlane = plane;
      document.getElementById('vv-plane-lbl').innerText = `Slice Plane: ${plane.toUpperCase()} (Z=${document.getElementById('vv-slice').value})`;
      drawVisvis();
    }

    function drawVisvis() {
      const sliceIdx = Math.min(parseInt(document.getElementById('vv-slice').value), volSize - 1);
      drawSlice(sliceIdx);
      drawMip();
    }

    function drawSlice(sliceIdx) {
      const c = document.getElementById('vv-slice-canvas');
      if (!c) return;
      const ctx = c.getContext('2d');
      const imgData = ctx.createImageData(volSize, volSize);

      for (let row = 0; row < volSize; row++) {
        for (let col = 0; col < volSize; col++) {
          let val = 0;
          if (visvisPlane === 'axial') {
            val = volumeData[sliceIdx * volSize * volSize + row * volSize + col];
          } else if (visvisPlane === 'coronal') {
            val = volumeData[row * volSize * volSize + sliceIdx * volSize + col];
          } else {
            val = volumeData[row * volSize * volSize + col * volSize + sliceIdx];
          }

          const pIdx = (row * volSize + col) * 4;
          const cVal = Math.floor(Math.min(val, 1.0) * 255);
          imgData.data[pIdx] = cVal > 100 ? cVal : 0;
          imgData.data[pIdx+1] = cVal;
          imgData.data[pIdx+2] = cVal > 150 ? 255 : cVal;
          imgData.data[pIdx+3] = 255;
        }
      }

      // Draw magnified to canvas
      const tempC = document.createElement('canvas');
      tempC.width = volSize; tempC.height = volSize;
      tempC.getContext('2d').putImageData(imgData, 0, 0);

      ctx.imageSmoothingEnabled = false;
      ctx.drawImage(tempC, 0, 0, c.width, c.height);
    }

    function drawMip() {
      const c = document.getElementById('vv-mip-canvas');
      if (!c) return;
      const ctx = c.getContext('2d');
      const imgData = ctx.createImageData(volSize, volSize);

      // Maximum Intensity Projection along Z
      for (let y = 0; y < volSize; y++) {
        for (let x = 0; x < volSize; x++) {
          let maxVal = 0;
          for (let z = 0; z < volSize; z++) {
            const val = volumeData[z * volSize * volSize + y * volSize + x];
            if (val > maxVal) maxVal = val;
          }
          const pIdx = (y * volSize + x) * 4;
          const cVal = Math.floor(Math.min(maxVal, 1.0) * 255);
          imgData.data[pIdx] = Math.floor(cVal * 0.2);
          imgData.data[pIdx+1] = cVal;
          imgData.data[pIdx+2] = Math.floor(cVal * 0.9);
          imgData.data[pIdx+3] = 255;
        }
      }

      const tempC = document.createElement('canvas');
      tempC.width = volSize; tempC.height = volSize;
      tempC.getContext('2d').putImageData(imgData, 0, 0);

      ctx.imageSmoothingEnabled = true;
      ctx.drawImage(tempC, 0, 0, c.width, c.height);
    }

    window.addEventListener('load', () => { setTimeout(drawVisvis, 100); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 9. CHACO
# ==============================================================================
def build_chaco(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">CHACO COMPONENT PLOTTING ARCHITECTURE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="toggleChacoCursor()" id="btn-chaco-cross" style="font-size:0.7rem; padding:3px 8px;">Crosshair Calipers</button>
        <button class="btn-action" onclick="toggleChacoTrace2()" style="font-size:0.7rem; padding:3px 8px;">Toggle Trace 2</button>
        <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--cyan-neon);">Δt: <span id="chaco-dt">1.45</span>ms</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#040705;">
      <canvas id="chaco-stage" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>plot = Plot(ArrayPlotData(x=t, y=signal)); plot.plot(('x', 'y'), type='line', color='teal')</span>
      <span>Enthought Traits + Enable GUI Layout Scenegraph Engine</span>
    </div>
    """

    custom_js = """
    let showCrosshair = true;
    let showTrace2 = true;
    let mousePos = { x: 280, y: 190 };

    function toggleChacoCursor() { showCrosshair = !showCrosshair; drawChaco(); }
    function toggleChacoTrace2() { showTrace2 = !showTrace2; drawChaco(); }

    function drawChaco() {
      const c = document.getElementById('chaco-stage');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const margin = { top: 40, right: 40, bottom: 50, left: 60 };
      const pw = W - margin.left - margin.right;
      const ph = H - margin.top - margin.bottom;

      // Plot area background
      ctx.fillStyle = '#070f0b';
      ctx.fillRect(margin.left, margin.top, pw, ph);
      ctx.strokeStyle = '#1e3a29';
      ctx.strokeRect(margin.left, margin.top, pw, ph);

      // Grid
      ctx.strokeStyle = 'rgba(255,255,255,0.06)';
      ctx.lineWidth = 1;
      for (let x = margin.left; x <= margin.left + pw; x += 50) {
        ctx.beginPath(); ctx.moveTo(x, margin.top); ctx.lineTo(x, margin.top + ph); ctx.stroke();
      }
      for (let y = margin.top; y <= margin.top + ph; y += 40) {
        ctx.beginPath(); ctx.moveTo(margin.left, y); ctx.lineTo(margin.left + pw, y); ctx.stroke();
      }

      // Trace 1: Primary Telemetry RF Signal
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.beginPath();
      const nPts = 300;
      for (let i = 0; i < nPts; i++) {
        const t = (i / nPts) * 10;
        const s = Math.sin(t * 2) * Math.cos(t * 0.5) + (Math.sin(t * 8) * 0.2);
        const px = margin.left + (i / nPts) * pw;
        const py = margin.top + ph/2 - s * (ph * 0.38);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Trace 2: Secondary Demodulated Envelope
      if (showTrace2) {
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 1.8;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        for (let i = 0; i < nPts; i++) {
          const t = (i / nPts) * 10;
          const s = Math.abs(Math.cos(t * 0.5)) * 1.1;
          const px = margin.left + (i / nPts) * pw;
          const py = margin.top + ph/2 - s * (ph * 0.38);
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Crosshair Measurement Calipers
      if (showCrosshair) {
        ctx.strokeStyle = '#00e5ff';
        ctx.lineWidth = 1;
        ctx.setLineDash([2, 2]);

        // Caliper A (Fixed)
        const calAx = margin.left + pw * 0.35;
        ctx.beginPath(); ctx.moveTo(calAx, margin.top); ctx.lineTo(calAx, margin.top + ph); ctx.stroke();

        // Caliper B (Mouse track)
        const calBx = Math.max(margin.left, Math.min(margin.left + pw, mousePos.x));
        ctx.beginPath(); ctx.moveTo(calBx, margin.top); ctx.lineTo(calBx, margin.top + ph); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(margin.left, mousePos.y); ctx.lineTo(margin.left + pw, mousePos.y); ctx.stroke();
        ctx.setLineDash([]);

        // Caliper span highlight
        ctx.fillStyle = 'rgba(0, 229, 255, 0.08)';
        ctx.fillRect(Math.min(calAx, calBx), margin.top, Math.abs(calBx - calAx), ph);

        const dt = (Math.abs(calBx - calAx) / pw * 10).toFixed(2);
        document.getElementById('chaco-dt').innerText = dt;

        ctx.fillStyle = '#00e5ff';
        ctx.font = '10px JetBrains Mono';
        ctx.fillText(`Δt = ${dt} ms`, Math.min(calAx, calBx) + 8, margin.top + 20);
      }

      // Legend
      ctx.fillStyle = 'rgba(10, 18, 14, 0.85)';
      ctx.fillRect(margin.left + 15, margin.top + 15, 160, 45);
      ctx.strokeStyle = 'rgba(255,255,255,0.1)';
      ctx.strokeRect(margin.left + 15, margin.top + 15, 160, 45);

      ctx.fillStyle = '#00e676';
      ctx.font = '10px JetBrains Mono';
      ctx.fillText('● Chaco Raw RF Stream', margin.left + 25, margin.top + 32);
      if (showTrace2) {
        ctx.fillStyle = '#f3cf65';
        ctx.fillText('● Demodulated Envelope', margin.left + 25, margin.top + 48);
      }
    }

    window.addEventListener('load', () => {
      setTimeout(() => {
        const c = document.getElementById('chaco-stage');
        if (c) {
          c.addEventListener('mousemove', (e) => {
            const rect = c.getBoundingClientRect();
            mousePos = { x: e.clientX - rect.left, y: e.clientY - rect.top };
            drawChaco();
          });
        }
        drawChaco();
      }, 100);
    });
    window.addEventListener('resize', drawChaco);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)
