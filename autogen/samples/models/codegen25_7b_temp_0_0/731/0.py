import math
def lateralsurface_cone(r,h):
  """
  Write a function to find the lateral surface area of a cone given radius r and the height h.
  """
  return math.pi*r*(r+h)

def lateralsurface_cylinder(r):
  """
  Write a function to find the lateral surface area of a cylinder given radius r.
  """
  return 2*math.pi*r*r

def lateralsurface_sphere(r):