def opposite_Signs(x,y): 
  """
  Write a python function to check whether the given two integers have opposite sign or not.
  """
  if x*y < 0:
    return True
  else:
    return False

print(opposite_Signs(2,3))
print(opposite_Signs(-2,-3))
print(opposite_Signs(-2,3))
print(opposite_Signs(2,-3))

