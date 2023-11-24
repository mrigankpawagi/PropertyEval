def swap_List(newList): 
  """
  Write a python function to interchange the first and last element in a given list.
  >>> swap_List([1,2,3]) == [3,2,1]
  """
  newList[0], newList[-1] = newList[-1], newList[0]
  return newList

def swap_List_2(newList):
  """
  Write a python function to interchange the first and last element in a given list.
  >>> swap_List_2([1,2,