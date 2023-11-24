def rearrange_bigger(n):
  """
  Write a function to create the next bigger number by rearranging the digits of a given number.
  >>> rearrange_bigger(12)==21
  """
  n = str(n)
  n = list(n)
  n = [int(i) for i in n]
  n = sorted(n)
  n = [str(i) for i in n]
  n = ''.join(n)
  n = int(n)
  return n

