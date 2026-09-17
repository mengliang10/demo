#!/usr/bin/env python3
"""
PyVisWorkbench Master Orchestrator & Site Generator
Generates all 45 unique, complex, non-reveal.js interactive visualization studio HTML applications.
"""

import os
import sys
import json
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(SCRIPT_DIR, "Python Visualization, Graphical, & Interactive Libraries")

sys.path.insert(0, SCRIPT_DIR)
from studio_template import get_studio_html
from data_cat1_statistical import TOOLS_CAT1
from data_cat2_scientific import TOOLS_CAT2
from data_cat3_diagrams import TOOLS_CAT3
from data_cat4_geospatial import TOOLS_CAT4
from data_cat5_dashboards import TOOLS_CAT5

ALL_CATEGORIES = [
    ("Statistical, Charting & Core Plotting", TOOLS_CAT1),
    ("3D, High-Performance & Scientific Graphics", TOOLS_CAT2),
    ("Diagrams, Graph Networks & Schematics", TOOLS_CAT3),
    ("Geospatial & Mapping", TOOLS_CAT4),
    ("Interactive Dashboards & Web Apps", TOOLS_CAT5)
]

def sanitize_filename(name):
    clean = re.sub(r'[^\w\-_\. ]', '_', name)
    clean = clean.replace(' ', '_')
    return clean

def build_all():
    print("=" * 70)
    print("PYVISWORKBENCH: MASTER INTERACTIVE STUDIO GENERATOR")
    print(f"Target Base: {BASE_DIR}")
    print("=" * 70)

    total_generated = 0
    generated_manifest = []

    for cat_name, tools in ALL_CATEGORIES:
        cat_dir = os.path.join(BASE_DIR, cat_name)
        print(f"\n[CATEGORY] {cat_name} ({len(tools)} tools)")

        if not os.path.exists(cat_dir):
            print(f"  [ERROR] Category directory not found: {cat_dir}")
            continue

        for tool in tools:
            tool_folder = tool.get("folder", tool["name"])
            tool_dir = os.path.join(cat_dir, tool_folder)

            if not os.path.exists(tool_dir):
                print(f"  [WARN] Tool folder not found, creating: {tool_dir}")
                os.makedirs(tool_dir, exist_ok=True)

            tool["clean_id"] = sanitize_filename(tool["name"])
            
            # Generate the rich HTML content
            html_content = get_studio_html(tool)

            # Write index.html
            index_path = os.path.join(tool_dir, "index.html")
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            # Also write tool-specific named HTML
            named_html_path = os.path.join(tool_dir, f"{tool['clean_id']}_studio.html")
            with open(named_html_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            file_size_kb = os.path.getsize(index_path) / 1024.0
            print(f"  [✓] {tool['name']:<35} -> index.html ({file_size_kb:.1f} KB)")
            total_generated += 1
            generated_manifest.append({
                "tool": tool["name"],
                "category": cat_name,
                "index_path": index_path,
                "size_kb": file_size_kb
            })

    print("\n" + "=" * 70)
    print(f"BUILD COMPLETE: Generated {total_generated} Interactive Visual Studios across 45 tools!")
    print("=" * 70)
    return generated_manifest

if __name__ == "__main__":
    manifest = build_all()
