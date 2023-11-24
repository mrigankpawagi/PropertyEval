def dif_Square(n): 
  """
  Write a python function to check whether the given number can be represented as the difference of two squares or not.
  >>> dif_Square(5) == True
  """
  if n == 1:
    return True
  elif n == 2:
    return False
  else:
    for i in range(2, n):
      if i*i == n:
        return True
      elif i*i > n:
        return False

def dif_Square(n):
