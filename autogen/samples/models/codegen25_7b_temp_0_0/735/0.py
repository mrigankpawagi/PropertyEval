def set_middle_bits(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def toggle_middle_bits(n): 
  """
  Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
  >>> toggle_middle_bits(9) == 15
  """
  n = n ^ (n >> 1)
  n = n ^ (n >> 2)
  n = n ^ (n >> 4)
  n = n ^ (n >> 8)
  n = n ^ (n >> 16)
  return n
def toggle_middle_bits_2(n):
  """
 