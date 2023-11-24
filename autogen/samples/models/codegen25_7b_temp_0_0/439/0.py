def multiple_to_single(L):
  """
  Write a function to join a list of multiple integers into a single integer.
  >>> multiple_to_single([11, 33, 50])==113350
  """
  return int("".join(str(i) for i in L))

def is_palindrome(n):
  """
  Write a function to check if a number is a palindrome.
  >>> is_palindrome(121)
  True
  >>> is_palindrome(1221)
  True