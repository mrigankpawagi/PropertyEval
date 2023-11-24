def even_bit_set_number(n): 
  """
  Write a python function to set all even bits of a given number.
  >>> even_bit_set_number(10) == 10
  """
  return n | (n >> 1)

def odd_bit_set_number(n): 
  """
  Write a python function to set all odd bits of a given number.
  >>> odd_bit_set_number(10) == 10
  """
  return n ^ (n >> 1)

def even_