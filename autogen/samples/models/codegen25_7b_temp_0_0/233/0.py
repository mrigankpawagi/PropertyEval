def lateralsuface_cylinder(r,h):
  """
  Write a function to find the lateral surface area of a cylinder.
  >>> math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
  """
  return 2*math.pi*r*(r+h)

def lateralsuface_cone(r,h):
  """
  Write a function to find the lateral surface area of a cone.
  >>> math.isclose(lateralsuface_cone(10,5), 314.15000000000003, rel_