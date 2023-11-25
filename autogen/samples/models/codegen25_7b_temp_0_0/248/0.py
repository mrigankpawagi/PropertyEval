def harmonic_sum(n):
  """
  Write a function that takes in an integer n and calculates the harmonic sum of n-1.
  """
  return 1 / (n - 1) + harmonic_sum(n - 1) if n > 1 else 1


def factorial(n):
  """
  Write a function that takes in an integer n and calculates the factorial of n.
  """
  return n * factorial(n - 1) if n > 1 else 1