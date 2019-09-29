# Irfansha Shaik, 29.09.2019, Aarhus.

'''
Running experiments for generating tough graphs.
'''


# Todos:
# 1. Improve functionality to allow various runs using different toughness computations.


import generator as gn
import toughness as t

# Prints toughness of each graph provided with naive-toughness computation:
def naive_experiment(lst):
  for g_seed in lst:
    G = gn.binomial_random_graph_gen(g_seed[0],g_seed[1],g_seed[2])
    G_toughness = t.bounded_toughness(G,1.5)
    print(G_toughness)

# Prints toughness of each graph provided with bounded-toughness computation:
def bounded_experiment(lst,bound):
  for g_seed in lst:
    G = gn.binomial_random_graph_gen(g_seed[0],g_seed[1],g_seed[2])
    G_toughness = t.bounded_toughness(G,bound)
    print(G_toughness)
