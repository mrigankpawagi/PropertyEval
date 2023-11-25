def even_bit_set_number(n): 
  """
  Write a python function to set all even bits of a given number.
  """
  return n & (n - 1)

def odd_bit_set_number(n): 
  """
  Write a python function to set all odd bits of a given number.
  """
  return n | (n + 1)

def set_bit(n, i): 
  """
  Write a python