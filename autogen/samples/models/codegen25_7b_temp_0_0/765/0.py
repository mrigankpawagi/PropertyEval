import math 
def is_polite(n): 
  """
  Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
  >>> is_polite(7) == 11
  """
  if n == 1:
    return 1
  else:
    return is_polite(n-1) + 2

def is_polite_2(n):
  """
  Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
  >>> is