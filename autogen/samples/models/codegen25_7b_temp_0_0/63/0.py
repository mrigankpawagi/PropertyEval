def max_difference(test_list):
  """
  Write a function to find the maximum difference between available pairs in the given tuple list.
  >>> max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
  """
  return max(abs(a - b) for a, b in test_list)

def max_difference_2(test_list):
  """
  Write a function to find the maximum difference between available pairs in the given tuple list.
  >>> max_difference_2([(3, 5), (1, 7),