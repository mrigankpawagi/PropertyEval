import re
def text_match_wordz(text):
  """
  Write a function that matches a word containing 'z'.
  >>> text_match_wordz("pythonz.")==True
  """
  x = re.search("[a-zA-Z]*z[a-zA-Z]*", text)
  if x:
    return True
  else:
    return False

def text_match_wordz_1(text):
  """
  Write a function that matches a word containing 'z