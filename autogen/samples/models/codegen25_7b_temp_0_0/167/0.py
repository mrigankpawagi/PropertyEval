def next_power_of_2(n): 
  """
  Write a python function to find the smallest power of 2 greater than or equal to n.
  """
  return 1 << (n - 1).bit_length()

def next_power_of_2_2(n):
  """
  Write a python function to find the smallest power of 2 greater than or equal to n.
  """
  return 2**(n - 1).bit_length()

def next_power_