from math import tan, pi
def area_polygon(s, l):
  """
  Write a function to calculate the area of a regular polygon given the length and number of its sides.
  """
  return (s * l) / (4 * tan(pi / l))

def area_triangle(b, h):
  """
  Write a function to calculate the area of a triangle given its base and height.
  """
  return (b * h) / 2

def area_rectangle(l, w):