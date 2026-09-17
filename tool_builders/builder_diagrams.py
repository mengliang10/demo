"""
Builder for Diagrams, Graph Networks & Schematics Tools (7 tools):
NetworkX, PyVis, Diagrams, SchemDraw, Graphviz, DNA Features Viewer, diaGrabber
Each tool gets completely different graph layouts, CAD schematics, physics engines, and interactive features!
"""

import os
import json
from .common_frame import render_tool_page
from data_cat3_diagrams import TOOLS_CAT3

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(SCRIPT_DIR, "Python Visualization, Graphical, & Interactive Libraries", "Diagrams, Graph Networks & Schematics")

def write_tool_output(tool_folder, html_content):
    target_dir = os.path.join(BASE_DIR, tool_folder)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    clean_name = tool_folder.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  [✓] {tool_folder:<35} -> Dedicated Interactive Studio Built ({len(html_content)/1024:.1f} KB)")

def build_diagrams_tools():
    tool_map = {t["folder"]: t for t in TOOLS_CAT3}

    build_networkx(tool_map["NetworkX"])
    build_pyvis(tool_map["PyVis"])
    build_diagrams(tool_map["Diagrams (diagrams as code)"])
    build_schemdraw(tool_map["SchemDraw"])
    build_graphviz(tool_map["Graphviz (Python interface)"])
    build_dna(tool_map["DNA Features Viewer"])
    build_diagrabber(tool_map["diaGrabber"])

