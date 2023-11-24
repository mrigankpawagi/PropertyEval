def volume_cylinder(r,h):
  """
  Write a function that takes in the radius and height of a cylinder and returns the the volume.
  >>> math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
  """
  return math.pi * r**2 * h

def volume_cone(r,h):
  """
  Write a function that takes in the radius and height of a cone and returns the the volume.
  >>> math.isclose(volume_cone(10,5), 1570.7500000000002, rel_tol=0