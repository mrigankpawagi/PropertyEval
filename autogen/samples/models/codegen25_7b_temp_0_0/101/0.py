def kth_element(arr, k):
  """
  Write a function to find the kth element in the given array using 1-based indexing.
  """
  if k > len(arr):
    return None
  return arr[k-1]

def kth_element_2(arr, k):
  """
  Write a function to find the kth element in the given array using 1-based indexing.
  """
  if k > len(arr):
    return