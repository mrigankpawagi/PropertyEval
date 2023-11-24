def ascii_value(k):
  """
  Write a function to find the ascii value of a character.
  >>> ascii_value('A')==65
  """
  return ord(k)

def is_vowel(k):
  """
  Write a function to check if a character is a vowel.
  >>> is_vowel('a')
  True
  >>> is_vowel('b')
  False
  """
  return k in ['a','e','