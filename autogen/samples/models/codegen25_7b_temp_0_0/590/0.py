import cmath
def polar_rect(x,y):
  """
  Write a function to convert polar coordinates to rectangular coordinates.
  """
  r = math.sqrt(x**2 + y**2)
  theta = math.atan(y/x)
  return r, theta

def rect_polar(r,theta):
  """
  Write a function to convert rectangular coordinates to polar coordinates.
  """
  x = r * math