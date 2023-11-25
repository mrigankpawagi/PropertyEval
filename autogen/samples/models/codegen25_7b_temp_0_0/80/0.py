def tetrahedral_number(n): 
  """
  Write a function to find the nth tetrahedral number.
  """
  return int(n * (n + 1) * (n + 2) / 6)

def is_tetrahedral_number(n):
  """
  Write a function to determine if a number is a tetrahedral number.
  """
  return n == tetrahedral_number(n)

def is_