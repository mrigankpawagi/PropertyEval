def is_product_even(arr): 
  """
  Write a function to check whether the product of numbers in a list is even or not.
  """
  product = 1
  for i in arr:
    product *= i
  return product % 2 == 0

print(is_product_even([1, 2, 3, 4, 5]))
print(is_product_even([1, 2, 3, 4, 5, 6]))
print(is_product_