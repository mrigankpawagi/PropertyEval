def new_tuple(test_list, test_str):
  """
  Write a function to create a new tuple from the given string and list.
  >>> new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
  """
  return tuple(test_list + [test_str])

def new_list(test_tuple, test_str):
  """
  Write a function to create a new list from the given string and tuple.
  >>> new_list(("WEB", "is"), "best") == ['WEB', 'is', '