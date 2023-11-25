def highest_Power_of_2(n): 
  """
  Write a python function to find the highest power of 2 that is less than or equal to n.
  """
  if n == 0:
    return 0
  else:
    return 2**(n.bit_length() - 1)

def is_palindrome(n):
  """
  Write a python function to check whether a number is palindrome or not.
  """
  n = str(n)
  return