def split_Arr(l, n):
  """
  Write a python function to split a list at the nth eelment and add the first part to the end.
  >>> split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
  """
  return l[n:] + l[:n]

def split_Arr_2(l, n):
  """
  Write a python function to split a list at the nth eelment and add the first part to the end.
  >>> split_Arr_2([12,10,5,6,52,