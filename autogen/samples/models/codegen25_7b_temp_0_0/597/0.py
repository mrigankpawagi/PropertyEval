def find_kth(arr1, arr2, k):
  """
  Write a function to find kth element from the given two sorted arrays.
  """
  if len(arr1) == 0:
    return arr2[k]
  if len(arr2) == 0:
    return arr1[k]
  if k == 0:
    return min(arr1[0], arr2[0])
  if k == 1:
    return max(arr1[0