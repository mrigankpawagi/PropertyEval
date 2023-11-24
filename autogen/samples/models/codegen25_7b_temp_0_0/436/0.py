def neg_nos(list1):
  """
  Write a python function to return the negative numbers in a list.
  >>> neg_nos([-1,4,5,-6]) == [-1,-6]
  """
  return [i for i in list1 if i < 0]

def pos_nos(list1):
  """
  Write a python function to return the positive numbers in a list.
  >>> pos_nos([-1,4,5,-6]) == [4,5]
  """
  return [i for i in