def is_product_even(arr): 
  """
  Write a function to check whether the product of numbers in a list is even or not.
  >>> is_product_even([1,2,3])
  """
  product = 1
  for i in arr:
    product *= i
  return product % 2 == 0

def is_product_even_2(arr):
  """
  Write a function to check whether the product of numbers in a list is even or not.
  >>> is_product_even_2([1,2