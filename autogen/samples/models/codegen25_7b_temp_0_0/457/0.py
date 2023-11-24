def Find_Min(lst): 
  """
  Write a python function to find the sublist having minimum length.
  >>> Find_Min([[1],[1,2],[1,2,3]]) == [1]
  """
  return min(lst, key=len)

def Find_Max(lst): 
  """
  Write a python function to find the sublist having maximum length.
  >>> Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
  """
  return