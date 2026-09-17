"""
Category 1: Statistical, Charting & Core Plotting (16 tools)
Contains authentic paradigms, production Python scripts, mathematical specs, and metrics.
"""

PEERS_CAT1 = [
    {"name": "Matplotlib", "paradigm": "Object-Oriented Canvas/Artist", "engine": "Agg / Vector / Canvas", "scale": "500K Points", "interactivity": "Widget / Event Listeners", "learning_curve": "Moderate - High"},
    {"name": "Seaborn", "paradigm": "Statistical Declarative DataFrame", "engine": "Matplotlib Agg Backend", "scale": "100K Points", "interactivity": "Static / Facet Interactive", "learning_curve": "Low - Moderate"},
    {"name": "Plotly Py (Plotly.py - Dash)", "paradigm": "JSON Schema / WebGL Declarative", "engine": "Plotly.js / WebGL / Canvas", "scale": "1M+ Points (WebGL)", "interactivity": "Native DOM / WebGL Zoom", "learning_curve": "Low - Moderate"},
    {"name": "Bokeh", "paradigm": "ColumnDataSource Scenegraph", "engine": "BokehJS / HTML5 Canvas", "scale": "250K Points", "interactivity": "WebSocket Server / Client JS", "learning_curve": "Moderate"},
    {"name": "Altair", "paradigm": "Grammar of Graphics (Vega-Lite)", "engine": "Vega-Lite JS / Canvas / SVG", "scale": "5K - 10K Points (Browser)", "interactivity": "Declarative Interval / Point", "learning_curve": "Low - Moderate"},
    {"name": "HoloViews", "paradigm": "Semantic Data Annotations", "engine": "Matplotlib / Bokeh / Plotly", "scale": "Domain Dependent", "interactivity": "DynamicMap Pipeline", "learning_curve": "Moderate - High"},
    {"name": "Pygal", "paradigm": "SVG Native Vector Output", "engine": "Pure Python XML / SVG", "scale": "10K Points", "interactivity": "SVG Tooltips / CSS", "learning_curve": "Very Low"},
    {"name": "Plotnine", "paradigm": "ggplot2 Grammar in Python", "engine": "Matplotlib Agg Backend", "scale": "100K Points", "interactivity": "Static Publication Ready", "learning_curve": "Low (for R users)"},
    {"name": "Chartify", "paradigm": "Spotify Opinionated Wrapper", "engine": "Bokeh JS Backend", "scale": "50K Points", "interactivity": "Native Bokeh Hover", "learning_curve": "Very Low"},
    {"name": "HVPlot", "paradigm": "High-Level .hvplot() API", "engine": "HoloViews + Bokeh", "scale": "100K - 1M Points", "interactivity": "Cross-filter / Linked Zoom", "learning_curve": "Low"},
    {"name": "bqplot", "paradigm": "Jupyter Interactive Widget Grammar", "engine": "d3.js + Jupyter Comm", "scale": "50K Points", "interactivity": "Two-Way Python Traitlets", "learning_curve": "Moderate"},
    {"name": "Leather", "paradigm": "Minimalist Zero-Dep SVG", "engine": "Python XML Writer", "scale": "5K Points", "interactivity": "Static SVG Only", "learning_curve": "Minimal"},
    {"name": "Veusz", "paradigm": "GUI & Scripting Scientific Plotting", "engine": "Qt / PyQt Vector Canvas", "scale": "100K Points", "interactivity": "Interactive GUI + Export", "learning_curve": "Moderate"},
    {"name": "GR Framework", "paradigm": "C-Accelerated Lightweight Rendering", "engine": "GR C-Engine / OpenGL", "scale": "1M+ Points (Microseconds)", "interactivity": "High-Frequency Realtime", "learning_curve": "Moderate"},
    {"name": "Visvis", "paradigm": "Object-Oriented 3D Plotting", "engine": "OpenGL / PyOpenGL", "scale": "500K Points", "interactivity": "3D Camera / Mouse Orbit", "learning_curve": "Moderate"},
    {"name": "Chaco", "paradigm": "Enthought Component Plotting Architecture", "engine": "Kiva C-Drawing / Wx / Qt", "scale": "200K Points", "interactivity": "Tools / Overlays / Pan-Zoom", "learning_curve": "High"}
]

