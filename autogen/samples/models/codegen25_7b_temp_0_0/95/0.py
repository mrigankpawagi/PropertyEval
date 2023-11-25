def Find_Min_Length(lst):  
  """
  Write a python function to find the length of the smallest list in a list of lists.
  """
  return min(len(lst) for lst in lst)

def Find_Max_Length(lst):  
  """
  Write a python function to find the length of the largest list in a list of lists.
  """
  return max(len(lst) for lst in lst)

def