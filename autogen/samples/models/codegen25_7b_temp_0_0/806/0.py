def max_run_uppercase(test_str):
  """
  Write a function to find maximum run of uppercase characters in the given string.
  >>> max_run_uppercase('GeMKSForGERksISBESt') == 5
  """
  max_run = 0
  for i in range(len(test_str)):
    if test_str[i].isupper():
      max_run += 1
    else:
      max_run = 0
    if max_run > max_run_uppercase.max_run:
      max_run_