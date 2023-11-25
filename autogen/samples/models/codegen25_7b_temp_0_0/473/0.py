def tuple_intersection(test_list1, test_list2):
  """
  Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
  """
  result = []
  for i in test_list1:
    if i in test_list2:
      result.append(i)
  return result

print(tuple_intersection([(1, 2), (3, 4), (5, 6)], [(5, 6), (7, 8), (9,