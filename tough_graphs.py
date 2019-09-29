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
    if (G_toughness[0] < bound):
      print("Not tough enough with atmost:")
    print(G_toughness)

# Prints toughness of each graph provided with bounded-toughness degree-heuristic computation:
def bounded_degree_heuristic_experiment(lst,bound):
  for g_seed in lst:
    G = gn.binomial_random_graph_gen(g_seed[0],g_seed[1],g_seed[2])
    G_toughness = t.degree_heuristic_toughness(G,bound)
    if (G_toughness[0] < bound):
      print("Not tough enough with atmost:")
    print(G_toughness)

# Prints approximate toughness of each graph with linear heuristic computation:
def linear_approximate_heuristic_experiment(lst):
  for g_seed in lst:
    G = gn.binomial_random_graph_gen(g_seed[0],g_seed[1],g_seed[2])
    G_toughness = t.linear_approx_heuristic_toughness(G)
    print(G_toughness)

# Prints approximate toughness of each graph with random tries of heuristic computation:
def random_approximate_heuristic_experiment(lst,n_tries):
  for g_seed in lst:
    G = gn.binomial_random_graph_gen(g_seed[0],g_seed[1],g_seed[2])
    G_toughness = t.random_approx_heuristic_toughness(G,n_tries)
    print(G_toughness)

# Prints approximate toughness of each graph with improved random tries of heuristic computation with bounds:
def improved_random_approximate_experiment(lst,n_tries,bound):
  for g_seed in lst:
    G = gn.binomial_random_graph_gen(g_seed[0],g_seed[1],g_seed[2])
    G_toughness = t.improved_random_approx_toughness(G,n_tries,bound)
    print(G_toughness)
