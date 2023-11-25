import re
def remove_parenthesis(items):
  """
  Write a function to remove the parenthesis and what is inbetween them from a string.
  """
  # remove the parenthesis
  items = re.sub(r'\(.*\)', '', items)
  # remove the spaces
  items = re.sub(r'\s', '', items)
  return items

def remove_parenthesis_v2(items):
  """
  Write a function to remove