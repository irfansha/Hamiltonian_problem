# Irfansha Shaik, 29.09.2019, Aarhus.

'''
Toughness for undirected graphs.
'''

# Todos:
# 1. Naive toughness computation.
# 2. Improve computation using properties of graphs.
# 3. Use SAT/QBF for efficient computation.

import networkx as nx

# Returns the toughness of the graph G with cut_set:
def local_toughness(cut_set,G):
  return 0

# Returns toughness of graph G:
#   - sorts the cut_sets using the total degree of the nodes in descending order.
def degree_heuristic_toughness(G):
  return 0


# Returns the toughness of the graph G:
def naive_toughness(G):
  return 0
