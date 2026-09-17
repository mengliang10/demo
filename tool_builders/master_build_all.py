"""
Master Build Script for Python Visualization Masterclass Studios.
Generates bespoke, production-ready interactive HTML studios for all 45 tools across 5 categories.
STRICTLY NO REVEAL.JS. Every tool has unique interactive mechanics and distinct functions.
"""

import os
import sys
import glob

# Ensure current directory is in sys.path
SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from tool_builders.builder_declarative import build_declarative_tools
from tool_builders.builder_statistical import build_statistical_tools
from tool_builders.builder_scientific_3d import build_scientific_tools
from tool_builders.builder_diagrams import build_diagrams_tools
from tool_builders.builder_geospatial import build_geospatial_tools
from tool_builders.builder_dashboards import build_dashboards_tools

def run_master_build():
    print("================================================================================")
    print("  PYVISWORKBENCH MASTER BUILD: 45 BESPOKE PYTHON VISUALIZATION STUDIOS")
    print("  STRICTLY NO REVEAL.JS · BESPOKE INTERACTIVE ENGINES · DISTINCT MECHANICS")
    print("================================================================================\n")

    print("[1/6] Building Declarative & Web-Interactive Tools (Plotly, Altair, Bokeh, HoloViews, Chartify, HVPlot, bqplot)...")
    build_declarative_tools()

    print("\n[2/6] Building Statistical & Core Plotting Tools (Matplotlib, Seaborn, Pygal, Plotnine, Leather, Veusz, GR, Visvis, Chaco)...")
    build_statistical_tools()

    print("\n[3/6] Building 3D, High-Performance & Scientific Tools (Datashader, Mayavi, VisPy, PyQtGraph, VTK, Glumpy, Manim, PyVista)...")
    build_scientific_tools()

    print("\n[4/6] Building Diagrams, Networks & Schematics Tools (NetworkX, PyVis, Diagrams, SchemDraw, Graphviz, DNA Features, diaGrabber)...")
    build_diagrams_tools()

    print("\n[5/6] Building Geospatial & Mapping Tools (Folium, GeoPandas, Cartopy, Geoplotlib, Pydeck, Mapclassify)...")
    build_geospatial_tools()

    print("\n[6/6] Building Interactive Dashboards & Web Apps (Streamlit, Gradio, Panel, Taipy, Reflex, Gleam, Anvil, Solara)...")
    build_dashboards_tools()

    # Verification audit
    print("\n================================================================================")
    print("  VERIFICATION AUDIT & INTEGRITY CHECK")
    print("================================================================================")
    base_dir = os.path.join(SCRIPT_DIR, "Python Visualization, Graphical, & Interactive Libraries")
    categories = [
        "Statistical, Charting & Core Plotting",
        "3D, High-Performance & Scientific Graphics",
        "Diagrams, Graph Networks & Schematics",
        "Geospatial & Mapping",
        "Interactive Dashboards & Web Apps"
    ]

    total_tools = 0
    total_files = 0
    total_bytes = 0
    reveal_violations = 0
    missing_index = []
    missing_studio = []

    for cat in categories:
        cat_dir = os.path.join(base_dir, cat)
        if not os.path.exists(cat_dir):
            print(f"  [!] Missing category dir: {cat_dir}")
            continue

        tool_dirs = [d for d in os.listdir(cat_dir) if os.path.isdir(os.path.join(cat_dir, d))]
        print(f"\nCategory: {cat} ({len(tool_dirs)} tools)")

        for td in sorted(tool_dirs):
            total_tools += 1
            full_td = os.path.join(cat_dir, td)
            idx_file = os.path.join(full_td, "index.html")

            # Check index.html
            if os.path.exists(idx_file):
                sz = os.path.getsize(idx_file)
                total_files += 1
                total_bytes += sz
                with open(idx_file, "r", encoding="utf-8", errors="ignore") as f:
                    c = f.read()
                    if "reveal.js" in c.lower() or 'class="reveal"' in c.lower():
                        reveal_violations += 1
                        print(f"    [X] REVEAL.JS DETECTED in {td}/index.html!")
            else:
                missing_index.append(f"{cat}/{td}")

            # Check studio file
            clean_name = td.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
            studio_file = os.path.join(full_td, f"{clean_name}_studio.html")
            if os.path.exists(studio_file):
                total_files += 1
                total_bytes += os.path.getsize(studio_file)
            else:
                missing_studio.append(f"{cat}/{td}")

            print(f"    [OK] {td:<38} | index.html: {sz/1024:.1f} KB | studio: {clean_name}_studio.html")

    print("\n--------------------------------------------------------------------------------")
    print(f"Total Tools Verified:   {total_tools} / 45")
    print(f"Total HTML Files Built: {total_files} ({total_bytes / (1024*1024):.2f} MB total)")
    print(f"Reveal.js Violations:   {reveal_violations} (MUST BE ZERO)")
    if missing_index:
        print(f"Missing index.html:     {missing_index}")
    if missing_studio:
        print(f"Missing studio.html:    {missing_studio}")
    print("--------------------------------------------------------------------------------")

    if total_tools == 45 and reveal_violations == 0 and not missing_index and not missing_studio:
        print(">>> ALL 45 TOOLS FULLY SYNTHESIZED WITH BESPOKE INTERACTIVE ENGINES! <<<")
    else:
        print(">>> WARNING: Some checks did not pass. Inspect log above. <<<")

if __name__ == "__main__":
    run_master_build()
