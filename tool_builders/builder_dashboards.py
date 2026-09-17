"""
Builder for Interactive Dashboards & Web Apps Tools (8 tools):
Streamlit, Gradio, Panel, Taipy, Reflex, Gleam, Anvil, Solara
Each tool gets a completely authentic, bespoke UI simulator reflecting its exact framework paradigm!
"""

import os
import json
from .common_frame import render_tool_page
from data_cat5_dashboards import TOOLS_CAT5

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(SCRIPT_DIR, "Python Visualization, Graphical, & Interactive Libraries", "Interactive Dashboards & Web Apps")

def write_tool_output(tool_folder, html_content):
    target_dir = os.path.join(BASE_DIR, tool_folder)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    clean_name = tool_folder.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  [✓] {tool_folder:<35} -> Dedicated Interactive Studio Built ({len(html_content)/1024:.1f} KB)")

def build_dashboards_tools():
    tool_map = {t["folder"]: t for t in TOOLS_CAT5}

    build_streamlit(tool_map["Streamlit"])
    build_gradio(tool_map["Gradio"])
    build_panel(tool_map["Panel"])
    build_taipy(tool_map["Taipy"])
    build_reflex(tool_map["Reflex"])
    build_gleam(tool_map["Gleam"])
    build_anvil(tool_map["Anvil"])
    build_solara(tool_map["Solara"])

