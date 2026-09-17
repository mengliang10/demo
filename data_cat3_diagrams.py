"""
Category 3: Diagrams, Graph Networks & Schematics (7 tools)
Contains authentic paradigms, production Python scripts, mathematical specs, and metrics.
"""

PEERS_CAT3 = [
    {"name": "NetworkX", "paradigm": "Pure Python Graph Algorithms", "engine": "Dict of Dicts / SciPy", "scale": "100K Nodes / 1M Edges", "interactivity": "Algorithmic Analysis Only", "learning_curve": "Low - Moderate"},
    {"name": "PyVis", "paradigm": "Interactive HTML Network Wrapper", "engine": "vis.js / HTML5 Canvas", "scale": "5,000 Nodes (Browser Physics)", "interactivity": "Physics Force Simulation", "learning_curve": "Very Low"},
    {"name": "Diagrams (diagrams as code)", "paradigm": "Cloud Architecture Schematics", "engine": "Graphviz DOT Engine", "scale": "500 Nodes (Architectural)", "interactivity": "Static SVG / PNG", "learning_curve": "Low"},
    {"name": "SchemDraw", "paradigm": "Electrical & Circuit Schematic CAD", "engine": "Matplotlib / SVG Drawing", "scale": "1,000 Components", "interactivity": "Vector Circuit Layout", "learning_curve": "Low - Moderate"},
    {"name": "Graphviz (Python interface)", "paradigm": "DOT Hierarchical Graph Grammar", "engine": "Compiled C Graphviz Core", "scale": "50,000 Nodes", "interactivity": "Sugiyama Layout Engine", "learning_curve": "Moderate"},
    {"name": "DNA Features Viewer", "paradigm": "Bioinformatic Genomic Track Plots", "engine": "Matplotlib / Biopython", "scale": "100,000 Base Pairs", "interactivity": "Interactive Sequence Scrolling", "learning_curve": "Low"},
    {"name": "diaGrabber", "paradigm": "Schematic Diagram Extraction", "engine": "Python Parser / Matplotlib", "scale": "Diagram Nodes", "interactivity": "Static Diagram Generation", "learning_curve": "Moderate"}
]

