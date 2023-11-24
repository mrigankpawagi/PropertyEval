def combinations_list(list1):
  """
  Write a function to find all possible combinations of the elements of a given list.
  >>> combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
  """
  return [[]] + [[list1[0]] + x for x in combinations_list(list1[1:])]

def combinations_list_2(list1):
  """
  Write a function to find all possible combinations of the elements of a given list.
  >>> combinations_list_2(['orange', 'red',