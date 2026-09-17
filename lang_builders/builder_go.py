"""
Builder for Go Visualization Libraries:
go-echarts, gonum/plot, Ebitengine, gio, svgo, chart, go-graphviz, fyne
"""
import os
from .common_frame import render_lang_page

BASE_DIR = "/run/media/ml/Storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/Go Visualization"

def write_tool(folder_name, html):
    target_dir = os.path.join(BASE_DIR, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    clean_name = folder_name.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [✓] Go :: {folder_name:<30} -> Studio Built ({len(html)/1024:.1f} KB)")

def build_go_all():
    build_go_echarts()
    build_gonum_plot()
    build_ebitengine()
    build_gio()
    build_svgo()
    build_chart()
    build_go_graphviz()
    build_fyne()

# 1. GO-ECHARTS
def build_go_echarts():
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.3/echarts.min.js"></script>'
    paradigms = [{
        "tag": "01 / APACHE ECHARTS IN GO",
        "title": "Interactive Multi-Dimensional Radar & Candlestick Charts",
        "subtitle": "go-echarts serializes Go structs directly into self-contained HTML containing Apache ECharts option trees.",
        "math_desc": "Multi-attribute normalized radar projection: $r_i = \\frac{x_i - \\min_i}{\\max_i - \\min_i}$ across $k$ radial axes.",
        "math_formula": "\\mathbf{p}_i = \\left( r_i R \\cos\\left(\\frac{2\\pi i}{k} - \\frac{\\pi}{2}\\right), r_i R \\sin\\left(\\frac{2\\pi i}{k} - \\frac{\\pi}{2}\\right) \\right)",
        "time_complexity": "O(N) JSON serialization",
        "space_complexity": "O(N) memory chart struct buffer",
        "enterprise_use": "Cloud-native microservice telemetry dashboards, enterprise procurement vendor scorecards.",
        "strengths": "Zero JavaScript required from the Go developer; outputs production-grade interactive HTML files.",
        "tradeoffs": "Relies on client-side Apache ECharts library runtime.",
        "metrics": [
            {"label": "Engine", "val": "Apache ECharts v5", "sub": "Canvas / SVG"},
            {"label": "Syntax", "val": "Fluent Go API", "sub": "Method Chaining"},
            {"label": "Deployment", "val": "Self-Contained HTML", "sub": "Zero-Server"},
            {"label": "License", "val": "MIT", "sub": "Open Source"}
        ],
        "code": """package main

import (
	"os"
	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
)

func main() {
	radar := charts.NewRadar()
	radar.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "Microservice Fleet Health Radar (go-echarts)"}),
		charts.WithInitializationOpts(opts.Initialization{Theme: "dark"}),
	)

	radar.AddSeries("Alpha Cluster", []opts.RadarData{
		{Value: []interface{}{85, 92, 78, 95, 88, 90}, Name: "US-East-1 Prod"},
	})

	f, _ := os.Create("radar_health.html")
	radar.Render(f)
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 8px #00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">GO-ECHARTS ACTIVE RUNTIME</span>
      </div>
    </div>
    <div class="canvas-body" id="echarts-stage" style="width:100%; height:100%; min-height:480px;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>radar := charts.NewRadar(); radar.Render(file)</span>
      <span>Apache ECharts v5 · Standalone Production HTML Generation in Go</span>
    </div>
    """

    custom_js = """
    function initGoEcharts() {
      const el = document.getElementById('echarts-stage');
      if (!el || typeof echarts === 'undefined') return;

      const chart = echarts.init(el, 'dark');
      const option = {
        backgroundColor: '#040705',
        title: { text: 'Microservice Cluster Performance (go-echarts)', textStyle: { color: '#fffefa', fontFamily: 'Newsreader' } },
        tooltip: {},
        radar: {
          indicator: [
            { name: 'Throughput (k rps)', max: 100 },
            { name: 'P99 Latency (ms)', max: 100 },
            { name: 'Memory Footprint', max: 100 },
            { name: 'CPU Utilization', max: 100 },
            { name: 'Availability (%)', max: 100 },
            { name: 'Error Budget', max: 100 }
          ],
          splitArea: { areaStyle: { color: ['#070b09', '#0e1712', '#14221a'] } }
        },
        series: [{
          name: 'Cluster SLA',
          type: 'radar',
          data: [
            { value: [88, 76, 85, 90, 99, 94], name: 'Cluster Alpha (Go Microservices)', itemStyle: { color: '#00e676' } },
            { value: [65, 88, 70, 75, 92, 80], name: 'Legacy Cluster Beta', itemStyle: { color: '#f3cf65' } }
          ]
        }]
      };
      chart.setOption(option);
      window.addEventListener('resize', () => chart.resize());
    }

    window.addEventListener('load', () => { setTimeout(initGoEcharts, 100); });
    """

    html = render_lang_page("Go", "go-echarts", "Go Visualization", 'go get github.com/go-echarts/go-echarts/v2',
                            "https://github.com/go-echarts/go-echarts",
                            "Apache ECharts library wrapper for Go generating standalone interactive HTML files.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("go-echarts", html)

# 2. GONUM/PLOT
def build_gonum_plot():
    paradigms = [{
        "tag": "01 / SCIENTIFIC CONTOUR MAPPING",
        "title": "Mathematical Contour Isolines & Scientific Rastering",
        "subtitle": "gonum/plot provides native Go mathematical plotting with vector output, integrating directly with gonum matrices.",
        "math_desc": "2D Gaussian potential contour surface: $V(x,y) = \\sum_i A_i e^{-\\frac{(x - x_i)^2 + (y - y_i)^2}{2\\sigma_i^2}}$ with marching squares isoline extraction.",
        "math_formula": "C_c = \\left\\{ (x,y) \\mid V(x,y) = c \\right\\}",
        "time_complexity": "O(N^2) marching squares grid traversal",
        "space_complexity": "O(N^2) float64 gonum dense matrix",
        "enterprise_use": "Subsea pipeline cathodic protection potential fields, antenna RF beam pattern contours.",
        "strengths": "Pure Go; zero C/Fortran shared library dependencies; highly reliable mathematical algorithms.",
        "tradeoffs": "Vector output is primarily SVG/PNG/EPS; lacks built-in client web zoom without JS wrapper.",
        "metrics": [
            {"label": "Matrix Engine", "val": "gonum/mat", "sub": "Pure Go BLAS"},
            {"label": "Output", "val": "SVG / PNG", "sub": "Resolution Matched"},
            {"label": "Algorithms", "val": "Marching Squares", "sub": "Isoline Exact"},
            {"label": "License", "val": "BSD 3-Clause", "sub": "Gonum Standard"}
        ],
        "code": """package main

import (
	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
)

func main() {
	p := plot.New()
	p.Title.Text = "Mathematical Potential Contours (gonum/plot)"

	// Render to standalone SVG
	p.Save(8*vg.Inch, 6*vg.Inch, "contours.svg")
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">GONUM/PLOT CONTOUR ENGINE</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="gonum-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>p := plot.New(); p.Save(8*vg.Inch, 6*vg.Inch, 'contours.svg')</span>
      <span>Pure Go Scientific Matrix Linear Algebra · Marching Squares Isoline Contours</span>
    </div>
    """

    custom_js = """
    function drawGonumPlot() {
      const c = document.getElementById('gonum-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const cx = W / 2; const cy = H / 2;
      const colors = ['#0a1d12', '#0e2e1d', '#134028', '#1a5636', '#00e676', '#f3cf65'];

      // Draw concentric Gaussian potential contours
      for (let i = colors.length - 1; i >= 0; i--) {
        const radX = (i + 1) * 32;
        const radY = (i + 1) * 22;

        ctx.fillStyle = colors[i];
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 1.2;

        ctx.beginPath();
        ctx.ellipse(cx - 40, cy, radX, radY, 0.2, 0, 2*Math.PI);
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.ellipse(cx + 60, cy - 20, radX * 0.7, radY * 0.7, -0.4, 0, 2*Math.PI);
        ctx.fill();
        ctx.stroke();
      }
    }

    window.addEventListener('load', () => { drawGonumPlot(); });
    window.addEventListener('resize', drawGonumPlot);
    """

    html = render_lang_page("Go", "gonum/plot", "Go Visualization", 'go get gonum.org/v1/plot/...',
                            "https://www.gonum.org",
                            "Native Go scientific and statistical plotting library with vector targets.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("gonum_plot", html)

# 3. EBITENGINE
def build_ebitengine():
    paradigms = [{
        "tag": "01 / 2D GPU WASM ENGINE",
        "title": "Hardware 2D Particle Simulation in WebAssembly",
        "subtitle": "Ebitengine provides a simple, dead-code-eliminated 2D game and graphics engine in Go that compiles cleanly into WebAssembly.",
        "math_desc": "Eulerian particle momentum update: $\\mathbf{v}_{t+\\Delta t} = \\mathbf{v}_t + \\mathbf{g} \\Delta t, \\; \\mathbf{x}_{t+\\Delta t} = \\mathbf{x}_t + \\mathbf{v}_{t+\\Delta t} \\Delta t$.",
        "math_formula": "\\mathbf{F}_{\\text{drag}} = -\\frac{1}{2} C_d \\rho A \\|\\mathbf{v}\\| \\mathbf{v}",
        "time_complexity": "O(N) hardware GPU textured quad blit",
        "space_complexity": "O(N) struct Particle contiguous slice",
        "enterprise_use": "Real-time automated conveyor logistics visualizer, airport baggage routing animation.",
        "strengths": "Ultra-lightweight Wasm runtime; consistent 60 FPS across desktop and web.",
        "tradeoffs": "Designed for 2D sprites/pixel manipulation rather than declarative scientific charts.",
        "metrics": [
            {"label": "Target", "val": "WebAssembly / WebGL", "sub": "Pure Go"},
            {"label": "Performance", "val": "60 FPS VSync", "sub": "GPU Blit"},
            {"label": "Memory", "val": "< 12 MB Wasm", "sub": "Tiny Binary"},
            {"label": "License", "val": "Apache 2.0", "sub": "Hajime Hoshi"}
        ],
        "code": """package main

import (
	"github.com/hajimehoshi/ebiten/v2"
	"image/color"
)

type Game struct{}

func (g *Game) Update() error { return nil }
func (g *Game) Draw(screen *ebiten.Image) {
	screen.Fill(color.RGBA{4, 7, 5, 255})
}
func (g *Game) Layout(w, h int) (int, int) { return 640, 480 }

func main() {
	ebiten.RunGame(&Game{})
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">EBITENGINE 2D WASM SIMULATOR</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="resetEbiten()" style="font-size:0.7rem; padding:3px 8px;">Emitter Burst</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="ebiten-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>ebiten.RunGame(&Game{}) · Compiles directly to wasm32</span>
      <span>Go Hardware 2D Blitter · WebAssembly Browser Execution</span>
    </div>
    """

    custom_js = """
    const ebParticles = [];
    function initEbiten() {
      ebParticles.length = 0;
      for (let i = 0; i < 280; i++) {
        ebParticles.push({
          x: 320, y: 240,
          vx: (Math.random() - 0.5) * 6,
          vy: (Math.random() - 0.5) * 6,
          col: (i % 2 === 0) ? '#00e5ff' : '#00e676'
        });
      }
    }
    initEbiten();
    function resetEbiten() { initEbiten(); }

    function ebitenLoop() {
      const c = document.getElementById('ebiten-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = 'rgba(4, 7, 5, 0.25)';
      ctx.fillRect(0, 0, W, H);

      ebParticles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 10 || p.x > W - 10) p.vx *= -1;
        if (p.y < 10 || p.y > H - 10) p.vy *= -1;

        ctx.fillStyle = p.col;
        ctx.beginPath(); ctx.arc(p.x, p.y, 3, 0, 2*Math.PI); ctx.fill();
      });

      requestAnimationFrame(ebitenLoop);
    }

    window.addEventListener('load', () => { requestAnimationFrame(ebitenLoop); });
    """

    html = render_lang_page("Go", "Ebitengine", "Go Visualization", 'go get github.com/hajimehoshi/ebiten/v2',
                            "https://ebitengine.org",
                            "Dead-simple 2D graphics and game engine for Go compiling directly to WebAssembly.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Ebitengine", html)

# 4. GIO
def build_gio():
    paradigms = [{
        "tag": "01 / IMMEDIATE-MODE VECTOR UI",
        "title": "Immediate-Mode Portable Vector Graphics in Pure Go",
        "subtitle": "Gio is an immediate-mode GUI and vector graphics library in pure Go running across Linux, macOS, iOS, Android, and WebAssembly.",
        "math_desc": "Vector path winding fill rule: non-zero winding number evaluation along cubic Bezier control points.",
        "math_formula": "\\mathbf{B}(t) = (1-t)^3 \\mathbf{P}_0 + 3(1-t)^2 t \\mathbf{P}_1 + 3(1-t) t^2 \\mathbf{P}_2 + t^3 \\mathbf{P}_3",
        "time_complexity": "O(V) vector path GPU tessellation",
        "space_complexity": "O(1) retained memory (immediate mode)",
        "enterprise_use": "Cross-platform industrial edge control terminals, air-gapped hardware telemetry displays.",
        "strengths": "Runs on every operating system + WebAssembly with zero CGO dependencies.",
        "tradeoffs": "Requires understanding immediate-mode layout semantics.",
        "metrics": [
            {"label": "Platform", "val": "All OS + Wasm", "sub": "Pure Go"},
            {"label": "Rendering", "val": "Hardware GPU", "sub": "Shader Tessellated"},
            {"label": "Dependencies", "val": "Zero CGO", "sub": "Pure Go Binary"},
            {"label": "License", "val": "MIT / UNLICENSE", "sub": "Elias Naur"}
        ],
        "code": """package main

import (
	"gioui.org/app"
	"gioui.org/layout"
	"gioui.org/widget/material"
)

func main() {
	go func() {
		w := new(app.Window)
		th := material.NewTheme()
		for e := range w.Events() {
			if e, ok := e.(app.FrameEvent); ok {
				gtx := app.NewContext(&layout.Context{}, e)
				layout.Center.Layout(gtx, func(gtx layout.Context) layout.Dimensions {
					return material.H4(th, "Gio: Pure Go Immediate Vector UI").Layout(gtx)
				})
				e.Frame(gtx.Ops)
			}
		}
	}()
	app.Main()
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">GIO VECTOR UI RUNTIME</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#070b09; display:flex; align-items:center; justify-content:center;">
      <div style="width:420px; background:#0e1712; border:1px solid rgba(255,255,255,0.12); border-radius:8px; padding:20px; box-shadow:0 10px 25px rgba(0,0,0,0.7);">
        <h4 style="font-family:'Newsreader', serif; font-size:1.3rem; color:#fff; margin-bottom:8px;">Gio Pure Go Material Card</h4>
        <p style="font-size:0.8rem; color:#94a3b8; line-height:1.4; margin-bottom:14px;">Immediate-mode vector rendering with zero CGO dependencies across all target platforms.</p>
        <button class="btn-action" style="background:#00e676; color:#040705; font-weight:700; width:100%; justify-content:center; padding:8px;">
          ⚡ material.Button(th, "Dispatch Transaction")
        </button>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>material.H4(th, 'Gio: Pure Go Vector UI').Layout(gtx)</span>
      <span>Zero CGO Immediate-Mode Vector Architecture · Wasm & Native Target</span>
    </div>
    """

    custom_js = ""

    html = render_lang_page("Go", "gio", "Go Visualization", 'go get gioui.org/...',
                            "https://gioui.org",
                            "Immediate-mode portable vector UI and graphics library in pure Go.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("gio", html)

# 5. SVGO
def build_svgo():
    paradigms = [{
        "tag": "01 / PURE GO SVG GENERATOR",
        "title": "Scalable Vector Graphics Generation & Technical Schematics",
        "subtitle": "svgo provides a clean, stream-oriented pure Go API to generate standard W3C SVG vector diagrams, engineering blueprints, and visual architectures.",
        "math_desc": "Linear Bézier curves and affine transformation matrix concatenation directly serializing XML elements.",
        "math_formula": "\\text{Transform}(x,y) = \\begin{pmatrix} a & c & e \\\\ b & d & f \\\\ 0 & 0 & 1 \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\\\ 1 \\end{pmatrix}",
        "time_complexity": "O(N) direct streaming I/O writer",
        "space_complexity": "O(1) buffer allocation",
        "enterprise_use": "Automated network rack architecture diagrams, electrical schematic blueprints.",
        "strengths": "Ultra-fast streaming; zero external dependencies; clean Go idiomatic API.",
        "tradeoffs": "Static SVG only; interactivity must be added via embedded CSS/JS.",
        "metrics": [
            {"label": "Standard", "val": "W3C SVG 1.1", "sub": "XML Streaming"},
            {"label": "Engine", "val": "io.Writer", "sub": "Zero-Alloc Stream"},
            {"label": "Weight", "val": "Minimalist", "sub": "Zero Dependency"},
            {"label": "License", "val": "MIT", "sub": "Anthony Starks"}
        ],
        "code": """package main

import (
	"os"
	"github.com/ajstarks/svgo"
)

func main() {
	f, _ := os.Create("network.svg")
	canvas := svg.New(f)
	canvas.Start(640, 480)
	canvas.Rect(0, 0, 640, 480, "fill:#040705")
	canvas.Circle(320, 240, 80, "fill:#00e676;opacity:0.6")
	canvas.Text(320, 245, "Core Switch", "text-anchor:middle;font-size:14px;fill:#ffffff")
	canvas.End()
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">SVGO STREAMING SVG ENGINE</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <svg viewBox="0 0 640 440" style="width:100%; max-width:640px; height:auto;">
        <rect x="0" y="0" width="640" height="440" fill="#040705"/>
        <line x1="80" y1="220" x2="320" y2="220" stroke="#334155" stroke-width="2"/>
        <line x1="320" y1="220" x2="560" y2="140" stroke="#334155" stroke-width="2"/>
        <line x1="320" y1="220" x2="560" y2="300" stroke="#334155" stroke-width="2"/>
        <circle cx="80" cy="220" r="35" fill="#f3cf65" opacity="0.85"/>
        <text x="80" y="225" fill="#040705" font-family="JetBrains Mono" font-size="11" font-weight="700" text-anchor="middle">Ingress</text>
        <circle cx="320" cy="220" r="45" fill="#00e676" opacity="0.85"/>
        <text x="320" y="225" fill="#040705" font-family="JetBrains Mono" font-size="12" font-weight="700" text-anchor="middle">Core Mesh</text>
        <circle cx="560" cy="140" r="30" fill="#00e5ff" opacity="0.85"/>
        <text x="560" y="145" fill="#040705" font-family="JetBrains Mono" font-size="10" font-weight="700" text-anchor="middle">Pod A</text>
        <circle cx="560" cy="300" r="30" fill="#00e5ff" opacity="0.85"/>
        <text x="560" y="305" fill="#040705" font-family="JetBrains Mono" font-size="10" font-weight="700" text-anchor="middle">Pod B</text>
      </svg>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>canvas := svg.New(f); canvas.Circle(320, 240, 80, 'fill:#00e676')</span>
      <span>Pure Go XML Stream Generation · Zero External C/CGO Linkage</span>
    </div>
    """

    custom_js = ""

    html = render_lang_page("Go", "svgo", "Go Visualization", 'go get github.com/ajstarks/svgo',
                            "https://github.com/ajstarks/svgo",
                            "Pure Go library for streaming W3C Scalable Vector Graphics.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("svgo", html)

# 6. CHART
def build_chart():
    paradigms = [{
        "tag": "01 / NATIVE GO CHARTING",
        "title": "Continuous Time-Series & Dual-Axis Moving Averages",
        "subtitle": "wcharczuk/go-chart is a pure Go chart drawing library providing multi-axis continuous time series and regression curves.",
        "math_desc": "Simple Moving Average: $\\text{SMA}_k(t) = \\frac{1}{k} \\sum_{i=0}^{k-1} P_{t-i}$ overlaid with Bollinger Band volatility envelopes.",
        "math_formula": "\\text{Upper} = \\text{SMA}_k + 2 \\sigma_k, \\quad \\text{Lower} = \\text{SMA}_k - 2 \\sigma_k",
        "time_complexity": "O(N) single-pass moving window accumulation",
        "space_complexity": "O(N) time series slice buffer",
        "enterprise_use": "Automated daily financial ledger balance charts, microservice SLA violation trends.",
        "strengths": "Pure Go; produces clean SVG and PNG; supports secondary Y-axes.",
        "tradeoffs": "Maintenance has slowed in recent years compared to go-echarts.",
        "metrics": [
            {"label": "Language", "val": "Pure Go", "sub": "Zero CGO"},
            {"label": "Axes", "val": "Dual Y-Axis", "sub": "Price & Volume"},
            {"label": "Output", "val": "SVG / PNG", "sub": "Vector Capable"},
            {"label": "License", "val": "MIT", "sub": "Open Standard"}
        ],
        "code": """package main

import (
	"os"
	"github.com/wcharczuk/go-chart/v2"
)

func main() {
	graph := chart.Chart{
		Series: []chart.Series{
			chart.ContinuousSeries{
				XValues: []float64{1.0, 2.0, 3.0, 4.0, 5.0},
				YValues: []float64{100.0, 110.0, 105.0, 125.0, 140.0},
			},
		},
	}
	f, _ := os.Create("chart.png")
	graph.Render(chart.PNG, f)
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">GO-CHART DUAL-AXIS PIPELINE</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="gochart-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>graph.Render(chart.PNG, f) · ContinuousSeries with Secondary Y-Axis</span>
      <span>Pure Go Vector Canvas Rendering · Zero Native System Dependencies</span>
    </div>
    """

    custom_js = """
    function drawGoChart() {
      const c = document.getElementById('gochart-canvas');
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
      for (let y = 0; y < H; y += 40) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      // Time series line
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.beginPath();
      const n = 120;
      let price = 100;
      for (let i = 0; i < n; i++) {
        price += (Math.random() - 0.48) * 4;
        const x = (i / n) * W;
        const y = H * 0.7 - ((price - 80) / 60) * (H * 0.5);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }

    window.addEventListener('load', () => { drawGoChart(); });
    window.addEventListener('resize', drawGoChart);
    """

    html = render_lang_page("Go", "chart", "Go Visualization", 'go get github.com/wcharczuk/go-chart/v2',
                            "https://github.com/wcharczuk/go-chart",
                            "Pure Go charting library for continuous timeseries and secondary axes.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("chart", html)

# 7. GO-GRAPHVIZ
def build_go_graphviz():
    paradigms = [{
        "tag": "01 / HIERARCHICAL AST COMPILER",
        "title": "Automated AST & DAG Pipeline Generation in Go",
        "subtitle": "goccy/go-graphviz embeds Graphviz C core directly into Go using WebAssembly or CGO for programmatic DAG synthesis.",
        "math_desc": "Sugiyama layered DAG ranking algorithm minimizing edge crossings through vertex ordering permutation passes.",
        "math_formula": "\\min_{\\pi} \\sum_{(u,v) \\in E} \\sum_{(x,y) \\in E} \\text{Cross}(\\pi(u), \\pi(v), \\pi(x), \\pi(y))",
        "time_complexity": "O(V \\cdot E) layered DAG layout heuristic",
        "space_complexity": "O(V + E) DOT graph scenegraph",
        "enterprise_use": "Go compiler AST syntax trees, Kubernetes operator reconcile dependency graphs.",
        "strengths": "Fastest hierarchical layout engine; direct Go struct binding.",
        "tradeoffs": "Requires CGO unless using pure Wasm graphviz port.",
        "metrics": [
            {"label": "Layout", "val": "Sugiyama DAG", "sub": "Hierarchical"},
            {"label": "Bindings", "val": "libgvc CGO/Wasm", "sub": "High Speed"},
            {"label": "Output", "val": "SVG / PNG / DOT", "sub": "W3C Compliant"},
            {"label": "License", "val": "MIT", "sub": "goccy"}
        ],
        "code": """package main

import (
	"bytes"
	"github.com/goccy/go-graphviz"
)

func main() {
	g := graphviz.New()
	graph, _ := g.Graph()
	defer graph.Close()

	n1, _ := graph.CreateNode("AST_Parser")
	n2, _ := graph.CreateNode("Type_Checker")
	graph.CreateEdge("parse_to_check", n1, n2)

	var buf bytes.Buffer
	g.Render(graph, graphviz.SVG, &buf)
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">GO-GRAPHVIZ AST SYNTHESIZER</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="gviz-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>g := graphviz.New(); graph.CreateEdge('ast', n1, n2); g.Render(SVG)</span>
      <span>Hierarchical Sugiyama Edge-Crossing Optimization · Go AST Visualization</span>
    </div>
    """

    custom_js = """
    function drawGoGraphviz() {
      const c = document.getElementById('gviz-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const nodes = [
        { id: 'parse', label: 'Go AST Lexer', x: 100, y: H/2 },
        { id: 'type', label: 'Type Checker', x: 260, y: H/2 - 60 },
        { id: 'ssa', label: 'SSA Optimization', x: 260, y: H/2 + 60 },
        { id: 'gen', label: 'Machine Code Gen', x: 440, y: H/2 }
      ];

      // Edges
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(100, H/2); ctx.lineTo(260, H/2 - 60);
      ctx.moveTo(100, H/2); ctx.lineTo(260, H/2 + 60);
      ctx.moveTo(260, H/2 - 60); ctx.lineTo(440, H/2);
      ctx.moveTo(260, H/2 + 60); ctx.lineTo(440, H/2);
      ctx.stroke();

      // Nodes
      nodes.forEach(n => {
        ctx.fillStyle = '#0e1712';
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 1.8;
        ctx.strokeRect(n.x - 55, n.y - 20, 110, 40);
        ctx.fillRect(n.x - 55, n.y - 20, 110, 40);

        ctx.fillStyle = '#fff';
        ctx.font = '10px JetBrains Mono';
        ctx.textAlign = 'center';
        ctx.fillText(n.label, n.x, n.y + 4);
      });
    }

    window.addEventListener('load', () => { drawGoGraphviz(); });
    window.addEventListener('resize', drawGoGraphviz);
    """

    html = render_lang_page("Go", "go-graphviz", "Go Visualization", 'go get github.com/goccy/go-graphviz',
                            "https://github.com/goccy/go-graphviz",
                            "Go interface to Graphviz for automated compiler AST and DAG generation.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("go-graphviz", html)

# 8. FYNE
def build_fyne():
    paradigms = [{
        "tag": "01 / CROSS-PLATFORM GO GUI",
        "title": "Declarative Cross-Platform Material Desktop & Wasm GUI",
        "subtitle": "Fyne provides a clean declarative UI toolkit written in pure Go that renders via OpenGL or compiles to WebAssembly with high DPI support.",
        "math_desc": "Resolution-independent vector canvas coordinates mapped to physical display pixel scale factor $S = \\text{DPI} / 96.0$.",
        "math_formula": "P_{\\text{pixel}} = \\text{Round}(P_{\\text{logical}} \\times S)",
        "time_complexity": "O(W) widget canvas tree traversal",
        "space_complexity": "O(W) retained widget tree",
        "enterprise_use": "On-premise edge computing appliance manager, secure cryptographic hardware key signer.",
        "strengths": "Looks clean across Windows, macOS, Linux, and WebAssembly; simple layout containers.",
        "tradeoffs": "Material theme is opinionated; custom look-and-feel requires overriding theme methods.",
        "metrics": [
            {"label": "Driver", "val": "OpenGL / WebGL", "sub": "Hardware Render"},
            {"label": "DPI Scaling", "val": "Vector Scaled", "sub": "Auto-Detect"},
            {"label": "Packaging", "val": "Single Binary", "sub": "Self-Contained"},
            {"label": "License", "val": "BSD 3-Clause", "sub": "Fyne.io"}
        ],
        "code": """package main

import (
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func main() {
	myApp := app.New()
	myWindow := myApp.NewWindow("Fyne: Go Desktop & Wasm")

	content := container.NewVBox(
		widget.NewLabel("Commercial Performance Hub"),
		widget.NewProgressBarInfinite(),
		widget.NewButton("Recalibrate Model", func() {}),
	)

	myWindow.SetContent(content)
	myWindow.ShowAndRun()
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">FYNE DECLARATIVE RUNTIME</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#070b09; display:flex; align-items:center; justify-content:center;">
      <div style="width:440px; background:#141b17; border:1px solid rgba(255,255,255,0.12); border-radius:6px; overflow:hidden; box-shadow:0 12px 30px rgba(0,0,0,0.8);">
        <div style="background:#1e2923; padding:8px 12px; font-family:var(--font-mono); font-size:0.75rem; color:#00e676;">
          Fyne Window: Commercial Operations Manager
        </div>
        <div style="padding:16px; display:flex; flex-direction:column; gap:12px;">
          <div style="font-size:0.85rem; color:#fff; font-weight:600;">System Fleet Status: OPERATIONAL</div>
          <div style="height:8px; background:#070b09; border-radius:4px; overflow:hidden;">
            <div style="width:78%; height:100%; background:#00e676;"></div>
          </div>
          <button class="btn-action" style="background:#00e676; color:#040705; font-weight:700; width:100%; justify-content:center; padding:8px;">
            widget.NewButton("Sync Edge Clusters")
          </button>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>container.NewVBox(widget.NewLabel(), widget.NewButton())</span>
      <span>Declarative Go GUI Layout · Resolution-Independent Vector OpenGL</span>
    </div>
    """

    custom_js = ""

    html = render_lang_page("Go", "fyne", "Go Visualization", 'go get fyne.io/fyne/v2',
                            "https://fyne.io",
                            "Cross-platform declarative GUI toolkit written in pure Go for desktop and web.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("fyne", html)

if __name__ == "__main__":
    build_go_all()
