import re
def text_match_two_three(text):
  """
  Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
  """
  pattern = re.compile(r'ab{2,3}')
  result = pattern.search(text)
  return result != None

def text_match_two_three_two(text):
  """
  Write a function that checks whether a string contains the 'a' character followed by two or three 'b'