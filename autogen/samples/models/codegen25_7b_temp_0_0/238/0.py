def number_of_substrings(str): 
  """
  Write a python function to count the number of non-empty substrings of a given string.
  >>> number_of_substrings("abc") == 6
  """
  return len(str) * len(str) + len(str) - 1

def number_of_substrings_2(str):
  """
  Write a python function to count the number of non-empty substrings of a given string.
  >>> number_of_substrings_2("abc") == 6
  """