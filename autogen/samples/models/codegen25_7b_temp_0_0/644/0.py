def reverse_Array_Upto_K(input, k): 
  """
  Write a python function to reverse an array upto a given position.
  """
  input[:k] = reversed(input[:k])
  return input

def reverse_Array_Between_K_and_M(input, k, m): 
  """
  Write a python function to reverse an array between a given position.
  """
  input[k:m+1] = reversed(input