def word_len(s): 
  """
  Write a python function to check whether the length of the word is odd or not.
  """
  if len(s) % 2 == 0:
    return False
  else:
    return True

def odd_even(s):
  """
  Write a python function to check whether the length of the word is odd or even.
  """
  if len(s) % 2 == 0:
    return "Even"