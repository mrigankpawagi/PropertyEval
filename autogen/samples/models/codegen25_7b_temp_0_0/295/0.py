def sum_div(number):
  """
  Write a function to return the sum of all divisors of a number.
  """
  sum = 0
  for i in range(1, number):
    if number % i == 0:
      sum += i
  return sum

def is_prime(number):
  """
  Write a function to determine if a number is prime.
  """
  if number == 1:
    return False
  for