# Irfansha Shaik, 25.09.2019, Aarhus.

'''
Basic tests for hamiltonian cycle.
'''

# Todos:
# 1. Test for sum of two non-adjacent vertices.

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

# Returns true is graph G is trivially non-hamiltonian:
def is_trivial_non_hamiltonian(G):
  # Hamiltonian graph must have a minimum degree of 2:
  if min_degree(G) < 2:
    return True
  # Hamiltonian graph must be connected:
  if k_components(G) > 1:
    return True
  return False

def is_trivial_hamiltonian(G):
  # A graph with minimum degree atleast n/2 is hamiltonian:
  if min_degree(G) >= len(G.nodes):
    return True
  return False
