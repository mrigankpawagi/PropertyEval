def even_Power_Sum(n): 
  """
  Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
  >>> even_Power_Sum(2) == 1056
  """
  return sum(i**5 for i in range(2, n+1, 2))

def is_Prime(n):
  """
  Write a python function that takes in an integer n and determines whether the number is prime or not.
  >>> is_Prime(2) == True
  >>> is_Prime(3) ==