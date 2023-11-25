import math 
def count_divisors(n) : 
  """
  Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
  """
  count = 0
  for i in range(1, n+1) : 
    if n % i == 0 : 
      count += 1
  return count

def is_prime(n) : 
  """
  Write a python function to check whether the number is prime or not. https://www.w3resource