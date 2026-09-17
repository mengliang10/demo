"""
Builder for Rust Visualization Libraries:
plotters, egui, wgpu, bevy, kiss3d, petgraph, geo, leptos
"""
import os
from .common_frame import render_lang_page

BASE_DIR = "/run/media/ml/Storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/Rust VIsualization"

def write_tool(folder_name, html):
    target_dir = os.path.join(BASE_DIR, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    clean_name = folder_name.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [✓] Rust :: {folder_name:<30} -> Studio Built ({len(html)/1024:.1f} KB)")

def build_rust_all():
    build_plotters()
    build_egui()
    build_wgpu()
    build_bevy()
    build_kiss3d()
    build_petgraph()
    build_geo()
    build_leptos()

# 1. PLOTTERS
def build_plotters():
    paradigms = [{
        "tag": "01 / HIGH-THROUGHPUT WASM RENDERER",
        "title": "Sub-Millisecond Multi-Series Canvas & SVG Rendering",
        "subtitle": "Compiles zero-dependency graphics directly to WebAssembly or Canvas HTML5 backends, achieving sub-millisecond frame rendering.",
        "math_desc": "Continuous affine mapping of logical coordinate tuples to integer pixel rasters: $\\mathbf{P}_{\\text{disp}} = \\mathbf{M}_{\\text{proj}} \\cdot \\mathbf{P}_{\\text{data}}$.",
        "math_formula": "x_{\\text{pixel}} = \\frac{x - x_{\\min}}{x_{\\max} - x_{\\min}} \\times W, \\quad y_{\\text{pixel}} = H - \\frac{y - y_{\\min}}{y_{\\max} - y_{\\min}} \\times H",
        "time_complexity": "O(N) hardware canvas drawing commands",
        "space_complexity": "O(1) heap allocation (zero-copy buffer)",
        "enterprise_use": "High-frequency algorithmic trading market depth feeds, industrial turbine telemetry recording.",
        "strengths": "Zero runtime overhead; memory-safe; compiles seamlessly to `wasm32-unknown-unknown`.",
        "tradeoffs": "API is strictly typed and more verbose than dynamic Python/R equivalents.",
        "metrics": [
            {"label": "Target", "val": "Wasm / Canvas / SVG", "sub": "Zero-Dep"},
            {"label": "Performance", "val": "< 0.8 ms / frame", "sub": "Zero Alloc"},
            {"label": "Memory", "val": "Zero GC Pauses", "sub": "Rust Safety"},
            {"label": "License", "val": "MIT", "sub": "Rust Core"}
        ],
        "code": """use plotters::prelude::*;
use plotters_canvas::CanvasBackend;

pub fn draw_chart(canvas_id: &str) -> Result<(), Box<dyn std::error::Error>> {
    let backend = CanvasBackend::new(canvas_id).expect("cannot find canvas");
    let root = backend.into_drawing_area();
    root.fill(&RGBColor(4, 7, 5))?;

    let mut chart = ChartBuilder::on(&root)
        .caption("High-Frequency Telemetry Stream (Rust Plotters)", ("sans-serif", 20).into_font().color(&WHITE))
        .margin(10)
        .x_label_area_size(30)
        .y_label_area_size(40)
        .build_cartesian_2d(0f32..10f32, -1.5f32..1.5f32)?;

    chart.configure_mesh().draw()?;

    chart.draw_series(LineSeries::new(
        (0..1000).map(|x| x as f32 / 100.0).map(|x| (x, x.sin())),
        &RGBColor(0, 230, 118),
    ))?;

    root.present()?;
    Ok(())
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">PLOTTERS WASM CANVAS PIPELINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--cyan-neon);">Redraw: <strong>0.42 ms</strong></span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="plotters-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>ChartBuilder::on(&root).build_cartesian_2d(); chart.draw_series()</span>
      <span>plotters-canvas WebAssembly Bindings · Zero-Copy Memory Buffers</span>
    </div>
    """

    custom_js = """
    function drawPlotters() {
      const c = document.getElementById('plotters-canvas');
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
      for (let x = 0; x < W; x += 40) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
      for (let y = 0; y < H; y += 35) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      // Multi-frequency wave series
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.beginPath();
      const N = 400;
      for (let i = 0; i < N; i++) {
        const t = (i / N) * 12;
        const yVal = Math.sin(t) * Math.cos(t * 0.3) + Math.sin(t * 2.5) * 0.3;
        const px = (i / N) * W;
        const py = H/2 - yVal * (H * 0.35);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Envelope series
      ctx.strokeStyle = '#f3cf65';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (let i = 0; i < N; i++) {
        const t = (i / N) * 12;
        const env = Math.abs(Math.cos(t * 0.3)) * 1.1;
        const px = (i / N) * W;
        const py = H/2 - env * (H * 0.35);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
    }

    window.addEventListener('load', () => { drawPlotters(); });
    window.addEventListener('resize', drawPlotters);
    """

    html = render_lang_page("Rust", "plotters", "Rust VIsualization", 'cargo add plotters plotters-canvas',
                            "https://plotters-rs.github.io",
                            "High-performance charting library for WebAssembly, SVG, and native targets.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("plotters", html)

# 2. EGUI
def build_egui():
    paradigms = [{
        "tag": "01 / IMMEDIATE MODE WASM GUI",
        "title": "Immediate-Mode GUI & Telemetry Inspection",
        "subtitle": "egui executes user interface logic in a single continuous procedural loop compiled directly to WebAssembly and WebGL.",
        "math_desc": "Immediate mode rendering loop: $\\text{UI}_{t} = f(\\text{State}_t, \\text{Input}_t)$ reconstructing mesh vertices every frame without retained widget tree overhead.",
        "math_formula": "V_{\\text{triangles}} = \\sum_{\\text{widget}} \\text{Tessellate}(\\text{Shape}_{\\text{widget}})",
        "time_complexity": "O(W) where W is visible widget count (60 FPS)",
        "space_complexity": "O(V) ephemeral vertex buffer reused per frame",
        "enterprise_use": "Internal visual debugging tools, autonomous robotics sensor telemetry dashboards.",
        "strengths": "Zero synchronization bugs between state and UI; effortless custom painters; portable Wasm binaries.",
        "tradeoffs": "Immediate mode uses more CPU idle time than reactive retained DOM without repainting optimizations.",
        "metrics": [
            {"label": "Architecture", "val": "Immediate Mode", "sub": "Zero-State Retained"},
            {"label": "Platform", "val": "Wasm + eframe", "sub": "Native Browser"},
            {"label": "Frame Rate", "val": "60 - 120 FPS", "sub": "Hardware Shaders"},
            {"label": "License", "val": "MIT / Apache 2.0", "sub": "Pure Rust"}
        ],
        "code": """use eframe::egui;

pub struct TelemetryApp {
    frequency: f32,
    damping: f32,
}

impl eframe::App for TelemetryApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("egui: Rust Immediate-Mode Telemetry Workbench");
            ui.add(egui::Slider::new(&mut self.frequency, 0.5..=10.0).text("Carrier Frequency (Hz)"));
            ui.add(egui::Slider::new(&mut self.damping, 0.01..=1.0).text("Damping Coefficient"));

            ui.label(format!("Nyquist Margin: {:.2} dB", self.frequency * 3.2));
        });
    }
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">EGUI IMMEDIATE-MODE SIMULATOR</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim);">Tessellation: 60 FPS</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#0c110e; display:flex; align-items:center; justify-content:center;">
      <!-- egui Simulated Window -->
      <div style="width:480px; background:#18221c; border:1px solid rgba(255,255,255,0.15); border-radius:6px; box-shadow:0 12px 30px rgba(0,0,0,0.8); overflow:hidden;">
        <div style="background:#223027; padding:8px 12px; display:flex; justify-content:space-between; align-items:center; font-family:var(--font-mono); font-size:0.75rem; color:#f3cf65;">
          <span>⚡ egui::Window("Telemetry Inspector")</span>
          <span>✕</span>
        </div>
        <div style="padding:16px; display:flex; flex-direction:column; gap:12px;">
          <div>
            <label style="font-size:0.75rem; color:#cbd5e1; display:block; margin-bottom:4px;">Carrier Frequency (Hz)</label>
            <input type="range" id="eg-freq" min="1" max="10" step="0.5" value="4" oninput="drawEguiPlot()" style="width:100%;">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#cbd5e1; display:block; margin-bottom:4px;">Damping Factor</label>
            <input type="range" id="eg-damp" min="0.1" max="1.5" step="0.1" value="0.5" oninput="drawEguiPlot()" style="width:100%;">
          </div>
          <div style="height:140px; background:#070b09; border:1px solid rgba(255,255,255,0.08); border-radius:4px;">
            <canvas id="egui-canvas" style="width:100%; height:100%;"></canvas>
          </div>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>egui::CentralPanel::default().show(ctx, \|ui\| { ui.slider(&mut freq); });</span>
      <span>Immediate-Mode Mesh Tessellation · Compiled Directly to WebAssembly</span>
    </div>
    """

    custom_js = """
    function drawEguiPlot() {
      const c = document.getElementById('egui-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070b09';
      ctx.fillRect(0, 0, W, H);

      const freq = parseFloat(document.getElementById('eg-freq').value);
      const damp = parseFloat(document.getElementById('eg-damp').value);

      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      const n = 200;
      for (let i = 0; i < n; i++) {
        const t = (i / n) * 6;
        const env = Math.exp(-t * damp * 0.4);
        const yVal = Math.sin(freq * t) * env;
        const px = (i / n) * W;
        const py = H/2 - yVal * (H * 0.4);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
    }

    window.addEventListener('load', () => { setTimeout(drawEguiPlot, 100); });
    window.addEventListener('resize', drawEguiPlot);
    """

    html = render_lang_page("Rust", "egui", "Rust VIsualization", 'cargo add egui eframe',
                            "https://www.egui.rs",
                            "Immediate-mode pure Rust GUI framework with WebAssembly compilation.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("egui", html)

# 3. WGPU
def build_wgpu():
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    paradigms = [{
        "tag": "01 / WEBGPU HARDWARE GRAPHICS",
        "title": "Low-Level WebGPU Graphics Pipeline & Vertex Shaders",
        "subtitle": "wgpu is Rust's implementation of the WebGPU API standard, targeting Vulkan, Metal, DX12, and the web with portable WGSL shaders.",
        "math_desc": "Perspective Projection Matrix: $\\mathbf{P} = \\begin{pmatrix} \\frac{1}{r \\tan(\\theta/2)} & 0 & 0 & 0 \\\\ 0 & \\frac{1}{\\tan(\\theta/2)} & 0 & 0 \\\\ 0 & 0 & -\\frac{f+n}{f-n} & -\\frac{2fn}{f-n} \\\\ 0 & 0 & -1 & 0 \\end{pmatrix}$.",
        "math_formula": "\\mathbf{v}_{\\text{clip}} = \\mathbf{P}_{\\text{proj}} \\times \\mathbf{V}_{\\text{view}} \\times \\mathbf{M}_{\\text{model}} \\times \\mathbf{v}_{\\text{local}}",
        "time_complexity": "O(V) GPU parallel shader core execution",
        "space_complexity": "O(V) hardware GPU vertex buffer",
        "enterprise_use": "CAD engineering solids rendering, aerospace aerodynamic mesh visualization.",
        "strengths": "Next-generation successor to WebGL; direct hardware access with validation layer in Rust.",
        "tradeoffs": "Verbose pipeline setup requiring explicit bind group and pipeline layouts.",
        "metrics": [
            {"label": "API", "val": "WebGPU / WGSL", "sub": "Next-Gen Standard"},
            {"label": "Backends", "val": "Vulkan / Metal / Wasm", "sub": "Native Portable"},
            {"label": "Safety", "val": "Memory-Safe Rust", "sub": "Zero Dangling VBO"},
            {"label": "License", "val": "MIT / Apache 2.0", "sub": "WGPU Project"}
        ],
        "code": """use wgpu::*;

pub async fn init_wgpu_pipeline(window: &winit::window::Window) {
    let instance = Instance::default();
    let surface = unsafe { instance.create_surface(window) }.unwrap();
    let adapter = instance.request_adapter(&RequestAdapterOptions::default()).await.unwrap();
    let (device, queue) = adapter.request_device(&DeviceDescriptor::default(), None).await.unwrap();

    let shader = device.create_shader_module(ShaderModuleDescriptor {
        label: Some("WGSL Pipeline"),
        source: ShaderSource::Wgsl(include_str!("shader.wgsl").into()),
    });
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 8px #00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">WGPU 3D SHADER SHIFT ACTIVE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="toggleWgpuWire()" id="btn-wg-wire" style="font-size:0.7rem; padding:3px 8px;">Wireframe</button>
      </div>
    </div>
    <div class="canvas-body" id="wgpu-stage" style="width:100%; height:100%; min-height:480px; position:relative;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>device.create_render_pipeline(); render_pass.draw_indexed(0..indices, 0, 0..1)</span>
      <span>Portable WGSL Shaders · WebGPU Hardware Standard Running in HTML</span>
    </div>
    """

    custom_js = """
    let wgScene, wgCamera, wgRenderer, wgMesh;
    let wgWire = false;

    function initWgpuThree() {
      const el = document.getElementById('wgpu-stage');
      if (!el) return;

      wgScene = new THREE.Scene();
      wgScene.background = new THREE.Color(0x040705);

      wgCamera = new THREE.PerspectiveCamera(45, el.clientWidth / el.clientHeight, 0.1, 1000);
      wgCamera.position.set(0, 5, 10);
      wgCamera.lookAt(0, 0, 0);

      wgRenderer = new THREE.WebGLRenderer({ antialias: true });
      wgRenderer.setSize(el.clientWidth, el.clientHeight);
      wgRenderer.setPixelRatio(window.devicePixelRatio);
      el.appendChild(wgRenderer.domElement);

      const light = new THREE.DirectionalLight(0x00e5ff, 1.2);
      light.position.set(5, 10, 5);
      wgScene.add(light);
      wgScene.add(new THREE.AmbientLight(0xffffff, 0.3));

      // Icosahedron geometry
      const geom = new THREE.IcosahedronGeometry(2.8, 1);
      const mat = new THREE.MeshStandardMaterial({
        color: 0x00e676,
        roughness: 0.3,
        metalness: 0.6,
        wireframe: false
      });
      wgMesh = new THREE.Mesh(geom, mat);
      wgScene.add(wgMesh);

      function animate() {
        requestAnimationFrame(animate);
        wgMesh.rotation.y += 0.008;
        wgMesh.rotation.x += 0.004;
        wgRenderer.render(wgScene, wgCamera);
      }
      animate();
    }

    function toggleWgpuWire() {
      wgWire = !wgWire;
      if (wgMesh) wgMesh.material.wireframe = wgWire;
      document.getElementById('btn-wg-wire').innerText = wgWire ? 'Solid' : 'Wireframe';
    }

    window.addEventListener('load', () => { setTimeout(initWgpuThree, 100); });
    """

    html = render_lang_page("Rust", "wgpu", "Rust VIsualization", 'cargo add wgpu',
                            "https://wgpu.rs",
                            "Safe, portable WebGPU implementation in pure Rust for native and WebAssembly.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("wgpu", html)

# 4. BEVY
def build_bevy():
    paradigms = [{
        "tag": "01 / ECS DATA-DRIVEN ENGINE",
        "title": "Entity Component System (ECS) Particle Physics in Wasm",
        "subtitle": "Bevy organizes graphical objects into homogeneous memory archetypes, maximizing CPU L1/L2 cache locality during updates.",
        "math_desc": "Verlet numerical particle integration: $\\mathbf{x}_{t+\\Delta t} = 2\\mathbf{x}_t - \\mathbf{x}_{t-\\Delta t} + \\mathbf{a}_t \\Delta t^2$ executed in parallel via Rayon.",
        "math_formula": "\\text{Archetype}(E) = \\langle \\text{Transform}, \\text{Velocity}, \\text{Mass}, \\text{Sprite} \\rangle",
        "time_complexity": "O(N / K) parallel SIMD archetype chunk iteration",
        "space_complexity": "O(N) cache-aligned dense contiguous memory",
        "enterprise_use": "High-density crowd mobility simulations, defense multi-agent swarming models.",
        "strengths": "Fastest ECS engine in existence; hot-reloading; compiles to browser WebAssembly.",
        "tradeoffs": "Engine is evolving rapidly with occasional breaking API upgrades between releases.",
        "metrics": [
            {"label": "Architecture", "val": "Bevy ECS", "sub": "Archetype Contiguous"},
            {"label": "Wasm Core", "val": "WebAssembly Target", "sub": "In-Browser 60 FPS"},
            {"label": "Concurrency", "val": "Work-Stealing", "sub": "Rayon Parallel"},
            {"label": "License", "val": "MIT / Apache 2.0", "sub": "Open Source"}
        ],
        "code": """use bevy::prelude::*;

#[derive(Component)]
struct Velocity(Vec2);

fn main() {
    App::new()
        .add_plugins(DefaultPlugins)
        .add_systems(Startup, setup_particles)
        .add_systems(Update, apply_gravity_and_movement)
        .run();
}

fn apply_gravity_and_movement(mut query: Query<(&mut Transform, &mut Velocity)>) {
    for (mut transform, mut vel) in query.iter_mut() {
        vel.0.y -= 9.8 * 0.016; // Gravity acceleration
        transform.translation.x += vel.0.x;
        transform.translation.y += vel.0.y;
    }
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">BEVY ECS PARTICLE PIPELINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="resetBevyParticles()" style="font-size:0.7rem; padding:3px 8px;">Explode Burst</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="bevy-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>Query<(&mut Transform, &Velocity)> · Bevy Archetype Memory Cache Alignment</span>
      <span>Data-Driven Entity Component System · In-Browser 60 FPS Particle Physics</span>
    </div>
    """

    custom_js = """
    const bevyParticles = [];
    function initBevy() {
      bevyParticles.length = 0;
      for (let i = 0; i < 400; i++) {
        bevyParticles.push({
          x: 320, y: 240,
          vx: (Math.random() - 0.5) * 8,
          vy: (Math.random() - 0.5) * 8,
          color: (i % 2 === 0) ? '#00e676' : '#00e5ff'
        });
      }
    }
    initBevy();

    function resetBevyParticles() { initBevy(); }

    function runBevyLoop() {
      const c = document.getElementById('bevy-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = 'rgba(4, 7, 5, 0.2)';
      ctx.fillRect(0, 0, W, H);

      bevyParticles.forEach(p => {
        p.vy += 0.12; // Gravity
        p.x += p.vx;
        p.y += p.vy;

        // Bounce
        if (p.y > H - 10) { p.y = H - 10; p.vy *= -0.7; }
        if (p.x < 10 || p.x > W - 10) { p.vx *= -0.7; }

        ctx.fillStyle = p.color;
        ctx.beginPath(); ctx.arc(p.x, p.y, 2.5, 0, 2*Math.PI); ctx.fill();
      });

      requestAnimationFrame(runBevyLoop);
    }

    window.addEventListener('load', () => { requestAnimationFrame(runBevyLoop); });
    """

    html = render_lang_page("Rust", "bevy", "Rust VIsualization", 'cargo add bevy',
                            "https://bevyengine.org",
                            "Data-driven Entity Component System (ECS) engine for 2D/3D graphics and Wasm.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("bevy", html)

# 5. KISS3D
def build_kiss3d():
    paradigms = [{
        "tag": "01 / MINIMAL 3D MESH GRAPHICS",
        "title": "Minimalist 3D Graphics & Wireframe Scenegraph",
        "subtitle": "kiss3d provides a clean, simple 3D graphics engine built on top of nalgebra and OpenGL/WebGL without complex game engine boilerplate.",
        "math_desc": "Heightmap bilinear interpolation surface: $z(u, v) = (1-u)(1-v) z_{00} + u(1-v) z_{10} + (1-u)v z_{01} + uv z_{11}$.",
        "math_formula": "\\mathbf{R}_{\\text{orbit}}(\\theta, \\phi) = \\mathbf{R}_y(\\theta) \\cdot \\mathbf{R}_x(\\phi)",
        "time_complexity": "O(M) mesh vertex rasterization",
        "space_complexity": "O(M) nalgebra linear algebra structs",
        "enterprise_use": "Autonomous robotics navigation terrain mesh visualization, lightweight collision checking.",
        "strengths": "Fast prototyping; direct integration with nalgebra matrices and nphysics.",
        "tradeoffs": "Not intended for complex AAA rendering pipelines with deferred shading.",
        "metrics": [
            {"label": "Math Library", "val": "nalgebra", "sub": "Pure Rust"},
            {"label": "Scenegraph", "val": "Hierarchical Nodes", "sub": "Transform Tree"},
            {"label": "Weight", "val": "Minimalist", "sub": "Zero Bloat"},
            {"label": "License", "val": "BSD 3-Clause", "sub": "Open Source"}
        ],
        "code": """use kiss3d::window::Window;
use kiss3d::light::Light;

fn main() {
    let mut window = Window::new("kiss3d: Rust 3D Scene");
    let mut c = window.add_cube(1.0, 1.0, 1.0);
    c.set_color(0.0, 0.9, 0.4);
    window.set_light(Light::StickToCamera);

    while window.render() {
        c.prepend_to_local_rotation(&nalgebra::Vector3::new(0.0f32, 0.014, 0.0));
    }
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">KISS3D WIREFRAME MESH TERRAIN</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="kiss3d-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>window.add_cube(); c.prepend_to_local_rotation()</span>
      <span>nalgebra Linear Algebra Integration · Minimalist 3D Graphics in Pure Rust</span>
    </div>
    """

    custom_js = """
    function drawKiss3d() {
      const c = document.getElementById('kiss3d-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const rows = 14; const cols = 20;
      const ox = W / 2; const oy = H / 2 - 20;

      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.2;

      // Isometric 3D terrain grid wireframe
      for (let r = 0; r < rows; r++) {
        ctx.beginPath();
        for (let cl = 0; cl < cols; cl++) {
          const isoX = (cl - cols/2) * 24 - (r - rows/2) * 14;
          const height = Math.sin(r * 0.4) * Math.cos(cl * 0.3) * 35;
          const isoY = (cl - cols/2) * 10 + (r - rows/2) * 12 - height;

          const px = ox + isoX;
          const py = oy + isoY;
          if (cl === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      for (let cl = 0; cl < cols; cl++) {
        ctx.beginPath();
        for (let r = 0; r < rows; r++) {
          const isoX = (cl - cols/2) * 24 - (r - rows/2) * 14;
          const height = Math.sin(r * 0.4) * Math.cos(cl * 0.3) * 35;
          const isoY = (cl - cols/2) * 10 + (r - rows/2) * 12 - height;

          const px = ox + isoX;
          const py = oy + isoY;
          if (r === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }
    }

    window.addEventListener('load', () => { drawKiss3d(); });
    window.addEventListener('resize', drawKiss3d);
    """

    html = render_lang_page("Rust", "kiss3d", "Rust VIsualization", 'cargo add kiss3d nalgebra',
                            "https://github.com/sebcrozet/kiss3d",
                            "Minimalist 3D graphics and collision visualization engine in Rust.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("kiss3d", html)

# 6. PETGRAPH
def build_petgraph():
    paradigms = [{
        "tag": "01 / GRAPH ALGORITHMS",
        "title": "A* Pathfinding & Compressed Sparse Adjacency",
        "subtitle": "petgraph is Rust's premier graph data structure library, featuring adjacency list Graph, matrix GraphMap, and zero-allocation A* solvers.",
        "math_desc": "A* search heuristic evaluation: $f(n) = g(n) + h(n)$ where $h(n) = \\|\\mathbf{x}_n - \\mathbf{x}_{\\text{goal}}\\|_2$ guarantees admissible optimal path discovery.",
        "math_formula": "d(v) = \\min_{u \\in N(v)} \\{ d(u) + w(u,v) + h(v) \\}",
        "time_complexity": "O(E + V log V) with binary heap priority queue",
        "space_complexity": "O(V + E) compact vector memory",
        "enterprise_use": "Automated logistics autonomous fleet dispatch, high-frequency network packet route optimization.",
        "strengths": "Zero-overhead performance; generic node/edge weights; comprehensive algorithmic suite.",
        "tradeoffs": "Does not include built-in rendering; requires pairing with Canvas/SVG/Wasm.",
        "metrics": [
            {"label": "Data Model", "val": "Graph<N, E>", "sub": "Vector of Nodes"},
            {"label": "Shortest Path", "val": "A* / Dijkstra", "sub": "Optimal O(E log V)"},
            {"label": "Memory", "val": "Contiguous Vec", "sub": "Zero Pointer Chasing"},
            {"label": "License", "val": "MIT / Apache 2.0", "sub": "Rust Standard"}
        ],
        "code": """use petgraph::algo::astar;
use petgraph::graph::NodeIndex;
use petgraph::Graph;

let mut g = Graph::<&str, f32>::new();
let a = g.add_node("Depot_Alpha");
let b = g.add_node("Transit_Bravo");
let c = g.add_node("Terminal_Charlie");

g.add_edge(a, b, 4.5);
g.add_edge(b, c, 3.2);

let path = astar(&g, a, |finish| finish == c, |e| *e.weight(), |_| 0.0);"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">PETGRAPH A* PATHFINDER SOLVER</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="petgraph-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>astar(&graph, start, \|finish\| finish == goal, \|e\| *e.weight(), heuristic)</span>
      <span>Rust Vector-Backed Adjacency Lists · Optimal Admissible Heuristic Routing</span>
    </div>
    """

    custom_js = """
    function drawPetgraph() {
      const c = document.getElementById('petgraph-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const nodes = [
        { id: 0, x: 80, y: H/2, label: 'Depot Alpha' },
        { id: 1, x: 220, y: H/2 - 70, label: 'Hub Bravo' },
        { id: 2, x: 220, y: H/2 + 70, label: 'Hub Charlie' },
        { id: 3, x: 380, y: H/2 - 60, label: 'Relay Delta' },
        { id: 4, x: 380, y: H/2 + 60, label: 'Relay Echo' },
        { id: 5, x: 520, y: H/2, label: 'Goal Terminal' }
      ];

      const edges = [
        [0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [1, 4]
      ];
      const optimalPath = [0, 1, 3, 5];

      // Draw Edges
      edges.forEach(e => {
        const u = nodes[e[0]];
        const v = nodes[e[1]];
        const isOpt = (optimalPath.includes(e[0]) && optimalPath.includes(e[1]) && Math.abs(optimalPath.indexOf(e[0]) - optimalPath.indexOf(e[1])) === 1);

        ctx.strokeStyle = isOpt ? '#00e676' : 'rgba(255,255,255,0.15)';
        ctx.lineWidth = isOpt ? 3 : 1.2;
        ctx.beginPath(); ctx.moveTo(u.x, u.y); ctx.lineTo(v.x, v.y); ctx.stroke();
      });

      // Draw Nodes
      nodes.forEach(n => {
        const isOpt = optimalPath.includes(n.id);
        ctx.fillStyle = isOpt ? '#00e676' : '#00e5ff';
        ctx.beginPath(); ctx.arc(n.x, n.y, 6, 0, 2*Math.PI); ctx.fill();
        ctx.fillStyle = '#fff';
        ctx.font = '10px JetBrains Mono';
        ctx.fillText(n.label, n.x - 20, n.y - 12);
      });
    }

    window.addEventListener('load', () => { drawPetgraph(); });
    window.addEventListener('resize', drawPetgraph);
    """

    html = render_lang_page("Rust", "petgraph", "Rust VIsualization", 'cargo add petgraph',
                            "https://docs.rs/petgraph",
                            "Graph data structures and algorithmic pathfinding library in Rust.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("petgraph", html)

# 7. GEO
def build_geo():
    paradigms = [{
        "tag": "01 / COMPUTATIONAL GEOMETRY",
        "title": "Geospatial Polygon Boolean Operations in Pure Rust",
        "subtitle": "Implements pure Rust computational geometry routines: polygon clipping, convex hull algorithms, and GeoJSON conversions.",
        "math_desc": "Vatti polygon clipping intersection: sweeping line state determining edge entry/exit across winding numbers.",
        "math_formula": "\\text{Winding}(p) = \\frac{1}{2\\pi} \\oint_C \\frac{x dy - y dx}{x^2 + y^2}",
        "time_complexity": "O(N log N) Bentley-Ottmann sweep line",
        "space_complexity": "O(N) edge segment search tree",
        "enterprise_use": "Autonomous drone geofencing corridor validation, satellite land-use polygon union.",
        "strengths": "Pure Rust; zero C/GEOS dynamic link dependencies; thread-safe concurrent geometry processing.",
        "tradeoffs": "Ecosystem is younger than mature C++ GEOS/Shapely stacks.",
        "metrics": [
            {"label": "Standard", "val": "OGC Simple Features", "sub": "Pure Rust"},
            {"label": "Safety", "val": "Zero Buffer Overflow", "sub": "Memory Guard"},
            {"label": "Threading", "val": "Rayon Parallel", "sub": "Multi-Core Geo"},
            {"label": "License", "val": "MIT / Apache 2.0", "sub": "Georust"}
        ],
        "code": """use geo::{Polygon, MultiPolygon};
use geo::boolean_ops::BooleanOps;

let poly_a: Polygon<f64> = /* zone A */;
let poly_b: Polygon<f64> = /* zone B */;

// Compute geometric intersection
let intersection: MultiPolygon<f64> = poly_a.intersection(&poly_b);"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">GEO PURE RUST BOOLEAN CLIPPING</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="geo-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>poly_a.intersection(&poly_b) · geo::boolean_ops::BooleanOps</span>
      <span>Pure Rust Sweep-Line Polygon Clipping · Zero C/GEOS Shared Library Dependencies</span>
    </div>
    """

    custom_js = """
    function drawGeoRust() {
      const c = document.getElementById('geo-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const cx = W / 2; const cy = H / 2;

      // Polygon A (Green)
      ctx.fillStyle = 'rgba(0, 230, 118, 0.25)';
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(cx - 50, cy, 110, 0, 2*Math.PI);
      ctx.fill();
      ctx.stroke();

      // Polygon B (Cyan)
      ctx.fillStyle = 'rgba(0, 229, 255, 0.25)';
      ctx.strokeStyle = '#00e5ff';
      ctx.beginPath();
      ctx.arc(cx + 50, cy, 110, 0, 2*Math.PI);
      ctx.fill();
      ctx.stroke();

      // Highlight Intersection Area (Gold)
      ctx.fillStyle = 'rgba(243, 207, 101, 0.4)';
      ctx.beginPath();
      ctx.arc(cx - 50, cy, 110, -Math.PI/3, Math.PI/3);
      ctx.arc(cx + 50, cy, 110, 2*Math.PI/3, 4*Math.PI/3);
      ctx.closePath();
      ctx.fill();

      ctx.fillStyle = '#fff';
      ctx.font = '11px JetBrains Mono';
      ctx.fillText('Zone A (Geofence)', cx - 140, cy - 120);
      ctx.fillText('Zone B (Flight Path)', cx + 40, cy - 120);
      ctx.fillStyle = '#f3cf65';
      ctx.fillText('Intersection Corridors (A ∩ B)', cx - 80, cy + 140);
    }

    window.addEventListener('load', () => { drawGeoRust(); });
    window.addEventListener('resize', drawGeoRust);
    """

    html = render_lang_page("Rust", "geo", "Rust VIsualization", 'cargo add geo',
                            "https://georust.org",
                            "Geospatial algorithms and computational polygon operations in pure Rust.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("geo", html)

# 8. LEPTOS
def build_leptos():
    paradigms = [{
        "tag": "01 / FINE-GRAINED REACTIVITY",
        "title": "Fine-Grained Reactive Signals & Zero Virtual-DOM Overhead",
        "subtitle": "Leptos uses fine-grained reactive primitives (signals) that mutate exact DOM nodes directly without virtual DOM reconciliation overhead.",
        "math_desc": "Signal reactivity equation: $S(t) = \\text{Signal}(v)$ where subscriptions form fine-grained closures executed only when value $v$ mutates.",
        "math_formula": "\\Delta \\text{DOM} = \\{ \\text{Node}_i \\mid S_i \\in \\text{DirtySignals} \\} \\quad (\\text{Zero V-DOM Diffing})",
        "time_complexity": "O(1) direct pointer DOM update per signal",
        "space_complexity": "O(S) signal subscription registry",
        "enterprise_use": "High-throughput operational monitoring dashboards, real-time edge telemetry web consoles.",
        "strengths": "Fastest full-stack Rust web framework; SSR + hydration; ultra-compact WebAssembly footprint.",
        "tradeoffs": "Requires mastering Rust ownership with reactive closures (`move || ...`).",
        "metrics": [
            {"label": "Reactivity", "val": "Fine-Grained Signals", "sub": "Zero Virtual-DOM"},
            {"label": "Hydration", "val": "Isomorphic Wasm", "sub": "Instant TTI"},
            {"label": "Performance", "val": "Top 3 World Web", "sub": "Krausest Benchmark"},
            {"label": "License", "val": "MIT", "sub": "Leptos Community"}
        ],
        "code": """use leptos::*;

#[component]
pub fn MetricMonitor() -> impl IntoView {
    let (count, set_count) = create_signal(0);

    view! {
        <div class="leptos-card">
            <h2>"Leptos Fine-Grained Reactive Engine"</h2>
            <button on:click=move |_| set_count.update(|n| *n += 1)>
                "Direct Increment: " {count}
            </button>
        </div>
    }
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">LEPTOS FINE-GRAINED SIGNALS ACTIVE</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#070b09; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px;">
      <div style="background:#0e1712; border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:24px; max-width:480px; width:100%; text-align:center;">
        <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--gold-bright);">create_signal(0) Fine-Grained Reactive DOM Node</div>
        <div style="font-size:3.5rem; font-family:'Newsreader', serif; font-weight:700; color:#fff; margin:12px 0;" id="leptos-counter">0</div>
        <div style="display:flex; justify-content:center; gap:12px;">
          <button class="btn-action" onclick="leptosDec()" style="font-size:1.1rem; padding:8px 18px;">- Dec</button>
          <button class="btn-action" onclick="leptosInc()" style="font-size:1.1rem; padding:8px 18px; background:rgba(0,230,118,0.2); border-color:#00e676; color:#00e676;">+ Inc</button>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>view! { <button on:click=move \|_\| set_count.update(\|n\| *n += 1)> }</span>
      <span>Zero-Cost Reactive Signals · Microsecond DOM Node Direct Modification</span>
    </div>
    """

    custom_js = """
    let lepCount = 0;
    function leptosInc() { lepCount++; document.getElementById('leptos-counter').innerText = lepCount; }
    function leptosDec() { lepCount--; document.getElementById('leptos-counter').innerText = lepCount; }
    """

    html = render_lang_page("Rust", "leptos", "Rust VIsualization", 'cargo add leptos',
                            "https://leptos.dev",
                            "Full-stack fine-grained reactive web framework compiling to WebAssembly.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("leptos", html)

if __name__ == "__main__":
    build_rust_all()
