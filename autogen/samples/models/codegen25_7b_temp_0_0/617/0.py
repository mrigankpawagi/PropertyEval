def min_Jumps(steps, d): 
  """
  Write a function to check for the number of jumps required of given length to reach a point of form (d, 0) from origin in a 2d plane.
  >>> min_Jumps((3,4),11)==3.5
  """
  if d == 0:
    return 0
  if d == 1:
    return 1
  if d == 2:
    return 2
  if d == 3:
    return 3
  if d == 4:
    return 4
  if d == 5:
    return 5
  if d == 6:
    return