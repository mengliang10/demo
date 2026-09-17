#!/usr/bin/env python3
"""
create_viz_structure.py
=======================
Creates the complete directory structure and documentation for:
- JavaScript Visualization, Graphical, & Interactive Libraries (5 categories, 77 tools)
- Python Visualization, Graphical, & Interactive Libraries (5 categories, 45 tools)

In: /mnt/storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software/
"""

import os
import sys

BASE_DIR = "/mnt/storage/Consultancy/07_PRESENTATION_AND_DIGITAL/Demostration of Visualization Software"

# Directory Structure and Library Metadata
DATA = {
    "JavaScript Visualization, Graphical, & Interactive Libraries": {
        "Chart & Plotting Engines": [
            {
                "name": "D3.js",
                "folder": "D3.js",
                "aliases": ["d3"],
                "url": "https://d3js.org",
                "npm": "npm install d3",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>',
                "summary": "Data-Driven Documents: low-level, powerful SVG/Canvas/HTML data-binding and visualization library.",
                "snippet": """const svg = d3.select("body").append("svg").attr("width", 400).attr("height", 200);
svg.selectAll("rect")
  .data([10, 35, 22, 55, 40])
  .join("rect")
  .attr("x", (d, i) => i * 60 + 20)
  .attr("y", d => 180 - d * 2.5)
  .attr("width", 45)
  .attr("height", d => d * 2.5)
  .attr("fill", "#00e676");"""
            },
            {
                "name": "Chart.js",
                "folder": "Chart.js",
                "aliases": ["chartjs"],
                "url": "https://www.chartjs.org",
                "npm": "npm install chart.js",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>',
                "summary": "Simple yet flexible JavaScript charting for designers & developers using HTML5 Canvas.",
                "snippet": """const ctx = document.getElementById('myChart');
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple'],
    datasets: [{ label: 'Votes', data: [12, 19, 3, 5, 2], borderWidth: 1 }]
  }
});"""
            },
            {
                "name": "Plotly.js",
                "folder": "Plotly.js",
                "aliases": ["plotlyjs"],
                "url": "https://plotly.com/javascript/",
                "npm": "npm install plotly.js-dist-min",
                "cdn": '<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>',
                "summary": "High-level, declarative charting library built on D3 and WebGL with over 40 chart types.",
                "snippet": """Plotly.newPlot('myDiv', [{
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  mode: 'markers+lines',
  type: 'scatter'
}], { title: 'Basic Plotly Chart' });"""
            },
            {
                "name": "Apache ECharts",
                "folder": "Apache ECharts",
                "aliases": ["echarts"],
                "url": "https://echarts.apache.org",
                "npm": "npm install echarts",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>',
                "summary": "Powerful charting and visualization library for enterprise applications with high rendering performance.",
                "snippet": """const chart = echarts.init(document.getElementById('main'));
chart.setOption({
  xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] },
  yAxis: { type: 'value' },
  series: [{ data: [150, 230, 224, 218, 135], type: 'line' }]
});"""
            },
            {
                "name": "Highcharts",
                "folder": "Highcharts",
                "aliases": ["highcharts"],
                "url": "https://www.highcharts.com",
                "npm": "npm install highcharts",
                "cdn": '<script src="https://code.highcharts.com/highcharts.js"></script>',
                "summary": "Industry-standard, interactive JavaScript charting engine for web and mobile.",
                "snippet": """Highcharts.chart('container', {
  title: { text: 'Monthly Average Temperature' },
  xAxis: { categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May'] },
  series: [{ name: 'Tokyo', data: [7.0, 6.9, 9.5, 14.5, 18.2] }]
});"""
            },
            {
                "name": "Google Charts",
                "folder": "Google Charts",
                "aliases": ["google-charts"],
                "url": "https://developers.google.com/chart",
                "npm": "npm install google-charts",
                "cdn": '<script src="https://www.gstatic.com/charts/loader.js"></script>',
                "summary": "Free visualization service with interactive charts and comprehensive cross-browser compatibility.",
                "snippet": """google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(() => {
  const data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'], ['Work', 8], ['Eat', 2], ['Sleep', 7]
  ]);
  const chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, { title: 'Daily Activities' });
});"""
            },
            {
                "name": "Vega",
                "folder": "Vega",
                "aliases": ["vega"],
                "url": "https://vega.github.io/vega/",
                "npm": "npm install vega",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>',
                "summary": "Declarative format for creating, saving, and sharing interactive visualization designs.",
                "snippet": """const spec = { "$schema": "https://vega.github.io/schema/vega/v5.json", "width": 400, "height": 200 };
const view = new vega.View(vega.parse(spec), { renderer: 'canvas', container: '#view' }).run();"""
            },
            {
                "name": "Vega-Lite",
                "folder": "Vega-Lite",
                "aliases": ["vega-lite"],
                "url": "https://vega.github.io/vega-lite/",
                "npm": "npm install vega-lite vega vega-embed",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>',
                "summary": "High-level grammar of interactive graphics, generating concise JSON visual specifications.",
                "snippet": """vegaEmbed('#vis', {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"values": [{"a": "A","b": 28}, {"a": "B","b": 55}]},
  "mark": "bar",
  "encoding": {
    "x": {"field": "a", "type": "nominal"},
    "y": {"field": "b", "type": "quantitative"}
  }
});"""
            },
            {
                "name": "Observable Plot",
                "folder": "Observable Plot",
                "aliases": ["observable-plot"],
                "url": "https://observablehq.com/plot",
                "npm": "npm install @observablehq/plot",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6"></script>',
                "summary": "Concise, expressive library for exploratory data visualization on the web.",
                "snippet": """const plot = Plot.rectY([1, 2, 3, 4, 5], {x: d => d, y: d => d * 2}).plot();
document.body.append(plot);"""
            },
            {
                "name": "ApexCharts",
                "folder": "ApexCharts",
                "aliases": ["apexcharts"],
                "url": "https://apexcharts.com",
                "npm": "npm install apexcharts",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>',
                "summary": "Modern SVG charting library for reactive applications with elegant dark mode and animations.",
                "snippet": """const options = {
  chart: { type: 'area', height: 350 },
  series: [{ name: 'Series 1', data: [30, 40, 45, 50, 49, 60, 70] }],
  xaxis: { categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997] }
};
const chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();"""
            },
            {
                "name": "amCharts",
                "folder": "amCharts",
                "aliases": ["amcharts", "amcharts5"],
                "url": "https://www.amcharts.com",
                "npm": "npm install @amcharts/amcharts5",
                "cdn": '<script src="https://cdn.amcharts.com/lib/5/index.js"></script>',
                "summary": "Fast, flexible data visualization library with advanced animations and Canvas engine (amCharts 5).",
                "snippet": """const root = am5.Root.new("chartdiv");
const chart = root.container.children.push(am5xy.XYChart.new(root, {}));
// configure axes and series..."""
            },
            {
                "name": "FusionCharts",
                "folder": "FusionCharts",
                "aliases": ["fusioncharts"],
                "url": "https://www.fusioncharts.com",
                "npm": "npm install fusioncharts",
                "cdn": '<script src="https://cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>',
                "summary": "Enterprise-grade JavaScript charts, maps, and dashboards for complex corporate systems.",
                "snippet": """FusionCharts.ready(function(){
  var chart = new FusionCharts({
    type: 'column2d',
    renderAt: 'chart-container',
    width: '500',
    height: '300',
    dataSource: { chart: { caption: "Quarterly Revenue" }, data: [{ label: "Q1", value: "195000" }] }
  }).render();
});"""
            },
            {
                "name": "C3.js",
                "folder": "C3.js",
                "aliases": ["c3"],
                "url": "https://c3js.org",
                "npm": "npm install c3",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/c3/0.7.20/c3.min.js"></script>',
                "summary": "D3-based reusable chart library providing simple API wrappers for common charts.",
                "snippet": """var chart = c3.generate({
  bindto: '#chart',
  data: {
    columns: [
      ['data1', 30, 200, 100, 400, 150, 250],
      ['data2', 50, 20, 10, 40, 15, 25]
    ]
  }
});"""
            },
            {
                "name": "Chartist.js",
                "folder": "Chartist.js",
                "aliases": ["chartist"],
                "url": "https://chartist.dev",
                "npm": "npm install chartist",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/chartist@1.3.0/dist/index.umd.min.js"></script>',
                "summary": "Lightweight, responsive charting library using SVG and simple CSS styling.",
                "snippet": """new Chartist.LineChart('#chart', {
  labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
  series: [[12, 9, 7, 8, 5]]
});"""
            },
            {
                "name": "Dygraphs",
                "folder": "Dygraphs",
                "aliases": ["dygraphs"],
                "url": "https://dygraphs.com",
                "npm": "npm install dygraphs",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/dygraph/2.2.1/dygraph.min.js"></script>',
                "summary": "Fast, flexible open-source JavaScript chart library optimized for huge, dense time-series datasets.",
                "snippet": """new Dygraph(document.getElementById("div_g"),
  "Date,Temperature\\n2008-05-07,75\\n2008-05-08,70\\n2008-05-09,80\\n", {});"""
            },
            {
                "name": "Taucharts",
                "folder": "Taucharts",
                "aliases": ["taucharts"],
                "url": "https://taucharts.com",
                "npm": "npm install taucharts",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/taucharts@2/dist/taucharts.min.js"></script>',
                "summary": "Flexible charting library based on D3 with grammar of graphics principles and facets.",
                "snippet": """const chart = new Taucharts.Chart({
  data: [{x: 1, y: 2}, {x: 2, y: 4}],
  type: 'scatterplot',
  x: 'x',
  y: 'y'
});
chart.renderTo('#chart');"""
            },
            {
                "name": "MetricsGraphics.js",
                "folder": "MetricsGraphics.js",
                "aliases": ["metricsgraphics"],
                "url": "https://metricsgraphicsjs.org",
                "npm": "npm install metricsgraphics",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/metrics-graphics/2.15.6/metricsgraphics.min.js"></script>',
                "summary": "D3-based library optimized for visualizing time-series and scatter data cleanly.",
                "snippet": """MG.data_graphic({
  title: "Line Chart",
  data: [{date: new Date('2020-01-01'), value: 10}, {date: new Date('2020-01-02'), value: 20}],
  width: 450,
  height: 200,
  target: '#chart',
  x_accessor: 'date',
  y_accessor: 'value'
});"""
            },
            {
                "name": "AntV G2",
                "folder": "AntV G2",
                "aliases": ["g2", "antv-g2"],
                "url": "https://g2.antv.antgroup.com",
                "npm": "npm install @antv/g2",
                "cdn": '<script src="https://unpkg.com/@antv/g2"></script>',
                "summary": "The grammar of graphics in JavaScript by Ant Financial / Alibaba.",
                "snippet": """import { Chart } from '@antv/g2';
const chart = new Chart({ container: 'container' });
chart.interval().data([{ genre: 'Sports', sold: 275 }, { genre: 'Strategy', sold: 115 }]).encode('x', 'genre').encode('y', 'sold');
chart.render();"""
            },
            {
                "name": "Vizzu",
                "folder": "Vizzu",
                "aliases": ["vizzu"],
                "url": "https://vizzuhq.com",
                "npm": "npm install vizzu",
                "cdn": '<script type="module" src="https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js"></script>',
                "summary": "Library for animated data stories and seamless morphing chart-to-chart transitions.",
                "snippet": """import Vizzu from 'https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js';
const chart = new Vizzu('myVizzu');
chart.initializing.then(chart => chart.animate({
  data: { series: [{ name: 'Foo', values: ['Alice', 'Bob'] }, { name: 'Bar', values: [15, 32] }] },
  config: { x: 'Foo', y: 'Bar', geometry: 'rectangle' }
}));"""
            },
            {
                "name": "NVD3",
                "folder": "NVD3",
                "aliases": ["nvd3"],
                "url": "https://nvd3.org",
                "npm": "npm install nvd3",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.6/nv.d3.min.js"></script>',
                "summary": "Reusable charts and chart components built on top of D3.js.",
                "snippet": """nv.addGraph(function() {
  const chart = nv.models.lineChart().useInteractiveGuideline(true);
  d3.select('#chart svg').datum(myData).call(chart);
  return chart;
});"""
            },
            {
                "name": "CanvasJS",
                "folder": "CanvasJS",
                "aliases": ["canvasjs"],
                "url": "https://canvasjs.com",
                "npm": "npm install @canvasjs/charts",
                "cdn": '<script src="https://cdn.canvasjs.com/canvasjs.min.js"></script>',
                "summary": "High-performance HTML5 canvas charting library with rich interactive features.",
                "snippet": """const chart = new CanvasJS.Chart("chartContainer", {
  title: { text: "Performance Metric" },
  data: [{ type: "column", dataPoints: [{ y: 10, label: "Apple" }, { y: 15, label: "Mango" }] }]
});
chart.render();"""
            },
            {
                "name": "Recharts",
                "folder": "Recharts",
                "aliases": ["recharts"],
                "url": "https://recharts.org",
                "npm": "npm install recharts",
                "cdn": "Bundled via npm / Webpack / Vite in React",
                "summary": "Redefined chart library built with React and D3 components for declarative composition.",
                "snippet": """import { BarChart, Bar, XAxis, YAxis, Tooltip } from 'recharts';
const App = () => (
  <BarChart width={400} height={250} data={[{name: 'A', uv: 400}, {name: 'B', uv: 700}]}>
    <XAxis dataKey="name" /><YAxis /><Tooltip /><Bar dataKey="uv" fill="#8884d8" />
  </BarChart>
);"""
            },
            {
                "name": "Victory",
                "folder": "Victory",
                "aliases": ["victory"],
                "url": "https://commerce.nearform.com/open-source/victory/",
                "npm": "npm install victory",
                "cdn": "Bundled via npm in React",
                "summary": "Modular React components for building interactive charts and data visualizations.",
                "snippet": """import { VictoryBar, VictoryChart, VictoryTheme } from 'victory';
const App = () => (
  <VictoryChart theme={VictoryTheme.material} domainPadding={20}>
    <VictoryBar data={[{x: 1, y: 2}, {x: 2, y: 3}, {x: 3, y: 5}]} />
  </VictoryChart>
);"""
            },
            {
                "name": "Nivo",
                "folder": "Nivo",
                "aliases": ["nivo"],
                "url": "https://nivo.rocks",
                "npm": "npm install @nivo/core @nivo/bar",
                "cdn": "Bundled via npm in React",
                "summary": "Rich set of data visualization components built on top of React and D3 with SVG, Canvas, and SSR.",
                "snippet": """import { ResponsiveBar } from '@nivo/bar';
const MyBar = ({ data }) => (
  <ResponsiveBar data={data} keys={['hot dog', 'burger']} indexBy="country" margin={{ top: 50, right: 130, bottom: 50, left: 60 }} />
);"""
            },
            {
                "name": "Visx",
                "folder": "Visx",
                "aliases": ["visx", "vx"],
                "url": "https://airbnb.io/visx/",
                "npm": "npm install @visx/shape @visx/scale @visx/group",
                "cdn": "Bundled via npm in React",
                "summary": "Low-level visualization components from Airbnb combining React state and D3 math.",
                "snippet": """import { Bar } from '@visx/shape';
import { Group } from '@visx/group';
// Composable primitive elements for custom chart architectures"""
            }
        ],
        "Diagramming, Flowcharts & Graph Networks": [
            {
                "name": "Cytoscape.js",
                "folder": "Cytoscape.js",
                "aliases": ["cytoscape"],
                "url": "https://js.cytoscape.org",
                "npm": "npm install cytoscape",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.28.1/cytoscape.min.js"></script>',
                "summary": "Graph theory / network library for analysis and visualization in bioinformatics and relational data.",
                "snippet": """const cy = cytoscape({
  container: document.getElementById('cy'),
  elements: [
    { data: { id: 'a' } }, { data: { id: 'b' } },
    { data: { id: 'ab', source: 'a', target: 'b' } }
  ],
  style: [{ selector: 'node', style: { 'background-color': '#666', 'label': 'data(id)' } }],
  layout: { name: 'grid' }
});"""
            },
            {
                "name": "Sigma.js",
                "folder": "Sigma.js",
                "aliases": ["sigmajs"],
                "url": "https://www.sigmajs.org",
                "npm": "npm install sigma graphology",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/sigma.js/2.4.0/sigma.min.js"></script>',
                "summary": "WebGL-powered JavaScript library dedicated to drawing massive network graphs.",
                "snippet": """import Graph from 'graphology';
import Sigma from 'sigma';
const graph = new Graph();
graph.addNode("1", { label: "Node 1", x: 0, y: 0, size: 10, color: "blue" });
graph.addNode("2", { label: "Node 2", x: 1, y: 1, size: 10, color: "red" });
graph.addEdge("1", "2");
const renderer = new Sigma(graph, document.getElementById("container"));"""
            },
            {
                "name": "Vis.js (vis-network / vis-timeline)",
                "folder": "Vis.js (vis-network - vis-timeline)",
                "aliases": ["Vis.js", "vis-network", "vis-timeline", "visjs"],
                "url": "https://visjs.org",
                "npm": "npm install vis-network vis-timeline",
                "cdn": '<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>',
                "summary": "Dynamic, browser-based visualization libraries for interactive networks and timeline data.",
                "snippet": """const nodes = new vis.DataSet([{ id: 1, label: 'Node 1' }, { id: 2, label: 'Node 2' }]);
const edges = new vis.DataSet([{ from: 1, to: 2 }]);
const network = new vis.Network(container, { nodes, edges }, {});"""
            },
            {
                "name": "AntV G6",
                "folder": "AntV G6",
                "aliases": ["g6", "antv-g6"],
                "url": "https://g6.antv.antgroup.com",
                "npm": "npm install @antv/g6",
                "cdn": '<script src="https://unpkg.com/@antv/g6"></script>',
                "summary": "Graph visualization engine for large relational data and knowledge graphs by Ant Group.",
                "snippet": """import { Graph } from '@antv/g6';
const graph = new Graph({
  container: 'container',
  width: 500,
  height: 500,
  data: { nodes: [{ id: 'node1' }, { id: 'node2' }], edges: [{ source: 'node1', target: 'node2' }] }
});
graph.render();"""
            },
            {
                "name": "JointJS",
                "folder": "JointJS",
                "aliases": ["jointjs"],
                "url": "https://www.jointjs.com",
                "npm": "npm install @joint/core",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/jointjs/3.7.7/joint.min.js"></script>',
                "summary": "Modern diagramming library for interactive visual tools, statecharts, and workflow builders.",
                "snippet": """const graph = new joint.dia.Graph();
const paper = new joint.dia.Paper({ el: document.getElementById('paper'), model: graph, width: 600, height: 400 });
const rect = new joint.shapes.standard.Rectangle();
rect.position(100, 30);
rect.resize(100, 40);
rect.attr({ body: { fill: 'blue' }, label: { text: 'Hello', fill: 'white' } });
rect.addTo(graph);"""
            },
            {
                "name": "GoJS",
                "folder": "GoJS",
                "aliases": ["gojs"],
                "url": "https://gojs.net",
                "npm": "npm install gojs",
                "cdn": '<script src="https://unpkg.com/gojs/release/go.js"></script>',
                "summary": "Feature-rich library for interactive diagrams, flowcharts, org charts, and BPMN systems.",
                "snippet": """const myDiagram = new go.Diagram("myDiagramDiv");
myDiagram.model = new go.GraphLinksModel(
  [{ key: "Alpha" }, { key: "Beta" }],
  [{ from: "Alpha", to: "Beta" }]
);"""
            },
            {
                "name": "Mermaid.js",
                "folder": "Mermaid.js",
                "aliases": ["mermaid"],
                "url": "https://mermaid.js.org",
                "npm": "npm install mermaid",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>',
                "summary": "Markdown-inspired text-to-diagram generation tool for flowcharts, sequences, and class diagrams.",
                "snippet": """mermaid.initialize({ startOnLoad: true });
// In HTML: <pre class="mermaid">graph TD; A-->B; A-->C; B-->D; C-->D;</pre>"""
            },
            {
                "name": "mxGraph",
                "folder": "mxGraph",
                "aliases": ["mxgraph"],
                "url": "https://github.com/jgraph/mxgraph",
                "npm": "npm install mxgraph",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/mxgraph@4.2.2/javascript/mxClient.js"></script>',
                "summary": "Battle-tested diagramming library powering enterprise tools like draw.io / diagrams.net.",
                "snippet": """const container = document.getElementById('graphContainer');
const graph = new mxGraph(container);
const parent = graph.getDefaultParent();
graph.getModel().beginUpdate();
try {
  const v1 = graph.insertVertex(parent, null, 'Hello,', 20, 20, 80, 30);
  const v2 = graph.insertVertex(parent, null, 'World!', 200, 150, 80, 30);
  graph.insertEdge(parent, null, '', v1, v2);
} finally { graph.getModel().endUpdate(); }"""
            },
            {
                "name": "Nomnoml",
                "folder": "Nomnoml",
                "aliases": ["nomnoml"],
                "url": "https://nomnoml.com",
                "npm": "npm install nomnoml",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/nomnoml/dist/nomnoml.min.js"></script>',
                "summary": "Sassy UML diagram renderer based on pure text syntax rendered to HTML5 Canvas.",
                "snippet": """const canvas = document.getElementById('target-canvas');
const source = '[Pirate]->[Car] [Car]->[Fuel]';
nomnoml.draw(canvas, source);"""
            },
            {
                "name": "jsPlumb",
                "folder": "jsPlumb",
                "aliases": ["jsplumb"],
                "url": "https://jsplumbtoolkit.com",
                "npm": "npm install @jsplumb/core",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/jsPlumb/2.15.6/js/jsplumb.min.js"></script>',
                "summary": "Visual connectivity library for wiring DOM elements together with lines, anchors, and arrows.",
                "snippet": """jsPlumb.ready(function() {
  jsPlumb.connect({
    source: "item1",
    target: "item2",
    endpoint: "Dot"
  });
});"""
            },
            {
                "name": "Svelvet",
                "folder": "Svelvet",
                "aliases": ["svelvet"],
                "url": "https://svelvet.mintlify.app",
                "npm": "npm install svelvet",
                "cdn": "Bundled in Svelte applications",
                "summary": "Lightweight, customizable Svelte component library for building interactive node-based UIs.",
                "snippet": """<script>
  import { Svelvet, Node } from 'svelvet';
</script>
<Svelvet>
  <Node label="Input" />
</Svelvet>"""
            },
            {
                "name": "Diagram.js",
                "folder": "Diagram.js",
                "aliases": ["diagram-js"],
                "url": "https://github.com/bpmn-io/diagram-js",
                "npm": "npm install diagram-js",
                "cdn": "Bundled via npm / Webpack",
                "summary": "Web-based diagramming library underpinning bpmn-io, dmn-io, and cmmn-io modeling engines.",
                "snippet": """import Diagram from 'diagram-js';
const diagram = new Diagram();
// Configure canvas, elementFactory, and modeling modules"""
            },
            {
                "name": "React Flow",
                "folder": "React Flow",
                "aliases": ["react-flow", "xyflow"],
                "url": "https://reactflow.dev",
                "npm": "npm install @xyflow/react",
                "cdn": "Bundled via npm in React",
                "summary": "Highly customizable React component for building node-based workflows and interactive graph UIs.",
                "snippet": """import { ReactFlow } from '@xyflow/react';
const nodes = [{ id: '1', position: { x: 0, y: 0 }, data: { label: 'Node 1' } }];
const edges = [];
export default () => <div style={{ height: 400 }}><ReactFlow nodes={nodes} edges={edges} /></div>;"""
            },
            {
                "name": "JointJS+",
                "folder": "JointJS+",
                "aliases": ["jointjs-plus", "rappid"],
                "url": "https://www.jointjs.com/jointjs-plus",
                "npm": "Commercial license package",
                "cdn": "Commercial vendor distribution",
                "summary": "Commercial diagramming toolkit (formerly Rappid) with advanced visual UI components.",
                "snippet": """// Advanced commercial toolkit extending JointJS with stencil palettes, inspector dialogs, and paper scroller."""
            },
            {
                "name": "State.js",
                "folder": "State.js",
                "aliases": ["statejs"],
                "url": "https://github.com/steelbreeze/state",
                "npm": "npm install @steelbreeze/state",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/@steelbreeze/state"></script>',
                "summary": "Hierarchical finite state machine (statechart) visualization and execution engine.",
                "snippet": """import * as state from '@steelbreeze/state';
const model = new state.State('my_state_machine');
const initial = new state.PseudoState('initial', model, state.PseudoStateKind.Initial);"""
            },
            {
                "name": "Ogma",
                "folder": "Ogma",
                "aliases": ["ogma"],
                "url": "https://linkurio.us/ogma/",
                "npm": "npm install @linkurious/ogma",
                "cdn": "Enterprise vendor distribution (Linkurious)",
                "summary": "Commercial high-performance JavaScript library for large-scale graph visualization and cyber analytics.",
                "snippet": """const ogma = new Ogma({ container: 'graph-container' });
ogma.setGraph({ nodes: [{id: 1, text: 'A'}, {id: 2, text: 'B'}], edges: [{source: 1, target: 2}] });"""
            },
            {
                "name": "Keylines",
                "folder": "Keylines",
                "aliases": ["keylines"],
                "url": "https://cambridge-intelligence.com/keylines/",
                "npm": "Commercial license (Cambridge Intelligence)",
                "cdn": "Vendor bundle",
                "summary": "Enterprise network visualization SDK tailored for intelligence, fraud, and cyber security investigation.",
                "snippet": """KeyLines.create({ id: 'chart-id' }, (chart) => {
  chart.load({ nodes: [...], items: [...] });
});"""
            },
            {
                "name": "yFiles",
                "folder": "yFiles",
                "aliases": ["yfiles"],
                "url": "https://www.yworks.com/products/yfiles",
                "npm": "npm install yfiles",
                "cdn": "Commercial evaluation / license bundle",
                "summary": "High-end commercial diagramming library with state-of-the-art automatic graph layouts (yWorks).",
                "snippet": """import { GraphComponent } from 'yfiles';
const graphComponent = new GraphComponent('#graphComponent');
const graph = graphComponent.graph;
const n1 = graph.createNodeAt([0, 0]);
const n2 = graph.createNodeAt([100, 100]);
graph.createEdge(n1, n2);"""
            },
            {
                "name": "VivaGraphJS",
                "folder": "VivaGraphJS",
                "aliases": ["vivagraph"],
                "url": "https://github.com/anvaka/VivaGraphJS",
                "npm": "npm install vivagraphjs",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/vivagraphjs@0.12.0/dist/vivagraph.min.js"></script>',
                "summary": "Graph drawing library designed for high performance with WebGL, SVG, and force-directed algorithms.",
                "snippet": """const graph = Viva.Graph.graph();
graph.addLink(1, 2);
const renderer = Viva.Graph.View.renderer(graph, { container: document.getElementById('graph1') });
renderer.run();"""
            }
        ],
        "Canvas, WebGL, 2D-3D Graphics & Creative Coding": [
            {
                "name": "Three.js",
                "folder": "Three.js",
                "aliases": ["threejs"],
                "url": "https://threejs.org",
                "npm": "npm install three",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>',
                "summary": "The premier 3D WebGL library for creating rich 3D computer graphics directly in the browser.",
                "snippet": """const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
const cube = new THREE.Mesh(new THREE.BoxGeometry(), new THREE.MeshBasicMaterial({ color: 0x00ff00 }));
scene.add(cube);
camera.position.z = 5;
renderer.render(scene, camera);"""
            },
            {
                "name": "PixiJS",
                "folder": "PixiJS",
                "aliases": ["pixijs"],
                "url": "https://pixijs.com",
                "npm": "npm install pixi.js",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/pixi.js/7.3.2/pixi.min.js"></script>',
                "summary": "Super fast 2D WebGL rendering engine with automatic Canvas fallback and rich sprite batching.",
                "snippet": """const app = new PIXI.Application({ width: 640, height: 360 });
document.body.appendChild(app.view);
const graphics = new PIXI.Graphics();
graphics.beginFill(0xDE3249);
graphics.drawRect(50, 50, 100, 100);
graphics.endFill();
app.stage.addChild(graphics);"""
            },
            {
                "name": "Two.js",
                "folder": "Two.js",
                "aliases": ["twojs"],
                "url": "https://two.js.org",
                "npm": "npm install two.js",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/two.js/0.8.10/two.min.js"></script>',
                "summary": "Two-dimensional drawing API agnostic to SVG, Canvas, or WebGL renderers.",
                "snippet": """const two = new Two({ width: 285, height: 200 }).appendTo(document.body);
const circle = two.makeCircle(72, 100, 50);
circle.fill = '#FF8000';
two.update();"""
            },
            {
                "name": "Fabric.js",
                "folder": "Fabric.js",
                "aliases": ["fabricjs"],
                "url": "http://fabricjs.com",
                "npm": "npm install fabric",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"></script>',
                "summary": "Powerful HTML5 canvas library with interactive object model, SVG parsing, and serialized states.",
                "snippet": """const canvas = new fabric.Canvas('c');
const rect = new fabric.Rect({ top: 100, left: 100, width: 60, height: 70, fill: 'red' });
canvas.add(rect);"""
            },
            {
                "name": "Konva.js",
                "folder": "Konva.js",
                "aliases": ["konva"],
                "url": "https://konvajs.org",
                "npm": "npm install konva",
                "cdn": '<script src="https://unpkg.com/konva@9/konva.min.js"></script>',
                "summary": "2D canvas framework for desktop and mobile with high-performance layer compositing and event handling.",
                "snippet": """const stage = new Konva.Stage({ container: 'container', width: 500, height: 500 });
const layer = new Konva.Layer();
const circle = new Konva.Circle({ x: stage.width() / 2, y: stage.height() / 2, radius: 70, fill: 'red' });
layer.add(circle);
stage.add(layer);"""
            },
            {
                "name": "Paper.js",
                "folder": "Paper.js",
                "aliases": ["paperjs"],
                "url": "http://paperjs.org",
                "npm": "npm install paper",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/paper.js/0.12.17/paper-full.min.js"></script>',
                "summary": "Vector graphics scripting framework running on top of the HTML5 Canvas with clean Bézier math.",
                "snippet": """paper.setup(document.getElementById('myCanvas'));
const path = new paper.Path();
path.strokeColor = 'black';
path.moveTo(new paper.Point(20, 20));
path.lineTo(new paper.Point(100, 100));
paper.view.draw();"""
            },
            {
                "name": "p5.js",
                "folder": "p5.js",
                "aliases": ["p5"],
                "url": "https://p5js.org",
                "npm": "npm install p5",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>',
                "summary": "Creative coding library inspired by Processing, making code accessible for generative art and education.",
                "snippet": """function setup() {
  createCanvas(400, 400);
}
function draw() {
  background(220);
  ellipse(mouseX, mouseY, 50, 50);
}"""
            },
            {
                "name": "Babylon.js",
                "folder": "Babylon.js",
                "aliases": ["babylonjs"],
                "url": "https://www.babylonjs.com",
                "npm": "npm install @babylonjs/core",
                "cdn": '<script src="https://cdn.babylonjs.com/babylon.js"></script>',
                "summary": "Complete, powerful, and accessible 3D game and WebGL/WebGPU rendering engine for the web.",
                "snippet": """const canvas = document.getElementById("renderCanvas");
const engine = new BABYLON.Engine(canvas, true);
const scene = new BABYLON.Scene(engine);
const camera = new BABYLON.FreeCamera("camera1", new BABYLON.Vector3(0, 5, -10), scene);
const sphere = BABYLON.MeshBuilder.CreateSphere("sphere", {diameter: 2}, scene);
engine.runRenderLoop(() => scene.render());"""
            },
            {
                "name": "Phaser",
                "folder": "Phaser",
                "aliases": ["phaser"],
                "url": "https://phaser.io",
                "npm": "npm install phaser",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/phaser@3.80.1/dist/phaser.min.js"></script>',
                "summary": "Fast, fun, and free 2D game framework for desktop and mobile HTML5 web applications.",
                "snippet": """const config = { type: Phaser.AUTO, width: 800, height: 600, scene: { preload, create } };
const game = new Phaser.Game(config);
function preload() {}
function create() { this.add.text(100, 100, 'Hello Phaser!', { fill: '#0f0' }); }"""
            },
            {
                "name": "Scene.js",
                "folder": "Scene.js",
                "aliases": ["scenejs"],
                "url": "https://daybrush.com/scenejs/",
                "npm": "npm install scenejs",
                "cdn": '<script src="https://daybrush.com/scenejs/release/latest/dist/scene.min.js"></script>',
                "summary": "JavaScript timeline-based animation library for creating complex choreographed web scenes.",
                "snippet": """const scene = new Scene({
  ".circle": {
    0: { transform: "scale(0)" },
    1: { transform: "scale(1)" }
  }
}, { duration: 1 }).play();"""
            },
            {
                "name": "zrender",
                "folder": "zrender",
                "aliases": ["zrender"],
                "url": "https://ecomfe.github.io/zrender-doc/public/",
                "npm": "npm install zrender",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/zrender@5.5.0/dist/zrender.min.js"></script>',
                "summary": "Lightweight 2D canvas rendering engine that powers Apache ECharts with rich graphic primitives.",
                "snippet": """const zr = zrender.init(document.getElementById('main'));
const circle = new zrender.Circle({
  shape: { cx: 150, cy: 50, r: 40 },
  style: { fill: 'none', stroke: '#F00' }
});
zr.add(circle);"""
            },
            {
                "name": "Curtains.js",
                "folder": "Curtains.js",
                "aliases": ["curtainsjs"],
                "url": "https://www.curtainsjs.com",
                "npm": "npm install curtainsjs",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/curtainsjs/8.1.5/curtains.min.js"></script>',
                "summary": "Lightweight WebGL library that converts HTML DOM elements into interactive 3D textured planes.",
                "snippet": """const curtains = new Curtains({ container: "canvas" });
const planeElement = document.getElementsByClassName("plane")[0];
const plane = new Plane(curtains, planeElement);"""
            },
            {
                "name": "OGL",
                "folder": "OGL",
                "aliases": ["ogl"],
                "url": "https://github.com/oframe/ogl",
                "npm": "npm install ogl",
                "cdn": '<script type="module">import { Renderer } from "https://unpkg.com/ogl";</script>',
                "summary": "Minimal, high-performance WebGL library designed for creative coders who master GLSL shaders.",
                "snippet": """import { Renderer, Camera, Transform, Program, Mesh, Box } from 'ogl';
const renderer = new Renderer();
document.body.appendChild(renderer.gl.canvas);
const scene = new Transform();
// Clean shader program setup..."""
            }
        ],
        "Math, Physics & Interactive Science": [
            {
                "name": "MathJax",
                "folder": "MathJax",
                "aliases": ["mathjax"],
                "url": "https://www.mathjax.org",
                "npm": "npm install mathjax",
                "cdn": '<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>',
                "summary": "Beautiful, accessible math typesetting in all browsers supporting LaTeX, MathML, and AsciiMath.",
                "snippet": """<p>When \\(a \\ne 0\\), there are two solutions to \\(ax^2 + bx + c = 0\\) and they are</p>
<p>$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$$</p>"""
            },
            {
                "name": "KaTeX",
                "folder": "KaTeX",
                "aliases": ["katex"],
                "url": "https://katex.org",
                "npm": "npm install katex",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>',
                "summary": "The fastest math typesetting library for the web, built by Khan Academy with zero dependencies.",
                "snippet": """katex.render("c = \\\\pm\\\\sqrt{a^2 + b^2}", element, {
  throwOnError: false
});"""
            },
            {
                "name": "FunctionPlot.js",
                "folder": "FunctionPlot.js",
                "aliases": ["function-plot"],
                "url": "https://mauriciopoppe.github.io/function-plot/",
                "npm": "npm install function-plot",
                "cdn": '<script src="https://unpkg.com/function-plot/dist/function-plot.js"></script>',
                "summary": "2D function plotter powered by D3 for mathematical curves, derivatives, and bounding equations.",
                "snippet": """functionPlot({
  target: '#root',
  data: [{ fn: 'x^2' }]
});"""
            },
            {
                "name": "math.js",
                "folder": "math.js",
                "aliases": ["mathjs"],
                "url": "https://mathjs.org",
                "npm": "npm install mathjs",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/12.4.0/math.js"></script>',
                "summary": "Extensive math library for JavaScript and Node.js with symbolic computation, matrices, and unit parsing.",
                "snippet": """const ans = math.evaluate('12 / (2.3 + 0.7)');
const d = math.derivative('x^2 + x', 'x');
console.log(d.toString()); // 2 * x + 1"""
            },
            {
                "name": "3Dmol.js",
                "folder": "3Dmol.js",
                "aliases": ["3dmol"],
                "url": "https://3dmol.csb.pitt.edu",
                "npm": "npm install 3dmol",
                "cdn": '<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>',
                "summary": "Object-oriented, WebGL-based molecular visualization library for proteins and chemical structures.",
                "snippet": """let viewer = $3Dmol.createViewer("gldiv", {});
viewer.addModel("ATOM      1  N   ASP A   1      27.282  15.225  37.994  1.00 24.97           N", "pdb");
viewer.setStyle({}, {stick: {}});
viewer.render();"""
            },
            {
                "name": "NGL Viewer",
                "folder": "NGL Viewer",
                "aliases": ["ngl"],
                "url": "https://nglviewer.org/ngl/",
                "npm": "npm install ngl",
                "cdn": '<script src="https://unpkg.com/ngl"></script>',
                "summary": "WebGL-based molecular viewer for large macromolecular structures, cryo-EM densities, and trajectories.",
                "snippet": """const stage = new NGL.Stage("viewport");
stage.loadFile("rcsb://1crn").then(function (o) {
  o.addRepresentation("cartoon");
  o.autoView();
});"""
            },
            {
                "name": "Matter.js",
                "folder": "Matter.js",
                "aliases": ["matterjs"],
                "url": "https://brm.io/matter-js/",
                "npm": "npm install matter-js",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>',
                "summary": "2D rigid body physics engine for the web featuring collision detection, restitution, and constraints.",
                "snippet": """const { Engine, Render, Runner, Bodies, Composite } = Matter;
const engine = Engine.create();
const render = Render.create({ element: document.body, engine: engine });
const box = Bodies.rectangle(400, 200, 80, 80);
const ground = Bodies.rectangle(400, 610, 810, 60, { isStatic: true });
Composite.add(engine.world, [box, ground]);
Render.run(render);
Runner.run(Runner.create(), engine);"""
            },
            {
                "name": "Cannon.js",
                "folder": "Cannon.js",
                "aliases": ["cannon", "cannon-es"],
                "url": "https://pmndrs.github.io/cannon-es/",
                "npm": "npm install cannon-es",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/cannon-es/dist/cannon-es.js"></script>',
                "summary": "Lightweight 3D physics engine for JavaScript, frequently paired with Three.js.",
                "snippet": """import * as CANNON from 'cannon-es';
const world = new CANNON.World({ gravity: new CANNON.Vec3(0, -9.82, 0) });
const body = new CANNON.Body({ mass: 5, shape: new CANNON.Sphere(1) });
world.addBody(body);"""
            },
            {
                "name": "Rapier.js",
                "folder": "Rapier.js",
                "aliases": ["rapier"],
                "url": "https://rapier.rs",
                "npm": "npm install @dimforge/rapier2d @dimforge/rapier3d",
                "cdn": "WebAssembly package via npm",
                "summary": "Fast, cross-platform 2D and 3D physics engine written in Rust and compiled to WebAssembly.",
                "snippet": """import('@dimforge/rapier2d').then(RAPIER => {
  let gravity = { x: 0.0, y: -9.81 };
  let world = new RAPIER.World(gravity);
});"""
            },
            {
                "name": "Box2D.js",
                "folder": "Box2D.js",
                "aliases": ["box2d"],
                "url": "https://box2d.org",
                "npm": "npm install box2dweb",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/box2dweb/2.1.a-1/Box2dWeb-2.1.a.3.min.js"></script>',
                "summary": "JavaScript port of Erin Catto's celebrated 2D physics engine Box2D.",
                "snippet": """// Box2D world creation and stepping logic"""
            },
            {
                "name": "Tone.js",
                "folder": "Tone.js",
                "aliases": ["tonejs"],
                "url": "https://tonejs.github.io",
                "npm": "npm install tone",
                "cdn": '<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>',
                "summary": "Web Audio framework for creating interactive music, synthesizers, and audio DSP in the browser.",
                "snippet": """const synth = new Tone.Synth().toDestination();
document.getElementById('play-btn').addEventListener('click', () => {
  Tone.start();
  synth.triggerAttackRelease("C4", "8n");
});"""
            },
            {
                "name": "Wavesurfer.js",
                "folder": "Wavesurfer.js",
                "aliases": ["wavesurfer"],
                "url": "https://wavesurfer.xyz",
                "npm": "npm install wavesurfer.js",
                "cdn": '<script src="https://unpkg.com/wavesurfer.js@7"></script>',
                "summary": "Interactive audio waveform visualizer built on the Web Audio API and HTML5 Canvas.",
                "snippet": """import WaveSurfer from 'wavesurfer.js';
const wavesurfer = WaveSurfer.create({
  container: '#waveform',
  waveColor: '#4F4A85',
  progressColor: '#383351',
  url: '/audio/track.mp3'
});"""
            }
        ],
        "Maps & Geospatial": [
            {
                "name": "Leaflet.js",
                "folder": "Leaflet.js",
                "aliases": ["leaflet"],
                "url": "https://leafletjs.com",
                "npm": "npm install leaflet",
                "cdn": '<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" /><script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>',
                "summary": "The leading open-source JavaScript library for mobile-friendly interactive mapping.",
                "snippet": """const map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
L.marker([51.5, -0.09]).addTo(map).bindPopup('A pretty CSS popup.').openPopup();"""
            },
            {
                "name": "Mapbox GL JS",
                "folder": "Mapbox GL JS",
                "aliases": ["mapbox-gl"],
                "url": "https://docs.mapbox.com/mapbox-gl-js/",
                "npm": "npm install mapbox-gl",
                "cdn": '<script src="https://api.mapbox.com/mapbox-gl-js/v3.2.0/mapbox-gl.js"></script>',
                "summary": "WebGL-based vector tile mapping library for fast, high-resolution interactive geographic displays.",
                "snippet": """mapboxgl.accessToken = 'YOUR_MAPBOX_ACCESS_TOKEN';
const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v12',
  center: [-74.5, 40],
  zoom: 9
});"""
            },
            {
                "name": "Deck.gl",
                "folder": "Deck.gl",
                "aliases": ["deckgl"],
                "url": "https://deck.gl",
                "npm": "npm install deck.gl @deck.gl/layers",
                "cdn": '<script src="https://unpkg.com/deck.gl@latest/dist.min.js"></script>',
                "summary": "WebGL2-powered framework for large-scale visual exploratory data analysis over geographic layers.",
                "snippet": """new deck.DeckGL({
  container: 'container',
  initialViewState: { longitude: -122.45, latitude: 37.8, zoom: 12 },
  controller: true,
  layers: [
    new deck.ScatterplotLayer({
      data: [{position: [-122.45, 37.8], size: 100}],
      getColor: [255, 0, 0],
      getRadius: d => d.size
    })
  ]
});"""
            },
            {
                "name": "CesiumJS",
                "folder": "CesiumJS",
                "aliases": ["cesium"],
                "url": "https://cesium.com/platform/cesiumjs/",
                "npm": "npm install cesium",
                "cdn": '<script src="https://cesium.com/downloads/cesiumjs/releases/1.115/Build/Cesium/Cesium.js"></script>',
                "summary": "Open-source JavaScript platform for creating 3D globes and 2D maps with dynamic WGS84 terrain.",
                "snippet": """const viewer = new Cesium.Viewer('cesiumContainer', {
  terrainProvider: Cesium.createWorldTerrain()
});"""
            },
            {
                "name": "OpenLayers",
                "folder": "OpenLayers",
                "aliases": ["openlayers", "ol"],
                "url": "https://openlayers.org",
                "npm": "npm install ol",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/ol@v9.1.0/dist/ol.js"></script>',
                "summary": "High-performance, feature-packed library for displaying dynamic map data from OGC, WMS, and GeoJSON.",
                "snippet": """import Map from 'ol/Map.js';
import View from 'ol/View.js';
import TileLayer from 'ol/layer/Tile.js';
import OSM from 'ol/source/OSM.js';
const map = new Map({
  target: 'map',
  layers: [new TileLayer({ source: new OSM() })],
  view: new View({ center: [0, 0], zoom: 2 })
});"""
            },
            {
                "name": "Kepler.gl",
                "folder": "Kepler.gl",
                "aliases": ["keplergl"],
                "url": "https://kepler.gl",
                "npm": "npm install @kepler.gl/components",
                "cdn": "Bundled via npm / React",
                "summary": "Data-agnostic, high-performance web-based application for geospatial visual analysis (built on Deck.gl).",
                "snippet": """import KeplerGl from '@kepler.gl/components';
const Map = () => <KeplerGl id="foo" mapboxApiAccessToken="YOUR_TOKEN" width={800} height={600} />;"""
            },
            {
                "name": "Tangram",
                "folder": "Tangram",
                "aliases": ["tangram"],
                "url": "https://github.com/tangrams/tangram",
                "npm": "npm install tangram",
                "cdn": '<script src="https://unpkg.com/tangram/dist/tangram.min.js"></script>',
                "summary": "Flexible 2D/3D map engine designed for real-time rendering of OpenStreetMap vector data with OpenGL.",
                "snippet": """const map = L.map('map');
const layer = Tangram.leafletLayer({ scene: 'scene.yaml' });
layer.addTo(map);"""
            },
            {
                "name": "Turf.js",
                "folder": "Turf.js",
                "aliases": ["turf"],
                "url": "https://turfjs.org",
                "npm": "npm install @turf/turf",
                "cdn": '<script src="https://cdn.jsdelivr.net/npm/@turf/turf@6/turf.min.js"></script>',
                "summary": "Advanced geospatial analysis engine for browsers and Node.js implementing GeoJSON algorithms.",
                "snippet": """const pt1 = turf.point([-75.343, 39.984]);
const pt2 = turf.point([-75.534, 39.123]);
const distance = turf.distance(pt1, pt2, { units: 'miles' });
console.log(`Distance: ${distance} miles`);"""
            }
        ]
    },
    "Python Visualization, Graphical, & Interactive Libraries": {
        "Statistical, Charting & Core Plotting": [
            {
                "name": "Matplotlib",
                "folder": "Matplotlib",
                "aliases": ["matplotlib"],
                "url": "https://matplotlib.org",
                "pip": "pip install matplotlib",
                "summary": "Comprehensive library for creating static, animated, and interactive visualizations in Python.",
                "snippet": """import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.figure(figsize=(8, 4))
plt.plot(x, np.sin(x), label='Sine Wave', color='#00e676')
plt.title('Matplotlib Starter')
plt.legend()
plt.savefig('plot.png')
plt.show()"""
            },
            {
                "name": "Seaborn",
                "folder": "Seaborn",
                "aliases": ["seaborn"],
                "url": "https://seaborn.pydata.org",
                "pip": "pip install seaborn",
                "summary": "Statistical data visualization based on Matplotlib providing high-level statistical chart themes.",
                "snippet": """import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set2")
plt.title("Seaborn Statistical Boxplot")
plt.show()"""
            },
            {
                "name": "Plotly Py (Plotly.py / Dash)",
                "folder": "Plotly Py (Plotly.py - Dash)",
                "aliases": ["Plotly Py", "Plotly.py", "Dash", "plotly"],
                "url": "https://plotly.com/python/",
                "pip": "pip install plotly dash",
                "summary": "Interactive graphing library and framework for analytical web applications in pure Python.",
                "snippet": """import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size='petal_length')
fig.write_html("plotly_scatter.html")
fig.show()"""
            },
            {
                "name": "Bokeh",
                "folder": "Bokeh",
                "aliases": ["bokeh"],
                "url": "https://bokeh.org",
                "pip": "pip install bokeh",
                "summary": "Interactive visualization library targeting modern web browsers for presentation in Jupyter and web apps.",
                "snippet": """from bokeh.plotting import figure, show
p = figure(title="Bokeh Basic Line", x_axis_label='x', y_axis_label='y')
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2, color="navy")
show(p)"""
            },
            {
                "name": "Altair",
                "folder": "Altair",
                "aliases": ["altair"],
                "url": "https://altair-viz.github.io",
                "pip": "pip install altair vega_datasets",
                "summary": "Declarative statistical visualization library for Python, based on Vega and Vega-Lite grammar.",
                "snippet": """import altair as alt
from vega_datasets import data
cars = data.cars()
chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).interactive()
chart.save('altair_chart.html')"""
            },
            {
                "name": "HoloViews",
                "folder": "HoloViews",
                "aliases": ["holoviews"],
                "url": "https://holoviews.org",
                "pip": "pip install holoviews",
                "summary": "High-level visualization library designed to make data analysis immediate, composable, and reproducible.",
                "snippet": """import numpy as np
import holoviews as hv
hv.extension('bokeh')
xs = np.linspace(0, np.pi*4, 100)
curve = hv.Curve((xs, np.sin(xs)), 'Time', 'Amplitude')
hv.save(curve, 'holoviews_curve.html')"""
            },
            {
                "name": "Pygal",
                "folder": "Pygal",
                "aliases": ["pygal"],
                "url": "https://www.pygal.org",
                "pip": "pip install pygal",
                "summary": "Sexy, pythonic SVG chart generator producing lightweight, resolution-independent vector graphics.",
                "snippet": """import pygal
bar_chart = pygal.Bar()
bar_chart.title = 'Quarterly Gross Revenue'
bar_chart.add('2023', [12, 19, 15, 25])
bar_chart.add('2024', [18, 24, 22, 31])
bar_chart.render_to_file('chart.svg')"""
            },
            {
                "name": "Plotnine (ggplot2 implementation)",
                "folder": "Plotnine (ggplot2 implementation)",
                "aliases": ["Plotnine", "plotnine"],
                "url": "https://plotnine.org",
                "pip": "pip install plotnine",
                "summary": "Grammar of graphics implementation for Python based closely on R's ggplot2.",
                "snippet": """from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars
p = (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm')
 + facet_wrap('~gear'))
p.save('plotnine_figure.png')"""
            },
            {
                "name": "Chartify",
                "folder": "Chartify",
                "aliases": ["chartify"],
                "url": "https://github.com/spotify/chartify",
                "pip": "pip install chartify",
                "summary": "Python library developed by Spotify making it straightforward for data scientists to create publication charts.",
                "snippet": """import chartify
ch = chartify.Chart(blank_labels=True, x_axis_type='categorical')
ch.set_title("Spotify Chartify Quickstart")
# Configure series and plot..."""
            },
            {
                "name": "HVPlot",
                "folder": "HVPlot",
                "aliases": ["hvplot"],
                "url": "https://hvplot.holoviz.org",
                "pip": "pip install hvplot",
                "summary": "High-level plotting API for pandas, dask, xarray, and polars built on top of HoloViews.",
                "snippet": """import pandas as pd
import hvplot.pandas
df = pd.DataFrame({'x': range(10), 'y': [i**2 for i in range(10)]})
plot = df.hvplot.line(x='x', y='y', title='hvPlot Line')
# Interactively renders in browser or notebook"""
            },
            {
                "name": "bqplot",
                "folder": "bqplot",
                "aliases": ["bqplot"],
                "url": "https://github.com/bqplot/bqplot",
                "pip": "pip install bqplot",
                "summary": "Interactive 2D plotting system for Jupyter Notebooks using ipywidgets and D3.js.",
                "snippet": """from bqplot import LinearScale, Lines, Figure, Axis
x_sc = LinearScale()
y_sc = LinearScale()
lines = Lines(x=[0, 1, 2, 3], y=[2, 4, 1, 5], scales={'x': x_sc, 'y': y_sc})
ax_x = Axis(scale=x_sc, label='Index')
ax_y = Axis(scale=y_sc, orientation='vertical', label='Value')
fig = Figure(marks=[lines], axes=[ax_x, ax_y], title='bqplot in Jupyter')"""
            },
            {
                "name": "Leather",
                "folder": "Leather",
                "aliases": ["leather"],
                "url": "https://leather.readthedocs.io",
                "pip": "pip install leather",
                "summary": "Python charting library designed for zero friction, fast SVG generation with no heavy dependencies.",
                "snippet": """import leather
chart = leather.Chart('Simple Dots')
chart.add_dots([(1, 2), (2, 4), (3, 6)])
chart.to_svg('dots.svg')"""
            },
            {
                "name": "Veusz",
                "folder": "Veusz",
                "aliases": ["veusz"],
                "url": "https://veusz.github.io",
                "pip": "pip install veusz",
                "summary": "GUI and Python scientific plotting package designed for producing publication-ready EPS and PDF figures.",
                "snippet": """import veusz.embed as veusz
embed = veusz.Embedded('window')
embed.To(embed.Root.Add('page'))
embed.To(embed.Current.Add('graph'))
# Add xy plots with scientific error bars..."""
            },
            {
                "name": "GR Framework",
                "folder": "GR Framework",
                "aliases": ["gr"],
                "url": "https://gr-framework.org",
                "pip": "pip install gr",
                "summary": "Universal visualization framework with ultra-fast rendering engines supporting real-time data feeds.",
                "snippet": """from gr.pygr import plot
import numpy as np
x = np.linspace(-2, 2, 40)
plot(x, x**3 - x)"""
            },
            {
                "name": "Visvis",
                "folder": "Visvis",
                "aliases": ["visvis"],
                "url": "https://github.com/almarklein/visvis",
                "pip": "pip install visvis",
                "summary": "Pure Python library for 1D, 2D, 3D, and 4D data visualization using OpenGL.",
                "snippet": """import visvis as vv
vv.plot([1, 2, 3, 1, 4, 2])
vv.title('Visvis Basic Plot')
app = vv.use()
app.Run()"""
            },
            {
                "name": "Chaco",
                "folder": "Chaco",
                "aliases": ["chaco"],
                "url": "https://github.com/enthought/chaco",
                "pip": "pip install chaco traitsui",
                "summary": "Interactive 2D plotting toolkit by Enthought for complex visualization applications and desktop GUIs.",
                "snippet": """from chaco.api import Plot, ArrayPlotData
from traits.api import HasTraits, Instance
# Production Trait-based application architecture"""
            }
        ],
        "3D, High-Performance & Scientific Graphics": [
            {
                "name": "Datashader",
                "folder": "Datashader",
                "aliases": ["datashader"],
                "url": "https://datashader.org",
                "pip": "pip install datashader",
                "summary": "Graphics pipeline system for synthesizing meaningful representations from billions of raw data points.",
                "snippet": """import datashader as ds
import pandas as pd
import numpy as np

df = pd.DataFrame({'x': np.random.normal(size=1000000), 'y': np.random.normal(size=1000000)})
cvs = ds.Canvas(plot_width=400, plot_height=400)
agg = cvs.points(df, 'x', 'y')
img = ds.transfer_functions.shade(agg)
img.to_pil().save('datashader_output.png')"""
            },
            {
                "name": "Mayavi",
                "folder": "Mayavi",
                "aliases": ["mayavi"],
                "url": "https://docs.enthought.com/mayavi/mayavi/",
                "pip": "pip install mayavi PyQt5",
                "summary": "3D scientific data visualization and plotting in Python powered by VTK and traits.",
                "snippet": """from mayavi import mlab
import numpy as np
x, y = np.mgrid[-3:3:100j, -3:3:100j]
z = np.sin(x**2 + y**2)
mlab.surf(x, y, z)
mlab.savefig('mayavi_surface.png')"""
            },
            {
                "name": "VisPy",
                "folder": "VisPy",
                "aliases": ["vispy"],
                "url": "https://vispy.org",
                "pip": "pip install vispy",
                "summary": "High-performance interactive 2D/3D data visualization library leveraging modern OpenGL shaders.",
                "snippet": """from vispy import scene
import numpy as np

canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()
scatter = scene.visuals.Markers()
scatter.set_data(np.random.normal(size=(500, 3)), edge_color=None, face_color=(1, 1, 0, .5), size=5)
view.add(scatter)
view.camera = 'turntable'"""
            },
            {
                "name": "PyQtGraph",
                "folder": "PyQtGraph",
                "aliases": ["pyqtgraph"],
                "url": "https://www.pyqtgraph.org",
                "pip": "pip install pyqtgraph PyQt6",
                "summary": "Fast data visualization and GUI library tailored for high-speed scientific and engineering instrumentation.",
                "snippet": """import pyqtgraph as pg
import numpy as np

app = pg.mkQApp("Plotting App")
win = pg.plot()
win.setWindowTitle('High-Speed Oscilloscope')
data = np.random.normal(size=10000)
win.plot(data, pen='g')
pg.exec()"""
            },
            {
                "name": "VTK (Python bindings)",
                "folder": "VTK (Python bindings)",
                "aliases": ["VTK", "vtk"],
                "url": "https://vtk.org",
                "pip": "pip install vtk",
                "summary": "Visualization Toolkit: world-renowned C++/Python engine for 3D graphics, volumetric processing, and CAD.",
                "snippet": """import vtk
cylinder = vtk.vtkCylinderSource()
cylinder.SetResolution(8)
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cylinder.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)"""
            },
            {
                "name": "Glumpy",
                "folder": "Glumpy",
                "aliases": ["glumpy"],
                "url": "https://glumpy.github.io",
                "pip": "pip install glumpy",
                "summary": "Scientific visualization library based on OpenGL and NumPy for fast shader-driven rendering.",
                "snippet": """from glumpy import app, gloo, gl
vertex = \"\"\"attribute vec2 position; void main() { gl_Position = vec4(position, 0.0, 1.0); }\"\"\"
fragment = \"\"\"void main() { gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); }\"\"\"
window = app.Window()
program = gloo.Program(vertex, fragment, count=4)
# Run glumpy event loop..."""
            },
            {
                "name": "Manim (Mathematical Animation Engine)",
                "folder": "Manim (Mathematical Animation Engine)",
                "aliases": ["Manim", "manim", "manimce"],
                "url": "https://www.manim.community",
                "pip": "pip install manim",
                "summary": "Animation engine for explanatory math and science videos created by Grant Sanderson (3Blue1Brown).",
                "snippet": """from manim import *
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))"""
            },
            {
                "name": "PyVista",
                "folder": "PyVista",
                "aliases": ["pyvista"],
                "url": "https://www.pyvista.org",
                "pip": "pip install pyvista",
                "summary": "3D plotting and spatial mesh analysis through a streamlined, Pythonic interface to VTK.",
                "snippet": """import pyvista as pv
mesh = pv.Sphere()
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh, color='turquoise', show_edges=True)
plotter.screenshot('pyvista_sphere.png')"""
            }
        ],
        "Diagrams, Graph Networks & Schematics": [
            {
                "name": "NetworkX",
                "folder": "NetworkX",
                "aliases": ["networkx"],
                "url": "https://networkx.org",
                "pip": "pip install networkx",
                "summary": "Comprehensive Python package for the creation, manipulation, and study of complex network structures.",
                "snippet": """import networkx as nx
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(n=30, p=0.15, seed=42)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, node_color='#00e676', edge_color='#444', with_labels=True)
plt.savefig('networkx_graph.png')"""
            },
            {
                "name": "PyVis",
                "folder": "PyVis",
                "aliases": ["pyvis"],
                "url": "https://pyvis.readthedocs.io",
                "pip": "pip install pyvis",
                "summary": "Python library for quick, interactive network graph visualizations using Vis.js under the hood.",
                "snippet": """from pyvis.network import Network
net = Network(notebook=False)
net.add_node(1, label="Node 1")
net.add_node(2, label="Node 2")
net.add_edge(1, 2)
net.save_graph("pyvis_network.html")"""
            },
            {
                "name": "Diagrams (diagrams as code)",
                "folder": "Diagrams (diagrams as code)",
                "aliases": ["Diagrams", "diagrams"],
                "url": "https://diagrams.mingrammer.com",
                "pip": "pip install diagrams",
                "summary": "Diagram as Code: prototype and document cloud system architectures in pure Python scripts.",
                "snippet": """from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service Architecture", show=False, filename="aws_arch"):
    ELB("lb") >> EC2("web") >> RDS("userdb")"""
            },
            {
                "name": "SchemDraw",
                "folder": "SchemDraw",
                "aliases": ["schemdraw"],
                "url": "https://schemdraw.readthedocs.io",
                "pip": "pip install schemdraw",
                "summary": "Python package for producing publication-quality electrical circuit diagrams and schematics.",
                "snippet": """import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(file='schematic.png') as d:
    d += elm.Battery().up().label('10V')
    d += elm.Resistor().right().label('100kΩ')
    d += elm.Capacitor().down().label('0.1µF')
    d += elm.Line().left()"""
            },
            {
                "name": "Graphviz (Python interface)",
                "folder": "Graphviz (Python interface)",
                "aliases": ["Graphviz", "graphviz"],
                "url": "https://graphviz.readthedocs.io",
                "pip": "pip install graphviz",
                "summary": "Python interface to the Graphviz graph layout engine with DOT language support.",
                "snippet": """import graphviz
dot = graphviz.Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.render('round_table', format='png', cleanup=True)"""
            },
            {
                "name": "DNA Features Viewer",
                "folder": "DNA Features Viewer",
                "aliases": ["dna_features_viewer"],
                "url": "https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer",
                "pip": "pip install dna_features_viewer",
                "summary": "Python library to visualize DNA features and genomic sequence annotations clearly.",
                "snippet": """from dna_features_viewer import GraphicFeature, GraphicRecord
record = GraphicRecord(sequence_length=1000, features=[
    GraphicFeature(start=20, end=500, strand=+1, color="#ffd700", label="Gene A"),
    GraphicFeature(start=400, end=700, strand=-1, color="#ffcccc", label="Gene B")
])
ax, _ = record.plot(figure_width=5)
ax.figure.savefig("dna_features.png")"""
            },
            {
                "name": "diaGrabber",
                "folder": "diaGrabber",
                "aliases": ["diagrabber"],
                "url": "https://github.com/search?q=diaGrabber",
                "pip": "pip install git+https://github.com/...",
                "summary": "Diagram extraction and vector schematic processing tool for engineering documentation.",
                "snippet": """# diaGrabber schematic integration module"""
            }
        ],
        "Geospatial & Mapping": [
            {
                "name": "Folium",
                "folder": "Folium",
                "aliases": ["folium"],
                "url": "https://python-visualization.github.io/folium/",
                "pip": "pip install folium",
                "summary": "Python library for visualizing geospatial data on interactive Leaflet maps with marker clusters.",
                "snippet": """import folium
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
folium.Marker([45.5236, -122.6750], popup="Portland").addTo(m)
m.save("folium_map.html")"""
            },
            {
                "name": "GeoPandas",
                "folder": "GeoPandas",
                "aliases": ["geopandas"],
                "url": "https://geopandas.org",
                "pip": "pip install geopandas",
                "summary": "Extends pandas data types to allow spatial operations on geometric types using Shapely.",
                "snippet": """import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot(column='pop_est', legend=True, cmap='viridis')
plt.savefig('world_population.png')"""
            },
            {
                "name": "Cartopy",
                "folder": "Cartopy",
                "aliases": ["cartopy"],
                "url": "https://scitools.org.uk/cartopy/docs/latest/",
                "pip": "pip install cartopy",
                "summary": "Python package designed for geospatial data processing and cartographic map projections.",
                "snippet": """import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()
plt.savefig('cartopy_globe.png')"""
            },
            {
                "name": "Geoplotlib",
                "folder": "Geoplotlib",
                "aliases": ["geoplotlib"],
                "url": "https://github.com/andrea-cuttone/geoplotlib",
                "pip": "pip install geoplotlib",
                "summary": "Python toolbox for visualizing geographical data, creating dot maps, kernel density, and spatial graphs.",
                "snippet": """import geoplotlib
# geoplotlib.dot(data)
# geoplotlib.show()"""
            },
            {
                "name": "Pydeck (Deck.gl wrapper)",
                "folder": "Pydeck (Deck.gl wrapper)",
                "aliases": ["Pydeck", "pydeck"],
                "url": "https://deckgl.readthedocs.io",
                "pip": "pip install pydeck",
                "summary": "High-scale spatial data visualization in Python powered by Deck.gl and WebGL2.",
                "snippet": """import pydeck as pdk
layer = pdk.Layer(
    "HexagonLayer",
    data="https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv",
    get_position="[lng, lat]",
    radius=1000,
    elevation_scale=50,
    extruded=True
)
view_state = pdk.ViewState(latitude=37.77, longitude=-122.4, zoom=11, pitch=50)
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.to_html("pydeck_hex.html")"""
            },
            {
                "name": "Mapclassify",
                "folder": "Mapclassify",
                "aliases": ["mapclassify"],
                "url": "https://pysal.org/mapclassify/",
                "pip": "pip install mapclassify",
                "summary": "Classification schemes for choropleth mapping and spatial data analysis (Fisher-Jenks, Quantiles).",
                "snippet": """import mapclassify
import numpy as np
data = np.random.exponential(scale=10, size=1000)
classifier = mapclassify.NaturalBreaks(data, k=5)
print(classifier)"""
            }
        ],
        "Interactive Dashboards & Web Apps": [
            {
                "name": "Streamlit",
                "folder": "Streamlit",
                "aliases": ["streamlit"],
                "url": "https://streamlit.io",
                "pip": "pip install streamlit",
                "summary": "Turn Python data scripts into shareable, reactive web applications in minutes with zero frontend code.",
                "snippet": """import streamlit as st
import numpy as np

st.title("Streamlit Dashboard")
x = st.slider("Select value", 0, 100, 25)
st.write(f"The square of {x} is {x**2}")
st.line_chart(np.random.randn(20, 3))"""
            },
            {
                "name": "Gradio",
                "folder": "Gradio",
                "aliases": ["gradio"],
                "url": "https://www.gradio.app",
                "pip": "pip install gradio",
                "summary": "Build and share machine learning demos, LLM user interfaces, and interactive web tools effortlessly.",
                "snippet": """import gradio as gr

def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
# demo.launch()"""
            },
            {
                "name": "Panel",
                "folder": "Panel",
                "aliases": ["panel"],
                "url": "https://panel.holoviz.org",
                "pip": "pip install panel",
                "summary": "Powerful data exploration and dashboarding toolkit for Python connecting to any plotting ecosystem.",
                "snippet": """import panel as pn
pn.extension()
slider = pn.widgets.IntSlider(name='Select', start=0, end=100)
pane = pn.pane.Markdown(slider.param.value)
pn.Row(slider, pane).servable()"""
            },
            {
                "name": "Taipy",
                "folder": "Taipy",
                "aliases": ["taipy"],
                "url": "https://www.taipy.io",
                "pip": "pip install taipy",
                "summary": "Enterprise-ready Python application framework for interactive GUIs and complex data pipelines.",
                "snippet": """from taipy.gui import Gui
page = \"\"\"
# Taipy Interactive Dashboard
<|{value}|slider|min=0|max=100|>
<|{value}|text|>
\"\"\"
value = 50
Gui(page=page).run(dark_mode=True)"""
            },
            {
                "name": "Reflex",
                "folder": "Reflex",
                "aliases": ["reflex", "pynecone"],
                "url": "https://reflex.dev",
                "pip": "pip install reflex",
                "summary": "Open-source full-stack framework for building web applications in pure Python (formerly Pynecone).",
                "snippet": """import reflex as rx

class State(rx.State):
    count: int = 0
    def increment(self):
        self.count += 1

def index():
    return rx.vstack(
        rx.heading(State.count),
        rx.button("Increment", on_click=State.increment)
    )

app = rx.App()
app.add_page(index)"""
            },
            {
                "name": "Gleam",
                "folder": "Gleam",
                "aliases": ["gleam"],
                "url": "https://github.com/dgrtwo/gleam",
                "pip": "pip install gleam",
                "summary": "Python package for building interactive web applications inspired by R's Shiny.",
                "snippet": """from gleam import Page, panels
# Lightweight Shiny-style reactive Python dashboards"""
            },
            {
                "name": "Anvil",
                "folder": "Anvil",
                "aliases": ["anvil"],
                "url": "https://anvil.works",
                "pip": "pip install anvil-uplink",
                "summary": "Full-stack web applications with nothing but Python, drag-and-drop designer, and client-server RPC.",
                "snippet": """import anvil.server
anvil.server.connect("YOUR_UPLINK_KEY")
@anvil.server.callable
def process_data(value):
    return f"Computed: {value * 2}"
anvil.server.wait_forever()"""
            },
            {
                "name": "Solara",
                "folder": "Solara",
                "aliases": ["solara"],
                "url": "https://solara.dev",
                "pip": "pip install solara",
                "summary": "Pure Python, reactive web framework for data apps built on ipywidgets and React-like hooks.",
                "snippet": """import solara

@solara.component
def Page():
    count, set_count = solara.use_state(0)
    solara.Button(label=f"Clicks: {count}", on_click=lambda: set_count(count + 1))"""
            }
        ]
    }
}


