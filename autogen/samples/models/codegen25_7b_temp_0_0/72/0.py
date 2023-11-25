def dif_Square(n): 
  """
  Write a python function to check whether the given number can be represented as the difference of two squares or not.
  """
  if n == 0:
    return True
  elif n < 0:
    return False
  else:
    for i in range(1, n):
      if i*i == n:
        return True
      elif i*i > n:
        return False

def dif_Square(n):
