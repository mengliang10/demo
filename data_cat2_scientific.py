"""
Category 2: 3D, High-Performance & Scientific Graphics (8 tools)
Contains authentic paradigms, production Python scripts, mathematical specs, and metrics.
"""

PEERS_CAT2 = [
    {"name": "Datashader", "paradigm": "Rasterized In-Memory Aggregation", "engine": "Numba JIT / Multi-Core", "scale": "100M - 1B Points", "interactivity": "Server-Side Dynamic Resample", "learning_curve": "Moderate"},
    {"name": "Mayavi", "paradigm": "3D Scientific VTK Pipeline", "engine": "VTK C++ / OpenGL", "scale": "5M Vertices", "interactivity": "3D Mouse Orbit / Slicing", "learning_curve": "Moderate - High"},
    {"name": "VisPy", "paradigm": "Hardware Modern OpenGL Shaders", "engine": "GLSL / PyOpenGL", "scale": "10M+ Points (60 FPS)", "interactivity": "Zero-Latency GPU Events", "learning_curve": "High"},
    {"name": "PyQtGraph", "paradigm": "High-Frequency Qt Hardware 2D/3D", "engine": "Qt GUI / OpenGL", "scale": "2M Points (Realtime)", "interactivity": "Sub-millisecond Zoom", "learning_curve": "Moderate"},
    {"name": "VTK (Python bindings)", "paradigm": "Industrial Visualization Toolkit", "engine": "Native C++ / Hardware Raytrace", "scale": "100M+ Elements", "interactivity": "Pipeline Filters / Slicing", "learning_curve": "High"},
    {"name": "Glumpy", "paradigm": "Scientific Modern OpenGL Prototyping", "engine": "OpenGL 2.1+ / GLSL Shaders", "scale": "5M Vertices", "interactivity": "Real-time Shader Uniforms", "learning_curve": "High"},
    {"name": "Manim", "paradigm": "Programmatic Mathematical Animations", "engine": "Cairo / ModernGL Shader", "scale": "Mathematical Vectors", "interactivity": "Video / Frame Sequencing", "learning_curve": "Moderate - High"},
    {"name": "PyVista", "paradigm": "Pythonic VTK Mesh & Voxel Analysis", "engine": "VTK / Trame Web Platform", "scale": "20M Vertices", "interactivity": "Browser & Desktop 3D", "learning_curve": "Low - Moderate"}
]

