"""
Builder for Deck 03: JavaScript Networks, Graphs & Node Diagrams
Generates 03-javascript-networks-graphs.html (20 distinct visual paradigms)
"""
import os
from template_engine import generate_deck_html

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_deck():
    deck_meta = {
        'id': 'deck-03',
        'series_num': '03',
        'title': 'JavaScript Networks, Graphs & Node Diagrams',
        'category': 'Networks & Node Graphs',
        'subtitle': '20 Graph Topology Paradigms across Cytoscape.js, Sigma.js, Vis.js Network, AntV G6, JointJS, GoJS, and Mermaid.js'
    }

    slides = [
        # 1. Cytoscape.js Force-Directed CoLA Layout
        {
            'slide_id': 'slide-01-cytoscape-force',
            'tag': '01 / Physics Simulation',
            'headline': 'Constraint Physics:',
            'headline_span': 'Cytoscape.js CoLA Force Graph',
            'subtitle': 'Spring-electrical node layout with geometric collision constraints and dynamic edge repulsion.',
            'library_badge': 'Cytoscape.js v3.28',
            'chart_html': """
              <div id="cy-stage" style="width:100%; height:100%; background:#070c09; border-radius:8px;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  if (!window.cytoscape) return;
                  cytoscape({
                    container: document.getElementById('cy-stage'),
                    elements: [
                      { data: { id: 'hotel', label: 'Asset Core' } },
                      { data: { id: 'web', label: 'Direct Web' } },
                      { data: { id: 'app', label: 'Mobile App' } },
                      { data: { id: 'ota', label: 'OTA Intermediary' } },
                      { data: { id: 'meta', label: 'Google Meta' } },
                      { data: { id: 'crm', label: 'Guest CDP' } },
                      { data: { source: 'hotel', target: 'web' } },
                      { data: { source: 'hotel', target: 'app' } },
                      { data: { source: 'hotel', target: 'crm' } },
                      { data: { source: 'ota', target: 'hotel' } },
                      { data: { source: 'meta', target: 'web' } },
                      { data: { source: 'web', target: 'crm' } },
                      { data: { source: 'app', target: 'crm' } }
                    ],
                    style: [
                      { selector: 'node', style: { 'background-color': '#d4af37', 'label': 'data(label)', 'color': '#fffefa', 'font-family': 'DM Sans', 'font-size': '11px', 'text-valign': 'center', 'width': 50, 'height': 50 } },
                      { selector: 'node[id = "hotel"]', style: { 'background-color': '#00e676', 'width': 65, 'height': 65, 'font-weight': 'bold' } },
                      { selector: 'node[id = "ota"]', style: { 'background-color': '#ff1744', 'width': 55, 'height': 55 } },
                      { selector: 'edge', style: { 'width': 2, 'line-color': 'rgba(212, 175, 55, 0.4)', 'target-arrow-color': '#d4af37', 'target-arrow-shape': 'triangle', 'curve-style': 'bezier' } }
                    ],
                    layout: { name: 'circle' }
                  });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Fruchterman-Reingold / CoLA force simulation: repulsive electrostatic forces $F_r = k^2/d$ and attractive spring forces $F_a = d^2/k$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate shareholding networks, enterprise architecture mapping, fraud detection syndicates.'},
                {'title': 'Technical Strengths', 'desc': 'Industrial-grade graph theory library with built-in Dijkstra, A*, Floyd-Warshall, and PageRank.'}
            ],
            'metrics': [
                {'label': 'Physics Engine', 'val': 'CoLA / Force', 'sub': 'Spring Physics'},
                {'label': 'Algorithms', 'val': 'PageRank / MST', 'sub': 'Built-In Graph'},
                {'label': 'DOM', 'val': 'Canvas Multi-Layer', 'sub': 'Smooth Drag'},
                {'label': 'License', 'val': 'MIT Open', 'sub': 'Academic & Corp'}
            ],
            'code_snippet': """cytoscape({
  container: document.getElementById('cy'),
  elements: graphData,
  layout: { name: 'cose', animate: true }
});"""
        },

        # 2. Sigma.js Large-Scale WebGL Graph
        {
            'slide_id': 'slide-02-sigma-webgl',
            'tag': '02 / Massive WebGL Graphs',
            'headline': 'Million-Node Scaling:',
            'headline_span': 'Sigma.js Hardware Graph Engine',
            'subtitle': 'GPU-accelerated vertex rendering supporting hundreds of thousands of nodes at 60 FPS.',
            'library_badge': 'Sigma.js WebGL',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; position:relative;">
                <canvas id="sigma-sim-canvas" width="460" height="340" style="background:#050806; border-radius:8px; border:1px solid rgba(0,230,118,0.3);"></canvas>
                <div style="position:absolute; bottom:14px; right:16px; background:rgba(7,12,9,0.85); padding:4px 10px; border-radius:4px; font-family:JetBrains Mono; font-size:0.75rem; color:#00e676;">
                  WebGL Shaders &bull; 2,500 Nodes Clustered
                </div>
              </div>
              <script>
              (function(){
                const canvas = document.getElementById('sigma-sim-canvas');
                if (!canvas) return;
                const ctx = canvas.getContext('2d');
                const clusters = [
                  { cx: 120, cy: 120, col: '#00e676' },
                  { cx: 340, cy: 110, col: '#d4af37' },
                  { cx: 230, cy: 250, col: '#00e5ff' }
                ];
                const nodes = [];
                clusters.forEach(c => {
                  for(let i=0; i<40; i++) {
                    nodes.push({
                      x: c.cx + (Math.random() - 0.5) * 110,
                      y: c.cy + (Math.random() - 0.5) * 100,
                      r: Math.random() * 3.5 + 1.5,
                      col: c.col
                    });
                  }
                });
                // Draw Edges
                ctx.strokeStyle = 'rgba(255,255,255,0.06)';
                ctx.lineWidth = 1;
                for(let i=0; i<nodes.length; i+=2) {
                  ctx.beginPath();
                  ctx.moveTo(nodes[i].x, nodes[i].y);
                  ctx.lineTo(nodes[(i+1)%nodes.length].x, nodes[(i+1)%nodes.length].y);
                  ctx.stroke();
                }
                // Draw Nodes
                nodes.forEach(n => {
                  ctx.fillStyle = n.col;
                  ctx.beginPath();
                  ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
                  ctx.fill();
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Direct OpenGL / WebGL vertex attribute buffers bypassing standard DOM elements entirely.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Social network community detection, anti-money laundering (AML) forensic transaction graphs.'},
                {'title': 'Technical Strengths', 'desc': 'Effortlessly renders 100,000+ nodes and 500,000 edges without memory exhaustion.'}
            ],
            'metrics': [
                {'label': 'Renderer', 'val': 'WebGL Shader', 'sub': 'GPU Vertex'},
                {'label': 'Node Limit', 'val': '100,000+', 'sub': '60 FPS Target'},
                {'label': 'Graph Data', 'val': 'Graphology', 'sub': 'High Speed'},
                {'label': 'Interaction', 'val': 'Camera Pan/Zoom', 'sub': 'Quaternion'}
            ],
            'code_snippet': """const renderer = new Sigma(graph, container, {
  renderEdgeLabels: false,
  enableEdgeClickEvents: false
});"""
        },

        # 3. Vis.js Dynamic Clustered Hierarchical Network
        {
            'slide_id': 'slide-03-vis-network',
            'tag': '03 / Dynamic Hierarchy',
            'headline': 'Interactive Hierarchies:',
            'headline_span': 'Vis.js Clustered Network Mesh',
            'subtitle': 'Physics-enabled tree network with automated node clustering and collapsible department nodes.',
            'library_badge': 'Vis.js Network',
            'chart_html': """
              <div id="vis-net-stage" style="width:100%; height:100%; background:#09100c; border-radius:8px;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const container = document.getElementById('vis-net-stage');
                  if (!container || !window.vis) return;
                  const nodes = new vis.DataSet([
                    { id: 1, label: 'Holding Co', color: '#f3cf65', font: { color: '#000' } },
                    { id: 2, label: 'OpCo Asia', color: '#00e676' },
                    { id: 3, label: 'OpCo Europe', color: '#00e5ff' },
                    { id: 4, label: 'Singapore Hotel', color: '#16281e', shape: 'box', font: { color: '#fff' } },
                    { id: 5, label: 'Tokyo Resort', color: '#16281e', shape: 'box', font: { color: '#fff' } },
                    { id: 6, label: 'London Heritage', color: '#16281e', shape: 'box', font: { color: '#fff' } }
                  ]);
                  const edges = new vis.DataSet([
                    { from: 1, to: 2 }, { from: 1, to: 3 },
                    { from: 2, to: 4 }, { from: 2, to: 5 },
                    { from: 3, to: 6 }
                  ]);
                  new vis.Network(container, { nodes, edges }, {
                    physics: { barnesHut: { gravitationalConstant: -3000 } },
                    edges: { color: { color: '#d4af37' }, width: 1.5 }
                  });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Barnes-Hut quadtree n-body approximation algorithm: $O(N \\log N)$ simulation efficiency.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate entity governance structures, active directory networks, IT infrastructure topologies.'},
                {'title': 'Technical Strengths', 'desc': 'Dynamic drag-and-drop physics, auto-stabilization, and hierarchical layout toggles.'}
            ],
            'metrics': [
                {'label': 'Physics Alg', 'val': 'Barnes-Hut Quad', 'sub': 'O(N log N)'},
                {'label': 'Clustering', 'val': 'Dynamic Collapse', 'sub': 'Sub-Trees'},
                {'label': 'DOM', 'val': 'HTML5 Canvas', 'sub': 'Retina Crisp'},
                {'label': 'Stabilize', 'val': 'Auto-Sleep', 'sub': 'Saves CPU'}
            ],
            'code_snippet': """const network = new vis.Network(container, data, {
  layout: { hierarchical: { direction: 'UD', sortMethod: 'directed' } }
});"""
        },

        # 4. AntV G6 Concentric Ring Radial Layout
        {
            'slide_id': 'slide-04-antv-g6',
            'tag': '04 / Concentric Centrality',
            'headline': 'Concentric Rings:',
            'headline_span': 'Centrality-Ranked Radial Mesh',
            'subtitle': 'Places sovereign core assets at center ring with peripheral intermediaries arranged by distance.',
            'library_badge': 'AntV G6 Graph Engine',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 320" style="width:280px; height:280px;">
                  <!-- Concentric Rings -->
                  <circle cx="160" cy="160" r="40" fill="none" stroke="#d4af37" stroke-width="1.5" stroke-dasharray="4"/>
                  <circle cx="160" cy="160" r="85" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
                  <circle cx="160" cy="160" r="130" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
                  <!-- Core Center Node -->
                  <circle cx="160" cy="160" r="22" fill="#00e676" stroke="#fffefa" stroke-width="2"/>
                  <text x="160" y="164" text-anchor="middle" fill="#070c09" font-family="DM Sans" font-size="9" font-weight="bold">Core Folio</text>
                  <!-- Ring 1 Nodes (Direct) -->
                  <circle cx="160" cy="75" r="14" fill="#f3cf65"/>
                  <line x1="160" y1="138" x2="160" y2="89" stroke="#d4af37" stroke-width="1.5"/>
                  <circle cx="245" cy="160" r="14" fill="#f3cf65"/>
                  <line x1="182" y1="160" x2="231" y2="160" stroke="#d4af37" stroke-width="1.5"/>
                  <!-- Ring 2 Nodes (Periphery) -->
                  <circle cx="75" cy="160" r="12" fill="#ff1744"/>
                  <circle cx="160" cy="290" r="12" fill="#ff1744"/>
                  <line x1="138" y1="160" x2="87" y2="160" stroke="#ff1744" stroke-width="1" stroke-dasharray="2"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Radial coordinate sorting: $r_i = k \\cdot \\text{Rank}(d_i)$, where rank is derived from Degree Centrality or PageRank.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Critical dependency identification, tier-1 vendor risk analysis, VIP customer relationship graphs.'},
                {'title': 'Technical Strengths', 'desc': 'Instantly separates core strategic assets from secondary peripheral intermediaries.'}
            ],
            'metrics': [
                {'label': 'Layout Mode', 'val': 'Concentric Ring', 'sub': 'Degree-Ranked'},
                {'label': 'Centrality', 'val': 'Eigenvector / Deg', 'sub': 'Mathematical'},
                {'label': 'Rings', 'val': '3 Tiers', 'sub': 'Core to Edge'},
                {'label': 'Alibaba Engine', 'val': 'AntV G6', 'sub': 'High-Scale'}
            ],
            'code_snippet': """const graph = new G6.Graph({
  container: 'mountNode',
  layout: { type: 'concentric', maxNodeSpacing: 50, preventOverlap: true }
});"""
        },

        # 5. Mermaid.js Sequence & Microservices Architecture
        {
            'slide_id': 'slide-05-mermaid-sequence',
            'tag': '05 / Protocol Sequences',
            'headline': 'Transactional Handshakes:',
            'headline_span': 'Mermaid.js Protocol Sequence',
            'subtitle': 'Declarative Markdown-based protocol handshake mapping direct conversational AI booking verification.',
            'library_badge': 'Mermaid.js v10',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:10px;">
                <div class="mermaid" style="width:100%; max-height:360px;">
                  sequenceDiagram
                    autonumber
                    actor Guest as Guest AI Agent
                    participant MCP as Hotel MCP Gateway
                    participant CRS as Central Reservation (CRS)
                    participant PMS as Property Folio (PMS)
                    Guest->>MCP: Query Verified Room Entity (JSON-LD)
                    MCP-->>Guest: Return Sovereign Rate & Live Inventory
                    Guest->>MCP: Submit Booking Token (Encrypted Pay)
                    MCP->>CRS: Validate Rate Parity & Hold Room
                    CRS->>PMS: Create Unmasked 1st-Party Folio
                    PMS-->>Guest: Instant Confirmation & Digital Key Token
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Sequential message passing state-machine tracking synchronous and asynchronous API execution.'},
                {'title': 'Enterprise Use Cases', 'desc': 'API architecture documentation, OAuth2 token handshakes, financial settlement workflows.'},
                {'title': 'Technical Strengths', 'desc': 'Pure Markdown textual syntax, version-controllable in git, auto-rendered in Reveal.js.'}
            ],
            'metrics': [
                {'label': 'Syntax', 'val': 'Pure Markdown', 'sub': 'Text-Driven'},
                {'label': 'Rendering', 'val': 'Vector SVG', 'sub': 'Zero Raster'},
                {'label': 'Versioning', 'val': 'Git Native', 'sub': 'Diff-Friendly'},
                {'label': 'Actors', 'val': 'Distributed', 'sub': 'Microservices'}
            ],
            'code_snippet': """sequenceDiagram
  Guest->>MCP: Query Room Entity
  MCP-->>Guest: Return Sovereign Rate
  Guest->>PMS: Create Unmasked Folio"""
        },

        # 6. JointJS BPMN Workflow Diagram
        {
            'slide_id': 'slide-06-jointjs-bpmn',
            'tag': '06 / Business Process Models',
            'headline': 'BPMN Process Engines:',
            'headline_span': 'Interactive Workflow Automations',
            'subtitle': 'BPMN 2.0 compliant workflow nodes tracking automated rate parity violation countermeasures.',
            'library_badge': 'JointJS Core',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; padding:15px;">
                <svg viewBox="0 0 450 220" style="width:100%; max-height:260px;">
                  <!-- Start Event -->
                  <circle cx="40" cy="110" r="18" fill="#13221b" stroke="#00e676" stroke-width="3"/>
                  <text x="40" y="114" text-anchor="middle" fill="#00e676" font-size="10">&#9658;</text>
                  <!-- Line 1 -->
                  <line x1="58" y1="110" x2="100" y2="110" stroke="#d4af37" stroke-width="2"/>
                  <!-- Task: Scraping -->
                  <rect x="100" y="85" width="100" height="50" fill="#1b2822" stroke="#d4af37" rx="6"/>
                  <text x="150" y="112" text-anchor="middle" fill="#fffefa" font-family="DM Sans" font-size="11">Detect OTA Leak</text>
                  <!-- Gateway -->
                  <path d="M 235 110 L 255 85 L 275 110 L 255 135 Z" fill="#1b2822" stroke="#f3cf65" stroke-width="2"/>
                  <!-- Diverging Flows -->
                  <line x1="275" y1="110" x2="320" y2="70" stroke="#00e676" stroke-width="2"/>
                  <rect x="320" y="50" width="105" height="40" fill="#13221b" stroke="#00e676" rx="4"/>
                  <text x="372" y="74" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="10">Auto Rate Adjust</text>
                  <line x1="275" y1="110" x2="320" y2="150" stroke="#ff1744" stroke-width="2"/>
                  <rect x="320" y="130" width="105" height="40" fill="#13221b" stroke="#ff1744" rx="4"/>
                  <text x="372" y="154" text-anchor="middle" fill="#ff1744" font-family="DM Sans" font-size="10">Issue Stop-Sell</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Petri-net formal execution semantics: transitions, tokens, and conditional branching gateways.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Revenue management escalation protocols, customer complaint resolution paths.'},
                {'title': 'Technical Strengths', 'desc': 'Full drag-and-drop authoring, custom SVG ports, robust connection routing.'}
            ],
            'metrics': [
                {'label': 'Standard', 'val': 'BPMN 2.0', 'sub': 'Process Standard'},
                {'label': 'Gateways', 'val': 'Exclusive (XOR)', 'sub': 'Conditional'},
                {'label': 'Ports', 'val': 'Custom Magnetic', 'sub': 'Snap-to-Connect'},
                {'label': 'Engine', 'val': 'JointJS', 'sub': 'Client Workflow'}
            ],
            'code_snippet': """const link = new joint.shapes.standard.Link();
link.source(taskDetect);
link.target(gatewayDecide);
link.addTo(graph);"""
        },

        # 7. GoJS Enterprise Hierarchy Tree with Ports
        {
            'slide_id': 'slide-07-gojs-hierarchy',
            'tag': '07 / Enterprise Hierarchy',
            'headline': 'Enterprise Node Systems:',
            'headline_span': 'GoJS Port-Connected Hierarchy',
            'subtitle': 'Commercial enterprise diagramming engine featuring custom data-bound node templates and orthogonal link routing.',
            'library_badge': 'GoJS Enterprise',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                <div style="background:#13221b; border:2px solid #d4af37; border-radius:6px; padding:10px 20px; text-align:center;">
                  <strong style="color:#f3cf65; font-size:1.1rem; font-family:Newsreader;">Chief Commercial Officer (CCO)</strong>
                  <div style="font-size:0.75rem; color:#9ba9a1;">P&L Demand Accountability</div>
                </div>
                <div style="width:2px; height:25px; background:#d4af37;"></div>
                <div style="width:280px; height:2px; background:#d4af37;"></div>
                <div style="display:flex; justify-content:space-between; width:340px; margin-top:10px;">
                  <div style="background:#101a16; border:1px solid #00e676; border-radius:4px; padding:8px 12px; text-align:center;">
                    <strong style="color:#00e676; font-size:0.9rem;">Dir. Direct Acquisition</strong>
                  </div>
                  <div style="background:#101a16; border:1px solid #00e5ff; border-radius:4px; padding:8px 12px; text-align:center;">
                    <strong style="color:#00e5ff; font-size:0.9rem;">Dir. Revenue AI</strong>
                  </div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Hierarchical tree layout with subtree bounding-box collision avoidance and orthogonal Bézier routing.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate organigrams, electrical schematic CAD, process control schematics.'},
                {'title': 'Technical Strengths', 'desc': 'Extremely mature, high-performance HTML5 Canvas diagramming framework for commercial apps.'}
            ],
            'metrics': [
                {'label': 'Routing', 'val': 'Orthogonal', 'sub': 'Bézier Avoidance'},
                {'label': 'Data Binding', 'val': 'Two-Way', 'sub': 'Reactive Sync'},
                {'label': 'Scale', 'val': 'Enterprise Grade', 'sub': 'Complex CAD'},
                {'label': 'License', 'val': 'Commercial', 'sub': 'Northwoods'}
            ],
            'code_snippet': """myDiagram.nodeTemplate = $(go.Node, "Auto",
  $(go.Shape, "RoundedRectangle", { fill: "#13221b" }),
  $(go.TextBlock, { margin: 8, stroke: "#fffefa" }, new go.Binding("text", "name"))
);"""
        },

        # 8. VivaGraphJS Fast Force-Directed Graph on Canvas
        {
            'slide_id': 'slide-08-vivagraph',
            'tag': '08 / High-Performance Graph',
            'headline': 'High-Throughput Force Graphs:',
            'headline_span': 'VivaGraphJS Fast Physics',
            'subtitle': 'Lightweight physics engine built for high-throughput node exploration with minimal memory footprint.',
            'library_badge': 'VivaGraphJS',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 260" style="width:100%; max-height:280px;">
                  <!-- Clustered Ring Network -->
                  <g stroke="#d4af37" stroke-width="1.2" opacity="0.6">
                    <line x1="80" y1="130" x2="140" y2="80"/>
                    <line x1="140" y1="80" x2="210" y2="80"/>
                    <line x1="210" y1="80" x2="270" y2="130"/>
                    <line x1="270" y1="130" x2="210" y2="180"/>
                    <line x1="210" y1="180" x2="140" y2="180"/>
                    <line x1="140" y1="180" x2="80" y2="130"/>
                    <line x1="140" y1="80" x2="210" y2="180"/>
                    <line x1="210" y1="80" x2="140" y2="180"/>
                  </g>
                  <circle cx="80" cy="130" r="9" fill="#00e676"/>
                  <circle cx="140" cy="80" r="9" fill="#f3cf65"/>
                  <circle cx="210" cy="80" r="9" fill="#00e5ff"/>
                  <circle cx="270" cy="130" r="9" fill="#00e676"/>
                  <circle cx="210" cy="180" r="9" fill="#f3cf65"/>
                  <circle cx="140" cy="180" r="9" fill="#00e5ff"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Verlet physics integration algorithm with spatial grid partitioning for rapid nearest-neighbor force evaluation.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Real-time social graph updates, cybersecurity node clustering, protein-protein interaction networks.'},
                {'title': 'Technical Strengths', 'desc': 'Extremely modular (pluggable renderers: WebGL, Canvas, SVG) with micro-footprint.'}
            ],
            'metrics': [
                {'label': 'Integrator', 'val': 'Verlet Physics', 'sub': 'Stable Dynamics'},
                {'label': 'Pluggable', 'val': 'WebGL / Canvas', 'sub': 'Multi-Backend'},
                {'label': 'Footprint', 'val': '35 KB Core', 'sub': 'Ultra Light'},
                {'label': 'Layout', 'val': 'Force-Directed', 'sub': 'Streaming'}
            ],
            'code_snippet': """var graph = Viva.Graph.graph();
graph.addLink(1, 2);
var renderer = Viva.Graph.View.renderer(graph, { container: document.body });
renderer.run();"""
        },

        # 9. D3 Bipartite Affiliation Network
        {
            'slide_id': 'slide-09-bipartite-network',
            'tag': '09 / Two-Mode Networks',
            'headline': 'Two-Mode Affiliations:',
            'headline_span': 'Bipartite Channel Matrix',
            'subtitle': 'Dual-partition graph connecting two disjoint classes of entities: Hotel Assets vs Intermediary Channels.',
            'library_badge': 'D3 Bipartite Layout',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:15px;">
                <svg viewBox="0 0 450 260" style="width:100%; max-height:300px;">
                  <!-- Left Partition: Hotel Assets -->
                  <g font-family="DM Sans" font-size="11">
                    <rect x="20" y="40" width="110" height="30" fill="#13221b" stroke="#00e676" rx="4"/>
                    <text x="75" y="60" text-anchor="middle" fill="#00e676">Singapore Flagship</text>
                    
                    <rect x="20" y="110" width="110" height="30" fill="#13221b" stroke="#00e676" rx="4"/>
                    <text x="75" y="130" text-anchor="middle" fill="#00e676">London Heritage</text>

                    <rect x="20" y="180" width="110" height="30" fill="#13221b" stroke="#00e676" rx="4"/>
                    <text x="75" y="200" text-anchor="middle" fill="#00e676">Tokyo Luxury Resort</text>
                  </g>

                  <!-- Right Partition: Intermediary Gateways -->
                  <g font-family="DM Sans" font-size="11">
                    <rect x="320" y="40" width="110" height="30" fill="#13221b" stroke="#d4af37" rx="4"/>
                    <text x="375" y="60" text-anchor="middle" fill="#f3cf65">Direct Web / App</text>

                    <rect x="320" y="110" width="110" height="30" fill="#13221b" stroke="#ffab00" rx="4"/>
                    <text x="375" y="130" text-anchor="middle" fill="#ffab00">Google Hotel Ads</text>

                    <rect x="320" y="180" width="110" height="30" fill="#13221b" stroke="#ff1744" rx="4"/>
                    <text x="375" y="200" text-anchor="middle" fill="#ff1744">OTA Intermediary</text>
                  </g>

                  <!-- Bipartite Links -->
                  <g stroke="rgba(212,175,55,0.4)" stroke-width="2">
                    <line x1="130" y1="55" x2="320" y2="55"/>
                    <line x1="130" y1="55" x2="320" y2="125"/>
                    <line x1="130" y1="125" x2="320" y2="55"/>
                    <line x1="130" y1="125" x2="320" y2="195"/>
                    <line x1="130" y1="195" x2="320" y2="55"/>
                    <line x1="130" y1="195" x2="320" y2="125"/>
                  </g>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Bipartite graph $G = (U, V, E)$ where edges only exist between distinct partitions $u \\in U$ and $v \\in V$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotels-to-channels distribution, board directors-to-committees, customer-to-product affinities.'},
                {'title': 'Technical Strengths', 'desc': 'Direct projection onto 1-mode network reveals hidden asset correlation.'}
            ],
            'metrics': [
                {'label': 'Graph Class', 'val': '2-Mode Bipartite', 'sub': 'Disjoint Sets'},
                {'label': 'Projection', 'val': 'Affiliation Matrix', 'sub': 'A x A^T'},
                {'label': 'Edges', 'val': 'Inter-Set Only', 'sub': 'No Intra Edges'},
                {'label': 'Application', 'val': 'Channel Mapping', 'sub': 'Distribution'}
            ],
            'code_snippet': """const topNodes = data.filter(d => d.type === 'hotel');
const bottomNodes = data.filter(d => d.type === 'channel');
drawBipartiteLinks(topNodes, bottomNodes);"""
        },

        # 10. Circular Edge-Bundled Connectogram
        {
            'slide_id': 'slide-10-chord-connectogram',
            'tag': '10 / Hierarchical Bundling',
            'headline': 'B-Spline Edge Bundling:',
            'headline_span': 'Circular Connectogram',
            'subtitle': 'Hierarchical edge bundling reducing visual line clutter by routing related edges along common tree stems.',
            'library_badge': 'D3 Hierarchical Edge Bundle',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 320" style="width:280px; height:280px;">
                  <!-- Outer Circular Node Ring -->
                  <circle cx="160" cy="160" r="120" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
                  <!-- Bundled B-Splines -->
                  <path d="M 60 160 Q 160 160, 160 60" fill="none" stroke="#00e676" stroke-width="2" opacity="0.7"/>
                  <path d="M 60 160 Q 160 160, 240 100" fill="none" stroke="#d4af37" stroke-width="2" opacity="0.7"/>
                  <path d="M 160 260 Q 160 160, 240 100" fill="none" stroke="#00e5ff" stroke-width="2" opacity="0.7"/>
                  <path d="M 160 260 Q 160 160, 160 60" fill="none" stroke="#f3cf65" stroke-width="2" opacity="0.7"/>
                  <path d="M 260 160 Q 160 160, 60 160" fill="none" stroke="#ff1744" stroke-width="1.5" opacity="0.5"/>
                  <!-- Ring Nodes -->
                  <circle cx="60" cy="160" r="8" fill="#00e676"/>
                  <circle cx="160" cy="60" r="8" fill="#f3cf65"/>
                  <circle cx="260" cy="160" r="8" fill="#00e5ff"/>
                  <circle cx="160" cy="260" r="8" fill="#d4af37"/>
                  <circle cx="240" cy="100" r="8" fill="#ffab00"/>
                  <text x="160" y="165" text-anchor="middle" fill="#fffefa" font-family="Newsreader" font-size="16">Edge Bundling</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Cubic B-spline curves pulled toward common ancestors in a radial tree hierarchy with bundling parameter $\\beta \\in [0, 1]$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Cross-departmental communication traffic, software package call dependencies, genomic co-expression.'},
                {'title': 'Technical Strengths', 'desc': 'Dramatically reduces visual hairball clutter by grouping parallel cross-graph connections.'}
            ],
            'metrics': [
                {'label': 'Spline Type', 'val': 'Cubic B-Spline', 'sub': 'Bézier Tension'},
                {'label': 'Tension Beta', 'val': 'β = 0.85', 'sub': 'Bundling Tightness'},
                {'label': 'Clutter', 'val': '-75% Noise', 'sub': 'Clean Voids'},
                {'label': 'Topology', 'val': 'Radial Circular', 'sub': 'Connectogram'}
            ],
            'code_snippet': """const line = d3.lineRadial()
  .curve(d3.curveBundle.beta(0.85))
  .radius(d => d.y).angle(d => d.x);"""
        },

        # 11. Directed Acyclic Graph (DAG) for AI Pipelines
        {
            'slide_id': 'slide-11-dag-pipeline',
            'tag': '11 / Pipeline Orchestration',
            'headline': 'Execution DAGs:',
            'headline_span': 'Directed Acyclic AI Pipeline',
            'subtitle': 'Topological dependency graph orchestrating revenue forecasting and MCP agentic execution.',
            'library_badge': 'DAGre / D3 DAG',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; gap:16px;">
                <div style="background:#13221b; border:1px solid #d4af37; border-radius:6px; padding:8px 18px;">
                  <strong style="color:#f3cf65; font-family:JetBrains Mono;">1. Ingest PMS/OTA Data</strong>
                </div>
                <div style="font-size:1.2rem; color:#d4af37;">&darr;</div>
                <div style="display:flex; gap:24px;">
                  <div style="background:#13221b; border:1px solid #00e676; border-radius:6px; padding:8px 14px;">
                    <strong style="color:#00e676; font-family:JetBrains Mono; font-size:0.85rem;">2A. Dynamic ADR Model</strong>
                  </div>
                  <div style="background:#13221b; border:1px solid #00e5ff; border-radius:6px; padding:8px 14px;">
                    <strong style="color:#00e5ff; font-family:JetBrains Mono; font-size:0.85rem;">2B. Entity Schema Validator</strong>
                  </div>
                </div>
                <div style="font-size:1.2rem; color:#d4af37;">&darr;</div>
                <div style="background:#13221b; border:1px solid #00e676; border-radius:6px; padding:8px 18px; box-shadow:0 0 10px rgba(0,230,118,0.3);">
                  <strong style="color:#00e676; font-family:JetBrains Mono;">3. Deploy to MCP Endpoints</strong>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Kahn’s algorithm topological sort computing non-cyclic execution order with $O(V + E)$ complexity.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Airflow / Prefect data orchestration, machine learning training pipelines, CI/CD builds.'},
                {'title': 'Technical Strengths', 'desc': 'Guarantees execution determinism; prevents deadlocks and cyclical infinite loops.'}
            ],
            'metrics': [
                {'label': 'Graph Class', 'val': 'DAG (No Cycles)', 'sub': 'Deterministic'},
                {'label': 'Algorithm', 'val': "Kahn's Topo Sort", 'sub': 'O(V + E)'},
                {'label': 'Parallelism', 'val': 'Multi-Branch', 'sub': 'Concurrent'},
                {'label': 'Standard', 'val': 'Airflow / Dagster', 'sub': 'Production'}
            ],
            'code_snippet': """dagre.layout(g);
g.nodes().forEach(v => {
  renderNode(v, g.node(v));
});"""
        },

        # 12. Knowledge Graph Semantic Mesh (RDF)
        {
            'slide_id': 'slide-12-knowledge-graph',
            'tag': '12 / Semantic Networks',
            'headline': 'Semantic Entity Meshes:',
            'headline_span': 'RDF Knowledge Graph Triples',
            'subtitle': 'Subject-Predicate-Object semantic mesh powering AI conversational agent discovery.',
            'library_badge': 'Semantic Graph Engine',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 450 220" style="width:100%; max-height:260px;">
                  <!-- Node 1: Hotel Entity -->
                  <circle cx="90" cy="110" r="38" fill="#13221b" stroke="#00e676" stroke-width="2"/>
                  <text x="90" y="108" text-anchor="middle" fill="#fffefa" font-family="DM Sans" font-size="11" font-weight="bold">Hotel Entity</text>
                  <text x="90" y="122" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="9">schema:Hotel</text>
                  <!-- Node 2: Amenity -->
                  <circle cx="360" cy="60" r="32" fill="#13221b" stroke="#d4af37" stroke-width="2"/>
                  <text x="360" y="58" text-anchor="middle" fill="#fffefa" font-family="DM Sans" font-size="11" font-weight="bold">Infinity Pool</text>
                  <text x="360" y="72" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">AmenityFeature</text>
                  <!-- Node 3: Sovereign Rate -->
                  <circle cx="360" cy="160" r="32" fill="#13221b" stroke="#00e5ff" stroke-width="2"/>
                  <text x="360" y="158" text-anchor="middle" fill="#fffefa" font-family="DM Sans" font-size="11" font-weight="bold">Direct Price</text>
                  <text x="360" y="172" text-anchor="middle" fill="#00e5ff" font-family="JetBrains Mono" font-size="9">UnitPriceSpec</text>
                  <!-- Predicate Arrows -->
                  <line x1="128" y1="102" x2="328" y2="66" stroke="#d4af37" stroke-width="2"/>
                  <rect x="195" y="72" width="75" height="18" fill="#070c09" rx="3"/>
                  <text x="232" y="85" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">amenityFeature</text>
                  <line x1="128" y1="118" x2="328" y2="154" stroke="#00e5ff" stroke-width="2"/>
                  <rect x="195" y="128" width="75" height="18" fill="#070c09" rx="3"/>
                  <text x="232" y="141" text-anchor="middle" fill="#00e5ff" font-family="JetBrains Mono" font-size="9">priceSpecification</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Directed labeled multigraph representation of RDF triples: $\\langle \\text{Subject}, \\text{Predicate}, \\text{Object} \\rangle$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Search engine GEO optimization, LLM RAG entity extraction, enterprise ontologies.'},
                {'title': 'Technical Strengths', 'desc': 'Machine-readable by Perplexity, ChatGPT, and Google Gemini crawlers for zero-shot citation.'}
            ],
            'metrics': [
                {'label': 'Data Model', 'val': 'RDF Triples', 'sub': 'W3C Standard'},
                {'label': 'Schema', 'val': 'Schema.org', 'sub': 'JSON-LD Compatible'},
                {'label': 'LLM Utility', 'val': 'High Citation', 'sub': 'AEO / GEO'},
                {'label': 'Query Lang', 'val': 'SPARQL / Cypher', 'sub': 'Graph Query'}
            ],
            'code_snippet': """{
  "@context": "https://schema.org",
  "@type": "Hotel",
  "name": "Luxury Sovereign",
  "amenityFeature": { "@type": "LocationFeatureSpecification", "value": "Pool" }
}"""
        },

        # 13. Deep Neural Network (DNN) Multi-Layer Architecture
        {
            'slide_id': 'slide-13-neural-network',
            'tag': '13 / Deep Learning Topology',
            'headline': 'Tensor Operations:',
            'headline_span': 'Multi-Layer Neural Network Graph',
            'subtitle': 'Input, hidden dense layers, activation matrices, and output probability nodes in revenue prediction.',
            'library_badge': 'Deep Learning Graph',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 450 240" style="width:100%; max-height:280px;">
                  <!-- Input Layer (4 nodes) -->
                  <g fill="#00e676">
                    <circle cx="60" cy="40" r="10"/>
                    <circle cx="60" cy="90" r="10"/>
                    <circle cx="60" cy="140" r="10"/>
                    <circle cx="60" cy="190" r="10"/>
                  </g>
                  <!-- Hidden Layer 1 (5 nodes) -->
                  <g fill="#d4af37">
                    <circle cx="190" cy="30" r="10"/>
                    <circle cx="190" cy="75" r="10"/>
                    <circle cx="190" cy="120" r="10"/>
                    <circle cx="190" cy="165" r="10"/>
                    <circle cx="190" cy="210" r="10"/>
                  </g>
                  <!-- Output Layer (2 nodes) -->
                  <g fill="#00e5ff">
                    <circle cx="360" cy="85" r="12"/>
                    <circle cx="360" cy="155" r="12"/>
                  </g>
                  <!-- Interconnections (sparse subset) -->
                  <g stroke="rgba(255,255,255,0.12)" stroke-width="1">
                    <line x1="60" y1="40" x2="190" y2="30"/>
                    <line x1="60" y1="40" x2="190" y2="75"/>
                    <line x1="60" y1="90" x2="190" y2="75"/>
                    <line x1="60" y1="90" x2="190" y2="120"/>
                    <line x1="60" y1="140" x2="190" y2="120"/>
                    <line x1="60" y1="140" x2="190" y2="165"/>
                    <line x1="60" y1="190" x2="190" y2="165"/>
                    <line x1="60" y1="190" x2="190" y2="210"/>
                    <line x1="190" y1="75" x2="360" y2="85"/>
                    <line x1="190" y1="120" x2="360" y2="85"/>
                    <line x1="190" y1="120" x2="360" y2="155"/>
                    <line x1="190" y1="165" x2="360" y2="155"/>
                  </g>
                  <!-- Labels -->
                  <text x="60" y="225" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="10">Inputs (X)</text>
                  <text x="190" y="235" text-anchor="middle" fill="#d4af37" font-family="DM Sans" font-size="10">Dense ReLU</text>
                  <text x="360" y="225" text-anchor="middle" fill="#00e5ff" font-family="DM Sans" font-size="10">Predictions</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Affine linear matrix transform: $\\mathbf{a}^{(l+1)} = \\sigma(\\mathbf{W}^{(l)} \\mathbf{a}^{(l)} + \\mathbf{b}^{(l)})$ with backpropagation.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Dynamic pricing prediction, guest cancellation propensity modeling, customer sentiment.'},
                {'title': 'Technical Strengths', 'desc': 'Visualizes weight magnitude through edge thickness and activation via node glow.'}
            ],
            'metrics': [
                {'label': 'Architecture', 'val': 'Feedforward MLP', 'sub': 'Fully Connected'},
                {'label': 'Activations', 'val': 'ReLU / Softmax', 'sub': 'Non-Linear'},
                {'label': 'Tensors', 'val': 'Matrix Product', 'sub': 'GPU Optimized'},
                {'label': 'Loss', 'val': 'Cross-Entropy', 'sub': 'Optimization'}
            ],
            'code_snippet': """model = nn.Sequential(
  nn.Linear(4, 5), nn.ReLU(),
  nn.Linear(5, 2), nn.Softmax(dim=-1)
)"""
        },

        # 14. Minimum Spanning Tree (MST) Kruskal Highlight
        {
            'slide_id': 'slide-14-mst-kruskal',
            'tag': '14 / Combinatorial Optimization',
            'headline': 'Optimal Connectivity:',
            'headline_span': 'Kruskal Minimum Spanning Tree',
            'subtitle': 'Sub-graph connecting all regional hotel nodes with minimum total network distribution cost.',
            'library_badge': 'MST Algorithm',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Discarded high-cost edges -->
                  <line x1="80" y1="60" x2="260" y2="60" stroke="#ff1744" stroke-width="1.5" stroke-dasharray="3"/>
                  <line x1="80" y1="60" x2="260" y2="180" stroke="#ff1744" stroke-width="1.5" stroke-dasharray="3"/>
                  <!-- Minimum Spanning Tree Edges (Green) -->
                  <line x1="80" y1="60" x2="140" y2="130" stroke="#00e676" stroke-width="3"/>
                  <line x1="140" y1="130" x2="80" y2="180" stroke="#00e676" stroke-width="3"/>
                  <line x1="140" y1="130" x2="220" y2="120" stroke="#00e676" stroke-width="3"/>
                  <line x1="220" y1="120" x2="260" y2="60" stroke="#00e676" stroke-width="3"/>
                  <line x1="220" y1="120" x2="260" y2="180" stroke="#00e676" stroke-width="3"/>
                  <!-- Nodes -->
                  <circle cx="80" cy="60" r="10" fill="#f3cf65"/>
                  <circle cx="140" cy="130" r="12" fill="#00e676"/>
                  <circle cx="80" cy="180" r="10" fill="#f3cf65"/>
                  <circle cx="220" cy="120" r="12" fill="#00e676"/>
                  <circle cx="260" cy="60" r="10" fill="#f3cf65"/>
                  <circle cx="260" cy="180" r="10" fill="#f3cf65"/>
                  <text x="175" y="225" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="11">MST Cost: $48k vs $142k Mesh</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Kruskal’s greedy algorithm utilizing disjoint-set data structure (Union-Find) in $O(E \\log E)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Fiber-optic data cable routing, centralized warehouse delivery routes, regional IT hub placement.'},
                {'title': 'Technical Strengths', 'desc': 'Mathematically provable minimum total edge cost guaranteeing full connectivity without cycles.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': "Kruskal's Greedy", 'sub': 'Union-Find'},
                {'label': 'Complexity', 'val': 'O(E log E)', 'sub': 'Fast Sorting'},
                {'label': 'Tree Property', 'val': 'V - 1 Edges', 'sub': 'No Cycles'},
                {'label': 'Cost Saving', 'val': '-66% Overhead', 'sub': 'Pruned Links'}
            ],
            'code_snippet': """edges.sort((a, b) => a.weight - b.weight);
for (const e of edges) {
  if (unionFind.find(e.u) !== unionFind.find(e.v)) {
    mst.push(e); unionFind.union(e.u, e.v);
  }
}"""
        },

        # 15. Sankey Node Energy Flow Network
        {
            'slide_id': 'slide-15-sankey-network',
            'tag': '15 / Nodal Ribbon Routing',
            'headline': 'Nodal Ribbon Routing:',
            'headline_span': 'Sankey Multi-Stage Graph',
            'subtitle': 'High-density multi-stage network mapping guest journey touches from initial search to repeat booking.',
            'library_badge': 'D3 Sankey Plugin',
            'chart_html': """
              <div id="d3-sankey-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('d3-sankey-stage');
                  if (!el || !window.Plotly) return;
                  const data = [{
                    type: 'sankey', orientation: 'h',
                    node: {
                      pad: 16, thickness: 20, line: { color: '#b5935b', width: 1 },
                      label: ["Discovery (100k)", "OTA (45k)", "Brand Search (35k)", "Direct Social (20k)", "Book Direct (28k)", "Book OTA (32k)", "Loyalty Rebook (18k)"],
                      color: ["#f3cf65", "#ff1744", "#00e676", "#00e5ff", "#00e676", "#ff1744", "#f3cf65"]
                    },
                    link: {
                      source: [0, 0, 0, 1, 2, 2, 3, 4],
                      target: [1, 2, 3, 5, 4, 5, 4, 6],
                      value:  [45, 35, 20, 32, 22, 13, 16, 18],
                      color: 'rgba(212, 175, 55, 0.25)'
                    }
                  }];
                  const layout = {
                    paper_bgcolor: 'transparent',
                    font: { color: '#fffefa', family: 'DM Sans', size: 12 },
                    margin: { l: 15, r: 15, t: 20, b: 20 }
                  };
                  Plotly.newPlot('d3-sankey-stage', data, layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Relaxation algorithm iteratively positioning nodes vertically to minimize ribbon edge crossings.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Customer conversion attribution, website user navigation clickstreams, supply chain logistics.'},
                {'title': 'Technical Strengths', 'desc': 'Proportional ribbon width conveys relative traffic volume at a single glance.'}
            ],
            'metrics': [
                {'label': 'Routing', 'val': 'Crossing Min', 'sub': 'Iterative Relax'},
                {'label': 'Conservation', 'val': 'Proportional', 'sub': 'Width = Flow'},
                {'label': 'Interactive', 'val': 'Node Vertical Drag', 'sub': 'Custom Ordering'},
                {'label': 'Clarity', 'val': 'Multi-Stage', 'sub': 'Funnel Path'}
            ],
            'code_snippet': """const sankey = d3.sankey()
  .nodeWidth(20).nodePadding(15)
  .extent([[1, 5], [width - 1, height - 5]]);
const {nodes, links} = sankey(graphData);"""
        },

        # 16. Shortest Path Dijkstra Real-time Graph Route Tracer
        {
            'slide_id': 'slide-16-dijkstra-tracer',
            'tag': '16 / Routing Algorithms',
            'headline': 'Pathfinding Tracers:',
            'headline_span': 'Dijkstra Shortest Route Search',
            'subtitle': 'Priority-queue driven single-source shortest path identifying optimal data transit routes.',
            'library_badge': 'Pathfinding Graph',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 240" style="width:100%; max-height:260px;">
                  <!-- Background Gray Links -->
                  <g stroke="rgba(255,255,255,0.1)" stroke-width="1.5">
                    <line x1="60" y1="120" x2="150" y2="50"/>
                    <line x1="60" y1="120" x2="150" y2="190"/>
                    <line x1="150" y1="50" x2="250" y2="50"/>
                    <line x1="150" y1="190" x2="250" y2="190"/>
                    <line x1="250" y1="50" x2="340" y2="120"/>
                  </g>
                  <!-- Shortest Path Highlight (Gold Glowing) -->
                  <g stroke="#00e676" stroke-width="3.5">
                    <line x1="60" y1="120" x2="150" y2="190"/>
                    <line x1="150" y1="190" x2="250" y2="120"/>
                    <line x1="250" y1="120" x2="340" y2="120"/>
                  </g>
                  <!-- Nodes -->
                  <circle cx="60" cy="120" r="14" fill="#00e676"/>
                  <text x="60" y="124" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="10" font-weight="bold">SRC</text>
                  <circle cx="150" cy="50" r="10" fill="#13221b" stroke="#fff"/>
                  <circle cx="150" cy="190" r="12" fill="#00e676"/>
                  <circle cx="250" cy="50" r="10" fill="#13221b" stroke="#fff"/>
                  <circle cx="250" cy="120" r="12" fill="#00e676"/>
                  <circle cx="250" cy="190" r="10" fill="#13221b" stroke="#fff"/>
                  <circle cx="340" cy="120" r="14" fill="#f3cf65"/>
                  <text x="340" y="124" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="10" font-weight="bold">DST</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Dijkstra relaxation: if $d[u] + w(u,v) < d[v]$ then $d[v] = d[u] + w(u,v)$ via min-heap priority queue.'},
                {'title': 'Enterprise Use Cases', 'desc': 'GPS navigation route planning, fiber optic packet routing, low-latency CDN origin pulls.'},
                {'title': 'Technical Strengths', 'desc': 'Guarantees the absolute shortest path on non-negative weighted networks in $O((V + E) \\log V)$.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': "Dijkstra's Min-Heap", 'sub': 'O((V+E) log V)'},
                {'label': 'Weights', 'val': 'Non-Negative', 'sub': 'Edge Cost'},
                {'label': 'Output', 'val': 'Optimal Vector', 'sub': 'Gold Route'},
                {'label': 'Latency', 'val': 'Sub-Millisecond', 'sub': 'Real-Time'}
            ],
            'code_snippet': """while (!pq.isEmpty()) {
  const { u, d } = pq.pop();
  for (const { v, weight } of adj[u]) {
    if (dist[u] + weight < dist[v]) { dist[v] = dist[u] + weight; pq.push({ v, dist[v] }); }
  }
}"""
        },

        # 17. Ego Network with 1-Hop and 2-Hop Degree Filters
        {
            'slide_id': 'slide-17-ego-network',
            'tag': '17 / Local Neighborhoods',
            'headline': 'Neighborhood Subgraphs:',
            'headline_span': 'Ego Network 1-Hop Extraction',
            'subtitle': 'Focused subgraph isolating a central ego entity and its immediate alter connections.',
            'library_badge': 'Ego Graph Filter',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 250" style="width:100%; max-height:270px;">
                  <!-- 2-Hop Outer Ring Boundary (Dashed) -->
                  <circle cx="175" cy="125" r="105" fill="none" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3"/>
                  <!-- 1-Hop Inner Ring Boundary -->
                  <circle cx="175" cy="125" r="60" fill="none" stroke="#d4af37" stroke-dasharray="4" stroke-width="1.2"/>
                  <!-- Ego Center Node -->
                  <circle cx="175" cy="125" r="18" fill="#f3cf65" stroke="#fff" stroke-width="2"/>
                  <text x="175" y="129" text-anchor="middle" fill="#070c09" font-family="DM Sans" font-size="10" font-weight="bold">Ego</text>
                  <!-- 1-Hop Alters -->
                  <circle cx="125" cy="90" r="10" fill="#00e676"/>
                  <circle cx="225" cy="90" r="10" fill="#00e676"/>
                  <circle cx="175" cy="185" r="10" fill="#00e676"/>
                  <!-- Edges to Alters -->
                  <line x1="175" y1="125" x2="125" y2="90" stroke="#00e676" stroke-width="2"/>
                  <line x1="175" y1="125" x2="225" y2="90" stroke="#00e676" stroke-width="2"/>
                  <line x1="175" y1="125" x2="175" y2="185" stroke="#00e676" stroke-width="2"/>
                  <!-- 2-Hop Peripheral Alters -->
                  <circle cx="90" cy="60" r="7" fill="#6c7d73"/>
                  <line x1="125" y1="90" x2="90" y2="60" stroke="#6c7d73" stroke-dasharray="2"/>
                  <circle cx="260" cy="70" r="7" fill="#6c7d73"/>
                  <line x1="225" y1="90" x2="260" y2="70" stroke="#6c7d73" stroke-dasharray="2"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Breadth-First Search (BFS) radius cutoff: $V_{\\text{ego}}(u, k) = \\{v \\in V \\mid \\text{dist}(u, v) \\le k\\}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Fraud investigation around a suspicious account, VIP guest influence networks, CRM account mapping.'},
                {'title': 'Technical Strengths', 'desc': 'Eliminates massive graph cognitive overload by zooming strictly into immediate spheres of influence.'}
            ],
            'metrics': [
                {'label': 'Filter Radius', 'val': 'k = 1, 2 Hops', 'sub': 'BFS Cutoff'},
                {'label': 'Focus', 'val': 'Single Ego Node', 'sub': 'Target Entity'},
                {'label': 'Complexity', 'val': 'O(deg(u))', 'sub': 'Instant Filter'},
                {'label': 'Noise Drop', 'val': '-90% Clutter', 'sub': 'Surgical View'}
            ],
            'code_snippet': """const egoGraph = (graph, egoId, radius = 1) => {
  const neighbors = new Set([egoId]);
  // BFS expand up to radius
  return extractSubgraph(graph, neighbors);
};"""
        },

        # 18. Cyber Threat Attack Graph
        {
            'slide_id': 'slide-18-threat-attack',
            'tag': '18 / Cybersecurity Graphs',
            'headline': 'Vulnerability Propagation:',
            'headline_span': 'Cyber Attack Vector Trees',
            'subtitle': 'Exploit chain propagation trees modeling attack surface vulnerabilities and perimeter breach vectors.',
            'library_badge': 'Threat Attack Graph',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 450 220" style="width:100%; max-height:250px;">
                  <!-- External Hacker -->
                  <circle cx="50" cy="110" r="20" fill="#13221b" stroke="#ff1744" stroke-width="2"/>
                  <text x="50" y="114" text-anchor="middle" fill="#ff1744" font-family="JetBrains Mono" font-size="10">Adversary</text>
                  <line x1="70" y1="110" x2="130" y2="110" stroke="#ff1744" stroke-width="2" stroke-dasharray="3"/>
                  <!-- Perimeter DMZ -->
                  <rect x="130" y="85" width="90" height="50" fill="#1b2822" stroke="#ffab00" rx="4"/>
                  <text x="175" y="107" text-anchor="middle" fill="#ffab00" font-family="DM Sans" font-size="10" font-weight="bold">Public Web API</text>
                  <text x="175" y="122" text-anchor="middle" fill="#9ba9a1" font-family="JetBrains Mono" font-size="8">CVE-2026-X</text>
                  <line x1="220" y1="110" x2="280" y2="110" stroke="#ff1744" stroke-width="2"/>
                  <!-- Lateral Movement -->
                  <rect x="280" y="85" width="90" height="50" fill="#1b2822" stroke="#ff1744" rx="4"/>
                  <text x="325" y="107" text-anchor="middle" fill="#ff1744" font-family="DM Sans" font-size="10" font-weight="bold">PMS Database</text>
                  <text x="325" y="122" text-anchor="middle" fill="#ff1744" font-family="JetBrains Mono" font-size="8">Cardholder Data</text>
                  <!-- Mitigated Block -->
                  <line x1="175" y1="135" x2="175" y2="180" stroke="#00e676" stroke-width="2"/>
                  <rect x="130" y="180" width="90" height="30" fill="#13221b" stroke="#00e676" rx="4"/>
                  <text x="175" y="200" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="9">WAF Rate-Limiter</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Bayesian attack graph probability calculation: $P(\\text{Breach}) = 1 - \\prod (1 - p_i)$ across lateral exploit stages.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Payment card industry (PCI-DSS) perimeter audits, cloud zero-trust infrastructure verification.'},
                {'title': 'Technical Strengths', 'desc': 'Pinpoints single-point-of-failure vulnerabilities before malicious exploitation.'}
            ],
            'metrics': [
                {'label': 'Graph Model', 'val': 'Attack Tree DAG', 'sub': 'Exploit Vector'},
                {'label': 'Security', 'val': 'PCI-DSS / ISO', 'sub': 'Audit Standard'},
                {'label': 'Severity', 'val': 'CVSS Ranked', 'sub': 'Critical Red'},
                {'label': 'Defense', 'val': 'WAF Layered', 'sub': 'Zero Trust'}
            ],
            'code_snippet': """const attackGraph = new AttackGraph({
  target: 'GuestCreditCardFolio',
  rules: [cveExploits, lateralMovementRules]
});"""
        },

        # 19. Hive Plot with Tri-Axis Node Sorting
        {
            'slide_id': 'slide-19-hive-plot',
            'tag': '19 / Deterministic Networks',
            'headline': 'Reproducible Network Geometry:',
            'headline_span': 'Tri-Axis Hive Plot',
            'subtitle': 'Martin Krzywinski hive plot placing nodes along three radial axes by structural categorical properties.',
            'library_badge': 'D3 Hive Plot',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 320" style="width:280px; height:280px;">
                  <!-- Three Radial Axes (120 degrees apart) -->
                  <!-- Axis 1: Vertical (270 deg) -->
                  <line x1="160" y1="160" x2="160" y2="40" stroke="#d4af37" stroke-width="2"/>
                  <!-- Axis 2: Bottom-Right (30 deg) -->
                  <line x1="160" y1="160" x2="264" y2="220" stroke="#d4af37" stroke-width="2"/>
                  <!-- Axis 3: Bottom-Left (150 deg) -->
                  <line x1="160" y1="160" x2="56" y2="220" stroke="#d4af37" stroke-width="2"/>
                  <!-- Curved Bézier Edges connecting nodes on axes -->
                  <path d="M 160 80 Q 200 120, 220 195" fill="none" stroke="#00e676" stroke-width="2" opacity="0.8"/>
                  <path d="M 160 120 Q 180 140, 180 170" fill="none" stroke="#00e676" stroke-width="2" opacity="0.8"/>
                  <path d="M 220 195 Q 160 210, 100 195" fill="none" stroke="#00e5ff" stroke-width="2" opacity="0.8"/>
                  <path d="M 100 195 Q 120 140, 160 80" fill="none" stroke="#f3cf65" stroke-width="2" opacity="0.8"/>
                  <!-- Nodes on Axes -->
                  <circle cx="160" cy="80" r="6" fill="#00e676"/>
                  <circle cx="160" cy="120" r="6" fill="#00e676"/>
                  <circle cx="220" cy="195" r="6" fill="#00e5ff"/>
                  <circle cx="180" cy="170" r="6" fill="#00e5ff"/>
                  <circle cx="100" cy="195" r="6" fill="#f3cf65"/>
                  <!-- Labels -->
                  <text x="160" y="30" text-anchor="middle" fill="#d4af37" font-family="JetBrains Mono" font-size="10">Direct Channels</text>
                  <text x="275" y="235" fill="#d4af37" font-family="JetBrains Mono" font-size="10">Corporate</text>
                  <text x="45" y="235" text-anchor="end" fill="#d4af37" font-family="JetBrains Mono" font-size="10">OTAs</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Deterministic coordinate assignment: nodes sorted along radial axes $\\theta_k$ by internal property $P_1$, position $r = f(P_2)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Comparing two networks without layout randomness, biological gene networks, telecom topologies.'},
                {'title': 'Technical Strengths', 'desc': '100% reproducible; eliminates the arbitrary visual randomness of force-directed layouts.'}
            ],
            'metrics': [
                {'label': 'Reproducibility', 'val': '100% Deterministic', 'sub': 'No Random Seed'},
                {'label': 'Axes', 'val': '3 Coordinate Rays', 'sub': '120° Spacing'},
                {'label': 'Curvature', 'val': 'Bézier Spline', 'sub': 'Inter-Axis Links'},
                {'label': 'Originator', 'val': 'M. Krzywinski', 'sub': 'Genome Science'}
            ],
            'code_snippet': """d3.hive.link()
  .angle(d => nodeAngle(d))
  .radius(d => nodeRadius(d));"""
        },

        # 20. 3D WebGL Spherical Force Network
        {
            'slide_id': 'slide-20-spherical-3d-graph',
            'tag': '20 / 3D Spatial Topology',
            'headline': 'Spherical Graph Shells:',
            'headline_span': '3D WebGL Network Orbit',
            'subtitle': 'Fully orbital 3D spherical constellation placing global hotel properties along coordinate shells.',
            'library_badge': '3D Force Graph WebGL',
            'chart_html': """
              <div id="plotly-3d-net-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('plotly-3d-net-stage');
                  if (!el || !window.Plotly) return;
                  const n = 35;
                  const x = [], y = [], z = [], color = [];
                  for(let i=0; i<n; i++) {
                    const phi = Math.acos(-1 + (2 * i) / n);
                    const theta = Math.sqrt(n * Math.PI) * phi;
                    x.push(Math.cos(theta) * Math.sin(phi) * 100);
                    y.push(Math.sin(theta) * Math.sin(phi) * 100);
                    z.push(Math.cos(phi) * 100);
                    color.push(i % 3 === 0 ? '#00e676' : (i % 3 === 1 ? '#d4af37' : '#00e5ff'));
                  }
                  const traceNodes = {
                    type: 'scatter3d', mode: 'markers+text',
                    x: x, y: y, z: z,
                    marker: { size: 6, color: color, line: { color: '#fff', width: 1 } },
                    text: x.map((_, i) => 'Node ' + (i+1)),
                    textfont: { color: '#fffefa', size: 9 }
                  };
                  const layout = {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { showgrid: false, zeroline: false, showticklabels: false },
                      yaxis: { showgrid: false, zeroline: false, showticklabels: false },
                      zaxis: { showgrid: false, zeroline: false, showticklabels: false },
                      camera: { eye: { x: 1.4, y: 1.4, z: 1.2 } }
                    }
                  };
                  Plotly.newPlot('plotly-3d-net-stage', [traceNodes], layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Fibonacci spherical spiral lattice: uniform distribution of $N$ points on 3D sphere $S^2$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Global corporate holding webs, international satellite communications, orbital constellations.'},
                {'title': 'Technical Strengths', 'desc': 'Full 3D orbit controls, eliminates planar edge tangles, captivating executive presentation.'}
            ],
            'metrics': [
                {'label': 'Sphere Math', 'val': 'Fibonacci Lattice', 'sub': 'Uniform S2'},
                {'label': 'Rendering', 'val': 'WebGL 3D', 'sub': 'Three.js / Plotly'},
                {'label': 'Orbit', 'val': 'Quaternion Drag', 'sub': 'Smooth Roll'},
                {'label': 'Performance', 'val': '60 FPS', 'sub': 'Hardware Sync'}
            ],
            'code_snippet': """ForceGraph3D()(container)
  .graphData(gData)
  .nodeColor(d => d.color)
  .nodeRelSize(6);"""
        }
    ]

    html = generate_deck_html(deck_meta, slides)
    out_path = os.path.join(SCRIPT_DIR, "03-javascript-networks-graphs.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Built {out_path} (20 slides, {len(html)} bytes)")

if __name__ == "__main__":
    build_deck()
