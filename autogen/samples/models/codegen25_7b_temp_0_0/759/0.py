def is_decimal(num):
  """
  Write a function to check whether a given string is a decimal number with a precision of 2.
  """
  try:
    float(num)
    return True
  except ValueError:
    return False

def is_palindrome(num):
  """
  Write a function to check whether a given number is a palindrome number.
  """
  num = str(num)
  return num == num[::-