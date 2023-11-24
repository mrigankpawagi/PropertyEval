def rear_extract(test_list):
  """
  Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
  >>> rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
  """
  return [x[-1] for x in test_list]

def reverse_list(test_list):
  """
  Write a function that takes in a list and returns a new list with the elements in reverse order.
  >>> reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3