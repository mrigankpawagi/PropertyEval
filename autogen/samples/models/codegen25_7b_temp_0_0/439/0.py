def multiple_to_single(L):
  """
  Write a function to join a list of multiple integers into a single integer.
  """
  return int("".join(str(i) for i in L))

def single_to_multiple(n):
  """
  Write a function to split a single integer into a list of integers.
  """
  return [int(i) for i in str(n)]

def is_palindrome(n):