def all_Bits_Set_In_The_Given_Range(n,l,r):  
  """
  Write a python function to check whether all the bits are unset in the given range or not.
  """
  if (n & (2**l-1)) == (2**l-1):
    return True
  else:
    return False

def all_Bits_Set_In_The_Given_Range(n,l,r):  
  """
  Write a python function to check whether all the bits are unset