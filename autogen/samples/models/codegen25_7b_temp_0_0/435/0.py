def last_Digit(n) :
  """
  Write a python function to find the last digit of a given number.
  """
  return n % 10

def first_Digit(n) :
  """
  Write a python function to find the first digit of a given number.
  """
  return n // 10**(len(str(n))-1)

def sum_of_digits(n) :
  """
  Write a