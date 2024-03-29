# Irfansha Shaik, 25.09.2019, Aarhus.

'''
Basic tests for hamiltonian cycle.
'''

# Todos:
# 1. Add cutset test.
#    - In a simple connected graph, if a cutset of size two results in atleast 3 disjoint sets
#      then it is non-hamiltonian.
# 2. Add appropriate asserts for correctness.

import networkx as nx

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
  if not is_connected(G):
    return True
  return False

# Returns true is graph G is trivially hamiltonian:
def is_trivial_hamiltonian(G):
  # A simple graph with minimum degree atleast n/2 is hamiltonian:
  if min_degree(G) >= len(G.nodes):
    return True
  # A simple graph with minimum sum of non-adjadent nodes degree atleast n is hamiltonian:
  if min_degree_sum_non_adjacent_nodes(G) >= len(G.nodes):
    return True
  return False

# Returns true if graph G is hamiltonian:
# Using all_simple_paths function in networkx,
# Very slow, use only for assertion:
def is_hamiltonian_slow(G):
  nodes = list(G.nodes)
  # Consider first node as source:
  s_node = nodes[0]
  adj_nodes = list(G.neighbors(s_node))
  if len(adj_nodes) == 0:
    return False
  assert(len(adj_nodes) != 0)
  for adj_node in adj_nodes:
    for path in nx.all_simple_paths(G, source = s_node, target = adj_node):
      if (len(path) == len(nodes)):
        return True
  return False
