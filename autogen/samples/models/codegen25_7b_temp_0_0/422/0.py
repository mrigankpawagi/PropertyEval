def find_Average_Of_Cube(n):  
  """
  Write a python function to find the average of cubes of first n natural numbers.
  >>> find_Average_Of_Cube(2) == 4.5
  """
  sum = 0
  for i in range(1,n+1):
    sum += i**3
  return sum/n

def find_Average_Of_Square(n):  
  """
  Write a python function to find the average of squares of first n natural numbers.
  >>> find_Average_Of_Square