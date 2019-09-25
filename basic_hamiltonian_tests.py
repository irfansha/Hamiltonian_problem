# Irfansha Shaik, 25.09.2019, Aarhus.

'''
Basic tests for hamiltonian cycle.
'''

# Todos:
# 1. Update trivial hamiltonian test.

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
def is_connected(G):
  return nx.is_connected(G)

# Returns minimum sum of degrees of non-adjacent nodes:
def min_degree_sum_non_adjacent_nodes(G):
  # If complete graph:
  if (G.size() == len(G.nodes)*(len(G.nodes) - 1)/2):
    return 2 * (len(G.nodes) - 1)
  # Degree of any vertex of simple graph is atmost (n-1),
  # where n is number of nodes:
  min_sum = 2 * len(G.nodes)
  for node1 in G.nodes:
    for node2 in G.nodes:
      # Avoiding redundant computation:
      if node1 >= node2:
        continue
      # if non-adjacent nodes:
      if (not G.has_edge(node1,node2)):
        if min_sum > G.degree[node1] + G.degree[node2]:
          min_sum = G.degree[node1] + G.degree[node2]
  #assert min_sum < (2 * len(G.nodes)), "min_sum is not updated."
  return min_sum

# Returns true is graph G is trivially non-hamiltonian:
def is_trivial_non_hamiltonian(G):
  # Hamiltonian graph must have a minimum degree of 2:
  if min_degree(G) < 2:
    return True
  # Hamiltonian graph must be connected:
  if is_connected(G) > 1:
    return True
  return False

def is_trivial_hamiltonian(G):
  # A simple graph with minimum degree atleast n/2 is hamiltonian:
  if min_degree(G) >= len(G.nodes):
    return True
  # A simple graph with minimum sum of non-adjadent nodes degree atleast n is hamiltonian:
  if min_degree_sum_non_adjacent_nodes(G) >= len(G.nodes):
    return True
  return False
