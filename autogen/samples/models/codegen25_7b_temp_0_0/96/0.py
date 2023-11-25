def divisor(n):
  """
  Write a python function to find the number of divisors of a given integer.
  """
  count = 0
  for i in range(1, n+1):
    if n % i == 0:
      count += 1
  return count

def divisor_sum(n):
  """
  Write a python function to find the sum of divisors of a given integer.
  """
  sum =