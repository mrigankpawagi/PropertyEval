import math
def is_not_prime(n):
  """
  Write a python function to identify non-prime numbers.
  """
  if n == 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def is_prime(n):
  """
  Write a python function to identify prime numbers.
  """
