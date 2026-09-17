"""
Builder for Julia Visualization Libraries:
Makie (WGLMakie), Plots.jl, Pluto.jl, Gadfly.jl, StatsPlots.jl, GraphRecipes.jl, GeoMakie.jl, Genie.jl
"""
import os
from .common_frame import render_lang_page

BASE_DIR = "/run/media/ml/Storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/Julia Visualization"

def write_tool(folder_name, html):
    target_dir = os.path.join(BASE_DIR, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    clean_name = folder_name.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [✓] Julia :: {folder_name:<30} -> Studio Built ({len(html)/1024:.1f} KB)")

def build_julia_all():
    build_makie()
    build_plots_jl()
    build_pluto()
    build_gadfly()
    build_statsplots()
    build_graphrecipes()
    build_geomakie()
    build_genie()

# 1. MAKIE
def build_makie():
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    paradigms = [{
        "tag": "01 / GPU SCIENTIFIC SHADERS",
        "title": "3D Lorenz Attractor & WGLMakie WebGL Shader Pipeline",
        "subtitle": "Makie compiles scientific scenes directly into hardware OpenGL / WebGL / Cairo buffers with native GPU shaders and camera orbit.",
        "math_desc": "Lorenz strange attractor dynamical system: $\\dot{x} = \\sigma(y - x), \\; \\dot{y} = x(\\rho - z) - y, \\; \\dot{z} = xy - \\beta z$ with Runge-Kutta 4th-order integration.",
        "math_formula": "\\mathbf{x}_{n+1} = \\mathbf{x}_n + \\frac{\\Delta t}{6} (k_1 + 2k_2 + 2k_3 + k_4)",
        "time_complexity": "O(N) hardware GPU line strip streaming",
        "space_complexity": "O(N) Float32 point array in VRAM",
        "enterprise_use": "Atmospheric climate convection turbulence, turbomachinery blade boundary layer vortex modeling.",
        "strengths": "C-speed execution in high-level Julia; unified backend (GLMakie desktop, WGLMakie web, CairoMakie vector PDF).",
        "tradeoffs": "Initial time-to-first-plot (TTFP) latency during Julia JIT compilation.",
        "metrics": [
            {"label": "Backends", "val": "WGL / GL / Cairo", "sub": "Unified Scenegraph"},
            {"label": "Throughput", "val": "1M+ Points (60 FPS)", "sub": "Native Julia GPU"},
            {"label": "Precision", "val": "Float64 Native", "sub": "Zero Downsampling"},
            {"label": "License", "val": "MIT", "sub": "NumFOCUS Backed"}
        ],
        "code": """using WGLMakie
using DifferentialEquations

# Lorenz attractor differential equations in Julia
function lorenz!(du, u, p, t)
    σ, ρ, β = p
    du[1] = σ * (u[2] - u[1])
    du[2] = u[1] * (ρ - u[3]) - u[2]
    du[3] = u[1] * u[2] - β * u[3]
end

u0 = [1.0, 0.0, 0.0]
tspan = (0.0, 60.0)
p = [10.0, 28.0, 8/3]
prob = ODEProblem(lorenz!, u0, tspan, p)
sol = solve(prob, Tsit5(), saveat = 0.02)

fig = Figure(backgroundcolor = :black, resolution = (1200, 800))
ax = Axis3(fig[1, 1], title = "Makie.jl: Lorenz Dynamical Strange Attractor",
           backgroundcolor = "#040705")

lines!(ax, sol[1, :], sol[2, :], sol[3, :],
       color = sol.t, colormap = :plasma, linewidth = 2.0)

# Export interactive WebGL HTML
WGLMakie.page(fig, "lorenz_makie.html")"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676; box-shadow:0 0 8px #00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">WGLMAKIE THREE.JS WEBGL PIPELINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Rho ρ:</label>
        <input type="range" id="mk-rho" min="10" max="40" step="1" value="28" oninput="updateMakieRho()" style="width:70px;">
        <button class="btn-action" onclick="toggleMakieSpin()" id="btn-mk-spin" style="font-size:0.7rem; padding:3px 8px;">Pause Orbit</button>
      </div>
    </div>
    <div class="canvas-body" id="makie-stage" style="width:100%; height:100%; min-height:480px; position:relative;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>lines!(ax, sol[1,:], sol[2,:], sol[3,:], colormap=:plasma)</span>
      <span>Julia JIT Scientific Runtime · WebGL Hardware Ray-Traced 3D Trajectory</span>
    </div>
    """

    custom_js = """
    let mkScene, mkCamera, mkRenderer, mkLineGroup;
    let mkSpin = true;

    function initMakieThree() {
      const container = document.getElementById('makie-stage');
      if (!container) return;

      mkScene = new THREE.Scene();
      mkScene.background = new THREE.Color(0x040705);

      mkCamera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      mkCamera.position.set(0, 20, 80);
      mkCamera.lookAt(0, 0, 25);

      mkRenderer = new THREE.WebGLRenderer({ antialias: true });
      mkRenderer.setSize(container.clientWidth, container.clientHeight);
      mkRenderer.setPixelRatio(window.devicePixelRatio);
      container.appendChild(mkRenderer.domElement);

      mkLineGroup = new THREE.Group();
      mkScene.add(mkLineGroup);

      generateLorenzCurve(28.0);

      // Drag Orbit
      let isDragging = false;
      let prevM = { x: 0, y: 0 };
      container.addEventListener('mousedown', (e) => { isDragging = true; prevM = { x: e.clientX, y: e.clientY }; });
      window.addEventListener('mouseup', () => { isDragging = false; });
      container.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const dx = e.clientX - prevM.x;
        const dy = e.clientY - prevM.y;
        mkLineGroup.rotation.y += dx * 0.01;
        mkLineGroup.rotation.x += dy * 0.01;
        prevM = { x: e.clientX, y: e.clientY };
      });

      function animate() {
        requestAnimationFrame(animate);
        if (mkSpin && !isDragging) {
          mkLineGroup.rotation.y += 0.005;
        }
        mkRenderer.render(mkScene, mkCamera);
      }
      animate();

      window.addEventListener('resize', () => {
        if (!container) return;
        mkCamera.aspect = container.clientWidth / container.clientHeight;
        mkCamera.updateProjectionMatrix();
        mkRenderer.setSize(container.clientWidth, container.clientHeight);
      });
    }

    function generateLorenzCurve(rho) {
      while (mkLineGroup.children.length > 0) {
        mkLineGroup.remove(mkLineGroup.children[0]);
      }

      let x = 0.1; let y = 0.0; let z = 0.0;
      const sigma = 10.0; const beta = 8.0 / 3.0; const dt = 0.01;
      const n = 2400;

      const positions = [];
      const colors = [];

      for (let i = 0; i < n; i++) {
        const dx = sigma * (y - x);
        const dy = x * (rho - z) - y;
        const dz = x * y - beta * z;

        x += dx * dt;
        y += dy * dt;
        z += dz * dt;

        positions.push(x, y, z);
        const c = new THREE.Color().setHSL(0.55 + (i / n) * 0.45, 1.0, 0.5);
        colors.push(c.r, c.g, c.b);
      }

      const geom = new THREE.BufferGeometry();
      geom.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
      geom.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));

      const mat = new THREE.LineBasicMaterial({ vertexColors: true, linewidth: 2 });
      const line = new THREE.Line(geom, mat);
      mkLineGroup.add(line);
    }

    function updateMakieRho() {
      const rho = parseFloat(document.getElementById('mk-rho').value);
      generateLorenzCurve(rho);
    }

    function toggleMakieSpin() {
      mkSpin = !mkSpin;
      document.getElementById('btn-mk-spin').innerText = mkSpin ? 'Pause Orbit' : 'Resume Orbit';
    }

    window.addEventListener('load', () => { setTimeout(initMakieThree, 100); });
    """

    html = render_lang_page("Julia", "Makie.jl", "Julia Visualization", 'using Pkg; Pkg.add("WGLMakie")',
                            "https://makie.org",
                            "High-performance GPU-accelerated scientific plotting & WebGL shaders.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Makie", html)

# 2. PLOTS.JL
def build_plots_jl():
    paradigms = [{
        "tag": "01 / UNIFIED METAPACKAGE",
        "title": "Backend-Agnostic Metapackage Architecture",
        "subtitle": "Decouples plotting commands from concrete graphics engines: switch between GR, PlotlyJS, and PyPlot with zero code refactoring.",
        "math_desc": "Parametric Fermat spiral: $r = c \\sqrt{\\theta}, \\; \\theta = n \\cdot 137.508^\\circ$ (golden angle phyllotaxis pattern).",
        "math_formula": "x_n = c \\sqrt{n} \\cos(n \\phi), \\quad y_n = c \\sqrt{n} \\sin(n \\phi), \\quad \\phi = \\pi (3 - \\sqrt{5})",
        "time_complexity": "O(N) backend dispatch",
        "space_complexity": "O(N) series attribute dictionary",
        "enterprise_use": "High-throughput numerical optimization convergence logging, algorithm benchmarking.",
        "strengths": "Single unified API across GR, Plotly, and PGFPlots; rich recipe ecosystem.",
        "tradeoffs": "Package load time can be high on fresh Julia sessions without precompilation (Sysimage).",
        "metrics": [
            {"label": "Backends", "val": "GR / Plotly / PyPlot", "sub": "Runtime Switch"},
            {"label": "Recipes", "val": "Full Julia Types", "sub": "Zero Overhead"},
            {"label": "Dispatch", "val": "Multiple Dispatch", "sub": "Native Julia"},
            {"label": "License", "val": "MIT", "sub": "JuliaLang"}
        ],
        "code": """using Plots
gr() # Switch to high-speed C-engine backend

n = 800
golden_angle = pi * (3 - sqrt(5))
theta = (1:n) .* golden_angle
r = sqrt.(1:n)

x = r .* cos.(theta)
y = r .* sin.(theta)

scatter(x, y,
        zcolor = theta,
        colormap = :viridis,
        markersize = 4,
        markerstrokewidth = 0,
        legend = false,
        background_color = "#040705",
        title = "Phyllotaxis Golden Ratio Fermat Spiral (Plots.jl)")

savefig("phyllotaxis.html")"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">PLOTS.JL DISPATCH SIMULATION</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Points:</label>
        <input type="range" id="pl-pts" min="200" max="1200" step="50" value="650" oninput="drawPlotsJl()" style="width:80px;">
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="plotsjl-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>scatter(x, y, zcolor=theta, colormap=:viridis) · backend: gr()</span>
      <span>Julia Multiple Dispatch Recipe Pipeline · High-Rate GR Engine Simulation</span>
    </div>
    """

    custom_js = """
    function drawPlotsJl() {
      const c = document.getElementById('plotsjl-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const N = parseInt(document.getElementById('pl-pts').value);
      const goldenAngle = Math.PI * (3 - Math.sqrt(5));
      const cx = W / 2; const cy = H / 2;

      for (let i = 1; i <= N; i++) {
        const theta = i * goldenAngle;
        const r = Math.sqrt(i) * 6.5;
        const x = cx + r * Math.cos(theta);
        const y = cy + r * Math.sin(theta);

        const hue = (theta % (2 * Math.PI)) / (2 * Math.PI) * 160 + 120;
        ctx.fillStyle = `hsl(${hue}, 90%, 55%)`;
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, 2*Math.PI);
        ctx.fill();
      }
    }

    window.addEventListener('load', () => { drawPlotsJl(); });
    window.addEventListener('resize', drawPlotsJl);
    """

    html = render_lang_page("Julia", "Plots.jl", "Julia Visualization", 'using Pkg; Pkg.add("Plots")',
                            "https://docs.juliaplots.org",
                            "Powerful unified metapackage interface across GR, Plotly, and PyPlot.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Plots.jl", html)

# 3. PLUTO.JL
def build_pluto():
    paradigms = [{
        "tag": "01 / REACTIVE NOTEBOOKS",
        "title": "Reactive Computational Notebooks with Zero Hidden State",
        "subtitle": "Pluto analyzes the AST of Julia code cells to build a static dependency DAG: modifying a slider updates only dependent reactive cells.",
        "math_desc": "Predator-Prey Lotka-Volterra ODE: $\\frac{dx}{dt} = \\alpha x - \\beta x y, \\; \\frac{dy}{dt} = \\delta x y - \\gamma y$ with live parameter sliders.",
        "math_formula": "\\mathbf{V}_{t+1} = \\mathbf{V}_t + \\Delta t \\cdot \\mathbf{F}(\\mathbf{V}_t; \\alpha, \\beta, \\gamma, \\delta)",
        "time_complexity": "O(N) per reactive state propagation",
        "space_complexity": "O(C) where C is notebook cell AST count",
        "enterprise_use": "Interactive university STEM curricula, computational biophysics research reproducible reports.",
        "strengths": "No hidden global state; exports self-contained HTML containing full Julia source and interactive state.",
        "tradeoffs": "Single cell cannot redefine existing variable names without creating a child scope.",
        "metrics": [
            {"label": "Reactivity", "val": "Static AST DAG", "sub": "Pure Reactive"},
            {"label": "Export", "val": "Standalone HTML", "sub": "Embedded Code"},
            {"label": "Hidden State", "val": "0%", "sub": "Deterministic"},
            {"label": "License", "val": "MIT", "sub": "Open Standard"}
        ],
        "code": """# Pluto.jl Reactive Notebook Cell Definition
using PlutoUI
using Plots

# Cell 1: Reactive Sliders
@bind alpha Slider(0.5:0.1:3.0, default=1.5, show_value=true)
@bind beta Slider(0.2:0.05:2.0, default=0.8, show_value=true)

# Cell 2: Reactive Simulation (Re-runs automatically when alpha or beta changes)
begin
    t = 0:0.05:20
    x = zeros(length(t)); y = zeros(length(t))
    x[1] = 10.0; y[1] = 5.0
    for i in 1:(length(t)-1)
        x[i+1] = x[i] + (alpha * x[i] - beta * x[i] * y[i]) * 0.05
        y[i+1] = y[i] + (0.05 * x[i] * y[i] - 0.8 * y[i]) * 0.05
    end
    plot(t, [x y], label=["Prey (x)" "Predator (y)"], linewidth=2, background_color="#050806")
end"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">PLUTO.JL REACTIVE NOTEBOOK DAG</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Prey Growth α:</label>
        <input type="range" id="pluto-alpha" min="0.5" max="2.5" step="0.1" value="1.2" oninput="updatePlutoSim()" style="width:70px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); margin-left:6px;">Predation β:</label>
        <input type="range" id="pluto-beta" min="0.2" max="1.5" step="0.1" value="0.6" oninput="updatePlutoSim()" style="width:70px;">
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; flex-direction:column; gap:12px;">
      <div style="background:#0c1410; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:10px;">
        <div style="font-family:var(--font-mono); font-size:0.72rem; color:#f3cf65;">Cell 1: @bind alpha Slider(...) & @bind beta Slider(...)</div>
        <div style="font-size:0.78rem; color:#94a3b8; margin-top:2px;">Topological dependency re-evaluates Cell 2 automatically with zero hidden state.</div>
      </div>
      <div style="flex:1; background:#070b09; border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:10px; display:flex; flex-direction:column;">
        <div style="font-family:var(--font-mono); font-size:0.68rem; color:#00e676; margin-bottom:4px;">Cell 2: Lotka-Volterra Predator-Prey Phase Evolution</div>
        <canvas id="pluto-canvas" style="width:100%; flex:1;"></canvas>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>@bind alpha Slider(); plot(t, [prey, predator])</span>
      <span>Static AST Invalidation · Export to Zero-Dependency Standalone HTML</span>
    </div>
    """

    custom_js = """
    function updatePlutoSim() {
      const alpha = parseFloat(document.getElementById('pluto-alpha').value);
      const beta = parseFloat(document.getElementById('pluto-beta').value);
      drawPluto(alpha, beta);
    }

    function drawPluto(alpha, beta) {
      const c = document.getElementById('pluto-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070b09';
      ctx.fillRect(0, 0, W, H);

      // Grid
      ctx.strokeStyle = 'rgba(255,255,255,0.05)';
      for (let y = 0; y < H; y += 30) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      const steps = 180;
      let prey = 10; let pred = 5;
      const preyPts = [prey];
      const predPts = [pred];

      for (let i = 0; i < steps; i++) {
        const dt = 0.08;
        const dPrey = (alpha * prey - beta * prey * pred) * dt;
        const dPred = (0.04 * prey * pred - 0.6 * pred) * dt;
        prey = Math.max(0.1, prey + dPrey);
        pred = Math.max(0.1, pred + dPred);
        preyPts.push(prey);
        predPts.push(pred);
      }

      // Plot Prey (Green)
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i <= steps; i++) {
        const x = (i / steps) * W;
        const y = H - 20 - (preyPts[i] / 25) * (H - 40);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Plot Predator (Gold)
      ctx.strokeStyle = '#f3cf65';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i <= steps; i++) {
        const x = (i / steps) * W;
        const y = H - 20 - (predPts[i] / 25) * (H - 40);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }

    window.addEventListener('load', () => { updatePlutoSim(); });
    window.addEventListener('resize', updatePlutoSim);
    """

    html = render_lang_page("Julia", "Pluto.jl", "Julia Visualization", 'using Pkg; Pkg.add("Pluto")',
                            "https://plutojl.org",
                            "Reactive computational notebook environment with deterministic HTML exports.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Pluto.jl", html)

# 4. GADFLY
def build_gadfly():
    paradigms = [{
        "tag": "01 / PURE JULIA GRAMMAR",
        "title": "Grammar of Graphics in Pure Julia & Direct SVG",
        "subtitle": "Implements Wilkinson's Grammar of Graphics directly in Julia without C/Python dependencies, outputting clean W3C SVG.",
        "math_desc": "2D Kernel density contour estimator: $\\hat{f}(x,y) = \\frac{1}{n h_x h_y} \\sum_{i=1}^n K\\left(\\frac{x-x_i}{h_x}\\right) K\\left(\\frac{y-y_i}{h_y}\\right)$.",
        "math_formula": "\\text{Plot} = \\text{layer}(\\text{x}=X, \\text{y}=Y, \\text{Geom.density2d}) + \\text{Theme}(\\text{dark})",
        "time_complexity": "O(N log N) grid density binning",
        "space_complexity": "O(N) Compose.jl vector canvas tree",
        "enterprise_use": "Automated biostatistical batch reporting, server-side SVG graphics generation.",
        "strengths": "Pure Julia implementation; beautiful Compose.jl vector geometry backend.",
        "tradeoffs": "Moderate compile times on older Julia versions.",
        "metrics": [
            {"label": "Engine", "val": "Compose.jl", "sub": "Pure Julia Vector"},
            {"label": "Output", "val": "W3C SVG / PDF", "sub": "Vector Target"},
            {"label": "Syntax", "val": "Grammar of Graphics", "sub": "Wilkinson Spec"},
            {"label": "License", "val": "MIT", "sub": "JuliaStats"}
        ],
        "code": """using Gadfly
using RDatasets

iris = dataset("datasets", "iris")

p = plot(iris, x=:SepalLength, y=:SepalWidth, color=:Species,
         Geom.point, Geom.density2d,
         Theme(background_color="#040705",
               default_color="#00e676",
               panel_stroke="#334155"))

draw(SVG("gadfly_density.svg", 8inch, 5inch), p)"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">GADFLY PURE JULIA SVG PIPELINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="toggleGadflyContours()" style="font-size:0.7rem; padding:3px 8px;">Toggle Contours</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="gadfly-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>plot(df, x=:x, y=:y, color=:group, Geom.point, Geom.density2d)</span>
      <span>Compose.jl Scenegraph · Pure Julia Vector Geometry Generation</span>
    </div>
    """

    custom_js = """
    let showGfContours = true;
    function toggleGadflyContours() { showGfContours = !showGfContours; drawGadfly(); }

    function drawGadfly() {
      const c = document.getElementById('gadfly-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const cx = W / 2; const cy = H / 2;

      // Draw 2D density contour ellipses
      if (showGfContours) {
        const colors = ['#2e1e3b', '#3b4371', '#407088', '#49a09d', '#00e676'];
        for (let lvl = 0; lvl < 5; lvl++) {
          const factor = (5 - lvl) / 5;
          ctx.strokeStyle = colors[lvl];
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.ellipse(cx, cy, 180 * factor, 110 * factor, -0.3, 0, 2*Math.PI);
          ctx.stroke();
        }
      }

      // Scatter points
      for (let i = 0; i < 90; i++) {
        const u = (Math.random() - 0.5) * 160;
        const v = (Math.random() - 0.5) * 90;
        const px = cx + u * Math.cos(-0.3) - v * Math.sin(-0.3);
        const py = cy + u * Math.sin(-0.3) + v * Math.cos(-0.3);

        ctx.fillStyle = (i % 2 === 0) ? '#00e676' : '#f3cf65';
        ctx.beginPath();
        ctx.arc(px, py, 3.5, 0, 2*Math.PI);
        ctx.fill();
      }
    }

    window.addEventListener('load', () => { drawGadfly(); });
    window.addEventListener('resize', drawGadfly);
    """

    html = render_lang_page("Julia", "Gadfly.jl", "Julia Visualization", 'using Pkg; Pkg.add("Gadfly")',
                            "http://gadflyjl.org",
                            "Grammar of graphics implementation written in 100% pure Julia.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Gadfly.jl", html)

# 5. STATSPLOTS
def build_statsplots():
    paradigms = [{
        "tag": "01 / STATISTICAL RECIPES",
        "title": "Marginal Distributions, Violin Plots & Correlation",
        "subtitle": "Provides rich statistical visualization recipes extending Plots.jl with automated marginal distributions, boxplots, and dendrograms.",
        "math_desc": "Kernel density marginal projection: $f_X(x) = \\int f_{X,Y}(x,y) dy$ coupled with interquartile range median notches.",
        "math_formula": "\\text{Notch} = \\text{Median} \\pm 1.57 \\times \\frac{\\text{IQR}}{\\sqrt{n}}",
        "time_complexity": "O(N log N) sorting and density estimation",
        "space_complexity": "O(N) recipe expansion memory",
        "enterprise_use": "Biostatistical clinical dose-response curves, quantitative hedge fund asset volatility clustering.",
        "strengths": "Deep integration with Julia DataFrames and Distributions.jl; effortless marginal plots via `@df` macro.",
        "tradeoffs": "Inherits Plots.jl backend dependencies.",
        "metrics": [
            {"label": "Recipes", "val": "StatsPlots Core", "sub": "Macro Driven"},
            {"label": "DataFrames", "val": "@df Integration", "sub": "Native Julia"},
            {"label": "Distributions", "val": "Distributions.jl", "sub": "Parametric"},
            {"label": "License", "val": "MIT", "sub": "JuliaStats"}
        ],
        "code": """using StatsPlots
using DataFrames, Random

df = DataFrame(
    Cohort = repeat(["Control", "Treatment A", "Treatment B"], inner = 150),
    Response = [randn(150) .* 1.2 .+ 5; randn(150) .* 0.8 .+ 7.5; randn(150) .* 1.5 .+ 9]
)

@df df violin(:Cohort, :Response, side=:left, color="#00e676", label="Distribution")
@df df boxplot!(:Cohort, :Response, side=:right, color="#f3cf65", label="IQR Box",
               title="Dose Response Stratification across Cohorts")"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">STATSPLOTS.JL STATISTICAL RECIPES</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="statsplots-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>@df df violin(:Cohort, :Response) · boxplot!(:Cohort, :Response)</span>
      <span>JuliaStats Recipe Metaprogramming · Asymmetric Half-Violin Distributions</span>
    </div>
    """

    custom_js = """
    function drawStatsPlots() {
      const c = document.getElementById('statsplots-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const cohorts = ['Control Cohort', 'Treatment Alpha', 'Treatment Beta'];
      const means = [45, 68, 85];
      const slotW = (W - 100) / cohorts.length;

      cohorts.forEach((cohort, idx) => {
        const cx = 80 + idx * slotW + slotW / 2;

        // Left half violin
        ctx.fillStyle = 'rgba(0, 230, 118, 0.4)';
        ctx.strokeStyle = '#00e676';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(cx, H - 40);

        for (let s = 0; s <= 30; s++) {
          const yVal = s * 4;
          const py = H - 40 - (yVal / 120) * (H - 80);
          const density = Math.exp(-Math.pow(yVal - means[idx], 2) / 300) * (slotW * 0.35);
          ctx.lineTo(cx - density, py);
        }
        ctx.lineTo(cx, 40);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Right half boxplot
        const medY = H - 40 - (means[idx] / 120) * (H - 80);
        ctx.fillStyle = '#0a140f';
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 1.8;
        ctx.fillRect(cx, medY - 30, 22, 60);
        ctx.strokeRect(cx, medY - 30, 22, 60);

        ctx.strokeStyle = '#fff';
        ctx.beginPath(); ctx.moveTo(cx, medY); ctx.lineTo(cx + 22, medY); ctx.stroke();

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '11px DM Sans';
        ctx.textAlign = 'center';
        ctx.fillText(cohort, cx, H - 15);
      });
    }

    window.addEventListener('load', () => { drawStatsPlots(); });
    window.addEventListener('resize', drawStatsPlots);
    """

    html = render_lang_page("Julia", "StatsPlots.jl", "Julia Visualization", 'using Pkg; Pkg.add("StatsPlots")',
                            "https://github.com/JuliaPlots/StatsPlots.jl",
                            "Statistical visualization recipes for DataFrames and distributions.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("StatsPlots.jl", html)

# 6. GRAPHRECIPES
def build_graphrecipes():
    paradigms = [{
        "tag": "01 / GRAPH RECIPES",
        "title": "Spectral & Tree Graph Visualization in Julia",
        "subtitle": "High-performance recipe for Graphs.jl data structures, supporting Kamada-Kawai, Buchheim trees, and spectral Laplacian embeddings.",
        "math_desc": "Spectral graph drawing: eigenvectors of graph Laplacian $\\mathbf{L} = \\mathbf{D} - \\mathbf{A}$ corresponding to smallest non-zero eigenvalues $\\lambda_2, \\lambda_3$.",
        "math_formula": "\\mathbf{L} \\mathbf{v}_k = \\lambda_k \\mathbf{v}_k, \\quad (x_i, y_i) = (v_{2,i}, v_{3,i})",
        "time_complexity": "O(V^3) or O(V k) Lanczos sparse solver",
        "space_complexity": "O(V + E) sparse adjacency matrix",
        "enterprise_use": "Compiler call graph analysis, large-scale supply chain logistics graph partitioning.",
        "strengths": "Operates directly on standard Graphs.jl graphs; zero data copying.",
        "tradeoffs": "Requires Plots.jl backend for final rendering.",
        "metrics": [
            {"label": "Core Engine", "val": "Graphs.jl", "sub": "Pure Julia"},
            {"label": "Spectral", "val": "Arpack.jl", "sub": "Eigen Solvers"},
            {"label": "Scale", "val": "50,000 Edges", "sub": "Sparse Memory"},
            {"label": "License", "val": "MIT", "sub": "JuliaPlots"}
        ],
        "code": """using GraphRecipes, Plots
using Graphs

# Barabasi-Albert scale-free graph in Julia
g = barabasi_albert(40, 2)

graphplot(g,
          layout = :spectral,
          nodecolor = "#00e676",
          nodesize = 0.2,
          linecolor = "#334155",
          linewidth = 1.2,
          background_color = "#040705",
          title = "GraphRecipes.jl: Spectral Laplacian Graph Embedding")"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">GRAPHRECIPES SPECTRAL EMBEDDING</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="gr-graph-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>graphplot(g, layout=:spectral, nodecolor=:teal)</span>
      <span>Graphs.jl Integration · Laplacian Eigenvector Coordinate Projection</span>
    </div>
    """

    custom_js = """
    function drawGraphRecipes() {
      const c = document.getElementById('gr-graph-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const N = 32;
      const nodes = [];
      for (let i = 0; i < N; i++) {
        const u = (i - N/2) / (N/2);
        nodes.push({
          x: W/2 + u * (W * 0.38) + Math.sin(i * 1.7) * 30,
          y: H/2 + (Math.pow(u, 2) - 0.4) * (H * 0.5) + Math.cos(i * 1.2) * 25
        });
      }

      // Edges
      ctx.strokeStyle = 'rgba(255,255,255,0.12)';
      ctx.lineWidth = 1.2;
      for (let i = 0; i < N; i++) {
        for (let j = i + 1; j < N; j++) {
          const dist = Math.hypot(nodes[i].x - nodes[j].x, nodes[i].y - nodes[j].y);
          if (dist < 120) {
            ctx.beginPath();
            ctx.moveTo(nodes[i].x, nodes[i].y);
            ctx.lineTo(nodes[j].x, nodes[j].y);
            ctx.stroke();
          }
        }
      }

      // Nodes
      nodes.forEach((n, idx) => {
        ctx.fillStyle = idx === 0 ? '#f3cf65' : '#00e5ff';
        ctx.beginPath();
        ctx.arc(n.x, n.y, 5, 0, 2*Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#040705';
        ctx.stroke();
      });
    }

    window.addEventListener('load', () => { drawGraphRecipes(); });
    window.addEventListener('resize', drawGraphRecipes);
    """

    html = render_lang_page("Julia", "GraphRecipes.jl", "Julia Visualization", 'using Pkg; Pkg.add("GraphRecipes")',
                            "https://github.com/JuliaPlots/GraphRecipes.jl",
                            "High-performance graph layout recipes for Graphs.jl network structures.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("GraphRecipes.jl", html)

# 7. GEOMAKIE
def build_geomakie():
    paradigms = [{
        "tag": "01 / HIGH-SPEED CARTOGRAPHY",
        "title": "GPU Geodesic Projections & Satellite Rasters",
        "subtitle": "Combines Makie's high-speed GPU pipeline with Proj.jl for real-time interactive coordinate re-projections directly in HTML.",
        "math_desc": "Geodesic transformation from ellipsoidal WGS84 coordinates to Orthographic projection: $x = R \\cos\\phi \\sin(\\lambda - \\lambda_0)$.",
        "math_formula": "y = R \\left[ \\cos\\phi_0 \\sin\\phi - \\sin\\phi_0 \\cos\\phi \\cos(\\lambda - \\lambda_0) \\right]",
        "time_complexity": "O(N) hardware GPU coordinate warp",
        "space_complexity": "O(N) vertex mesh array",
        "enterprise_use": "Oceanographic global currents telemetry, aviation transatlantic routing optimization.",
        "strengths": "Fastest cartographic rendering engine in Julia; zero Python/GDAL bottlenecks.",
        "tradeoffs": "Ecosystem is evolving rapidly; requires recent Julia release.",
        "metrics": [
            {"label": "Projection", "val": "Proj.jl Native", "sub": "Geodesic C++"},
            {"label": "Engine", "val": "Makie GL", "sub": "Hardware Shader"},
            {"label": "Output", "val": "WebGL / Cairo", "sub": "Interactive 3D"},
            {"label": "License", "val": "MIT", "sub": "JuliaGeo"}
        ],
        "code": """using GeoMakie, GLMakie

fig = Figure(backgroundcolor = "#040705")
ga = GeoAxis(fig[1, 1],
             dest = "+proj=ortho +lon_0=103.8 +lat_0=1.35",
             title = "GeoMakie.jl: Satellite Orthographic Projection")

lines!(ga, GeoMakie.coastlines(), color = "#00e676")
fig"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">GEOMAKIE GEODESIC PROJECTION</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="geomakie-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>GeoAxis(dest='+proj=ortho +lon_0=103.8') · GeoMakie.coastlines()</span>
      <span>Proj.jl Fast Coordinate Transformations · Native Julia GPU Cartography</span>
    </div>
    """

    custom_js = """
    function drawGeoMakie() {
      const c = document.getElementById('geomakie-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const cx = W / 2; const cy = H / 2; const R = 170;

      // Globe background
      ctx.fillStyle = '#08140e';
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, 2*Math.PI); ctx.fill();
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.8;
      ctx.stroke();

      // Parallels
      ctx.strokeStyle = 'rgba(255,255,255,0.1)';
      for (let lat = -60; lat <= 60; lat += 30) {
        const yOffset = cy - Math.sin((lat * Math.PI) / 180) * R;
        const rLat = Math.cos((lat * Math.PI) / 180) * R;
        ctx.beginPath();
        ctx.ellipse(cx, yOffset, rLat, rLat * 0.25, 0, 0, 2*Math.PI);
        ctx.stroke();
      }

      // Geodesic Flight Route
      ctx.strokeStyle = '#f3cf65';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(cx + 40, cy - 10);
      ctx.bezierCurveTo(cx + 10, cy - 100, cx - 60, cy - 90, cx - 80, cy - 60);
      ctx.stroke();
    }

    window.addEventListener('load', () => { drawGeoMakie(); });
    window.addEventListener('resize', drawGeoMakie);
    """

    html = render_lang_page("Julia", "GeoMakie.jl", "Julia Visualization", 'using Pkg; Pkg.add("GeoMakie")',
                            "https://geo.makie.org",
                            "High-performance geospatial cartography and geodesic projections.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("GeoMakie.jl", html)

# 8. GENIE.JL
def build_genie():
    paradigms = [{
        "tag": "01 / FULL-STACK JULIA WEB",
        "title": "Full-Stack Julia MVC & Stipple Reactive Dashboards",
        "subtitle": "Genie and Stipple provide pure Julia reactive full-stack web applications with two-way WebSockets and Vue.js hydration.",
        "math_desc": "Two-way model reactive synchronization: changes in Julia struct fields trigger reactive DOM mutations via JSON-RPC.",
        "math_formula": "\\Delta \\text{State} = \\text{Diff}(\\mathbf{M}_{t+1}, \\mathbf{M}_t) \\xrightarrow{\\text{WS}} \\text{DOM.patch()}",
        "time_complexity": "O(1) incremental state diff",
        "space_complexity": "O(M) memory session state",
        "enterprise_use": "High-throughput industrial telemetry web dashboards, real-time algorithmic trading consoles.",
        "strengths": "C-speed backend logic written in 100% Julia; enterprise MVC modularity.",
        "tradeoffs": "Ecosystem is smaller than Python's Django/FastAPI.",
        "metrics": [
            {"label": "Protocol", "val": "WebSocket JSON-RPC", "sub": "Sub-millisecond"},
            {"label": "Frontend", "val": "Stipple Vue Bridge", "sub": "Hydrated DOM"},
            {"label": "Speed", "val": "C-Speed Backend", "sub": "Native Julia"},
            {"label": "License", "val": "MIT", "sub": "GenieFramework"}
        ],
        "code": """using GenieFramework
@genietools

@app begin
    @in active_channel = "Direct Hospitality"
    @out kpi_rev = "$2.48M"
    @out kpi_roas = "5.2x"
    @onchange active_channel begin
        kpi_rev = active_channel == "Direct Hospitality" ? "$2.48M" : "$1.85M"
    end
end

ui() = [
    h1("Genie.jl Commercial Strategy Control Room"),
    row([
        cell(class="st-card", [h4("Attributed Net"), h2("{{kpi_rev}}")]),
        cell(class="st-card", [h4("Target ROAS"), h2("{{kpi_roas}}")])
    ])
]

@page("/", ui)
Server.up()"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">GENIE.JL FULL-STACK JULIA RUNTIME</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#070b09; display:flex; flex-direction:column; gap:16px;">
      <h3 style="font-family:'Newsreader', serif; font-size:1.4rem; color:#fff;">Genie.jl Enterprise Commercial Control Room</h3>
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px;">
        <div style="background:#0e1712; border:1px solid rgba(255,255,255,0.08); padding:14px; border-radius:6px;">
          <div style="font-size:0.7rem; color:#94a3b8;">Commercial Gross Attributed</div>
          <div style="font-size:1.6rem; font-weight:700; color:#00e676; margin-top:4px;">$2.48M</div>
          <div style="font-size:0.72rem; color:#00e676;">▲ +18.4% vs OTA Benchmark</div>
        </div>
        <div style="background:#0e1712; border:1px solid rgba(255,255,255,0.08); padding:14px; border-radius:6px;">
          <div style="font-size:0.7rem; color:#94a3b8;">Channel Commission Recapture</div>
          <div style="font-size:1.6rem; font-weight:700; color:#f3cf65; margin-top:4px;">$610K</div>
          <div style="font-size:0.72rem; color:#00e676;">▲ 74.2% Member Share</div>
        </div>
        <div style="background:#0e1712; border:1px solid rgba(255,255,255,0.08); padding:14px; border-radius:6px;">
          <div style="font-size:0.7rem; color:#94a3b8;">Julia Execution Latency</div>
          <div style="font-size:1.6rem; font-weight:700; color:#00e5ff; margin-top:4px;">1.4 ms</div>
          <div style="font-size:0.72rem; color:#94a3b8;">Sub-millisecond Event Loop</div>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>GenieFramework · Stipple.jl Reactive Two-Way WebSockets</span>
      <span>C-Speed Pure Julia Backend Server · Zero JavaScript Overhead</span>
    </div>
    """

    custom_js = ""

    html = render_lang_page("Julia", "Genie.jl", "Julia Visualization", 'using Pkg; Pkg.add("GenieFramework")',
                            "https://genieframework.com",
                            "Full-stack reactive web applications and Stipple dashboards in pure Julia.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Genie.jl", html)

if __name__ == "__main__":
    build_julia_all()
