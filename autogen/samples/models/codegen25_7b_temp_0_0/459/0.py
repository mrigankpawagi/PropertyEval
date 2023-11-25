import re
def remove_uppercase(str1):
  """
  Write a function to remove uppercase substrings from a given string.
  """
  return re.sub(r'[A-Z]', '', str1)

def remove_lowercase(str1):
  """
  Write a function to remove lowercase substrings from a given string.
  """
  return re.sub(r'[a-z]', '', str1)

def