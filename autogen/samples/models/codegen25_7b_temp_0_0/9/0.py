def find_Rotations(str): 
  """
  Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
  """
  count = 0
  for i in range(len(str)):
    if str[i:] + str[:i] == str:
      count += 1
  return count

def find_Rotations_2(str):
  """
  Write a python function to find the minimum number of rotations (greater than 0