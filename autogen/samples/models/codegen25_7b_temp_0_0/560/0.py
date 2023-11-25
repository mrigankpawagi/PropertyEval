def union_elements(test_tup1, test_tup2):
  """
  Write a function to find the union of the elements of two given tuples and output them in sorted order.
  """
  return sorted(set(test_tup1) | set(test_tup2))

print(union_elements((1, 2, 3, 4, 5), (5, 6, 7, 8, 9)))

def intersection_elements(test_tup1, test_tup2):
  """
