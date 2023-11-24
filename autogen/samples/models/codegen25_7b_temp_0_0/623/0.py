def nth_nums(nums,n):
  """
  Write a function to compute the n-th power of each number in a list.
  >>> nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  """
  return [i**n for i in nums]

def is_palindrome(s):
  """
  Write a function to check if a string is a palindrome.
  >>> is_palindrome("racecar")
  True
  >>> is_palindrome("hello")
  False
  """
