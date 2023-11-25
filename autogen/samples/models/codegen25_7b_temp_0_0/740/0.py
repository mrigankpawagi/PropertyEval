def tuple_to_dict(test_tup):
  """
  Write a function to convert the given tuple to a key-value dictionary using adjacent elements. https://www.geeksforgeeks.org/python-convert-tuple-to-adjacent-pair-dictionary/
  """
  test_dict = {}
  for i in range(0, len(test_tup), 2):
    test_dict[test_tup[i]] = test_tup[i+1]
  return test_dict

def dict_to_tuple(test_dict):
  """
  Write a function