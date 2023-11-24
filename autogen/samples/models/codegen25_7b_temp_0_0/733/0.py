def find_first_occurrence(A, x):
  """
  Write a function to find the index of the first occurrence of a given number in a sorted array.
  >>> find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
  """
  low = 0
  high = len(A) - 1
  while low <= high:
    mid = (low + high) // 2
    if A[mid] == x:
      if mid == 0 or A[mid - 1] < x:
        return mid
      high = mid - 1
    elif A[