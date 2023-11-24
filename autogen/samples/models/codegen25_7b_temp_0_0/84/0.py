def sequence(n): 
  """
  Write a function to find the nth number in the newman conway sequence.
  >>> sequence(10) == 6
  """
  if n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    return sequence(n-1) + sequence(n-2)

def fib(n):
  """
  Write a function to find the nth number in the fibonacci sequence.
  >>> fib(