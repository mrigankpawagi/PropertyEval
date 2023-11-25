def frequency_lists(list1):
  """
  Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
  """
  frequency = {}
  for i in list1:
    for j in i:
      if j in frequency:
        frequency[j] += 1
      else:
        frequency[j] = 1
  return frequency

def flatten_list(list1):
  """
  Write a function to flatten a list of