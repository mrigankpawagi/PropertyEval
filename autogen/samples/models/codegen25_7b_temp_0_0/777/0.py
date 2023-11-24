def find_sum(arr): 
  """
  Write a python function to find the sum of non-repeated elements in a given list.
  >>> find_sum([1,2,3,1,1,4,5,6]) == 21
  """
  return sum(set(arr))

def find_max(arr):
  """
  Write a python function to find the maximum element in a given list.
  >>> find_max([1,2,3,1,1,4,5,6]) == 6
  """
  return max(arr)

def find