# ==============================================================================
# 1. STREAMLIT
# ==============================================================================
def build_streamlit(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#ff4b4b;"></span>
        <span style="color:#ff4b4b; font-family:var(--font-mono); font-size:0.75rem;">STREAMLIT REACTIVE RUNTIME v1.32</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">Running: app.py</span>
        <button class="btn-action" onclick="rerunStreamlit()" style="font-size:0.7rem; padding:3px 8px;">Rerun (R)</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:0; background:#0e1117; display:flex; height:100%; min-height:480px; color:#fafafa; font-family:'DM Sans', sans-serif;">
      <!-- Streamlit Sidebar -->
      <div style="width:240px; background:#262730; border-right:1px solid rgba(255,255,255,0.1); padding:16px; display:flex; flex-direction:column; gap:16px;">
        <div style="font-family:var(--font-mono); font-size:0.75rem; color:#94a3b8; text-transform:uppercase;">st.sidebar</div>
        <div>
          <label style="font-size:0.75rem; color:#fafafa; display:block; margin-bottom:4px;">Sampling Horizon (Days)</label>
          <input type="range" id="st-slider" min="15" max="180" value="60" oninput="updateStreamlit()" style="width:100%;">
          <div style="font-family:var(--font-mono); font-size:0.7rem; color:#ff4b4b; text-align:right;" id="st-slider-val">60 days</div>
        </div>
        <div>
          <label style="font-size:0.75rem; color:#fafafa; display:block; margin-bottom:4px;">st.selectbox("Channel")</label>
          <select id="st-channel" onchange="updateStreamlit()" style="width:100%; background:#0e1117; color:#fff; border:1px solid rgba(255,255,255,0.2); font-size:0.75rem; padding:4px; border-radius:4px;">
            <option value="all">All Channels (Blended)</option>
            <option value="direct">Direct Web / App</option>
            <option value="retail">Retail Media Network</option>
          </select>
        </div>
        <div style="margin-top:auto; font-family:var(--font-mono); font-size:0.68rem; color:#64748b;">
          Memory: 48.2 MB<br>Session ID: sess_94f8a
        </div>
      </div>

      <!-- Main App Page -->
      <div style="flex:1; padding:20px; overflow-y:auto; display:flex; flex-direction:column; gap:16px;">
        <h2 style="font-family:'Newsreader', serif; font-size:1.6rem; font-weight:600; color:#fff;">Commercial Revenue Governance</h2>

        <!-- st.columns(3) Metric Cards -->
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px;">
          <div style="background:#262730; padding:12px; border-radius:6px; border:1px solid rgba(255,255,255,0.06);">
            <div style="font-size:0.75rem; color:#94a3b8;">Total Attributed Gross</div>
            <div style="font-size:1.4rem; font-weight:700; color:#fff; margin:4px 0;" id="st-kpi-rev">$1.42M</div>
            <div style="font-size:0.75rem; color:#00e676;">▲ +14.2% YoY</div>
          </div>
          <div style="background:#262730; padding:12px; border-radius:6px; border:1px solid rgba(255,255,255,0.06);">
            <div style="font-size:0.75rem; color:#94a3b8;">Commission Recapture</div>
            <div style="font-size:1.4rem; font-weight:700; color:#ff4b4b; margin:4px 0;" id="st-kpi-comm">$385K</div>
            <div style="font-size:0.75rem; color:#00e676;">▲ +22.8% Recaptured</div>
          </div>
          <div style="background:#262730; padding:12px; border-radius:6px; border:1px solid rgba(255,255,255,0.06);">
            <div style="font-size:0.75rem; color:#94a3b8;">Blended ROAS Target</div>
            <div style="font-size:1.4rem; font-weight:700; color:#f3cf65; margin:4px 0;">4.85x</div>
            <div style="font-size:0.75rem; color:#00e676;">▲ Above SLA (4.0x)</div>
          </div>
        </div>

        <!-- st.line_chart -->
        <div style="background:#262730; padding:12px; border-radius:6px; border:1px solid rgba(255,255,255,0.06); flex:1; min-height:220px; display:flex; flex-direction:column;">
          <div style="font-family:var(--font-mono); font-size:0.72rem; color:#94a3b8; margin-bottom:6px;">st.line_chart(df[['Direct', 'Recapture']])</div>
          <canvas id="st-chart-canvas" style="width:100%; flex:1;"></canvas>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>st.set_page_config(layout='wide'); st.sidebar.slider(); st.metric(); st.line_chart()</span>
      <span>Tornado Reactive Engine · AST Hash @st.cache_data Memoization</span>
    </div>
    """

    custom_js = """
    function updateStreamlit() {
      const days = parseInt(document.getElementById('st-slider').value);
      document.getElementById('st-slider-val').innerText = `${days} days`;
      document.getElementById('st-kpi-rev').innerText = `$${(days * 0.024).toFixed(2)}M`;
      document.getElementById('st-kpi-comm').innerText = `$${Math.round(days * 6.4)}K`;
      drawStreamlitChart(days);
    }

    function rerunStreamlit() { updateStreamlit(); }

    function drawStreamlitChart(days) {
      const c = document.getElementById('st-chart-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#262730';
      ctx.fillRect(0, 0, W, H);

      // Grid
      ctx.strokeStyle = 'rgba(255,255,255,0.05)';
      for (let y = 0; y < H; y += 30) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      // Direct curve
      ctx.strokeStyle = '#ff4b4b';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i < days; i++) {
        const x = (i / days) * W;
        const y = H * 0.8 - Math.sin(i * 0.1) * 30 - (i / days) * (H * 0.5);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Recapture curve
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      for (let i = 0; i < days; i++) {
        const x = (i / days) * W;
        const y = H * 0.85 - Math.cos(i * 0.08) * 20 - (i / days) * (H * 0.35);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }

    window.addEventListener('load', () => { setTimeout(updateStreamlit, 100); });
    window.addEventListener('resize', updateStreamlit);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 2. GRADIO
# ==============================================================================
def build_gradio(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">GRADIO BLOCKS ML INFERENCE INTERFACE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">Gradio v4.19 · FastAPI Backend</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#0b0f17; display:flex; flex-direction:column; gap:16px; height:100%; min-height:480px; overflow-y:auto; color:#f8fafc;">
      <h3 style="font-family:'Newsreader', serif; font-size:1.4rem; color:#fff;">Multi-Modal Commercial Intelligence Assistant</h3>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; flex:1;">
        <!-- Inputs Block -->
        <div style="background:#1a202c; border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:14px; display:flex; flex-direction:column; gap:12px;">
          <div style="font-family:var(--font-mono); font-size:0.72rem; color:#f3cf65; text-transform:uppercase;">gr.Column() - Model Inputs</div>
          <div>
            <label style="font-size:0.75rem; color:#cbd5e1; display:block; margin-bottom:4px;">Prompt Instruction</label>
            <textarea id="gr-prompt" style="width:100%; height:80px; background:#0b0f17; border:1px solid rgba(255,255,255,0.15); color:#fff; font-family:'DM Sans', sans-serif; font-size:0.82rem; padding:8px; border-radius:4px; resize:none;">Analyze Q3 APAC direct booking conversion delta with Bayesian holdout lift.</textarea>
          </div>
          <div>
            <label style="font-size:0.75rem; color:#cbd5e1; display:block; margin-bottom:4px;">Foundation Model</label>
            <select id="gr-model" style="width:100%; background:#0b0f17; color:#fff; border:1px solid rgba(255,255,255,0.15); font-size:0.8rem; padding:6px; border-radius:4px;">
              <option value="claude">Claude 3.5 Sonnet (Commercial Strategy)</option>
              <option value="llama">Llama-3-70B-Instruct (Local Private Enclave)</option>
              <option value="gemini">Gemini 1.5 Pro (Long-Context Audit)</option>
            </select>
          </div>
          <div>
            <label style="font-size:0.75rem; color:#cbd5e1; display:block; margin-bottom:4px;">Temperature (Creativity vs Determinism)</label>
            <input type="range" id="gr-temp" min="0.0" max="1.0" step="0.05" value="0.2" style="width:100%;">
          </div>
          <button class="btn-action" onclick="runGradioInference()" style="margin-top:auto; background:#f3cf65; color:#040705; font-weight:700; font-size:0.8rem; padding:8px; text-align:center; border:none; justify-content:center;">
            ⚡ gr.Button("Submit Query")
          </button>
        </div>

        <!-- Outputs Block -->
        <div style="background:#1a202c; border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:14px; display:flex; flex-direction:column; gap:10px;">
          <div style="font-family:var(--font-mono); font-size:0.72rem; color:#00e676; text-transform:uppercase;">gr.Column() - Reactive Output</div>
          <div id="gr-output-box" style="flex:1; background:#0b0f17; border:1px solid rgba(255,255,255,0.1); border-radius:4px; padding:12px; font-family:var(--font-mono); font-size:0.78rem; color:#cbd5e1; overflow-y:auto; line-height:1.5;">
            Ready for inference request...
          </div>
          <div style="display:flex; justify-content:space-between; font-family:var(--font-mono); font-size:0.7rem; color:#64748b;">
            <span>Latency: <strong id="gr-lat" style="color:#00e676;">--</strong></span>
            <span>Tokens: <strong id="gr-tok" style="color:#f3cf65;">--</strong></span>
          </div>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>with gr.Blocks() as demo: prompt = gr.Textbox(); btn = gr.Button(); btn.click(fn=predict, inputs=prompt, outputs=ans)</span>
      <span>FastAPI Async Engine · Svelte Component Two-Way Event Hydration</span>
    </div>
    """

    custom_js = """
    function runGradioInference() {
      const out = document.getElementById('gr-output-box');
      out.innerHTML = '<span style="color:#f3cf65;">[Gradio WebSocket Stream: Generating tokens...]</span>';
      document.getElementById('gr-lat').innerText = '...';

      setTimeout(() => {
        out.innerHTML = `
<strong style="color:#00e676;">[Evaluation Complete]</strong>
• <strong>Bayesian Incremental Lift:</strong> +4.8% (95% HDI [2.1%, 7.4%])
• <strong>Estimated Margin Recapture:</strong> +S$148,000 / month
• <strong>Governance Risk Flag:</strong> Low attribution cannibalization across branded search.
• <strong>Recommended Action:</strong> Maintain current 10% non-exposed holdout cluster.
        `;
        document.getElementById('gr-lat').innerText = '248 ms';
        document.getElementById('gr-tok').innerText = '142 tokens';
      }, 400);
    }
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 3. PANEL
# ==============================================================================
def build_panel(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">PANEL PARAM REACTIVE SCIENTIFIC DASHBOARD</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Param Metric:</label>
        <select id="pn-metric" onchange="drawPanelCharts()" style="background:#070d09; color:#fff; border:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; padding:2px 6px; border-radius:4px;">
          <option value="conversion">Direct Booking Conversion Rate (%)</option>
          <option value="aov">Average Order Value (AOV in USD)</option>
        </select>
        <button class="btn-action" onclick="resamplePanel()" style="font-size:0.7rem; padding:3px 8px;">Sync Param</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; flex-direction:column; gap:12px;">
      <div style="display:grid; grid-template-columns: 1.2fr 1fr; gap:12px; flex:1;">
        <div style="background:#070d09; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:10px; display:flex; flex-direction:column;">
          <div style="font-family:var(--font-mono); font-size:0.7rem; color:var(--gold-bright); margin-bottom:6px;">pn.bind(view_timeseries, metric=metric_selector)</div>
          <canvas id="pn-canvas-time" style="width:100%; flex:1; min-height:220px;"></canvas>
        </div>
        <div style="background:#070d09; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:10px; display:flex; flex-direction:column;">
          <div style="font-family:var(--font-mono); font-size:0.7rem; color:var(--cyan-neon); margin-bottom:6px;">pn.bind(view_breakdown, metric=metric_selector)</div>
          <canvas id="pn-canvas-bar" style="width:100%; flex:1; min-height:220px;"></canvas>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>template = pn.template.FastListTemplate(title='Portfolio Analytics'); template.servable()</span>
      <span>HoloViz Param Ecosystem · Bi-directional Bokeh Server WebSockets</span>
    </div>
    """

    custom_js = """
    function resamplePanel() { drawPanelCharts(); }

    function drawPanelCharts() {
      const metric = document.getElementById('pn-metric').value;
      drawPanelTimeseries(metric);
      drawPanelBars(metric);
    }

    function drawPanelTimeseries(metric) {
      const c = document.getElementById('pn-canvas-time');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070d09';
      ctx.fillRect(0, 0, W, H);

      ctx.strokeStyle = '#00e5ff';
      ctx.lineWidth = 2;
      ctx.beginPath();
      const n = 50;
      for (let i = 0; i < n; i++) {
        const x = (i / n) * W;
        const val = metric === 'conversion' ? (2.5 + Math.sin(i * 0.2) * 0.8) : (350 + Math.sin(i * 0.2) * 80);
        const norm = metric === 'conversion' ? (val / 5.0) : (val / 600);
        const y = H - 20 - norm * (H - 40);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }

    function drawPanelBars(metric) {
      const c = document.getElementById('pn-canvas-bar');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070d09';
      ctx.fillRect(0, 0, W, H);

      const regions = ['Singapore', 'Seoul', 'Tokyo', 'London', 'Sydney'];
      const vals = metric === 'conversion' ? [4.2, 3.8, 3.1, 2.9, 3.5] : [480, 420, 390, 520, 450];
      const maxV = metric === 'conversion' ? 6.0 : 600;

      const barW = (W - 40) / regions.length;
      regions.forEach((r, idx) => {
        const h = (vals[idx] / maxV) * (H - 50);
        const x = 20 + idx * barW;
        const y = H - 30 - h;

        ctx.fillStyle = '#00e676';
        ctx.fillRect(x, y, barW - 12, h);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '9px JetBrains Mono';
        ctx.fillText(r, x, H - 12);
      });
    }

    window.addEventListener('load', () => { setTimeout(drawPanelCharts, 100); });
    window.addEventListener('resize', drawPanelCharts);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 4. TAIPY
# ==============================================================================
def build_taipy(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">TAIPY ENTERPRISE SCENARIO ORCHESTRATION</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Active Scenario:</label>
        <select id="tp-scenario" onchange="updateTaipyScenario()" style="background:#070d09; color:#fff; border:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; padding:2px 6px; border-radius:4px;">
          <option value="base">Baseline 2026 Strategy</option>
          <option value="agg" selected>Aggressive Retail Media Acceleration</option>
          <option value="hedge">Downside FX & Demand Protection</option>
        </select>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; flex-direction:column; gap:16px;">
      <!-- Pipeline DAG Execution Status -->
      <div style="background:#0a120d; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:12px;">
        <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--gold-bright); margin-bottom:8px;">taipy.core.Scenario Pipeline Pipeline Status</div>
        <div style="display:flex; align-items:center; gap:16px;">
          <div style="background:#0e2417; border:1px solid #00e676; padding:6px 12px; border-radius:4px; font-family:var(--font-mono); font-size:0.75rem; color:#00e676;">
            Data Sourcing: COMPLETED
          </div>
          <span style="color:var(--text-dim);">→</span>
          <div style="background:#0e2417; border:1px solid #00e676; padding:6px 12px; border-radius:4px; font-family:var(--font-mono); font-size:0.75rem; color:#00e676;">
            Optimization Engine: COMPLETED
          </div>
          <span style="color:var(--text-dim);">→</span>
          <div style="background:#241d0a; border:1px solid #f3cf65; padding:6px 12px; border-radius:4px; font-family:var(--font-mono); font-size:0.75rem; color:#f3cf65;">
            Sensitivity Frontier: EVALUATING
          </div>
        </div>
      </div>

      <!-- KPI Diff Matrix -->
      <div style="background:#0a120d; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:12px; flex:1;">
        <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--cyan-neon); margin-bottom:10px;">Enterprise KPI Comparison Diff vs Baseline</div>
        <table style="width:100%; font-family:var(--font-mono); font-size:0.8rem; border-collapse:collapse; color:#cbd5e1;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.1); color:var(--text-muted); text-align:left;">
              <th style="padding:6px;">Metric</th>
              <th style="padding:6px;">Baseline</th>
              <th style="padding:6px;">Current Scenario</th>
              <th style="padding:6px;">Net Delta</th>
            </tr>
          </thead>
          <tbody id="tp-kpi-rows">
            <!-- Populated by JS -->
          </tbody>
        </table>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>scenario = tp.create_scenario(scenario_cfg); tp.submit(scenario); Gui(page).run()</span>
      <span>Enterprise Multi-Scenario Decision Governance & DAG Data Pipelines</span>
    </div>
    """

    custom_js = """
    function updateTaipyScenario() {
      const scen = document.getElementById('tp-scenario').value;
      const data = {
        base: [
          { m: 'Net Revenue Attributed', base: '$12.4M', cur: '$12.4M', delta: '$0.0M (0.0%)' },
          { m: 'Channel Commission Savings', base: '$1.85M', cur: '$1.85M', delta: '$0.0M (0.0%)' },
          { m: 'EBITDA Contribution', base: '$3.20M', cur: '$3.20M', delta: '$0.0M (0.0%)' }
        ],
        agg: [
          { m: 'Net Revenue Attributed', base: '$12.4M', cur: '$15.8M', delta: '+$3.4M (+27.4%)' },
          { m: 'Channel Commission Savings', base: '$1.85M', cur: '$2.65M', delta: '+$0.80M (+43.2%)' },
          { m: 'EBITDA Contribution', base: '$3.20M', cur: '$4.15M', delta: '+$0.95M (+29.7%)' }
        ],
        hedge: [
          { m: 'Net Revenue Attributed', base: '$12.4M', cur: '$11.6M', delta: '-$0.8M (-6.4%)' },
          { m: 'Channel Commission Savings', base: '$1.85M', cur: '$2.10M', delta: '+$0.25M (+13.5%)' },
          { m: 'EBITDA Contribution', base: '$3.20M', cur: '$3.45M', delta: '+$0.25M (+7.8%)' }
        ]
      }[scen];

      const tbody = document.getElementById('tp-kpi-rows');
      tbody.innerHTML = data.map(row => `
        <tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
          <td style="padding:8px 6px;">${row.m}</td>
          <td style="padding:8px 6px; color:#94a3b8;">${row.base}</td>
          <td style="padding:8px 6px; color:#f3cf65; font-weight:600;">${row.cur}</td>
          <td style="padding:8px 6px; color:#00e676;">${row.delta}</td>
        </tr>
      `).join('');
    }

    window.addEventListener('load', () => { updateTaipyScenario(); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 5. REFLEX
# ==============================================================================
def build_reflex(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">REFLEX PURE PYTHON FULL-STACK REACT COMPILER</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">Next.js Virtual DOM + FastAPI</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#070b09; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px;">
      <div style="background:#0e1712; border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:24px; max-width:480px; width:100%; text-align:center;">
        <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--gold-bright); margin-bottom:8px;">class State(rx.State): count: int = 0</div>
        <div style="font-size:3.5rem; font-family:'Newsreader', serif; font-weight:700; color:#fff; margin:12px 0;" id="rx-counter">0</div>
        <div style="display:flex; justify-content:center; gap:12px;">
          <button class="btn-action" onclick="reflexDecrement()" style="font-size:1.1rem; padding:8px 18px;">- Dec</button>
          <button class="btn-action" onclick="reflexIncrement()" style="font-size:1.1rem; padding:8px 18px; background:rgba(0,230,118,0.2); border-color:#00e676; color:#00e676;">+ Inc</button>
        </div>
      </div>

      <!-- Live WebSocket Event Stream -->
      <div style="background:#050806; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:10px; max-width:480px; width:100%; font-family:var(--font-mono); font-size:0.72rem; color:#94a3b8; height:120px; overflow-y:auto;" id="rx-event-log">
        <div>[WebSocket Connected: ws://localhost:8000/event]</div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>app = rx.App(); app.add_page(index); app.compile()</span>
      <span>Pure Python Full-Stack Framework Compiling to Next.js + Tailwind CSS</span>
    </div>
    """

    custom_js = """
    let rxCount = 0;
    function logRxEvent(action) {
      const log = document.getElementById('rx-event-log');
      const time = new Date().toISOString().substring(11, 19);
      log.innerHTML += `<div>[${time}] Event Dispatched: State.${action}() → count=${rxCount}</div>`;
      log.scrollTop = log.scrollHeight;
    }

    function reflexIncrement() {
      rxCount++;
      document.getElementById('rx-counter').innerText = rxCount;
      logRxEvent('increment');
    }

    function reflexDecrement() {
      rxCount--;
      document.getElementById('rx-counter').innerText = rxCount;
      logRxEvent('decrement');
    }
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 6. GLEAM
# ==============================================================================
def build_gleam(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">GLEAM DECLARATIVE WEB APP (SHINY IN PYTHON)</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="runGleamSim()" style="font-size:0.7rem; padding:3px 8px;">Run Simulation</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; flex-direction:column; gap:12px;">
      <div style="display:grid; grid-template-columns: 240px 1fr; gap:16px; flex:1;">
        <!-- Form inputs -->
        <div style="background:#0a120d; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:14px; display:flex; flex-direction:column; gap:12px;">
          <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--gold-bright);">gleam.inputs Panel</div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block; margin-bottom:4px;">Drift Rate μ</label>
            <input type="range" id="gm-mu" min="-0.2" max="0.5" step="0.05" value="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block; margin-bottom:4px;">Volatility σ</label>
            <input type="range" id="gm-sigma" min="0.05" max="0.5" step="0.05" value="0.2" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8; display:block; margin-bottom:4px;">Path Trajectories</label>
            <select id="gm-paths" style="width:100%; background:#040705; color:#fff; border:1px solid rgba(255,255,255,0.15); font-size:0.75rem; padding:4px;">
              <option value="10">10 Paths</option>
              <option value="25" selected>25 Paths</option>
              <option value="50">50 Paths</option>
            </select>
          </div>
        </div>

        <!-- Output plot -->
        <div style="background:#0a120d; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:10px; display:flex; flex-direction:column;">
          <div style="font-family:var(--font-mono); font-size:0.7rem; color:var(--cyan-neon); margin-bottom:6px;">Geometric Brownian Motion Monte Carlo Output</div>
          <canvas id="gm-canvas" style="width:100%; flex:1; min-height:260px;"></canvas>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>app = gleam.Page(title='GBM Simulator', inputs=[Slider('mu'), Slider('sigma')], output=Plot(sim))</span>
      <span>Declarative Shiny-Style Interface · WSGI Native Web Application</span>
    </div>
    """

    custom_js = """
    function runGleamSim() {
      const c = document.getElementById('gm-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#0a120d';
      ctx.fillRect(0, 0, W, H);

      const mu = parseFloat(document.getElementById('gm-mu').value);
      const sigma = parseFloat(document.getElementById('gm-sigma').value);
      const nPaths = parseInt(document.getElementById('gm-paths').value);
      const nSteps = 80;

      // Draw Monte Carlo Paths
      for (let p = 0; p < nPaths; p++) {
        let price = 100;
        ctx.strokeStyle = `hsla(${(p * 360 / nPaths)}, 80%, 60%, 0.6)`;
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        for (let s = 0; s <= nSteps; s++) {
          const x = (s / nSteps) * W;
          const y = H * 0.7 - ((price - 50) / 150) * (H * 0.6);
          if (s === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);

          const dt = 1 / 252;
          const z = (Math.random() + Math.random() + Math.random() - 1.5) * 2;
          price = price * Math.exp((mu - 0.5 * sigma * sigma) * dt + sigma * Math.sqrt(dt) * z);
        }
        ctx.stroke();
      }
    }

    window.addEventListener('load', () => { setTimeout(runGleamSim, 100); });
    window.addEventListener('resize', runGleamSim);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 7. ANVIL
# ==============================================================================
def build_anvil(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">ANVIL FULL-STACK PURE PYTHON PLATFORM</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="anvilRpcCall()" style="font-size:0.7rem; padding:3px 8px;">Call Server RPC</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; flex-direction:column; gap:16px;">
      <div style="background:#0a120d; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:14px;">
        <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--gold-bright); margin-bottom:8px;">anvil.tables.app_tables.transactions.search()</div>
        <table style="width:100%; font-family:var(--font-mono); font-size:0.78rem; border-collapse:collapse; color:#cbd5e1;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.1); color:var(--text-muted); text-align:left;">
              <th style="padding:6px;">Tx ID</th>
              <th style="padding:6px;">Timestamp</th>
              <th style="padding:6px;">Property Asset</th>
              <th style="padding:6px;">Amount</th>
              <th style="padding:6px;">Channel</th>
            </tr>
          </thead>
          <tbody id="anvil-table-body">
            <!-- Populated by JS -->
          </tbody>
        </table>
      </div>

      <div style="background:#030504; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:10px; font-family:var(--font-mono); font-size:0.72rem; color:#94a3b8;">
        <span style="color:#00e676;">[Server Uplink Live]</span> Connected to Anvil Enterprise Private Uplink (AES-256 RPC)
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>@anvil.server.callable def get_data(): return app_tables.users.search()</span>
      <span>Full-Stack Drag-and-Drop Python with Built-in PostgreSQL Database</span>
    </div>
    """

    custom_js = """
    const anvilData = [
      { id: 'TX-9021', time: '2026-09-17 02:40', prop: 'Fraser Suites Sydney', amt: '$4,280', ch: 'Direct App' },
      { id: 'TX-9022', time: '2026-09-17 02:45', prop: 'Capri by Fraser Changi', amt: '$1,950', ch: 'Direct Web' },
      { id: 'TX-9023', time: '2026-09-17 02:51', prop: 'Fraser Residence Seoul', amt: '$3,400', ch: 'Corporate Portal' }
    ];

    function anvilRpcCall() {
      const newId = 'TX-' + Math.floor(9024 + Math.random() * 100);
      anvilData.unshift({
        id: newId,
        time: new Date().toISOString().substring(0, 16).replace('T', ' '),
        prop: 'Fraser Place Canary Wharf',
        amt: '$' + Math.floor(2000 + Math.random() * 3000),
        ch: 'Direct Web'
      });
      if (anvilData.length > 5) anvilData.pop();
      renderAnvil();
    }

    function renderAnvil() {
      const tb = document.getElementById('anvil-table-body');
      tb.innerHTML = anvilData.map(r => `
        <tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
          <td style="padding:6px; color:#00e5ff;">${r.id}</td>
          <td style="padding:6px; color:#94a3b8;">${r.time}</td>
          <td style="padding:6px; color:#fff;">${r.prop}</td>
          <td style="padding:6px; color:#00e676;">${r.amt}</td>
          <td style="padding:6px; color:#f3cf65;">${r.ch}</td>
        </tr>
      `).join('');
    }

    window.addEventListener('load', () => { renderAnvil(); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 8. SOLARA
# ==============================================================================
def build_solara(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">SOLARA REACT-LIKE PYTHON VIRTUAL DOM</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">Pure Python Hooks: use_state()</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#050806; display:flex; flex-direction:column; gap:16px;">
      <div style="background:#0c1410; border:1px solid rgba(255,255,255,0.08); border-radius:8px; padding:16px;">
        <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--gold-bright); margin-bottom:10px;">@solara.component def CommercialDashboard()</div>

        <!-- Filter Chips -->
        <div style="display:flex; gap:8px; margin-bottom:16px;">
          <button class="btn-action active" onclick="setSolaraFilter('all')" id="btn-sol-all" style="font-size:0.75rem;">All Markets</button>
          <button class="btn-action" onclick="setSolaraFilter('apac')" id="btn-sol-apac" style="font-size:0.75rem;">APAC Only</button>
          <button class="btn-action" onclick="setSolaraFilter('emea')" id="btn-sol-emea" style="font-size:0.75rem;">EMEA Only</button>
        </div>

        <!-- Metric Grid -->
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px;">
          <div style="background:#070b09; border:1px solid rgba(255,255,255,0.06); padding:12px; border-radius:6px;">
            <div style="font-size:0.72rem; color:#94a3b8;">Active Properties</div>
            <div style="font-size:1.5rem; font-weight:700; color:#00e676; margin-top:4px;" id="sol-kpi-props">148 Units</div>
          </div>
          <div style="background:#070b09; border:1px solid rgba(255,255,255,0.06); padding:12px; border-radius:6px;">
            <div style="font-size:0.72rem; color:#94a3b8;">Member Booking Ratio</div>
            <div style="font-size:1.5rem; font-weight:700; color:#f3cf65; margin-top:4px;" id="sol-kpi-mem">74.2%</div>
          </div>
          <div style="background:#070b09; border:1px solid rgba(255,255,255,0.06); padding:12px; border-radius:6px;">
            <div style="font-size:0.72rem; color:#94a3b8;">Attributed ROAS</div>
            <div style="font-size:1.5rem; font-weight:700; color:#00e5ff; margin-top:4px;" id="sol-kpi-roas">5.1x</div>
          </div>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>@solara.component def Page(): count, set_count = solara.use_state(0)</span>
      <span>React-Style Pure Python Virtual DOM Architecture · Fast Hot-Reloading</span>
    </div>
    """

    custom_js = """
    function setSolaraFilter(f) {
      document.querySelectorAll('.btn-action').forEach(b => b.classList.remove('active'));
      const btn = document.getElementById(`btn-sol-${f}`);
      if (btn) btn.classList.add('active');

      if (f === 'apac') {
        document.getElementById('sol-kpi-props').innerText = '92 Units';
        document.getElementById('sol-kpi-mem').innerText = '78.5%';
        document.getElementById('sol-kpi-roas').innerText = '5.4x';
      } else if (f === 'emea') {
        document.getElementById('sol-kpi-props').innerText = '56 Units';
        document.getElementById('sol-kpi-mem').innerText = '67.1%';
        document.getElementById('sol-kpi-roas').innerText = '4.6x';
      } else {
        document.getElementById('sol-kpi-props').innerText = '148 Units';
        document.getElementById('sol-kpi-mem').innerText = '74.2%';
        document.getElementById('sol-kpi-roas').innerText = '5.1x';
      }
    }
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)
