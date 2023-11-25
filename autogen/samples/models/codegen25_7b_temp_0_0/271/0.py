def even_Power_Sum(n): 
  """
  Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
  """
  sum = 0
  for i in range(2, n+1, 2):
    sum += i**5
  return sum

def odd_Power_Sum(n): 
  """
  Write a python function that takes in an integer n and finds the sum of the first n odd natural numbers that are raised to the fifth power