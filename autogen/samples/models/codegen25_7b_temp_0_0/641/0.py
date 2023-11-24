def is_nonagonal(n): 
  """
  Write a function to find the nth nonagonal number.
  >>> is_nonagonal(10) == 325
  """
  return (n*(n+1)*(2*n+1))/6

def is_triangular(n):
  """
  Write a function to find the nth triangular number.
  >>> is_triangular(10) == 55
  """
  return (n*(n+1))/2

