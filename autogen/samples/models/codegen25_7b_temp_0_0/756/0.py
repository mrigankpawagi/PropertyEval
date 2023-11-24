import re
def text_match_zero_one(text):
  """
  Write a function that matches a string that has an 'a' followed by one or more 'b's. https://www.w3resource.com/python-exercises/re/python-re-exercise-3.php
  >>> text_match_zero_one("ac")==False
  """
  pattern = "ab*"
  if re.search(pattern, text):
    return True
  return False

def text_match_zero_or_more(text):
  """
  Write a function that matches a string that has an 'a' followed by one or more 'b's. https://www.w3resource