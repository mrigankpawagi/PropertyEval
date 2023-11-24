def odd_values_string(str):
  """
  Write a python function to remove the characters which have odd index values of a given string.
  >>> odd_values_string('abcdef') == 'ace'
  """
  return ''.join(str[i] for i in range(len(str)) if i % 2 == 0)

def odd_values_list(lst):
  """
  Write a python function to remove the characters which have odd index values of a given list.
  >>> odd_values_list([1, 2, 3