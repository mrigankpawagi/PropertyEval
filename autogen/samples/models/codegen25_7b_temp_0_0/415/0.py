def max_Product(arr): 
  """
  Write a python function to find a pair with highest product from a given array of integers.
  >>> max_Product([1,2,3,4,7,0,8,4]) == (7,8)
  """
  arr.sort()
  return (arr[-1]*arr[-2], arr[-1], arr[-2])

def max_Product_2(arr): 
  """
  Write a python function to find a pair with highest product from a given array of integers.
  >>> max_Product_2([1