def jacobsthal_num(n): 
  """
  Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
  """
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return jacobsthal_num(n-1) + jacobsthal_num(n-2)

def jacobsthal_num_rec(n):
  """
  Write