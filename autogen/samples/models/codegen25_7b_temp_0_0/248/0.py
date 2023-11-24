def harmonic_sum(n):
  """
  Write a function that takes in an integer n and calculates the harmonic sum of n-1.
  >>> math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
  """
  return 1 / (n - 1) + harmonic_sum(n - 1) if n > 1 else 0

def harmonic_sum_2(n):
  """
  Write a function that takes in an integer n and calculates the harmonic sum of n-1.
  >>> math.isclose(harmonic_sum_2(7