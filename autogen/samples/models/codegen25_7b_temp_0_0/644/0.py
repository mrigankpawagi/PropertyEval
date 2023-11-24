def reverse_Array_Upto_K(input, k): 
  """
  Write a python function to reverse an array upto a given position.
  >>> reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
  """
  return input[:k][::-1] + input[k:]

def reverse_Array_Between_K_and_M(input, k, m): 
  """
  Write a python function to reverse an array between a given position.
  >>> reverse_Array_Between_K_and_M([1, 2,