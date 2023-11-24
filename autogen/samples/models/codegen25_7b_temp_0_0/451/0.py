import re
def remove_whitespaces(text1):
  """
  Write a function to remove all whitespaces from the given string.
  >>> remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
  """
  return re.sub(r'\s+', '', text1)

def remove_punctuation(text2):
  """
  Write a function to remove all punctuation from the given string.
  >>> remove_punctuation('Hello, how are you?') == 'Hellohowareyou'
  """
 