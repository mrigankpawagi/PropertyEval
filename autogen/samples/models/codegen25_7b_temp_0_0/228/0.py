def all_Bits_Set_In_The_Given_Range(n,l,r):  
  """
  Write a python function to check whether all the bits are unset in the given range or not.
  >>> all_Bits_Set_In_The_Given_Range(4,1,2) == True
  """
  return (n & (2**(r+1)-1)) == (2**(r+1)-1)

def all_Bits_Set_In_The_Given_Range(n,l,r):  
  """
  Write a python function to check whether all the bits are unset in the given range or not