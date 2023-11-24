def swap_List(newList): 
  """
  Write a python function to interchange the first and last elements in a list.
  >>> swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
  """
  newList[0], newList[-1] = newList[-1], newList[0]
  return newList

def reverse_List(newList):
  """
  Write a python function to reverse a list.
  >>> reverse_List([12, 35, 9, 56, 24]) == [24, 56