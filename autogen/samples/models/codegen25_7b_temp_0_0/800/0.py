import re
def remove_all_spaces(text):
  """
  Write a function to remove all whitespaces from a string.
  >>> remove_all_spaces('python  program')==('pythonprogram')
  """
  return re.sub(r'\s+', '', text)

def remove_all_spaces_v2(text):
  """
  Write a function to remove all whitespaces from a string.
  >>> remove_all_spaces_v2('python  program')==('pythonprogram')
  """
 