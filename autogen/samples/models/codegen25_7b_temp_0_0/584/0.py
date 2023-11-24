import re
def find_adverbs(text):
  """
  Write a function to find the first adverb ending with ly and its positions in a given string.
  >>> find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
  """
  return re.findall(r'\b\w+ly\b', text)

def find_digits(text):
  """
  Write a function to find all digits in a given string.
  >>> find_digits("I have a 1.5 pound bag.") == '1.5'
  """
 