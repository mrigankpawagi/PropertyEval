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
  """
  n = (n & ~(1 << 1)) | (n & ~(1 << (n.bit_length() - 2))) | (n & ~(1 << (n.bit_length() - 1)))
  return n
def toggle_middle_bits_2(n): 
  """
  Write a python function to