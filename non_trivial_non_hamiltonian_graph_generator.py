# Irfansha Shaik, 25.09.2019, Aarhus.

'''
Generating non-trivial non-hamiltonian graphs.
'''

import generator as gn
import basic_hamiltonian_tests as bh_test
import matplotlib.pyplot as plt
import networkx as nx

# Returns the list of non_trivial_non_hamiltonian graphs:
def ntnh_atlas_graphs():
  all_small_graphs = gn.all_atlas_graphs()
  ntnh_graphs = []
  for G in all_small_graphs:
    if (len(G.nodes) <= 2):
      continue
    if not (bh_test.is_trivial_non_hamiltonian(G) or bh_test.is_trivial_hamiltonian(G)):
      if not (bh_test.is_hamiltonian_slow(G)):
        ntnh_graphs.append(G)
  return ntnh_graphs

# Returns list of all non-trivial non-hamiltonian graph arguments within seeds range:
def ntnh_random_graphs(N, E, start_seed, end_seed):
  ntnh_graphs = []
  for i in range(start_seed,end_seed+1):
    G = gn.random_graph_gen(N,E,i)
    if not (bh_test.is_trivial_non_hamiltonian(G) or bh_test.is_trivial_hamiltonian(G)):
      if not (bh_test.is_hamiltonian_slow(G)):
        ntnh_graphs.append([N,E,i])
  return ntnh_graphs

# An example use of ntnh_random_graphs function:
# Returns all non-trivial non-hamiltonian graphs arguments:
# print(ntnh_random_graphs(10,15,0,200))
