import re
def text_match_wordz(text):
  """
  Write a function that matches a word containing 'z'.
  """
  pattern = re.compile(r'\w*z\w*')
  result = pattern.findall(text)
  return result

print(text_match_wordz("The quick brown fox jumps over the lazy dog"))

def text_match_wordz(text):
  """
  Write a function that