TOOLS_CAT2 = [
    {
        "name": "Datashader",
        "category": "3D, High-Performance & Scientific Graphics",
        "folder": "Datashader",
        "pip": "pip install datashader bokeh numba",
        "docs": "https://datashader.org",
        "license": "BSD 3-Clause",
        "tagline": "Billion-scale point and network rasterization engine eliminating visual overplotting entirely.",
        "peers": PEERS_CAT2,
        "paradigms": [
            {
                "tag": "01 / BILLION-POINT HDR RASTER",
                "title": "Billion-Scale Perceptual HDR Cloud & Density Equalization",
                "subtitle": "Direct memory aggregation into screen-resolution pixel bins using Numba JIT and histogram equalization.",
                "math_desc": "Equalized transfer function mapping raw histogram bin counts to visual lightness: $I(x,y) = \\text{CDF}(C(x,y))$ ensuring every point contributes perceptually.",
                "math_formula": "C(x,y) = \\sum_{i=1}^N \\delta\\left(x - \\lfloor x_i / \\Delta x \\rfloor\\right) \\delta\\left(y - \\lfloor y_i / \\Delta y \\rfloor\\right)",
                "time_complexity": "O(N) single parallel reduction pass",
                "space_complexity": "O(W \\times H) screen pixel buffer",
                "enterprise_use": "Nationwide cellular mobility GPS pings, astrophysics N-body dark matter galaxy clusters.",
                "strengths": "Renders 100,000,000 points without browser memory crashes or visual saturation.",
                "tradeoffs": "Generates 2D raster image buffers rather than selectable vector DOM elements.",
                "metrics": [
                    {"label": "Scale", "val": "10M - 1B Points", "sub": "Out-of-Core"},
                    {"label": "JIT Engine", "val": "Numba Parallel", "sub": "Multi-Threaded"},
                    {"label": "Overplotting", "val": "Zero Saturation", "sub": "Equalized HDR"},
                    {"label": "Output", "val": "2D RGBA Raster", "sub": "Resolution Matched"}
                ],
                "code": """import datashader as ds
import datashader.transfer_functions as tf
import pandas as pd
import numpy as np

# Generate 10,000,000 synthetic GPS coordinates
n_pts = n_samples * 50000
x = np.random.normal(0, 1, n_pts)
y = np.random.normal(0, 1, n_pts)
df = pd.DataFrame({'x': x, 'y': y})

cvs = ds.Canvas(plot_width=800, plot_height=600)
agg = cvs.points(df, 'x', 'y')
img = tf.shade(agg, cmap=['#040705', '#00e676', '#f3cf65', '#ffffff'], how='eq_hist')
img.to_pil().save('datashader_output.png')"""
            }
        ]
    },
    {
        "name": "Mayavi",
        "category": "3D, High-Performance & Scientific Graphics",
        "folder": "Mayavi",
        "pip": "pip install mayavi vtk PyQt5",
        "docs": "https://docs.enthought.com/mayavi/mayavi",
        "license": "BSD 3-Clause",
        "tagline": "High-level 3D scientific data visualization and pipeline toolkit built on VTK.",
        "peers": PEERS_CAT2,
        "paradigms": [
            {
                "tag": "01 / 3D VECTOR STREAMLINE",
                "title": "3D Vector Flow Field Integration & Tensor Glyphs",
                "subtitle": "Hardware-accelerated 3D vector arrows, stream tubes, and contour cut-planes on unstructured volumetric meshes.",
                "math_desc": "3D streamline curve integration: $\\frac{d\\mathbf{x}}{dt} = \\mathbf{u}(\\mathbf{x})$ with oriented elliptical tensor glyphs displaying velocity gradients.",
                "math_formula": "\\mathbf{x}(t) = \\mathbf{x}_0 + \\int_0^t \\mathbf{u}(\\mathbf{x}(\\tau)) d\\tau",
                "time_complexity": "O(N) VTK pipeline execution",
                "space_complexity": "O(M) 3D unstructured mesh memory",
                "enterprise_use": "Magnetohydrodynamic plasma physics, cardiovascular blood flow vector tomography.",
                "strengths": "Rich interactive 3D visual pipeline with interactive slicing planes and contour filters.",
                "tradeoffs": "Heavy dependency tree (VTK, Qt, PyFace).",
                "metrics": [
                    {"label": "Engine", "val": "VTK 9.x Core", "sub": "Hardware C++"},
                    {"label": "Geometry", "val": "Unstructured 3D", "sub": "Volumetric"},
                    {"label": "Glyphs", "val": "Oriented Tensors", "sub": "Vector Field"},
                    {"label": "Interface", "val": "mlab Scripting", "sub": "Pythonic API"}
                ],
                "code": """from mayavi import mlab
import numpy as np

x, y, z = np.mgrid[-2:2:20j, -2:2:20j, -2:2:20j]
u = -1 - x**2 + y
v = 1 + x - y**2
w = z

mlab.figure(bgcolor=(0.02, 0.03, 0.02), size=(800, 600))
src = mlab.pipeline.vector_field(u, v, w)
mlab.pipeline.vectors(src, mask_points=10, scale_factor=0.3, colormap='Spectral')
mlab.pipeline.vector_cut_plane(src, plane_orientation='z_axes')
mlab.savefig('mayavi_flow.png')"""
            }
        ]
    },
    {
        "name": "VisPy",
        "category": "3D, High-Performance & Scientific Graphics",
        "folder": "VisPy",
        "pip": "pip install vispy pyopengl",
        "docs": "https://vispy.org",
        "license": "BSD 3-Clause",
        "tagline": "High-performance interactive scientific visualization library leveraging modern OpenGL shaders.",
        "peers": PEERS_CAT2,
        "paradigms": [
            {
                "tag": "01 / GPU SHADER POINT CLOUD",
                "title": "Hardware Shader Multi-Million Point Particle Cloud",
                "subtitle": "Leverages direct GPU GLSL fragment shaders for sub-millisecond particle physics and camera orbit.",
                "math_desc": "Hardware vertex displacement: $\\mathbf{p}_{\\text{gl}} = \\mathbf{P} \\cdot \\mathbf{V} \\cdot \\mathbf{M} \\cdot (\\mathbf{p} + \\mathbf{a} \\sin(\\omega t))$ evaluated on GPU cores.",
                "math_formula": "\\mathbf{gl\\_PointSize} = d_{\\text{base}} \\cdot \\frac{f_{\\text{focal}}}{z_{\\text{eye}}}",
                "time_complexity": "O(1) CPU dispatch; O(N) GPU pipeline",
                "space_complexity": "O(N) VRAM buffer",
                "enterprise_use": "Autonomous driving LiDAR point cloud live streaming, particle accelerator collision displays.",
                "strengths": "Sustains 60 FPS on 10,000,000+ points by offloading computation to custom GLSL shaders.",
                "tradeoffs": "Requires understanding of OpenGL graphics pipeline and GLSL syntax for custom marks.",
                "metrics": [
                    {"label": "Throughput", "val": "60 FPS @ 10M Pts", "sub": "Hardware Shaders"},
                    {"label": "Shaders", "val": "Custom GLSL", "sub": "Vertex + Fragment"},
                    {"label": "Latency", "val": "< 2 ms", "sub": "Immediate Mode"},
                    {"label": "Backend", "val": "OpenGL 2.1 - 4.5", "sub": "Native Driver"}
                ],
                "code": """import numpy as np
from vispy import app, scene

canvas = scene.SceneCanvas(keys='interactive', bgcolor='#050806', size=(800, 600))
view = canvas.central_widget.add_view()
view.camera = 'turntable'

N = n_samples * 1000
pos = np.random.normal(size=(N, 3), scale=2.0)
colors = np.random.uniform(0.2, 1.0, size=(N, 4))

scatter = scene.visuals.Markers()
scatter.set_data(pos, edge_color=None, face_color=colors, size=4)
view.add(scatter)
canvas.show()
app.run()"""
            }
        ]
    },
    {
        "name": "PyQtGraph",
        "category": "3D, High-Performance & Scientific Graphics",
        "folder": "PyQtGraph",
        "pip": "pip install pyqtgraph PyQt5",
        "docs": "https://pyqtgraph.readthedocs.io",
        "license": "MIT License",
        "tagline": "Fast, interactive 2D/3D visualization library for real-time engineering and biomedical applications.",
        "peers": PEERS_CAT2,
        "paradigms": [
            {
                "tag": "01 / REAL-TIME BIOMEDICAL STREAM",
                "title": "Sub-Millisecond Multi-Channel Real-Time Oscilloscope",
                "subtitle": "High-throughput Qt GraphicsView and OpenGL hardware streaming at 100+ frames per second.",
                "math_desc": "Circular ring-buffer memory streaming: $\\mathbf{y}_{t} = \\mathbf{y}_{t-1} \\circ \\mathbf{S}_{\\text{shift}} + \\Delta \\mathbf{y}_{\\text{in}}$ updating GraphicsItem dirty rects.",
                "math_formula": "f_{\\text{refresh}} \\ge 120 \\text{ Hz} \\quad \\text{with } N = 10^5 \\text{ samples/ch}",
                "time_complexity": "O(N) ring buffer copy",
                "space_complexity": "O(N) Qt GraphicsItem memory",
                "enterprise_use": "Brain-computer interfaces (BCI EEG streaming), high-speed industrial motor dynamometer monitoring.",
                "strengths": "Fastest 2D interactive plotting toolkit on Python desktop; seamless Qt UI embedding.",
                "tradeoffs": "Desktop-centric; requires packaging desktop Qt dependencies.",
                "metrics": [
                    {"label": "Framerate", "val": "120+ FPS", "sub": "Realtime Audio/EEG"},
                    {"label": "UI Toolkit", "val": "Qt5 / Qt6 Native", "sub": "Signal/Slots"},
                    {"label": "Interactivity", "val": "Instant Drag/Zoom", "sub": "Hardware Rect"},
                    {"label": "License", "val": "MIT Permissive", "sub": "Commercial Ready"}
                ],
                "code": """import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets
import numpy as np

app = pg.mkQApp("Real-Time Telemetry")
win = pg.GraphicsLayoutWidget(show=True, title="PyQtGraph Ultra-Fast Scope")
win.resize(800, 500)
p = win.addPlot(title="High-Speed Sensor Ingestion (120 Hz)")
curve = p.plot(pen=pg.mkPen('#00e676', width=1.5))

data = np.zeros(n_samples * 10)
ptr = 0

def update():
    global data, ptr
    data[:-1] = data[1:]
    data[-1] = np.sin(ptr * 0.05) + np.random.normal(0, 0.1)
    ptr += 1
    curve.setData(data)

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(8)  # ~120 FPS
pg.exec()"""
            }
        ]
    },
    {
        "name": "VTK (Python bindings)",
        "category": "3D, High-Performance & Scientific Graphics",
        "folder": "VTK (Python bindings)",
        "pip": "pip install vtk",
        "docs": "https://vtk.org",
        "license": "BSD 3-Clause",
        "tagline": "The industrial-standard open-source system for 3D computer graphics, modeling, and scientific processing.",
        "peers": PEERS_CAT2,
        "paradigms": [
            {
                "tag": "01 / INDUSTRIAL DATA PIPELINE",
                "title": "Demand-Driven Executive Pipeline with Ray-Casting",
                "subtitle": "Connects Source $\\rightarrow$ Filter $\\rightarrow$ Mapper $\\rightarrow$ Actor across complex 3D polydata meshes.",
                "math_desc": "Demand-driven pipeline execution: updates trigger `RequestUpdateExtent()` and `RequestData()` only when upstream modifications occur.",
                "math_formula": "\\mathbf{Output} = \\mathcal{A}_{\\text{actor}}(\\mathcal{M}_{\\text{mapper}}(\\mathcal{F}_{\\text{filter}}(\\mathcal{S}_{\\text{source}})))",
                "time_complexity": "O(N) hardware geometry pipeline",
                "space_complexity": "O(N) C++ native memory",
                "enterprise_use": "CAD/CAM mechanical stress analysis, aerospace CFD supersonic shockwave rendering.",
                "strengths": "Battle-tested across 30+ years in defense, aerospace, medical, and petroleum supercomputing.",
                "tradeoffs": "Steep learning curve with low-level C++ object model semantics.",
                "metrics": [
                    {"label": "Standard", "val": "Global Scientific Benchmark", "sub": "30+ Year Legacy"},
                    {"label": "Pipeline", "val": "Demand-Driven", "sub": "Zero Redundant Exec"},
                    {"label": "Output", "val": "Direct OpenGL/Raytrace", "sub": "Hardware Ray Cast"},
                    {"label": "Language", "val": "C++ Wrapped in Py", "sub": "Zero Overhead"}
                ],
                "code": """import vtk

sphere = vtk.vtkSphereSource()
sphere.SetRadius(1.0)
sphere.SetPhiResolution(50)
sphere.SetThetaResolution(50)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.0, 0.9, 0.46)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.02, 0.03, 0.02)

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(800, 600)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)
renderWindow.Render()
interactor.Start()"""
            }
        ]
    },
    {
        "name": "Glumpy",
        "category": "3D, High-Performance & Scientific Graphics",
        "folder": "Glumpy",
        "pip": "pip install glumpy pyopengl",
        "docs": "https://glumpy.github.io",
        "license": "BSD 2-Clause",
        "tagline": "Fast, flexible scientific visualization on modern OpenGL connecting NumPy arrays directly to GPU shaders.",
        "peers": PEERS_CAT2,
        "paradigms": [
            {
                "tag": "01 / GPU ZERO-COPY ARRAYS",
                "title": "Zero-Copy NumPy GPU Shaders with GLSL Uniforms",
                "subtitle": "Bridges CPU NumPy memory buffers directly into GPU VRAM with dynamic shader uniform interpolation.",
                "math_desc": "GLSL Fragment raymarcher: continuous distance field evaluation: $d(\\mathbf{p}) = \\|\\mathbf{p}\\| - R$ executed across GPU cores.",
                "math_formula": "\\mathbf{Color} = \\text{shader}(\\mathbf{uniforms}, \\mathbf{attributes})",
                "time_complexity": "O(1) CPU dispatch",
                "space_complexity": "O(V) VRAM vertex allocation",
                "enterprise_use": "Computational neuroscience neural spikes raster displays, laser interferometry live feeds.",
                "strengths": "Direct access to raw OpenGL shaders without heavyweight framework bloat.",
                "tradeoffs": "Requires hands-on GLSL shader writing skills.",
                "metrics": [
                    {"label": "Memory", "val": "Zero-Copy Bridge", "sub": "NumPy to GPU"},
                    {"label": "Shader", "val": "GLSL 1.20 - 3.30", "sub": "Direct Shaders"},
                    {"label": "Framerate", "val": "V-Sync Capped (144Hz)", "sub": "Hardware Sync"},
                    {"label": "Weight", "val": "< 2 MB Package", "sub": "Ultra-Lean"}
                ],
                "code": """from glumpy import app, gloo, gl
import numpy as np

vertex = '''
attribute vec2 position;
void main() { gl_Position = vec4(position, 0.0, 1.0); }
'''
fragment = '''
uniform vec4 color;
void main() { gl_FragColor = color; }
'''

window = app.Window(width=800, height=600, color=(0.02, 0.03, 0.02, 1.0))
quad = gloo.Program(vertex, fragment, count=4)
quad['position'] = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
quad['color'] = (0.0, 0.9, 0.46, 1.0)

@window.event
def on_draw(dt):
    window.clear()
    quad.draw(gl.GL_TRIANGLE_STRIP)

app.run()"""
            }
        ]
    },
    {
        "name": "Manim (Mathematical Animation Engine)",
        "category": "3D, High-Performance & Scientific Graphics",
        "folder": "Manim (Mathematical Animation Engine)",
        "pip": "pip install manim",
        "docs": "https://www.manim.community",
        "license": "MIT License",
        "tagline": "The open-source programmatic mathematical animation engine behind 3Blue1Brown.",
        "peers": PEERS_CAT2,
        "paradigms": [
            {
                "tag": "01 / FOURIER EPICYCLE DECOMPOSITION",
                "title": "Fourier Epicycle Decomposition of Complex Parametric Curves",
                "subtitle": "Decomposes arbitrary closed vector outlines into revolving rotating complex frequency vectors.",
                "math_desc": "Continuous complex Fourier series decomposition: $c_n = \\frac{1}{T} \\int_0^T f(t) e^{-i \\frac{2\\pi n}{T} t} dt$ visualised as linked epicyclic circles.",
                "math_formula": "f(t) = \\sum_{n=-\\infty}^{\\infty} c_n e^{i 2\\pi n t / T}",
                "time_complexity": "O(N \\log N) FFT coefficients",
                "space_complexity": "O(K) rotating vector states",
                "enterprise_use": "Executive technical explaining videos, AI/ML university video course creation, mathematical research presentations.",
                "strengths": "Pristine cinematic typography, exact LaTeX equation rendering, mathematical rigor.",
                "tradeoffs": "Non-realtime frame-by-frame rendering engine; exports to MP4/WebM video.",
                "metrics": [
                    {"label": "Engine", "val": "Cairo / ModernGL", "sub": "Vector + GPU"},
                    {"label": "Output", "val": "4K 60FPS Video", "sub": "MP4 / GIF"},
                    {"label": "Equations", "val": "Native LaTeX", "sub": "Perfect Kerning"},
                    {"label": "Creator", "val": "3Blue1Brown Base", "sub": "Community Fork"}
                ],
                "code": """from manim import *

class FourierEpicycles(Scene):
    def construct(self):
        self.camera.background_color = "#050806"
        title = MathTex(r"f(t) = \\sum_{n=-\\infty}^{\\infty} c_n e^{i n \\omega_0 t}", color="#f3cf65")
        title.to_edge(UP)
        self.play(Write(title))
        
        circle1 = Circle(radius=2.0, color="#00e676")
        circle2 = Circle(radius=0.8, color="#00e5ff").shift(RIGHT * 2.0)
        self.play(Create(circle1), Create(circle2), run_time=2)
        self.wait(1)"""
            }
        ]
    },
    {
        "name": "PyVista",
        "category": "3D, High-Performance & Scientific Graphics",
        "folder": "PyVista",
        "pip": "pip install pyvista",
        "docs": "https://docs.pyvista.org",
        "license": "MIT License",
        "tagline": "3D plotting and mesh analysis made simple and pythonic through modern VTK wrapping.",
        "peers": PEERS_CAT2,
        "paradigms": [
            {
                "tag": "01 / PYTHONIC 3D MESH FILTERS",
                "title": "3D PolyData Mesh Curvature & Streamline Tracing",
                "subtitle": "Pythonic NumPy-like array slicing and geometric filters with zero VTK boilerplate code.",
                "math_desc": "Gaussian surface curvature calculation: $K = \\kappa_1 \\kappa_2$ and Mean curvature $H = \\frac{\\kappa_1 + \\kappa_2}{2}$ mapped across triangulated mesh vertices.",
                "math_formula": "K = \\frac{LN - M^2}{EG - F^2}",
                "time_complexity": "O(V) surface curvature solver",
                "space_complexity": "O(V + F) PolyData mesh memory",
                "enterprise_use": "Subsurface mining ore-body geostatistics, wind turbine aerodynamic mesh blade analysis.",
                "strengths": "Transforms clunky VTK pipelines into clean, pythonic `mesh.curvature()` calls.",
                "tradeoffs": "Large surface meshes require dedicated system memory.",
                "metrics": [
                    {"label": "Backend", "val": "VTK 9.x Pythonic", "sub": "Clean Wrapper"},
                    {"label": "Web Export", "val": "Trame / HTML", "sub": "Interactive Browser"},
                    {"label": "Array Access", "val": "NumPy Native", "sub": "Direct ndarray"},
                    {"label": "Raytracing", "val": "OSPRay Capable", "sub": "Photorealistic"}
                ],
                "code": """import pyvista as pv
import numpy as np

# Create complex 3D parametric surface
sphere = pv.Sphere(radius=1.0, phi_resolution=100, theta_resolution=100)
curv = sphere.curvature(curv_type='gaussian')
sphere['Gaussian Curvature'] = curv

plotter = pv.Plotter(off_screen=True)
plotter.set_background('#050806')
plotter.add_mesh(sphere, scalars='Gaussian Curvature', cmap='plasma', smooth_shading=True)
plotter.camera_position = 'iso'
plotter.screenshot('pyvista_mesh.png')"""
            }
        ]
    }
]
