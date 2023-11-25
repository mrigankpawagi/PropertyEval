def is_Diff(n): 
  """
  Write a python function to find whether a number is divisible by 11.
  """
  if n % 11 == 0:
    return True
  else:
    return False

def is_Perfect(n):
  """
  Write a python function to find whether a number is perfect or not.
  """
  sum = 0
  for i in range(1, n):
    if n % i == 0