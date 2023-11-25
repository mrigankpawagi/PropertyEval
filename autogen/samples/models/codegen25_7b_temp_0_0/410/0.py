def min_val(listval):
  """
  Write a function to find the minimum value in a given heterogeneous list.
  """
  min_val = listval[0]
  for i in listval:
    if i < min_val:
      min_val = i
  return min_val

def max_val(listval):
  """
  Write a function to find the maximum value in a given heterogeneous list.
  """
 