def find_Volume(l,b,h) : 
  """
  Write a python function to find the volume of a triangular prism.
  >>> find_Volume(10,8,6) == 240
  """
  return l*b*h

def find_Area(l,b,h) : 
  """
  Write a python function to find the area of a triangular prism.
  >>> find_Area(10,8,6) == 120
  """
  return 2*(l*b + l*h + b*h