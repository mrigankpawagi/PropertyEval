def is_num_decagonal(n): 
  """
  Write a function to find the nth decagonal number.
  >>> is_num_decagonal(3) == 27
  """
  return n * (3 * n - 2) // 2

def is_num_hexagonal(n): 
  """
  Write a function to find the nth hexagonal number.
  >>> is_num_hexagonal(3) == 27
  """
  return n * (2 * n - 1)

def