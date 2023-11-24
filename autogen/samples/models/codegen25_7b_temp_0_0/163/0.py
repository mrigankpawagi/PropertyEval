from math import tan, pi
def area_polygon(s, l):
  """
  Write a function to calculate the area of a regular polygon given the length and number of its sides.
  >>> math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)
  """
  return (s * l) / (4 * tan(pi / l))

def area_rectangle(w, l):
  """
  Write a function to calculate the area of a rectangle given its width and length.
  >>> math.isclose(area_rectangle(4, 20), 400., rel_tol=0