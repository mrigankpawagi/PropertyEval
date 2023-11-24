import re
def text_match_three(text):
  """
  Write a function that matches a string that has an a followed by three 'b'.
  >>> not text_match_three("ac")
  """
  pattern = "ab{3}"
  if re.search(pattern,  text):
    return True
  return False

def text_match_two(text):
  """
  Write a function that matches a string that has an a followed by two 'b'.
  >>> not text_match_two("ac")
 