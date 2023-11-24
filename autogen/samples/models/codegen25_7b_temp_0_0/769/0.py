def Diff(li1,li2):
  """
  Write a python function to get the difference between two lists.
  >>> (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
  """
  return (list(set(li1)-set(li2)))

def Remove(li1, li2):
  """
  Write a python function to remove all elements of a list that are present in another list.
  >>> (Remove([10, 15, 20, 25, 30, 35, 40], [25, 40, 35