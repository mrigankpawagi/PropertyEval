def find_kth(arr1, arr2, k):
  """
  Write a function to find kth element from the given two sorted arrays.
  >>> find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
  """
  if len(arr1) == 0:
    return arr2[k - 1]
  if len(arr2) == 0:
    return arr1[k - 1]
  if k == 1:
    return min(arr1[0], arr2[0])
  if arr1[0] < arr2[