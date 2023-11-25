def find_Max_Num(arr) : 
  """
  Write a python function to find the largest number that can be formed with the given list of digits.
  """
  arr.sort()
  arr.reverse()
  return int("".join(map(str, arr)))

def find_Min_Num(arr) : 
  """
  Write a python function to find the smallest number that can be formed with the given list of digits.
  """
  arr.sort()
  return