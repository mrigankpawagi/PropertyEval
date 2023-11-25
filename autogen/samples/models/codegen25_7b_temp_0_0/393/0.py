def max_length_list(input_list):
  """
  Write a function to find the list with maximum length.
  """
  max_length = 0
  max_length_list = []
  for i in input_list:
    if len(i) > max_length:
      max_length = len(i)
      max_length_list = [i]
    elif len(i) == max_length:
      max_length