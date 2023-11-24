def tuple_intersection(test_list1, test_list2):
  """
  Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
  >>> tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
  """
  return set(test_list1).intersection(set(test_list2))

def tuple_union(test_list1, test_list2):
  """
  Write a function to find the tuple union of elements in the given tuple list irrespective of their order.
  >>> tuple_union([(3, 4), (5