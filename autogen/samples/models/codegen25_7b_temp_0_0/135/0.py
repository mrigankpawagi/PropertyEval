def hexagonal_num(n): 
  """
  Write a function to find the nth hexagonal number.
  >>> hexagonal_num(10) == 190
  """
  return (n * (n + 1)) * (3 * n - 1) // 2

def hexagonal_num_2(n):
  """
  Write a function to find the nth hexagonal number.
  >>> hexagonal_num_2(10) == 190
  """
  return n * (2 * n