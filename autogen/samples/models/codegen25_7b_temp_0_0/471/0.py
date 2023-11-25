def find_remainder(arr, n): 
  """
  Write a python function to find the product of the array multiplication modulo n.
  """
  product = 1
  for i in arr:
    product *= i
  return product % n

def find_remainder_2(arr, n):
  """
  Write a python function to find the product of the array multiplication modulo n.
  """
  product = 1
  for i in arr:
