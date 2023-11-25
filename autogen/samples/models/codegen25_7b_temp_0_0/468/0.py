def max_product(arr):   
  """
  Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
  """
  # Time O(n) || Space O(1)
  if len(arr) < 3:
    return -1
  maxProduct = -1
  maxProductSoFar = -1
  secondMaxProductSoFar = -1
  for i in range(len(arr)):
    if arr[i] > max