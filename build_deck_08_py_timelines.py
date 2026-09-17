"""
Builder for Deck 08: Python Timelines, Network & Specialized Visualization
Generates 08-python-timelines-networks.html (20 distinct visual paradigms)
"""
import os
from template_engine import generate_deck_html

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_deck():
    deck_meta = {
        'id': 'deck-08',
        'series_num': '08',
        'title': 'Python Timelines, Network & Specialized Visualization',
        'category': 'Python Networks & Timelines',
        'subtitle': '20 Specialized Paradigms across NetworkX, PyVis, Matplotlib Eventplots, Broken Barh, and Duality Timelines'
    }

    slides = [
        # 1. PyVis Interactive Physics Force Graph with Gravity Sliders
        {
            'slide_id': 'slide-01-pyvis-physics',
            'tag': '01 / Physics-Engine Graphs',
            'headline': 'Interactive Dynamic Physics:',
            'headline_span': 'PyVis Standalone HTML Force Graph',
            'subtitle': 'Generates self-contained interactive Vis.js physics networks directly from NetworkX Python graph objects.',
            'library_badge': 'PyVis (Vis.js Python Wrapper)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Physics Nodes connected with springs -->
                  <g stroke="#d4af37" stroke-width="1.5">
                    <line x1="80" y1="120" x2="175" y2="70"/>
                    <line x1="175" y1="70" x2="270" y2="120"/>
                    <line x1="270" y1="120" x2="175" y2="170"/>
                    <line x1="175" y1="170" x2="80" y2="120"/>
                    <line x1="175" y1="70" x2="175" y2="170"/>
                  </g>
                  <circle cx="80" cy="120" r="14" fill="#00e676"/>
                  <circle cx="175" cy="70" r="16" fill="#f3cf65"/>
                  <circle cx="270" cy="120" r="14" fill="#00e5ff"/>
                  <circle cx="175" cy="170" r="16" fill="#ff1744"/>
                  <text x="175" y="74" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="9" font-weight="bold">PMS Core</text>
                  <text x="80" y="124" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="9" font-weight="bold">Direct</text>
                  <text x="270" y="124" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="9" font-weight="bold">Meta</text>
                  <text x="175" y="174" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9" font-weight="bold">OTA</text>
                  <text x="175" y="225" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Drag Nodes to Trigger Live Vis.js Physics Engine</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Converts NetworkX `nx.Graph` data structures into interactive HTML/Vis.js JavaScript physics bundles.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Presenting complex network graphs to non-technical stakeholders who want interactive click-and-drag capability.'},
                {'title': 'Technical Strengths', 'desc': 'Generates standalone HTML files without requiring a Node.js build pipeline or web server.'}
            ],
            'metrics': [
                {'label': 'Input', 'val': 'networkx.Graph', 'sub': 'Python Native'},
                {'label': 'Output', 'val': 'Interactive HTML', 'sub': 'Vis.js Powered'},
                {'label': 'UI Controls', 'val': 'Live Physics Sliders', 'sub': 'Gravity / Spring'},
                {'label': 'Delivery', 'val': 'Self-Contained', 'sub': 'Zero Dependencies'}
            ],
            'code_snippet': """from pyvis.network import Network
net = Network(notebook=False, bgcolor="#070c09", font_color="#fff")
net.from_nx(G)
net.show_buttons(filter_=['physics'])
net.save_graph("network.html")"""
        },

        # 2. Matplotlib Broken Barh Machine Allocation Gantt
        {
            'slide_id': 'slide-02-mpl-brokenbarh',
            'tag': '02 / Native Python Gantt',
            'headline': 'Discontinuous Scheduling:',
            'headline_span': 'Matplotlib Broken Barh Allocation',
            'subtitle': 'High-performance native timeline plotting non-contiguous server and operational activity windows.',
            'library_badge': 'Matplotlib broken_barh',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 240" style="width:100%; max-height:260px;">
                  <!-- Y Axis Labels -->
                  <text x="75" y="60" text-anchor="end" fill="#fffefa" font-family="DM Sans" font-size="11">Direct Engine</text>
                  <text x="75" y="110" text-anchor="end" fill="#fffefa" font-family="DM Sans" font-size="11">Google Meta</text>
                  <text x="75" y="160" text-anchor="end" fill="#fffefa" font-family="DM Sans" font-size="11">OTA Polling</text>
                  <!-- Bars -->
                  <rect x="90" y="45" width="90" height="22" fill="#00e676" rx="3"/>
                  <rect x="200" y="45" width="140" height="22" fill="#00e676" rx="3"/>
                  <rect x="90" y="95" width="160" height="22" fill="#d4af37" rx="3"/>
                  <rect x="270" y="95" width="80" height="22" fill="#d4af37" rx="3"/>
                  <rect x="120" y="145" width="60" height="22" fill="#ff1744" rx="3"/>
                  <rect x="220" y="145" width="120" height="22" fill="#ff1744" rx="3"/>
                  <!-- Time Axis -->
                  <line x1="90" y1="185" x2="360" y2="185" stroke="rgba(255,255,255,0.2)"/>
                  <text x="90" y="205" fill="#9ba9a1" font-family="JetBrains Mono" font-size="9">00:00</text>
                  <text x="225" y="205" fill="#9ba9a1" font-family="JetBrains Mono" font-size="9">12:00</text>
                  <text x="360" y="205" fill="#9ba9a1" font-family="JetBrains Mono" font-size="9">24:00</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Accepts sequence of horizontal start-duration pairs: `[(start_1, len_1), (start_2, len_2)]` mapped to vertical offset intervals.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Manufacturing equipment utilization schedules, airline flight turnaround Gantt, CPU thread scheduling.'},
                {'title': 'Technical Strengths', 'desc': 'Ultra-fast vector rendering with zero JavaScript dependency; ideal for automated PDF executive reports.'}
            ],
            'metrics': [
                {'label': 'Python Core', 'val': 'ax.broken_barh()', 'sub': 'Native Matplotlib'},
                {'label': 'Data Format', 'val': 'Tuples (Start, Dur)', 'sub': 'Compact Memory'},
                {'label': 'Resolution', 'val': 'Microsecond Exact', 'sub': 'Continuous Time'},
                {'label': 'Export', 'val': 'PDF / SVG / EPS', 'sub': 'Lossless Vector'}
            ],
            'code_snippet': """fig, ax = plt.subplots()
ax.broken_barh([(0, 90), (200, 140)], (40, 20), facecolors='#00e676')
ax.broken_barh([(0, 160), (270, 80)], (10, 20), facecolors='#d4af37')"""
        },

        # 3. NetworkX Bipartite Affiliation Graph
        {
            'slide_id': 'slide-03-nx-bipartite',
            'tag': '03 / NetworkX 2-Mode Graphs',
            'headline': 'Dual-Partition Networks:',
            'headline_span': 'NetworkX Bipartite Projection',
            'subtitle': 'Two-mode corporate network projecting inter-firm corporate director affiliations onto ownership webs.',
            'library_badge': 'NetworkX Bipartite',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Top Layer: Directors -->
                  <circle cx="80" cy="50" r="10" fill="#f3cf65"/>
                  <circle cx="175" cy="50" r="10" fill="#f3cf65"/>
                  <circle cx="270" cy="50" r="10" fill="#f3cf65"/>
                  <!-- Bottom Layer: Boards -->
                  <rect x="60" y="160" width="50" height="24" fill="#1b2822" stroke="#00e676" rx="4"/>
                  <rect x="150" y="160" width="50" height="24" fill="#1b2822" stroke="#00e676" rx="4"/>
                  <rect x="240" y="160" width="50" height="24" fill="#1b2822" stroke="#00e676" rx="4"/>
                  <!-- Bipartite Edges -->
                  <g stroke="#d4af37" stroke-width="1.5">
                    <line x1="80" y1="50" x2="85" y2="160"/>
                    <line x1="80" y1="50" x2="175" y2="160"/>
                    <line x1="175" y1="50" x2="175" y2="160"/>
                    <line x1="175" y1="50" x2="265" y2="160"/>
                    <line x1="270" y1="50" x2="265" y2="160"/>
                  </g>
                  <text x="175" y="25" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Board Directors (Set U)</text>
                  <text x="175" y="215" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="10">Corporate Entities (Set V)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Bipartite graph projection using adjacency matrix multiplication: $B_{\\text{proj}} = A A^T$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate governance interlocking directorates, customer-to-product market baskets, medical drug-target interactions.'},
                {'title': 'Technical Strengths', 'desc': 'Provides formal graph algorithms (maximum matching, vertex covers, bipartite degree centralities).'}
            ],
            'metrics': [
                {'label': 'Graph Class', 'val': 'Bipartite 2-Mode', 'sub': 'Disjoint Partitions'},
                {'label': 'Projection', 'val': 'Weighted 1-Mode', 'sub': 'Affiliation'},
                {'label': 'Algorithms', 'val': 'Hopcroft-Karp', 'sub': 'Max Matching'},
                {'label': 'Ecosystem', 'val': 'NetworkX Core', 'sub': 'Pure Python'}
            ],
            'code_snippet': """from networkx.algorithms import bipartite
B = nx.Graph()
B.add_nodes_from(directors, bipartite=0)
B.add_nodes_from(companies, bipartite=1)
proj = bipartite.projected_graph(B, directors)"""
        },

        # 4. Matplotlib Eventplot Neural Spike Trains
        {
            'slide_id': 'slide-04-mpl-eventplot',
            'tag': '04 / Spike Telemetry',
            'headline': 'High-Frequency Event Trains:',
            'headline_span': 'Matplotlib Eventplot Spike Raster',
            'subtitle': 'Raster plot displaying millisecond-scale discrete point events across multiple telemetry channels.',
            'library_badge': 'Matplotlib eventplot',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:15px; box-sizing:border-box;">
                <svg viewBox="0 0 450 240" style="width:100%; max-height:260px; background:#070d09; border-radius:6px;">
                  <!-- 4 Event Channels with vertical tick marks -->
                  <!-- Channel 1 (Green) -->
                  <text x="30" y="55" fill="#00e676" font-family="JetBrains Mono" font-size="9">API Gateway</text>
                  <g stroke="#00e676" stroke-width="2">
                    <line x1="120" y1="40" x2="120" y2="60"/>
                    <line x1="140" y1="40" x2="140" y2="60"/>
                    <line x1="145" y1="40" x2="145" y2="60"/>
                    <line x1="210" y1="40" x2="210" y2="60"/>
                    <line x1="280" y1="40" x2="280" y2="60"/>
                    <line x1="340" y1="40" x2="340" y2="60"/>
                  </g>
                  <!-- Channel 2 (Gold) -->
                  <text x="30" y="105" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">Booking Engines</text>
                  <g stroke="#f3cf65" stroke-width="2">
                    <line x1="130" y1="90" x2="130" y2="110"/>
                    <line x1="180" y1="90" x2="180" y2="110"/>
                    <line x1="215" y1="90" x2="215" y2="110"/>
                    <line x1="310" y1="90" x2="310" y2="110"/>
                  </g>
                  <!-- Channel 3 (Red Alerts) -->
                  <text x="30" y="155" fill="#ff1744" font-family="JetBrains Mono" font-size="9">Parity Leaks</text>
                  <g stroke="#ff1744" stroke-width="2.5">
                    <line x1="212" y1="140" x2="212" y2="160"/>
                    <line x1="218" y1="140" x2="218" y2="160"/>
                  </g>
                  <!-- Timeline baseline -->
                  <line x1="100" y1="190" x2="420" y2="190" stroke="rgba(255,255,255,0.15)"/>
                  <text x="215" y="210" text-anchor="middle" fill="#ff1744" font-family="JetBrains Mono" font-size="9">&uarr; Synchronized Spike Burst (14:15:22)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Point process temporal representation: $S(t) = \\sum_i \\delta(t - t_i)$ displayed as 1D vertical ticks.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Neuroscience spike train telemetry, cybersecurity DDoS packet bursts, financial limit order arrivals.'},
                {'title': 'Technical Strengths', 'desc': 'Extremely memory efficient for visualizing millions of discrete event times across hundreds of parallel channels.'}
            ],
            'metrics': [
                {'label': 'Function', 'val': 'ax.eventplot()', 'sub': 'Point Process'},
                {'label': 'Resolution', 'val': 'Sub-Millisecond', 'sub': 'Time Exact'},
                {'label': 'Visual Noise', 'val': 'Zero Area Waste', 'sub': 'Crisp Ticks'},
                {'label': 'Scalability', 'val': 'Thousands of Rows', 'sub': 'Fast Render'}
            ],
            'code_snippet': """import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.eventplot(spike_trains, lineoffsets=[1, 2, 3],
             linelengths=0.8, colors=['#00e676', '#f3cf65', '#ff1744'])"""
        },

        # 5. PyVis Hierarchical Tree Flow with Collapse/Expand
        {
            'slide_id': 'slide-05-pyvis-tree',
            'tag': '05 / Collapsible Tree Topologies',
            'headline': 'Interactive Tree Exploration:',
            'headline_span': 'PyVis Collapsible Hierarchies',
            'subtitle': 'Hierarchical tree layout with automated branch collapse and expansion on node double-click.',
            'library_badge': 'PyVis Layout',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                <div style="background:#13221b; border:2px solid #d4af37; border-radius:6px; padding:8px 18px; text-align:center;">
                  <strong style="color:#f3cf65; font-family:JetBrains Mono;">Global Brand Holdings</strong>
                </div>
                <div style="width:2px; height:20px; background:#d4af37;"></div>
                <div style="display:flex; gap:30px;">
                  <div style="background:#101a16; border:1px solid #00e676; border-radius:4px; padding:6px 14px;">
                    <strong style="color:#00e676; font-size:0.85rem;">Luxury Urban</strong>
                  </div>
                  <div style="background:#101a16; border:1px solid #00e5ff; border-radius:4px; padding:6px 14px;">
                    <strong style="color:#00e5ff; font-size:0.85rem;">Resort & Spa</strong>
                  </div>
                </div>
                <div style="margin-top:14px; font-size:0.8rem; color:#9ba9a1;">
                  Double-click branch nodes to collapse / expand sub-trees dynamically
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Directed hierarchical graph layout computing node levels $L(v)$ and horizontal spacing to minimize edge crossings.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate entity tax structuring, enterprise IT network subnets, file directory browsing.'},
                {'title': 'Technical Strengths', 'desc': 'Enables non-technical executives to navigate massive corporate trees without overwhelming visual clutter.'}
            ],
            'metrics': [
                {'label': 'Hierarchy', 'val': 'Top-Down Directed', 'sub': 'Tree Layout'},
                {'label': 'Interaction', 'val': 'Collapse / Expand', 'sub': 'Double-Click'},
                {'label': 'Output', 'val': 'Interactive HTML', 'sub': 'PyVis Standalone'},
                {'label': 'Physics', 'val': 'Hierarchical Repulsion', 'sub': 'Smooth Spring'}
            ],
            'code_snippet': """net = Network(layout='hierarchical')
net.set_options('{"layout": {"hierarchical": {"direction": "UD", "sortMethod": "directed"}}}')
net.from_nx(tree_graph)"""
        },

        # 6. NetworkX Betweenness Centrality Heatmap
        {
            'slide_id': 'slide-06-nx-centrality',
            'tag': '06 / Critical Bottlenecks',
            'headline': 'Information Gatekeepers:',
            'headline_span': 'NetworkX Betweenness Centrality',
            'subtitle': 'Quantifies the proportion of all shortest network paths passing through a specific hub node.',
            'library_badge': 'NetworkX Centrality',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 380 240" style="width:100%; max-height:260px;">
                  <!-- Left Cluster -->
                  <circle cx="80" cy="80" r="8" fill="#1b382b" stroke="#00e676"/>
                  <circle cx="80" cy="160" r="8" fill="#1b382b" stroke="#00e676"/>
                  <circle cx="50" cy="120" r="8" fill="#1b382b" stroke="#00e676"/>
                  <!-- Right Cluster -->
                  <circle cx="300" cy="80" r="8" fill="#1b382b" stroke="#00e676"/>
                  <circle cx="300" cy="160" r="8" fill="#1b382b" stroke="#00e676"/>
                  <circle cx="330" cy="120" r="8" fill="#1b382b" stroke="#00e676"/>
                  <!-- Edges to Bridge Node -->
                  <g stroke="rgba(212,175,55,0.4)" stroke-width="1.5">
                    <line x1="80" y1="80" x2="190" y2="120"/>
                    <line x1="80" y1="160" x2="190" y2="120"/>
                    <line x1="50" y1="120" x2="190" y2="120"/>
                    <line x1="300" y1="80" x2="190" y2="120"/>
                    <line x1="300" y1="160" x2="190" y2="120"/>
                    <line x1="330" y1="120" x2="190" y2="120"/>
                  </g>
                  <!-- Critical Bridge Node (High Centrality Core) -->
                  <circle cx="190" cy="120" r="22" fill="#ff1744" stroke="#fff" stroke-width="2.5" filter="drop-shadow(0 0 12px #ff1744)"/>
                  <text x="190" y="124" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9" font-weight="bold">Cb = 0.94</text>
                  <text x="190" y="210" text-anchor="middle" fill="#ff1744" font-family="DM Sans" font-size="10" font-weight="bold">Single-Point-of-Failure Chokepoint</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Brandes algorithm computing betweenness centrality: $C_B(v) = \\sum_{s \\neq v \\neq t} \\frac{\\sigma_{st}(v)}{\\sigma_{st}}$ in $O(V \\cdot E)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Identifying critical communication chokepoints in executive organizations, supplier dependency bottlenecks.'},
                {'title': 'Technical Strengths', 'desc': 'High-performance Brandes algorithm implementation in Python/C.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': "Brandes' Fast Cb", 'sub': 'O(V*E) Complexity'},
                {'label': 'Metric', 'val': 'Betweenness (0 to 1)', 'sub': 'Path Fraction'},
                {'label': 'Vulnerability', 'val': 'Chokepoint Highlight', 'sub': 'Red Alert'},
                {'label': 'Library', 'val': 'networkx.centrality', 'sub': 'Standard'}
            ],
            'code_snippet': """import networkx as nx
cb = nx.betweenness_centrality(G)
node_colors = [cb[n] for n in G.nodes()]
nx.draw(G, node_color=node_colors, cmap='plasma')"""
        },

        # 7. Matplotlib Multi-Tier Project Timeline with Critical Path
        {
            'slide_id': 'slide-07-mpl-timeline',
            'tag': '07 / Multi-Tier Roadmaps',
            'headline': 'Production Project Roadmaps:',
            'headline_span': 'Matplotlib Phased Timeline & Milestones',
            'subtitle': 'Publication-grade multi-track Gantt timeline linking project phases to milestone stage gates.',
            'library_badge': 'Matplotlib Custom Timeline',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 240" style="width:100%; max-height:260px;">
                  <!-- Track 1 -->
                  <rect x="60" y="40" width="120" height="26" fill="#1b2822" stroke="#00e676" rx="4"/>
                  <text x="120" y="57" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="10">Phase 1: Direct Web</text>
                  <!-- Track 2 -->
                  <rect x="160" y="90" width="140" height="26" fill="#1b2822" stroke="#d4af37" rx="4"/>
                  <text x="230" y="107" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Phase 2: Parity Defense</text>
                  <!-- Track 3 -->
                  <rect x="260" y="140" width="100" height="26" fill="#1b2822" stroke="#00e5ff" rx="4"/>
                  <text x="310" y="157" text-anchor="middle" fill="#00e5ff" font-family="DM Sans" font-size="10">Phase 3: MCP Agent</text>
                  <!-- Dependency link lines -->
                  <path d="M 180 53 L 200 53 L 200 90" fill="none" stroke="#d4af37" stroke-width="1.5" stroke-dasharray="2"/>
                  <path d="M 300 103 L 320 103 L 320 140" fill="none" stroke="#00e5ff" stroke-width="1.5" stroke-dasharray="2"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Coordinate projection mapping discrete calendar dates to continuous matplotlib units with barh layering.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Board quarterly strategy presentations, project management milestone reviews, M&A timelines.'},
                {'title': 'Technical Strengths', 'desc': 'Completely scriptable via Python, outputting lossless high-resolution SVG and vector PDF graphics.'}
            ],
            'metrics': [
                {'label': 'Render Backend', 'val': 'Matplotlib Patches', 'sub': 'Polygon Rect'},
                {'label': 'Dates', 'val': 'mdates.DateFormatter', 'sub': 'Auto-Locators'},
                {'label': 'Output', 'val': 'Lossless PDF / SVG', 'sub': 'Vector Crisp'},
                {'label': 'Automation', 'val': 'Scriptable Python', 'sub': 'Automated Run'}
            ],
            'code_snippet': """ax.barh(y=lanes, width=durations, left=starts, color=colors)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))"""
        },

        # 8. NetworkX Minimum Spanning Tree with Edge Cost Labels
        {
            'slide_id': 'slide-08-nx-mst',
            'tag': '08 / Minimum Cost Trees',
            'headline': 'Spanning Optimization:',
            'headline_span': 'NetworkX MST with Edge Costs',
            'subtitle': 'Identifies the minimal cost distribution network connecting all hotel assets without redundancy.',
            'library_badge': 'NetworkX tree.minimum_spanning_tree',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Redundant Edges (Discarded - Red Dashed) -->
                  <line x1="80" y1="60" x2="270" y2="60" stroke="#ff1744" stroke-width="1.5" stroke-dasharray="3"/>
                  <text x="175" y="50" text-anchor="middle" fill="#ff1744" font-family="JetBrains Mono" font-size="8">$85k Discarded</text>
                  <!-- MST Edges (Green Solid) -->
                  <line x1="80" y1="60" x2="140" y2="130" stroke="#00e676" stroke-width="3"/>
                  <text x="100" y="105" fill="#00e676" font-family="JetBrains Mono" font-size="8">$12k</text>
                  <line x1="140" y1="130" x2="220" y2="130" stroke="#00e676" stroke-width="3"/>
                  <text x="180" y="145" fill="#00e676" font-family="JetBrains Mono" font-size="8">$18k</text>
                  <line x1="220" y1="130" x2="270" y2="60" stroke="#00e676" stroke-width="3"/>
                  <text x="255" y="105" fill="#00e676" font-family="JetBrains Mono" font-size="8">$15k</text>
                  <!-- Nodes -->
                  <circle cx="80" cy="60" r="10" fill="#f3cf65"/>
                  <circle cx="140" cy="130" r="12" fill="#00e676"/>
                  <circle cx="220" cy="130" r="12" fill="#00e676"/>
                  <circle cx="270" cy="60" r="10" fill="#f3cf65"/>
                  <text x="175" y="215" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="10">Minimum Spanning Tree: $45k Optimal Cost</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Kruskal / Prim minimum spanning tree algorithm: finding tree $T \\subseteq G$ minimizing $\\sum_{e \\in T} w(e)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Centralized IT server interconnects, hotel supply chain regional delivery routes, fiber backbones.'},
                {'title': 'Technical Strengths', 'desc': 'Built-in `nx.minimum_spanning_tree()` execution with automatic edge attribute preservation.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': 'nx.minimum_spanning_tree', 'sub': 'Kruskal/Prim'},
                {'label': 'Cycles', 'val': 'Strictly Zero', 'sub': 'Acyclic Tree'},
                {'label': 'Nodes Connected', 'val': 'All |V| Nodes', 'sub': 'Full Coverage'},
                {'label': 'Complexity', 'val': 'O(E log V)', 'sub': 'Fast Heuristic'}
            ],
            'code_snippet': """mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
pos = nx.spring_layout(mst)
nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)"""
        },

        # 9. PyVis Community Detection Louvain Clusters
        {
            'slide_id': 'slide-09-pyvis-louvain',
            'tag': '09 / Community Modularity',
            'headline': 'Unsupervised Community Detection:',
            'headline_span': 'PyVis Louvain Modularity Clusters',
            'subtitle': 'Heuristic modularity optimization partitioning hotel portfolio assets into organic operational clusters.',
            'library_badge': 'PyVis Louvain Engine',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Cluster A (Green) -->
                  <ellipse cx="110" cy="110" rx="60" ry="50" fill="rgba(0,230,118,0.12)" stroke="#00e676" stroke-dasharray="3"/>
                  <circle cx="90" cy="95" r="8" fill="#00e676"/>
                  <circle cx="130" cy="100" r="8" fill="#00e676"/>
                  <circle cx="105" cy="130" r="8" fill="#00e676"/>
                  <!-- Cluster B (Gold) -->
                  <ellipse cx="240" cy="110" rx="60" ry="50" fill="rgba(212,175,55,0.12)" stroke="#d4af37" stroke-dasharray="3"/>
                  <circle cx="220" cy="95" r="8" fill="#f3cf65"/>
                  <circle cx="260" cy="100" r="8" fill="#f3cf65"/>
                  <circle cx="235" cy="130" r="8" fill="#f3cf65"/>
                  <!-- Bridge Edge -->
                  <line x1="130" y1="100" x2="220" y2="95" stroke="#fff" stroke-width="1.5" stroke-dasharray="2"/>
                  <text x="110" y="180" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="10">Cluster 1: Urban Flagships</text>
                  <text x="240" y="180" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Cluster 2: Boutique Resorts</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Louvain algorithm modularity optimization: $Q = \\frac{1}{2m} \\sum_{i,j} \\left[ A_{ij} - \\frac{k_i k_j}{2m} \\right] \\delta(c_i, c_j)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Customer behavioral segmentation, fraud syndicate ring detection, asset portfolio sub-grouping.'},
                {'title': 'Technical Strengths', 'desc': 'Color codes distinct detected communities automatically inside interactive browser physics networks.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': 'Louvain Modularity', 'sub': 'Unsupervised'},
                {'label': 'Modularity Q', 'val': 'Q > 0.65', 'sub': 'Strong Clusters'},
                {'label': 'Coloring', 'val': 'Auto-Palette', 'sub': 'Per-Community'},
                {'label': 'Interactivity', 'val': 'Drag Physics', 'sub': 'Real-Time'}
            ],
            'code_snippet': """import community as community_louvain
partition = community_louvain.best_partition(G)
for node, comm_id in partition.items():
    net.get_node(node)['color'] = palette[comm_id]"""
        },

        # 10. Matplotlib Historical Chronological Milestone Stem Plot
        {
            'slide_id': 'slide-10-mpl-stem',
            'tag': '10 / Chronological Stems',
            'headline': 'Alternating Stem Timelines:',
            'headline_span': 'Matplotlib Stem Plot Markers',
            'subtitle': 'Staggered vertical stem plots displaying chronological milestones above and below an baseline axis.',
            'library_badge': 'Matplotlib stem',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 240" style="width:100%; max-height:260px;">
                  <!-- Baseline Axis -->
                  <line x1="30" y1="120" x2="370" y2="120" stroke="#d4af37" stroke-width="2"/>
                  <!-- Stem 1 (Up) -->
                  <line x1="80" y1="120" x2="80" y2="60" stroke="#00e676" stroke-width="2"/>
                  <circle cx="80" cy="60" r="6" fill="#00e676"/>
                  <text x="80" y="45" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="9">2015 GHA</text>
                  <!-- Stem 2 (Down) -->
                  <line x1="160" y1="120" x2="160" y2="180" stroke="#f3cf65" stroke-width="2"/>
                  <circle cx="160" cy="180" r="6" fill="#f3cf65"/>
                  <text x="160" y="200" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">2018 Direct Engine</text>
                  <!-- Stem 3 (Up) -->
                  <line x1="250" y1="120" x2="250" y2="50" stroke="#00e5ff" stroke-width="2"/>
                  <circle cx="250" cy="50" r="6" fill="#00e5ff"/>
                  <text x="250" y="35" text-anchor="middle" fill="#00e5ff" font-family="JetBrains Mono" font-size="9">2022 CDP Mesh</text>
                  <!-- Stem 4 (Down) -->
                  <line x1="330" y1="120" x2="330" y2="180" stroke="#00e676" stroke-width="2"/>
                  <circle cx="330" cy="180" r="6" fill="#00e676"/>
                  <text x="330" y="200" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="9">2026 Sovereign AI</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Dirac-delta impulse representation: vertical lines from baseline $y_0$ to discrete event timestamps $t_i$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate historical roadmaps, product release milestones, financial audit discovery sequences.'},
                {'title': 'Technical Strengths', 'desc': 'Crystal clear visual aesthetics with zero risk of horizontal label collision.'}
            ],
            'metrics': [
                {'label': 'Function', 'val': 'plt.stem()', 'sub': 'Discrete Impulse'},
                {'label': 'Orientation', 'val': 'Alternating ±y', 'sub': 'Staggered'},
                {'label': 'Markers', 'val': 'Stem Caps', 'sub': 'Custom Shapes'},
                {'label': 'Styling', 'val': 'Publication Grade', 'sub': 'Lossless PDF'}
            ],
            'code_snippet': """markerline, stemlines, baseline = plt.stem(
    dates, levels, linefmt='#d4af37', markerfmt='o', basefmt='#fff'
)"""
        },

        # 11. NetworkX Ego Graph Extraction
        {
            'slide_id': 'slide-11-nx-ego',
            'tag': '11 / Subgraph Extraction',
            'headline': 'Local Neighborhood Induction:',
            'headline_span': 'NetworkX Induced Ego Subgraphs',
            'subtitle': 'Isolates the sub-network of nodes within radius $k$ around a focal asset to audit immediate counterparty risks.',
            'library_badge': 'NetworkX ego_graph',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Induced boundary circle -->
                  <circle cx="175" cy="120" r="75" fill="rgba(212,175,55,0.15)" stroke="#d4af37" stroke-dasharray="3"/>
                  <!-- Center Ego Node -->
                  <circle cx="175" cy="120" r="16" fill="#f3cf65" stroke="#fff" stroke-width="2"/>
                  <text x="175" y="124" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="9" font-weight="bold">EGO</text>
                  <!-- 1-Hop Neighbors -->
                  <circle cx="130" cy="80" r="9" fill="#00e676"/>
                  <circle cx="220" cy="80" r="9" fill="#00e676"/>
                  <circle cx="175" cy="175" r="9" fill="#00e676"/>
                  <line x1="175" y1="120" x2="130" y2="80" stroke="#00e676" stroke-width="2"/>
                  <line x1="175" y1="120" x2="220" y2="80" stroke="#00e676" stroke-width="2"/>
                  <line x1="175" y1="120" x2="175" y2="175" stroke="#00e676" stroke-width="2"/>
                  <text x="175" y="215" text-anchor="middle" fill="#fffefa" font-family="DM Sans" font-size="10">Induced Subgraph G[N(u)] &bull; Radius k=1</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Induced subgraph extraction: $G[V_{\\text{ego}}] = (V_{\\text{ego}}, E_{\\text{ego}})$ where $V_{\\text{ego}} = \\{v \\mid d(u,v) \\le k\\}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Financial counterparty systemic exposure audits, VIP loyalty influencer networks, cyber blast-radius modeling.'},
                {'title': 'Technical Strengths', 'desc': 'Instantly isolates subgraphs in $O(V_{\\text{local}} + E_{\\text{local}})$ from multi-million node graphs.'}
            ],
            'metrics': [
                {'label': 'Function', 'val': 'nx.ego_graph()', 'sub': 'Induced Mesh'},
                {'label': 'Radius', 'val': 'k = 1, 2 Hops', 'sub': 'Distance Bound'},
                {'label': 'Edges', 'val': 'Induced Subset', 'sub': 'Preserved Links'},
                {'label': 'Performance', 'val': 'Microsecond', 'sub': 'BFS Filter'}
            ],
            'code_snippet': """ego = nx.ego_graph(full_graph, n='CentralAsset', radius=1)
nx.draw(ego, with_labels=True, node_color='#00e676')"""
        },

        # 12. PyVis Dark Luxury Corporate Boardroom Web
        {
            'slide_id': 'slide-12-pyvis-boardroom',
            'tag': '12 / Executive Governance',
            'headline': 'Corporate Ownership Webs:',
            'headline_span': 'PyVis Dark Luxury Governance Mesh',
            'subtitle': 'Visualizes parent holding companies, subsidiary OpCo entities, and beneficial owner cross-holdings.',
            'library_badge': 'PyVis Corporate Theme',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Central Institutional Investor -->
                  <circle cx="175" cy="50" r="16" fill="#f3cf65" stroke="#fff" stroke-width="2"/>
                  <text x="175" y="54" text-anchor="middle" fill="#070c09" font-family="DM Sans" font-size="9" font-weight="bold">Holding Co</text>
                  <!-- Mid OpCos -->
                  <circle cx="100" cy="130" r="12" fill="#00e676"/>
                  <circle cx="250" cy="130" r="12" fill="#00e5ff"/>
                  <line x1="175" y1="50" x2="100" y2="130" stroke="#d4af37" stroke-width="2"/>
                  <line x1="175" y1="50" x2="250" y2="130" stroke="#d4af37" stroke-width="2"/>
                  <!-- Properties Below -->
                  <rect x="70" y="180" width="60" height="22" fill="#1b2822" stroke="#00e676" rx="3"/>
                  <rect x="220" y="180" width="60" height="22" fill="#1b2822" stroke="#00e5ff" rx="3"/>
                  <line x1="100" y1="130" x2="100" y2="180" stroke="#00e676" stroke-width="1.5"/>
                  <line x1="250" y1="130" x2="250" y2="180" stroke="#00e5ff" stroke-width="1.5"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Multi-tier directed acyclic ownership graph with edge weights representing percentage shareholding stakes.'},
                {'title': 'Enterprise Use Cases', 'desc': 'M&A due diligence, beneficial ownership transparency, antitrust regulatory compliance.'},
                {'title': 'Technical Strengths', 'desc': 'Customized with Demand Journeys luxury gold, deep obsidian forest, and emerald styling.'}
            ],
            'metrics': [
                {'label': 'Styling', 'val': 'Luxury Dark', 'sub': 'Gold / Forest'},
                {'label': 'Entities', 'val': 'Multi-Tier OpCo', 'sub': 'Cross-Holding'},
                {'label': 'Physics', 'val': 'Stabilized Mesh', 'sub': 'Clean Spacing'},
                {'label': 'Delivery', 'val': 'Self-Contained', 'sub': 'HTML5 / Vis.js'}
            ],
            'code_snippet': """net = Network(bgcolor="#070c09", font_color="#fffefa")
net.add_node("HoldingCo", label="Global Holdings", color="#f3cf65", size=30)
net.add_edge("HoldingCo", "OpCoAsia", value=0.75)"""
        },

        # 13. NetworkX DAG Task Dependencies & Topological Sort
        {
            'slide_id': 'slide-13-nx-dag',
            'tag': '13 / Task Scheduling',
            'headline': 'Deterministic Pipelines:',
            'headline_span': 'NetworkX Topological Task Sort',
            'subtitle': 'Linear ordering of graph vertices such that for every directed edge $(u, v)$, vertex $u$ comes before $v$.',
            'library_badge': 'NetworkX topological_sort',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; gap:14px;">
                <div style="display:flex; gap:16px;">
                  <div style="background:#13221b; border:1px solid #00e676; border-radius:6px; padding:6px 12px; font-family:JetBrains Mono; font-size:0.8rem; color:#00e676;">
                    1. PMS Folio Extract
                  </div>
                  <div style="color:#d4af37; font-weight:bold;">&rarr;</div>
                  <div style="background:#13221b; border:1px solid #f3cf65; border-radius:6px; padding:6px 12px; font-family:JetBrains Mono; font-size:0.8rem; color:#f3cf65;">
                    2. Parity Harmonizer
                  </div>
                  <div style="color:#d4af37; font-weight:bold;">&rarr;</div>
                  <div style="background:#13221b; border:1px solid #00e5ff; border-radius:6px; padding:6px 12px; font-family:JetBrains Mono; font-size:0.8rem; color:#00e5ff;">
                    3. MCP Agent Publish
                  </div>
                </div>
                <div style="font-size:0.8rem; color:#9ba9a1;">
                  Topological Sort Guarantees Precedence Order & Zero Deadlocks
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Kahn’s in-degree zero-elimination topological sorting algorithm running in $O(V + E)$ linear time.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel room distribution rate publishing sequences, software dependency package resolution.'},
                {'title': 'Technical Strengths', 'desc': 'Immediately detects circular dependencies and raises `NetworkXUnfeasible` error on cycles.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': "Kahn's Linear Sort", 'sub': 'O(V + E)'},
                {'label': 'Cycle Check', 'val': 'nx.is_directed_acyclic_graph', 'sub': 'Strict DAG'},
                {'label': 'Determinism', 'val': 'Guaranteed', 'sub': 'Precedence'},
                {'label': 'Framework', 'val': 'networkx.algorithms.dag', 'sub': 'Standard'}
            ],
            'code_snippet': """order = list(nx.topological_sort(task_dag))
# Output: ['Extract', 'Harmonize', 'Publish']"""
        },

        # 14. Matplotlib Calendar Heatmap Timeline
        {
            'slide_id': 'slide-14-mpl-calendar',
            'tag': '14 / Annual Calendar Heatmaps',
            'headline': 'Rolling Annual Telemetry:',
            'headline_span': 'Matplotlib 365-Day Calendar Matrix',
            'subtitle': 'Generates GitHub-style annual daily activity heatmaps mapped across 7 days of week and 52 weeks.',
            'library_badge': 'Matplotlib / Calplot',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 400 160" style="width:100%; max-height:180px;">
                  <g transform="translate(40, 20)">
                    <rect x="0" y="0" width="340" height="90" fill="#070d09" stroke="rgba(255,255,255,0.12)" rx="4"/>
                    <!-- Clustered green squares -->
                    <circle cx="50" cy="45" r="14" fill="#00e676"/>
                    <circle cx="120" cy="45" r="18" fill="#00e676"/>
                    <circle cx="190" cy="45" r="12" fill="#d4af37"/>
                    <circle cx="260" cy="45" r="16" fill="#00e676"/>
                    <text x="170" y="50" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="11" font-weight="bold">365 Days Direct Flow</text>
                  </g>
                  <text x="200" y="140" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Python calplot / matplotlib calendar matrix</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': '2D matrix folding of 365-day time series into calendar day-of-week and week-of-year array coordinates.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Daily direct website booking revenue intensity, corporate IT server uptime, employee attendance.'},
                {'title': 'Technical Strengths', 'desc': 'Pure Python generation outputting publication-ready vector SVG and PDF graphics.'}
            ],
            'metrics': [
                {'label': 'Python Lib', 'val': 'calplot / Matplotlib', 'sub': 'Pandas Datetime'},
                {'label': 'Time Span', 'val': 'Full 365 Days', 'sub': '52 Weeks'},
                {'label': 'Color Ramps', 'val': 'Greens / YlGn', 'sub': 'Intensity'},
                {'label': 'Output', 'val': 'Vector Graphics', 'sub': 'Clean DPI'}
            ],
            'code_snippet': """import calplot
calplot.calplot(series_daily, cmap='YlGn', fillcolor='#070d09')"""
        },

        # 15. NetworkX Circos / Circular Chord Diagram
        {
            'slide_id': 'slide-15-nx-circos',
            'tag': '15 / Circular Chord Networks',
            'headline': 'Circular Inter-Connections:',
            'headline_span': 'NetworkX Circos Chord Diagram',
            'subtitle': 'Arranges nodes along a circular perimeter with curved internal ribbons tracking cross-channel flows.',
            'library_badge': 'PyCircos / NetworkX',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 280 280" style="width:250px; height:250px;">
                  <circle cx="140" cy="140" r="105" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                  <!-- Chords -->
                  <path d="M 50 140 Q 140 140, 140 35" fill="none" stroke="#00e676" stroke-width="2.5" opacity="0.8"/>
                  <path d="M 50 140 Q 140 140, 230 140" fill="none" stroke="#d4af37" stroke-width="2" opacity="0.8"/>
                  <path d="M 140 35 Q 140 140, 205 215" fill="none" stroke="#00e5ff" stroke-width="2" opacity="0.8"/>
                  <!-- Nodes on Ring -->
                  <circle cx="50" cy="140" r="8" fill="#00e676"/>
                  <circle cx="140" cy="35" r="8" fill="#f3cf65"/>
                  <circle cx="230" cy="140" r="8" fill="#00e5ff"/>
                  <circle cx="205" cy="215" r="8" fill="#ff1744"/>
                  <circle cx="75" cy="215" r="8" fill="#b5935b"/>
                  <text x="140" y="145" text-anchor="middle" fill="#fffefa" font-family="Newsreader" font-size="14">Circos</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Circular chord routing: perimeter angular coordinate mapping with interior cubic Bézier connections.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Inter-departmental communication exchanges, banking financial liquidity flows, genomic translocations.'},
                {'title': 'Technical Strengths', 'desc': 'Provides a symmetrical, aesthetically stunning presentation for complex multi-party interactions.'}
            ],
            'metrics': [
                {'label': 'Layout', 'val': 'Circos Perimeter', 'sub': 'Equiangular'},
                {'label': 'Curves', 'val': 'Bézier Splines', 'sub': 'Interior Ribbons'},
                {'label': 'Symmetry', 'val': 'High Aesthetic', 'sub': 'Publication Std'},
                {'label': 'Python', 'val': 'pycircos / NX', 'sub': 'Graph Integration'}
            ],
            'code_snippet': """import pycircos
circos = pycircos.Gcircos()
circos.add_arc(arc_data)
circos.chord_plot(start, end, color='#00e676')"""
        },

        # 16. PyVis Edge-Weight Filter Slider
        {
            'slide_id': 'slide-16-pyvis-filter',
            'tag': '16 / Real-Time Topology Pruning',
            'headline': 'Real-Time Graph Pruning:',
            'headline_span': 'PyVis Dynamic Edge-Weight Filter',
            'subtitle': 'Interactive GUI slider pruning weak transactions to reveal the structural backbone of the network.',
            'library_badge': 'PyVis Interactive Filter',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; padding:15px; box-sizing:border-box;">
                <svg viewBox="0 0 350 180" style="width:100%; max-height:190px;">
                  <!-- Backbone Thick Edges (Retained) -->
                  <line x1="80" y1="90" x2="175" y2="90" stroke="#00e676" stroke-width="4"/>
                  <line x1="175" y1="90" x2="270" y2="90" stroke="#00e676" stroke-width="4"/>
                  <!-- Pruned Thin Edges (Faded Out) -->
                  <line x1="80" y1="90" x2="130" y2="150" stroke="#ff1744" stroke-width="1" stroke-dasharray="2" opacity="0.3"/>
                  <line x1="175" y1="90" x2="220" y2="150" stroke="#ff1744" stroke-width="1" stroke-dasharray="2" opacity="0.3"/>
                  <circle cx="80" cy="90" r="12" fill="#00e676"/>
                  <circle cx="175" cy="90" r="14" fill="#f3cf65"/>
                  <circle cx="270" cy="90" r="12" fill="#00e676"/>
                </svg>
                <!-- Slider Widget UI -->
                <div style="width:75%; display:flex; align-items:center; gap:10px; margin-top:8px;">
                  <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#9ba9a1;">Weight Filter:</span>
                  <div style="flex:1; height:6px; background:rgba(255,255,255,0.15); border-radius:3px; position:relative;">
                    <div style="position:absolute; left:0; width:60%; height:100%; background:#d4af37; border-radius:3px;"></div>
                    <div style="position:absolute; left:60%; top:-4px; width:14px; height:14px; background:#fff; border-radius:50%;"></div>
                  </div>
                  <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#f3cf65;">&ge; $50k Flow</span>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Threshold filtering: $G_\\theta = (V, \\{e \\in E \\mid w(e) \\ge \\theta\\})$ evaluated dynamically upon slider events.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Focusing on top revenue-generating channels while filtering out hundreds of low-volume long-tail bedbanks.'},
                {'title': 'Technical Strengths', 'desc': 'Instant client-side Vis.js filtering without requiring graph re-computation on a Python server.'}
            ],
            'metrics': [
                {'label': 'Filter Logic', 'val': 'Threshold Prune', 'sub': 'w(e) >= theta'},
                {'label': 'Noise Drop', 'val': '-85% Minor Edges', 'sub': 'Backbone Core'},
                {'label': 'Interaction', 'val': 'Live Slider', 'sub': 'HTML Widget'},
                {'label': 'Speed', 'val': '< 10 ms Redraw', 'sub': 'Client Side'}
            ],
            'code_snippet': """net.show_buttons(filter_=['nodes', 'edges'])
net.set_edge_smooth('dynamic')"""
        },

        # 17. NetworkX Spectral Graph Embedding (Laplacian Eigenvectors)
        {
            'slide_id': 'slide-17-nx-spectral',
            'tag': '17 / Spectral Graph Theory',
            'headline': 'Algebraic Connectivity:',
            'headline_span': 'NetworkX Spectral Laplacian Embedding',
            'subtitle': 'Projects graph topology into low-dimensional Euclidean space using eigenvectors of the unnormalized graph Laplacian.',
            'library_badge': 'NetworkX Spectral',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Spectral 2D Coordinate Grid -->
                  <line x1="60" y1="120" x2="290" y2="120" stroke="rgba(255,255,255,0.15)"/>
                  <line x1="175" y1="40" x2="175" y2="200" stroke="rgba(255,255,255,0.15)"/>
                  <!-- Spectral Node Coordinates (Fiedler vector v2 vs v3) -->
                  <circle cx="100" cy="70" r="8" fill="#00e676"/>
                  <circle cx="120" cy="90" r="8" fill="#00e676"/>
                  <circle cx="90" cy="110" r="8" fill="#00e676"/>
                  <circle cx="250" cy="150" r="8" fill="#ff1744"/>
                  <circle cx="270" cy="170" r="8" fill="#ff1744"/>
                  <line x1="100" y1="70" x2="120" y2="90" stroke="#00e676" stroke-width="1.5"/>
                  <line x1="250" y1="150" x2="270" y2="170" stroke="#ff1744" stroke-width="1.5"/>
                  <line x1="120" y1="90" x2="250" y2="150" stroke="#d4af37" stroke-width="1" stroke-dasharray="3"/>
                  <text x="175" y="225" text-anchor="middle" fill="#f3cf65" font-family="JetBrains Mono" font-size="10">Fiedler Vector v₂ (Algebraic Connectivity)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Graph Laplacian matrix: $\\mathbf{L} = \\mathbf{D} - \\mathbf{A}$; layout coordinates $(x,y)$ are given by the 2nd and 3rd smallest eigenvectors.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Spectral graph partitioning, image segmentation, unsupervised social network community discovery.'},
                {'title': 'Technical Strengths', 'desc': 'Global mathematical optimum; entirely avoids local minima traps inherent in force simulations.'}
            ],
            'metrics': [
                {'label': 'Operator', 'val': 'Graph Laplacian L', 'sub': 'D - A Matrix'},
                {'label': 'Fiedler Value', 'val': 'λ2 > 0', 'sub': 'Algebraic Connect'},
                {'label': 'Optimum', 'val': 'Global Rayleigh', 'sub': 'No Local Minima'},
                {'label': 'Complexity', 'val': 'O(V^3) / SciPy Arpack', 'sub': 'Exact SVD'}
            ],
            'code_snippet': """pos = nx.spectral_layout(G)
nx.draw(G, pos, node_color='#00e676')"""
        },

        # 18. Matplotlib Broken Barh Thread Concurrency Profiler
        {
            'slide_id': 'slide-18-mpl-concurrency',
            'tag': '18 / Concurrency Profiling',
            'headline': 'Asynchronous Concurrency:',
            'headline_span': 'CPU Core Thread Timeline Profiler',
            'subtitle': 'Millisecond execution trace mapping concurrent thread execution, lock contention, and idle wait states.',
            'library_badge': 'Execution Trace Profiler',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:20px; box-sizing:border-box;">
                <svg viewBox="0 0 400 180" style="width:100%; max-height:200px;">
                  <!-- 4 CPU Core Rows -->
                  <g font-family="JetBrains Mono" font-size="9" fill="#fff">
                    <text x="50" y="38" text-anchor="end">Core 0</text>
                    <rect x="60" y="25" width="80" height="18" fill="#00e676" rx="2"/>
                    <rect x="160" y="25" width="120" height="18" fill="#00e676" rx="2"/>
                    
                    <text x="50" y="78" text-anchor="end">Core 1</text>
                    <rect x="80" y="65" width="60" height="18" fill="#00e676" rx="2"/>
                    <rect x="150" y="65" width="40" height="18" fill="#ff1744" rx="2"/>
                    <rect x="210" y="65" width="90" height="18" fill="#00e676" rx="2"/>

                    <text x="50" y="118" text-anchor="end">Core 2</text>
                    <rect x="60" y="105" width="180" height="18" fill="#00e676" rx="2"/>
                    
                    <text x="50" y="158" text-anchor="end">Core 3</text>
                    <rect x="120" y="145" width="100" height="18" fill="#d4af37" rx="2"/>
                  </g>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Contiguous memory span collection plotting timestamp intervals $(t_{\\text{start}}, t_{\\text{end}})$ per CPU core.'},
                {'title': 'Enterprise Use Cases', 'desc': 'High-concurrency hotel booking engine latency audits, GIL lock profiling in Python async apps.'},
                {'title': 'Technical Strengths', 'desc': 'Pinpoints thread contention bottlenecks where tasks stall waiting on database locks.'}
            ],
            'metrics': [
                {'label': 'Resolution', 'val': 'Microsecond Trace', 'sub': 'GIL Profiling'},
                {'label': 'Contention', 'val': 'Lock Alert (Red)', 'sub': 'Resource Stall'},
                {'label': 'Concurrency', 'val': 'Multi-Core CPU', 'sub': 'Parallel Tracks'},
                {'label': 'Framework', 'val': 'cProfile / MPL', 'sub': 'Python Native'}
            ],
            'code_snippet': """ax.broken_barh(core_0_spans, (30, 9), facecolors='#00e676')
ax.broken_barh(lock_spans, (20, 9), facecolors='#ff1744')"""
        },

        # 19. PyVis Academic Citation Co-Authorship Network with Node Scaling
        {
            'slide_id': 'slide-19-pyvis-citation',
            'tag': '19 / Academic Citation Graphs',
            'headline': 'Research Citation Authority:',
            'headline_span': 'PyVis Degree-Scaled Citation Mesh',
            'subtitle': 'Node radii scaled proportional to h-index citation counts with edge thickness reflecting co-authorship frequency.',
            'library_badge': 'PyVis Bibliometrics',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <g stroke="#d4af37" stroke-width="2">
                    <line x1="80" y1="120" x2="175" y2="80"/>
                    <line x1="175" y1="80" x2="270" y2="120"/>
                    <line x1="175" y1="80" x2="175" y2="180"/>
                  </g>
                  <!-- Degree-scaled nodes -->
                  <circle cx="175" cy="80" r="24" fill="#f3cf65" stroke="#fff" stroke-width="2"/>
                  <text x="175" y="84" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="9" font-weight="bold">h=48</text>
                  <circle cx="80" cy="120" r="14" fill="#00e676"/>
                  <circle cx="270" cy="120" r="12" fill="#00e5ff"/>
                  <circle cx="175" cy="180" r="10" fill="#00e676"/>
                  <text x="175" y="225" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Node Area = Citation Volume &bull; Link = Co-Authorship</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Non-linear node radius scaling: $r_i = r_{\\min} + k \\cdot \\sqrt{\\text{InDegree}(v)}$; edge width $w = f(\\text{Citations})$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate patent co-citation landscapes, key opinion leader (KOL) discovery, medical literature review.'},
                {'title': 'Technical Strengths', 'desc': 'Interactive node hover highlights all incoming and outgoing citation links dynamically.'}
            ],
            'metrics': [
                {'label': 'Scaling', 'val': 'Square-Root Degree', 'sub': 'Perceptual Safe'},
                {'label': 'Metric', 'val': 'h-index / Citations', 'sub': 'Bibliometrics'},
                {'label': 'Hover', 'val': 'Neighborhood Glow', 'sub': 'Dynamic Tooltip'},
                {'label': 'Engine', 'val': 'Vis.js HTML5 Canvas', 'sub': 'PyVis Python'}
            ],
            'code_snippet': """for node in G.nodes():
    net.add_node(node, size=math.sqrt(citations[node]) * 3,
                 title=f"Citations: {citations[node]}")"""
        },

        # 20. NetworkX 3D Spring Layout Network
        {
            'slide_id': 'slide-20-nx-spring3d',
            'tag': '20 / 3D Graph Optimization',
            'headline': 'Volumetric Graph Topology:',
            'headline_span': 'NetworkX 3D Spring Embedding',
            'subtitle': 'Iterative 3D force simulation resolving complex graph knots by utilizing third spatial dimension coordinates.',
            'library_badge': 'NetworkX dim=3 + Plotly',
            'chart_html': """
              <div id="nx-3d-spring-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('nx-3d-spring-stage');
                  if (!el || !window.Plotly) return;
                  const x = [0, 20, -20, 10, -10];
                  const y = [0, -15, -15, 25, 25];
                  const z = [30, -10, -10, -10, -10];
                  const data = [
                    {
                      type: 'scatter3d', mode: 'lines',
                      x: [0, 20, null, 0, -20, null, 0, 10, null, 0, -10, null, 20, -20, null, 10, -10],
                      y: [0, -15, null, 0, -15, null, 0, 25, null, 0, 25, null, -15, -15, null, 25, 25],
                      z: [30, -10, null, 30, -10, null, 30, -10, null, 30, -10, null, -10, -10, null, -10, -10],
                      line: { color: 'rgba(212, 175, 55, 0.6)', width: 3 }
                    },
                    {
                      type: 'scatter3d', mode: 'markers+text',
                      x: x, y: y, z: z,
                      marker: { size: 10, color: ['#00e676', '#f3cf65', '#f3cf65', '#00e5ff', '#00e5ff'] },
                      text: ['Sovereign Root', 'Node A', 'Node B', 'Node C', 'Node D'],
                      textfont: { color: '#fffefa', size: 10 }
                    }
                  ];
                  Plotly.newPlot('nx-3d-spring-stage', data, {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { showgrid: false, zeroline: false, showticklabels: false },
                      yaxis: { showgrid: false, zeroline: false, showticklabels: false },
                      zaxis: { showgrid: false, zeroline: false, showticklabels: false },
                      camera: { eye: { x: 1.4, y: 1.4, z: 1.2 } }
                    }
                  }, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Fruchterman-Reingold force-directed simulation in $\\mathbb{R}^3$: `nx.spring_layout(G, dim=3)`. '},
                {'title': 'Enterprise Use Cases', 'desc': 'High-density corporate shareholding knots, molecular protein backbones, 3D internet backbone maps.'},
                {'title': 'Technical Strengths', 'desc': 'Eliminates 2D planar edge crossings; nodes untangle cleanly into 3D volumetric space.'}
            ],
            'metrics': [
                {'label': 'Dimensions', 'val': 'R³ Volumetric', 'sub': 'dim=3 Spring'},
                {'label': 'Untangling', 'val': 'Zero Crossing', 'sub': 'Z-Axis Freedom'},
                {'label': 'Visualizer', 'val': 'Plotly 3D WebGL', 'sub': '60 FPS Orbit'},
                {'label': 'Python Spec', 'val': 'nx.spring_layout', 'sub': 'dim=3 Parameter'}
            ],
            'code_snippet': """pos_3d = nx.spring_layout(G, dim=3, seed=42)
# pos_3d[node] -> numpy array [x, y, z]
# Rendered via Plotly go.Scatter3d"""
        }
    ]

    html = generate_deck_html(deck_meta, slides)
    out_path = os.path.join(SCRIPT_DIR, "08-python-timelines-networks.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Built {out_path} (20 slides, {len(html)} bytes)")

if __name__ == "__main__":
    build_deck()
