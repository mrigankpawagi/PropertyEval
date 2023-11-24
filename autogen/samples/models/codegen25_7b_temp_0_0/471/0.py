def find_remainder(arr, n): 
  """
  Write a python function to find the product of the array multiplication modulo n.
  >>> find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
  """
  product = 1
  for i in arr:
    product = product * i
  return product % n

def find_remainder_2(arr, n): 
  """
  Write a python function to find the product of the array multiplication modulo n.
  >>> find_remainder_2([ 100, 10