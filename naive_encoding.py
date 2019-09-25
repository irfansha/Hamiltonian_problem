# Irfansha Shaik, 25.09.2019, Aarhus.
# Copy from https://github.com/irfansha/Encodings/blob/master/hamiltonian_path/naive_encoding.py
# Naive encoding for Hamiltonian path

# Todos:
# 1. Update comments.


'''
Input format: graph G (Same format as networkx)
'''

import sys
import networkx as nx

# Relabeling nodes for direct encoding:
# Starting from 1 to N where N is number of nodes:
def relabel(G):
  new_labels = dict()
  nodes = list(G.nodes)
  for i in range(1, len(nodes)+1):
    new_labels[nodes[i-1]] = i
  return nx.relabel_nodes(G,new_labels)

# To dictionary of dictionaries:
def to_adj_dict(G):
  return nx.convert.to_dict_of_lists(G)

# AtMostOne constraints for every pair of variables:
def AMO(var):
  for i in range(0, len(var)):
    for j in range(i + 1, len(var)):
      cnf_output.append([-var[i], -var[j], 0])

# AtLeastOne constraint for the set of variables:
def ALO(var):
  var.append(0)
  cnf_output.append(var)

# Constraints for adjacent nodes of different levels for cycle:
def edg_con_cycle(node,neighbours):
  for i in range(1,N):
    temp_clause = [-var_map(i, node)]
    for neighbour in neighbours:
      temp_clause.append(var_map(i+1,int(neighbour)))
    temp_clause.append(0)
    cnf_output.append(temp_clause)
  # Additional edge to complete the cycle:
  temp_clause = [-var_map(N, node)]
  temp_clause.extend(neighbours)
  temp_clause.append(0)
  cnf_output.append(temp_clause)

# Mapping variables with level i and node j to single integer:
def var_map(i, j):
  return ((i - 1) * N + j)

# Joining variables in each constraint for cnf format:
def convert(lst):
  s = [str(i) for i in lst]
  return ' '.join(s)

# print the constraints in dimacs/qdimacs based on the option provided:
def print_cnf():
  print("p cnf " + str(N * N) + " " + str(len(cnf_output)))
  for line in cnf_output:
    print(convert(line))

# Number of nodes
N = 0
# Number of edges
E = 0
# List for final cnf output:
cnf_output = []


def encoding(G):
  global N
  N = len(G.nodes)
  global E
  E = G.size()
  G = relabel(G)
  adj_dict = to_adj_dict(G)
  # Exactly one node each turn:
  for i in range(1, N + 1):
    # AtMostOne constraints for each level:
    temp_var = []
    for j in range(1, N + 1):
      temp_var.append(var_map(i, j))
    AMO(temp_var)

  for i in range(1, N + 1):
    # AtLeastOne constraints for each level:
    temp_var = []
    for j in range(1, N + 1):
      temp_var.append(var_map(i, j))
    ALO(temp_var)

  # Visit every vertex only once:
  for j in range(1, N + 1):
    temp_var = []
    for i in range(1, N + 1):
      temp_var.append(var_map(i, j))
    AMO(temp_var)

  for j in range(1, N + 1):
    temp_var = []
    for i in range(1, N + 1):
      temp_var.append(var_map(i, j))
    ALO(temp_var)

  # Edge constraints:
  for node, neighbours in adj_dict.iteritems():
    edg_con_cycle(node, neighbours)
  print_cnf()
