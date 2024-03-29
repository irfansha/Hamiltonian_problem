# Irfansha Shaik, 24.09.2019, Aarhus.

'''
Graph generator using Networkx library.
For finding non-hamiltonian "hard-graphs", random graphs and special graphs are generated.
'''

# Todos:
# 1. Update the options to include special graphs.
# 2. Add option to write the graph to files.

# Install networkx
try:
  import networkx as nx
except:
  raise

# Returns list of atlas graphs
def all_atlas_graphs():
  return nx.atlas.graph_atlas_g()

# Returns a G_(n,p) random graph or Erods-Renyi/binomial graph,
# With n nodes, p edge probability and seed for random number generation:
def binomial_random_graph_gen(n, p, seed):
  assert p <= 1, "Probability should be less than 1."
  return nx.generators.random_graphs.fast_gnp_random_graph(n, p, seed)

# Returns a G_(n,m) random graph,
# With n nodes, m edges and seed for random number generation:
def random_graph_gen(n, m, seed):
  assert m <= n*(n-1), "Too many edges."
  return nx.generators.random_graphs.gnm_random_graph(n, m, seed)
