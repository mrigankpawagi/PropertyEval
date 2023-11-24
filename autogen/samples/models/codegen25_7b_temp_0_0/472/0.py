def check_Consecutive(l): 
  """
  Write a python function to check whether the given list contains consecutive numbers or not.
  >>> check_Consecutive([1,2,3,4,5]) == True
  """
  for i in range(len(l)-1):
    if l[i+1] - l[i] == 1:
      return True
  return False

def check_Consecutive_2(l):
  """
  Write a python function to check whether the given list contains consecutive numbers or not.
  >>> check