import math  
def even_binomial_Coeff_Sum( n): 
  """
  Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
  """
  sum = 0
  for i in range(0, n+1): 
    if i % 2 == 0: 
      sum += math.factorial(i) 
  return sum 

def odd_binomial_Coeff_Sum( n): 
  """
  Write a python function that takes in a