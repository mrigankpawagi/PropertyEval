def max_product_tuple(list1):
  """
  Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
  >>> max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
  """
  list1.sort(key=lambda x: x[0]*x[1])
  return list1[-1][0]*list1[-1][1]

def max_product_tuple_2(list1):
  """
  Write a function to find the maximum absolute product between numbers in pairs of tu