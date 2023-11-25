import re
def remove_all_spaces(text):
  """
  Write a function to remove all whitespaces from a string.
  """
  return re.sub(r'\s+', '', text)

def remove_all_special_characters(text):
  """
  Write a function to remove all special characters from a string.
  """
  return re.sub(r'[^a-zA-Z0-9\s]', '