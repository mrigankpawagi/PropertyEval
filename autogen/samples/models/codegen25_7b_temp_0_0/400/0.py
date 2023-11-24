def extract_freq(test_list):
  """
  Write a function to extract the number of unique tuples in the given list.
  >>> extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
  """
  return len(set(test_list))

def extract_freq_2(test_list):
  """
  Write a function to extract the number of unique tuples in the given list.
  >>> extract_freq_2([(3, 4), (1, 2), (4, 3), (5, 6)]