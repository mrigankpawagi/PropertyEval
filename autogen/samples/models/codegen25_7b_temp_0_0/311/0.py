def set_left_most_unset_bit(n): 
  """
  Write a python function to set the left most unset bit.
  """
  return n | (n+1)

def set_right_most_unset_bit(n): 
  """
  Write a python function to set the right most unset bit.
  """
  return n ^ (n-1)

def set_right_most_set_bit(n): 
 