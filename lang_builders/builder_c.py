"""
Builder for C Visualization Libraries:
Raylib (C), Nuklear (C), Cairo (C), Graphviz (libgvc C), Plplot (C), OpenGL (C), SDL2 (C)
"""
import os
from .common_frame import render_lang_page

BASE_DIR = "/run/media/ml/Storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/C Visualization"

def write_tool(folder_name, html):
    target_dir = os.path.join(BASE_DIR, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    clean_name = folder_name.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [✓] C :: {folder_name:<30} -> Studio Built ({len(html)/1024:.1f} KB)")

def build_c_all():
    build_raylib()
    build_nuklear()
    build_cairo()
    build_graphviz_c()
    build_plplot()
    build_opengl_c()
    build_sdl2()

# 1. RAYLIB
def build_raylib():
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    paradigms = [{
        "tag": "01 / SIMPLE C GRAPHICS & WASM",
        "title": "Minimalist C Graphics & Procedural Voxel Engine",
        "subtitle": "Raylib provides a simple, clean C99 API for 2D/3D graphics and games that compiles directly into standalone HTML via Emscripten.",
        "math_desc": "3D Orthographic & Perspective camera frustum transformations executed via modern OpenGL 3.3/ES 2.0.",
        "math_formula": "\\mathbf{v}_{\\text{screen}} = \\text{ViewportTransform}(\\mathbf{P} \\times \\mathbf{V} \\times \\mathbf{M} \\times \\mathbf{v}_{\\text{local}})",
        "time_complexity": "O(N) hardware GPU drawing loop (60 FPS)",
        "space_complexity": "O(1) memory footprint (clean C allocation)",
        "enterprise_use": "Interactive procedural CAD viewers, lightweight embedded medical monitor graphics.",
        "strengths": "Simplest C API in existence; zero external dependencies; compiles to web HTML in one command.",
        "tradeoffs": "Intentionally avoids complex enterprise engine bloat (e.g., no built-in visual editor).",
        "metrics": [
            {"label": "Standard", "val": "C99 Standard", "sub": "Zero-Bloat"},
            {"label": "Wasm Support", "val": "Native Emscripten", "sub": "Single HTML"},
            {"label": "Performance", "val": "60 - 120 FPS", "sub": "Direct OpenGL"},
            {"label": "License", "val": "zlib/libpng", "sub": "Ramon Santamaria"}
        ],
        "code": """#include "raylib.h"

int main(void) {
    InitWindow(800, 600, "Raylib: C99 Interactive Studio");
    Camera3D camera = { 0 };
    camera.position = (Vector3){ 0.0f, 10.0f, 10.0f };
    camera.target = (Vector3){ 0.0f, 0.0f, 0.0f };
    camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };
    camera.fovy = 45.0f;
    camera.projection = CAMERA_PERSPECTIVE;

    SetTargetFPS(60);
    while (!WindowShouldClose()) {
        UpdateCamera(&camera, CAMERA_ORBITAL);
        BeginDrawing();
            ClearBackground((Color){ 4, 7, 5, 255 });
            BeginMode3D(camera);
                DrawCube((Vector3){ 0.0f, 0.0f, 0.0f }, 2.0f, 2.0f, 2.0f, (Color){ 0, 230, 118, 255 });
                DrawCubeWires((Vector3){ 0.0f, 0.0f, 0.0f }, 2.0f, 2.0f, 2.0f, WHITE);
            EndMode3D();
        EndDrawing();
    }
    CloseWindow();
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676; box-shadow:0 0 8px #00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">RAYLIB C99 3D WASM ACTIVE</span>
      </div>
    </div>
    <div class="canvas-body" id="raylib-stage" style="width:100%; height:100%; min-height:480px; position:relative;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>BeginMode3D(camera); DrawCube(); EndMode3D();</span>
      <span>C99 Clean Architecture · Single-Command Emscripten HTML Compilation</span>
    </div>
    """

    custom_js = """
    let rlScene, rlCamera, rlRenderer, rlCube;
    function initRaylibThree() {
      const el = document.getElementById('raylib-stage');
      if (!el) return;

      rlScene = new THREE.Scene();
      rlScene.background = new THREE.Color(0x040705);

      rlCamera = new THREE.PerspectiveCamera(45, el.clientWidth / el.clientHeight, 0.1, 1000);
      rlCamera.position.set(5, 5, 5);
      rlCamera.lookAt(0, 0, 0);

      rlRenderer = new THREE.WebGLRenderer({ antialias: true });
      rlRenderer.setSize(el.clientWidth, el.clientHeight);
      rlRenderer.setPixelRatio(window.devicePixelRatio);
      el.appendChild(rlRenderer.domElement);

      const light = new THREE.DirectionalLight(0x00e676, 1.2);
      light.position.set(5, 10, 5);
      rlScene.add(light);
      rlScene.add(new THREE.AmbientLight(0xffffff, 0.3));

      const geom = new THREE.BoxGeometry(2, 2, 2);
      const mat = new THREE.MeshStandardMaterial({ color: 0x00e676, roughness: 0.3 });
      rlCube = new THREE.Mesh(geom, mat);
      rlScene.add(rlCube);

      function animate() {
        requestAnimationFrame(animate);
        rlCube.rotation.y += 0.01;
        rlCube.rotation.x += 0.005;
        rlRenderer.render(rlScene, rlCamera);
      }
      animate();
    }

    window.addEventListener('load', () => { setTimeout(initRaylibThree, 100); });
    """

    html = render_lang_page("C", "Raylib", "C Visualization", 'apt-get install libraylib-dev',
                            "https://www.raylib.com",
                            "Simple and easy-to-use C99 graphics library compiling directly to HTML5.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Raylib", html)

# 2. NUKLEAR
def build_nuklear():
    paradigms = [{
        "tag": "01 / ANSI C SINGLE-HEADER GUI",
        "title": "Zero-Dependency ANSI C Immediate-Mode Interface",
        "subtitle": "Nuklear is a single-header ANSI C immediate-mode GUI with zero runtime dependencies and total memory control.",
        "math_desc": "Immediate mode draw command queue: generates contiguous buffers of vertex and index primitives for arbitrary graphics backends.",
        "math_formula": "\\text{CommandBuffer} = \\sum \\langle \\text{nk_command}, \\text{rect}, \\text{color} \\rangle",
        "time_complexity": "O(W) linear widget loop",
        "space_complexity": "O(1) stack or fixed buffer memory",
        "enterprise_use": "Embedded medical devices, avionics cockpit instrumentation user interfaces.",
        "strengths": "Single header (`nuklear.h`); zero heap allocation mode; compiles on any C89 compiler.",
        "tradeoffs": "Developer must provide their own font baking and platform window backend.",
        "metrics": [
            {"label": "Standard", "val": "ANSI C89", "sub": "Universal Port"},
            {"label": "Packaging", "val": "Single Header", "sub": "nuklear.h"},
            {"label": "Memory", "val": "Zero-Heap Mode", "sub": "Fixed Buffer"},
            {"label": "License", "val": "MIT / Public Domain", "sub": "Micha Mettke"}
        ],
        "code": """#define NK_INCLUDE_FIXED_TYPES
#define NK_IMPLEMENTATION
#include "nuklear.h"

void RenderNuklearUI(struct nk_context *ctx) {
    if (nk_begin(ctx, "Turbine Governor", nk_rect(50, 50, 240, 200),
        NK_WINDOW_BORDER|NK_WINDOW_MOVABLE|NK_WINDOW_TITLE)) {
        static int pressure = 65;
        nk_layout_row_dynamic(ctx, 30, 1);
        nk_property_int(ctx, "Fuel Pressure (PSI):", 0, &pressure, 100, 1, 1);
    }
    nk_end(ctx);
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">NUKLEAR ANSI C GUI RUNTIME</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#070b09; display:flex; align-items:center; justify-content:center;">
      <div style="width:380px; background:#18201a; border:1px solid #334539; border-radius:4px; padding:16px; box-shadow:0 10px 25px rgba(0,0,0,0.8);">
        <div style="font-family:var(--font-mono); font-size:0.75rem; color:#f3cf65; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px; margin-bottom:12px;">
          nuklear.h: ANSI C Fixed-Buffer Governor
        </div>
        <div style="display:flex; flex-direction:column; gap:10px;">
          <div style="font-size:0.75rem; color:#cbd5e1;">Valve Actuator Position: 65%</div>
          <div style="height:8px; background:#040705; border-radius:4px; overflow:hidden;">
            <div style="width:65%; height:100%; background:#00e676;"></div>
          </div>
          <button class="btn-action" style="background:#f3cf65; color:#040705; font-weight:700; width:100%; justify-content:center; padding:6px; border:none;">
            nk_button_label(ctx, "Calibrate Valve")
          </button>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>nk_begin(ctx, 'Governor', nk_rect(), flags); nk_property_int(); nk_end(ctx)</span>
      <span>Single-Header ANSI C89 Immediate Mode · Zero Heap Allocation Mode Available</span>
    </div>
    """

    custom_js = ""

    html = render_lang_page("C", "Nuklear", "C Visualization", '# header-only nuklear.h',
                            "https://github.com/Immediate-Mode-UI/Nuklear",
                            "Single-header ANSI C immediate-mode graphical user interface library.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Nuklear", html)

# 3. CAIRO
def build_cairo():
    paradigms = [{
        "tag": "01 / SUB-PIXEL 2D VECTOR",
        "title": "Sub-Pixel Anti-Aliased 2D Vector Drawing in C",
        "subtitle": "Cairo is the foundational 2D vector graphics library behind GNOME, GTK, and Firefox, supporting PDF, PostScript, and SVG backends.",
        "math_desc": "Sub-pixel anti-aliasing via trapezoid rasterization: decomposes cubic Bézier splines into horizontal trapezoidal scanlines.",
        "math_formula": "A(T) = \\frac{1}{2} (b_1 + b_2) h \\quad \\xrightarrow{\\text{coverage}} \\text{ColorBlending}",
        "time_complexity": "O(N) vector spline path rasterization",
        "space_complexity": "O(1) image surface buffer",
        "enterprise_use": "High-precision cartographic vector print production, architectural CAD SVG export.",
        "strengths": "Pixel-perfect consistency across vector and raster backends; gold standard for anti-aliasing.",
        "tradeoffs": "CPU-bound rasterization compared to hardware GPU shader pipelines.",
        "metrics": [
            {"label": "Standard", "val": "PostScript / PDF", "sub": "Vector Target"},
            {"label": "Adoption", "val": "GTK / Firefox Core", "sub": "Linux Standard"},
            {"label": "Precision", "val": "Sub-pixel (1/256)", "sub": "Anti-Aliased"},
            {"label": "License", "val": "LGPL / MPL", "sub": "Universal"}
        ],
        "code": """#include <cairo/cairo.h>

int main() {
    cairo_surface_t *surface = cairo_image_surface_create(CAIRO_FORMAT_ARGB32, 640, 480);
    cairo_t *cr = cairo_create(surface);

    cairo_set_source_rgb(cr, 0.02, 0.03, 0.02);
    cairo_paint(cr);

    cairo_set_source_rgb(cr, 0.0, 0.9, 0.4);
    cairo_set_line_width(cr, 3.0);
    cairo_arc(cr, 320.0, 240.0, 100.0, 0, 2 * 3.14159);
    cairo_stroke(cr);

    cairo_surface_write_to_png(surface, "cairo_art.png");
    cairo_destroy(cr);
    cairo_surface_destroy(surface);
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">CAIRO 2D VECTOR ENGINE</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="cairo-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>cairo_arc(cr, cx, cy, r, 0, 2*pi); cairo_stroke(cr)</span>
      <span>Sub-Pixel Anti-Aliased Vector Graphics · PostScript & PDF Compliant</span>
    </div>
    """

    custom_js = """
    function drawCairo() {
      const c = document.getElementById('cairo-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const cx = W / 2; const cy = H / 2;

      // Concentric anti-aliased geometric vector arcs
      for (let i = 1; i <= 6; i++) {
        ctx.strokeStyle = (i % 2 === 0) ? '#00e676' : '#00e5ff';
        ctx.lineWidth = 2.0;
        ctx.beginPath();
        ctx.arc(cx, cy, i * 28, 0, Math.PI * 1.5);
        ctx.stroke();
      }

      ctx.strokeStyle = '#f3cf65';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(cx - 150, cy + 100);
      ctx.bezierCurveTo(cx - 50, cy - 80, cx + 50, cy + 80, cx + 150, cy - 100);
      ctx.stroke();
    }

    window.addEventListener('load', () => { drawCairo(); });
    window.addEventListener('resize', drawCairo);
    """

    html = render_lang_page("C", "Cairo", "C Visualization", 'apt-get install libcairo2-dev',
                            "https://www.cairographics.org",
                            "2D vector graphics library supporting multiple output devices.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Cairo", html)

# 4. GRAPHVIZ (C)
def build_graphviz_c():
    paradigms = [{
        "tag": "01 / NATIVE C GRAPH COMPILATION",
        "title": "Low-Level libgvc Graph Layout & Spline Routing",
        "subtitle": "Native C library interface (libgvc) behind Graphviz, generating hierarchical Sugiyama DAGs and spline routing.",
        "math_desc": "Bézier spline edge routing around obstacle bounding boxes using shortest paths in visibility graphs.",
        "math_formula": "\\min_{\\gamma} \\int_0^1 \\|\\gamma''(t)\\|^2 dt \\quad \\text{subject to } \\gamma(t) \\cap \\text{Obstacle} = \\emptyset",
        "time_complexity": "O(V \\cdot E) layered DAG layout heuristic",
        "space_complexity": "O(V + E) Agraph_t C struct graph",
        "enterprise_use": "Automated chip placement floorplanning, microkernel operating system process trees.",
        "strengths": "Fastest execution speed for Graphviz algorithms; native C memory layout.",
        "tradeoffs": "C memory lifecycle requires explicit `agclose()` and `gvFreeLayout()` calls.",
        "metrics": [
            {"label": "Library", "val": "libgvc C", "sub": "Native C Core"},
            {"label": "Algorithms", "val": "dot / neato / fdp", "sub": "Unified C API"},
            {"label": "Splines", "val": "Cubic Bézier", "sub": "Collision-Free"},
            {"label": "License", "val": "CPL / Eclipse", "sub": "Standard Core"}
        ],
        "code": """#include <gvc.h>

int main() {
    GVC_t *gvc = gvContext();
    Agraph_t *g = agopen("ProcessDAG", Agdirected, 0);

    Agnode_t *n1 = agnode(g, "Init_Core", 1);
    Agnode_t *n2 = agnode(g, "Scheduler", 1);
    agedge(g, n1, n2, 0, 1);

    gvLayout(gvc, g, "dot");
    gvRenderFilename(gvc, g, "svg", "process_tree.svg");

    gvFreeLayout(gvc, g);
    agclose(g);
    gvFreeContext(gvc);
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">LIBGVC NATIVE C GRAPH PIPELINE</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="gvc-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>gvLayout(gvc, g, 'dot'); gvRenderFilename('svg')</span>
      <span>Native C libgvc Engine · Spline Edge Obstacle Avoidance Optimization</span>
    </div>
    """

    custom_js = """
    function drawGvc() {
      const c = document.getElementById('gvc-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const nodes = [
        { label: 'init (PID 1)', x: W/2, y: 70 },
        { label: 'kthreadd', x: W/2 - 140, y: 190 },
        { label: 'systemd', x: W/2 + 140, y: 190 },
        { label: 'sshd', x: W/2 + 60, y: 310 },
        { label: 'nginx', x: W/2 + 220, y: 310 }
      ];

      // Edges
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      ctx.moveTo(W/2, 90); ctx.lineTo(W/2 - 140, 170);
      ctx.moveTo(W/2, 90); ctx.lineTo(W/2 + 140, 170);
      ctx.moveTo(W/2 + 140, 210); ctx.lineTo(W/2 + 60, 290);
      ctx.moveTo(W/2 + 140, 210); ctx.lineTo(W/2 + 220, 290);
      ctx.stroke();

      nodes.forEach(n => {
        ctx.fillStyle = '#0e1712';
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 1.8;
        ctx.strokeRect(n.x - 50, n.y - 18, 100, 36);
        ctx.fillRect(n.x - 50, n.y - 18, 100, 36);

        ctx.fillStyle = '#fff';
        ctx.font = '10px JetBrains Mono';
        ctx.textAlign = 'center';
        ctx.fillText(n.label, n.x, n.y + 4);
      });
    }

    window.addEventListener('load', () => { drawGvc(); });
    window.addEventListener('resize', drawGvc);
    """

    html = render_lang_page("C", "Graphviz (libgvc)", "C Visualization", 'apt-get install libgraphviz-dev',
                            "https://graphviz.org",
                            "Native C API for Graphviz layout engines and spline edge routing.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Graphviz", html)

# 5. PLPLOT
def build_plplot():
    paradigms = [{
        "tag": "01 / SCIENTIFIC C SURFACES",
        "title": "Scientific Multi-Color 3D Surface & Contour Plots",
        "subtitle": "PLplot is a venerable C scientific plotting library providing 3D surface meshes with hidden-line removal and cross-platform drivers.",
        "math_desc": "3D surface hidden-line elimination using Watkin's interval scanning algorithm across polygon edges.",
        "math_formula": "z = f(x,y) = \\frac{\\sin\\sqrt{x^2+y^2}}{\\sqrt{x^2+y^2}}",
        "time_complexity": "O(N^2 log N) depth-sorted polygon scan",
        "space_complexity": "O(N^2) grid elevation array",
        "enterprise_use": "Aerospace atmospheric pressure gradient contour mapping, antenna propagation patterns.",
        "strengths": "Ultra-lightweight; binds directly to C, Fortran, and Ada; supports vector SVG.",
        "tradeoffs": "Legacy API design originating in the early scientific computing era.",
        "metrics": [
            {"label": "Language", "val": "ANSI C Core", "sub": "Polyglot Bindings"},
            {"label": "Algorithms", "val": "Hidden-Line", "sub": "Depth Sorted"},
            {"label": "Drivers", "val": "SVG / Cairo / X11", "sub": "Vector Drivers"},
            {"label": "License", "val": "LGPL", "sub": "Scientific Standard"}
        ],
        "code": """#include <plplot/plplot.h>

int main(int argc, char *argv[]) {
    plsdev("svg");
    plsfnam("surface.svg");
    plinit();

    pladv(0);
    plvpor(0.1, 0.9, 0.1, 0.9);
    plwind(-1.0, 1.0, -1.0, 1.0);
    plbox("bcnst", 0.0, 0, "bcnst", 0.0, 0);

    plend();
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">PLPLOT SCIENTIFIC 3D MESH</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="plplot-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>plmesh(x, y, z, nx, ny, opt) · Hidden-Line Removal Algorithm</span>
      <span>Venerable Scientific C Plotting Library · Direct Vector Driver Output</span>
    </div>
    """

    custom_js = """
    function drawPlplot() {
      const c = document.getElementById('plplot-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const rows = 16; const cols = 22;
      const ox = W / 2; const oy = H / 2 - 20;

      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.2;

      for (let r = 0; r < rows; r++) {
        ctx.beginPath();
        for (let cl = 0; cl < cols; cl++) {
          const isoX = (cl - cols/2) * 20 - (r - rows/2) * 12;
          const dist = Math.hypot(cl - cols/2, r - rows/2) + 0.1;
          const height = (Math.sin(dist * 0.8) / dist) * 70;
          const isoY = (cl - cols/2) * 8 + (r - rows/2) * 10 - height;

          const px = ox + isoX;
          const py = oy + isoY;
          if (cl === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }
    }

    window.addEventListener('load', () => { drawPlplot(); });
    window.addEventListener('resize', drawPlplot);
    """

    html = render_lang_page("C", "PLplot", "C Visualization", 'apt-get install libplplot-dev',
                            "https://plplot.sourceforge.net",
                            "Scientific plotting library written in C for mathematical surface meshes.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("PLplot", html)

# 6. OPENGL (C)
def build_opengl_c():
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    paradigms = [{
        "tag": "01 / CORE PIPELINE SHADERS",
        "title": "Classic OpenGL Pipeline & Hardware Vertex Buffers in C",
        "subtitle": "The foundational industrial graphics standard: manages GPU context, GLSL shader programs, and Vertex Array Objects (VAO).",
        "math_desc": "Phong illumination reflection: $I = I_a k_a + I_d k_d (\\mathbf{L} \\cdot \\mathbf{N}) + I_s k_s (\\mathbf{R} \\cdot \\mathbf{V})^n$.",
        "math_formula": "\\mathbf{v}_{\\text{ndc}} = \\frac{\\mathbf{P} \\times \\mathbf{V} \\times \\mathbf{M} \\times \\mathbf{v}}{w}",
        "time_complexity": "O(V) hardware GPU parallel vertex stage",
        "space_complexity": "O(V) GL_ARRAY_BUFFER VBO allocation",
        "enterprise_use": "Automotive CAD solids rendering, aerospace cockpit synthetic vision displays.",
        "strengths": "Direct hardware driver access; supported on billions of devices world-wide.",
        "tradeoffs": "Verbose boilerplate requiring manual memory pointer arithmetic.",
        "metrics": [
            {"label": "Standard", "val": "OpenGL 3.3+ / ES", "sub": "Hardware Core"},
            {"label": "Shaders", "val": "GLSL Native", "sub": "Hardware Exec"},
            {"label": "Language", "val": "Pure C Driver", "sub": "Direct Khronos"},
            {"label": "License", "val": "Open Standard", "sub": "Khronos Group"}
        ],
        "code": """#include <GL/glew.h>
#include <GLFW/glfw3.h>

int main() {
    glfwInit();
    GLFWwindow* window = glfwCreateWindow(800, 600, "OpenGL Core in C", NULL, NULL);
    glfwMakeContextCurrent(window);
    glewInit();

    while (!glfwWindowShouldClose(window)) {
        glClearColor(0.02f, 0.03f, 0.02f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwTerminate();
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 8px #00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">OPENGL C CORE PIPELINE</span>
      </div>
    </div>
    <div class="canvas-body" id="opengl-stage" style="width:100%; height:100%; min-height:480px; position:relative;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>glDrawElements(GL_TRIANGLES, count, GL_UNSIGNED_INT, 0)</span>
      <span>Native Khronos OpenGL C Specification · Hardware Shader Rasterization</span>
    </div>
    """

    custom_js = """
    let glScene, glCamera, glRenderer, glMesh;
    function initGlThree() {
      const el = document.getElementById('opengl-stage');
      if (!el) return;

      glScene = new THREE.Scene();
      glScene.background = new THREE.Color(0x040705);

      glCamera = new THREE.PerspectiveCamera(45, el.clientWidth / el.clientHeight, 0.1, 1000);
      glCamera.position.set(0, 0, 7);

      glRenderer = new THREE.WebGLRenderer({ antialias: true });
      glRenderer.setSize(el.clientWidth, el.clientHeight);
      glRenderer.setPixelRatio(window.devicePixelRatio);
      el.appendChild(glRenderer.domElement);

      const light = new THREE.DirectionalLight(0x00e5ff, 1.5);
      light.position.set(5, 5, 5);
      glScene.add(light);
      glScene.add(new THREE.AmbientLight(0xffffff, 0.2));

      // Octahedron geometry
      const geom = new THREE.OctahedronGeometry(2.4, 0);
      const mat = new THREE.MeshStandardMaterial({
        color: 0x00e676,
        roughness: 0.2,
        metalness: 0.8
      });
      glMesh = new THREE.Mesh(geom, mat);
      glScene.add(glMesh);

      function animate() {
        requestAnimationFrame(animate);
        glMesh.rotation.y += 0.008;
        glMesh.rotation.x += 0.005;
        glRenderer.render(glScene, glCamera);
      }
      animate();
    }

    window.addEventListener('load', () => { setTimeout(initGlThree, 100); });
    """

    html = render_lang_page("C", "OpenGL", "C Visualization", 'apt-get install libgl-dev libglew-dev',
                            "https://www.opengl.org",
                            "The industry standard C graphics programming interface for GPU shaders.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("OpenGL", html)

# 7. SDL2
def build_sdl2():
    paradigms = [{
        "tag": "01 / HARDWARE BLITTING",
        "title": "Cross-Platform Hardware Blitting & Event Loop",
        "subtitle": "Simple DirectMedia Layer (SDL2) provides low-level hardware access to audio, keyboard, mouse, and 2D hardware-accelerated renderers.",
        "math_desc": "Hardware texture blitting: copies pixel rectangles between VRAM buffers via direct memory access (DMA).",
        "math_formula": "\\text{SDL\\_RenderCopy}(R, T, \\text{srcRect}, \\text{dstRect})",
        "time_complexity": "O(1) GPU DMA texture blit",
        "space_complexity": "O(W \\times H) texture memory footprint",
        "enterprise_use": "Flight simulator peripheral IO dashboards, cross-platform industrial telemetry consoles.",
        "strengths": "Runs on practically every computer architecture on Earth; compiles seamlessly to WebAssembly.",
        "tradeoffs": "Provides low-level primitives; requires implementing chart axes manually.",
        "metrics": [
            {"label": "Standard", "val": "ANSI C Core", "sub": "Hardware Abstraction"},
            {"label": "Platform", "val": "Every Known OS", "sub": "Native + Wasm"},
            {"label": "Industry", "val": "Valve / Steam Core", "sub": "Gaming Standard"},
            {"label": "License", "val": "zlib", "sub": "Sam Lantinga"}
        ],
        "code": """#include <SDL2/SDL.h>

int main() {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *win = SDL_CreateWindow("SDL2 C Telemetry", 100, 100, 640, 480, SDL_WINDOW_SHOWN);
    SDL_Renderer *ren = SDL_CreateRenderer(win, -1, SDL_RENDERER_ACCELERATED);

    SDL_SetRenderDrawColor(ren, 4, 7, 5, 255);
    SDL_RenderClear(ren);

    SDL_SetRenderDrawColor(ren, 0, 230, 118, 255);
    SDL_Rect r = { 280, 200, 80, 80 };
    SDL_RenderFillRect(ren, &r);

    SDL_RenderPresent(ren);
    SDL_Delay(3000);

    SDL_DestroyRenderer(ren);
    SDL_DestroyWindow(win);
    SDL_Quit();
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">SDL2 HARDWARE 2D BLITTER</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="sdl-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>SDL_RenderCopy(); SDL_RenderPresent(renderer)</span>
      <span>Simple DirectMedia Layer in C · Hardware Blitting & Event Polling</span>
    </div>
    """

    custom_js = """
    const sdlSprites = [];
    function initSdl() {
      sdlSprites.length = 0;
      for (let i = 0; i < 25; i++) {
        sdlSprites.push({
          x: 100 + Math.random() * 400,
          y: 100 + Math.random() * 260,
          w: 24, h: 24,
          vx: (Math.random() - 0.5) * 5,
          vy: (Math.random() - 0.5) * 5,
          col: (i % 2 === 0) ? '#00e676' : '#f3cf65'
        });
      }
    }
    initSdl();

    function sdlLoop() {
      const c = document.getElementById('sdl-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      sdlSprites.forEach(s => {
        s.x += s.vx;
        s.y += s.vy;
        if (s.x < 10 || s.x > W - 34) s.vx *= -1;
        if (s.y < 10 || s.y > H - 34) s.vy *= -1;

        ctx.fillStyle = s.col;
        ctx.fillRect(s.x, s.y, s.w, s.h);
        ctx.strokeStyle = '#fff';
        ctx.strokeRect(s.x, s.y, s.w, s.h);
      });

      requestAnimationFrame(sdlLoop);
    }

    window.addEventListener('load', () => { requestAnimationFrame(sdlLoop); });
    """

    html = render_lang_page("C", "SDL2", "C Visualization", 'apt-get install libsdl2-dev',
                            "https://www.libsdl.org",
                            "Simple DirectMedia Layer in C for hardware graphics and event loops.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("SDL2", html)

if __name__ == "__main__":
    build_c_all()
