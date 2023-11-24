import math 
def find_Index(n): 
  """
  Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
  >>> find_Index(2) == 4
  """
  return int(n*(n+1)/2)

def find_Index_2(n): 
  """
  Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits