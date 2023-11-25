def min_product_tuple(list1):
  """
  Write a function to find the minimum product from the pairs of tuples within a given list.
  """
  min_product = list1[0][0] * list1[0][1]
  for i in range(len(list1)):
    if list1[i][0] * list1[i][1] < min_product:
      min_product = list1[i][0] * list1[i][