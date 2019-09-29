# Irfansha Shaik, 29.09.2019, Aarhus.

'''
Toughness for undirected graphs.
'''

# Todos:
# 1. Use bounding to improve toughness computation.
# 2. Improve computation using properties of graphs.
# 3. Use SAT/QBF for efficient computation.

import networkx as nx
import math
from itertools import combinations

# Returns the toughness of the graph G with cut_set:
def local_toughness(cut_set,G):
  for v in cut_set:
    G.remove_node(v)
  n = nx.number_connected_components(G)
  if (n != 1):
    return len(cut_set)/n
  else:
    return math.inf

# Returns toughness of graph G:
#   - sorts the cut_sets using the total degree of the nodes in descending order.
def degree_heuristic_toughness(G):
  return 0


# Returns the toughness and cut_set of the graph G:
def naive_toughness(G):
  nodes = G.nodes()
  min_toughness = math.inf
  min_cut_set = []
  for cut_size in range(1, len(nodes)):
    cut_set_gen = combinations(nodes,cut_size)
    for cut_set in cut_set_gen:
      l_toughness = local_toughness(cut_set,G.copy())
      if l_toughness < min_toughness:
        min_toughness = l_toughness
        min_cut_set = cut_set
  return (min_toughness,min_cut_set)
