def string_to_tuple(str1):
  """
  Write a function to convert a given string to a tuple of characters.
  >>> string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
  """
  return tuple(str1)

def tuple_to_string(tup1):
  """
  Write a function to convert a given tuple to a string.
  >>> tuple_to_string(('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0'))==