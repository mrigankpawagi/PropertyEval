def is_Sub_Array(A,B): 
  """
  Write a python function to check whether a list is sublist of another or not.
  >>> is_Sub_Array([1,4,3,5],[1,2]) == False
  """
  if len(A) < len(B):
    return False
  for i in range(len(B)):
    if B[i] != A[i]:
      return False
  return True

def is_Sub_Array_2(A,B):
  """
  Write a python function to check whether a