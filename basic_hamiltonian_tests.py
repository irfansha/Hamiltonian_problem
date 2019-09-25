# Irfansha Shaik, 25.09.2019, Aarhus.

'''
Basic tests for hamiltonian cycle.
'''

# Todos:
# 1. Test for minimum vertex degree.
# 2. Test for disjointness of graph.
# 3. Test for sum of two non-adjacent vertices.

# Install matplotlib
try:
  import matplotlib.pyplot as plt
except:
  raise

# Install networkx
try:
  import networkx as nx
except:
  raise

# Returns minimum degree of graph G:
def min_degree(G):
  nodes_deg =  []
  for node in G.nodes:
    nodes_deg.append(G.degree[node])
  return min(nodes_deg)

# Returns number of disjoint components in graph G:
def k_components(G):
  return len(nx.k_components(G))
