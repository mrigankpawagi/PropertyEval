import re
def text_lowercase_underscore(text):
  """
  Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
  >>> text_lowercase_underscore("aab_cbbbc")==(True)
  """
  return re.search("[a-z_]+", text)

def text_lowercase_underscore_2(text):
  """
  Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
  >>> text_lowercase_underscore_2("aab