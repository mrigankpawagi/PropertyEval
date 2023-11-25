def is_Even(n) : 
  """
  Write a python function to check whether the given number is even or not.
  """
  if n % 2 == 0 : 
    return True
  else : 
    return False

def is_Prime(n) : 
  """
  Write a python function to check whether the given number is prime or not.
  """
  if n > 1 : 
    for i in range(2, n)