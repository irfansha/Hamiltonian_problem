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

4. ntnh_random_binomial_graphs(20,0.4,0,1000000)
[[20, 0.4, 78689], [20, 0.4, 135466], [20, 0.4, 140465], [20, 0.4, 151893], [20, 0.4, 165039], [20, 0.4, 173980], [20, 0.4, 186891], [20, 0.4, 211751], [20, 0.4, 231141], [20, 0.4, 239279], [20, 0.4, 278682], [20, 0.4, 334966], [20, 0.4, 356335], [20, 0.4, 361744], [20, 0.4, 393350], [20, 0.4, 410707], [20, 0.4, 411764], [20, 0.4, 435014], [20, 0.4, 438936], [20, 0.4, 444421], [20, 0.4, 465634], [20, 0.4, 504504], [20, 0.4, 568064], [20, 0.4, 581353], [20, 0.4, 582090], [20, 0.4, 650666], [20, 0.4, 677240], [20, 0.4, 693802], [20, 0.4, 751053], [20, 0.4, 797020], [20, 0.4, 827010], [20, 0.4, 833663], [20, 0.4, 835923], [20, 0.4, 839604], [20, 0.4, 846841], [20, 0.4, 850091], [20, 0.4, 860535], [20, 0.4, 907136], [20, 0.4, 926244]]

real	985m54,130s
user	899m27,630s
sys	87m30,618s

'''


# Todos:
# 1. Add assertions for correctness.
# 2. Separate basic tests.


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
