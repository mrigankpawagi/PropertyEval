def square_Sum(n):  
  """
  Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
  >>> square_Sum(2) == 20
  """
  return sum([i**2 for i in range(2,n+1,2)])

def square_Sum_2(n):
  """
  Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
  >>> square_Sum_2(2) == 20
  """