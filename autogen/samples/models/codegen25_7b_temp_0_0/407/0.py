def rearrange_bigger(n):
  """
  Write a function to create the next bigger number by rearranging the digits of a given number.
  """
  # convert n to string
  n = str(n)
  # find the first digit that is not in order
  for i in range(len(n) - 1):
    if n[i] > n[i + 1]:
      # find the digit that is not in order
      for j in range(i + 1