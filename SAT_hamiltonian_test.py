# Irfansha Shaik, 26.09.2019, Aarhus.

'''
SAT test for hamiltonian cycle.
'''

import generator as gn
import naive_encoding as n_en
import os

# Todos:
# 1. Add asserts for correctness.

def read_first_line(file_name):
  f = open(file_name,"r")
  line = f.readline()
  return line

def is_hamiltonian_SAT(G):
  file_name = "hamiltonian_"+str(len(G.nodes))+"_"+str(G.size())
  n_en.encoding(G,file_name)
  # Assuming tawSolver executable is in the same directory:
  command = "./tawSolver ./" + file_name + " > stats"
  os.system(command)
  os.system("rm ./" + file_name)
  line = read_first_line("stats")
  os.system("rm ./stats")
  line = line.rstrip().rstrip("\n")
  if (line == "s SATISFIABLE"):
    return True
  return False
