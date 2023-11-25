import re
def text_match_zero_one(text):
  """
  Write a function that matches a string that has an 'a' followed by one or more 'b's. https://www.w3resource.com/python-exercises/re/python-re-exercise-3.php
  """
  pattern = "ab*"
  result = re.findall(pattern, text)
  return result

def text_match_zero_one_or_more(text):
  """
  Write a function that matches a string that has an 'a' followed by one or more 'b's. https://www.w3resource