import sys
def next_smallest_palindrome(num):
  """
  Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
  """
  num = str(num)
  num = num[::-1]
  num = int(num)
  num += 1
  num = str(num)
  num = num[::-1]
  return int(num)

def next_largest_palindrome(num):
  """
  Write a