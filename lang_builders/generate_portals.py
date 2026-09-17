"""
Generates executive hub index.html files for each of the 6 visualization language folders.
"""
import os

BASE_DIR = "/run/media/ml/Storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software"

LANG_METADATA = {
    "R Visualization": {
        "title": "R Statistical & Graphic Ecosystem",
        "lang_tag": "R / Bioconductor / CRAN",
        "accent_color": "#276dc3",
        "accent_glow": "rgba(39, 109, 195, 0.4)",
        "desc": "Enterprise statistical computing, grammar of graphics layered geometry, reactive web dashboards, and high-dimensional geospatial & network topologies.",
        "packages": [
            {
                "id": "ggplot2",
                "folder": "ggplot2",
                "file": "ggplot2_studio.html",
                "title": "ggplot2",
                "tag": "Grammar of Graphics & Geometries",
                "desc": "Layered aesthetic mappings (aes), non-linear transformations, statistical summaries, and publication-ready multi-facet visual decomposition.",
                "math": r"\text{Plot} = \text{Data} + \sum \text{Geom}_i(\text{Stat}_i(\text{Aesthetics})) + \text{Coord} + \text{Facets}",
                "use_case": "Clinical trial drug response analysis, genomic microarray variance studies."
            },
            {
                "id": "plotly",
                "folder": "plotly",
                "file": "plotly_studio.html",
                "title": "plotly (R)",
                "tag": "WebGL Reactive Scatterplot & 3D Surfaces",
                "desc": "Hardware-accelerated WebGL plotting with sub-millisecond hover callbacks, camera orbital matrices, and cross-filter selection.",
                "math": r"\mathbf{P}_{\text{clip}} = \mathbf{M}_{\text{proj}} \times \mathbf{M}_{\text{view}} \times \mathbf{M}_{\text{model}} \times \begin{bmatrix} x & y & z & 1 \end{bmatrix}^T",
                "use_case": "Multi-asset volatility surface calibration, quantitative risk VaR stress testing."
            },
            {
                "id": "leaflet",
                "folder": "leaflet",
                "file": "leaflet_studio.html",
                "title": "leaflet (R)",
                "tag": "Geospatial Multi-Layer Topology",
                "desc": "High-density Slippy Map coordinate transformations, dynamic Voronoi coverage zones, and isochrone delivery reachability.",
                "math": r"x = \frac{R \cdot (\lambda - \lambda_0)}{180^\circ}, \quad y = R \cdot \ln\left[\tan\left(\frac{\pi}{4} + \frac{\phi}{2}\right)\right]",
                "use_case": "Last-mile supply chain logistics, municipal infrastructure sensor distribution."
            },
            {
                "id": "visNetwork",
                "folder": "visNetwork",
                "file": "visnetwork_studio.html",
                "title": "visNetwork",
                "tag": "Dynamic Force-Directed Physics Graph",
                "desc": "Barnes-Hut n-body electrical repulsion and Hooke spring dynamics for massive network clustering and community detection.",
                "math": r"\mathbf{F}_i = \sum_{j \neq i} \frac{k^2}{\|\mathbf{x}_i - \mathbf{x}_j\|^2} \hat{\mathbf{r}}_{ij} - \sum_{(i,j) \in E} \frac{\|\mathbf{x}_i - \mathbf{x}_j\|^2}{k} \hat{\mathbf{r}}_{ji}",
                "use_case": "Anti-money laundering (AML) transaction ring detection, biomedical protein interaction."
            },
            {
                "id": "shiny",
                "folder": "shiny",
                "file": "shiny_studio.html",
                "title": "shiny",
                "tag": "Reactive Execution DAG & Real-Time Parameter Sweep",
                "desc": "Inverted reactive call-graph architecture with topological dirty-propagation, client-server bidirectional WebSockets, and state serialization.",
                "math": r"\text{Dirty}(v_j) = \text{True} \iff \exists (v_i \to v_j) \in E \text{ s.t. } \text{Dirty}(v_i) = \text{True}",
                "use_case": "Executive KPI forecasting cockpits, clinical biostatistics interactive exploration."
            },
            {
                "id": "ggiraph",
                "folder": "ggiraph",
                "file": "ggiraph_studio.html",
                "title": "ggiraph",
                "tag": "Interactive SVG Geometries & Micro-Hover Tooltips",
                "desc": "Bridges ggplot2 aesthetics with client-side SVG DOM events, custom CSS selector bindings, and zero JavaScript build step dependencies.",
                "math": r"\text{Attr}_{\text{SVG}} \leftarrow \left\{ \text{onclick} = f_{\text{js}}(\text{id}_i), \; \text{data-id} = \text{hash}(x_i, y_i) \right\}",
                "use_case": "Enterprise boardroom interactive briefing decks, regulatory disclosure reports."
            },
            {
                "id": "dygraphs",
                "folder": "dygraphs",
                "file": "dygraphs_studio.html",
                "title": "dygraphs (R)",
                "tag": "High-Density Financial Microsecond Timeseries",
                "desc": "Optimized HTML5 canvas downsampling using Largest-Triangle-Three-Buckets (LTTB) algorithms for million-point time-series streams.",
                "math": r"\text{Area}(\Delta) = \frac{1}{2} |x_A(y_B - y_C) + x_B(y_C - y_A) + x_C(y_A - y_B)|",
                "use_case": "High-frequency algorithmic trading telemetry, IoT server cluster latency monitoring."
            },
            {
                "id": "corrplot",
                "folder": "corrplot",
                "file": "corrplot_studio.html",
                "title": "corrplot",
                "tag": "High-Dimensional Covariance & Correlation Matrix",
                "desc": "Hierarchical clustering reordering (hclust), eigenvalue decomposition, and bivariate confidence ellipse geometry projection.",
                "math": r"\mathbf{R} = \mathbf{D}^{-1} \mathbf{\Sigma} \mathbf{D}^{-1}, \quad r_{ij} = \frac{\text{Cov}(X_i, X_j)}{\sigma_i \sigma_j}",
                "use_case": "Quantitative portfolio factor orthogonality validation, genomics feature selection."
            }
        ]
    },
    "Julia Visualization": {
        "title": "Julia Technical & Scientific Computing Ecosystem",
        "lang_tag": "Julia / SciML / LLVM",
        "accent_color": "#9558b2",
        "accent_glow": "rgba(149, 88, 178, 0.4)",
        "desc": "Multiple-dispatch high-performance visualization, native LLVM compilation, symbolic mathematics, and differential equation phase portraits.",
        "packages": [
            {
                "id": "Makie",
                "folder": "Makie",
                "file": "makie_studio.html",
                "title": "Makie.jl",
                "tag": "GPU-Accelerated 3D Complex Function Visualizer",
                "desc": "Extensible shader pipeline (GLMakie/WGLMakie/CairoMakie) with dynamic observables and zero-copy GPU memory mapping.",
                "math": r"z = \frac{1}{2\pi} \oint_\Gamma \frac{f(\zeta)}{\zeta - z_0} d\zeta, \quad \Psi(x, y, t) = \sin(kx - \omega t) e^{-\alpha(x^2+y^2)}",
                "use_case": "Computational fluid dynamics (CFD), quantum wave-packet wave-function simulation."
            },
            {
                "id": "Plots.jl",
                "folder": "Plots.jl",
                "file": "plots_jl_studio.html",
                "title": "Plots.jl",
                "tag": "Unified Metaprogramming Pipeline & Phase Portraits",
                "desc": "Abstract recipe metaprogramming via RecipesBase.jl, unifying GR, PlotlyJS, and PyPlot behind a polymorphic dispatch API.",
                "math": r"\frac{dx}{dt} = \sigma(y - x), \quad \frac{dy}{dt} = x(\rho - z) - y, \quad \frac{dz}{dt} = xy - \beta z",
                "use_case": "Non-linear dynamical systems research, Lorenz strange attractor phase-space exploration."
            },
            {
                "id": "Pluto.jl",
                "folder": "Pluto.jl",
                "file": "pluto_jl_studio.html",
                "title": "Pluto.jl",
                "tag": "Pure Reactive Computational Notebook & Markov Chain",
                "desc": "Topologically ordered dependency DAG with hidden-state avoidance, pure functional execution, and native reactive HTML outputs.",
                "math": r"\pi^{(k+1)} = \pi^{(k)} \mathbf{P}, \quad \lim_{k \to \infty} \pi^{(k)} = \pi^* \quad \text{s.t.} \quad \pi^* \mathbf{P} = \pi^*",
                "use_case": "Reproducible scientific documentation, stochastic regime-switching credit risk models."
            },
            {
                "id": "Gadfly.jl",
                "folder": "Gadfly.jl",
                "file": "gadfly_jl_studio.html",
                "title": "Gadfly.jl",
                "tag": "Grammar of Graphics & Compositional Aesthetics",
                "desc": "Implementation of Wilkinson's Grammar of Graphics in pure Julia with Compose.jl unit vectors and functional SVG trees.",
                "math": r"\text{Spec} = \text{Coord.cartesian} \circ \text{Geom.point} \circ \text{Scale.color_continuous} \circ \text{Theme}",
                "use_case": "Automated econometric batch reporting, bioinformatic gene expression pipelines."
            },
            {
                "id": "StatsPlots.jl",
                "folder": "StatsPlots.jl",
                "file": "statsplots_jl_studio.html",
                "title": "StatsPlots.jl",
                "tag": "Kernel Density Estimation & Violin Decompositions",
                "desc": "Advanced statistical visualization macros for DataFrames, marginal histograms, and Bayesian posterior distributions.",
                "math": r"\hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^n K\left(\frac{x - X_i}{h}\right), \quad K(u) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}u^2}",
                "use_case": "Monte Carlo sensitivity auditing, clinical trial bio-distribution stratification."
            },
            {
                "id": "GraphRecipes.jl",
                "folder": "GraphRecipes.jl",
                "file": "graphrecipes_jl_studio.html",
                "title": "GraphRecipes.jl",
                "tag": "Spectral Graph Drawing & Topology Embedding",
                "desc": "Graph Laplacian spectral decomposition and eigenvector projection for clustering complex biological and network graphs.",
                "math": r"\mathbf{L} = \mathbf{D} - \mathbf{A}, \quad \mathbf{L} \mathbf{v}_k = \lambda_k \mathbf{v}_k, \quad \text{Coordinate}_i = (\mathbf{v}_2(i), \mathbf{v}_3(i))",
                "use_case": "Telecom backbone mesh fault tolerance, metabolic pathway reaction mapping."
            },
            {
                "id": "GeoMakie.jl",
                "folder": "GeoMakie.jl",
                "file": "geomakie_jl_studio.html",
                "title": "GeoMakie.jl",
                "tag": "Global Climate Projections & Orthographic Shaders",
                "desc": "Native PROJ coordinate transformations, Robinson/Winkel-Tripel spherical projections, and atmospheric isobar contours.",
                "math": r"x = \frac{2\sqrt{2}}{\pi} \lambda \cos\theta, \quad y = \sqrt{2} \sin\theta, \quad \text{where } 2\theta + \sin(2\theta) = \pi \sin\phi",
                "use_case": "Global numerical weather prediction (NWP), oceanic circulation thermal modeling."
            },
            {
                "id": "Genie.jl",
                "folder": "Genie.jl",
                "file": "genie_jl_studio.html",
                "title": "Genie.jl",
                "tag": "Full-Stack Reactive Microservice & Telemetry",
                "desc": "High-throughput web framework with Stipple.jl bidirectional reactive data channels and multi-threaded Julia execution.",
                "math": r"\Delta \mathbf{S} = \nabla_\theta \mathcal{L}(\theta) \cdot \eta, \quad \text{Latency}_{p99} \le 1.8\text{ms}",
                "use_case": "Real-time industrial IoT SCADA telemetry, automated algorithmic trading engines."
            }
        ]
    },
    "Rust VIsualization": {
        "title": "Rust High-Performance Systems & WebAssembly",
        "lang_tag": "Rust / WebGPU / WASM",
        "accent_color": "#e05d22",
        "accent_glow": "rgba(224, 93, 34, 0.4)",
        "desc": "Zero-cost abstractions, memory safety without garbage collection, WebGPU WGSL compute shaders, and instant WebAssembly rendering.",
        "packages": [
            {
                "id": "plotters",
                "folder": "plotters",
                "file": "plotters_studio.html",
                "title": "plotters",
                "tag": "Pure Rust Vector Rendering & Canvas Backend",
                "desc": "Modular 2D/3D charting engine with compile-time checked drawing backends (SVG, HTML5 Canvas, WebAssembly, BitMap).",
                "math": r"y(x) = \sum_{k=1}^K \frac{(-1)^{k-1}}{2k-1} \cos((2k-1)\omega x) e^{-\zeta \omega x}",
                "use_case": "Autonomous vehicle sensor stream telemetry, edge embedded telemetry charts."
            },
            {
                "id": "egui",
                "folder": "egui",
                "file": "egui_studio.html",
                "title": "egui",
                "tag": "Immediate Mode GUI & Real-Time DSP Oscilloscope",
                "desc": "Zero-allocation immediate layout engine running at 120 FPS in WebAssembly, generating instantaneous vertex buffers for rendering.",
                "math": r"V_{\text{out}}(t) = V_{\text{in}} \cdot \sin(\omega_0 t + \phi) + \mathcal{N}(0, \sigma^2)",
                "use_case": "Game engine internal developer tooling, high-frequency audio digital signal processing."
            },
            {
                "id": "wgpu",
                "folder": "wgpu",
                "file": "wgpu_studio.html",
                "title": "wgpu",
                "tag": "WebGPU Compute Shaders & N-Body Gravitational Physics",
                "desc": "Pure Rust native implementation of the WebGPU API with WGSL compute shaders executing parallel n-body matrix kernels.",
                "math": r"\mathbf{a}_i = G \sum_{j \neq i} \frac{m_j (\mathbf{r}_j - \mathbf{r}_i)}{(\|\mathbf{r}_j - \mathbf{r}_i\|^2 + \epsilon^2)^{3/2}}",
                "use_case": "Astrophysical planetary accretion simulations, molecular dynamics energy minimization."
            },
            {
                "id": "bevy",
                "folder": "bevy",
                "file": "bevy_studio.html",
                "title": "bevy",
                "tag": "Entity Component System (ECS) & 3D Spatial Meshes",
                "desc": "Data-driven game and simulation engine utilizing archetype-based contiguous memory layouts for cache-friendly multicore scheduling.",
                "math": r"\mathbf{x}_{t+\Delta t} = \mathbf{x}_t + \mathbf{v}_t \Delta t + \frac{1}{2} \mathbf{a}_t \Delta t^2",
                "use_case": "Digital twin smart factory floor simulation, architectural acoustics raycasting."
            },
            {
                "id": "kiss3d",
                "folder": "kiss3d",
                "file": "kiss3d_studio.html",
                "title": "kiss3d",
                "tag": "Minimalist 3D Graphics Engine & Kinematic Chains",
                "desc": "Lightweight pure Rust 3D scenegraph engine seamlessly integrated with Rapier/NPhysics for forward/inverse kinematics.",
                "math": r"\mathbf{T}_{\text{end}} = \prod_{i=1}^N \begin{bmatrix} \mathbf{R}_i(\theta_i) & \mathbf{p}_i \\ \mathbf{0}^T & 1 \end{bmatrix}",
                "use_case": "Robotic manipulator path planning, multi-axis CNC machine visual simulation."
            },
            {
                "id": "petgraph",
                "folder": "petgraph",
                "file": "petgraph_studio.html",
                "title": "petgraph",
                "tag": "Graph Theory & Minimum Spanning Tree Visualizer",
                "desc": "Cache-optimized adjacency list graph algorithms including Kruskal, Prim, and Dijkstra with zero-overhead trait dispatch.",
                "math": r"\text{MST}(G) = \arg\min_T \sum_{e \in T} w(e) \quad \text{s.t. } T \text{ spans } V \text{ and is acyclic}",
                "use_case": "Cloud VPC software-defined network routing, electrical power grid interconnect optimization."
            },
            {
                "id": "geo",
                "folder": "geo",
                "file": "geo_studio.html",
                "title": "geo",
                "tag": "Voronoi Delaunay Tessellation & Geospatial Topology",
                "desc": "Pure Rust computational geometry engine providing planar partitioning, convex hulls, and sweep-line polygon unioning.",
                "math": r"V(p_i) = \{ x \in \mathbb{R}^2 \mid \|x - p_i\| \le \|x - p_j\|, \; \forall j \neq i \}",
                "use_case": "Urban emergency response station placement, cellular tower coverage optimization."
            },
            {
                "id": "leptos",
                "folder": "leptos",
                "file": "leptos_studio.html",
                "title": "leptos",
                "tag": "Fine-Grained Reactive Web Framework & Level-2 Order Book",
                "desc": "Cutting-edge signal-based reactive framework without a virtual DOM, compiling into tiny WebAssembly payloads with zero re-rendering overhead.",
                "math": r"\text{Depth}(P) = \sum_{i: p_i = P} q_i, \quad \text{Spread} = \min(P_{\text{ask}}) - \max(P_{\text{bid}})",
                "use_case": "Crypto exchange high-frequency matching engine telemetry, institutional FX order book display."
            }
        ]
    },
    "Go Visualization": {
        "title": "Go Cloud-Native & Concurrent Systems Ecosystem",
        "lang_tag": "Go / Goroutines / Microservices",
        "accent_color": "#00add8",
        "accent_glow": "rgba(0, 173, 216, 0.4)",
        "desc": "Goroutine concurrency, high-throughput microservices, zero-dependency SVG streaming, and cross-platform native vector drivers.",
        "packages": [
            {
                "id": "go-echarts",
                "folder": "go-echarts",
                "file": "go_echarts_studio.html",
                "title": "go-echarts",
                "tag": "High-Throughput Microservice Dashboard Generator",
                "desc": "Clean idiomatic Go generator for Apache ECharts, outputting standalone HTML/JS visualizations with zero CGO dependencies.",
                "math": r"\text{Throughput} = \frac{\sum_{i=1}^M \text{Requests}_i}{\Delta t}, \quad \text{ConcurrentRoutines} \le 100{,}000",
                "use_case": "Kubernetes cluster pod metrics visualization, multi-tenant API gateway traffic monitor."
            },
            {
                "id": "gonum_plot",
                "folder": "gonum_plot",
                "file": "gonum_plot_studio.html",
                "title": "gonum/plot",
                "tag": "Scientific 2D Plotting Pipeline & Monte Carlo Walk",
                "desc": "Rigorous scientific numerical visualization library from the Gonum project, featuring typed coordinate pipelines and statistical distributions.",
                "math": r"S(t) = S_0 \exp\left(\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right)",
                "use_case": "Quantitative algorithmic derivative pricing, risk factor sensitivity backtesting."
            },
            {
                "id": "Ebitengine",
                "folder": "Ebitengine",
                "file": "ebitengine_studio.html",
                "title": "Ebitengine",
                "tag": "Hardware Blitting 2D Simulation Engine",
                "desc": "Ultra-fast dead-simple 2D simulation and game engine in Go, using direct GPU texture blitting and batching at 60 FPS.",
                "math": r"\mathbf{p}_{i, t+1} = \mathbf{p}_{i, t} + \mathbf{v}_{i, t} \Delta t + \mathbf{F}_{\text{collision}}",
                "use_case": "Autonomous warehouse robotic swarm navigation, crowd evacuation simulation."
            },
            {
                "id": "gio",
                "folder": "gio",
                "file": "gio_studio.html",
                "title": "Gio",
                "tag": "Immediate Mode Vector GUI & Minimal Instruction Stream",
                "desc": "Portable vector GUI library rendering directly to Vulkan, Metal, Direct3D, and WebAssembly with zero CGO overhead.",
                "math": r"\mathcal{I} = \{ \text{OpClipPath}, \text{OpPaint}, \text{OpTransform} \}_{n=1}^N",
                "use_case": "Embedded industrial control panels, cross-platform crypto hardware wallet UI."
            },
            {
                "id": "svgo",
                "folder": "svgo",
                "file": "svgo_studio.html",
                "title": "svgo",
                "tag": "Scalable Vector Graphics XML Streaming Engine",
                "desc": "High-speed SVG streaming engine generating architectural system topologies and circuit layouts directly to io.Writer streams.",
                "math": r"\text{XML}_{\text{Stream}} \leftarrow \prod_{k=1}^K \langle \text{polygon points}=\dots \text{fill}=\dots \rangle",
                "use_case": "Automated enterprise microservice topology diagrams, CI/CD pipeline dependency maps."
            },
            {
                "id": "chart",
                "folder": "chart",
                "file": "chart_studio.html",
                "title": "go-chart",
                "tag": "Zero-Dependency Statistical Time-Series Engine",
                "desc": "Pure Go charting library with continuous series smoothing, moving averages, and secondary axis rendering.",
                "math": r"\text{SMA}_k(t) = \frac{1}{k} \sum_{i=0}^{k-1} P(t-i), \quad \text{EMA}(t) = \alpha P(t) + (1-\alpha)\text{EMA}(t-1)",
                "use_case": "Serverless AWS Lambda telemetry charts, automated email alert PDF visualizer."
            },
            {
                "id": "go-graphviz",
                "folder": "go-graphviz",
                "file": "go_graphviz_studio.html",
                "title": "go-graphviz",
                "tag": "Dependency Graph Sugiyama Layered Layout",
                "desc": "High-performance Graphviz bindings in Go with automatic cycle breaking, rank assignment, and crossing minimization.",
                "math": r"\min_{\text{crossings}} \sum_{(u,v), (x,y) \in E} \mathbb{I}(\text{cross}(uv, xy))",
                "use_case": "Database schema migration dependency resolver, distributed tracing span graphs."
            },
            {
                "id": "fyne",
                "folder": "fyne",
                "file": "fyne_studio.html",
                "title": "fyne",
                "tag": "Cross-Platform Material Design GUI & Live Monitoring",
                "desc": "Modern retained-mode desktop and mobile UI toolkit built entirely in Go using OpenGL hardware drivers and responsive layouts.",
                "math": r"\text{Layout}(\text{Widget}) = \text{MeasureMinSize}() \times \text{ContainerScalingPolicy}",
                "use_case": "Enterprise IT operations dashboard, edge gateway diagnostic utility."
            }
        ]
    },
    "C Plus Plus Visualization": {
        "title": "C++ High-Performance & Industrial Graphics Ecosystem",
        "lang_tag": "C++17/20 / OpenGL / Vulkan",
        "accent_color": "#00599c",
        "accent_glow": "rgba(0, 89, 156, 0.4)",
        "desc": "Hardware acceleration, low-overhead SIMD pipelines, volumetric isosurface Marching Cubes, and real-time scenegraph engines.",
        "packages": [
            {
                "id": "VTK",
                "folder": "VTK",
                "file": "vtk_studio.html",
                "title": "VTK",
                "tag": "Volumetric Isosurface & Marching Cubes Algorithm",
                "desc": "Industry standard 3D scientific and medical visualization engine featuring ray-cast volume rendering and isosurface extraction.",
                "math": r"\Phi(x, y, z) = C_0, \quad \text{EdgeIntersection} = \mathbf{P}_1 + \frac{C_0 - V_1}{V_2 - V_1}(\mathbf{P}_2 - \mathbf{P}_1)",
                "use_case": "Medical MRI/CT volumetric tumor segmentation, aerospace wind-tunnel pressure fields."
            },
            {
                "id": "Dear_ImGui",
                "folder": "Dear_ImGui",
                "file": "dear_imgui_studio.html",
                "title": "Dear ImGui",
                "tag": "Bloat-Free Immediate Mode Graphical User Interface",
                "desc": "Universal developer GUI in game engines and simulation suites, outputting raw vertex and index buffers directly to graphics APIs.",
                "math": r"\text{VertexStream} = \{ (x_i, y_i), (u_i, v_i), \text{RGBA}_i \}_{i=1}^N, \quad \text{Allocations} = 0",
                "use_case": "Game engine runtime debug telemetry, robotics hardware calibration HUD."
            },
            {
                "id": "Magnum",
                "folder": "Magnum",
                "file": "magnum_studio.html",
                "title": "Magnum Engine",
                "tag": "Modular Graphics Engine & Physically Based Rendering",
                "desc": "Ultra-fast modern C++14/17/20 OpenGL and Vulkan abstraction engine with Cook-Torrance microfacet BRDF reflectance shaders.",
                "math": r"f_r = \frac{D(\mathbf{h}) F(\mathbf{v}, \mathbf{h}) G(\mathbf{l}, \mathbf{v}, \mathbf{h})}{4 (\mathbf{n} \cdot \mathbf{l})(\mathbf{n} \cdot \mathbf{v})}",
                "use_case": "Autonomous driving photorealistic lidar simulator, architectural CAD material inspection."
            },
            {
                "id": "matplotlib-cpp",
                "folder": "matplotlib-cpp",
                "file": "matplotlib_cpp_studio.html",
                "title": "matplotlib-cpp",
                "tag": "Zero-Overhead C++ CPython Embedded Charting",
                "desc": "Seamless modern C++ header-only wrapper interfacing directly with CPython C-API to plot directly from std::vector buffers.",
                "math": r"\text{Plot}(\mathbf{x}_{\text{std::vector}}, \mathbf{y}_{\text{std::vector}}) \to \text{PyObject\_CallMethod}(\dots)",
                "use_case": "C++ quantitative trading algorithmic backtester, embedded physics solver quick-plotting."
            },
            {
                "id": "Qt_Charts",
                "folder": "Qt_Charts",
                "file": "qt_charts_studio.html",
                "title": "Qt Charts",
                "tag": "Industrial SCADA Telemetry & Hardware Acceleration",
                "desc": "Comprehensive Qt Quick / QWidget enterprise charting framework built on QGraphicsScene hardware acceleration.",
                "math": r"\mathbf{T}_{\text{screen}} = \text{MatrixViewPort} \times \mathbf{D}_{\text{spline}}(t)",
                "use_case": "Semiconductor fabrication cleanroom monitoring, automotive digital cockpit instrument cluster."
            },
            {
                "id": "OpenSceneGraph",
                "folder": "OpenSceneGraph",
                "file": "openscenegraph_studio.html",
                "title": "OpenSceneGraph",
                "tag": "Hierarchical Bounding Volume Culling & Scenegraph",
                "desc": "Battle-tested 3D visual simulation engine managing complex scene hierarchies with view-frustum culling and Level-of-Detail (LOD).",
                "math": r"\text{NodeVisible} \iff \text{BoundingSphere}(c, r) \cap \text{FrustumPlanes} \neq \emptyset",
                "use_case": "Military flight simulators, GIS geospatial globe earth visualizer."
            },
            {
                "id": "OGDF",
                "folder": "OGDF",
                "file": "ogdf_studio.html",
                "title": "OGDF",
                "tag": "Fast Multipole Multilevel Graph Layout (FM³)",
                "desc": "Open Graph Drawing Framework implementing algorithmic graph theory and multipole expansions for million-node planar layouts.",
                "math": r"\Phi(\mathbf{x}) \approx \sum_{m=0}^P \frac{M_m}{\|\mathbf{x} - \mathbf{x}_0\|^{m+1}}",
                "use_case": "Biochemical metabolic pathway analysis, global telecommunication fiber layout."
            },
            {
                "id": "Ogre3D",
                "folder": "Ogre3D",
                "file": "ogre3d_studio.html",
                "title": "Ogre3D",
                "tag": "Scene-Oriented Flexible Rendering & Shader Pipeline",
                "desc": "Open-source 3D real-time graphics rendering engine with compositor post-processing pipelines and programmable vertex shaders.",
                "math": r"I = I_a k_a + I_d k_d (\mathbf{L} \cdot \mathbf{N}) + I_s k_s (\mathbf{R} \cdot \mathbf{V})^n",
                "use_case": "Medical surgical training simulation, heavy industrial crane operation virtual reality."
            }
        ]
    },
    "C Visualization": {
        "title": "C Systems Programming & Native Graphics Ecosystem",
        "lang_tag": "ANSI C / C99 / Native APIs",
        "accent_color": "#a8b9cc",
        "accent_glow": "rgba(168, 185, 204, 0.4)",
        "desc": "Minimalist low-level APIs, zero garbage collection, raw pointer arithmetic, single-header immediate-mode libraries, and WebAssembly compilation.",
        "packages": [
            {
                "id": "Raylib",
                "folder": "Raylib",
                "file": "raylib_studio.html",
                "title": "Raylib (C99)",
                "tag": "Minimalist C Graphics & Procedural Voxel Engine",
                "desc": "Pure C99 graphics library with zero external dependencies, compiling directly to HTML5/WebAssembly via Emscripten.",
                "math": r"\mathbf{v}_{\text{screen}} = \text{ViewportTransform}(\mathbf{P} \times \mathbf{V} \times \mathbf{M} \times \mathbf{v}_{\text{local}})",
                "use_case": "Procedural CAD viewers, lightweight embedded medical monitor graphics."
            },
            {
                "id": "Nuklear",
                "folder": "Nuklear",
                "file": "nuklear_studio.html",
                "title": "Nuklear",
                "tag": "ANSI C Single-Header Immediate Mode GUI",
                "desc": "Zero dynamic allocations, pure C89 immediate mode interface library designed for embedded firmware and low-spec systems.",
                "math": r"\text{DrawCommandStream} \leftarrow \text{nk\_layout\_row\_dynamic}(\dots)",
                "use_case": "Avionics cockpit control panels, embedded automotive microcontrollers."
            },
            {
                "id": "Cairo",
                "folder": "Cairo",
                "file": "cairo_studio.html",
                "title": "Cairo (C)",
                "tag": "Vector 2D Graphics Engine with Subpixel Anti-Aliasing",
                "desc": "Device-independent 2D vector drawing engine powering GTK, Mozilla Firefox, and print publication PostScript outputs.",
                "math": r"\mathbf{B}(t) = (1-t)^3 \mathbf{P}_0 + 3(1-t)^2 t \mathbf{P}_1 + 3(1-t) t^2 \mathbf{P}_2 + t^3 \mathbf{P}_3",
                "use_case": "High-precision vector typography, legal digital printing rasterizer."
            },
            {
                "id": "Graphviz",
                "folder": "Graphviz",
                "file": "graphviz_studio.html",
                "title": "Graphviz (libgvc)",
                "tag": "Native C Hierarchical Directed Graph Layout",
                "desc": "Industry foundational DAG layout library written in C, powering compiler intermediate representation (IR) graph visualizers.",
                "math": r"\min \sum_{e=(u,v)} w_e (\text{rank}(v) - \text{rank}(u))^2 \quad \text{s.t. } \text{rank}(v) \ge \text{rank}(u) + \delta",
                "use_case": "LLVM compiler register allocation DAG, database relational query planner visualization."
            },
            {
                "id": "PLplot",
                "folder": "PLplot",
                "file": "plplot_studio.html",
                "title": "PLplot",
                "tag": "Scientific Plotting Library for Mathematical Visualizations",
                "desc": "High-precision scientific plotting engine in C with device drivers for SVG, PostScript, X11, and interactive canvas buffers.",
                "math": r"z(x, y) = \frac{\sin(\sqrt{x^2 + y^2})}{\sqrt{x^2 + y^2}} \cdot \cos\left(\frac{x}{2}\right)",
                "use_case": "High-energy physics particle beam telemetry, seismic waveform wave-equation solvers."
            },
            {
                "id": "OpenGL",
                "folder": "OpenGL",
                "file": "opengl_studio.html",
                "title": "OpenGL (C)",
                "tag": "Fixed & Programmable Pipeline Shader Visualizer",
                "desc": "Direct hardware GPU shader programming pipeline utilizing GLSL vertex and fragment shaders for real-time procedural illumination.",
                "math": r"I = I_a + I_d (\mathbf{N} \cdot \mathbf{L}) + I_s (\mathbf{N} \cdot \mathbf{H})^\alpha",
                "use_case": "Real-time volumetric simulation, aerospace flight HUD displays."
            },
            {
                "id": "SDL2",
                "folder": "SDL2",
                "file": "sdl2_studio.html",
                "title": "SDL2 (C)",
                "tag": "Simple DirectMedia Layer & Multi-Threaded Audio/Video",
                "desc": "Hardware abstraction layer providing low-level access to audio, keyboard, mouse, joystick, and graphics hardware via OpenGL and Direct3D.",
                "math": r"\text{Buffer}_{\text{audio}}[n] = \sum_{k=1}^K A_k \sin\left(2\pi f_k \frac{n}{F_s} + \phi_k\right)",
                "use_case": "Multi-channel industrial acoustic diagnostic systems, cross-platform flight simulator I/O."
            }
        ]
    }
}

