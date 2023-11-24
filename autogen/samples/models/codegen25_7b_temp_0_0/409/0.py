def min_product_tuple(list1):
  """
  Write a function to find the minimum product from the pairs of tuples within a given list.
  >>> min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
  """
  list1.sort(key=lambda x: x[0]*x[1])
  return list1[0][0]*list1[0][1]

def min_product_tuple_2(list1):
  """
  Write a function to find the minimum product from the pairs of tuples within a given