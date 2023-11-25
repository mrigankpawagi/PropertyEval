def is_Monotonic(A): 
  """
  Write a python function to check whether the given array is monotonic or not.
  """
  increasing = True
  decreasing = True
  for i in range(1, len(A)):
    if A[i] < A[i-1]:
      increasing = False
    if A[i] > A[i-1]:
      decreasing = False
  return increasing or decreasing

def is_Monotonic