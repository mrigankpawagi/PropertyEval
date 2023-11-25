def extract_rear(test_tuple):
  """
  Write a function to extract only the rear index element of each string in the given tuple.
  """
  return tuple(map(lambda x: x[-1], test_tuple))

print(extract_rear(("hello", "world", "!")))

# Write a function to extract only the first index element of each string in the given tuple.
def extract_front(test_tuple):
  """
 