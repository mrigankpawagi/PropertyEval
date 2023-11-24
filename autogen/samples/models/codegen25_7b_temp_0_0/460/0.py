def Extract(lst): 
  """
  Write a python function to get the first element of each sublist.
  >>> Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
  """
  return [lst[i][0] for i in range(len(lst))]

def Extract_2(lst):
  """
  Write a python function to get the first element of each sublist.
  >>> Extract_2([[1, 2], [3, 4, 5], [6, 7, 8