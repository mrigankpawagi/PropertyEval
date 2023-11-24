def Find_Min_Length(lst):  
  """
  Write a python function to find the length of the smallest list in a list of lists.
  >>> Find_Min_Length([[1],[1,2]]) == 1
  """
  return min(len(lst) for lst in lst)

def Find_Max_Length(lst):  
  """
  Write a python function to find the length of the largest list in a list of lists.
  >>> Find_Max_Length([[1],[1,2]]) == 2
  """
