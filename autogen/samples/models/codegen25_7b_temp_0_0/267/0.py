def square_Sum(n):  
  """
  Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
  """
  sum = 0
  for i in range(1, n+1, 2):
    sum += i**2
  return sum

print(square_Sum(10))

def square_Sum_2(n):
  """
  Write a python function that takes in an integer n and returns the sum of the squares of the