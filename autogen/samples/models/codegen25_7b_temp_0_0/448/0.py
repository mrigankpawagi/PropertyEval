def cal_sum(n): 
  """
  Write a function to calculate the sum of perrin numbers.
  >>> cal_sum(9) == 49
  """
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return cal_sum(n-1) + n

def cal_sum_2(n):
  """
  Write a function to calculate the sum of perrin numbers.
  >>> cal_sum_2