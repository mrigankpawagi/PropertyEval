import math 
def is_polite(n): 
  """
  Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
  """
  if n == 1: 
    return 1
  else: 
    return (is_polite(n-1) + 1) * (n-1)

def is_polite_2(n): 
  """
  Write a function to find nth polite number. geeksforgeeks.org/n-