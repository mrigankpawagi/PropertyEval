def check_value(dict, n):
  """
  Write a function to check if all values are same in a dictionary.
  """
  return len(set(dict.values())) == 1 and dict.values()[0] == n

def check_value_2(dict, n):
  """
  Write a function to check if all values are same in a dictionary.
  """
  return all(dict.values()) == n

def check_value