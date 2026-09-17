"""
Category 5: Interactive Dashboards & Web Apps (8 tools)
Contains authentic paradigms, production Python scripts, mathematical specs, and metrics.
"""

PEERS_CAT5 = [
    {"name": "Streamlit", "paradigm": "Reactive Top-to-Bottom Execution", "engine": "Tornado / React Virtual DOM", "scale": "High (Cached Data)", "interactivity": "Widget State Re-execution", "learning_curve": "Minimal"},
    {"name": "Gradio", "paradigm": "Machine Learning Interface Blocks", "engine": "FastAPI / Svelte Components", "scale": "Real-time Model Inference", "interactivity": "Input/Output Binding", "learning_curve": "Very Low"},
    {"name": "Panel", "paradigm": "Flexible Param / PyViz Reactive Engine", "engine": "Bokeh Server / Tornado", "scale": "Large Data / Dynamic Streams", "interactivity": "Bi-directional WebSocket", "learning_curve": "Moderate"},
    {"name": "Taipy", "paradigm": "Enterprise Pipeline & Scenario GUI", "engine": "Flask / React Custom Engine", "scale": "Enterprise Big Data", "interactivity": "Multi-scenario Comparison", "learning_curve": "Moderate"},
    {"name": "Reflex", "paradigm": "Pure Python Full-Stack (React Compiler)", "engine": "FastAPI + Next.js / React", "scale": "Full-Stack Web App", "interactivity": "Event Handlers / WebSockets", "learning_curve": "Moderate"},
    {"name": "Gleam", "paradigm": "Shiny-Inspired Declarative Dashboard", "engine": "Python Web / WTForms", "scale": "Small to Medium", "interactivity": "Form Submit / Reactive", "learning_curve": "Low"},
    {"name": "Anvil", "paradigm": "Full-Stack Web Apps in Pure Python", "engine": "Anvil Cloud / Skulpt Py", "scale": "Cloud Hosted Full-Stack", "interactivity": "Client-Server RPC Events", "learning_curve": "Low"},
    {"name": "Solara", "paradigm": "React-like Pure Python Virtual DOM", "engine": "ipywidgets / React Wrapper", "scale": "Fast Hot-Reloading", "interactivity": "Hooks (use_state, use_effect)", "learning_curve": "Moderate"}
]

