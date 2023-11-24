def max_Abs_Diff(arr): 
  """
  Write a python function to find the maximum difference between any two elements in a given array.
  >>> max_Abs_Diff((2,1,5,3)) == 4
  """
  arr.sort()
  return arr[-1] - arr[0]

def max_Abs_Diff_2(arr):
  """
  Write a python function to find the maximum difference between any two elements in a given array.
  >>> max_Abs_Diff_2((2,1,5,3)) == 4