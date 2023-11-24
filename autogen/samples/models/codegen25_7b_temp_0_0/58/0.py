def opposite_Signs(x,y): 
  """
  Write a python function to check whether the given two integers have opposite sign or not.
  >>> opposite_Signs(1,-2) == True
  """
  return x*y < 0

def is_Palindrome(x):
  """
  Write a python function to check whether the given number is palindrome or not.
  >>> is_Palindrome(121) == True
  """
  return str(x) == str(x)[::-1]

def