def is_undulating(n): 
  """
  Write a function to check whether the given number is undulating or not.
  """
  if n < 0:
    return False
  if n == 0:
    return True
  if n == 1:
    return False
  if n == 2:
    return True
  if n == 3:
    return False
  if n == 4:
    return True
  if n == 5:
    return