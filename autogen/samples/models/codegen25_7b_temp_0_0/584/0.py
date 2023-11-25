import re
def find_adverbs(text):
  """
  Write a function to find the first adverb ending with ly and its positions in a given string.
  """
  adverbs = re.findall(r'\b[a-zA-Z]+ly\b', text)
  return adverbs

def find_adjectives(text):
  """
  Write a function to find the first adjective ending withly and its positions in a given string.
  """
  adjectives =