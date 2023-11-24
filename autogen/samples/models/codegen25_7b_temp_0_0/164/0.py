import math 
def div_sum(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total

def are_equivalent(num1, num2): 
  """
  Write a function to determine if the sum of the divisors of two integers are the same.
  >>> are_equivalent(36, 57) == False
  """
  return div_sum(num1) == div_sum(num2)

def is_prime(num):
  """
  Write a function to determine if a number is prime.
  >>> is_prime(2) == True
  >>> is_prime(3) == True
  >>> is_prime(4) == False