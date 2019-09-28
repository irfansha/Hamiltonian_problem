# Irfansha Shaik, 25.09.2019, Aarhus.

'''
Generating non-trivial non-hamiltonian graphs.
'''

'''
An example use of ntnh_random_binomial_graphs function:
print(ntnh_random_binomial_graphs(20,0.3,0,1000)):

prints [[20, 0.3, 24], [20, 0.3, 494], [20, 0.3, 923], [20, 0.3, 957]]

These are non-trivial non-hamiltonian graphs.
Almost takes 3 minutes though.
'''

'''
Analysis:
1. ntnh_random_binomial_graphs(20,0.3,0,1000)
  [[20, 0.3, 24], [20, 0.3, 494], [20, 0.3, 923], [20, 0.3, 957]]
  real	2m39,758s
  user	2m35,402s
  sys	0m5,079s
2. ntnh_random_binomial_graphs(20,0.5,0,100000)
  []
  real	50m0,004s
  user	40m32,106s
  sys	9m23,457s
3. ntnh_random_binomial_graphs(20,0.55,0,100000)
[]

real	41m35,822s
user	35m38,525s
sys	6m6,374s

'''


# Todos:
# 1. Add assertions for correctness.


import generator as gn
import basic_hamiltonian_tests as bh_test
import networkx as nx
import SAT_hamiltonian_test as s_test

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
      if not (s_test.is_hamiltonian_SAT(G)):
        ntnh_graphs.append([N,E,i])
  return ntnh_graphs

# Returns list of all non-trivial non-hamiltonian binomial graph arguments within seeds range:
def ntnh_random_binomial_graphs(N, p, start_seed, end_seed):
  ntnh_graphs = []
  for i in range(start_seed,end_seed+1):
    G = gn.binomial_random_graph_gen(N,p,i)
    if not (bh_test.is_trivial_non_hamiltonian(G) or bh_test.is_trivial_hamiltonian(G)):
      if not (s_test.is_hamiltonian_SAT(G)):
        ntnh_graphs.append([N,p,i])
  return ntnh_graphs
