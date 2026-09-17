"""
Master Multi-Language Visualization Builder
Runs all 6 language builders (R, Julia, Rust, Go, C++, C) and generates root hub portals.
"""
import os
import sys

# Ensure lang_builders is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lang_builders.builder_r import build_r_all
from lang_builders.builder_julia import build_julia_all
from lang_builders.builder_rust import build_rust_all
from lang_builders.builder_go import build_go_all
from lang_builders.builder_cpp import build_cpp_all
from lang_builders.builder_c import build_c_all
from lang_builders.generate_portals import generate_all_portals

def run_all_builders():
    print("================================================================")
    print("  EXECUTING FULL MULTI-LANGUAGE VISUALIZATION STUDIO BUILDER    ")
    print("================================================================")
    
    print("\n--- 1. BUILDING R VISUALIZATION STUDIOS ---")
    build_r_all()
    
    print("\n--- 2. BUILDING JULIA VISUALIZATION STUDIOS ---")
    build_julia_all()
    
    print("\n--- 3. BUILDING RUST VISUALIZATION STUDIOS ---")
    build_rust_all()
    
    print("\n--- 4. BUILDING GO VISUALIZATION STUDIOS ---")
    build_go_all()
    
    print("\n--- 5. BUILDING C++ VISUALIZATION STUDIOS ---")
    build_cpp_all()
    
    print("\n--- 6. BUILDING C VISUALIZATION STUDIOS ---")
    build_c_all()

    print("\n--- 7. GENERATING EXECUTIVE HUB PORTALS ---")
    generate_all_portals()
    print("\n[✓] ALL VISUALIZATION STUDIOS AND PORTALS READY.")

if __name__ == "__main__":
    run_all_builders()
