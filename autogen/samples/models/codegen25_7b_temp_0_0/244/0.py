import math  
def next_Perfect_Square(N): 
  """
  Write a python function to find the next perfect square greater than a given number.
  """
  if N == 1: 
    return 2
  else: 
    return int(math.sqrt(N))**2

def next_Perfect_Square1(N): 
  """
  Write a python function to find the next perfect square greater than a given number.
  """
  if N == 1: 