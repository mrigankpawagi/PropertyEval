def empty_list(length):
  """
  Write a function to create a list of N empty dictionaries.
  >>> empty_list(5)==[{},{},{},{},{}]
  """
  return [{} for _ in range(length)]

def create_list(length):
  """
  Write a function to create a list of N dictionaries with keys from 1 to N.
  >>> create_list(5)==[{1:1},{2:2},{3:3},{4:4},