def find_Average_Of_Cube(n):  
  """
  Write a python function to find the average of cubes of first n natural numbers.
  """
  sum = 0
  for i in range(1,n+1):
    sum += i**3
  return sum/n

print(find_Average_Of_Cube(10))

# Write a python program to find the average of the first n natural numbers.

def find_Average_Of_Natural_Numbers(