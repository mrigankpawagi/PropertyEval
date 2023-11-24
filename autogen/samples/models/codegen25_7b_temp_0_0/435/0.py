def last_Digit(n) :
  """
  Write a python function to find the last digit of a given number.
  >>> last_Digit(123) == 3
  """
  return n % 10

def is_Prime(n) :
  """
  Write a python function to check whether a given number is prime or not.
  >>> is_Prime(123) == False
  >>> is_Prime(2) == True
  """
  if n == 1 :
    return False
  for i