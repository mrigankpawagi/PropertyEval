import math
def lateralsurface_cone(r,h):
  """
  Write a function to find the lateral surface area of a cone given radius r and the height h.
  >>> lateralsurface_cone(5,12)==204.20352248333654
  """
  return math.pi*r*r+math.pi*r*h

def lateralsurface_cylinder(r,h):
  """
  Write a function to find the lateral surface area of a cylinder given radius r and the height h.
  >>> lateralsurface_cylinder(5,12)==204.