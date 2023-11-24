import re
def replace_specialchar(text):
  """
  Write a function to replace all occurrences of spaces, commas, or dots with a colon.
  >>> replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
  """
  text = re.sub(r'\s', ':', text)
  text = re.sub(r'\,', ':', text)
  text = re.sub(r'\.', ':', text)
  return text

def remove_punctuation(text):
  """
  Write a