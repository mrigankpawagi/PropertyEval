def odd_Equivalent(s,n): 
  """
  Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
  >>> odd_Equivalent("011001",6) == 3
  """
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 1
  if n == 3:
    return 2
  if n == 4:
    return 2
  if n == 5:
    return 3
  if n == 6:
    return