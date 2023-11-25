def last(arr,x):
  """
  Write a python function to find the last position of an element in a sorted array.
  """
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
      if mid == len(arr) - 1 or arr[mid + 1] != x:
        return mid
      else:
        low =