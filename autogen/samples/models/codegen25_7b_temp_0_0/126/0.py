def sum(a,b): 
  """
  Write a python function to find the sum of common divisors of two given numbers.
  """
  sum = 0
  for i in range(1, min(a,b)+1):
    if a%i == 0 and b%i == 0:
      sum += i
  return sum

def sum_of_divisors(n):
  """
  Write a python function to find the sum of all divis