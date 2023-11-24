def min_k(test_list, K):
  """
  Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
  >>> min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
  """
  return sorted(test_list, key=lambda x: x[1])[:K]

def min_k_2(test_list, K):
  """
  Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-