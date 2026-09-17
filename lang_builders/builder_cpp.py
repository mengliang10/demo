"""
Builder for C++ Visualization Libraries:
VTK (C++), Dear ImGui, Magnum, matplotlib-cpp, Qt Charts, OpenSceneGraph, OGDF, Ogre3D
"""
import os
from .common_frame import render_lang_page

BASE_DIR = "/run/media/ml/Storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/C Plus Plus Visualization"

def write_tool(folder_name, html):
    target_dir = os.path.join(BASE_DIR, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    clean_name = folder_name.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_").replace("+", "p")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [✓] C++ :: {folder_name:<30} -> Studio Built ({len(html)/1024:.1f} KB)")

def build_cpp_all():
    build_vtk_cpp()
    build_imgui()
    build_magnum()
    build_matplotlib_cpp()
    build_qt_charts()
    build_osg()
    build_ogdf()
    build_ogre3d()

# 1. VTK (C++)
def build_vtk_cpp():
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    paradigms = [{
        "tag": "01 / NATIVE C++ PIPELINE",
        "title": "Industrial 3D Finite Element & Volumetric Pipeline in C++",
        "subtitle": "VTK's native C++ pipeline connects data sources, algorithmic filters, and hardware OpenGL mappers via demand-driven execution.",
        "math_desc": "Marching cubes isosurface triangulation: interpolates vertex positions along cube edges where scalar field $S(x,y,z) = c$.",
        "math_formula": "\\mathbf{P}_{\\text{iso}} = \\mathbf{P}_1 + \\frac{c - S_1}{S_2 - S_1} (\\mathbf{P}_2 - \\mathbf{P}_1)",
        "time_complexity": "O(N) voxel marching cubes pass",
        "space_complexity": "O(N) vtkPolyData vertex buffer in memory",
        "enterprise_use": "Aerospace wind tunnel CFD simulations, medical CT/MRI volumetric multi-planar re-slicing.",
        "strengths": "The global industrial standard for high-performance 3D scientific visualization; handles 100M+ elements.",
        "tradeoffs": "C++ memory management requires understanding VTK smart pointers (`vtkSmartPointer<T>`).",
        "metrics": [
            {"label": "Core Engine", "val": "Native C++ / OpenGL", "sub": "Hardware Raytrace"},
            {"label": "Scale", "val": "100M+ Elements", "sub": "Out-of-Core"},
            {"label": "Pipeline", "val": "Demand-Driven", "sub": "Modified Time (MTime)"},
            {"label": "License", "val": "BSD 3-Clause", "sub": "Kitware Industrial"}
        ],
        "code": """#include <vtkSmartPointer.h>
#include <vtkSphereSource.h>
#include <vtkPolyDataMapper.h>
#include <vtkActor.h>
#include <vtkRenderer.h>
#include <vtkRenderWindow.h>

int main(int argc, char* argv[]) {
    auto sphere = vtkSmartPointer<vtkSphereSource>::New();
    sphere->SetRadius(5.0);
    sphere->SetThetaResolution(64);

    auto mapper = vtkSmartPointer<vtkPolyDataMapper>::New();
    mapper->SetInputConnection(sphere->GetOutputPort());

    auto actor = vtkSmartPointer<vtkActor>::New();
    actor->SetMapper(mapper);

    auto renderer = vtkSmartPointer<vtkRenderer>::New();
    renderer->AddActor(actor);
    renderer->SetBackground(0.02, 0.03, 0.02);

    auto renWin = vtkSmartPointer<vtkRenderWindow>::New();
    renWin->AddRenderer(renderer);
    renWin->Render();
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676; box-shadow:0 0 8px #00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">VTK C++ 3D PIPELINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="toggleVtkWire()" id="btn-vtk-wire" style="font-size:0.7rem; padding:3px 8px;">Wireframe</button>
      </div>
    </div>
    <div class="canvas-body" id="vtk-cpp-stage" style="width:100%; height:100%; min-height:480px; position:relative;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>vtkSmartPointer<vtkActor>::New() · OpenGL Hardware Shaders</span>
      <span>C++ Native Visualization Toolkit · Demand-Driven Pipeline Architecture</span>
    </div>
    """

    custom_js = """
    let vtkScene, vtkCamera, vtkRenderer, vtkMesh;
    let vtkWire = false;

    function initVtkCppThree() {
      const el = document.getElementById('vtk-cpp-stage');
      if (!el) return;

      vtkScene = new THREE.Scene();
      vtkScene.background = new THREE.Color(0x040705);

      vtkCamera = new THREE.PerspectiveCamera(45, el.clientWidth / el.clientHeight, 0.1, 1000);
      vtkCamera.position.set(0, 8, 16);
      vtkCamera.lookAt(0, 0, 0);

      vtkRenderer = new THREE.WebGLRenderer({ antialias: true });
      vtkRenderer.setSize(el.clientWidth, el.clientHeight);
      vtkRenderer.setPixelRatio(window.devicePixelRatio);
      el.appendChild(vtkRenderer.domElement);

      const light = new THREE.DirectionalLight(0x00e676, 1.2);
      light.position.set(10, 15, 10);
      vtkScene.add(light);
      vtkScene.add(new THREE.AmbientLight(0xffffff, 0.3));

      // Torus knot geometry
      const geom = new THREE.TorusKnotGeometry(4.0, 1.2, 100, 24);
      const mat = new THREE.MeshStandardMaterial({
        color: 0x00e676,
        roughness: 0.3,
        metalness: 0.5,
        wireframe: false
      });
      vtkMesh = new THREE.Mesh(geom, mat);
      vtkScene.add(vtkMesh);

      function animate() {
        requestAnimationFrame(animate);
        vtkMesh.rotation.y += 0.005;
        vtkRenderer.render(vtkScene, vtkCamera);
      }
      animate();
    }

    function toggleVtkWire() {
      vtkWire = !vtkWire;
      if (vtkMesh) vtkMesh.material.wireframe = vtkWire;
      document.getElementById('btn-vtk-wire').innerText = vtkWire ? 'Solid' : 'Wireframe';
    }

    window.addEventListener('load', () => { setTimeout(initVtkCppThree, 100); });
    """

    html = render_lang_page("C++", "VTK (C++)", "C Plus Plus Visualization", 'vcpkg install vtk',
                            "https://vtk.org",
                            "The industrial gold standard C++ visualization toolkit for 3D meshes and CFD.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("VTK", html)

# 2. DEAR IMGUI
def build_imgui():
    paradigms = [{
        "tag": "01 / IMMEDIATE MODE TOOLKIT",
        "title": "Bloat-Free Immediate-Mode Game Engine Tooling",
        "subtitle": "Dear ImGui compiles ultra-fast debug tooling and telemetry panels into game engines and real-time graphics pipelines.",
        "math_desc": "Immediate mode clipping rect intersection: clips widget rendering commands against active parent window viewport.",
        "math_formula": "\\text{ClipRect} = [\\max(x_1, x_w), \\max(y_1, y_w), \\min(x_2, x_w + w), \\min(y_2, y_w + h)]",
        "time_complexity": "O(W) per-frame immediate tessellation (144 FPS)",
        "space_complexity": "O(1) memory overhead; zero allocated objects",
        "enterprise_use": "AAA game engine level editors, self-driving automotive simulation telemetry consoles.",
        "strengths": "Fastest C++ GUI library; zero dependencies; compiles directly to WebAssembly via Emscripten.",
        "tradeoffs": "Designed for internal developer tooling rather than consumer-facing styled apps.",
        "metrics": [
            {"label": "Style", "val": "Immediate Mode", "sub": "Bloat-Free"},
            {"label": "Frame Rate", "val": "144+ FPS", "sub": "Zero Allocation"},
            {"label": "Adoption", "val": "AAA Gaming Standard", "sub": "Unreal / Unity"},
            {"label": "License", "val": "MIT", "sub": "Omar Cornut"}
        ],
        "code": """#include "imgui.h"

void RenderTelemetryDashboard() {
    ImGui::Begin("Propulsion Systems Telemetry");
    static float core_temp = 85.4f;
    static float thrust_vector = 104.2f;

    ImGui::SliderFloat("Core Temperature (C)", &core_temp, 20.0f, 180.0f);
    ImGui::SliderFloat("Thrust Vector (kN)", &thrust_vector, 0.0f, 250.0f);

    ImGui::Text("Turbine Efficiency: %.2f%%", (thrust_vector / core_temp) * 85.0f);
    ImGui::End();
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">DEAR IMGUI WASM ACTIVE</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:20px; background:#070b09; display:flex; align-items:center; justify-content:center;">
      <div style="width:480px; background:#18201a; border:1px solid #334539; border-radius:4px; box-shadow:0 10px 25px rgba(0,0,0,0.8); overflow:hidden;">
        <div style="background:#222f26; padding:6px 10px; font-family:var(--font-mono); font-size:0.75rem; color:#f3cf65; display:flex; justify-content:space-between;">
          <span>Dear ImGui: Subsystem Telemetry</span>
          <span>_ □ ✕</span>
        </div>
        <div style="padding:14px; display:flex; flex-direction:column; gap:12px;">
          <div>
            <label style="font-size:0.75rem; color:#cbd5e1; display:block; margin-bottom:4px;">ImGui::SliderFloat("Core Temp")</label>
            <input type="range" id="imgui-temp" min="40" max="140" value="85" oninput="drawImGuiPlot()" style="width:100%;">
          </div>
          <div style="height:120px; background:#040705; border:1px solid rgba(255,255,255,0.08); border-radius:4px;">
            <canvas id="imgui-canvas" style="width:100%; height:100%;"></canvas>
          </div>
        </div>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>ImGui::Begin('Telemetry'); ImGui::SliderFloat(); ImGui::End()</span>
      <span>Immediate-Mode C++ Architecture · Zero Allocation per Frame (144+ FPS)</span>
    </div>
    """

    custom_js = """
    function drawImGuiPlot() {
      const c = document.getElementById('imgui-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const val = parseFloat(document.getElementById('imgui-temp').value);

      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      for (let i = 0; i < 60; i++) {
        const x = (i / 60) * W;
        const y = H/2 - Math.sin(i * 0.3) * (val * 0.25);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }

    window.addEventListener('load', () => { drawImGuiPlot(); });
    window.addEventListener('resize', drawImGuiPlot);
    """

    html = render_lang_page("C++", "Dear ImGui", "C Plus Plus Visualization", 'vcpkg install imgui',
                            "https://github.com/ocornut/imgui",
                            "Bloat-free immediate mode graphical user interface library for C++.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Dear_ImGui", html)

# 3. MAGNUM
def build_magnum():
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    paradigms = [{
        "tag": "01 / MODERN C++ GRAPHICS",
        "title": "Lightweight & Modular C++11/20 Graphics Middleware",
        "subtitle": "Magnum provides a clean, modular C++ graphics middleware integrating Vulkan, OpenGL, and WebGL with modern C++ abstractions.",
        "math_desc": "Cook-Torrance microfacet specular reflection: $f_r = \\frac{D F G}{4 (\\mathbf{n} \\cdot \\mathbf{l})(\\mathbf{n} \\cdot \\mathbf{v})}$ evaluating GGX normal distribution.",
        "math_formula": "D(\\mathbf{h}) = \\frac{\\alpha^2}{\\pi ((\\mathbf{n} \\cdot \\mathbf{h})^2 (\\alpha^2 - 1) + 1)^2}",
        "time_complexity": "O(M) hardware GPU fragment shader",
        "space_complexity": "O(1) heap allocation (RAII primitives)",
        "enterprise_use": "High-fidelity spatial robotics simulation (Habitat-Sim), interactive 3D scientific visualization.",
        "strengths": "Fastest compile times; modular architecture; seamless Emscripten WebAssembly compilation.",
        "tradeoffs": "Ecosystem is specialized for graphics developers rather than novice chart builders.",
        "metrics": [
            {"label": "Standard", "val": "C++11/20 + WebGL", "sub": "Zero Overhead"},
            {"label": "Platform", "val": "Vulkan / GL / Wasm", "sub": "Native Cross-Target"},
            {"label": "Used In", "val": "Meta AI Habitat", "sub": "Robotics Sim"},
            {"label": "License", "val": "MIT", "sub": "Vladimír Vondruš"}
        ],
        "code": """#include <Magnum/GL/Renderer.h>
#include <Magnum/Platform/EmscriptenApplication.h>

class MagnumStudio: public Platform::Application {
    void drawEvent() override {
        GL::Renderer::setClearColor(Color4{0.02f, 0.03f, 0.02f, 1.0f});
        GL::Renderer::clear(GL::Renderer::Clear::Color | GL::Renderer::Clear::Depth);
        swapBuffers();
    }
};"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">MAGNUM C++ SHADER PIPELINE</span>
      </div>
    </div>
    <div class="canvas-body" id="magnum-stage" style="width:100%; height:100%; min-height:480px; position:relative;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>Magnum::GL::Renderer · Modular C++ Graphics Middleware</span>
      <span>Physically-Based Rendering (PBR) Shader · Emscripten WebAssembly Target</span>
    </div>
    """

    custom_js = """
    let mgScene, mgCamera, mgRenderer, mgSphere;
    function initMagnumThree() {
      const el = document.getElementById('magnum-stage');
      if (!el) return;

      mgScene = new THREE.Scene();
      mgScene.background = new THREE.Color(0x040705);

      mgCamera = new THREE.PerspectiveCamera(45, el.clientWidth / el.clientHeight, 0.1, 1000);
      mgCamera.position.set(0, 0, 8);

      mgRenderer = new THREE.WebGLRenderer({ antialias: true });
      mgRenderer.setSize(el.clientWidth, el.clientHeight);
      mgRenderer.setPixelRatio(window.devicePixelRatio);
      el.appendChild(mgRenderer.domElement);

      const light = new THREE.PointLight(0x00e5ff, 1.5, 50);
      light.position.set(5, 5, 5);
      mgScene.add(light);
      mgScene.add(new THREE.AmbientLight(0xffffff, 0.2));

      // Metallic sphere with PBR material
      const geom = new THREE.SphereGeometry(2.5, 64, 64);
      const mat = new THREE.MeshStandardMaterial({
        color: 0x00e676,
        metalness: 0.9,
        roughness: 0.2
      });
      mgSphere = new THREE.Mesh(geom, mat);
      mgScene.add(mgSphere);

      function animate() {
        requestAnimationFrame(animate);
        mgSphere.rotation.y += 0.006;
        mgRenderer.render(mgScene, mgCamera);
      }
      animate();
    }

    window.addEventListener('load', () => { setTimeout(initMagnumThree, 100); });
    """

    html = render_lang_page("C++", "Magnum", "C Plus Plus Visualization", 'vcpkg install magnum',
                            "https://magnum.graphics",
                            "Lightweight and modular C++ graphics middleware for games and simulations.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Magnum", html)

# 4. MATPLOTLIB-CPP
def build_matplotlib_cpp():
    paradigms = [{
        "tag": "01 / PYTHON EMBEDDED C++",
        "title": "Zero-Overhead C++ Plotting via Python C-API",
        "subtitle": "matplotlib-cpp provides a header-only C++ wrapper around Python's matplotlib library using direct Python C-API bindings.",
        "math_desc": "Subplot figure layout transform matrix mapping data coordinates directly to publication-ready vector figures.",
        "math_formula": "\\mathbf{T}_{\\text{fig}} = \\mathbf{M}_{\\text{disp}} \\cdot \\mathbf{M}_{\\text{axes}} \\cdot \\mathbf{M}_{\\text{data}}",
        "time_complexity": "O(N) C++ vector marshaling",
        "space_complexity": "O(N) contiguous memory vector allocation",
        "enterprise_use": "Embedded C++ quantitative research backtesting reports, scientific C++ laboratory data output.",
        "strengths": "Familiar matplotlib syntax in pure C++; header-only; outputs publication-grade figures.",
        "tradeoffs": "Requires Python development headers (`Python.h`) installed on the host system.",
        "metrics": [
            {"label": "Design", "val": "Header-Only", "sub": "Zero-Compile C++"},
            {"label": "Engine", "val": "Python C-API", "sub": "Native C Interface"},
            {"label": "Output", "val": "Vector SVG / PNG", "sub": "Publication Quality"},
            {"label": "License", "val": "MIT", "sub": "Benno Rice"}
        ],
        "code": """#include "matplotlibcpp.h"
#include <vector>
#include <cmath>

namespace plt = matplotlibcpp;

int main() {
    std::vector<double> x(500), y(500);
    for (size_t i = 0; i < 500; ++i) {
        x[i] = i * 0.02;
        y[i] = std::sin(x[i]) * std::exp(-x[i] * 0.1);
    }

    plt::figure_size(1200, 780);
    plt::plot(x, y, "g-");
    plt::title("Damped Harmonic Oscillator (matplotlib-cpp)");
    plt::save("oscillator.svg");
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">MATPLOTLIB-CPP VECTOR WRAPPER</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="mpl-cpp-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>plt::plot(x, y, 'g-'); plt::save('oscillator.svg')</span>
      <span>Header-Only C++ Library · Direct Python C-API Integration</span>
    </div>
    """

    custom_js = """
    function drawMplCpp() {
      const c = document.getElementById('mpl-cpp-canvas');
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
      for (let y = 0; y < H; y += 35) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2;
      ctx.beginPath();
      const n = 300;
      for (let i = 0; i < n; i++) {
        const t = (i / n) * 12;
        const yVal = Math.sin(t * 2) * Math.exp(-t * 0.18);
        const px = (i / n) * W;
        const py = H/2 - yVal * (H * 0.4);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
    }

    window.addEventListener('load', () => { drawMplCpp(); });
    window.addEventListener('resize', drawMplCpp);
    """

    html = render_lang_page("C++", "matplotlib-cpp", "C Plus Plus Visualization", '# header-only matplotlibcpp.h',
                            "https://github.com/lava/matplotlib-cpp",
                            "Header-only C++ library wrapping Python's matplotlib via direct C-API.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("matplotlib-cpp", html)

# 5. QT CHARTS
def build_qt_charts():
    paradigms = [{
        "tag": "01 / HARDWARE QT GRAPHICS",
        "title": "Hardware-Accelerated Qt 6 GraphicsView & QChart",
        "subtitle": "Qt Charts provides C++ desktop developers with hardware-accelerated time series, candlestick, and polar charts.",
        "math_desc": "Sub-pixel anti-aliased path interpolation across QGraphicsScene coordinate frames.",
        "math_formula": "P_{\\text{scene}} = \\mathbf{M}_{\\text{view}} \\cdot P_{\\text{item}}",
        "time_complexity": "O(N) hardware GPU line strip blit",
        "space_complexity": "O(N) QList<QPointF> points buffer",
        "enterprise_use": "Automotive infotainment clusters, industrial SCADA automation telemetry screens.",
        "strengths": "Flawless integration with Qt QML and C++ signals/slots; high aesthetic polish.",
        "tradeoffs": "Large framework dependency (Qt Core, Gui, Widgets).",
        "metrics": [
            {"label": "Engine", "val": "QGraphicsView", "sub": "OpenGL Backend"},
            {"label": "Signals", "val": "Qt Signals / Slots", "sub": "Event Driven"},
            {"label": "Adoption", "val": "Industrial Standard", "sub": "Automotive / Med"},
            {"label": "License", "val": "GPL / Commercial", "sub": "The Qt Company"}
        ],
        "code": """#include <QtCharts/QChartView>
#include <QtCharts/QLineSeries>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    auto *series = new QLineSeries();
    for (int i = 0; i < 100; ++i) {
        series->append(i, qSin(i * 0.1));
    }

    auto *chart = new QChart();
    chart->addSeries(series);
    chart->createDefaultAxes();
    chart->setTitle("Qt 6 Charts: Realtime ECG Monitor");

    auto *chartView = new QChartView(chart);
    chartView->setRenderHint(QPainter::Antialiasing);
    chartView->show();
    return app.exec();
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">QT CHARTS C++ RUNTIME</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705;">
      <canvas id="qt-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>QChart::addSeries(); chartView->setRenderHint(Antialiasing)</span>
      <span>Qt 6 QGraphicsScene Scenegraph · Hardware-Accelerated Industrial Telemetry</span>
    </div>
    """

    custom_js = """
    function drawQtCharts() {
      const c = document.getElementById('qt-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      // Hospital phosphor ECG grid
      ctx.strokeStyle = 'rgba(0, 230, 118, 0.08)';
      for (let x = 0; x < W; x += 25) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
      for (let y = 0; y < H; y += 25) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2.2;
      ctx.beginPath();
      const n = 280;
      for (let i = 0; i < n; i++) {
        const t = (i / n) * 8;
        const beat = (t % 1.0);
        let spike = 0;
        if (beat > 0.2 && beat < 0.25) spike = 1.6;
        else if (beat > 0.25 && beat < 0.28) spike = -0.4;
        const px = (i / n) * W;
        const py = H/2 - spike * (H * 0.35);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
    }

    window.addEventListener('load', () => { drawQtCharts(); });
    window.addEventListener('resize', drawQtCharts);
    """

    html = render_lang_page("C++", "Qt Charts", "C Plus Plus Visualization", 'vcpkg install qtcharts',
                            "https://doc.qt.io/qt-6/qtcharts-index.html",
                            "Hardware-accelerated charting components for Qt C++ desktop applications.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Qt_Charts", html)

# 6. OPENSCENEGRAPH
def build_osg():
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    paradigms = [{
        "tag": "01 / SCENEGRAPH & LEVEL-OF-DETAIL",
        "title": "High-Performance 3D Scenegraph & Flight Simulation",
        "subtitle": "OpenSceneGraph provides an industrial C++ scenegraph managing Level-of-Detail (LOD), frustum culling, and spatial paging.",
        "math_desc": "View frustum sphere intersection culling: $\\mathbf{n} \\cdot \\mathbf{c} + d \\ge -r$ discarding out-of-view geometry nodes.",
        "math_formula": "\\text{LOD}(d) = \\begin{cases} \\text{Mesh}_{\\text{high}} & d < D_1 \\\\ \\text{Mesh}_{\\text{med}} & D_1 \\le d < D_2 \\\\ \\text{Mesh}_{\\text{low}} & d \\ge D_2 \\end{cases}",
        "time_complexity": "O(log N) bounding sphere tree traversal",
        "space_complexity": "O(N) node scenegraph tree",
        "enterprise_use": "Military aviation flight simulators, maritime port ship routing simulators.",
        "strengths": "Handles massive gigabyte-scale GIS terrains with continuous level-of-detail paging.",
        "tradeoffs": "Traditional C++ inheritance patterns require strict memory lifecycle care.",
        "metrics": [
            {"label": "Engine", "val": "Native C++ / OpenGL", "sub": "Frustum Culled"},
            {"label": "Paging", "val": "PagedLOD Terrains", "sub": "Virtual Texture"},
            {"label": "Industry", "val": "Aerospace Standard", "sub": "FAA Flight Sim"},
            {"label": "License", "val": "OSGPL (LGPL)", "sub": "Commercial Safe"}
        ],
        "code": """#include <osgViewer/Viewer>
#include <osg/ShapeDrawable>

int main() {
    osgViewer::Viewer viewer;
    auto* root = new osg::Group();
    auto* sphere = new osg::ShapeDrawable(new osg::Sphere(osg::Vec3(0,0,0), 2.0f));
    auto* geode = new osg::Geode();
    geode->addDrawable(sphere);
    root->addChild(geode);

    viewer.setSceneData(root);
    return viewer.run();
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">OPENSCENEGRAPH LOD PIPELINE</span>
      </div>
    </div>
    <div class="canvas-body" id="osg-stage" style="width:100%; height:100%; min-height:480px; position:relative;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>osg::PagedLOD · Frustum Culling & Bounding Sphere Optimization</span>
      <span>Industrial Flight Simulation Scenegraph in Native C++</span>
    </div>
    """

    custom_js = """
    let osgScene, osgCamera, osgRenderer, osgMesh;
    function initOsgThree() {
      const el = document.getElementById('osg-stage');
      if (!el) return;

      osgScene = new THREE.Scene();
      osgScene.background = new THREE.Color(0x040705);

      osgCamera = new THREE.PerspectiveCamera(45, el.clientWidth / el.clientHeight, 0.1, 1000);
      osgCamera.position.set(0, 10, 20);
      osgCamera.lookAt(0, 0, 0);

      osgRenderer = new THREE.WebGLRenderer({ antialias: true });
      osgRenderer.setSize(el.clientWidth, el.clientHeight);
      osgRenderer.setPixelRatio(window.devicePixelRatio);
      el.appendChild(osgRenderer.domElement);

      const light = new THREE.DirectionalLight(0x00e676, 1.2);
      light.position.set(10, 20, 10);
      osgScene.add(light);
      osgScene.add(new THREE.AmbientLight(0xffffff, 0.3));

      // Terrain mesh
      const geom = new THREE.PlaneGeometry(16, 16, 32, 32);
      const pos = geom.attributes.position;
      for (let i = 0; i < pos.count; i++) {
        const u = pos.getX(i); const v = pos.getY(i);
        pos.setZ(i, Math.sin(u * 0.5) * Math.cos(v * 0.5) * 2.0);
      }
      geom.computeVertexNormals();

      const mat = new THREE.MeshStandardMaterial({
        color: 0x00e5ff,
        wireframe: true
      });
      osgMesh = new THREE.Mesh(geom, mat);
      osgMesh.rotation.x = -Math.PI / 2.5;
      osgScene.add(osgMesh);

      function animate() {
        requestAnimationFrame(animate);
        osgMesh.rotation.z += 0.004;
        osgRenderer.render(osgScene, osgCamera);
      }
      animate();
    }

    window.addEventListener('load', () => { setTimeout(initOsgThree, 100); });
    """

    html = render_lang_page("C++", "OpenSceneGraph", "C Plus Plus Visualization", 'vcpkg install openscenegraph',
                            "http://www.openscenegraph.org",
                            "High-performance real-time 3D graphics toolkit for flight simulation.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("OpenSceneGraph", html)

# 7. OGDF
def build_ogdf():
    paradigms = [{
        "tag": "01 / ALGORITHMIC GRAPH DRAWING",
        "title": "Sugiyama Layered Graph & Planarization Engine",
        "subtitle": "OGDF is an advanced C++ library for algorithmic graph drawing, computing minimal-crossing planar embeddings and hierarchical DAGs.",
        "math_desc": "Barycenter heuristic for crossing reduction: orders vertices in layer $L_{k+1}$ by the average position of their neighbors in layer $L_k$.",
        "math_formula": "\\text{Barycenter}(v) = \\frac{1}{|N(v)|} \\sum_{u \\in N(v)} \\text{Pos}(u)",
        "time_complexity": "O(V log V) per layer ordering pass",
        "space_complexity": "O(V + E) combinatorial planar embedding graph",
        "enterprise_use": "VLSI chip circuit diagram routing, UML software architecture dependency reverse-engineering.",
        "strengths": "Fastest algorithmic layout library in C++; mathematically rigorous layout algorithms.",
        "tradeoffs": "Pure algorithmic graph solver; rendering is delegated to SVG/Cairo backends.",
        "metrics": [
            {"label": "Algorithms", "val": "Sugiyama / FMMM", "sub": "Exact Planar"},
            {"label": "Performance", "val": "Optimized C++", "sub": "Multi-Threaded"},
            {"label": "Topology", "val": "Planarization", "sub": "Minimal Crossing"},
            {"label": "License", "val": "GNU GPL", "sub": "Academic / Corp"}
        ],
        "code": """#include <ogdf/basic/Graph.h>
#include <ogdf/layered/SugiyamaLayout.h>

int main() {
    ogdf::Graph G;
    auto v1 = G.newNode();
    auto v2 = G.newNode();
    G.newEdge(v1, v2);

    ogdf::SugiyamaLayout layout;
    ogdf::GraphAttributes GA(G);
    layout.call(GA);
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">OGDF PLANAR GRAPH SOLVER</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="ogdf-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>SugiyamaLayout::call(GA) · Planarization & Barycenter Crossing Reduction</span>
      <span>Open Graph Drawing Framework in Native C++ · VLSI Circuit Topology</span>
    </div>
    """

    custom_js = """
    function drawOgdf() {
      const c = document.getElementById('ogdf-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const layers = [
        [{ x: 100, y: H/2, lbl: 'Source' }],
        [{ x: 260, y: H/2 - 80, lbl: 'ALU' }, { x: 260, y: H/2 + 80, lbl: 'Registers' }],
        [{ x: 420, y: H/2 - 80, lbl: 'Pipeline' }, { x: 420, y: H/2 + 80, lbl: 'Cache' }],
        [{ x: 560, y: H/2, lbl: 'Drain' }]
      ];

      // Edges with Bezier curves
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      ctx.moveTo(100, H/2); ctx.lineTo(260, H/2 - 80);
      ctx.moveTo(100, H/2); ctx.lineTo(260, H/2 + 80);
      ctx.moveTo(260, H/2 - 80); ctx.lineTo(420, H/2 - 80);
      ctx.moveTo(260, H/2 + 80); ctx.lineTo(420, H/2 + 80);
      ctx.moveTo(420, H/2 - 80); ctx.lineTo(560, H/2);
      ctx.moveTo(420, H/2 + 80); ctx.lineTo(560, H/2);
      ctx.stroke();

      // Nodes
      layers.flat().forEach(n => {
        ctx.fillStyle = '#0e1712';
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 2;
        ctx.strokeRect(n.x - 45, n.y - 18, 90, 36);
        ctx.fillRect(n.x - 45, n.y - 18, 90, 36);

        ctx.fillStyle = '#fff';
        ctx.font = '10px JetBrains Mono';
        ctx.textAlign = 'center';
        ctx.fillText(n.lbl, n.x, n.y + 4);
      });
    }

    window.addEventListener('load', () => { drawOgdf(); });
    window.addEventListener('resize', drawOgdf);
    """

    html = render_lang_page("C++", "OGDF", "C Plus Plus Visualization", 'vcpkg install ogdf',
                            "https://ogdf.uos.de",
                            "Open Graph Drawing Framework in C++ for algorithmic graph layouts.",
                            paradigms, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("OGDF", html)

# 8. OGRE3D
def build_ogre3d():
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    paradigms = [{
        "tag": "01 / SCENE-ORIENTED 3D ENGINE",
        "title": "Scene-Oriented Real-Time 3D Rendering Engine",
        "subtitle": "Ogre3D provides a mature C++ scenegraph with material scripts, compositors, and hardware particle systems.",
        "math_desc": "Hardware particle emission rate: $N(t) = \\int_0^t R(\\tau) d\\tau$ with stochastic Brownian noise velocity vectors.",
        "math_formula": "\\mathbf{v}_i(t+\\Delta t) = \\mathbf{v}_i(t) + \\mathbf{a} \\Delta t + \\mathcal{N}(0, \\sigma^2)",
        "time_complexity": "O(P) particle billboard GPU drawing",
        "space_complexity": "O(P) instanced vertex buffer",
        "enterprise_use": "Autonomous driving sensor simulation, virtual reality surgical training.",
        "strengths": "Mature production pedigree; clean separation of graphics hardware backends.",
        "tradeoffs": "Heavyweight codebase compared to modern minimal engines like Magnum.",
        "metrics": [
            {"label": "Engine", "val": "Ogre3D Next-Gen", "sub": "DirectX / Vulkan / GL"},
            {"label": "Particles", "val": "GPU Instanced", "sub": "Additive Blending"},
            {"label": "Materials", "val": "HLSL / GLSL Scripts", "sub": "Compositor Nodes"},
            {"label": "License", "val": "MIT", "sub": "Tor_Andersson"}
        ],
        "code": """#include <Ogre.h>

int main() {
    Ogre::Root* root = new Ogre::Root("plugins.cfg");
    Ogre::SceneManager* scnMgr = root->createSceneManager();
    Ogre::SceneNode* camNode = scnMgr->getRootSceneNode()->createChildSceneNode();
    Ogre::Camera* cam = scnMgr->createCamera("MainCam");
    camNode->attachObject(cam);

    Ogre::ParticleSystem* partSys = scnMgr->createParticleSystem("Nimbus", "Examples/Smoke");
    scnMgr->getRootSceneNode()->attachObject(partSys);
    return 0;
}"""
    }]

    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">OGRE3D PARTICLE EMITTER ACTIVE</span>
      </div>
    </div>
    <div class="canvas-body" id="ogre-stage" style="width:100%; height:100%; min-height:480px; position:relative;"></div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>scnMgr->createParticleSystem('Nimbus') · Ogre3D Hardware Particle Engine</span>
      <span>Scene-Oriented Real-Time 3D Rendering Engine in Native C++</span>
    </div>
    """

    custom_js = """
    let ogreScene, ogreCamera, ogreRenderer, ogreParticles;
    function initOgreThree() {
      const el = document.getElementById('ogre-stage');
      if (!el) return;

      ogreScene = new THREE.Scene();
      ogreScene.background = new THREE.Color(0x040705);

      ogreCamera = new THREE.PerspectiveCamera(45, el.clientWidth / el.clientHeight, 0.1, 1000);
      ogreCamera.position.set(0, 0, 15);

      ogreRenderer = new THREE.WebGLRenderer({ antialias: true });
      ogreRenderer.setSize(el.clientWidth, el.clientHeight);
      ogreRenderer.setPixelRatio(window.devicePixelRatio);
      el.appendChild(ogreRenderer.domElement);

      const pCount = 1200;
      const geom = new THREE.BufferGeometry();
      const pos = [];
      for (let i = 0; i < pCount; i++) {
        pos.push((Math.random() - 0.5) * 12, (Math.random() - 0.5) * 12, (Math.random() - 0.5) * 12);
      }
      geom.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));

      const mat = new THREE.PointsMaterial({
        color: 0x00e676,
        size: 0.15,
        transparent: true,
        opacity: 0.8
      });
      ogreParticles = new THREE.Points(geom, mat);
      ogreScene.add(ogreParticles);

      function animate() {
        requestAnimationFrame(animate);
        ogreParticles.rotation.y += 0.005;
        ogreRenderer.render(ogreScene, ogreCamera);
      }
      animate();
    }

    window.addEventListener('load', () => { setTimeout(initOgreThree, 100); });
    """

    html = render_lang_page("C++", "Ogre3D", "C Plus Plus Visualization", 'vcpkg install ogre',
                            "https://www.ogre3d.org",
                            "Scene-oriented real-time 3D rendering engine in C++.",
                            paradigms, extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool("Ogre3D", html)

if __name__ == "__main__":
    build_cpp_all()
