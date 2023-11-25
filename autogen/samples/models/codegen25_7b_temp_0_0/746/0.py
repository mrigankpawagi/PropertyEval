import math
def sector_area(r,a):
  """
  Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
  """
  if a > 360:
    return None
  else:
    return (r**2)*(a/360)*math.pi/180

def circle_area(r):
  """
  Write a function to find area of a circle. The function takes the radius as input.
  """
  return (r**2)*