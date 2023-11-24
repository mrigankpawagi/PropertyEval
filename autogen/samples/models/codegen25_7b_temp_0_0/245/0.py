def max_sum(arr): 
  """
  Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
  >>> max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
  """
  # Base case
  if len(arr) == 1:
    return arr[0]
  # Recursive case
  else:
    # Find the maximum sum of a bitonic subsequence for the first half of the array
    max_sum_first_half = max_sum(arr[:len(arr)//2])