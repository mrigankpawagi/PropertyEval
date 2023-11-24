def is_octagonal(n): 
  """
  Write a function to find the nth octagonal number.
  >>> is_octagonal(5) == 65
  """
  return n * (3 * n - 2) / 2

def is_pentagonal(n): 
  """
  Write a function to find the nth pentagonal number.
  >>> is_pentagonal(5) == 35
  """
  return n * (3 * n - 1) / 2

def is_