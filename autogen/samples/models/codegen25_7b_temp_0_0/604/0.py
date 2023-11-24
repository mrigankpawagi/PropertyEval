def reverse_words(s):
  """
  Write a function to reverse words seperated by spaces in a given string.
  >>> reverse_words("python program")==("program python")
  """
  return ' '.join(reversed(s.split()))

def reverse_words_in_string(s):
  """
  Write a function to reverse words seperated by spaces in a given string.
  >>> reverse_words("python program")==("program python")
  """
  return ' '.join(re