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

# Draws nothing
G = nx.Graph()
nx.draw(G)
plt.show()
