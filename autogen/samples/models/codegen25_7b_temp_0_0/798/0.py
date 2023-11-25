def _sum(arr):  
  """
  Write a python function to find the sum of an array.
  """
  sum = 0
  for i in arr:
    sum += i
  return sum

def _max(arr):  
  """
  Write a python function to find the maximum element in an array.
  """
  max = arr[0]
  for i in arr:
    if i > max:
      max