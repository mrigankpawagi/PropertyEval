def Find_Max(lst): 
  """
  Write a python function to find the element of a list having maximum length.
  >>> Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
  """
  return max(lst, key=len)

def Find_Min(lst): 
  """
  Write a python function to find the element of a list having minimum length.
  >>> Find_Min([['A'],['A','B'],['A','B','C']]) == ['A']
  """