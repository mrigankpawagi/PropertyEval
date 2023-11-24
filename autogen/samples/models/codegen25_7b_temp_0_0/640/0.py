import re
def remove_parenthesis(items):
  """
  Write a function to remove the parenthesis and what is inbetween them from a string.
  >>> remove_parenthesis(["python (chrome)"])==("python")
  """
  for item in items:
    item = re.sub(r'\([^)]*\)', '', item)
  return items

def remove_parenthesis_2(items):
  """
  Write a function to remove the parenthesis and what is inbetween them from a string.
  >>> remove_parenthesis(["