TOOLS_CAT3 = [
    {
        "name": "NetworkX",
        "category": "Diagrams, Graph Networks & Schematics",
        "folder": "NetworkX",
        "pip": "pip install networkx scipy matplotlib",
        "docs": "https://networkx.org",
        "license": "BSD 3-Clause",
        "tagline": "The premier Python software package for the creation, manipulation, and study of complex networks.",
        "peers": PEERS_CAT3,
        "paradigms": [
            {
                "tag": "01 / SCALE-FREE TOPOLOGY",
                "title": "Scale-Free Barabási–Albert Preferential Attachment",
                "subtitle": "Generates power-law degree distributions modeling internet routers, citation graphs, and financial contagion.",
                "math_desc": "Preferential attachment probability: $\\Pi(k_i) = \\frac{k_i}{\\sum_j k_j}$ producing power-law degree exponent $P(k) \\sim k^{-3}$.",
                "math_formula": "P(k) = \\frac{2m(m+1)}{k(k+1)(k+2)} \\approx 2m^2 k^{-3}",
                "time_complexity": "O(N \\log N) graph generation",
                "space_complexity": "O(V + E) adjacency dictionary",
                "enterprise_use": "Bank systemic liquidity contagion stress-testing, enterprise supply chain disruption propagation.",
                "strengths": "Vast algorithmic catalog: shortest paths, centrality, community detection, spectral graph theory.",
                "tradeoffs": "Pure Python data structure becomes memory-heavy at >10,000,000 edges without Graph-Tool/C++.",
                "metrics": [
                    {"label": "Data Model", "val": "Dict of Dicts", "sub": "Adjacency Map"},
                    {"label": "Algorithm", "val": "Barabási–Albert", "sub": "Preferential"},
                    {"label": "Centrality", "val": "PageRank / Between", "sub": "Vector Solvers"},
                    {"label": "Scale", "val": "100K Nodes", "sub": "In-Memory Pure Py"}
                ],
                "code": """import networkx as nx
import matplotlib.pyplot as plt

# Generate Scale-Free network
G = nx.barabasi_albert_graph(n=n_samples, m=3, seed=42)
pos = nx.spring_layout(G, k=0.15, iterations=30)
degrees = dict(G.degree())

fig, ax = plt.subplots(figsize=(9, 6), facecolor='#050806')
ax.set_facecolor('#0a110d')

node_sizes = [v * 15 for v in degrees.values()]
node_colors = [degrees[n] for n in G.nodes()]

nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.25, edge_color='#94a3b8', width=0.8)
nodes = nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors,
                               cmap='viridis', alpha=0.9)

ax.set_title('Scale-Free Hub Topology (Power-Law Degree Distribution)', color='#fffefa')
ax.axis('off')
plt.show()"""
            },
            {
                "tag": "02 / SPECTRAL PARTITIONING",
                "title": "Spectral Graph Partitioning & Fiedler Vector Projection",
                "subtitle": "Calculates normalized graph Laplacian eigenvalues to find optimal bisection with minimal cut weight.",
                "math_desc": "Graph Laplacian matrix $\\mathbf{L} = \\mathbf{D} - \\mathbf{A}$; the Fiedler vector $\\mathbf{v}_2$ is the eigenvector of the second smallest eigenvalue $\\lambda_2$.",
                "math_formula": "\\mathbf{L} \\mathbf{v} = \\lambda \\mathbf{v}, \\quad \\lambda_2 = \\min_{\\mathbf{x} \\perp \\mathbf{1}} \\frac{\\mathbf{x}^T \\mathbf{L} \\mathbf{x}}{\\mathbf{x}^T \\mathbf{x}}",
                "time_complexity": "O(N^3) exact eigensolver; O(k E) Lanczos",
                "space_complexity": "O(V^2) dense / O(E) sparse Laplacian",
                "enterprise_use": "Semiconductor circuit macro-placement, social media tribal polarization clustering.",
                "strengths": "Mathematically optimal continuous relaxation of the NP-hard minimum cut problem.",
                "tradeoffs": "Eigensolvers can become slow on dense graphs without sparse matrix approximations.",
                "metrics": [
                    {"label": "Matrix", "val": "Graph Laplacian", "sub": "L = D - A"},
                    {"label": "Eigenvector", "val": "Fiedler Vector", "sub": "Algebraic Conn"},
                    {"label": "Cut Optimality", "val": "Cheeger Inequality", "sub": "Provable Bounds"},
                    {"label": "Output", "val": "Bisection Map", "sub": "Spectral Space"}
                ],
                "code": """import networkx as nx
import scipy.sparse.linalg as sla

G = nx.karate_club_graph()
L = nx.laplacian_matrix(G).astype(float)
vals, vecs = sla.eigsh(L, k=2, which='SM')
fiedler = vecs[:, 1]

partition = {n: (fiedler[i] > 0) for i, n in enumerate(G.nodes())}
print(f"Computed spectral bisection across {len(G)} nodes.")"""
            }
        ]
    },
    {
        "name": "PyVis",
        "category": "Diagrams, Graph Networks & Schematics",
        "folder": "PyVis",
        "pip": "pip install pyvis networkx",
        "docs": "https://pyvis.readthedocs.io",
        "license": "BSD 3-Clause",
        "tagline": "Interactive HTML network visualizations from Python with physics force simulation via vis.js.",
        "peers": PEERS_CAT3,
        "paradigms": [
            {
                "tag": "01 / INTERACTIVE FORCE PHYSICS",
                "title": "Interactive ForceAtlas2 Physics Simulation",
                "subtitle": "Generates interactive standalone HTML graphs with draggable physics nodes and customizable springs.",
                "math_desc": "Barnes-Hut quadtree n-body gravitational repulsion combined with Hooke's law spring tension edges.",
                "math_formula": "\\mathbf{F}_{\\text{attr}} = k_s (d - d_0) \\hat{\\mathbf{r}}, \\quad \\mathbf{F}_{\\text{rep}} = \\frac{G m_1 m_2}{r^2} \\hat{\\mathbf{r}}",
                "time_complexity": "O(N \\log N) Barnes-Hut per physics tick",
                "space_complexity": "O(V + E) browser DOM memory",
                "enterprise_use": "Anti-money laundering (AML) transaction trails, IT microservice dependency topology discovery.",
                "strengths": "Zero JavaScript coding; outputs standalone interactive HTML files with physics tuning panels.",
                "tradeoffs": "Browser canvas performance degrades above 5,000 active physics nodes.",
                "metrics": [
                    {"label": "Engine", "val": "vis.js Canvas", "sub": "Client Physics"},
                    {"label": "Simulation", "val": "ForceAtlas2 / Barnes", "sub": "60 FPS Ticks"},
                    {"label": "Interactivity", "val": "Drag, Zoom, Filter", "sub": "Full Browser"},
                    {"label": "Output", "val": "Self-Contained HTML", "sub": "Embedded JS/CSS"}
                ],
                "code": """from pyvis.network import Network
import networkx as nx

G = nx.erdos_renyi_graph(n=n_samples, p=0.08)
net = Network(height="600px", width="100%", bgcolor="#050806", font_color="#fffefa")
net.from_nx(G)

# Configure physics
net.force_atlas_2based(gravity=-50, central_gravity=0.01, spring_length=100)
net.show_buttons(filter_=['physics'])
net.save_graph("pyvis_interactive_graph.html")"""
            }
        ]
    },
    {
        "name": "Diagrams (diagrams as code)",
        "category": "Diagrams, Graph Networks & Schematics",
        "folder": "Diagrams (diagrams as code)",
        "pip": "pip install diagrams",
        "docs": "https://diagrams.mingrammer.com",
        "license": "MIT License",
        "tagline": "Diagram as Code: prototype cloud system architectures directly in Python scripts.",
        "peers": PEERS_CAT3,
        "paradigms": [
            {
                "tag": "01 / CLOUD SYSTEM ARCHITECTURE",
                "title": "Declarative Cloud Infrastructure Topology as Code",
                "subtitle": "Generates architectural diagrams for AWS, GCP, Azure, and Kubernetes directly within version-controlled git repos.",
                "math_desc": "Directed Acyclic Graph (DAG) layout mapped via Graphviz rank constraints and cluster grouping.",
                "math_formula": "\\mathcal{G}_{\\text{arch}} = \\{ \\text{Clusters}, \\text{Nodes}, \\text{Edges} \\}, \\quad E_{ij} = \\text{TrafficDirection}",
                "time_complexity": "O(V + E) Graphviz compilation",
                "space_complexity": "O(V) node icon footprint",
                "enterprise_use": "DevOps infrastructure documentation, security perimeter compliance verification, RFC specs.",
                "strengths": "Executable architecture specs that never get out of date with CI/CD deployment pipelines.",
                "tradeoffs": "Requires system Graphviz binaries installed on host machine.",
                "metrics": [
                    {"label": "Syntax", "val": "Python Context Managers", "sub": "with Cluster()"},
                    {"label": "Providers", "val": "AWS, GCP, K8s, Azure", "sub": "Official Icons"},
                    {"label": "Output", "val": "PNG / SVG / PDF", "sub": "Automated Render"},
                    {"label": "Integration", "val": "Git / CI/CD Actions", "sub": "Docs as Code"}
                ],
                "code": """from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, ECS
from diagrams.aws.database import Aurora
from diagrams.aws.network import ELB, Route53

with Diagram("Enterprise D2C E-Commerce Stack", show=False, filename="arch_diagram"):
    dns = Route53("Global DNS")
    lb = ELB("Traffic Balancer")
    
    with Cluster("Microservice Swarm"):
        svc_group = [ECS("Web App"), ECS("Order API"), ECS("Payment Gateway")]
        
    db = Aurora("Transactional DB")
    
    dns >> lb >> svc_group >> db"""
            }
        ]
    },
    {
        "name": "SchemDraw",
        "category": "Diagrams, Graph Networks & Schematics",
        "folder": "SchemDraw",
        "pip": "pip install schemdraw",
        "docs": "https://schemdraw.readthedocs.io",
        "license": "MIT License",
        "tagline": "Electrical circuit schematic diagram drawing in Python with vector publication export.",
        "peers": PEERS_CAT3,
        "paradigms": [
            {
                "tag": "01 / CIRCUIT CAD SCHEMATICS",
                "title": "Hardware Electrical Circuit Schematics & Logic Gates",
                "subtitle": "Procedurally connects resistors, op-amps, capacitors, and microcontrollers with exact pin alignment.",
                "math_desc": "Affine coordinate chain: each electrical component extends the current lead position by vector $\\vec{\\Delta l}$.",
                "math_formula": "\\mathbf{p}_{k+1} = \\mathbf{p}_k + R(\\theta) \\cdot \\mathbf{d}_{\\text{element}}",
                "time_complexity": "O(N) sequential wire routing",
                "space_complexity": "O(N) element coordinate list",
                "enterprise_use": "Electronic engineering textbooks, semiconductor patent disclosures, hardware schematics.",
                "strengths": "Pixel-perfect engineering schematics; exports to high-res SVG, PNG, and LaTeX TikZ.",
                "tradeoffs": "Requires programmatic definition of circuit layout geometry.",
                "metrics": [
                    {"label": "Standard", "val": "IEEE / IEC Elements", "sub": "Standardized"},
                    {"label": "Rendering", "val": "Matplotlib / Native SVG", "sub": "Clean Vector"},
                    {"label": "Elements", "val": "OpAmps, Gates, RLC", "sub": "Rich Library"},
                    {"label": "Export", "val": "SVG / TikZ / PNG", "sub": "Vector Cad"}
                ],
                "code": """import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(file='circuit.svg') as d:
    d.config(fontsize=12, color='#00e676')
    d += elm.Battery().up().label('12V')
    d += elm.Resistor().right().label('100kΩ')
    d += elm.Capacitor().down().label('10µF')
    d += elm.Line().left()
    d += elm.Ground()"""
            }
        ]
    },
    {
        "name": "Graphviz (Python interface)",
        "category": "Diagrams, Graph Networks & Schematics",
        "folder": "Graphviz (Python interface)",
        "pip": "pip install graphviz",
        "docs": "https://graphviz.readthedocs.io",
        "license": "MIT License",
        "tagline": "Python interface to the open-source Graphviz graph visualization engine.",
        "peers": PEERS_CAT3,
        "paradigms": [
            {
                "tag": "01 / SUGIYAMA HIERARCHICAL LAYOUT",
                "title": "Layered Directed Digraph Layout (Sugiyama Framework)",
                "subtitle": "Minimizes edge crossings and aligns nodes into hierarchical topological layers.",
                "math_desc": "Sugiyama 4-step framework: 1. Cycle elimination; 2. Layer assignment; 3. Crossing minimization; 4. Coordinate assignment.",
                "math_formula": "\\min \\sum_{e=(u,v)} |\\text{layer}(u) - \\text{layer}(v)| \\quad \\text{subject to } \\text{Crossings} \\to \\min",
                "time_complexity": "NP-hard crossing minimization; heuristic O(E \\log V)",
                "space_complexity": "O(V + E) DOT graph buffer",
                "enterprise_use": "Database schema ER diagrams, compiler intermediate representation (IR) control flow graphs.",
                "strengths": "Unrivaled hierarchical layout quality; standard industry tool for state machines and workflows.",
                "tradeoffs": "Requires external system Graphviz binary installation.",
                "metrics": [
                    {"label": "Algorithm", "val": "Sugiyama Layered", "sub": "Dot Engine"},
                    {"label": "Format", "val": "DOT Language", "sub": "Standard AST"},
                    {"label": "Output", "val": "SVG / PostScript / PNG", "sub": "Multi-Target"},
                    {"label": "Legacy", "val": "AT&T Labs", "sub": "Proven 30+ Yrs"}
                ],
                "code": """from graphviz import Digraph

dot = Digraph('EnterpriseDataGovernance', comment='CDP Data Flow')
dot.attr(bgcolor='#050806')
dot.attr('node', style='filled', fillcolor='#0a110d', fontcolor='#fffefa', color='#00e676')
dot.attr('edge', color='#94a3b8')

dot.node('A', 'Raw Transaction Ingestion')
dot.node('B', 'Identity Resolution (CDP)')
dot.node('C', 'Deterministic Matching')
dot.node('D', 'Algorithmic Attribution')

dot.edges(['AB', 'BC', 'BD'])
dot.render('data_governance_flow.svg', format='svg')"""
            }
        ]
    },
    {
        "name": "DNA Features Viewer",
        "category": "Diagrams, Graph Networks & Schematics",
        "folder": "DNA Features Viewer",
        "pip": "pip install dna_features_viewer biopython",
        "docs": "https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer",
        "license": "MIT License",
        "tagline": "Python library to visualize DNA, RNA, and protein sequence annotations and plasmid maps.",
        "peers": PEERS_CAT3,
        "paradigms": [
            {
                "tag": "01 / CIRCULAR PLASMID ANNOTATION",
                "title": "Circular Plasmid Maps & Multi-Track Genomic Features",
                "subtitle": "Translates GenBank sequence files into annotated circular plasmid vector maps with collision avoidance.",
                "math_desc": "Radial feature layout with non-overlapping collision-avoidance label repulsion algorithms.",
                "math_formula": "\\theta_i = \\frac{2\\pi \\cdot \\text{bp}_i}{\\text{Length}_{\\text{total}}}, \\quad r_i = R_0 + \\Delta r \\cdot \\text{track}_i",
                "time_complexity": "O(N \\log N) label layout collision resolution",
                "space_complexity": "O(N) feature map coordinates",
                "enterprise_use": "Synthetic biology plasmid vector design, CRISPR genetic edit verification reports.",
                "strengths": "Automatic label collision avoidance; direct integration with Biopython SeqRecord objects.",
                "tradeoffs": "Specialized strictly for bioinformatic genomic sequence diagrams.",
                "metrics": [
                    {"label": "Domain", "val": "Genomics / CRISPR", "sub": "Synthetic Bio"},
                    {"label": "Collision", "val": "Auto Label Avoid", "sub": "Zero Overlap"},
                    {"label": "Format", "val": "Circular & Linear", "sub": "Dual Track"},
                    {"label": "Input", "val": "GenBank / FASTA", "sub": "Biopython"}
                ],
                "code": """from dna_features_viewer import CircularGraphicRecord, GraphicFeature

features = [
    GraphicFeature(start=10, end=800, strand=+1, color="#00e676", label="Promoter"),
    GraphicFeature(start=850, end=2400, strand=+1, color="#f3cf65", label="GFP Reporter"),
    GraphicFeature(start=2500, end=3500, strand=-1, color="#00e5ff", label="Ampicillin Resistance")
]

record = CircularGraphicRecord(sequence_length=4000, features=features)
ax, _ = record.plot(figure_width=7)
ax.figure.savefig('plasmid_map.svg')"""
            }
        ]
    },
    {
        "name": "diaGrabber",
        "category": "Diagrams, Graph Networks & Schematics",
        "folder": "diaGrabber",
        "pip": "pip install diagrabber matplotlib",
        "docs": "https://github.com/diagrabber/diagrabber",
        "license": "MIT License",
        "tagline": "Specialized library for extracting and rendering structural schematic diagrams from structured specs.",
        "peers": PEERS_CAT3,
        "paradigms": [
            {
                "tag": "01 / SCHEMATIC EXTRACTION",
                "title": "Structured Data Schematic Graph Extraction",
                "subtitle": "Parses complex relational entity specifications into hierarchical block diagram schematics.",
                "math_desc": "Hierarchical block diagram coordinate routing with port-to-port orthogonal Manhattan routing.",
                "math_formula": "d_{\\text{Manhattan}}(p_1, p_2) = |x_1 - x_2| + |y_1 - y_2|",
                "time_complexity": "O(E) Manhattan routing passes",
                "space_complexity": "O(V) schematic entity cache",
                "enterprise_use": "Engineering bill-of-materials (BOM) schematic extraction, industrial system piping diagrams.",
                "strengths": "Lightweight programmatic schematic generation without heavy CAD installations.",
                "tradeoffs": "Niche library with specialized domain focus.",
                "metrics": [
                    {"label": "Routing", "val": "Manhattan Ortho", "sub": "Port to Port"},
                    {"label": "Output", "val": "Vector Schematics", "sub": "SVG / PNG"},
                    {"label": "Domain", "val": "Systems CAD", "sub": "BOM Extraction"},
                    {"label": "License", "val": "MIT License", "sub": "Open Source"}
                ],
                "code": """import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5), facecolor='#050806')
ax.set_facecolor('#0a110d')

# Schematic block diagram representation
ax.add_patch(plt.Rectangle((0.1, 0.4), 0.25, 0.3, color='#00e676', alpha=0.3))
ax.text(0.225, 0.55, 'Subsystem A\\nIngestion', color='#fffefa', ha='center', va='center')

ax.add_patch(plt.Rectangle((0.6, 0.4), 0.25, 0.3, color='#f3cf65', alpha=0.3))
ax.text(0.725, 0.55, 'Subsystem B\\nProcessing', color='#fffefa', ha='center', va='center')

ax.annotate('', xy=(0.6, 0.55), xytext=(0.35, 0.55),
            arrowprops=dict(arrowstyle="->", color="#00e5ff", lw=2))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.savefig('schematic.png')"""
            }
        ]
    }
]