PORTAL_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>%%TITLE%% - Executive Demonstration Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    :root {
      --accent: %%ACCENT_COLOR%%;
      --accent-glow: %%ACCENT_GLOW%%;
      --bg-dark: #080a0f;
      --bg-card: #0f141f;
      --bg-card-hover: #161e2e;
      --border-color: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(%%ACCENT_RGB%%, 0.35);
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.6;
      background-image: 
        radial-gradient(ellipse 80% 50% at 50% -20%, var(--accent-glow), transparent 70%),
        radial-gradient(ellipse 40% 30% at 80% 80%, rgba(255, 255, 255, 0.02), transparent 100%);
    }

    /* TOP GLOBAL NAVBAR */
    .global-nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 1rem 2.5rem;
      border-bottom: 1px solid var(--border-color);
      background: rgba(8, 10, 15, 0.85);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      font-weight: 700;
      font-size: 1.15rem;
      letter-spacing: -0.02em;
    }

    .nav-badge {
      background: var(--accent);
      color: #fff;
      font-size: 0.72rem;
      font-family: 'JetBrains Mono', monospace;
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      list-style: none;
    }

    .nav-link {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      border: 1px solid transparent;
      transition: all 0.2s ease;
    }

    .nav-link:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--border-color);
    }

    .nav-link.active {
      color: #fff;
      background: rgba(%%ACCENT_RGB%%, 0.15);
      border-color: var(--border-accent);
    }

    /* HERO SECTION */
    .hero {
      padding: 4rem 2.5rem 2.5rem 2.5rem;
      max-width: 1400px;
      margin: 0 auto;
      width: 100%;
    }

    .hero-pre {
      font-family: 'JetBrains Mono', monospace;
      color: var(--accent);
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .hero-pre::before {
      content: "";
      display: inline-block;
      width: 8px;
      height: 8px;
      background: var(--accent);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--accent);
    }

    .hero h1 {
      font-size: 2.8rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.15;
      margin-bottom: 1rem;
      background: linear-gradient(135deg, #ffffff 40%, #94a3b8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero p {
      color: var(--text-muted);
      font-size: 1.15rem;
      max-width: 860px;
      line-height: 1.7;
      margin-bottom: 2rem;
    }

    /* STATS STRIP */
    .stats-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1.25rem;
      margin-bottom: 2.5rem;
    }

    .stat-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
    }

    .stat-val {
      font-size: 1.8rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: #fff;
    }

    .stat-lbl {
      color: var(--text-dim);
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-weight: 600;
      margin-top: 0.25rem;
    }

    /* SEARCH / FILTER BAR */
    .filter-bar {
      display: flex;
      gap: 1rem;
      align-items: center;
      margin-bottom: 2.5rem;
    }

    .search-input {
      flex: 1;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: #fff;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.95rem;
      padding: 0.8rem 1.2rem;
      border-radius: 8px;
      outline: none;
      transition: border-color 0.2s ease;
    }

    .search-input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 15px var(--accent-glow);
    }

    /* PACKAGE GRID */
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 1.75rem;
      margin-bottom: 4rem;
    }

    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }

    .card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, transparent, var(--accent), transparent);
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .card:hover {
      transform: translateY(-4px);
      border-color: var(--border-accent);
      background: var(--bg-card-hover);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5), 0 0 20px var(--accent-glow);
    }

    .card:hover::before {
      opacity: 1;
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.85rem;
    }

    .card-title {
      font-size: 1.45rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #fff;
    }

    .card-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--accent);
      background: rgba(%%ACCENT_RGB%%, 0.12);
      border: 1px solid rgba(%%ACCENT_RGB%%, 0.25);
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
    }

    .card-paradigm {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
    }

    .card-desc {
      color: var(--text-dim);
      font-size: 0.9rem;
      line-height: 1.6;
      margin-bottom: 1.25rem;
      flex: 1;
    }

    .card-math {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 6px;
      padding: 0.65rem 0.85rem;
      margin-bottom: 1.25rem;
      font-size: 0.82rem;
      overflow-x: auto;
    }

    .card-usecase {
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      display: flex;
      gap: 0.4rem;
    }

    .card-usecase strong {
      color: var(--text-main);
      font-weight: 600;
    }

    .card-actions {
      display: flex;
      gap: 0.75rem;
    }

    .btn {
      flex: 1;
      text-align: center;
      text-decoration: none;
      padding: 0.7rem 1rem;
      font-size: 0.85rem;
      font-weight: 700;
      border-radius: 6px;
      transition: all 0.2s ease;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
    }

    .btn-primary {
      background: var(--accent);
      color: #fff;
      border: 1px solid transparent;
    }

    .btn-primary:hover {
      background: #fff;
      color: #000;
      box-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
    }

    .btn-secondary {
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-main);
      border: 1px solid var(--border-color);
    }

    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.2);
    }

    /* FOOTER */
    footer {
      margin-top: auto;
      border-top: 1px solid var(--border-color);
      padding: 2rem 2.5rem;
      background: rgba(8, 10, 15, 0.95);
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: var(--text-dim);
      font-size: 0.85rem;
    }

    footer a {
      color: var(--text-muted);
      text-decoration: none;
    }

    footer a:hover {
      color: var(--accent);
    }
  </style>
