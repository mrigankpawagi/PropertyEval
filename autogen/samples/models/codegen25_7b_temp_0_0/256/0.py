def count_Primes_nums(n):
  """
  Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
  """
  if n < 2:
    return 0
  else:
    return count_Primes_nums(n-1) + 1 if is_prime(n) else count_Primes_nums(n-1)

def is_prime(n):
  """
  Write a python function that takes in a non-