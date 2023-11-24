def square_Sum(n):  
  """
  Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
  >>> square_Sum(2) == 10
  """
  return sum([i**2 for i in range(1,n+1,2)])

def square_Sum_2(n):
  """
  Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
  >>> square_Sum_2(2) == 10