def max_length_list(input_list):
  """
  Write a function to find the list with maximum length.
  >>> max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
  """
  max_length = 0
  max_list = []
  for i in input_list:
    if len(i) > max_length:
      max_length = len(i)
      max_list = i
  return max_length, max_list

def max_length_list_2(input_list