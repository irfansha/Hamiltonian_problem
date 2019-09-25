# Irfansha Shaik, 24.09.2019, Aarhus.

'''
Graph generator using Networkx library.
For finding non-hamiltonian "hard-graphs", random graphs and special graphs are generated.
'''

# Todos:
# 1. Generate simple graphs with set number of nodes and edges.
# 2. Update the options to include special graphs.
# 3. Add option to write the graph to files.
# 4. Specify input and output for this module.

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
