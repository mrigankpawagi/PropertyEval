def count_Primes_nums(n):
  """
  Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
  >>> count_Primes_nums(5) == 2
  """
  if n < 2:
    return 0
  else:
    return count_Primes_nums(n-1) + count_Primes_nums(n-2) + count_Primes_nums(n-3)

def count_Primes_nums_2(n):
  """
 