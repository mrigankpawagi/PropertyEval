def geometric_sum(n):
  """
  Write a function to calculate the geometric sum of n-1. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-9.php
  """
  if n == 1:
    return 1
  return n * geometric_sum(n - 1)

def geometric_sum_2(n):
  """
  Write a function to calculate the geometric sum of n-1. https://www.w3resource.com/python-exercises/data-structures-and-