def square_Sum(n):  
  """
  Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
  """
  sum = 0
  for i in range(2, n+1, 2):
    sum += i*i
  return sum

print(square_Sum(10))

def square_Sum(n):  
  """
  Write a python function takes in an integer n and returns the sum of squares of first n even natural