def remove_nested(test_tup):
  """
  Write a function to remove tuples from the given tuple.
  >>> remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
  """
  return tuple(x for x in test_tup if not isinstance(x, tuple))

def remove_duplicates(test_tup):
  """
  Write a function to remove duplicates from the given tuple.
  >>> remove_duplicates((1, 2, 3, 4, 5, 6, 7,