# Irfansha Shaik, 29.09.2019, Aarhus.

'''
Toughness for undirected graphs.
'''

# Todos:
# 1. Improve computation using properties of graphs.
# 2. Use SAT/QBF for efficient computation.

import networkx as nx
import math
import random
from itertools import combinations
from itertools import permutations

# Returns the toughness of the graph G with cut_set:
def local_toughness(cut_set,G):
  for v in cut_set:
    G.remove_node(v)
  # Compute number of connected components:
  n = nx.number_connected_components(G)
  if (n != 1):
    return len(cut_set)/n
  else:
    return math.inf

# Returns approximate toughness with only upper bounds guarantee:
def linear_approx_heuristic_toughness(G):
  sorted_list = sorted(G.degree, key=lambda x: x[1], reverse=True)
  sorted_nodes = []
  # Sorted node-list with descending degree:
  for item in sorted_list:
    sorted_nodes.append(item[0])
  min_toughness = math.inf
  min_cut_set = []
  # Iteratively computing toughness for first i nodes in the sorted list:
  for i in range(1, len(sorted_nodes)):
    cut_set = sorted_nodes[:i]
    l_toughness = local_toughness(cut_set,G.copy())
    if l_toughness < min_toughness:
      min_toughness = l_toughness
      min_cut_set = cut_set
  return (min_toughness,min_cut_set)

# Returns approximate toughness with only upper bounds guarantee with random heuristics:
def random_approx_heuristic_toughness(G,n_tries):
  nodes = list(G.nodes())
  min_toughness = math.inf
  min_cut_set = []
  # Shuffles the nodes list n_tires times:
  for i in range(0,n_tries):
    random.shuffle(nodes)
    # Iteratively computing toughness for first i nodes in the random list:
    for i in range(1, len(nodes)):
      cut_set = nodes[:i]
      l_toughness = local_toughness(cut_set,G.copy())
      if l_toughness < min_toughness:
        min_toughness = l_toughness
        min_cut_set = cut_set
  return (min_toughness,min_cut_set)

# Returns approximate toughness with only upper bounds guarantee with random heuristics:
def improved_random_approx_toughness(G,n_tries,bound):
  sorted_list = sorted(G.degree, key=lambda x: x[1], reverse=True)
  sorted_nodes = []
  # Sorted node-list with descending degree:
  for item in sorted_list:
    sorted_nodes.append(item[0])
  min_toughness = math.inf
  min_cut_set = []
  random.seed(0)
  # Shuffles the nodes list n_tires times:
  for i in range(0,n_tries):
    # Iteratively computing toughness for first i nodes in the random list:
    for i in range(1, len(sorted_nodes)):
      # Returns if the min_toughness is already less than or equal to bound provided:
      if min_toughness <= bound:
        return (min_toughness,min_cut_set)
      cut_set = sorted_nodes[:i]
      l_toughness = local_toughness(cut_set,G.copy())
      if l_toughness < min_toughness:
        min_toughness = l_toughness
        min_cut_set = cut_set
    random.shuffle(sorted_nodes)
  return (min_toughness,min_cut_set)

# Returns toughness of graph G:
#   - sorts the cut_sets using the total degree of the nodes in descending order.
def degree_heuristic_toughness(G,bound):
  sorted_list = sorted(G.degree, key=lambda x: x[1], reverse=True)
  sorted_nodes = []
  # Sorted node-list with descending degree:
  for item in sorted_list:
    sorted_nodes.append(item[0])
  min_toughness = math.inf
  min_cut_set = []
  for cut_size in range(1, len(sorted_nodes)):
    # Computes the combinations of cut_size:
    cut_set_gen = combinations(sorted_nodes,cut_size)
    for cut_set in cut_set_gen:
      # Returns if the min_toughness is already less than or equal to bound provided:
      if min_toughness <= bound:
        return (min_toughness,min_cut_set)
      l_toughness = local_toughness(cut_set,G.copy())
      if l_toughness < min_toughness:
        min_toughness = l_toughness
        min_cut_set = cut_set
  return (min_toughness,min_cut_set)

# Return toughness of graph G if the toughness is greater than bound
# else returns the min_toughness computed:
def bounded_toughness(G,bound):
  nodes = G.nodes()
  min_toughness = math.inf
  min_cut_set = []
  for cut_size in range(1, len(nodes)):
    # Computes the combinations of cut_size:
    cut_set_gen = combinations(nodes,cut_size)
    for cut_set in cut_set_gen:
      # Returns if the min_toughness is already less than or equal to bound provided:
      if min_toughness <= bound:
        return (min_toughness,min_cut_set)
      l_toughness = local_toughness(cut_set,G.copy())
      if l_toughness < min_toughness:
        min_toughness = l_toughness
        min_cut_set = cut_set
  return (min_toughness,min_cut_set)

# Returns the toughness and cut_set of the graph G:
def naive_toughness(G):
  nodes = G.nodes()
  min_toughness = math.inf
  min_cut_set = []
  for cut_size in range(1, len(nodes)):
    # Computes the combinations of cut_size:
    cut_set_gen = combinations(nodes,cut_size)
    for cut_set in cut_set_gen:
      l_toughness = local_toughness(cut_set,G.copy())
      if l_toughness < min_toughness:
        min_toughness = l_toughness
        min_cut_set = cut_set
  return (min_toughness,min_cut_set)
