def len_log(list1):
  """
  Write a python function to find the length of the longest word.
  """
  return len(max(list1, key=len))

def count_vowels(string):
  """
  Write a python function to count the number of vowels in a given string.
  """
  vowels = 0
  for i in string:
    if i in 'aeiou':
      vowels