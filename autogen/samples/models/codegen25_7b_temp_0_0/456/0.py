def reverse_string_list(stringlist):
  """
  Write a function to reverse each string in a given list of string values.
  >>> reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
  """
  return [s[::-1] for s in stringlist]

def reverse_string_list_recursive(stringlist):
  """
  Write a function to reverse each string in a given list of string values.
  >>> reverse_string_list_recursive(['Red', 'Green', 'Blue', 'White', '