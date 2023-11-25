def count_Set_Bits(n): 
  """
  Write a python function to count the number of set bits (binary digits with value 1) in a given number.
  """
  count = 0
  while n: 
    count += n & 1
    n >>= 1
  return count 

def count_Set_Bits_2(n): 
  """
  Write a python function to count the number of set bits (binary digits with value 1) in a given number.
  """
