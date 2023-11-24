import math
def volume_sphere(r):
  """
  Write a function to find the volume of a sphere.
  >>> math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
  """
  return (4/3)*math.pi*(r**3)

def volume_cube(l):
  """
  Write a function to find the volume of a cube.
  >>> math.isclose(volume_cube(10), 1000, rel_tol=0.001)
  """
  return l**3