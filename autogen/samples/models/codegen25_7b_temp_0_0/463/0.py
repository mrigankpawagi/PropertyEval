def max_subarray_product(arr):
  """
  Write a function to find the maximum product subarray of the given array.
  >>> max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
  """
  max_product = arr[0]
  current_product = arr[0]
  for i in range(1, len(arr)):
    current_product = max(arr[i], current_product * arr[i])
    max_product = max(max_product, current_product)
  return max_product