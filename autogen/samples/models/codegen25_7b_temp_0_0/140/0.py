def extract_singly(test_list):
  """
  Write a function to flatten the list of lists into a single set of numbers.
  >>> set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
  """
  return set([item for sublist in test_list for item in sublist])

def extract_doubly(test_list):
  """
  Write a function to flatten the list of lists into a single set of numbers.
  >>> set(extract_doubly([[3, 4, 5], [4,