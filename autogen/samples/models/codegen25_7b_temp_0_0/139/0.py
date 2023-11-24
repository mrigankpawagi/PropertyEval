def circle_circumference(r):
  """
  Write a function to find the circumference of a circle.
  >>> math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
  """
  return 2 * math.pi * r

def circle_area(r):
  """
  Write a function to find the area of a circle.
  >>> math.isclose(circle_area(10), 314.16000000000003, rel_tol=0.001)
  """
  return math.pi * r