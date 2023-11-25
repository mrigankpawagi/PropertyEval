def max_run_uppercase(test_str):
  """
  Write a function to find maximum run of uppercase characters in the given string.
  """
  max_run = 0
  current_run = 0
  for i in range(len(test_str)):
    if test_str[i].isupper():
      current_run += 1
    else:
      current_run = 0
    max_run = max(max_run, current_run)
 