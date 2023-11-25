def remove_nested(test_tup):
  """
  Write a function to remove tuples from the given tuple.
  """
  return tuple(x for x in test_tup if type(x) != tuple)

print(remove_nested((1, 2, (3,), (4, 5))))

# Write a function to find the maximum number in the given tuple.
def max_tup(test_tup):
  """
 