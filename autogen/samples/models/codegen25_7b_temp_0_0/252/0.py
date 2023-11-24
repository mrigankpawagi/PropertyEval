import cmath  
def convert(numbers):    
  """
  Write a python function to convert complex numbers to polar coordinates.
  >>> convert(1) == (1.0, 0.0)
  """
  return cmath.polar(numbers)

def convert1(numbers):
  """
  Write a python function to convert polar coordinates to complex numbers.
  >>> convert1(1, 0) == 1.0
  """
  return cmath.rect(numbers[0], numbers[1])

def convert