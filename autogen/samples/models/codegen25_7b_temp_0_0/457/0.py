def Find_Min(lst): 
  """
  Write a python function to find the sublist having minimum length.
  """
  min_len = len(lst[0]) 
  for i in range(len(lst)): 
    if len(lst[i]) < min_len: 
      min_len = len(lst[i]) 
  return min_len 

def Find_Max(lst): 