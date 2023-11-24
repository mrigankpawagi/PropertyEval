def divisible_by_digits(startnum, endnum):
  """
  Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
  >>> divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
  """
  return list(filter(lambda x: all(x%i==0 for i in str(x)), range(startnum, endnum+1)))

def divisible_by_digits(startnum, endnum):
  """
  Write a function to find numbers within a given range from startnum ti endnum where every number is