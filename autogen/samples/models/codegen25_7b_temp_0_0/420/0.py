def cube_Sum(n): 
  """
  Write a python function to find the cube sum of first n even natural numbers.
  >>> cube_Sum(2) == 72
  """
  return sum(i**3 for i in range(2,n+1,2))

def cube_Sum_2(n):
  """
  Write a python function to find the cube sum of first n even natural numbers.
  >>> cube_Sum_2(2) == 72
  """
  return sum(i**