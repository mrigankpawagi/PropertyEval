def sum_Of_Subarray_Prod(arr):
  """
  Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
  >>> sum_Of_Subarray_Prod([1,2,3]) == 20
  """
  return sum([x*y for x in arr for y in arr])

def sum_Of_Subarray_Prod_2(arr):
  """
  Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of