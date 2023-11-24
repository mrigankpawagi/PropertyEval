def similar_elements(test_tup1, test_tup2):
  """
  Write a function to find the shared elements from the given two lists.
  >>> set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
  """
  return set(test_tup1).intersection(set(test_tup2))

def find_duplicates(test_list):
  """
  Write a function to find the duplicates in the given list.
  >>> find_duplicates([1, 2, 3, 4, 5, 6, 7,