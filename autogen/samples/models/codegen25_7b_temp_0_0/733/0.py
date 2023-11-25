def find_first_occurrence(A, x):
  """
  Write a function to find the index of the first occurrence of a given number in a sorted array.
  """
  low = 0
  high = len(A) - 1
  while low <= high:
    mid = (low + high) // 2
    if A[mid] == x:
      return mid
    elif A[mid] < x:
      low = mid + 1
    else:
      high = mid - 1