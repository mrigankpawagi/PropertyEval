def tetrahedral_number(n): 
  """
  Write a function to find the nth tetrahedral number.
  >>> tetrahedral_number(5) == 35
  """
  return int(n * (n + 1) * (n + 2) / 6)

def fibonacci_number(n):
  """
  Write a function to find the nth Fibonacci number.
  >>> fibonacci_number(5) == 5
  """
  if n == 0:
    return