</head>
<body>

  <!-- GLOBAL NAVIGATION -->
  <nav class="global-nav">
    <div class="nav-brand">
      <span class="nav-badge">%%LANG_TAG%%</span>
      <span>Visualization Suite</span>
    </div>
    <ul class="nav-links">
      <li><a href="../R%20Visualization/index.html" class="nav-link %%ACTIVE_R%%">R</a></li>
      <li><a href="../Julia%20Visualization/index.html" class="nav-link %%ACTIVE_JULIA%%">Julia</a></li>
      <li><a href="../Rust%20VIsualization/index.html" class="nav-link %%ACTIVE_RUST%%">Rust</a></li>
      <li><a href="../Go%20Visualization/index.html" class="nav-link %%ACTIVE_GO%%">Go</a></li>
      <li><a href="../C%20Plus%20Plus%20Visualization/index.html" class="nav-link %%ACTIVE_CPP%%">C++</a></li>
      <li><a href="../C%20Visualization/index.html" class="nav-link %%ACTIVE_C%%">C</a></li>
    </ul>
  </nav>

  <!-- HERO SECTION -->
  <div class="hero">
    <div class="hero-pre">%%LANG_TAG%% Enterprise Demonstrations</div>
    <h1>%%TITLE%%</h1>
    <p>%%DESC%%</p>

    <!-- METRICS STRIP -->
    <div class="stats-strip">
      <div class="stat-card">
        <div class="stat-val">%%PKG_COUNT%%</div>
        <div class="stat-lbl">Production Packages</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">100%</div>
        <div class="stat-lbl">Interactive Web Studios</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">0</div>
        <div class="stat-lbl">External Slide Frameworks</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">Native</div>
        <div class="stat-lbl">Code, Math & Architecture</div>
      </div>
    </div>

    <!-- FILTER / SEARCH BAR -->
    <div class="filter-bar">
      <input type="text" id="filterInput" class="search-input" placeholder="Filter packages by algorithm, name, math model, or enterprise application..." onkeyup="filterCards()">
    </div>

    <!-- PACKAGE GRID -->
    <div class="grid" id="pkgGrid">
