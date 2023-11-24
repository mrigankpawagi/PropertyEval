def last_Digit_Factorial(n): 
  """
  Write a python function to find the last digit in factorial of a given number.
  >>> last_Digit_Factorial(4) == 4
  """
  if n == 0:
    return 1
  else:
    return n * last_Digit_Factorial(n - 1)

def last_Digit_Palindrome(n):
  """
  Write a python function to check whether a given number is palindrome or not.
  >>> last_Digit_