def max_val(listval):
  """
  Write a function to find the maximum value in a given heterogeneous list.
  """
  max_val = listval[0]
  for i in listval:
    if i > max_val:
      max_val = i
  return max_val

def min_val(listval):
  """
  Write a function to find the minimum value in a given heterogeneous list.
  """
 