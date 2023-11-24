def Find_Max_Length(lst):  
  """
  Write a python function to find the length of the longest sublists.
  >>> Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
  """
  return max(len(lst) for lst in lst)

def Find_Max_Length_2(lst):  
  """
  Write a python function to find the length of the longest sublists.
  >>> Find_Max_Length_2([[1],[1,4],[5,6,7,8