def get_max_sum (n):
  """
  Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
  >>> get_max_sum(60) == 106
  """
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 3
  elif n == 4:
    return 4
  elif n == 5:
    return 5
  elif n == 6:
    return 6
  elif n