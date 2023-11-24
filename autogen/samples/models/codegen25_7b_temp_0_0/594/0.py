def diff_even_odd(list1):
  """
  Write a function to find the difference of the first even and first odd number of a given list.
  >>> diff_even_odd([1,3,5,7,4,1,6,8])==3
  """
  even_list = []
  odd_list = []
  for i in list1:
    if i % 2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)
  return even_list[0] - odd_list[0]

def sum_