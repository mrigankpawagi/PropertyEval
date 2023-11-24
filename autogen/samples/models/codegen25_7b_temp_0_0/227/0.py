def min_of_three(a,b,c): 
  """
  Write a function to find minimum of three numbers.
  >>> min_of_three(10,20,0)==0
  """
  if a<b and a<c:
    return a
  elif b<a and b<c:
    return b
  else:
    return c

def is_palindrome(s):
  """
  Write a function to check whether a string is palindrome or not.
  >>> is_pal