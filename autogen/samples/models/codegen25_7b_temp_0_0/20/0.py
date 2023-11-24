def is_woodall(x): 
  """
  Write a function to check if the given number is woodball or not.
  >>> is_woodall(383) == True
  """
  if x == 0:
    return False
  if x == 1:
    return True
  if x % 2 == 0:
    return False
  if x % 3 == 0:
    return False
  if x % 5 == 0:
    return False
  if x % 7 == 0:
    return False
 