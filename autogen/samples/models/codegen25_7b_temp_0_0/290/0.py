def max_length(list1):
  """
  Write a function to find the list of maximum length in a list of lists.
  """
  max_len = 0
  for i in list1:
    if len(i) > max_len:
      max_len = len(i)
  return max_len

def max_length_2(list1):
  """
  Write a function to find the list of maximum length in a list of lists.