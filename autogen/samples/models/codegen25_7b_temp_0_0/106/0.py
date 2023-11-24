def add_lists(test_list, test_tup):
  """
  Write a function to append the given list to the given tuples.
  >>> add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
  """
  return test_list + list(test_tup)

def add_lists_2(test_list, test_tup):
  """
  Write a function to append the given list to the given tuples.
  >>> add_lists_2([5, 6, 7], (9, 10)) == (9, 10