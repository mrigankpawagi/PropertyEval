def tuple_to_dict(test_tup):
  """
  Write a function to convert the given tuple to a key-value dictionary using adjacent elements. https://www.geeksforgeeks.org/python-convert-tuple-to-adjacent-pair-dictionary/
  >>> tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
  """
  return {test_tup[i]: test_tup[i + 1] for i in range(0, len(test_tup), 2)}

def dict_to_tuple(test_dict):
  """
  Write a function to convert the given dictionary to a tuple using adjacent elements. https://www.geeks