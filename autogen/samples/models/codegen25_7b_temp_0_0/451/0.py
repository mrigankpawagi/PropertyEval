import re
def remove_whitespaces(text1):
  """
  Write a function to remove all whitespaces from the given string.
  """
  return re.sub(r'\s+', '', text1)

def remove_punctuation(text2):
  """
  Write a function to remove all punctuation from the given string.
  """
  return re.sub(r'[^\w\s]', '', text2)

def