import re
def text_match_two_three(text):
  """
  Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
  >>> text_match_two_three("ac")==(False)
  """
  pattern = re.compile(r'ab{2,3}')
  result = pattern.search(text)
  return bool(result)

def text_match_two_three_1(text):
  """
  Write a function that checks whether a string contains the 'a' character followed by two or three 'b