import math
def surfacearea_sphere(r):
  """
  Write a function to find the surface area of a sphere.
  >>> math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
  """
  return 4 * math.pi * r**2

def volume_sphere(r):
  """
  Write a function to find the volume of a sphere.
  >>> math.isclose(volume_sphere(10), 4188.79020478639, rel_tol=0.001)
  """
 