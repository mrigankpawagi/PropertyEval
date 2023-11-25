def get_Inv_Count(arr): 
  """
  Write a python function to count inversions in an array.
  """
  count = 0
  for i in range(len(arr)): 
    for j in range(i + 1, len(arr)): 
      if (arr[i] > arr[j]): 
        count += 1
  return count 

def get_Inv_Count_Optimized(arr): 