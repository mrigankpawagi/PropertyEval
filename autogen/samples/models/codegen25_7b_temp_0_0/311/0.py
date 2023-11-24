def set_left_most_unset_bit(n): 
  """
  Write a python function to set the left most unset bit.
  >>> set_left_most_unset_bit(10) == 14
  """
  return n | (n + 1)

def set_right_most_unset_bit(n): 
  """
  Write a python function to set the right most unset bit.
  >>> set_right_most_unset_bit(10) == 13
  """
  return n ^ (n - 1)