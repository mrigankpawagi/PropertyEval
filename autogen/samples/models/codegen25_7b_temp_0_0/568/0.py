def empty_list(length):
  """
  Write a function to create a list of N empty dictionaries.
  """
  return [{} for _ in range(length)]


def create_list_of_dicts(length):
  """
  Write a function to create a list of N dictionaries with keys from 1 to N.
  """
  return [{i: i} for i in range(1, length + 1)]


def