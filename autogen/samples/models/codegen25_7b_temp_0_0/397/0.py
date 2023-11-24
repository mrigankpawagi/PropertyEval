def median_numbers(a,b,c):
  """
  Write a function to find the median of three numbers.
  >>> median_numbers(25,55,65)==55.0
  """
  return sorted([a,b,c])[1]

def is_prime(n):
  """
  Write a function to check if a number is prime or not.
  >>> is_prime(5)
  True
  >>> is_prime(10)
  False
  """
  if n == 1:
