def next_power_of_2(n): 
  """
  Write a python function to find the smallest power of 2 greater than or equal to n.
  >>> next_power_of_2(0) == 1
  """
  return 1 << (n - 1).bit_length()

def is_power_of_2(n):
  """
  Write a python function to check whether a number is a power of 2 or not.
  >>> is_power_of_2(1)
  True
  >>> is_power_of_2(