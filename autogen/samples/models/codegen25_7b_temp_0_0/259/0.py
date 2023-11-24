def maximize_elements(test_tup1, test_tup2):
  """
  Write a function to maximize the given two tuples.
  >>> maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
  """
  return tuple(map(lambda x: max(x), zip(test_tup1, test_tup2)))

def maximize_elements_2(test_tup1, test_tup2):
  """
  Write a function to maximize the given two tuples.
  >>> maximize_elements_2((