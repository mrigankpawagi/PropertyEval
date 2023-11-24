def last(arr,x):
  """
  Write a python function to find the last position of an element in a sorted array.
  >>> last([1,2,3],1) == 0
  """
  if x in arr:
    return arr.index(x)
  else:
    return -1

def first(arr,x):
  """
  Write a python function to find the first position of an element in a sorted array.
  >>> first([1,2,3],1) == 1
  """
 