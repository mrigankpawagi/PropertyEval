def max_length(list1):
  """
  Write a function to find the list of maximum length in a list of lists.
  >>> max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
  """
  max_len = 0
  max_list = []
  for i in list1:
    if len(i) > max_len:
      max_len = len(i)
      max_list = i
  return max_len, max_list

def max_length_2(list1):
  """