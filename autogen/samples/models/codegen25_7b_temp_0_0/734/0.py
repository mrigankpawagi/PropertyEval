def sum_Of_Subarray_Prod(arr):
  """
  Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
  """
  n = len(arr)
  sum = 0
  for i in range(n):
    for j in range(i, n):
      sum += arr[i] * arr[j]
  return sum

def sum_Of_Subarray_Prod_2(arr):
  """
  Write a python function