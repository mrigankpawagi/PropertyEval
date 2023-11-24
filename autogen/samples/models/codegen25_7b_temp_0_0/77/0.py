def is_Diff(n): 
  """
  Write a python function to find whether a number is divisible by 11.
  >>> is_Diff (12345) == False
  """
  if n % 11 == 0:
    return True
  else:
    return False

def is_Perfect(n):
  """
  Write a python function to find whether a number is perfect or not.
  >>> is_Perfect (6) == True
  """
  sum = 0
  for i in range(1