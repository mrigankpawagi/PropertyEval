def list_to_float(test_list):
  """
  Write a function to convert all possible convertible elements in a list of lists to floats.
  """
  for i in range(len(test_list)):
    for j in range(len(test_list[i])):
      try:
        test_list[i][j] = float(test_list[i][j])
      except ValueError:
        pass
  return test_list

def list_to