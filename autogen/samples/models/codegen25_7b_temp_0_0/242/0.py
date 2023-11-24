def count_charac(str1):
  """
  Write a function to count the total number of characters in a string.
  >>> count_charac("python programming")==18
  """
  return len(str1)

def count_charac_2(str1):
  """
  Write a function to count the total number of characters in a string.
  >>> count_charac_2("python programming")==18
  """
  return sum(1 for i in str1)

def count_char