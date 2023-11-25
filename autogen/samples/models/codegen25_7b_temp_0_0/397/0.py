def median_numbers(a,b,c):
  """
  Write a function to find the median of three numbers.
  """
  if a > b:
    if b > c:
      return b
    elif a < c:
      return a
    else:
      return c
  elif a < b:
    if b > c:
      return b
    elif a > c:
      return a
    else:
      return