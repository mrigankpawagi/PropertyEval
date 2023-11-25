def divisible_by_digits(startnum, endnum):
  """
  Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
  """
  return [i for i in range(startnum, endnum+1) if all(i%int(j)==0 for j in str(i))]

print(divisible_by_digits(1,100))

# Write a function to find numbers within a given range from startnum ti endnum where every number is