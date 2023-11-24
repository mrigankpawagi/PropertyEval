def triangle_area(r) :  
  """
  Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
  >>> triangle_area(-1) == None
  """
  if r < 0 :
    return None
  else :
    return math.sqrt(r**2 * math.pi)

def triangle_area(r) :  
  """
  Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
  >>>