TOOLS_CAT1 = [
    {
        "name": "Matplotlib",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Matplotlib",
        "pip": "pip install matplotlib numpy",
        "docs": "https://matplotlib.org",
        "license": "PSF License",
        "tagline": "The foundational publication-grade 2D/3D visualization engine for the scientific Python ecosystem.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / MULTI-PANEL GRIDSPEC",
                "title": "Hierarchical Multi-Axis GridSpec Architecture",
                "subtitle": "Complex subplot arrangement with non-uniform row/column ratios and twin axis projections.",
                "math_desc": "Subplot coordinate affine transformation matrix: $T: (x, y) \\mapsto (M x + t_x, N y + t_y)$ mapping normalized figure coordinates $[0,1]^2$ to display pixel targets.",
                "math_formula": "P_{\\text{pixel}} = \\mathbf{M}_{\\text{disp}} \\cdot \\mathbf{M}_{\\text{axes}} \\cdot \\mathbf{M}_{\\text{data}} \\cdot P_{\\text{data}}",
                "time_complexity": "O(N) rendering passes",
                "space_complexity": "O(N) display list",
                "enterprise_use": "Aerospace flight recorder analysis, clinical drug trial pharmacokinetic/pharmacodynamic multi-tier panels.",
                "strengths": "Pixel-perfect publication alignment, arbitrary artist customization, complete backend independence.",
                "tradeoffs": "Verbose imperative API requiring manual canvas layout orchestration.",
                "metrics": [
                    {"label": "Backend", "val": "Agg / Vector", "sub": "Anti-Grain Geometry"},
                    {"label": "Max Nodes", "val": "500,000", "sub": "Scatter Cap"},
                    {"label": "Layout", "val": "GridSpec2D", "sub": "Constrained Spacing"},
                    {"label": "License", "val": "PSF Open", "sub": "Enterprise Safe"}
                ],
                "code": """import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Synthetic telemetry stream
t = np.linspace(0, 10, n_samples)
signal = np.sin(t) + np.random.normal(0, noise, n_samples)
spectrum = np.abs(np.fft.rfft(signal))

fig = plt.figure(figsize=(10, 6), facecolor='#050806')
gs = gridspec.GridSpec(2, 2, height_ratios=[2, 1], width_ratios=[3, 1], hspace=0.3, wspace=0.25)

ax_main = fig.add_subplot(gs[0, 0], facecolor='#0a110d')
ax_main.plot(t, signal, color='#00e676', lw=1.5, label='Raw Sensor Stream')
ax_main.set_title('Time-Series Signal Acquisition', color='#fffefa', fontsize=12)
ax_main.tick_params(colors='#94a3b8')

ax_fft = fig.add_subplot(gs[1, 0], facecolor='#0a110d')
ax_fft.plot(spectrum, color='#f3cf65', lw=1.2)
ax_fft.set_title('Fast Fourier Spectral Density', color='#fffefa', fontsize=10)
ax_fft.tick_params(colors='#94a3b8')

ax_hist = fig.add_subplot(gs[:, 1], facecolor='#0a110d')
ax_hist.hist(signal, bins=25, orientation='horizontal', color='#00e5ff', alpha=0.7)
ax_hist.set_title('Amplitude Probability Distribution', color='#fffefa', fontsize=10)
ax_hist.tick_params(colors='#94a3b8')

plt.show()"""
            },
            {
                "tag": "02 / CONTINUOUS STREAMPLOT",
                "title": "2D Vector Field & Streamline Integration",
                "subtitle": "Runge-Kutta numerical integration visualizing magnetic flux and fluid dynamic velocity fields.",
                "math_desc": "Streamline vector field trajectory governed by the autonomous ODE: $\\frac{d\\mathbf{r}}{ds} = \\frac{\\mathbf{v}(\\mathbf{r})}{\\|\\mathbf{v}(\\mathbf{r})\\|}$ integrated using 4th-order Runge-Kutta (RK4).",
                "math_formula": "\\mathbf{r}_{n+1} = \\mathbf{r}_n + \\frac{\\Delta s}{6}(k_1 + 2k_2 + 2k_3 + k_4)",
                "time_complexity": "O(W \\times H) cell rasterization",
                "space_complexity": "O(W \\times H) grid matrix",
                "enterprise_use": "Computational fluid dynamics (CFD) airflow simulation around automotive fuselages, wind turbine micro-siting.",
                "strengths": "Dense flow visualization with adaptive streamline density and vector color-mapping.",
                "tradeoffs": "Requires regular Cartesian grid interpolation for unstructured mesh points.",
                "metrics": [
                    {"label": "Method", "val": "RK4 ODE", "sub": "Adaptive Step"},
                    {"label": "Grid Size", "val": "200x200", "sub": "Regular Mesh"},
                    {"label": "Velocity", "val": "Vector Norm", "sub": "Colormapped"},
                    {"label": "Format", "val": "Matplotlib Agg", "sub": "Native Vector"}
                ],
                "code": """import matplotlib.pyplot as plt
import numpy as np

Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)

fig, ax = plt.subplots(figsize=(8, 6), facecolor='#050806')
ax.set_facecolor('#0a110d')

stream = ax.streamplot(X, Y, U, V, color=speed, cmap='plasma', density=1.4, linewidth=1.2, arrowsize=1.2)
fig.colorbar(stream.lines, ax=ax, label='Velocity Magnitude (m/s)')
ax.set_title('Phase Space Flow Dynamics', color='#fffefa')
ax.tick_params(colors='#94a3b8')

plt.show()"""
            },
            {
                "tag": "03 / 3D PARAMETRIC SURFACE",
                "title": "3D Parametric Mesh with Orthographic Shadowing",
                "subtitle": "Surface topology projection across rotating viewpoint angles with lighting shading normals.",
                "math_desc": "Parametric surface elevation: $z = f(x,y) = \\sin(\\sqrt{x^2+y^2}) / \\sqrt{x^2+y^2}$ mapped across a 2D meshgrid with Gouraud smooth surface shading.",
                "math_formula": "I_p = k_a I_a + k_d (\\mathbf{L} \\cdot \\mathbf{N}) I_d + k_s (\\mathbf{R} \\cdot \\mathbf{V})^n I_s",
                "time_complexity": "O(N^2) surface tessellation",
                "space_complexity": "O(N^2) face normal buffer",
                "enterprise_use": "Semiconductor wafer topography profiling, terrain elevation model (DEM) visualization.",
                "strengths": "Built-in mplot3d projection with zero external C++ dependencies.",
                "tradeoffs": "Lacks true GPU z-buffer hardware depth testing; relies on artist painter's algorithm.",
                "metrics": [
                    {"label": "Engine", "val": "mplot3d", "sub": "Painter's Sort"},
                    {"label": "Mesh Faces", "val": "10,000+", "sub": "Triangulated"},
                    {"label": "Colormap", "val": "Viridis", "sub": "Perceptual"},
                    {"label": "Shading", "val": "Phong/Gouraud", "sub": "Surface Normals"}
                ],
                "code": """import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

X = np.linspace(-5, 5, 60)
Y = np.linspace(-5, 5, 60)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2) + 0.001
Z = np.sin(R) / R

fig = plt.figure(figsize=(9, 6), facecolor='#050806')
ax = fig.add_subplot(111, projection='3d', facecolor='#050806')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9, antialiased=True)
ax.view_init(elev=35, azim=45)
ax.set_title('Parametric Wavefield Topology', color='#fffefa')
fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()"""
            }
        ]
    },
    {
        "name": "Seaborn",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Seaborn",
        "pip": "pip install seaborn pandas matplotlib",
        "docs": "https://seaborn.pydata.org",
        "license": "BSD 3-Clause",
        "tagline": "Statistical data visualization framework unifying statistical estimation with beautiful visual themes.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / JOINT PROBABILITY GRID",
                "title": "Bivariate JointGrid with Marginal KDE & Rug Overlays",
                "subtitle": "Unifies joint multivariate correlation density with 1D univariate distribution symmetry.",
                "math_desc": "2D Gaussian kernel density estimation: $\\hat{f}(x,y) = \\frac{1}{n h_x h_y} \\sum_{i=1}^n K\\left(\\frac{x - x_i}{h_x}\\right) K\\left(\\frac{y - y_i}{h_y}\\right)$ with Scott bandwidth factor.",
                "math_formula": "h = n^{-1/(d+4)} \\cdot \\hat{\\sigma}",
                "time_complexity": "O(N^2) pairwise kernel evaluation",
                "space_complexity": "O(K \\times M) grid contour buffer",
                "enterprise_use": "Customer lifetime value (LTV) vs Acquisition cost (CAC) clustering, biometric clinical trials.",
                "strengths": "One-line statistical modeling with confidence interval estimation and automatic aggregation.",
                "tradeoffs": "Coupled to Matplotlib backend; not optimized for streaming data.",
                "metrics": [
                    {"label": "Method", "val": "Bivariate KDE", "sub": "JointGrid"},
                    {"label": "Bandwidth", "val": "Scott's Rule", "sub": "Optimal h"},
                    {"label": "Marginals", "val": "KDE + Hist", "sub": "Aligned Axes"},
                    {"label": "Data Input", "val": "Tidy DataFrame", "sub": "Pandas Native"}
                ],
                "code": """import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate bivariate financial cohort data
np.random.seed(42)
adr = np.random.normal(250, 45, n_samples)
occ = np.clip(100 - (adr * 0.15) + np.random.normal(0, noise*20, n_samples), 10, 95)
df = pd.DataFrame({'ADR': adr, 'Occupancy': occ})

g = sns.JointGrid(data=df, x='ADR', y='Occupancy', height=7)
g.plot_joint(sns.kdeplot, fill=True, cmap='emerald', thresh=0.05)
g.plot_marginals(sns.histplot, kde=True, color='#00e676', bins=20)
g.fig.patch.set_facecolor('#050806')
g.ax_joint.set_facecolor('#0a110d')

plt.show()"""
            },
            {
                "tag": "02 / HIERARCHICAL CLUSTERMAP",
                "title": "Clustered Heatmap with Dual Hierarchical Dendrograms",
                "subtitle": "Unsupervised UPGMA agglomerative clustering ordering gene or feature interaction matrices.",
                "math_desc": "Euclidean metric distance matrix $D_{ij} = \\|\\mathbf{x}_i - \\mathbf{x}_j\\|_2$ clustered iteratively via Ward's minimum variance criterion.",
                "math_formula": "d(u, v) = \\sqrt{\\frac{|s| + |u|}{|s| + |u| + |v|} d(s,u)^2 + \\frac{|s| + |v|}{|s| + |u| + |v|} d(s,v)^2 - \\frac{|s|}{|s| + |u| + |v|} d(u,v)^2}",
                "time_complexity": "O(N^3) standard Ward clustering",
                "space_complexity": "O(N^2) pairwise distance matrix",
                "enterprise_use": "Microarray genomic expression profiles, multi-asset financial cross-correlation matrices.",
                "strengths": "Reveals latent categorical grouping and modular structure in dense numerical matrices.",
                "tradeoffs": "Computationally prohibitive for matrices with $N > 5000$ without GPU acceleration.",
                "metrics": [
                    {"label": "Algorithm", "val": "Ward Hierarchical", "sub": "Agglomerative"},
                    {"label": "Linkage", "val": "SciPy Cluster", "sub": "Dual Dendrogram"},
                    {"label": "Normalization", "val": "Z-score Scale", "sub": "Per Feature"},
                    {"label": "Colormap", "val": "Spectral / Magma", "sub": "Diverging"}
                ],
                "code": """import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.randn(30, 20)
df = pd.DataFrame(data, columns=[f'Gene_{i}' for i in range(20)])

g = sns.clustermap(df.corr(), cmap='magma', standard_scale=1, figsize=(8, 8),
                   dendrogram_ratio=(0.15, 0.15), cbar_pos=(0.02, 0.8, 0.03, 0.15))
g.fig.patch.set_facecolor('#050806')

plt.show()"""
            }
        ]
    },
    {
        "name": "Plotly Py (Plotly.py - Dash)",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Plotly Py (Plotly.py - Dash)",
        "pip": "pip install plotly dash pandas",
        "docs": "https://plotly.com/python",
        "license": "MIT License",
        "tagline": "Declarative interactive WebGL and D3 charting engine with full Dash web application integration.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / HARDWARE WEBGL SCATTER",
                "title": "Million-Point Hardware WebGL Scatter & Density",
                "subtitle": "Direct GPU shader buffer mapping supporting smooth 60 FPS zoom, box-select, and lasso queries.",
                "math_desc": "WebGL vertex buffer attribute streaming: $\\mathbf{V}_{xy} = \\text{Float32Array}(\\{x_i, y_i\\})$ rendered via GPU instancing with custom vertex and fragment shaders.",
                "math_formula": "\\text{gl\\_Position} = \\mathbf{P}_{\\text{matrix}} \\cdot \\mathbf{V}_{\\text{matrix}} \\cdot \\text{vec4}(x, y, 0.0, 1.0)",
                "time_complexity": "O(N) GPU pipeline pass",
                "space_complexity": "O(N) VRAM buffer",
                "enterprise_use": "Autonomous vehicle sensor telemetry point clouds, high-frequency equity tick trade feeds.",
                "strengths": "Fluid browser interactivity, zero server round-trips for pan/zoom, built-in SVG/PNG export.",
                "tradeoffs": "Large standalone HTML bundle sizes (Plotly.js is ~3.5MB uncompressed).",
                "metrics": [
                    {"label": "Rendering", "val": "WebGL / Shaders", "sub": "GPU Accelerated"},
                    {"label": "Scale", "val": "1,000,000 Pts", "sub": "60 FPS Refresh"},
                    {"label": "Format", "val": "JSON Spec", "sub": "Plotly.js Bound"},
                    {"label": "Framework", "val": "Dash Native", "sub": "Reactive Callbacks"}
                ],
                "code": """import plotly.graph_objects as go
import numpy as np

N = n_samples * 100
x = np.random.randn(N)
y = np.random.randn(N)
colors = np.sqrt(x**2 + y**2)

fig = go.Figure(data=go.Scattergl(
    x=x, y=y,
    mode='markers',
    marker=dict(
        size=3,
        color=colors,
        colorscale='Viridis',
        showscale=True,
        opacity=0.8
    )
))

fig.update_layout(
    template='plotly_dark',
    title='Million-Point WebGL Accelerated Scatter',
    paper_bgcolor='#050806',
    plot_bgcolor='#0a110d'
)
fig.show()"""
            },
            {
                "tag": "02 / 3D VOLUMETRIC ISOSURFACE",
                "title": "3D Implicit Scalar Field Isosurface Extraction",
                "subtitle": "Marching cubes isosurface reconstruction with interactive 3D rotation, slicing caps, and lighting normals.",
                "math_desc": "Isosurface contour extraction satisfying $S(x,y,z) = c$ interpolated across regular 3D voxel cells via tetrahedral cell decomposition.",
                "math_formula": "S(x,y,z) = x^2 + y^2 - z^2 - \\alpha = 0",
                "time_complexity": "O(V) voxel evaluation",
                "space_complexity": "O(T) triangulated mesh buffer",
                "enterprise_use": "Medical MRI/CT volumetric organ scanning, reservoir geological porosity modeling.",
                "strengths": "Interactive 3D orbit directly in browser with cap slicing and dynamic threshold sliders.",
                "tradeoffs": "Demands client-side GPU memory; initial mesh triangulation can take ~1-2s.",
                "metrics": [
                    {"label": "Engine", "val": "Plotly 3D WebGL", "sub": "Marching Cubes"},
                    {"label": "Voxel Grid", "val": "40x40x40", "sub": "64,000 Voxels"},
                    {"label": "Cap Slicing", "val": "Realtime Ortho", "sub": "X, Y, Z Planes"},
                    {"label": "Shading", "val": "Specular Normals", "sub": "Lighting Shader"}
                ],
                "code": """import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]
values = X**2 + Y**2 - Z**2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(), y=Y.flatten(), z=Z.flatten(),
    value=values.flatten(),
    isomin=-5, isomax=15,
    surface_count=3,
    caps=dict(x_show=False, y_show=False),
    colorscale='Plasma'
))

fig.update_layout(
    scene=dict(bgcolor='#050806'),
    paper_bgcolor='#050806',
    title='3D Scalar Field Quadric Isosurface'
)
fig.show()"""
            }
        ]
    },
    {
        "name": "Bokeh",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Bokeh",
        "pip": "pip install bokeh pandas",
        "docs": "https://bokeh.org",
        "license": "BSD 3-Clause",
        "tagline": "Interactive streaming visualization library with Python-JavaScript two-way websocket bindings.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / LINKED STREAMING BRUSHING",
                "title": "Two-Way Linked Brushing via ColumnDataSource",
                "subtitle": "Coordinates selections across multiple scatter and histogram plots via client-side JavaScript callbacks.",
                "math_desc": "Bidirectional selection index mask $\\mathcal{I}_{\\text{selected}} = \\{i \\mid x_i \\in [x_{\\min}, x_{\\max}] \\land y_i \\in [y_{\\min}, y_{\\max}]\\}$ broadcast across linked views.",
                "math_formula": "\\mathcal{S}_{\\text{hist}}(b) = \\sum_{i \\in \\mathcal{I}_{\\text{selected}}} \\mathbb{I}(v_i \\in \\text{bin}_b)",
                "time_complexity": "O(N) index filtering",
                "space_complexity": "O(N) shared ColumnDataSource buffer",
                "enterprise_use": "Semiconductor defect yield analysis, real-time IoT manufacturing telemetry dashboards.",
                "strengths": "Rich Python-JS two-way server protocol (`bokeh serve`) with zero JavaScript writing required.",
                "tradeoffs": "Requires running Bokeh server daemon for real-time Python callback bindings.",
                "metrics": [
                    {"label": "Data Bridge", "val": "ColumnDataSource", "sub": "Shared Memory"},
                    {"label": "Server", "val": "Tornado Async", "sub": "WebSockets"},
                    {"label": "Brushing", "val": "Cross-Plot Linked", "sub": "Client Side JS"},
                    {"label": "Canvas", "val": "HTML5 2D", "sub": "BokehJS"}
                ],
                "code": """from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, BoxSelectTool
from bokeh.layouts import gridplot
import numpy as np

source = ColumnDataSource(data=dict(
    x=np.random.randn(n_samples),
    y=np.random.randn(n_samples),
    z=np.random.rand(n_samples)
))

p1 = figure(width=400, height=350, tools="pan,box_select,reset", background_fill_color="#0a110d")
p1.scatter('x', 'y', source=source, color="#00e676", alpha=0.6, selection_color="#f3cf65")

p2 = figure(width=400, height=350, tools="pan,box_select,reset", background_fill_color="#0a110d")
p2.scatter('x', 'z', source=source, color="#00e5ff", alpha=0.6, selection_color="#f3cf65")

grid = gridplot([[p1, p2]])
show(grid)"""
            }
        ]
    },
    {
        "name": "Altair",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Altair",
        "pip": "pip install altair pandas",
        "docs": "https://altair-viz.github.io",
        "license": "BSD 3-Clause",
        "tagline": "Declarative statistical grammar of graphics based on Vega and Vega-Lite specifications.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / DECLARATIVE GRAMMAR SPLOM",
                "title": "Interactive Scatter Plot Matrix (SPLOM) with Interval Selection",
                "subtitle": "Coordinates multi-dimensional feature selections across all pairwise projections via declarative bindings.",
                "math_desc": "Declarative visual encoding mapping: $\\phi: (D, \\tau) \\mapsto (X, Y, C, S)$ expressing channel mappings without procedural canvas loops.",
                "math_formula": "\\text{Spec} = \\left\\{ \\text{data}: D, \\text{mark}: M, \\text{encoding}: \\{\\text{x}: \\text{Field}_1, \\text{y}: \\text{Field}_2, \\text{color}: \\text{Field}_3\\} \\right\\}",
                "time_complexity": "O(N) declarative evaluation",
                "space_complexity": "O(N) JSON payload",
                "enterprise_use": "Exploratory data analysis in genomics, financial multi-factor credit risk scoring.",
                "strengths": "Concise declarative API, highly reusable specs, direct export to Vega-Lite web dashboards.",
                "tradeoffs": "Dataset size capped at ~5,000 rows by default to avoid browser DOM memory bloat.",
                "metrics": [
                    {"label": "Grammar", "val": "Vega-Lite Spec", "sub": "Pure JSON"},
                    {"label": "Selection", "val": "Interval Brush", "sub": "Linked Filter"},
                    {"label": "Data Size", "val": "< 10K Rows", "sub": "In-Memory JSON"},
                    {"label": "Rendering", "val": "Canvas / SVG", "sub": "Vega Runtime"}
                ],
                "code": """import altair as alt
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'Revenue': np.random.normal(100, 20, n_samples),
    'Spend': np.random.normal(40, 10, n_samples),
    'CAC': np.random.normal(15, 4, n_samples),
    'Cohort': np.random.choice(['Enterprise', 'Mid-Market', 'SMB'], n_samples)
})

brush = alt.selection_interval()

chart = alt.Chart(df).mark_circle(size=60).encode(
    x='Spend:Q',
    y='Revenue:Q',
    color=alt.condition(brush, 'Cohort:N', alt.value('grey')),
    tooltip=['Revenue', 'Spend', 'Cohort']
).add_params(brush)

chart.save('chart.html')"""
            }
        ]
    },
    {
        "name": "HoloViews",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "HoloViews",
        "pip": "pip install holoviews bokeh",
        "docs": "https://holoviews.org",
        "license": "BSD 3-Clause",
        "tagline": "Semantic data annotation and composable pipeline visualization framework.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / COMPOSABLE OVERLAYS",
                "title": "Composable DynamicMap & Overlay Algebra",
                "subtitle": "Combines plots with mathematical operators `*` (overlay) and `+` (layout) across continuous dimensions.",
                "math_desc": "Visual algebra: $(A * B)$ denotes layered visual composition; $(A + B)$ denotes spatial grid juxtaposition.",
                "math_formula": "\\mathcal{V}_{\\text{composite}} = \\bigoplus_{i} \\mathcal{E}_i \\otimes \\mathbf{D}",
                "time_complexity": "O(N) pipeline execution",
                "space_complexity": "O(N) semantic metadata",
                "enterprise_use": "Satellite imagery band blending, weather radar temporal scrubbing.",
                "strengths": "Separates data semantics from rendering backend (switch between Bokeh, Matplotlib, Plotly).",
                "tradeoffs": "Abstract syntax requires learning HoloViews dimensional model concepts.",
                "metrics": [
                    {"label": "Algebra", "val": "* (Overlay), + (Grid)", "sub": "Composable"},
                    {"label": "Backends", "val": "Bokeh, MPL, Plotly", "sub": "Swappable"},
                    {"label": "Streaming", "val": "DynamicMap", "sub": "Lazy Pipeline"},
                    {"label": "License", "val": "BSD 3-Clause", "sub": "Enterprise Safe"}
                ],
                "code": """import holoviews as hv
import numpy as np
hv.extension('bokeh')

t = np.linspace(0, 10, n_samples)
curve1 = hv.Curve((t, np.sin(t)), 'Time', 'Amplitude', label='Harmonic 1').opts(color='#00e676')
curve2 = hv.Curve((t, np.cos(t)), 'Time', 'Amplitude', label='Harmonic 2').opts(color='#f3cf65')

layout = (curve1 * curve2).opts(width=600, height=400, bgcolor='#0a110d')
hv.save(layout, 'holoviews_plot.html')"""
            }
        ]
    },
    {
        "name": "Pygal",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Pygal",
        "pip": "pip install pygal",
        "docs": "http://www.pygal.org",
        "license": "LGPL 3.0",
        "tagline": "Sexy, resolution-independent SVG charting library for Python with custom CSS theming.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / VECTOR SVG SPARKLINE",
                "title": "Resolution-Independent Pure SVG Radar & Gauge",
                "subtitle": "Generates lightweight vector XML nodes with embedded SVG CSS transitions and hover tooltips.",
                "math_desc": "Radial coordinate transformation: $x_i = r_i \\cos(\\theta_i), y_i = r_i \\sin(\\theta_i)$ with $\\theta_i = \\frac{2\\pi i}{K}$.",
                "math_formula": "\\mathbf{v}_i = \\left(c_x + \\rho_i R \\cos\\frac{2\\pi i}{K}, c_y + \\rho_i R \\sin\\frac{2\\pi i}{K}\\right)",
                "time_complexity": "O(N) XML string generation",
                "space_complexity": "O(N) SVG DOM footprint",
                "enterprise_use": "Automated PDF/SVG reporting engines, executive dashboard email digest attachments.",
                "strengths": "Zero JavaScript dependency, perfect print vector scaling, pure Python implementation.",
                "tradeoffs": "Limited to modest dataset sizes due to SVG DOM node rendering limits.",
                "metrics": [
                    {"label": "Output", "val": "Pure SVG XML", "sub": "No JS Needed"},
                    {"label": "Styling", "val": "Custom CSS", "sub": "Web Themeable"},
                    {"label": "Size", "val": "< 50 KB", "sub": "Lightweight"},
                    {"label": "Interactivity", "val": "Native Tooltips", "sub": "SVG Elements"}
                ],
                "code": """import pygal
from pygal.style import DarkGreenBlueStyle

radar_chart = pygal.Radar(fill=True, style=DarkGreenBlueStyle)
radar_chart.title = 'Enterprise Cyber Threat Surface Assessment'
radar_chart.x_labels = ['Auth', 'Network', 'Endpoint', 'Cloud', 'Data Integrity', 'IAM']
radar_chart.add('Production Node A', [85, 92, 78, 95, 88, 70])
radar_chart.add('Staging Node B', [65, 75, 60, 80, 72, 55])

radar_chart.render_to_file('radar_chart.svg')"""
            }
        ]
    },
    {
        "name": "Plotnine (ggplot2 implementation)",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Plotnine (ggplot2 implementation)",
        "pip": "pip install plotnine pandas",
        "docs": "https://plotnine.readthedocs.io",
        "license": "MIT License",
        "tagline": "A complete implementation of the Grammar of Graphics in Python, matching R's ggplot2.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / GRAMMAR FACETED STAT",
                "title": "Grammar of Graphics Faceted Regression with Error Bands",
                "subtitle": "Declarative layered grammar mapping aesthetics `aes()` to data variables with statistical smoothers.",
                "math_desc": "Local polynomial regression smoother: $\\hat{y}(x) = \\arg\\min_\\beta \\sum_{i=1}^n w_i(x) (y_i - \\mathbf{x}_i^T \\beta)^2$ across categorical facet panels.",
                "math_formula": "w_i(x) = W\\left(\\frac{|x - x_i|}{h(x)}\\right)",
                "time_complexity": "O(K \\times N) regression fits",
                "space_complexity": "O(N) aesthetic mapping",
                "enterprise_use": "Econometric policy analysis, academic scientific papers requiring standard ggplot2 layout.",
                "strengths": "Familiar syntax for R/ggplot2 data scientists, strict layer composability.",
                "tradeoffs": "Inherits Matplotlib rendering overhead; not suited for streaming animation.",
                "metrics": [
                    {"label": "Grammar", "val": "Wilkinson Grammar", "sub": "Layered"},
                    {"label": "Backend", "val": "Matplotlib Agg", "sub": "Vector"},
                    {"label": "Faceting", "val": "facet_wrap()", "sub": "Multi-Panel"},
                    {"label": "Smoother", "val": "LOESS / OLS", "sub": "Stat Model"}
                ],
                "code": """from plotnine import ggplot, aes, geom_point, geom_smooth, facet_wrap, theme_dark
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Engine_Size': np.random.uniform(1.2, 5.0, n_samples),
    'Emissions': np.random.uniform(100, 350, n_samples),
    'Vehicle_Type': np.random.choice(['SUV', 'Sedan', 'Truck'], n_samples)
})

plot = (
    ggplot(df, aes(x='Engine_Size', y='Emissions', color='Vehicle_Type'))
    + geom_point(alpha=0.7)
    + geom_smooth(method='lm')
    + facet_wrap('~Vehicle_Type')
    + theme_dark()
)
plot.save('plotnine_chart.png')"""
            }
        ]
    },
    {
        "name": "Chartify",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Chartify",
        "pip": "pip install chartify pandas",
        "docs": "https://github.com/spotify/chartify",
        "license": "Apache 2.0",
        "tagline": "Spotify's opinionated Python charting library for quick, brand-consistent executive charts.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / OPINIONATED EXECUTIVE CHART",
                "title": "Dual-Axis Revenue Callout & Brand Consistency",
                "subtitle": "Enforces corporate typography, standardized margins, and callout annotations automatically.",
                "math_desc": "Automatic baseline normalization and dual-scale linear mapping aligning primary revenue with secondary margin percentages.",
                "math_formula": "y_{\\text{scaled}} = \\frac{y - y_{\\min}}{y_{\\max} - y_{\\min}} \\cdot H",
                "time_complexity": "O(N) plot assembly",
                "space_complexity": "O(N) Bokeh scenegraph",
                "enterprise_use": "Board decks, executive shareholder presentations, corporate quarterly business reviews.",
                "strengths": "Guarantees brand aesthetic compliance without manual margin or font tweaking.",
                "tradeoffs": "Less flexible for non-standard or bespoke 3D/scientific plots.",
                "metrics": [
                    {"label": "Author", "val": "Spotify Lab", "sub": "Enterprise Tested"},
                    {"label": "Backend", "val": "Bokeh Engine", "sub": "HTML5 Canvas"},
                    {"label": "Design", "val": "Opinionated", "sub": "Zero Ugly Defaults"},
                    {"label": "Output", "val": "Interactive HTML", "sub": "PNG/SVG Export"}
                ],
                "code": """import chartify
import pandas as pd
import numpy as np

ch = chartify.Chart(blank_labels=True, y_axis_type='linear')
ch.set_title("Quarterly Enterprise SaaS ARR Growth")
ch.set_subtitle("Direct distribution scaling from Q1 2024 to Q4 2026")

df = pd.DataFrame({
    'quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'arr': [12.5, 16.8, 22.4, 31.0]
})

ch.plot.bar(data_frame=df, categorical_columns='quarter', numeric_column='arr', color_column='quarter')
ch.callout.text(text="Project Meta Deployed (+56%)", x='Q3', y=22.4)
ch.save('chartify_output.html')"""
            }
        ]
    },
    {
        "name": "HVPlot",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "HVPlot",
        "pip": "pip install hvplot pandas dask",
        "docs": "https://hvplot.holoviz.org",
        "license": "BSD 3-Clause",
        "tagline": "Familiar high-level `.hvplot()` API for Pandas, Dask, XArray, and Polars dataframes.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / SEAMLESS DATAFRAME EXTENSION",
                "title": "Interactive Streaming Time-Series with Zero Boilerplate",
                "subtitle": "Adds one-line interactive Bokeh and Datashader capabilities directly onto DataFrame objects.",
                "math_desc": "Lazy pipeline query translation from tabular expressions to reactive HoloViews streams.",
                "math_formula": "\\mathbf{Plot} = \\text{DataFrame}.\\text{hvplot}(\\text{params})",
                "time_complexity": "O(N) streamed data pass",
                "space_complexity": "O(N) in-memory buffer",
                "enterprise_use": "High-velocity financial trading backtests, IoT fleet battery monitoring.",
                "strengths": "Direct drop-in replacement for `df.plot()` with full interactivity.",
                "tradeoffs": "Requires installing the broader HoloViz ecosystem dependencies.",
                "metrics": [
                    {"label": "API", "val": "df.hvplot()", "sub": "Pandas Integrated"},
                    {"label": "Dask Support", "val": "Native Out-of-Core", "sub": "Distributed"},
                    {"label": "Interactive", "val": "Pan, Zoom, Hover", "sub": "Bokeh Canvas"},
                    {"label": "Streaming", "val": "Streamz Aware", "sub": "Real-time"}
                ],
                "code": """import hvplot.pandas
import pandas as pd
import numpy as np

dates = pd.date_range('2026-01-01', periods=n_samples)
df = pd.DataFrame({
    'Revenue': np.cumsum(np.random.normal(500, 50, n_samples)),
    'Commission_Savings': np.cumsum(np.random.normal(120, 20, n_samples))
}, index=dates)

plot = df.hvplot.line(
    title='Direct Channel Commercial Recapture Velocity',
    width=700, height=400,
    cmap=['#00e676', '#f3cf65']
)
hvplot.save(plot, 'hvplot_output.html')"""
            }
        ]
    },
    {
        "name": "bqplot",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "bqplot",
        "pip": "pip install bqplot ipywidgets",
        "docs": "https://bqplot.readthedocs.io",
        "license": "Apache 2.0",
        "tagline": "Two-way interactive 2D plotting system for Jupyter based on grammar of graphics and ipywidgets.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / JUPYTER TWO-WAY BINDING",
                "title": "Interactive Traitlets-Driven Regression Line Fitting",
                "subtitle": "Two-way synchronizes plot selections and Python kernel variables via Jupyter Comm channels.",
                "math_desc": "Event-driven callback loop: moving a graphical mark on screen updates Python state variables directly in memory.",
                "math_formula": "\\Delta \\mathbf{\\theta}_{\\text{kernel}} \\propto \\text{Event}_{\\text{drag}}(P_{\\text{mark}})",
                "time_complexity": "O(N) mark re-rendering",
                "space_complexity": "O(N) Jupyter Comm buffer",
                "enterprise_use": "Interactive financial risk simulation in Jupyter, human-in-the-loop ML annotation.",
                "strengths": "True two-way state binding between client JavaScript and Python kernel.",
                "tradeoffs": "Tightly coupled to Jupyter widget architecture.",
                "metrics": [
                    {"label": "Architecture", "val": "ipywidgets Traitlets", "sub": "Two-Way Comm"},
                    {"label": "Renderer", "val": "d3.js", "sub": "Client DOM"},
                    {"label": "Kernel", "val": "IPython", "sub": "State Sync"},
                    {"label": "Interaction", "val": "Brush & Lasso", "sub": "Mark Dragging"}
                ],
                "code": """from bqplot import LinearScale, Axis, Lines, Figure
import numpy as np

x_sc = LinearScale()
y_sc = LinearScale()

x_data = np.linspace(0.0, 10.0, n_samples)
y_data = np.sin(x_data)

line = Lines(x=x_data, y=y_data, scales={'x': x_sc, 'y': y_sc}, colors=['#00e676'])
ax_x = Axis(scale=x_sc, label='Index')
ax_y = Axis(scale=y_sc, orientation='vertical', label='Target')

fig = Figure(marks=[line], axes=[ax_x, ax_y], title='bqplot Traitlet Pipeline')"""
            }
        ]
    },
    {
        "name": "Leather",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Leather",
        "pip": "pip install leather",
        "docs": "https://leather.readthedocs.io",
        "license": "MIT License",
        "tagline": "Python charting library for those who need simple charts right now without dependencies.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / ZERO-DEPENDENCY SVG",
                "title": "Minimalist Zero-Dependency Vector Plotter",
                "subtitle": "Renders pure XML SVG graphics using standard library strings without NumPy or SciPy.",
                "math_desc": "Linear scalar interpolation mapping domain $[A, B]$ to range $[0, W]$.",
                "math_formula": "x_{\\text{svg}} = \\frac{x - A}{B - A} \\cdot W",
                "time_complexity": "O(N) pure Python iteration",
                "space_complexity": "O(N) string buffer",
                "enterprise_use": "Embedded IoT devices, zero-footprint microservices, automated CLI reporting scripts.",
                "strengths": "Ultra-lightweight, zero binary dependencies, instant execution in pure Python.",
                "tradeoffs": "No advanced statistical models or complex interactive controls.",
                "metrics": [
                    {"label": "Dependencies", "val": "Zero (Pure Py)", "sub": "No NumPy Needed"},
                    {"label": "Output", "val": "Native SVG", "sub": "Vector XML"},
                    {"label": "Footprint", "val": "< 100 KB", "sub": "Microservice Safe"},
                    {"label": "Execution", "val": "< 5ms", "sub": "Instantaneous"}
                ],
                "code": """import leather

chart = leather.Chart('Operational Cost vs Margin')
data = [(1, 3), (2, 5), (3, 8), (4, 12), (5, 18)]
chart.add_line(data, color='#00e676')
chart.to_svg('leather_chart.svg')"""
            }
        ]
    },
    {
        "name": "Veusz",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Veusz",
        "pip": "pip install veusz",
        "docs": "https://veusz.github.io",
        "license": "GPL 2.0+",
        "tagline": "Scientific plotting and graphing package designed to produce publication-ready vector graphics.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / PUBLICATION SCIENTIFIC EXPORT",
                "title": "Publication-Grade Vector Hierarchy with Error Ellipses",
                "subtitle": "Modular widget-tree architecture generating EPS, PDF, and SVG with LaTeX font rendering.",
                "math_desc": "Confidence covariance ellipse parametric equation: $(\\mathbf{x} - \\mu)^T \\mathbf{\\Sigma}^{-1} (\\mathbf{x} - \\mu) = \\chi_p^2(\\alpha)$.",
                "math_formula": "\\lambda_1, \\lambda_2 = \\text{eig}(\\mathbf{\\Sigma})",
                "time_complexity": "O(N) vector drawing pass",
                "space_complexity": "O(N) node tree",
                "enterprise_use": "Peer-reviewed academic physics journals, patent documentation figures.",
                "strengths": "Dual interface: Python scripting API plus interactive Qt GUI editor.",
                "tradeoffs": "Qt dependency required for GUI functionality.",
                "metrics": [
                    {"label": "Output", "val": "EPS / PDF / SVG", "sub": "Print Ready"},
                    {"label": "Fonts", "val": "LaTeX Math", "sub": "Typeset"},
                    {"label": "Interface", "val": "CLI + Qt GUI", "sub": "Dual Mode"},
                    {"label": "License", "val": "GPL 2.0+", "sub": "Academic Core"}
                ],
                "code": """import veusz.embed as veusz

embed = veusz.Embedded('Veusz Scientific Studio')
embed.To(embed.Add('page'))
embed.To(embed.Add('graph'))
embed.SetData('x', [1, 2, 3, 4, 5])
embed.SetData('y', [2.5, 4.2, 5.8, 8.1, 9.4])
embed.Add('xy', xData='x', yData='y', marker='circle', Color='#00e676')
embed.Export('veusz_plot.svg')"""
            }
        ]
    },
    {
        "name": "GR Framework",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "GR Framework",
        "pip": "pip install gr",
        "docs": "https://gr-framework.org",
        "license": "MIT License",
        "tagline": "Universal framework for visualization applications with microsecond-level C rendering speed.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / ULTRA-FAST REALTIME OSCILLOSCOPE",
                "title": "Sub-Millisecond 1,000,000 Point Oscilloscope Stream",
                "subtitle": "Direct compiled C-engine pipeline executing at hundreds of frames per second for high-rate telemetry.",
                "math_desc": "Memory-mapped contiguous array streaming directly to underlying C workstation graphics primitives.",
                "math_formula": "T_{\\text{latency}} < 500 \\mu\\text{s} \\quad \\forall N \\le 10^6",
                "time_complexity": "O(N) raw memory copy",
                "space_complexity": "O(1) in-place buffer",
                "enterprise_use": "High-frequency algorithmic trading market depth feeds, particle accelerator beam telemetry.",
                "strengths": "Fastest rendering library in scientific Python (orders of magnitude faster than Matplotlib).",
                "tradeoffs": "Lower level API; less declarative than Seaborn or Altair.",
                "metrics": [
                    {"label": "Engine", "val": "Compiled C Core", "sub": "GR Kernel"},
                    {"label": "Framerate", "val": "200+ FPS", "sub": "Sub-millisecond"},
                    {"label": "Capacity", "val": "10M Points", "sub": "Realtime"},
                    {"label": "Latency", "val": "< 0.5 ms", "sub": "Ultra-Low"}
                ],
                "code": """import gr
import numpy as np

x = np.linspace(0, 10, n_samples)
y = np.sin(x) + np.random.normal(0, noise, n_samples)

gr.clearws()
gr.setviewport(0.1, 0.95, 0.1, 0.95)
gr.setwindow(0, 10, -2, 2)
gr.polyline(x, y)
gr.axes(1, 0.5, 0, 0, 2, 2, -0.01)
gr.updatews()"""
            }
        ]
    },
    {
        "name": "Visvis",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Visvis",
        "pip": "pip install visvis pyopengl",
        "docs": "https://github.com/almarklein/visvis",
        "license": "BSD 3-Clause",
        "tagline": "Object-oriented plotting framework for 1D, 2D, 3D and 4D volumetric visualization on OpenGL.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / VOLUMETRIC 3D TEXTURE",
                "title": "4D Spatio-Temporal Volumetric Texture Rendering",
                "subtitle": "Direct OpenGL 3D texture rendering with transfer function color mapping and interactive camera axes.",
                "math_desc": "Ray-casting voxel line integral: $C = \\int_0^L c(s) \\tau(s) \\exp\\left(-\\int_0^s \\tau(t) dt\\right) ds$.",
                "math_formula": "T_i = \\prod_{j=1}^{i-1} (1 - \\alpha_j)",
                "time_complexity": "O(W \\times H \\times D) ray marching",
                "space_complexity": "O(W \\times H \\times D) 3D texture buffer",
                "enterprise_use": "Atmospheric climate plume dispersal simulations, seismic acoustic inversion 3D cubes.",
                "strengths": "Native support for multi-dimensional volumetric numpy arrays in OpenGL.",
                "tradeoffs": "Legacy codebase, primarily maintenance mode.",
                "metrics": [
                    {"label": "Backend", "val": "OpenGL Textures", "sub": "Direct GPU"},
                    {"label": "Dimension", "val": "1D to 4D", "sub": "Volume Ready"},
                    {"label": "Camera", "val": "Full Orbit / Pan", "sub": "Interactive"},
                    {"label": "License", "val": "BSD 3-Clause", "sub": "Permissive"}
                ],
                "code": """import visvis as vv
import numpy as np

vol = np.random.normal(0, 1, (40, 40, 40))
app = vv.use()
f = vv.clf()
a = vv.cla()
vv.volshow(vol, renderStyle='mip')
app.Run()"""
            }
        ]
    },
    {
        "name": "Chaco",
        "category": "Statistical, Charting & Core Plotting",
        "folder": "Chaco",
        "pip": "pip install chaco traitsui",
        "docs": "https://docs.enthought.com/chaco",
        "license": "BSD 3-Clause",
        "tagline": "Enthought's component-based interactive scientific plotting toolkit with high performance C-drawing.",
        "peers": PEERS_CAT1,
        "paradigms": [
            {
                "tag": "01 / COMPONENT PLOT ARCHITECTURE",
                "title": "Modular Data Component Architecture with Custom Overlays",
                "subtitle": "Decouples data arrays, coordinate transforms, renderers, and interactive tools into reusable Trait components.",
                "math_desc": "Component pipeline: $\\mathbf{DataSource} \\longrightarrow \\mathbf{Mapper} \\longrightarrow \\mathbf{PlotRenderer} \\longrightarrow \\mathbf{OverlayTool}$.",
                "math_formula": "\\mathcal{C}_{\\text{view}} = \\mathcal{T}_{\\text{tool}} \\circ \\mathcal{R}_{\\text{render}}(\\mathcal{M}_{\\text{map}}(\\mathcal{D}_{\\text{source}}))",
                "time_complexity": "O(N) vector drawing",
                "space_complexity": "O(N) traits cache",
                "enterprise_use": "Petroleum geology reservoir modeling software (Enthought Canopy platform).",
                "strengths": "Clean architectural decoupling, custom interactive tool composition.",
                "tradeoffs": "Heavy Enthought toolchain dependency (Traits, TraitsUI, Kiva).",
                "metrics": [
                    {"label": "Architecture", "val": "Traits MVC", "sub": "Component Tree"},
                    {"label": "Drawing", "val": "Kiva C-Engine", "sub": "Hardware Vector"},
                    {"label": "Tools", "val": "Custom Overlays", "sub": "Pan / Zoom / Lasso"},
                    {"label": "Enterprise", "val": "Oil & Gas Scientific", "sub": "Mission Critical"}
                ],
                "code": """from chaco.api import Plot, ArrayPlotData
from traits.api import HasTraits, Instance
import numpy as np

class LinePlot(HasTraits):
    plot = Instance(Plot)
    def __init__(self):
        super().__init__()
        x = np.linspace(0, 10, n_samples)
        y = np.sin(x)
        data = ArrayPlotData(x=x, y=y)
        self.plot = Plot(data)
        self.plot.plot(('x', 'y'), type='line', color='#00e676')"""
            }
        ]
    }
]