TOOLS_CAT5 = [
    {
        "name": "Streamlit",
        "category": "Interactive Dashboards & Web Apps",
        "folder": "Streamlit",
        "pip": "pip install streamlit pandas numpy",
        "docs": "https://streamlit.io",
        "license": "Apache 2.0",
        "tagline": "The fastest way to build and share data-driven web applications in pure Python.",
        "peers": PEERS_CAT5,
        "paradigms": [
            {
                "tag": "01 / REACTIVE SCRIPT EXECUTION",
                "title": "Reactive State Machine & `@st.cache_data` Memoization",
                "subtitle": "Treats scripts as pure reactive functions: user interactions re-run the script top-to-bottom with intelligent cache hashing.",
                "math_desc": "Pure functional memoization with cryptographic AST hashing: $\\text{Output} = f(\\text{State})$ where $f$ is re-evaluated only on dirty state inputs.",
                "math_formula": "\\mathcal{H}(\\text{code}) = \\text{SHA256}(\\text{AST}(f) \\parallel \\text{Args}), \\quad \\text{CacheHit} \\implies \\text{O}(1)",
                "time_complexity": "O(N) script rerun; O(1) on cache hits",
                "space_complexity": "O(M) in-memory session cache",
                "enterprise_use": "Executive AI portfolio monitoring dashboards, rapid generative AI prototyping, risk simulation tools.",
                "strengths": "Zero HTML/CSS/JS knowledge required; converts linear Python scripts directly into modern web applications.",
                "tradeoffs": "Top-to-bottom re-execution paradigm can lead to redundant compute without strict caching discipline.",
                "metrics": [
                    {"label": "Execution", "val": "Top-to-Bottom", "sub": "Pure Reactive"},
                    {"label": "Caching", "val": "@st.cache_data", "sub": "AST Hash Memo"},
                    {"label": "Components", "val": "React Wrappers", "sub": "Two-Way Bridge"},
                    {"label": "Deployment", "val": "Streamlit Cloud", "sub": "Docker / K8s Ready"}
                ],
                "code": """import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Commercial Revenue Governance", layout="wide")

@st.cache_data
def load_data(n_samples):
    dates = pd.date_range("2026-01-01", periods=n_samples)
    return pd.DataFrame({
        "Direct_Bookings": np.cumsum(np.random.normal(500, 50, n_samples)),
        "Commission_Recapture": np.cumsum(np.random.normal(120, 20, n_samples))
    }, index=dates)

st.title("Enterprise Commercial P&L Governance")
sample_slider = st.sidebar.slider("Sampling Horizon (Days)", 30, 365, n_samples)
df = load_data(sample_slider)

col1, col2 = st.columns(2)
col1.metric("Total Direct Revenue", f"${df['Direct_Bookings'].iloc[-1]:,.0f}", "+56%")
col2.metric("Commission Recaptured", f"${df['Commission_Recapture'].iloc[-1]:,.0f}", "+18%")

st.line_chart(df)"""
            }
        ]
    },
    {
        "name": "Gradio",
        "category": "Interactive Dashboards & Web Apps",
        "folder": "Gradio",
        "pip": "pip install gradio torch transformers",
        "docs": "https://www.gradio.app",
        "license": "Apache 2.0",
        "tagline": "Build and share delightful machine learning web apps and demos with minimal Python code.",
        "peers": PEERS_CAT5,
        "paradigms": [
            {
                "tag": "01 / ML MODEL PLAYGROUND",
                "title": "Machine Learning Model Interface Blocks & Real-Time Inpainting",
                "subtitle": "Declarative `gr.Blocks()` layouts connecting image, audio, and multimodal LLMs to interactive web widgets.",
                "math_desc": "Event-driven asynchronous prediction mapping: $\\mathbf{y} = \\mathcal{M}_{\\text{model}}(\\mathbf{x})$ over WebSockets.",
                "math_formula": "\\mathbf{y}_{\\text{pred}} = \\text{argmax}_{c} P(y=c \\mid \\mathbf{x}_{\\text{input}}; \\mathbf{\\theta})",
                "time_complexity": "O(M) model inference forward pass",
                "space_complexity": "O(B) batch payload memory",
                "enterprise_use": "Hugging Face model benchmarking demos, clinical diagnostic imaging model validation playgrounds.",
                "strengths": "Fastest way to build interactive UI for ML models; built-in public sharing links via tunneling.",
                "tradeoffs": "Less suitable for complex non-ML multi-page enterprise database CRUD portals.",
                "metrics": [
                    {"label": "Backend", "val": "FastAPI + Uvicorn", "sub": "Async Python"},
                    {"label": "Frontend", "val": "Svelte Components", "sub": "Reactive JS"},
                    {"label": "Sharing", "val": "Public Tunnel", "sub": "Instant URL"},
                    {"label": "Hugging Face", "val": "Official Standard", "sub": "Spaces Native"}
                ],
                "code": """import gradio as gr
import numpy as np

def predict_ad_incrementality(spend, channel, discount_rate):
    lift = spend * (1.8 if channel == 'Paid Search' else 1.2) * (1 - discount_rate/100)
    return f"Estimated Incremental EBITDA: ${lift:,.2f}"

with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# Marketing Mix Incrementality Simulator")
    with gr.Row():
        spend_input = gr.Slider(1000, 100000, value=25000, label="Media Spend ($)")
        channel_input = gr.Dropdown(['Paid Search', 'Social', 'Affiliate'], label="Channel")
        discount_input = gr.Slider(0, 50, value=10, label="Promotional Discount (%)")
    
    output_text = gr.Textbox(label="Model Output")
    btn = gr.Button("Evaluate Econometric Lift", variant="primary")
    btn.click(predict_ad_incrementality, inputs=[spend_input, channel_input, discount_input], outputs=output_text)

demo.launch()"""
            }
        ]
    },
    {
        "name": "Panel",
        "category": "Interactive Dashboards & Web Apps",
        "folder": "Panel",
        "pip": "pip install panel param bokeh",
        "docs": "https://panel.holoviz.org",
        "license": "BSD 3-Clause",
        "tagline": "Powerful data exploration and web app framework built on Bokeh and the HoloViz ecosystem.",
        "peers": PEERS_CAT5,
        "paradigms": [
            {
                "tag": "01 / REACTIVE PARAM PIPELINES",
                "title": "Reactive Param Pipelines & Big Data Explorer",
                "subtitle": "Connects multi-library visualizations (Bokeh, Matplotlib, Plotly, Altair) into unified reactive dashboards.",
                "math_desc": "Parametric dependency graph tracking: `@pn.depends` triggers localized subtree re-renders without whole-page refresh.",
                "math_formula": "\\mathcal{G}_{\\text{reactive}} = \\{ V_{\\text{params}}, E_{\\text{callbacks}} \\}, \\quad \\Delta v_i \\implies \\text{BFS}(v_i)",
                "time_complexity": "O(K) downstream dependent nodes",
                "space_complexity": "O(N) Bokeh scenegraph cache",
                "enterprise_use": "Satellite remote sensing temporal explorer, quantitative energy grid load forecasting consoles.",
                "strengths": "Deploy anywhere: runs identical code inside Jupyter notebooks, standalone server, or WebAssembly (Pyodide).",
                "tradeoffs": "Steeper learning curve than Streamlit due to advanced Param reactive concepts.",
                "metrics": [
                    {"label": "Wasm Ready", "val": "Pyodide Native", "sub": "Serverless HTML"},
                    {"label": "Frameworks", "val": "MPL, Plotly, Bokeh", "sub": "Multi-Engine"},
                    {"label": "Reactivity", "val": "Param Dependent", "sub": "Granular Diff"},
                    {"label": "Server", "val": "Bokeh / Tornado", "sub": "Two-Way Websockets"}
                ],
                "code": """import panel as pn
import numpy as np
import holoviews as hv
pn.extension('bokeh')

class TelemetryDashboard(pn.viewable.Viewer):
    frequency = pn.widgets.FloatSlider(name='Frequency', start=0.5, end=5.0, value=1.0)
    
    @pn.depends('frequency.value')
    def view(self):
        t = np.linspace(0, 10, n_samples)
        y = np.sin(t * self.frequency.value)
        return hv.Curve((t, y), 'Time', 'Signal').opts(color='#00e676', width=600, height=350)
    
    def __panel__(self):
        return pn.Column("# Sensor Frequency Analysis", self.frequency, self.view)

TelemetryDashboard().servable()"""
            }
        ]
    },
    {
        "name": "Taipy",
        "category": "Interactive Dashboards & Web Apps",
        "folder": "Taipy",
        "pip": "pip install taipy pandas",
        "docs": "https://www.taipy.io",
        "license": "Apache 2.0",
        "tagline": "Full-stack Python application framework for building production AI and business workflows.",
        "peers": PEERS_CAT5,
        "paradigms": [
            {
                "tag": "01 / ENTERPRISE SCENARIO PIPELINE",
                "title": "Enterprise Scenario Management & What-If Simulations",
                "subtitle": "Combines reactive GUI with underlying DAG data pipelines and persistent scenario version control.",
                "math_desc": "Scenario parameter optimization: $\\mathbf{x}^* = \\arg\\max_{\\mathbf{x} \\in \\mathcal{X}_s} \\text{EBITDA}(\\mathbf{x})$ across historical snapshots.",
                "math_formula": "\\mathcal{S} = \\{ \\text{Config}, \\text{Pipelines}, \\text{Snapshots}, \\text{Audits} \\}",
                "time_complexity": "O(N) pipeline execution pass",
                "space_complexity": "O(S) persistent scenario storage",
                "enterprise_use": "Supply chain inventory demand planning, airline revenue management seat pricing scenarios.",
                "strengths": "Built specifically for multi-scenario comparative business planning with built-in DAG executor.",
                "tradeoffs": "Relatively newer ecosystem compared to Streamlit or Dash.",
                "metrics": [
                    {"label": "Focus", "val": "Scenario Management", "sub": "What-If Analysis"},
                    {"label": "Pipeline", "val": "DAG Core Engine", "sub": "Version Controlled"},
                    {"label": "UI Engine", "val": "React Custom", "sub": "High Density Tables"},
                    {"label": "License", "val": "Apache 2.0", "sub": "Enterprise Ready"}
                ],
                "code": """from taipy.gui import Gui
import numpy as np
import pandas as pd

n_pts = n_samples
data = pd.DataFrame({
    'Days': range(n_pts),
    'Demand': np.random.normal(500, 50, n_pts)
})

page = \"\"\"
# Enterprise Demand Planning Scenario
<|{data}|chart|type=line|x=Days|y=Demand|line_color=#00e676|>
\"\"\"

Gui(page).run(dark_mode=True)"""
            }
        ]
    },
    {
        "name": "Reflex",
        "category": "Interactive Dashboards & Web Apps",
        "folder": "Reflex",
        "pip": "pip install reflex",
        "docs": "https://reflex.dev",
        "license": "Apache 2.0",
        "tagline": "Pure Python full-stack reactive framework that compiles directly into Next.js and React.",
        "peers": PEERS_CAT5,
        "paradigms": [
            {
                "tag": "01 / PURE PYTHON NEXT.JS",
                "title": "Full-Stack Reactive State Machine (Compiled to Next.js)",
                "subtitle": "Write Python classes that compile into production Next.js frontend with FastAPI WebSocket backend.",
                "math_desc": "Server-side state reducer: $\\mathbf{S}_{t+1} = \\delta(\\mathbf{S}_t, \\text{Event})$ pushed as JSON patches to the React virtual DOM.",
                "math_formula": "\\Delta \\text{DOM} = \\text{Reconcile}(\\text{VDOM}(\\mathbf{S}_{t+1}), \\text{VDOM}(\\mathbf{S}_t))",
                "time_complexity": "O(1) localized state dispatch",
                "space_complexity": "O(Clients) server session states",
                "enterprise_use": "Customer-facing SaaS commercial web applications, B2B internal admin portals.",
                "strengths": "Produces real production Next.js applications with SEO optimization without writing JavaScript.",
                "tradeoffs": "Compilation step requires Node.js runtime during application build.",
                "metrics": [
                    {"label": "Compiler", "val": "Python to Next.js", "sub": "Production React"},
                    {"label": "Backend", "val": "FastAPI Async", "sub": "WebSocket Engine"},
                    {"label": "State", "val": "Server Redux-like", "sub": "Diff Patches"},
                    {"label": "Styling", "val": "Tailwind / Radix", "sub": "Modern Theme"}
                ],
                "code": """import reflex as rx

class State(rx.State):
    count: int = 0
    
    def increment(self):
        self.count += 1
        
    def decrement(self):
        self.count -= 1

def index():
    return rx.container(
        rx.heading("Enterprise KPI Counter", color="#fffefa"),
        rx.hstack(
            rx.button("-", on_click=State.decrement, color_scheme="red"),
            rx.text(State.count, font_size="2em", color="#00e676"),
            rx.button("+", on_click=State.increment, color_scheme="green")
        )
    )

app = rx.App()
app.add_page(index)"""
            }
        ]
    },
    {
        "name": "Gleam",
        "category": "Interactive Dashboards & Web Apps",
        "folder": "Gleam",
        "pip": "pip install gleam matplotlib",
        "docs": "https://github.com/dgrtwo/gleam",
        "license": "MIT License",
        "tagline": "Minimalist interactive dashboards in Python inspired by R's Shiny framework.",
        "peers": PEERS_CAT5,
        "paradigms": [
            {
                "tag": "01 / DECLARATIVE FORM BINDINGS",
                "title": "Minimalist Declarative Form-to-Plot Binding",
                "subtitle": "Converts HTML form inputs directly into Matplotlib plot updates with minimal boilerplate.",
                "math_desc": "Declarative form parameter mapping: $\\mathbf{P} \\mapsto f(\\mathbf{P})$ evaluated on submission.",
                "math_formula": "\\mathbf{Plot} = f(x_1, x_2, \\dots, x_k)",
                "time_complexity": "O(N) plot generation",
                "space_complexity": "O(1) memory footprint",
                "enterprise_use": "Lightweight scientific laboratory equipment parameter adjustment consoles.",
                "strengths": "Extremely concise Shiny-like declarative structure in pure Python.",
                "tradeoffs": "Legacy package; not actively maintained compared to modern frameworks.",
                "metrics": [
                    {"label": "Inspiration", "val": "R Shiny", "sub": "Declarative Inputs"},
                    {"label": "Rendering", "val": "Matplotlib Backend", "sub": "Static Image"},
                    {"label": "Weight", "val": "< 500 KB", "sub": "Ultra-light"},
                    {"label": "License", "val": "MIT Permissive", "sub": "Open Source"}
                ],
                "code": """from gleam import Page, panels
import matplotlib.pyplot as plt
import numpy as np

class ScatterPlot(Page):
    title = "Minimalist Parameter Explorer"
    inputs = [
        panels.Slider(name="n_points", min=10, max=500, value=n_samples),
        panels.Select(name="color", options=["green", "gold", "cyan"])
    ]
    def output(self, inputs):
        fig, ax = plt.subplots(facecolor='#050806')
        x = np.random.randn(inputs.n_points)
        y = np.random.randn(inputs.n_points)
        ax.scatter(x, y, color='#00e676')
        return fig"""
            }
        ]
    },
    {
        "name": "Anvil",
        "category": "Interactive Dashboards & Web Apps",
        "folder": "Anvil",
        "pip": "pip install anvil-uplink",
        "docs": "https://anvil.works",
        "license": "Proprietary / Open Core",
        "tagline": "Build full-stack web applications with pure Python, from drag-and-drop UI to backend databases.",
        "peers": PEERS_CAT5,
        "paradigms": [
            {
                "tag": "01 / CLIENT-SERVER RPC",
                "title": "Pure Python Client-Server RPC & Embedded PostgreSQL",
                "subtitle": "Executes Python in the browser via Skulpt and calls server functions seamlessly via `@anvil.server.callable`.",
                "math_desc": "Transparent Remote Procedure Call (RPC) network abstraction over SSL WebSockets.",
                "math_formula": "\\mathbf{R}_{\\text{client}} = \\text{RPC}_{\\text{server}}(\\text{Func}, \\text{Args})",
                "time_complexity": "O(Network RTT) round-trip",
                "space_complexity": "O(1) client payload",
                "enterprise_use": "Rapid internal corporate tools with built-in user authentication and role-based access control.",
                "strengths": "Complete full-stack in pure Python; zero HTML/CSS/JS or SQL required.",
                "tradeoffs": "Tied to Anvil runtime platform or Anvil Open Source App Server.",
                "metrics": [
                    {"label": "Full Stack", "val": "Client + Server Py", "sub": "Zero JavaScript"},
                    {"label": "Database", "val": "PostgreSQL Built-in", "sub": "Python ORM"},
                    {"label": "Auth", "val": "Built-in RBAC", "sub": "Enterprise Auth"},
                    {"label": "Hosting", "val": "Anvil Cloud / Self-Host", "sub": "Docker App Server"}
                ],
                "code": """import anvil.server

@anvil.server.callable
def calculate_commercial_roi(investment, direct_share_lift):
    savings = investment * (direct_share_lift / 100.0) * 0.15
    return {"net_savings": savings, "status": "APPROVED"}

anvil.server.connect("YOUR_SERVER_UPLINK_KEY")
print("Connected to Anvil Uplink RPC Bridge.")"""
            }
        ]
    },
    {
        "name": "Solara",
        "category": "Interactive Dashboards & Web Apps",
        "folder": "Solara",
        "pip": "pip install solara pandas",
        "docs": "https://solara.dev",
        "license": "MIT License",
        "tagline": "Pure Python React-like component framework with virtual DOM and instant hot reloading.",
        "peers": PEERS_CAT5,
        "paradigms": [
            {
                "tag": "01 / REACT HOOKS IN PYTHON",
                "title": "React Component Model with `use_state` & `use_effect` Hooks",
                "subtitle": "Brings the declarative React component paradigm and virtual DOM reconciliation to pure Python.",
                "math_desc": "Virtual DOM reconciliation algorithm calculating minimal delta patches on component state mutation.",
                "math_formula": "\\Delta = \\text{Diff}(\\text{Tree}_{t+1}, \\text{Tree}_t), \\quad \\text{RenderCount} = \\text{Minimal}",
                "time_complexity": "O(N) virtual DOM diff",
                "space_complexity": "O(N) component tree hierarchy",
                "enterprise_use": "High-complexity multi-tab scientific workspaces, satellite spatial analysis platforms.",
                "strengths": "True React paradigm in pure Python; runs in Jupyter, FastAPI, and Starlette seamlessly.",
                "tradeoffs": "Requires understanding of React hook rules and component lifecycle.",
                "metrics": [
                    {"label": "Model", "val": "React in Python", "sub": "use_state / use_effect"},
                    {"label": "Hot Reload", "val": "Instant Sub-second", "sub": "State Preserved"},
                    {"label": "Environments", "val": "Jupyter + Web", "sub": "Universal"},
                    {"label": "License", "val": "MIT Permissive", "sub": "Open Core"}
                ],
                "code": """import solara

@solara.component
def Page():
    count, set_count = solara.use_state(0)
    
    with solara.Card("Enterprise Metric Counter"):
        solara.Markdown(f"### Current Value: **{count}**")
        solara.Button("Increment +1", on_click=lambda: set_count(count + 1), color="#00e676")"""
            }
        ]
    }
]
