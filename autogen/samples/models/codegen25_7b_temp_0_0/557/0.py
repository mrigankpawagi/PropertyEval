def toggle_string(string):
  """
  Write a function to toggle the case of all characters in a string.
  >>> toggle_string("Python")==("pYTHON")
  """
  return string.swapcase()

def is_palindrome(string):
  """
  Write a function to check if a string is a palindrome.
  >>> is_palindrome("racecar")
  True
  >>> is_palindrome("python")
  False
  """
  return string ==