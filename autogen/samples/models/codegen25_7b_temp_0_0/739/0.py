import math 
def find_Index(n): 
  """
  Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
  """
  n = int(n)
  if n == 0:
    return 0
  else:
    return int(n * (n + 1) / 2)

def find_Triangular_Number(n):
  """
  Write a python function to find the nth triangular number. https://www.geeksforgeeks.