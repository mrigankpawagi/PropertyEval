def diff_even_odd(list1):
  """
  Write a function to find the difference of the first even and first odd number of a given list.
  """
  even = 0
  odd = 0
  for i in list1:
    if i % 2 == 0:
      even = i
    else:
      odd = i
  return even - odd

def sum_even_odd(list1):
  """
  Write a function to find the sum of the first even and