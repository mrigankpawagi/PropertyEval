def max_product_tuple(list1):
  """
  Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
  """
  max_product = 0
  for i in range(len(list1)):
    for j in range(i+1, len(list1)):
      product = list1[i][0] * list1[i][1] * list1[j][0] * list1[j][1]
      if product