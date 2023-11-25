def bell_number(n):   
  """
  Write a function to find the number of ways to partition a set of Bell numbers.
  """
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 5
  if n == 4:
    return 15
  if n == 5:
    return 52
  if n == 6:
    return