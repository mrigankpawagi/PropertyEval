def list_to_float(test_list):
  """
  Write a function to convert all possible convertible elements in a list of lists to floats.
  >>> list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
  """
  return [tuple(map(float, x)) for x in test_list]

def list_to_int(test_list):
  """
  Write a function to convert all possible convertible elements in a list of lists to integers.
  >>> list_to_int( [("3", "4"), ("1", "26