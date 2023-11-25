def min_Swaps(str1,str2) : 
  """
  Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
  """
  count = 0
  for i in range(len(str1)) : 
    if str1[i] != str2[i] : 
      count += 1
  return count//2

def min_Swaps(str1,str2) : 
  """
  Write a python function to count minimum number of