def build_structure():
    total_tools = 0
    total_categories = 0
    created_dirs = []

    print(f"[INFO] Setting up visualization directory hierarchy under:\\n  {BASE_DIR}\\n")

    for ecosystem, categories in DATA.items():
        eco_path = os.path.join(BASE_DIR, ecosystem)
        os.makedirs(eco_path, exist_ok=True)
        created_dirs.append(eco_path)
        print(f"[+] Ecosystem directory: {ecosystem}")

        # Ecosystem README
        eco_readme_path = os.path.join(eco_path, "README.md")
        eco_readme_lines = [
            f"# {ecosystem}",
            "",
            f"Comprehensive catalog of visualization, graphical, and interactive libraries.",
            "",
            "## Categories:",
            ""
        ]

        for cat_name, tools in categories.items():
            total_categories += 1
            cat_path = os.path.join(eco_path, cat_name)
            os.makedirs(cat_path, exist_ok=True)
            created_dirs.append(cat_path)
            print(f"  ├── Category: {cat_name} ({len(tools)} tools)")

            eco_readme_lines.append(f"### [{cat_name}](./{cat_name.replace(' ', '%20')}/)")
            eco_readme_lines.append(f"- **Count:** {len(tools)} libraries")
            tool_names = ", ".join([f"[{t['name']}](./{cat_name.replace(' ', '%20')}/{t['folder'].replace(' ', '%20')}/)" for t in tools])
            eco_readme_lines.append(f"- **Tools:** {tool_names}")
            eco_readme_lines.append("")

            # Category README
            cat_readme_lines = [
                f"# {cat_name}",
                f"**Ecosystem:** [{ecosystem}](../)",
                "",
                f"This category contains **{len(tools)}** production-grade frameworks and libraries.",
                "",
                "| Library / Tool | Focus / Description | Official Link | Subdirectory |",
                "| :--- | :--- | :--- | :--- |"
            ]

            for tool in tools:
                total_tools += 1
                tool_path = os.path.join(cat_path, tool["folder"])
                os.makedirs(tool_path, exist_ok=True)
                created_dirs.append(tool_path)

                cat_readme_lines.append(
                    f"| **{tool['name']}** | {tool['summary']} | [Website]({tool['url']}) | [`./{tool['folder']}/`](./{tool['folder'].replace(' ', '%20')}/) |"
                )

                # Tool README
                tool_readme_lines = [
                    f"# {tool['name']}",
                    f"**Category:** [{cat_name}](../)",
                    f"**Ecosystem:** [{ecosystem}](../../)",
                    "",
                    f"## Overview",
                    f"{tool['summary']}",
                    "",
                    f"## Official Resources",
                    f"- **Website / Documentation:** [{tool['url']}]({tool['url']})",
                    ""
                ]

                if "npm" in tool:
                    tool_readme_lines.extend([
                        "## Installation & Setup",
                        "```bash",
                        tool["npm"],
                        "```",
                        ""
                    ])
                if "cdn" in tool:
                    tool_readme_lines.extend([
                        "### CDN Embed:",
                        "```html",
                        tool["cdn"],
                        "```",
                        ""
                    ])
                if "pip" in tool:
                    tool_readme_lines.extend([
                        "## Installation & Setup",
                        "```bash",
                        tool["pip"],
                        "```",
                        ""
                    ])

                code_lang = "html" if "JavaScript" in ecosystem and ("<script" in tool.get("snippet", "") or "<p>" in tool.get("snippet", "")) else ("javascript" if "JavaScript" in ecosystem else "python")
                tool_readme_lines.extend([
                    "## Starter / Hello World Example",
                    f"```{code_lang}",
                    tool["snippet"],
                    "```",
                    ""
                ])

                with open(os.path.join(tool_path, "README.md"), "w", encoding="utf-8") as f:
                    f.write("\n".join(tool_readme_lines))

                # Create aliases / symlinks if needed
                for alias in tool.get("aliases", []):
                    if alias != tool["folder"]:
                        alias_path = os.path.join(cat_path, alias)
                        if not os.path.exists(alias_path):
                            try:
                                os.symlink(tool["folder"], alias_path)
                            except OSError:
                                pass

            with open(os.path.join(cat_path, "README.md"), "w", encoding="utf-8") as f:
                f.write("\n".join(cat_readme_lines))

        with open(eco_readme_path, "w", encoding="utf-8") as f:
            f.write("\n".join(eco_readme_lines))

    # Also create convenient short symlinks at root:
    # JavaScript -> JavaScript Visualization, Graphical, & Interactive Libraries
    # Python -> Python Visualization, Graphical, & Interactive Libraries
    symlinks = {
        "JavaScript": "JavaScript Visualization, Graphical, & Interactive Libraries",
        "Python": "Python Visualization, Graphical, & Interactive Libraries"
    }
    for short_name, full_name in symlinks.items():
        sym_path = os.path.join(BASE_DIR, short_name)
        if not os.path.exists(sym_path):
            try:
                os.symlink(full_name, sym_path)
                print(f"[+] Created convenient root symlink: {short_name} -> {full_name}")
            except OSError:
                pass

    # Create root master catalog README update or append
    print(f"\n[SUCCESS] Successfully created:")
    print(f"  - 2 Ecosystem Master Directories")
    print(f"  - {total_categories} Category Subdirectories")
    print(f"  - {total_tools} Framework & Tool Subdirectories")
    print(f"  - Complete documentation, install guides, and code snippets in all subdirectories.")


if __name__ == "__main__":
    build_structure()
