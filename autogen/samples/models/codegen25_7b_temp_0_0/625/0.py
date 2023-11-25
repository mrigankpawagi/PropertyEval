def swap_List(newList): 
  """
  Write a python function to interchange the first and last element in a given list.
  """
  newList[0], newList[-1] = newList[-1], newList[0]
  return newList

def reverse_List(newList):
  """
  Write a python function to reverse a given list.
  """
  newList.reverse()
  return newList

def sort_List