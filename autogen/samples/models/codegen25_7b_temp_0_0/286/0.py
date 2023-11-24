def max_sub_array_sum_repeated(a, n, k): 
  """
  Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
  >>> max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
  """
  # Time complexity: O(n)
  # Space complexity: O(1)
  if n == 0:
    return 0
  if n == 1:
    return a[0]
  if k == 0:
    return max(a)
  if k == 1:
    return max(a) * n
