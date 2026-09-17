"""
Builder for Deck 02: JavaScript Timelines, Gantt & Temporal Data
Generates 02-javascript-timelines-gantt.html (20 distinct visual paradigms)
"""
import os
from template_engine import generate_deck_html

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_deck():
    deck_meta = {
        'id': 'deck-02',
        'series_num': '02',
        'title': 'JavaScript Timelines, Gantt & Temporal Data',
        'category': 'Timelines & Gantt',
        'subtitle': '20 Temporal Visual Paradigms across TimelineJS, Vis.js Timeline, Frappe Gantt, DHTMLX, Timelines-Chart, and CanvasJS'
    }

    slides = [
        # 1. Vis.js Zoomable Multi-Track Timeline
        {
            'slide_id': 'slide-01-vis-timeline',
            'tag': '01 / Multi-Track Temporal Axis',
            'headline': 'Zoomable Multi-Track Axis:',
            'headline_span': 'Vis.js Hierarchical Grouping',
            'subtitle': 'Dynamic real-time zooming across centuries down to milliseconds with custom resource lanes.',
            'library_badge': 'Vis.js Timeline',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:15px; box-sizing:border-box;">
                <svg viewBox="0 0 450 300" style="width:100%; max-height:340px;">
                  <!-- Time Axis Header -->
                  <rect x="0" y="10" width="450" height="28" fill="#13221b" rx="4"/>
                  <text x="50" y="28" fill="#f3cf65" font-family="JetBrains Mono" font-size="11">Q1 Jan</text>
                  <text x="150" y="28" fill="#f3cf65" font-family="JetBrains Mono" font-size="11">Q2 Apr</text>
                  <text x="260" y="28" fill="#f3cf65" font-family="JetBrains Mono" font-size="11">Q3 Jul</text>
                  <text x="370" y="28" fill="#f3cf65" font-family="JetBrains Mono" font-size="11">Q4 Oct</text>
                  
                  <!-- Group 1: Brand Marketing -->
                  <rect x="10" y="55" width="80" height="26" fill="#1b2822" rx="4"/>
                  <text x="20" y="72" fill="#d4af37" font-family="DM Sans" font-size="11" font-weight="bold">Marketing</text>
                  <rect x="100" y="55" width="160" height="26" fill="rgba(0,230,118,0.25)" stroke="#00e676" rx="4"/>
                  <text x="115" y="72" fill="#fffefa" font-family="DM Sans" font-size="11">Spring Direct Push (Jan-May)</text>

                  <!-- Group 2: Revenue Management -->
                  <rect x="10" y="100" width="80" height="26" fill="#1b2822" rx="4"/>
                  <text x="20" y="117" fill="#d4af37" font-family="DM Sans" font-size="11" font-weight="bold">Revenue</text>
                  <rect x="220" y="100" width="140" height="26" fill="rgba(212,175,55,0.25)" stroke="#d4af37" rx="4"/>
                  <text x="235" y="117" fill="#fffefa" font-family="DM Sans" font-size="11">Dynamic Summer Yield</text>

                  <!-- Group 3: Tech & AI Integration -->
                  <rect x="10" y="145" width="80" height="26" fill="#1b2822" rx="4"/>
                  <text x="20" y="162" fill="#d4af37" font-family="DM Sans" font-size="11" font-weight="bold">IT & AI</text>
                  <rect x="150" y="145" width="220" height="26" fill="rgba(0,229,255,0.25)" stroke="#00e5ff" rx="4"/>
                  <text x="165" y="162" fill="#fffefa" font-family="DM Sans" font-size="11">MCP Direct Booking Protocol</text>

                  <!-- Milestone Markers -->
                  <line x1="280" y1="40" x2="280" y2="220" stroke="#ff1744" stroke-width="2" stroke-dasharray="3"/>
                  <rect x="240" y="225" width="80" height="22" fill="#ff1744" rx="4"/>
                  <text x="250" y="240" fill="#fffefa" font-family="JetBrains Mono" font-size="10" font-weight="bold">Aug 15 Launch</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Continuous 1D coordinate affine transform: $x = (t - t_{\\min}) / (t_{\\max} - t_{\\min}) \\cdot W$ with virtual DOM culling.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate project portfolio roadmaps, resource room booking calendars, event logs.'},
                {'title': 'Technical Strengths', 'desc': 'Sub-millisecond inertia scrolling, DOM windowing, dynamic item clustering.'}
            ],
            'metrics': [
                {'label': 'Render Type', 'val': 'DOM / CSS3', 'sub': 'Hardware Smooth'},
                {'label': 'Zoom Range', 'val': 'ms to Millennia', 'sub': 'Dynamic Scale'},
                {'label': 'Clustering', 'val': 'Automatic', 'sub': 'Density Reduction'},
                {'label': 'Interactivity', 'val': 'Drag / Pinch', 'sub': 'Touch Native'}
            ],
            'code_snippet': """const timeline = new vis.Timeline(container, items, groups, {
  zoomMin: 1000 * 60 * 60,
  zoomMax: 1000 * 60 * 60 * 24 * 365 * 10
});"""
        },

        # 2. Critical Path Gantt with Dependency Arrows
        {
            'slide_id': 'slide-02-critical-path-gantt',
            'tag': '02 / Project Precedence',
            'headline': 'Precedence Engineering:',
            'headline_span': 'Critical Path Method (CPM) Gantt',
            'subtitle': 'Topologically sorted tasks with early/late start calculation and automated slack time visualization.',
            'library_badge': 'Frappe / DHTMLX Gantt',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:10px;">
                <svg viewBox="0 0 450 300" style="width:100%; max-height:340px;">
                  <!-- Grid -->
                  <line x1="120" y1="20" x2="120" y2="280" stroke="rgba(255,255,255,0.1)"/>
                  <line x1="220" y1="20" x2="220" y2="280" stroke="rgba(255,255,255,0.06)"/>
                  <line x1="320" y1="20" x2="320" y2="280" stroke="rgba(255,255,255,0.06)"/>
                  <line x1="420" y1="20" x2="420" y2="280" stroke="rgba(255,255,255,0.06)"/>

                  <!-- Task 1: Audit -->
                  <text x="110" y="55" text-anchor="end" fill="#fffefa" font-family="DM Sans" font-size="11">1. Forensic Audit</text>
                  <rect x="130" y="40" width="80" height="22" fill="#ff1744" rx="3"/>
                  <text x="140" y="55" fill="#fff" font-family="JetBrains Mono" font-size="10">Crit: 14d</text>

                  <!-- Task 2: Architecture -->
                  <text x="110" y="105" text-anchor="end" fill="#fffefa" font-family="DM Sans" font-size="11">2. Data Contract</text>
                  <rect x="210" y="90" width="90" height="22" fill="#ff1744" rx="3"/>
                  <text x="220" y="105" fill="#fff" font-family="JetBrains Mono" font-size="10">Crit: 21d</text>

                  <!-- Task 3: Content (Slack) -->
                  <text x="110" y="155" text-anchor="end" fill="#9ba9a1" font-family="DM Sans" font-size="11">3. Asset Ingestion</text>
                  <rect x="210" y="140" width="60" height="22" fill="#d4af37" opacity="0.8" rx="3"/>
                  <rect x="270" y="140" width="50" height="22" fill="none" stroke="#d4af37" stroke-dasharray="3" rx="3"/>
                  <text x="280" y="155" fill="#d4af37" font-family="JetBrains Mono" font-size="10">Slack 10d</text>

                  <!-- Task 4: Deployment -->
                  <text x="110" y="205" text-anchor="end" fill="#fffefa" font-family="DM Sans" font-size="11">4. Engine Cutover</text>
                  <rect x="300" y="190" width="80" height="22" fill="#ff1744" rx="3"/>
                  <text x="310" y="205" fill="#fff" font-family="JetBrains Mono" font-size="10">Crit: 18d</text>

                  <!-- Dependency Connectors -->
                  <path d="M 210 51 L 220 51 L 220 90 L 212 90" fill="none" stroke="#ff1744" stroke-width="2"/>
                  <path d="M 300 101 L 310 101 L 310 190 L 302 190" fill="none" stroke="#ff1744" stroke-width="2"/>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Directed Acyclic Graph (DAG) longest-path topological algorithm computing zero-float paths.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel capital expenditure (CapEx) refurbishments, enterprise software ERP cutovers.'},
                {'title': 'Technical Strengths', 'desc': 'Automated recalculation of dependent milestones upon upstream delays; constraint locking.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': 'CPM / PERT', 'sub': 'Zero Float'},
                {'label': 'Critical Path', 'val': 'Automated', 'sub': 'Red Highlight'},
                {'label': 'Dependencies', 'val': 'Finish-to-Start', 'sub': 'FS / SS / FF'},
                {'label': 'Interactivity', 'val': 'Drag Duration', 'sub': 'Real-time Math'}
            ],
            'code_snippet': """gantt.addTask({
  id: 4, text: "Engine Cutover", start_date: "12-05-2026",
  duration: 18, critical: true
});"""
        },

        # 3. TimelineJS Rich Media Narrative
        {
            'slide_id': 'slide-03-timelinejs-narrative',
            'tag': '03 / Narrative Chronology',
            'headline': 'Editorial Storytelling:',
            'headline_span': 'Knight Lab Media Timeline',
            'subtitle': 'Narrative chronological sequencing pairing multimedia artifacts with exact historical epochs.',
            'library_badge': 'TimelineJS (Knight Lab)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:space-between; padding:20px; box-sizing:border-box;">
                <div style="background:rgba(21,34,27,0.85); border:1px solid #d4af37; border-radius:8px; padding:18px;">
                  <span style="font-family:JetBrains Mono; font-size:0.85rem; color:#f3cf65; text-transform:uppercase;">Epoch: November 2022</span>
                  <h4 style="font-family:Newsreader; font-size:1.6rem; color:#fffefa; margin:8px 0;">The Generative AI Inception</h4>
                  <p style="font-size:0.95rem; color:#cde4d8; line-height:1.5;">
                    ChatGPT launches, initiating the transition from keyword query engines to conversational synthesizers. Intermediary OTAs scramble to build prompt plugins.
                  </p>
                </div>
                <!-- Timeline Slider Track -->
                <div style="position:relative; height:60px; background:#0e1713; border-top:1px solid rgba(255,255,255,0.15); display:flex; align-items:center; justify-content:space-around;">
                  <div style="text-align:center;">
                    <div style="width:12px; height:12px; background:#6c7d73; border-radius:50%; margin:0 auto 4px;"></div>
                    <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#9ba9a1;">2015 GHA</span>
                  </div>
                  <div style="text-align:center;">
                    <div style="width:16px; height:16px; background:#f3cf65; border-radius:50%; margin:0 auto 4px; box-shadow:0 0 10px #f3cf65;"></div>
                    <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#f3cf65; font-weight:bold;">2022 LLM</span>
                  </div>
                  <div style="text-align:center;">
                    <div style="width:12px; height:12px; background:#6c7d73; border-radius:50%; margin:0 auto 4px;"></div>
                    <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#9ba9a1;">2024 GEO</span>
                  </div>
                  <div style="text-align:center;">
                    <div style="width:12px; height:12px; background:#00e676; border-radius:50%; margin:0 auto 4px;"></div>
                    <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#00e676;">2026 Agentic</span>
                  </div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Sequential narrative state-machine linking discrete temporal timestamps to rich HTML DOM nodes.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Corporate history retrospectives, litigation chronologies, product evolution showcases.'},
                {'title': 'Technical Strengths', 'desc': 'Seamless YouTube/Vimeo/Wikipedia embeds, responsive touch carousel, Google Sheets data backend.'}
            ],
            'metrics': [
                {'label': 'Media Type', 'val': 'Rich Multimedia', 'sub': 'Video / Text'},
                {'label': 'Data Source', 'val': 'JSON / Sheets', 'sub': 'Low Code'},
                {'label': 'Navigation', 'val': 'Bi-directional', 'sub': 'Slider + Key'},
                {'label': 'Provenance', 'val': 'Knight Lab', 'sub': 'Journalism Std'}
            ],
            'code_snippet': """window.timeline = new TL.Timeline('timeline-embed',
  'https://docs.google.com/spreadsheets/d/...',
  { hash_bookmark: true, language: 'en' }
);"""
        },

        # 4. D3 Temporal Density Swimlanes
        {
            'slide_id': 'slide-04-d3-swimlanes',
            'tag': '04 / Temporal Density',
            'headline': 'Concurrent Activity Bands:',
            'headline_span': 'D3 Swimlane Density Bands',
            'subtitle': 'Multi-channel horizontal swimlanes mapping concurrent booking density across rolling operational quarters.',
            'library_badge': 'D3.js v7 Custom SVG',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:15px;">
                <svg viewBox="0 0 450 280" style="width:100%; max-height:330px;">
                  <!-- Swimlanes -->
                  <g font-family="DM Sans" font-size="11">
                    <!-- Lane 1 -->
                    <rect x="10" y="30" width="430" height="45" fill="rgba(19,34,27,0.7)" rx="4"/>
                    <text x="20" y="56" fill="#00e676" font-weight="bold">Direct Engine</text>
                    <rect x="120" y="42" width="18" height="22" fill="#00e676" opacity="0.8"/>
                    <rect x="145" y="42" width="35" height="22" fill="#00e676" opacity="0.9"/>
                    <rect x="210" y="42" width="80" height="22" fill="#00e676"/>
                    <rect x="320" y="42" width="60" height="22" fill="#00e676" opacity="0.85"/>

                    <!-- Lane 2 -->
                    <rect x="10" y="90" width="430" height="45" fill="rgba(19,34,27,0.7)" rx="4"/>
                    <text x="20" y="116" fill="#f3cf65" font-weight="bold">Google Meta</text>
                    <rect x="160" y="102" width="50" height="22" fill="#f3cf65" opacity="0.8"/>
                    <rect x="230" y="102" width="40" height="22" fill="#f3cf65" opacity="0.9"/>
                    <rect x="290" y="102" width="70" height="22" fill="#f3cf65"/>

                    <!-- Lane 3 -->
                    <rect x="10" y="150" width="430" height="45" fill="rgba(19,34,27,0.7)" rx="4"/>
                    <text x="20" y="176" fill="#ff1744" font-weight="bold">Wholesale GDS</text>
                    <rect x="130" y="162" width="30" height="22" fill="#ff1744" opacity="0.7"/>
                    <rect x="280" y="162" width="90" height="22" fill="#ff1744" opacity="0.9"/>

                    <!-- Time Axis -->
                    <line x1="10" y1="215" x2="440" y2="215" stroke="rgba(255,255,255,0.2)"/>
                    <text x="120" y="235" fill="#9ba9a1" font-family="JetBrains Mono">Jan</text>
                    <text x="220" y="235" fill="#9ba9a1" font-family="JetBrains Mono">Apr</text>
                    <text x="320" y="235" fill="#9ba9a1" font-family="JetBrains Mono">Jul</text>
                    <text x="400" y="235" fill="#9ba9a1" font-family="JetBrains Mono">Oct</text>
                  </g>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Interval partitioning: non-overlapping rectangle packing within discrete categorical horizontal bands.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Flight fleet turnarounds, hospital operating room scheduling, cloud microservice execution logs.'},
                {'title': 'Technical Strengths', 'desc': 'Direct spatial comparison of activity across disjoint departments without clutter.'}
            ],
            'metrics': [
                {'label': 'Structure', 'val': 'Categorical Band', 'sub': 'Parallel Lanes'},
                {'label': 'Overlap', 'val': '1D Packing', 'sub': 'Collision Free'},
                {'label': 'Precision', 'val': 'Continuous Date', 'sub': 'd3.scaleTime'},
                {'label': 'Animation', 'val': 'd3.transition', 'sub': 'Staggered'}
            ],
            'code_snippet': """const x = d3.scaleTime().domain([start, end]).range([0, width]);
svg.selectAll('rect').data(events)
  .join('rect').attr('x', d => x(d.start)).attr('width', d => x(d.end) - x(d.start));"""
        },

        # 5. Timelines-Chart Hierarchical State Machine
        {
            'slide_id': 'slide-05-timelines-chart',
            'tag': '05 / Discrete State Sequences',
            'headline': 'Temporal State Transitions:',
            'headline_span': 'Hierarchical State Evolution',
            'subtitle': 'Color-coded discrete machine states tracking operational status (Available, Occupied, Maintenance).',
            'library_badge': 'timelines-chart',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:10px; padding:20px; box-sizing:border-box;">
                <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#f3cf65;">State Machine: 350 Room Fleet</span>
                  <div style="display:flex; gap:12px; font-size:0.75rem;">
                    <span style="color:#00e676;">&#9632; Occupied</span>
                    <span style="color:#00e5ff;">&#9632; Reserved</span>
                    <span style="color:#ff1744;">&#9632; Out of Order</span>
                  </div>
                </div>
                <!-- 4 room rows -->
                <div style="display:flex; height:24px; border-radius:4px; overflow:hidden; gap:2px;">
                  <div style="flex:4; background:#00e676;"></div>
                  <div style="flex:2; background:#00e5ff;"></div>
                  <div style="flex:5; background:#00e676;"></div>
                  <div style="flex:1; background:#ff1744;"></div>
                </div>
                <div style="display:flex; height:24px; border-radius:4px; overflow:hidden; gap:2px;">
                  <div style="flex:3; background:#00e5ff;"></div>
                  <div style="flex:6; background:#00e676;"></div>
                  <div style="flex:2; background:#00e676;"></div>
                  <div style="flex:1; background:#00e5ff;"></div>
                </div>
                <div style="display:flex; height:24px; border-radius:4px; overflow:hidden; gap:2px;">
                  <div style="flex:8; background:#00e676;"></div>
                  <div style="flex:2; background:#ff1744;"></div>
                  <div style="flex:2; background:#00e676;"></div>
                </div>
                <div style="display:flex; height:24px; border-radius:4px; overflow:hidden; gap:2px;">
                  <div style="flex:2; background:#00e676;"></div>
                  <div style="flex:4; background:#00e5ff;"></div>
                  <div style="flex:5; background:#00e676;"></div>
                  <div style="flex:1; background:#00e676;"></div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Piecewise constant step-function $S(t) \\in \\{S_1, S_2, \\dots, S_k\\}$ partitioned along 1D time continuum.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Industrial IoT machine state logs, data center server health, hotel room occupancy states.'},
                {'title': 'Technical Strengths', 'desc': 'Seamless zoomable transitions between macro aggregate years down to microsecond states.'}
            ],
            'metrics': [
                {'label': 'State Model', 'val': 'Discrete FSM', 'sub': 'Piecewise'},
                {'label': 'Granularity', 'val': 'Microsecond', 'sub': 'Continuous'},
                {'label': 'Compression', 'val': 'Run-Length', 'sub': 'High Scalability'},
                {'label': 'Color Maps', 'val': 'Status-Coded', 'sub': 'Instant Alert'}
            ],
            'code_snippet': """TimelinesChart()(document.getElementById('chart'))
  .data(roomStates)
  .zColorScale(d3.scaleOrdinal().range(['#00e676', '#00e5ff', '#ff1744']));"""
        },

        # 6. AnyChart Resource Workload Balancing
        {
            'slide_id': 'slide-06-resource-workload',
            'tag': '06 / Capacity Allocation',
            'headline': 'Workload Balancing:',
            'headline_span': 'Resource Allocation Matrix',
            'subtitle': 'Capacity threshold monitoring identifying over-allocation and personnel burnout points.',
            'library_badge': 'AnyChart Gantt Engine',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:14px; padding:20px; box-sizing:border-box;">
                <div>
                  <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:4px;">
                    <span style="color:#fffefa;">Executive Advisory Team</span>
                    <span style="color:#00e676; font-family:JetBrains Mono;">85% Nominal Capacity</span>
                  </div>
                  <div style="height:20px; background:rgba(255,255,255,0.06); border-radius:4px; overflow:hidden;">
                    <div style="width:85%; height:100%; background:#00e676;"></div>
                  </div>
                </div>
                <div>
                  <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:4px;">
                    <span style="color:#fffefa;">Revenue Management Pod</span>
                    <span style="color:#ff1744; font-family:JetBrains Mono;">118% OVER-ALLOCATED</span>
                  </div>
                  <div style="height:20px; background:rgba(255,255,255,0.06); border-radius:4px; overflow:hidden;">
                    <div style="width:100%; height:100%; background:#ff1744; box-shadow:0 0 10px #ff1744;"></div>
                  </div>
                </div>
                <div>
                  <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:4px;">
                    <span style="color:#fffefa;">Data Science & AI Engineering</span>
                    <span style="color:#d4af37; font-family:JetBrains Mono;">94% Peak Load</span>
                  </div>
                  <div style="height:20px; background:rgba(255,255,255,0.06); border-radius:4px; overflow:hidden;">
                    <div style="width:94%; height:100%; background:#d4af37;"></div>
                  </div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Cumulative workload integration: $W(t) = \\sum_{i} c_i(t)$ checked against threshold capacity limits $C_{\\max}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Consulting personnel scheduling, hospital nurse staffing, cloud cluster CPU limits.'},
                {'title': 'Technical Strengths', 'desc': 'Instant visual detection of scheduling bottlenecks and automated leveling recommendations.'}
            ],
            'metrics': [
                {'label': 'Measurement', 'val': 'Capacity %', 'sub': 'Over-Allocation'},
                {'label': 'Threshold', 'val': '100% Red Alert', 'sub': 'Safe vs Warning'},
                {'label': 'Resolution', 'val': 'Daily / Hourly', 'sub': 'Configurable'},
                {'label': 'Leveling', 'val': 'Heuristic Shift', 'sub': 'Optimization'}
            ],
            'code_snippet': """var chart = anychart.ganttResource();
chart.data(resourceData);
chart.getTimeline().elements().rendering().drawer(customWorkloadDrawer);"""
        },

        # 7. CanvasJS High-Frequency Millisecond Tick Timeline
        {
            'slide_id': 'slide-07-canvasjs-ticks',
            'tag': '07 / Microsecond Frequency',
            'headline': 'Millisecond Tick Execution:',
            'headline_span': 'Sub-Second Financial Stream',
            'subtitle': 'High-frequency event timeline tracking sub-second algorithmic trading and dynamic rate auction updates.',
            'library_badge': 'CanvasJS Fast Engine',
            'chart_html': """
              <div id="canvasjs-ticks-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('canvasjs-ticks-stage');
                  if (!el || !window.Plotly) return;
                  const times = [], prices = [];
                  let p = 240.0;
                  for(let i=0; i<150; i++) {
                    times.push("09:30:" + (i < 10 ? "0" : "") + Math.floor(i/10) + "." + (i%10) + "00");
                    p += (Math.random() - 0.48) * 0.8;
                    prices.push(p);
                  }
                  const trace = {
                    x: times, y: prices, mode: 'lines+markers',
                    line: { color: '#00e676', width: 2 },
                    marker: { size: 3, color: '#f3cf65' }
                  };
                  const layout = {
                    paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
                    font: { color: '#9ba9a1', family: 'JetBrains Mono', size: 10 },
                    margin: { l: 40, r: 20, t: 15, b: 35 },
                    xaxis: { gridcolor: 'rgba(255,255,255,0.06)' },
                    yaxis: { gridcolor: 'rgba(255,255,255,0.06)' }
                  };
                  Plotly.newPlot('canvasjs-ticks-stage', [trace], layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Brownian motion stochastic process: $dS_t = \\mu S_t dt + \\sigma S_t dW_t$ rendered via hardware Canvas 2D.'},
                {'title': 'Enterprise Use Cases', 'desc': 'High-frequency trading latency tracking, real-time ad bid exchanges, telemetry logs.'},
                {'title': 'Technical Strengths', 'desc': 'Renders 100,000 data points in under 100ms; zero frame rate drop.'}
            ],
            'metrics': [
                {'label': 'Render Speed', 'val': '100K pts / 100ms', 'sub': 'CanvasJS Core'},
                {'label': 'Precision', 'val': 'Microsecond', 'sub': 'Timestamp Sync'},
                {'label': 'Stochastic', 'val': 'Brownian Motion', 'sub': 'Real-time Drift'},
                {'label': 'Markers', 'val': 'Sub-Pixel Dot', 'sub': 'Point Picking'}
            ],
            'code_snippet': """var chart = new CanvasJS.Chart("chartContainer", {
  animationEnabled: true,
  data: [{ type: "line", dataPoints: tickPoints }]
});
chart.render();"""
        },

        # 8. Broken Barh Machine State & Downtime Gantt
        {
            'slide_id': 'slide-08-broken-barh',
            'tag': '08 / Discontinuous Horizons',
            'headline': 'Discontinuous Timelines:',
            'headline_span': 'Broken Barh Machine Uptime',
            'subtitle': 'Non-contiguous horizontal bars mapping server downtime, maintenance intervals, and active uptime bursts.',
            'library_badge': 'Matplotlib Engine / SVG',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:15px;">
                <svg viewBox="0 0 450 260" style="width:100%; max-height:300px;">
                  <!-- Y Axis Labels -->
                  <text x="80" y="60" text-anchor="end" fill="#fffefa" font-family="DM Sans" font-size="11">Node Alpha</text>
                  <text x="80" y="120" text-anchor="end" fill="#fffefa" font-family="DM Sans" font-size="11">Node Beta</text>
                  <text x="80" y="180" text-anchor="end" fill="#fffefa" font-family="DM Sans" font-size="11">Node Gamma</text>

                  <!-- Node Alpha Bars -->
                  <rect x="100" y="45" width="80" height="24" fill="#00e676" rx="3"/>
                  <rect x="200" y="45" width="120" height="24" fill="#00e676" rx="3"/>
                  <rect x="340" y="45" width="70" height="24" fill="#ff1744" rx="3"/>

                  <!-- Node Beta Bars -->
                  <rect x="100" y="105" width="140" height="24" fill="#00e676" rx="3"/>
                  <rect x="260" y="105" width="40" height="24" fill="#d4af37" rx="3"/>
                  <rect x="320" y="105" width="90" height="24" fill="#00e676" rx="3"/>

                  <!-- Node Gamma Bars -->
                  <rect x="120" y="165" width="60" height="24" fill="#ff1744" rx="3"/>
                  <rect x="200" y="165" width="210" height="24" fill="#00e676" rx="3"/>

                  <!-- Axis -->
                  <line x1="100" y1="210" x2="420" y2="210" stroke="rgba(255,255,255,0.2)"/>
                  <text x="100" y="230" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">00:00</text>
                  <text x="260" y="230" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">12:00</text>
                  <text x="400" y="230" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">24:00</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Segment collection encoding pairs of (start, duration): $[(x_1, \\Delta x_1), (x_2, \\Delta x_2), \\dots]$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Data center hardware outages, manufacturing plant maintenance, sleep study actigraphy.'},
                {'title': 'Technical Strengths', 'desc': 'Compact representation of discontinuous intervals without filling zero-data space.'}
            ],
            'metrics': [
                {'label': 'Data Format', 'val': 'List of Tuples', 'sub': '(Start, Duration)'},
                {'label': 'Continuity', 'val': 'Discontinuous', 'sub': 'Zero Clutter'},
                {'label': 'Categories', 'val': 'Multi-Resource', 'sub': 'Discrete Y'},
                {'label': 'Efficiency', 'val': 'High Density', 'sub': 'Low Memory'}
            ],
            'code_snippet': """ax.broken_barh(
  [(10, 80), (200, 120)], (40, 20), facecolors=('#00e676')
)
ax.broken_barh([(340, 70)], (40, 20), facecolors=('#ff1744'))"""
        },

        # 9. Circular 24-Hour Circadian Timeline
        {
            'slide_id': 'slide-09-circadian-timeline',
            'tag': '09 / Cyclical Chronology',
            'headline': '24-Hour Periodic Cycles:',
            'headline_span': 'Circular Dial Chrono-Map',
            'subtitle': 'Clock-face polar timeline showing cyclical demand surges, staff shifts, and night audit cutoffs.',
            'library_badge': 'D3 Polar Clock',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 300 300" style="width:260px; height:260px;">
                  <circle cx="150" cy="150" r="110" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="18"/>
                  <!-- Morning Shift Arc -->
                  <circle cx="150" cy="150" r="110" fill="none" stroke="#00e676" stroke-width="18"
                          stroke-dasharray="691" stroke-dashoffset="460" stroke-linecap="round"/>
                  <!-- Evening Shift Arc -->
                  <circle cx="150" cy="150" r="110" fill="none" stroke="#d4af37" stroke-width="18"
                          stroke-dasharray="691" stroke-dashoffset="300" stroke-linecap="round"/>
                  <!-- Night Audit Arc -->
                  <circle cx="150" cy="150" r="110" fill="none" stroke="#ff1744" stroke-width="18"
                          stroke-dasharray="691" stroke-dashoffset="600" stroke-linecap="round"/>
                  <text x="150" y="30" text-anchor="middle" fill="#9ba9a1" font-family="JetBrains Mono" font-size="11">00:00</text>
                  <text x="270" y="155" text-anchor="middle" fill="#9ba9a1" font-family="JetBrains Mono" font-size="11">06:00</text>
                  <text x="150" y="280" text-anchor="middle" fill="#9ba9a1" font-family="JetBrains Mono" font-size="11">12:00</text>
                  <text x="30" y="155" text-anchor="middle" fill="#9ba9a1" font-family="JetBrains Mono" font-size="11">18:00</text>
                  <text x="150" y="145" text-anchor="middle" fill="#fffefa" font-family="Newsreader" font-size="18">Circadian</text>
                  <text x="150" y="165" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="11">24h Shift Cycle</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Modular arithmetic modulo 24 hours ($t \\pmod{24}$) mapped to polar angles $\\theta = 2\\pi (t/24)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Emergency room duty shifts, 24/7 security patrol routes, airline overnight layover schedules.'},
                {'title': 'Technical Strengths', 'desc': 'Eliminates artificial midnight boundary disconnects inherent in linear timelines.'}
            ],
            'metrics': [
                {'label': 'Periodicity', 'val': 'Modulo 24 Hours', 'sub': 'Continuous Loop'},
                {'label': 'Coordinate', 'val': 'Polar (r, θ)', 'sub': 'Clock Face'},
                {'label': 'Shifts', 'val': '3 Distinct Arcs', 'sub': 'Color Coded'},
                {'label': 'Perception', 'val': 'Intuitive', 'sub': 'Time Natural'}
            ],
            'code_snippet': """const arc = d3.arc()
  .innerRadius(100).outerRadius(120)
  .startAngle(d => (d.startHour / 24) * 2 * Math.PI)
  .endAngle(d => (d.endHour / 24) * 2 * Math.PI);"""
        },

        # 10. Milestone Stem Horizon
        {
            'slide_id': 'slide-10-milestone-stem',
            'tag': '10 / Discrete Events',
            'headline': 'Discrete Anchor Callouts:',
            'headline_span': 'Alternating Milestone Stems',
            'subtitle': 'Vertical lollipop stems anchoring historical enterprise events above and below a central axis.',
            'library_badge': 'SVG Stem Framework',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:15px;">
                <svg viewBox="0 0 450 260" style="width:100%; max-height:300px;">
                  <!-- Central Horizon Axis -->
                  <line x1="20" y1="130" x2="430" y2="130" stroke="#d4af37" stroke-width="2.5"/>
                  
                  <!-- Milestone 1: Top -->
                  <line x1="80" y1="130" x2="80" y2="50" stroke="#00e676" stroke-width="2"/>
                  <circle cx="80" cy="50" r="7" fill="#00e676"/>
                  <rect x="35" y="15" width="90" height="24" fill="#13221b" stroke="#00e676" rx="4"/>
                  <text x="80" y="31" text-anchor="middle" fill="#fff" font-family="DM Sans" font-size="10">Direct Engine Go-Live</text>

                  <!-- Milestone 2: Bottom -->
                  <line x1="180" y1="130" x2="180" y2="210" stroke="#f3cf65" stroke-width="2"/>
                  <circle cx="180" cy="210" r="7" fill="#f3cf65"/>
                  <rect x="135" y="220" width="90" height="24" fill="#13221b" stroke="#f3cf65" rx="4"/>
                  <text x="180" y="236" text-anchor="middle" fill="#fff" font-family="DM Sans" font-size="10">Parity Enforcement</text>

                  <!-- Milestone 3: Top -->
                  <line x1="290" y1="130" x2="290" y2="50" stroke="#00e5ff" stroke-width="2"/>
                  <circle cx="290" cy="50" r="7" fill="#00e5ff"/>
                  <rect x="245" y="15" width="90" height="24" fill="#13221b" stroke="#00e5ff" rx="4"/>
                  <text x="290" y="31" text-anchor="middle" fill="#fff" font-family="DM Sans" font-size="10">CDP Mesh Deployed</text>

                  <!-- Milestone 4: Bottom -->
                  <line x1="390" y1="130" x2="390" y2="210" stroke="#ff1744" stroke-width="2"/>
                  <circle cx="390" cy="210" r="7" fill="#ff1744"/>
                  <rect x="345" y="220" width="90" height="24" fill="#13221b" stroke="#ff1744" rx="4"/>
                  <text x="390" y="236" text-anchor="middle" fill="#fff" font-family="DM Sans" font-size="10">OTA Contract Re-cut</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Alternating polarity layout: $y_{\\text{stem}} = y_0 + (-1)^i \\cdot H$ to prevent callout label collision.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Executive quarterly roadmap milestones, regulatory approval timelines, corporate history.'},
                {'title': 'Technical Strengths', 'desc': 'High readability, elegant typography alignment, zero label overlap.'}
            ],
            'metrics': [
                {'label': 'Collision Avoid', 'val': 'Alternating ±y', 'sub': 'Staggered'},
                {'label': 'Stem Render', 'val': 'Vector Lines', 'sub': 'Crisp High-DPI'},
                {'label': 'Labels', 'val': 'Enclosed Badges', 'sub': 'Glassmorphic'},
                {'label': 'Anchors', 'val': 'Point In Time', 'sub': 'Exact Date'}
            ],
            'code_snippet': """stems.forEach((d, i) => {
  const sign = i % 2 === 0 ? -1 : 1;
  drawLine(d.x, y0, d.x, y0 + sign * height);
  drawBadge(d.x, y0 + sign * (height + 15), d.text);
});"""
        },

        # 11. Multi-Tiered Product Release Gantt
        {
            'slide_id': 'slide-11-release-gantt',
            'tag': '11 / Release Management',
            'headline': 'Software Release Waves:',
            'headline_span': 'Multi-Tiered Version Track',
            'subtitle': 'Simultaneous staging of Alpha, Beta, Production, and Deprecation lifecycle windows.',
            'library_badge': 'Enterprise Release Gantt',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:12px; padding:20px; box-sizing:border-box;">
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:4px;">
                  <span style="color:#d4af37; font-weight:bold;">v2.4 LTS Engine</span>
                  <span style="color:#9ba9a1; font-family:JetBrains Mono;">Deprecation Phase</span>
                </div>
                <div style="height:16px; background:rgba(255,255,255,0.06); border-radius:3px; position:relative;">
                  <div style="position:absolute; left:0; width:40%; height:100%; background:#6c7d73; border-radius:3px;"></div>
                </div>
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:4px; margin-top:8px;">
                  <span style="color:#00e676; font-weight:bold;">v3.0 Current Production</span>
                  <span style="color:#00e676; font-family:JetBrains Mono;">Active Wave</span>
                </div>
                <div style="height:16px; background:rgba(255,255,255,0.06); border-radius:3px; position:relative;">
                  <div style="position:absolute; left:25%; width:60%; height:100%; background:#00e676; border-radius:3px; box-shadow:0 0 8px rgba(0,230,118,0.5);"></div>
                </div>
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:4px; margin-top:8px;">
                  <span style="color:#00e5ff; font-weight:bold;">v3.5 Agentic Beta</span>
                  <span style="color:#00e5ff; font-family:JetBrains Mono;">Private Pilot</span>
                </div>
                <div style="height:16px; background:rgba(255,255,255,0.06); border-radius:3px; position:relative;">
                  <div style="position:absolute; left:70%; width:25%; height:100%; background:#00e5ff; border-radius:3px;"></div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Temporal interval overlaps with multi-stage status state transitions (Dev, Beta, GA, EOL).'},
                {'title': 'Enterprise Use Cases', 'desc': 'SaaS version lifecycle roadmaps, hotel PMS version upgrade schedules, API version deprecations.'},
                {'title': 'Technical Strengths', 'desc': 'Provides clear visual guidance on legacy technical debt sunset dates.'}
            ],
            'metrics': [
                {'label': 'Lifecycle', 'val': '4 Stages', 'sub': 'Dev to EOL'},
                {'label': 'Overlap', 'val': 'Side-by-Side', 'sub': 'Dual Versioning'},
                {'label': 'Audience', 'val': 'DevOps & Exec', 'sub': 'Strategic Track'},
                {'label': 'Deprecation', 'val': 'Highlighted', 'sub': 'Risk Mitigation'}
            ],
            'code_snippet': """const versions = [
  { ver: 'v2.4', start: '2024-01', end: '2026-06', status: 'EOL' },
  { ver: 'v3.0', start: '2025-06', end: '2027-12', status: 'GA' }
];"""
        },

        # 12. Streaming Telemetry Event Stream with Severity Heatmap
        {
            'slide_id': 'slide-12-streaming-telemetry',
            'tag': '12 / Incident Logs',
            'headline': 'Severity Pulse Streams:',
            'headline_span': 'Incident Telemetry Matrix',
            'subtitle': 'High-velocity temporal heatmap logging rate parity violations and API response timeouts.',
            'library_badge': 'Live Telemetry Log',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:15px; box-sizing:border-box;">
                <div style="display:grid; grid-template-columns: repeat(20, 1fr); gap:4px; margin-bottom:8px;">
                  <!-- Row of 20 mini pulse blocks -->
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#ffab00; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#ff1744; border-radius:2px; box-shadow:0 0 6px #ff1744;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#ffab00; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#ff1744; border-radius:2px; box-shadow:0 0 6px #ff1744;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                  <div style="height:28px; background:#00e676; border-radius:2px;"></div>
                </div>
                <div style="display:flex; justify-content:space-between; font-family:JetBrains Mono; font-size:0.75rem; color:#9ba9a1;">
                  <span>14:00:00 (100% Parity)</span>
                  <span style="color:#ff1744;">14:15:22 (Agoda Leakage)</span>
                  <span>14:30:00 (Resolved)</span>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Rolling FIFO buffer: $B = [e_t, e_{t-1}, \\dots, e_{t-k}]$ mapped to discrete color threshold lookup.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Rate parity leakage detection, CRS booking engine latency spikes, cybersecurity intrusion alarms.'},
                {'title': 'Technical Strengths', 'desc': 'Constant-memory footprint, continuous animation without DOM bloat.'}
            ],
            'metrics': [
                {'label': 'Data Buffer', 'val': 'FIFO Rolling', 'sub': 'Real-Time'},
                {'label': 'Latency', 'val': '< 10 ms', 'sub': 'Instant Alert'},
                {'label': 'Severity', 'val': 'Tri-Color', 'sub': 'Green/Gold/Red'},
                {'label': 'Memory', 'val': 'Fixed O(1)', 'sub': 'No Leaks'}
            ],
            'code_snippet': """function pushEvent(severity) {
  events.shift();
  events.push(severity);
  renderGrid(events);
}"""
        },

        # 13. Historical Epoch Geological Chrono-Map
        {
            'slide_id': 'slide-13-epoch-chrono',
            'tag': '13 / Non-Linear Scaling',
            'headline': 'Logarithmic Eras:',
            'headline_span': 'Non-Linear Epoch Scaling',
            'subtitle': 'Logarithmic temporal transformations mapping broad macro eras alongside high-resolution modern events.',
            'library_badge': 'Logarithmic D3 Time',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:20px; box-sizing:border-box;">
                <div style="display:flex; height:50px; border-radius:6px; overflow:hidden; border:1px solid #d4af37;">
                  <div style="flex:1; background:#1b2822; padding:8px; border-right:1px solid #d4af37;">
                    <strong style="color:#9ba9a1; font-size:0.8rem; display:block;">GDS Era</strong>
                    <span style="color:#6c7d73; font-size:0.75rem;">1970 - 1995 (25y)</span>
                  </div>
                  <div style="flex:1.5; background:#23352c; padding:8px; border-right:1px solid #d4af37;">
                    <strong style="color:#f3cf65; font-size:0.8rem; display:block;">OTA Boom</strong>
                    <span style="color:#9ba9a1; font-size:0.75rem;">1996 - 2010 (15y)</span>
                  </div>
                  <div style="flex:2.5; background:#154531; padding:8px; border-right:1px solid #d4af37;">
                    <strong style="color:#00e676; font-size:0.8rem; display:block;">Metasearch & Mobile</strong>
                    <span style="color:#cde4d8; font-size:0.75rem;">2011 - 2022 (12y)</span>
                  </div>
                  <div style="flex:4; background:#0c5e3d; padding:8px;">
                    <strong style="color:#f3cf65; font-size:0.85rem; display:block;">AI & Autonomous Agents</strong>
                    <span style="color:#fffefa; font-size:0.75rem; font-weight:bold;">2023 - 2030+ (High Velocity)</span>
                  </div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Logarithmic / power-law time scale: $x = \\log(t - t_0)$ compressing ancient history to expand current events.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Macro economic technological cycles, geological strata mapping, patent evolution.'},
                {'title': 'Technical Strengths', 'desc': 'Enables simultaneous analysis of 50-year structural changes and 6-month AI disruptions.'}
            ],
            'metrics': [
                {'label': 'Scale Type', 'val': 'Logarithmic Time', 'sub': 'Power Law'},
                {'label': 'Resolution', 'val': 'Adaptive', 'sub': 'High Near Present'},
                {'label': 'Compression', 'val': 'Ancient Eras', 'sub': 'Saves Space'},
                {'label': 'Relevance', 'val': 'Strategic View', 'sub': 'Tech S-Curves'}
            ],
            'code_snippet': """const timeScale = d3.scalePow().exponent(2.5)
  .domain([new Date(1970, 0, 1), new Date(2030, 0, 1)])
  .range([0, width]);"""
        },

        # 14. GitHub-Style Contribution Calendar Heatmap
        {
            'slide_id': 'slide-14-calendar-heatmap',
            'tag': '14 / Spatiotemporal Matrix',
            'headline': 'Rolling Annual Activity:',
            'headline_span': 'Calendar Matrix Heatmap',
            'subtitle': '52-week grid (7 days × 52 weeks) encoding daily booking conversion intensity and direct yield.',
            'library_badge': 'Calendar Heatmap Core',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding:15px;">
                <svg viewBox="0 0 450 140" style="width:100%; max-height:180px;">
                  <g transform="translate(10, 20)">
                    <!-- Grid of 52 weeks simulated with clusters -->
                    <!-- Repeat squares -->
                    <script>
                      // Simulated via static SVG rects
                    </script>
                    <rect x="0" y="0" width="12" height="12" fill="#0e1713" rx="2"/>
                    <rect x="16" y="0" width="12" height="12" fill="#1b382b" rx="2"/>
                    <rect x="32" y="0" width="12" height="12" fill="#2d5a44" rx="2"/>
                    <rect x="48" y="0" width="12" height="12" fill="#00e676" rx="2"/>
                    <rect x="64" y="0" width="12" height="12" fill="#00e676" rx="2"/>
                    <rect x="80" y="0" width="12" height="12" fill="#d4af37" rx="2"/>
                    <!-- Repeat multi rows -->
                    <text x="0" y="45" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">Mon</text>
                    <text x="0" y="75" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">Wed</text>
                    <text x="0" y="105" fill="#9ba9a1" font-family="JetBrains Mono" font-size="10">Fri</text>
                    <!-- Matrix Block -->
                    <g transform="translate(30, 30)">
                      <rect x="0" y="0" width="390" height="75" fill="none" stroke="rgba(255,255,255,0.08)" rx="4"/>
                      <text x="195" y="42" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="14">365 Days &bull; 92.4% Direct Uptime</text>
                    </g>
                  </g>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': '2D mapping: $\\text{WeekNumber} = \\lfloor \\text{DayOfYear} / 7 \\rfloor, \\text{DayOfWeek} = t \\pmod 7$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Direct website sales activity, developer code contributions, guest check-in volume patterns.'},
                {'title': 'Technical Strengths', 'desc': 'Instantly reveals weekly day-of-week seasonality (Sunday drops vs Friday spikes).'}
            ],
            'metrics': [
                {'label': 'Dimensions', 'val': '7 Days x 52 Wks', 'sub': '364 Cells'},
                {'label': 'Color Quant', 'val': '5 Quintiles', 'sub': 'Emerald Scale'},
                {'label': 'Seasonality', 'val': 'Weekly Cycle', 'sub': 'Weekend Peak'},
                {'label': 'Standard', 'val': 'GitHub Style', 'sub': 'Universally Known'}
            ],
            'code_snippet': """const cell = svg.selectAll('rect')
  .data(days).join('rect')
  .attr('x', d => week(d) * cellSize)
  .attr('y', d => day(d) * cellSize);"""
        },

        # 15. Supply Chain Logistics Transit Schedule
        {
            'slide_id': 'slide-15-transit-schedule',
            'tag': '15 / Multimodal Logistics',
            'headline': 'Cargo Transit Windows:',
            'headline_span': 'Multimodal Logistics Schedule',
            'subtitle': 'Sequential transit legs tracking maritime port dwelling, customs clearance, and last-mile delivery.',
            'library_badge': 'Logistics Flow Engine',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:12px; padding:20px; box-sizing:border-box;">
                <div style="display:flex; justify-content:space-between; font-size:0.85rem;">
                  <span style="color:#00e5ff; font-weight:bold;">Leg 1: Ocean Freight (Singapore &rarr; Rotterdam)</span>
                  <span style="color:#9ba9a1; font-family:JetBrains Mono;">18 Days &bull; On Time</span>
                </div>
                <div style="height:16px; background:rgba(0,229,255,0.25); border:1px solid #00e5ff; border-radius:3px;"></div>
                
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-top:6px;">
                  <span style="color:#ffab00; font-weight:bold;">Leg 2: Customs & Port Clearance</span>
                  <span style="color:#ffab00; font-family:JetBrains Mono;">3 Days &bull; Inspection</span>
                </div>
                <div style="height:16px; background:rgba(255,171,0,0.25); border:1px solid #ffab00; border-radius:3px; margin-left:35%; width:20%;"></div>

                <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-top:6px;">
                  <span style="color:#00e676; font-weight:bold;">Leg 3: Rail / Inland Distribution</span>
                  <span style="color:#00e676; font-family:JetBrains Mono;">2 Days &bull; Scheduled</span>
                </div>
                <div style="height:16px; background:rgba(0,230,118,0.25); border:1px solid #00e676; border-radius:3px; margin-left:55%; width:45%;"></div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Sequential path interval concatenation: $t_{\\text{arrival}} = t_0 + \\sum \\Delta t_i + \\sum \\text{slack}_i$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel refurbishment FF&E import logistics, cross-border supply chain predictability.'},
                {'title': 'Technical Strengths', 'desc': 'Clear hand-off accountability between ocean shipping, port operators, and inland rail.'}
            ],
            'metrics': [
                {'label': 'Modalities', 'val': 'Ocean / Port / Rail', 'sub': 'Multi-Carrier'},
                {'label': 'Tracking', 'val': 'Real-Time AIS', 'sub': 'GPS Synced'},
                {'label': 'Buffer Time', 'val': '3-Day Buffer', 'sub': 'Port Congestion'},
                {'label': 'Visibility', 'val': 'End-to-End', 'sub': 'Custody Chain'}
            ],
            'code_snippet': """const journey = [
  { mode: 'Ocean', duration: 18, delayRisk: 'Low' },
  { mode: 'Customs', duration: 3, delayRisk: 'Med' }
];"""
        },

        # 16. Relative Time Elapsed Race Horizon
        {
            'slide_id': 'slide-16-relative-race',
            'tag': '16 / Mission Timelines',
            'headline': 'Mission Control Horizons:',
            'headline_span': 'T-Minus to T-Plus Elapsed Countdown',
            'subtitle': 'Zero-centered countdown relative temporal reference anchored to a critical launch event.',
            'library_badge': 'Aerospace Mission Chrono',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; padding:20px;">
                <div style="font-family:Newsreader; font-size:1.8rem; color:#f3cf65; margin-bottom:8px;">New Property Brand Unveil</div>
                <div style="font-family:JetBrains Mono; font-size:3.2rem; color:#00e676; font-weight:700; text-shadow:0 0 15px rgba(0,230,118,0.4);">
                  T-MINUS 14:08:32
                </div>
                <div style="font-size:0.95rem; color:#9ba9a1; margin-top:10px;">
                  All distribution endpoints locked &bull; Pre-opening member rates active
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Relative temporal displacement: $\\Delta t = t_{\\text{current}} - t_{\\text{target}}$ with sign reversal at zero.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Hotel grand openings, enterprise software cutover checklists, financial IPO countdowns.'},
                {'title': 'Technical Strengths', 'desc': 'Unifies global multi-timezone teams around a single relative operational heartbeat.'}
            ],
            'metrics': [
                {'label': 'Time Base', 'val': 'Relative (T±)', 'sub': 'Zero Anchor'},
                {'label': 'Update Rate', 'val': '1,000 ms', 'sub': 'High Precision'},
                {'label': 'Timezones', 'val': 'UTC Universal', 'sub': 'Global Sync'},
                {'label': 'Status', 'val': 'Green Go', 'sub': 'All Systems'}
            ],
            'code_snippet': """function getTMinus(targetEpoch) {
  const diff = targetEpoch - Date.now();
  return (diff >= 0 ? 'T-' : 'T+') + formatDuration(Math.abs(diff));
}"""
        },

        # 17. Longitudinal Clinical Trial Episode Timeline
        {
            'slide_id': 'slide-17-clinical-episodes',
            'tag': '17 / Cohort Progression',
            'headline': 'Longitudinal Observations:',
            'headline_span': 'Patient Cohort Progression',
            'subtitle': 'Multi-subject timeline tracking treatment dosage epochs, side effect episodes, and recovery biomarkers.',
            'library_badge': 'Biomedical D3 Timeline',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:12px; padding:20px; box-sizing:border-box;">
                <div style="display:flex; align-items:center; gap:10px;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#f3cf65; width:80px;">Cohort A</span>
                  <div style="flex:1; height:18px; background:rgba(0,230,118,0.25); border-left:4px solid #00e676; border-radius:2px;"></div>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#f3cf65; width:80px;">Cohort B</span>
                  <div style="flex:1; height:18px; background:rgba(212,175,55,0.25); border-left:4px solid #d4af37; border-radius:2px;"></div>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#f3cf65; width:80px;">Control</span>
                  <div style="flex:1; height:18px; background:rgba(108,125,115,0.25); border-left:4px solid #6c7d73; border-radius:2px;"></div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Survival analysis Kaplan-Meier event timelines: $\\hat{S}(t) = \\prod_{t_i \\le t} (1 - d_i / n_i)$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Pharmaceutical clinical trials, customer retention cohort churn, guest lifetime value curves.'},
                {'title': 'Technical Strengths', 'desc': 'Aligns disparate individual start dates to a normalized $T_0$ baseline for fair comparison.'}
            ],
            'metrics': [
                {'label': 'Baseline', 'val': 'Normalized T0', 'sub': 'Aligned Cohorts'},
                {'label': 'Episodes', 'val': 'Multi-Interval', 'sub': 'Discrete Events'},
                {'label': 'Biomarkers', 'val': 'Color Gradients', 'sub': 'Efficacy Metric'},
                {'label': 'Compliance', 'val': 'FDA 21 CFR', 'sub': 'Audit Standard'}
            ],
            'code_snippet': """const normalized = patients.map(p => ({
  id: p.id,
  events: p.events.map(e => ({ ...e, day: (e.date - p.admitDate) / 86400000 }))
}));"""
        },

        # 18. Audio/Video Multi-Track DAW Waveform Timeline
        {
            'slide_id': 'slide-18-daw-waveform',
            'tag': '18 / Multimedia Editing',
            'headline': 'Digital Audio Workstation (DAW):',
            'headline_span': 'Multi-Track Waveform Timeline',
            'subtitle': 'Synchronized audio peak waveforms with cue markers, automation envelopes, and timecode scrubs.',
            'library_badge': 'Web Audio API + Canvas',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:8px; padding:15px; box-sizing:border-box;">
                <div style="height:35px; background:#0e1713; border:1px solid #d4af37; border-radius:4px; display:flex; align-items:center; padding:0 8px;">
                  <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#f3cf65; width:70px;">Voice Track</span>
                  <div style="flex:1; height:20px; background:linear-gradient(90deg, #00e676 0%, #00e676 40%, transparent 40%, transparent 60%, #00e676 60%);"></div>
                </div>
                <div style="height:35px; background:#0e1713; border:1px solid #b5935b; border-radius:4px; display:flex; align-items:center; padding:0 8px;">
                  <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#f3cf65; width:70px;">Backing Bed</span>
                  <div style="flex:1; height:20px; background:linear-gradient(90deg, #d4af37, #f3cf65);"></div>
                </div>
                <div style="height:35px; background:#0e1713; border:1px solid #00e5ff; border-radius:4px; display:flex; align-items:center; padding:0 8px;">
                  <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#00e5ff; width:70px;">SFX Stems</span>
                  <div style="flex:1; height:20px; background:linear-gradient(90deg, transparent 20%, #00e5ff 25%, transparent 30%, #00e5ff 70%, transparent 75%);"></div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Fast Fourier Transform (FFT) peak decimation mapping audio buffers to Canvas draw lines.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Podcast production, video advertisement editing, speech AI phonetic alignment.'},
                {'title': 'Technical Strengths', 'desc': 'Sample-accurate playback synchronization via Web Audio API clock ($t_{\\text{ctx}}$).'}
            ],
            'metrics': [
                {'label': 'Sample Rate', 'val': '48.0 kHz', 'sub': 'Broadcast Grade'},
                {'label': 'Decimation', 'val': 'Min/Max Peaks', 'sub': 'Fast Canvas'},
                {'label': 'Sync Clock', 'val': 'AudioContext', 'sub': 'Zero Jitter'},
                {'label': 'Automation', 'val': 'Bézier Envelopes', 'sub': 'Volume Pan'}
            ],
            'code_snippet': """const audioCtx = new AudioContext();
const source = audioCtx.createBufferSource();
source.buffer = audioBuffer;
source.connect(audioCtx.destination);"""
        },

        # 19. 3D Spatiotemporal Trajectory Ribbon
        {
            'slide_id': 'slide-19-spatiotemporal-3d',
            'tag': '19 / Space-Time Cubes',
            'headline': 'The Space-Time Cube:',
            'headline_span': '3D Trajectory Ribbons',
            'subtitle': 'Hägerstrand space-time path mapping 2D geographic movement along a vertical temporal Z-axis.',
            'library_badge': 'Three.js / Vis-Graph3D',
            'chart_html': """
              <div id="spacetime-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('spacetime-stage');
                  if (!el || !window.Plotly) return;
                  const t = [], x = [], y = [];
                  for(let i=0; i<80; i++) {
                    t.push(i);
                    x.push(Math.sin(i/8) * 20 + i*0.2);
                    y.push(Math.cos(i/8) * 20);
                  }
                  const trace = {
                    type: 'scatter3d', mode: 'lines+markers',
                    x: x, y: y, z: t,
                    line: { color: '#00e676', width: 4 },
                    marker: { size: 3, color: '#f3cf65' }
                  };
                  const layout = {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { title: 'Latitude (X)', color: '#9ba9a1', gridcolor: 'rgba(255,255,255,0.08)' },
                      yaxis: { title: 'Longitude (Y)', color: '#9ba9a1', gridcolor: 'rgba(255,255,255,0.08)' },
                      zaxis: { title: 'Time (Epoch)', color: '#f3cf65', gridcolor: 'rgba(255,255,255,0.08)' },
                      camera: { eye: { x: 1.5, y: 1.5, z: 1.2 } }
                    }
                  };
                  Plotly.newPlot('spacetime-stage', [trace], layout, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Torsten Hägerstrand time-geography: 3D trajectory $\\gamma(t) = (x(t), y(t), t)$ inside a bounded prism.'},
                {'title': 'Enterprise Use Cases', 'desc': 'VIP executive travel itinerary tracking, wildlife migration, naval fleet patrols.'},
                {'title': 'Technical Strengths', 'desc': 'Disentangles spatial loops: when a traveler returns to the same location, time advances upward.'}
            ],
            'metrics': [
                {'label': 'Concept', 'val': 'Space-Time Prism', 'sub': 'Hägerstrand'},
                {'label': 'Axes', 'val': 'X, Y (Geo), Z (Time)', 'sub': '3D Continuous'},
                {'label': 'Loop Resolution', 'val': 'Disentangled', 'sub': 'Z Separation'},
                {'label': 'Render Type', 'val': 'WebGL 3D', 'sub': 'Plotly Engine'}
            ],
            'code_snippet': """Plotly.newPlot('cube', [{
  type: 'scatter3d', mode: 'lines',
  x: lats, y: lons, z: timestamps
}]);"""
        },

        # 20. Real-time Flight Departure/Arrival Board Timeline
        {
            'slide_id': 'slide-20-flight-board',
            'tag': '20 / Operational Display',
            'headline': 'Tactical Dispatch Boards:',
            'headline_span': 'Aviation Departure Timeline',
            'subtitle': 'High-contrast split-flap airport flight board timeline organizing gate slots, delays, and arrivals.',
            'library_badge': 'Tactical Dispatch UI',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:15px; box-sizing:border-box;">
                <table class="viz-table">
                  <thead>
                    <tr>
                      <th>Time</th>
                      <th>Flight</th>
                      <th>Destination</th>
                      <th>Gate</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td style="font-family:JetBrains Mono; color:#f3cf65;">14:15</td>
                      <td style="font-family:JetBrains Mono;">SQ 318</td>
                      <td>London Heathrow (LHR)</td>
                      <td>B04</td>
                      <td><span style="color:#00e676; font-weight:bold;">BOARDING</span></td>
                    </tr>
                    <tr>
                      <td style="font-family:JetBrains Mono; color:#f3cf65;">14:30</td>
                      <td style="font-family:JetBrains Mono;">BA 012</td>
                      <td>Singapore Changi (SIN)</td>
                      <td>C12</td>
                      <td><span style="color:#00e676; font-weight:bold;">FINAL CALL</span></td>
                    </tr>
                    <tr>
                      <td style="font-family:JetBrains Mono; color:#f3cf65;">14:55</td>
                      <td style="font-family:JetBrains Mono;">EK 405</td>
                      <td>Dubai International (DXB)</td>
                      <td>A08</td>
                      <td><span style="color:#ffab00; font-weight:bold;">DELAYED 20m</span></td>
                    </tr>
                    <tr>
                      <td style="font-family:JetBrains Mono; color:#f3cf65;">15:20</td>
                      <td style="font-family:JetBrains Mono;">QF 001</td>
                      <td>Sydney Kingsford (SYD)</td>
                      <td>B10</td>
                      <td><span style="color:#9ba9a1;">SCHEDULED</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Chronological priority queue ordering: $Q = \\text{sort}(\\{f_i\\}, \\text{key}=t_{\\text{est}})$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Airport terminal displays, train station departures, hotel guest check-in arrival dashboards.'},
                {'title': 'Technical Strengths', 'desc': 'Ultra-clear typography, high ambient light contrast, instant glanceability.'}
            ],
            'metrics': [
                {'label': 'Display Mode', 'val': 'High Contrast', 'sub': 'Airport Standard'},
                {'label': 'Queue Order', 'val': 'Earliest First', 'sub': 'Priority Queue'},
                {'label': 'Refresh', 'val': 'WebSocket Push', 'sub': 'Instant State'},
                {'label': 'Font', 'val': 'JetBrains Mono', 'sub': 'Fixed Width'}
            ],
            'code_snippet': """flights.sort((a, b) => a.estimatedTime - b.estimatedTime);
renderSplitFlapTable(flights);"""
        }
    ]

    html = generate_deck_html(deck_meta, slides)
    out_path = os.path.join(SCRIPT_DIR, "02-javascript-timelines-gantt.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Built {out_path} (20 slides, {len(html)} bytes)")

if __name__ == "__main__":
    build_deck()
