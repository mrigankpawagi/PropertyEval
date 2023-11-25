import re
def snake_to_camel(word):
  """
  Write a function to convert the given snake case string to camel case string.
  """
  return ''.join(x.capitalize() for x in word.split('_'))

def camel_to_snake(word):
  """
  Write a function to convert the given camel case string to snake case string.
  """
  return ''.join(x.lower() for x in re.findall('