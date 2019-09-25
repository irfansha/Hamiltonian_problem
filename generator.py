# Irfansha Shaik, 24.09.2019, Aarhus.

'''
Graph generator using Networkx library.
For finding non-hamiltonian "hard-graphs", random graphs and special graphs are generated.
'''

# Todos:
# 1. Update the options to include special graphs.
# 2. Add option to write the graph to files.

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

# Takes long time:
def visualise_all_atlas_graphs():
  all_small_graphs = nx.atlas.graph_atlas_g()
  for G in all_small_graphs:
    nx.draw(G)
    plt.show(block=False)
    plt.pause(0.5)
    plt.close()

# Returns list of atlas graphs
def all_atlas_graphs():
  return nx.atlas.graph_atlas_g()

# Returns a G_(n,p) random graph or Erods-Renyi/binomial graph,
# With n nodes, p edge probability and seed for random number generation:
def binomial_random_graph_gen(n, p, seed):
  return fast_gnp_random_graph(n, p, seed)

# Returns a G_(n,m) random graph,
# With n nodes, m edges and seed for random number generation:
def random_graph_gen(n, p, seed):
  return fast_gnp_random_graph(n, p, seed)
