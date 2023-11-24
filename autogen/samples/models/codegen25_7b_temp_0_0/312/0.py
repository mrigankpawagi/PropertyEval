import math
def volume_cone(r,h):
  """
  Write a function to find the volume of a cone.
  >>> math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
  """
  return (1/3)*math.pi*r**2*h

def volume_sphere(r):
  """
  Write a function to find the volume of a sphere.
  >>> math.isclose(volume_sphere(5), 314.1592653589793, rel_tol=0.001)
