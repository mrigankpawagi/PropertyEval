def max_product(arr):   
  """
  Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
  >>> max_product([3, 100, 4, 5, 150, 6]) == 3000
  """
  max_product = 1
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      max_product = max(max_product, arr[i] * arr[j])
  return max_product

def max_product_2(arr):
  """
 