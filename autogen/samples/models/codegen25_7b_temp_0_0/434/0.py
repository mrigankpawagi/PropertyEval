import re
def text_match_one(text):
  """
  Write a function that matches a string that has an a followed by one or more b's.
  >>> text_match_one("ac")==False
  """
  pattern = "ab*"
  result = re.findall(pattern, text)
  return bool(result)

def text_match_two(text):
  """
  Write a function that matches a string that has an a followed by one or more b's.
  >>> text_match_two("ac")==False