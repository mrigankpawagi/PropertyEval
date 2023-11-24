import math
def area_tetrahedron(side):
  """
  Write a function to caluclate the area of a tetrahedron.
  >>> area_tetrahedron(3)==15.588457268119894
  """
  return (4*math.pow(side,2))/3

def area_cube(side):
  """
  Write a function to caluclate the area of a cube.
  >>> area_cube(3)==27
  """
  return 6*math.pow(side,2)

def area