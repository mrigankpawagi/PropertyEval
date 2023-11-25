import re
def find_char_long(text):
  """
  Write a function to find all words which are at least 4 characters long in a string.
  """
  return [word for word in text.split() if len(word) >= 4]

def find_char_long_v2(text):
  """
  Write a function to find all words which are at least 4 characters long in a string.
  """
  return [word for word in text.split() if len(word