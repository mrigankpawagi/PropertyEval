def add_dict_to_tuple(test_tup, test_dict):
  """
  Write a function to add a dictionary to the tuple. The output should be a tuple.
  >>> add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
  """
  return test_tup + (test_dict,)

def add_dict_to_tuple_2(test_tup, test_dict):
  """
  Write a function to add a dictionary to the tuple. The output should be a tuple.
  >>> add_dict_to_tuple_2((4, 5