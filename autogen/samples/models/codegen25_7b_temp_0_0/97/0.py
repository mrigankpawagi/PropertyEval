def frequency_lists(list1):
  """
  Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
  >>> frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
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