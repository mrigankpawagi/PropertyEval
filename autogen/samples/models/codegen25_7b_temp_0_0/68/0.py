def is_Monotonic(A): 
  """
  Write a python function to check whether the given array is monotonic or not.
  >>> is_Monotonic([6, 5, 4, 4]) == True
  """
  return (all(A[i] <= A[i+1] for i in range(len(A)-1)) or
          all(A[i] >= A[i+1] for i in range(len(A)-1)))

def is_Monotonic_2(A):
  """
  Write a python