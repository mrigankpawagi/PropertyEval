def bell_number(n):   
  """
  Write a function to find the number of ways to partition a set of Bell numbers.
  >>> bell_number(2)==2
  """
  if n==0:
    return 1
  else:
    return bell_number(n-1)*(n+1)

def fibonacci(n):
  """
  Write a function to find the nth Fibonacci number.
  >>> fibonacci(0)==0
  >>> fibonacci(