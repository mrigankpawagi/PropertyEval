import math 
def count_divisors(n) : 
  """
  Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
  >>> count_divisors(10)
  """
  count = 0
  for i in range(1, n+1) : 
    if n % i == 0 : 
      count += 1
  if count % 2 == 0 : 
    return True
  else : 
    return False

def is_prime(n) : 
  """
  Write a