def max_subarray_product(arr):
  """
  Write a function to find the maximum product subarray of the given array.
  """
  max_product = 1
  max_product_subarray = []
  for i in range(len(arr)):
    max_product *= arr[i]
    if max_product > max_product_subarray[-1]:
      max_product_subarray.append(max_product)
    elif