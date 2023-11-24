def first_Digit(n) :  
  """
  Write a python function to find the first digit of a given number.
  >>> first_Digit(123) == 1
  """
  return int(n/10**(len(str(n))-1))

def second_Digit(n) :  
  """
  Write a python function to find the second digit of a given number.
  >>> second_Digit(123) == 2
  """
  return int(n/10**(len