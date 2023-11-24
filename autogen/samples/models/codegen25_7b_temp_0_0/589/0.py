def perfect_squares(a, b):
  """
  Write a function to find perfect squares between two given numbers.
  >>> perfect_squares(1,30)==[1, 4, 9, 16, 25]
  """
  return [i**2 for i in range(a,b+1) if i**2%a==0]

def perfect_squares2(a, b):
  """
  Write a function to find perfect squares between two given numbers.
  >>> perfect_squares2(1,30)==[1, 4,