# ==============================================================================
# 1. NETWORKX
# ==============================================================================
def build_networkx(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">NETWORKX GRAPH ALGORITHMIC SOLVER</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Layout:</label>
        <select id="nx-layout" onchange="updateNxLayout()" style="background:#070d09; color:#fff; border:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; padding:2px 6px; border-radius:4px;">
          <option value="spring" selected>spring_layout (Fruchterman-Reingold)</option>
          <option value="circular">circular_layout</option>
          <option value="spectral">spectral_layout (Laplacian Eigen)</option>
        </select>
        <button class="btn-action" onclick="findNxPath()" style="font-size:0.7rem; padding:3px 8px;">Dijkstra Shortest Path</button>
        <button class="btn-action" onclick="resampleNxGraph()" style="font-size:0.7rem; padding:3px 8px;">Re-Generate</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#040705;">
      <canvas id="nx-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>G = nx.barabasi_albert_graph(n=45, m=2); path = nx.shortest_path(G, source=0, target=target)</span>
      <span>Adjacency Dict Representation · SciPy Sparse Eigen Spectral Decomposition</span>
    </div>
    """

    custom_js = """
    let nxNodes = [];
    let nxEdges = [];
    let highlightedPath = [];

    function generateNxGraph() {
      nxNodes = [];
      nxEdges = [];
      highlightedPath = [];
      const N = 38;

      // Seed core clique
      for (let i = 0; i < 3; i++) {
        nxNodes.push({ id: i, degree: 0, x: 0, y: 0, targetX: 0, targetY: 0 });
      }
      nxEdges.push([0, 1], [1, 2], [2, 0]);
      nxNodes[0].degree = 2; nxNodes[1].degree = 2; nxNodes[2].degree = 2;

      // Preferential attachment Barabasi-Albert
      for (let i = 3; i < N; i++) {
        nxNodes.push({ id: i, degree: 0, x: 0, y: 0, targetX: 0, targetY: 0 });
        const m = 2;
        let totalDegree = nxNodes.reduce((acc, n) => acc + n.degree, 0);
        let targets = new Set();
        while (targets.size < m) {
          let rand = Math.random() * totalDegree;
          let cum = 0;
          for (let j = 0; j < i; j++) {
            cum += nxNodes[j].degree;
            if (cum >= rand) { targets.add(j); break; }
          }
        }
        for (let t of targets) {
          nxEdges.push([i, t]);
          nxNodes[i].degree++;
          nxNodes[t].degree++;
        }
      }
      computePositions();
    }

    function computePositions() {
      const mode = document.getElementById('nx-layout').value;
      const N = nxNodes.length;

      if (mode === 'circular') {
        for (let i = 0; i < N; i++) {
          const angle = (i / N) * 2 * Math.PI;
          nxNodes[i].x = Math.cos(angle) * 190;
          nxNodes[i].y = Math.sin(angle) * 190;
        }
      } else if (mode === 'spectral') {
        for (let i = 0; i < N; i++) {
          const u = (i - N/2) / (N/2);
          nxNodes[i].x = u * 240 + Math.sin(i * 1.5) * 40;
          nxNodes[i].y = (Math.pow(u, 2) - 0.5) * 160 + (nxNodes[i].degree * 8);
        }
      } else {
        // Simple force layout
        for (let i = 0; i < N; i++) {
          const angle = Math.random() * 2 * Math.PI;
          const r = 40 + Math.random() * 180;
          nxNodes[i].x = Math.cos(angle) * r;
          nxNodes[i].y = Math.sin(angle) * r;
        }
      }
      drawNxGraph();
    }

    function updateNxLayout() { computePositions(); }
    function resampleNxGraph() { generateNxGraph(); }

    function findNxPath() {
      // Breadth First Search shortest path from node 0 to furthest node
      const target = nxNodes.length - 1;
      const queue = [[0]];
      const visited = new Set([0]);
      highlightedPath = [];

      while (queue.length > 0) {
        const path = queue.shift();
        const curr = path[path.length - 1];
        if (curr === target) {
          highlightedPath = path;
          break;
        }
        // find neighbors
        const neighbors = [];
        for (let e of nxEdges) {
          if (e[0] === curr && !visited.has(e[1])) neighbors.push(e[1]);
          else if (e[1] === curr && !visited.has(e[0])) neighbors.push(e[0]);
        }
        for (let n of neighbors) {
          visited.add(n);
          queue.push([...path, n]);
        }
      }
      drawNxGraph();
    }

    function drawNxGraph() {
      const c = document.getElementById('nx-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;
      const cx = W / 2; const cy = H / 2;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      // Edges
      for (let e of nxEdges) {
        const n1 = nxNodes[e[0]];
        const n2 = nxNodes[e[1]];

        // Check if edge is in highlighted path
        let isPath = false;
        if (highlightedPath.length > 1) {
          for (let p = 0; p < highlightedPath.length - 1; p++) {
            if ((highlightedPath[p] === e[0] && highlightedPath[p+1] === e[1]) ||
                (highlightedPath[p] === e[1] && highlightedPath[p+1] === e[0])) {
              isPath = true;
              break;
            }
          }
        }

        ctx.strokeStyle = isPath ? '#00e676' : 'rgba(255, 255, 255, 0.12)';
        ctx.lineWidth = isPath ? 3 : 1;
        ctx.beginPath();
        ctx.moveTo(cx + n1.x, cy + n1.y);
        ctx.lineTo(cx + n2.x, cy + n2.y);
        ctx.stroke();
      }

      // Nodes
      for (let n of nxNodes) {
        const rad = 4 + n.degree * 2;
        const isPath = highlightedPath.includes(n.id);

        ctx.fillStyle = isPath ? '#00e676' : (n.id === 0 ? '#f3cf65' : '#00e5ff');
        ctx.beginPath();
        ctx.arc(cx + n.x, cy + n.y, rad, 0, 2*Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#040705';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '9px JetBrains Mono';
        ctx.fillText(n.id, cx + n.x + rad + 2, cy + n.y + 3);
      }

      // Banner if path highlighted
      if (highlightedPath.length > 0) {
        ctx.fillStyle = 'rgba(10, 18, 14, 0.9)';
        ctx.fillRect(20, 20, 320, 36);
        ctx.strokeStyle = '#00e676';
        ctx.strokeRect(20, 20, 320, 36);
        ctx.fillStyle = '#00e676';
        ctx.font = '11px JetBrains Mono';
        ctx.fillText(`Shortest Path [${highlightedPath.join(' → ')}]`, 32, 42);
      }
    }

    window.addEventListener('load', () => {
      generateNxGraph();
    });
    window.addEventListener('resize', drawNxGraph);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 2. PYVIS
# ==============================================================================
def build_pyvis(tool):
    extra_cdn = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" rel="stylesheet" />
    """
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">PYVIS REALTIME VIS.JS PHYSICS ENGINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="togglePyvisPhysics()" id="btn-pv-phys" style="font-size:0.7rem; padding:3px 8px;">Stabilize / Freeze</button>
        <button class="btn-action" onclick="fitPyvisGraph()" style="font-size:0.7rem; padding:3px 8px;">Center View</button>
        <button class="btn-action" onclick="addPyvisNode()" style="font-size:0.7rem; padding:3px 8px;">+ Add Node</button>
      </div>
    </div>
    <div class="canvas-body" id="pyvis-network-container" style="width:100%; height:100%; min-height:480px; background:#040705;">
      <!-- Vis.js Injected Here -->
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>net = Network(height='600px', bgcolor='#040705', font_color='white'); net.barnes_hut()</span>
      <span>Barnes-Hut Quadtree Gravitational Simulation · Draggable Interactive Nodes</span>
    </div>
    """

    custom_js = """
    let pyvisNetwork, pyvisNodes, pyvisEdges;
    let physicsActive = true;

    function initPyvisNetwork() {
      const container = document.getElementById('pyvis-network-container');
      if (!container || typeof vis === 'undefined') return;

      pyvisNodes = new vis.DataSet([
        { id: 1, label: 'Central Hub', color: '#00e676', size: 25, shape: 'dot' },
        { id: 2, label: 'Auth Gateway', color: '#00e5ff', size: 18, shape: 'dot' },
        { id: 3, label: 'Billing Pod', color: '#f3cf65', size: 16, shape: 'dot' },
        { id: 4, label: 'Postgres DB', color: '#ff1744', size: 20, shape: 'dot' },
        { id: 5, label: 'Redis Cache', color: '#d500f9', size: 16, shape: 'dot' },
        { id: 6, label: 'Analytics Worker', color: '#00e5ff', size: 14, shape: 'dot' },
        { id: 7, label: 'Edge Proxy', color: '#00e676', size: 18, shape: 'dot' }
      ]);

      pyvisEdges = new vis.DataSet([
        { from: 1, to: 2, color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 1, to: 3, color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 2, to: 4, color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 3, to: 4, color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 1, to: 5, color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 5, to: 6, color: { color: 'rgba(255,255,255,0.3)' } },
        { from: 7, to: 1, color: { color: 'rgba(255,255,255,0.3)' } }
      ]);

      const data = { nodes: pyvisNodes, edges: pyvisEdges };
      const options = {
        physics: {
          barnesHut: { gravitationalConstant: -3000, springLength: 120, springConstant: 0.04 },
          stabilization: { iterations: 100 }
        },
        interaction: { hover: true, dragNodes: true, zoomView: true },
        nodes: { font: { color: '#fffefa', face: 'JetBrains Mono', size: 12 } }
      };

      pyvisNetwork = new vis.Network(container, data, options);
    }

    function togglePyvisPhysics() {
      physicsActive = !physicsActive;
      if (pyvisNetwork) pyvisNetwork.setOptions({ physics: { enabled: physicsActive } });
      document.getElementById('btn-pv-phys').innerText = physicsActive ? 'Stabilize / Freeze' : 'Resume Physics';
    }

    function fitPyvisGraph() {
      if (pyvisNetwork) pyvisNetwork.fit({ animation: true });
    }

    let nodeCounter = 8;
    function addPyvisNode() {
      if (!pyvisNodes) return;
      const newId = nodeCounter++;
      pyvisNodes.add({ id: newId, label: `Worker_${newId}`, color: '#00e5ff', size: 14, shape: 'dot' });
      pyvisEdges.add({ from: 1, to: newId, color: { color: 'rgba(255,255,255,0.3)' } });
    }

    window.addEventListener('load', () => { setTimeout(initPyvisNetwork, 100); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 3. DIAGRAMS
# ==============================================================================
def build_diagrams(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">DIAGRAMS-AS-CODE CLOUD ARCHITECTURE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="toggleDiagTraffic()" id="btn-dia-trf" style="font-size:0.7rem; padding:3px 8px;">Simulate Traffic</button>
        <button class="btn-action" onclick="triggerFailover()" id="btn-dia-fail" style="font-size:0.7rem; padding:3px 8px;">Trigger DB Failover</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="diag-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>with Diagram('Production Cluster', show=False): DNS('Route53') >> ALB('Ingress') >> EKS('Pods') >> Aurora('DB')</span>
      <span>Graphviz DOT Layout Synthesis · Enterprise Cloud Infrastructure Architecture</span>
    </div>
    """

    custom_js = """
    let diaTraffic = true;
    let diaDbHealthy = true;
    let packetOffset = 0;

    function toggleDiagTraffic() {
      diaTraffic = !diaTraffic;
      document.getElementById('btn-dia-trf').innerText = diaTraffic ? 'Pause Traffic' : 'Simulate Traffic';
    }

    function triggerFailover() {
      diaDbHealthy = !diaDbHealthy;
      document.getElementById('btn-dia-fail').innerText = diaDbHealthy ? 'Trigger DB Failover' : 'Restore Primary DB';
    }

    function renderDiagram() {
      const c = document.getElementById('diag-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      packetOffset += 0.04;

      // Group Boxes (VPC & Clusters)
      ctx.strokeStyle = 'rgba(255,255,255,0.12)';
      ctx.fillStyle = 'rgba(255,255,255,0.02)';
      ctx.lineWidth = 1;
      ctx.strokeRect(40, 60, W - 80, H - 100);
      ctx.fillRect(40, 60, W - 80, H - 100);
      ctx.fillStyle = '#64748b';
      ctx.font = '11px JetBrains Mono';
      ctx.fillText('AWS VPC: us-east-1 (Production Enclave)', 55, 80);

      // Node layout definitions
      const nodes = [
        { id: 'dns', label: 'Route53 DNS', x: 100, y: H/2, color: '#f3cf65', icon: '🌐' },
        { id: 'alb', label: 'ALB Ingress', x: 230, y: H/2, color: '#00e5ff', icon: '⚖️' },
        { id: 'pod1', label: 'EKS Pod Alpha', x: 380, y: H/2 - 70, color: '#00e676', icon: '📦' },
        { id: 'pod2', label: 'EKS Pod Beta', x: 380, y: H/2 + 70, color: '#00e676', icon: '📦' },
        { id: 'rds_pri', label: 'Aurora Primary', x: 540, y: H/2 - 60, color: diaDbHealthy ? '#00e676' : '#ff1744', icon: '🗄️' },
        { id: 'rds_sec', label: 'Aurora Replica', x: 540, y: H/2 + 60, color: diaDbHealthy ? '#94a3b8' : '#00e676', icon: '🗄️' }
      ];

      // Draw Edges & Traffic
      const edges = [
        ['dns', 'alb'],
        ['alb', 'pod1'],
        ['alb', 'pod2'],
        ['pod1', diaDbHealthy ? 'rds_pri' : 'rds_sec'],
        ['pod2', diaDbHealthy ? 'rds_pri' : 'rds_sec']
      ];

      edges.forEach(e => {
        const n1 = nodes.find(n => n.id === e[0]);
        const n2 = nodes.find(n => n.id === e[1]);
        ctx.strokeStyle = 'rgba(255,255,255,0.2)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(n1.x, n1.y);
        ctx.lineTo(n2.x, n2.y);
        ctx.stroke();

        if (diaTraffic) {
          // Draw pulsing packet dots
          const dist = Math.sqrt(Math.pow(n2.x - n1.x, 2) + Math.pow(n2.y - n1.y, 2));
          const nDots = 4;
          for (let d = 0; d < nDots; d++) {
            const frac = ((packetOffset + d / nDots) % 1.0);
            const px = n1.x + (n2.x - n1.x) * frac;
            const py = n1.y + (n2.y - n1.y) * frac;
            ctx.fillStyle = '#00e676';
            ctx.beginPath();
            ctx.arc(px, py, 3, 0, 2*Math.PI);
            ctx.fill();
          }
        }
      });

      // Draw Node cards
      nodes.forEach(n => {
        ctx.fillStyle = '#0a140f';
        ctx.strokeStyle = n.color;
        ctx.lineWidth = 1.8;
        ctx.strokeRect(n.x - 55, n.y - 25, 110, 50);
        ctx.fillRect(n.x - 55, n.y - 25, 110, 50);

        ctx.font = '16px serif';
        ctx.textAlign = 'center';
        ctx.fillText(n.icon, n.x, n.y - 3);

        ctx.fillStyle = '#fff';
        ctx.font = '10px JetBrains Mono';
        ctx.fillText(n.label, n.x, n.y + 16);
      });

      requestAnimationFrame(renderDiagram);
    }

    window.addEventListener('load', () => { requestAnimationFrame(renderDiagram); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 4. SCHEMDRAW
# ==============================================================================
def build_schemdraw(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">SCHEMDRAW ELECTRICAL CIRCUIT CAD</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Active Probe:</label>
        <button class="btn-action" onclick="setProbe('TP1')" id="btn-tp1" style="font-size:0.7rem; padding:3px 8px;">TP1 (AC In)</button>
        <button class="btn-action" onclick="setProbe('TP2')" id="btn-tp2" style="font-size:0.7rem; padding:3px 8px;">TP2 (OpAmp Out)</button>
        <button class="btn-action" onclick="setProbe('TP3')" id="btn-tp3" style="font-size:0.7rem; padding:3px 8px;">TP3 (Filtered DC)</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#040705; display:flex; flex-direction:column; gap:8px;">
      <div style="flex:1; width:100%; position:relative;">
        <canvas id="schem-circuit-canvas" style="width:100%; height:100%; min-height:280px;"></canvas>
      </div>
      <div style="height:160px; width:100%; background:#000; border:1px solid rgba(255,255,255,0.1); border-radius:4px; padding:6px; position:relative;">
        <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--cyan-neon); margin-bottom:2px;" id="schem-probe-lbl">Virtual Oscilloscope: TP1 Input 1.0 Vpp Sine</div>
        <canvas id="schem-scope-canvas" style="width:100%; height:calc(100% - 18px);"></canvas>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>with schemdraw.Drawing() as d: d += elm.Opamp(); d += elm.Resistor().right()</span>
      <span>Vector Circuit Synthesis · Standard IEEE 315 Electrical CAD Standards</span>
    </div>
    """

    custom_js = """
    let activeProbe = 'TP1';
    let scopeTime = 0;

    function setProbe(tp) {
      activeProbe = tp;
      const desc = {
        TP1: 'Virtual Oscilloscope: TP1 AC Source (1.0 Vpp @ 1 kHz)',
        TP2: 'Virtual Oscilloscope: TP2 Inverted Amplified Output (-4.2 Vpp)',
        TP3: 'Virtual Oscilloscope: TP3 Low-Pass Filtered DC Rail (+3.3V DC)'
      }[tp];
      document.getElementById('schem-probe-lbl').innerText = desc;
    }

    function drawCircuitSchematic() {
      const c = document.getElementById('schem-circuit-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      ctx.strokeStyle = '#e2e8f0';
      ctx.lineWidth = 2;

      // AC Source
      const sx = 80; const sy = H/2;
      ctx.beginPath(); ctx.arc(sx, sy, 18, 0, 2*Math.PI); ctx.stroke();
      ctx.fillStyle = '#f3cf65'; ctx.font = '14px DM Sans'; ctx.fillText('~', sx - 4, sy + 5);

      // Lead to R1
      ctx.beginPath(); ctx.moveTo(sx + 18, sy); ctx.lineTo(sx + 80, sy); ctx.stroke();

      // TP1 probe marker
      drawTestPoint(ctx, sx + 50, sy, 'TP1', activeProbe === 'TP1');

      // Resistor R1 (zigzag)
      drawResistor(ctx, sx + 80, sy, sx + 160, sy, 'R1 (10k)');

      // Op-Amp triangle
      const opX = sx + 220; const opY = sy;
      ctx.beginPath();
      ctx.moveTo(opX, opY - 35);
      ctx.lineTo(opX + 60, opY);
      ctx.lineTo(opX, opY + 35);
      ctx.closePath();
      ctx.stroke();

      ctx.fillStyle = '#cbd5e1';
      ctx.font = '12px JetBrains Mono';
      ctx.fillText('-', opX + 8, opY - 12);
      ctx.fillText('+', opX + 8, opY + 18);

      // Output line to R2/C1
      ctx.beginPath(); ctx.moveTo(opX + 60, opY); ctx.lineTo(opX + 130, opY); ctx.stroke();
      drawTestPoint(ctx, opX + 95, opY, 'TP2', activeProbe === 'TP2');

      // Capacitor to Ground
      const capX = opX + 170;
      ctx.beginPath(); ctx.moveTo(opX + 130, opY); ctx.lineTo(capX, opY); ctx.stroke();
      drawCapacitor(ctx, capX, opY, 'C1 (100nF)');
      drawTestPoint(ctx, capX + 30, opY, 'TP3', activeProbe === 'TP3');
    }

    function drawTestPoint(ctx, x, y, label, isActive) {
      ctx.fillStyle = isActive ? '#00e676' : '#ff1744';
      ctx.beginPath(); ctx.arc(x, y, 5, 0, 2*Math.PI); ctx.fill();
      ctx.fillStyle = isActive ? '#00e676' : '#94a3b8';
      ctx.font = '10px JetBrains Mono';
      ctx.fillText(label, x - 8, y - 10);
    }

    function drawResistor(ctx, x1, y1, x2, y2, label) {
      ctx.beginPath(); ctx.moveTo(x1, y1);
      const dx = (x2 - x1) / 6;
      ctx.lineTo(x1 + dx, y1 - 10);
      ctx.lineTo(x1 + dx*2, y1 + 10);
      ctx.lineTo(x1 + dx*3, y1 - 10);
      ctx.lineTo(x1 + dx*4, y1 + 10);
      ctx.lineTo(x1 + dx*5, y1 - 10);
      ctx.lineTo(x2, y2);
      ctx.stroke();
      ctx.fillStyle = '#f3cf65'; ctx.font = '10px JetBrains Mono';
      ctx.fillText(label, x1 + 15, y1 - 16);
    }

    function drawCapacitor(ctx, x, y, label) {
      ctx.beginPath();
      ctx.moveTo(x, y - 15); ctx.lineTo(x, y + 15);
      ctx.moveTo(x + 8, y - 15); ctx.lineTo(x + 8, y + 15);
      ctx.stroke();
      ctx.fillStyle = '#00e5ff'; ctx.font = '10px JetBrains Mono';
      ctx.fillText(label, x - 15, y + 30);
    }

    function drawScope() {
      const c = document.getElementById('schem-scope-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#010502';
      ctx.fillRect(0, 0, W, H);

      // Scope reticle
      ctx.strokeStyle = 'rgba(0, 230, 118, 0.1)';
      for (let x = 0; x < W; x += 30) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
      for (let y = 0; y < H; y += 20) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      scopeTime += 0.08;
      ctx.strokeStyle = activeProbe === 'TP1' ? '#f3cf65' : (activeProbe === 'TP2' ? '#ff1744' : '#00e676');
      ctx.lineWidth = 2;
      ctx.beginPath();

      for (let x = 0; x < W; x += 2) {
        const t = (x / W) * 4 * Math.PI + scopeTime;
        let yVal = 0;
        if (activeProbe === 'TP1') yVal = Math.sin(t) * (H * 0.35);
        else if (activeProbe === 'TP2') yVal = -Math.sin(t) * (H * 0.45);
        else yVal = (H * 0.25) + Math.sin(t * 0.1) * 3; // Filtered DC
        const py = H/2 - yVal;
        if (x === 0) ctx.moveTo(x, py); else ctx.lineTo(x, py);
      }
      ctx.stroke();
      requestAnimationFrame(drawScope);
    }

    window.addEventListener('load', () => {
      drawCircuitSchematic();
      requestAnimationFrame(drawScope);
    });
    window.addEventListener('resize', drawCircuitSchematic);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 5. GRAPHVIZ
# ==============================================================================
def build_graphviz(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">GRAPHVIZ HIERARCHICAL SUGIYAMA DAG</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Execution:</label>
        <button class="btn-action" onclick="stepGraphvizDag()" id="btn-gv-step" style="font-size:0.7rem; padding:3px 8px;">Next Step ▶</button>
        <button class="btn-action" onclick="resetGraphvizDag()" style="font-size:0.7rem; padding:3px 8px;">Reset DAG</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="gv-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>dot = graphviz.Digraph('Pipeline', format='svg'); dot.node('A', shape='box'); dot.edge('A', 'B')</span>
      <span>Layered Hierarchical Graph Drawing · Minimal Edge-Crossing Heuristic</span>
    </div>
    """

    custom_js = """
    let gvStep = 0;
    const gvNodes = [
      { id: 'start', layer: 0, label: 'Git Push Commit', status: 'done' },
      { id: 'lint', layer: 1, label: 'Ruff Linter & AST', status: 'pending' },
      { id: 'test', layer: 1, label: 'PyTest Unit Suite', status: 'pending' },
      { id: 'build', layer: 2, label: 'Docker Multi-Stage', status: 'pending' },
      { id: 'sec', layer: 2, label: 'Trivy CVE Security', status: 'pending' },
      { id: 'deploy', layer: 3, label: 'Canary Kubernetes', status: 'pending' }
    ];

    const gvEdges = [
      ['start', 'lint'], ['start', 'test'],
      ['lint', 'build'], ['test', 'build'],
      ['build', 'sec'], ['sec', 'deploy']
    ];

    function stepGraphvizDag() {
      gvStep = (gvStep + 1) % (gvNodes.length + 1);
      for (let i = 0; i < gvNodes.length; i++) {
        gvNodes[i].status = i < gvStep ? 'done' : (i === gvStep ? 'running' : 'pending');
      }
      drawGraphviz();
    }

    function resetGraphvizDag() {
      gvStep = 1;
      for (let i = 0; i < gvNodes.length; i++) {
        gvNodes[i].status = i === 0 ? 'done' : 'pending';
      }
      drawGraphviz();
    }

    function drawGraphviz() {
      const c = document.getElementById('gv-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      // Layer vertical columns
      const layerX = [W * 0.15, W * 0.40, W * 0.65, W * 0.88];
      const layerYs = {
        start: [H / 2],
        lint: [H / 2 - 60],
        test: [H / 2 + 60],
        build: [H / 2 - 60],
        sec: [H / 2 + 60],
        deploy: [H / 2]
      };

      // Assign coordinates
      gvNodes.forEach(n => {
        n.x = layerX[n.layer];
        n.y = layerYs[n.id][0];
      });

      // Draw Edges (Splines)
      gvEdges.forEach(e => {
        const u = gvNodes.find(n => n.id === e[0]);
        const v = gvNodes.find(n => n.id === e[1]);

        ctx.strokeStyle = (u.status === 'done' && (v.status === 'done' || v.status === 'running')) ? '#00e676' : 'rgba(255,255,255,0.15)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(u.x + 55, u.y);
        ctx.bezierCurveTo((u.x + v.x)/2, u.y, (u.x + v.x)/2, v.y, v.x - 55, v.y);
        ctx.stroke();
      });

      // Draw Nodes
      gvNodes.forEach(n => {
        let borderCol = '#475569';
        let bgCol = '#0a120e';
        if (n.status === 'done') { borderCol = '#00e676'; bgCol = '#0a1e12'; }
        else if (n.status === 'running') { borderCol = '#f3cf65'; bgCol = '#241a06'; }

        ctx.fillStyle = bgCol;
        ctx.strokeStyle = borderCol;
        ctx.lineWidth = 2;
        ctx.strokeRect(n.x - 65, n.y - 20, 130, 40);
        ctx.fillRect(n.x - 65, n.y - 20, 130, 40);

        ctx.fillStyle = '#f8fafc';
        ctx.font = '10px JetBrains Mono';
        ctx.textAlign = 'center';
        ctx.fillText(n.label, n.x, n.y + 3);
      });
    }

    window.addEventListener('load', () => { resetGraphvizDag(); });
    window.addEventListener('resize', drawGraphviz);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 6. DNA FEATURES VIEWER
# ==============================================================================
def build_dna(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">DNA FEATURES VIEWER GENOMIC PLASMID MAP</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="btn-action" onclick="setDnaMode('circular')" id="btn-dna-circ" style="font-size:0.7rem; padding:3px 8px;">Circular Plasmid</button>
        <button class="btn-action" onclick="setDnaMode('linear')" id="btn-dna-lin" style="font-size:0.7rem; padding:3px 8px;">Linear CDS Track</button>
      </div>
    </div>
    <div class="canvas-body" id="dna-container" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="dna-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>from dna_features_viewer import CircularGraphicRecord; record.plot(figure_width=7)</span>
      <span>BioPython SeqFeature Mapping · Overlap-Resolving Collision Pipeline</span>
    </div>
    """

    custom_js = """
    let dnaMode = 'circular';

    function setDnaMode(m) {
      dnaMode = m;
      drawDna();
    }

    function drawDna() {
      const c = document.getElementById('dna-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      const features = [
        { name: 'AmpR (Ampicillin)', start: 400, end: 1260, color: '#00e676' },
        { name: 'pUC Origin (ori)', start: 1600, end: 2300, color: '#f3cf65' },
        { name: 'lacZ Alpha Peptide', start: 2700, end: 3400, color: '#00e5ff' },
        { name: 'Cas9 Guide gRNA', start: 3800, end: 4600, color: '#ff1744' },
        { name: 'CMV Promoter', start: 5000, end: 5700, color: '#d500f9' }
      ];
      const TOTAL_BP = 6200;

      if (dnaMode === 'circular') {
        const cx = W / 2; const cy = H / 2; const R = 150;

        // Base plasmid backbone
        ctx.strokeStyle = 'rgba(255,255,255,0.15)';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.arc(cx, cy, R, 0, 2*Math.PI);
        ctx.stroke();

        // Plasmid Title in center
        ctx.fillStyle = '#fff';
        ctx.font = '16px Newsreader';
        ctx.textAlign = 'center';
        ctx.fillText('pUC19-CRISPR-v2', cx, cy - 8);
        ctx.fillStyle = '#94a3b8';
        ctx.font = '11px JetBrains Mono';
        ctx.fillText('6,200 bp', cx, cy + 12);

        // Feature Arcs
        features.forEach(f => {
          const a1 = (f.start / TOTAL_BP) * 2 * Math.PI - Math.PI/2;
          const a2 = (f.end / TOTAL_BP) * 2 * Math.PI - Math.PI/2;

          ctx.strokeStyle = f.color;
          ctx.lineWidth = 14;
          ctx.beginPath();
          ctx.arc(cx, cy, R, a1, a2);
          ctx.stroke();

          // Label
          const midAngle = (a1 + a2) / 2;
          const lx = cx + (R + 35) * Math.cos(midAngle);
          const ly = cy + (R + 35) * Math.sin(midAngle);
          ctx.fillStyle = f.color;
          ctx.font = '10px DM Sans';
          ctx.fillText(f.name, lx, ly);
        });
      } else {
        // Linear track
        const ox = 60; const oy = H / 2; const trackW = W - 120;
        ctx.strokeStyle = '#64748b';
        ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + trackW, oy); ctx.stroke();

        // Ruler ticks
        for (let bp = 0; bp <= TOTAL_BP; bp += 1000) {
          const px = ox + (bp / TOTAL_BP) * trackW;
          ctx.beginPath(); ctx.moveTo(px, oy - 6); ctx.lineTo(px, oy + 6); ctx.stroke();
          ctx.fillStyle = '#64748b';
          ctx.font = '10px JetBrains Mono';
          ctx.textAlign = 'center';
          ctx.fillText(bp + 'bp', px, oy + 22);
        }

        // Feature blocks with arrow tips
        features.forEach((f, idx) => {
          const x1 = ox + (f.start / TOTAL_BP) * trackW;
          const x2 = ox + (f.end / TOTAL_BP) * trackW;
          const blockH = 26;
          const by = oy - 45 - (idx % 2) * 35;

          ctx.fillStyle = f.color;
          ctx.fillRect(x1, by, x2 - x1, blockH);

          ctx.fillStyle = '#050806';
          ctx.font = '10px JetBrains Mono';
          ctx.textAlign = 'left';
          ctx.fillText(f.name, x1 + 6, by + 16);
        });
      }
    }

    window.addEventListener('load', () => { drawDna(); });
    window.addEventListener('resize', drawDna);
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 7. DIAGRABBER
# ==============================================================================
def build_diagrabber(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">DIAGRABBER INDUSTRIAL P&ID PROCESS SCHEMATIC</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Valve V-101:</label>
        <button class="btn-action" onclick="toggleDiaValve()" id="btn-dia-vlv" style="font-size:0.7rem; padding:3px 8px;">Throttle 100%</button>
        <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--cyan-neon);">Flow: <strong id="dia-flow-rate">45.2</strong> m³/h</span>
      </div>
    </div>
    <div class="canvas-body" style="padding:16px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="diagrab-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>import diagrabber; pid = diagrabber.parse_piping('plant_alpha.dxf'); pid.render()</span>
      <span>Process & Instrumentation Diagram Vector Parser · ISA-5.1 Instrumentation Standard</span>
    </div>
    """

    custom_js = """
    let valveOpen = true;
    let diaAnimOffset = 0;

    function toggleDiaValve() {
      valveOpen = !valveOpen;
      document.getElementById('btn-dia-vlv').innerText = valveOpen ? 'Throttle 100%' : 'Closed (0%)';
      document.getElementById('dia-flow-rate').innerText = valveOpen ? '45.2' : '0.0';
    }

    function drawDiagrabber() {
      const c = document.getElementById('diagrab-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      if (valveOpen) diaAnimOffset += 0.05;

      // Tank TK-101 (Storage Vessel)
      const tk1x = 100; const tk1y = H/2 - 80;
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2.5;
      ctx.strokeRect(tk1x, tk1y, 90, 160);
      ctx.fillStyle = 'rgba(0, 230, 118, 0.15)';
      ctx.fillRect(tk1x, tk1y + 40, 90, 120);
      ctx.fillStyle = '#fff';
      ctx.font = '11px JetBrains Mono';
      ctx.fillText('TK-101', tk1x + 22, tk1y + 30);

      // Centrifugal Pump P-101
      const pmpx = 280; const pmpy = tk1y + 120;
      ctx.strokeStyle = '#00e5ff';
      ctx.beginPath(); ctx.arc(pmpx, pmpy, 25, 0, 2*Math.PI); ctx.stroke();
      ctx.fillStyle = 'rgba(0, 229, 255, 0.2)'; ctx.fill();
      ctx.fillStyle = '#fff'; ctx.fillText('P-101', pmpx - 16, pmpy + 4);

      // Distillation Column C-102
      const colX = W - 180; const colY = H/2 - 120;
      ctx.strokeStyle = '#f3cf65';
      ctx.strokeRect(colX, colY, 80, 240);
      ctx.fillStyle = 'rgba(243, 207, 101, 0.1)'; ctx.fillRect(colX, colY, 80, 240);
      ctx.fillStyle = '#fff'; ctx.fillText('C-102', colX + 22, colY + 30);

      // Pipeline from TK-101 to Pump
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(tk1x + 90, tk1y + 120);
      ctx.lineTo(pmpx - 25, pmpy);
      ctx.stroke();

      // Pipeline from Pump to Column with Valve V-101
      ctx.beginPath();
      ctx.moveTo(pmpx + 25, pmpy);
      ctx.lineTo(colX, colY + 160);
      ctx.stroke();

      // Draw Valve V-101
      const vlvX = (pmpx + 25 + colX) / 2;
      const vlvY = (pmpy + colY + 160) / 2;
      ctx.fillStyle = valveOpen ? '#00e676' : '#ff1744';
      ctx.beginPath();
      ctx.moveTo(vlvX - 12, vlvY - 10);
      ctx.lineTo(vlvX + 12, vlvY + 10);
      ctx.lineTo(vlvX + 12, vlvY - 10);
      ctx.lineTo(vlvX - 12, vlvY + 10);
      ctx.closePath();
      ctx.fill();
      ctx.fillStyle = '#fff';
      ctx.font = '10px JetBrains Mono';
      ctx.fillText('V-101', vlvX - 14, vlvY - 14);

      requestAnimationFrame(drawDiagrabber);
    }

    window.addEventListener('load', () => { requestAnimationFrame(drawDiagrabber); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)
