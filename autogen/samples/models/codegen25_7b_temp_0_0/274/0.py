import math  
def even_binomial_Coeff_Sum( n): 
  """
  Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
  >>> even_binomial_Coeff_Sum(4) == 8
  """
  if n == 0: 
    return 0
  if n == 1: 
    return 1
  if n == 2: 
    return 2
  if n == 3: 
    return 6
  if n == 4: 
    return 20
  if n == 5: 
    return 72
  if n