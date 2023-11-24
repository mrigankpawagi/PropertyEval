import math
def radian_degree(degree):
  """
  Write a function to convert degrees to radians.
  >>> radian_degree(90)==1.5707963267948966
  """
  return degree*math.pi/180

def radian_degree(radian):
  """
  Write a function to convert radians to degrees.
  >>> radian_degree(1.5707963267948966)==90
  """
  return radian*180/math.pi

def sin(rad