def find_First_Missing(array,start=0,end=None):
  """
  Write a python function to find the smallest missing number from a sorted list of natural numbers.
  >>> find_First_Missing([0,1,2,3]) == 4
  """
  if end is None:
    end = len(array) - 1
  if start == end:
    return start + 1
  mid = (start + end) // 2
  if array[mid] == mid + 1:
    return find_First_Missing(array,mid + 1,end)
  elif array[