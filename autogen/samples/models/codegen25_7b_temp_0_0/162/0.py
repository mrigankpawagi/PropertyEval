def sum_series(n):
  """
  Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
  >>> sum_series(6) == 12
  """
  if n <= 0:
    return 0
  else:
    return n + sum_series(n - 2)


def sum_series_2(n):
  """
  Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2)