def count(lst):   
  """
  Write a python function to count true booleans in the given list.
  >>> count([True,False,True]) == 2
  """
  return sum(lst)

def sum_of_squares(lst):
  """
  Write a python function to sum the squares of the elements in the given list.
  >>> sum_of_squares([1,2,3]) == 14
  """
  return sum(x**2 for x in lst