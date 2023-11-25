def new_tuple(test_list, test_str):
  """
  Write a function to create a new tuple from the given string and list.
  """
  return tuple(test_list) + (test_str,)

print(new_tuple([1, 2, 3], "Hello"))

# Output: (1, 2, 3, 'Hello')

#%%

def new_tuple(test_list, test_str):
  """
  Write a function