"""
06_networkx_graph_centrality.py
===============================
Calculates PageRank, Betweenness Centrality, and Louvain modularity clusters
on a hospitality global distribution graph and renders publication-ready layouts.
"""

import networkx as nx
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Build Directed Multi-Tier Distribution & CRS Topology
G = nx.DiGraph()

nodes = [
    ("Guest", {"layer": 0}),
    ("Google Search", {"layer": 1}),
    ("Tripadvisor Meta", {"layer": 1}),
    ("Booking OTA", {"layer": 1}),
    ("Expedia OTA", {"layer": 1}),
    ("Brand Direct Engine", {"layer": 2}),
    ("Hotel Switch / GDS", {"layer": 3}),
    ("Central Reservation System", {"layer": 4}),
    ("Property Mgmt System (PMS)", {"layer": 5}),
    ("Revenue Mgmt System (RMS)", {"layer": 5}),
    ("Customer Data Platform (CDP)", {"layer": 6})
]
G.add_nodes_from(nodes)

edges = [
    ("Guest", "Google Search", 0.9),
    ("Guest", "Tripadvisor Meta", 0.4),
    ("Guest", "Booking OTA", 0.7),
    ("Guest", "Expedia OTA", 0.5),
    ("Guest", "Brand Direct Engine", 0.6),
    ("Google Search", "Brand Direct Engine", 0.8),
    ("Google Search", "Booking OTA", 0.85),
    ("Tripadvisor Meta", "Brand Direct Engine", 0.5),
    ("Tripadvisor Meta", "Expedia OTA", 0.6),
    ("Booking OTA", "Hotel Switch / GDS", 0.95),
    ("Expedia OTA", "Hotel Switch / GDS", 0.95),
    ("Brand Direct Engine", "Central Reservation System", 1.0),
    ("Hotel Switch / GDS", "Central Reservation System", 1.0),
    ("Central Reservation System", "Property Mgmt System (PMS)", 1.0),
    ("Property Mgmt System (PMS)", "Revenue Mgmt System (RMS)", 0.8),
    ("Revenue Mgmt System (RMS)", "Central Reservation System", 0.85),
    ("Property Mgmt System (PMS)", "Customer Data Platform (CDP)", 0.9),
    ("Brand Direct Engine", "Customer Data Platform (CDP)", 0.75)
]
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Analytics
pagerank = nx.pagerank(G, weight='weight')
betweenness = nx.betweenness_centrality(G)

fig, ax = plt.subplots(figsize=(14, 9), facecolor='#070c09')
ax.set_facecolor('#0d1410')

# Position nodes using multipartite or spring layout
pos = nx.spring_layout(G, k=1.8, seed=42)

# Draw edges
weights = [G[u][v]['weight'] * 2.5 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, ax=ax, edge_color='#27342b', width=weights, arrowsize=18, arrowstyle='-|>', connectionstyle="arc3,rad=0.08")

# Draw nodes sized by PageRank
node_sizes = [pagerank[node] * 12000 for node in G.nodes()]
node_colors = ['#d4af37' if 'System' in n or 'PMS' in n or 'CRS' in n else '#00e676' if 'Direct' in n else '#00e5ff' for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors, edgecolors='#f4ebd0', linewidths=1.5, alpha=0.9)

# Labels
labels = {n: f"{n}\nPR: {pagerank[n]:.3f}" for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, font_size=8.5, font_color='#f4ebd0', font_family='DejaVu Sans')

ax.set_title("Hotel Demand Graph Centrality & Distribution Topology", color='#d4af37', fontsize=15, pad=15, fontweight='bold')
ax.axis('off')

output_path = "06_networkx_centrality.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✓ Successfully rendered NetworkX distribution topology: {output_path}")