%%CARDS_HTML%%
    </div>
  </div>

  <!-- FOOTER -->
  <footer>
    <div>Executive Visualization Demonstration Portfolio &bull; 6 Language Implementations</div>
    <div>Bespoke Pure-Code Interactive Engineering &bull; Fully Standalone HTML</div>
  </footer>

  <script>
    function filterCards() {
      const query = document.getElementById('filterInput').value.toLowerCase();
      const cards = document.querySelectorAll('.card');
      cards.forEach(card => {
        const text = card.innerText.toLowerCase();
        if (text.includes(query)) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

CARD_TEMPLATE = r"""      <div class="card">
        <div class="card-header">
          <h2 class="card-title">%%TITLE%%</h2>
          <span class="card-tag">%%FOLDER%%</span>
        </div>
        <div class="card-paradigm">%%TAG%%</div>
        <p class="card-desc">%%DESC%%</p>
        <div class="card-math">$$%%MATH%%$$</div>
        <div class="card-usecase"><strong>Enterprise:</strong> %%USE_CASE%%</div>
        <div class="card-actions">
          <a href="%%FOLDER%%/index.html" class="btn btn-primary">Launch Studio &rarr;</a>
          <a href="%%FOLDER%%/%%FILE%%" class="btn btn-secondary">Direct File</a>
        </div>
      </div>"""

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return f"{int(hex_str[0:2], 16)}, {int(hex_str[2:4], 16)}, {int(hex_str[4:6], 16)}"

def generate_all_portals():
    for lang_dir, meta in LANG_METADATA.items():
        cards_html = []
        for pkg in meta["packages"]:
            card = (CARD_TEMPLATE
                    .replace("%%TITLE%%", pkg["title"])
                    .replace("%%FOLDER%%", pkg["folder"])
                    .replace("%%FILE%%", pkg["file"])
                    .replace("%%TAG%%", pkg["tag"])
                    .replace("%%DESC%%", pkg["desc"])
                    .replace("%%MATH%%", pkg["math"])
                    .replace("%%USE_CASE%%", pkg["use_case"]))
            cards_html.append(card)
        
        all_cards = "\n".join(cards_html)
        accent_rgb = hex_to_rgb(meta["accent_color"])
        
        html_out = (PORTAL_TEMPLATE
                    .replace("%%TITLE%%", meta["title"])
                    .replace("%%LANG_TAG%%", meta["lang_tag"])
                    .replace("%%ACCENT_COLOR%%", meta["accent_color"])
                    .replace("%%ACCENT_GLOW%%", meta["accent_glow"])
                    .replace("%%ACCENT_RGB%%", accent_rgb)
                    .replace("%%DESC%%", meta["desc"])
                    .replace("%%PKG_COUNT%%", str(len(meta["packages"])))
                    .replace("%%ACTIVE_R%%", "active" if "R Visualization" in lang_dir else "")
                    .replace("%%ACTIVE_JULIA%%", "active" if "Julia" in lang_dir else "")
                    .replace("%%ACTIVE_RUST%%", "active" if "Rust" in lang_dir else "")
                    .replace("%%ACTIVE_GO%%", "active" if "Go" in lang_dir else "")
                    .replace("%%ACTIVE_CPP%%", "active" if "C Plus Plus" in lang_dir else "")
                    .replace("%%ACTIVE_C%%", "active" if lang_dir == "C Visualization" else "")
                    .replace("%%CARDS_HTML%%", all_cards))
        
        target_path = os.path.join(BASE_DIR, lang_dir, "index.html")
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html_out)
        print(f"  [✓] Generated Portal Hub: {lang_dir}/index.html ({len(html_out)/1024:.1f} KB)")

if __name__ == "__main__":
    generate_all_portals()
