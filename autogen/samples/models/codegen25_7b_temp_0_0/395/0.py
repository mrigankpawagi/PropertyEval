def first_non_repeating_character(str1):
  """
  Write a python function to find the first non-repeated character in a given string.
  >>> first_non_repeating_character("abcabc") == None
  """
  for i in str1:
    if str1.count(i) == 1:
      return i
  return None

def first_non_repeating_character_2(str1):
  """
  Write a python function to find the first non-repeating character in a given string.
  >>> first_non_