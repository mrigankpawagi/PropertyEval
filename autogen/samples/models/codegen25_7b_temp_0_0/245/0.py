def max_sum(arr): 
  """
  Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
  """
  # Time O(n) || Space O(1)
  if len(arr) == 0:
    return 0
  max_sum = 0
  for i in range(len(arr)):
    left_sum = arr[i]
    right_sum = arr[i]
    for j in range(i +