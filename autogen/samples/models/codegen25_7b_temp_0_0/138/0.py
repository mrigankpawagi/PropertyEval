def is_Sum_Of_Powers_Of_Two(n): 
  """
  Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
  """
  if n == 0:
    return False
  while n != 0:
    if n % 2 == 0:
      n = n // 2
    else:
      return False
  return True

def is_Sum_Of_Powers_Of_Two_1(n):
  """
  Write a python function to