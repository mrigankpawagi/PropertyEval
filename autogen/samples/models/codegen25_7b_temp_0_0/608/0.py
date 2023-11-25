def bell_Number(n): 
  """
  Write a python function to find nth bell number.
  """
  if n == 0: 
    return 0
  elif n == 1: 
    return 1
  else: 
    return bell_Number(n-1) + bell_Number(n-2)

def fibonacci(n):
  """
  Write a python function to find nth fibonacci number