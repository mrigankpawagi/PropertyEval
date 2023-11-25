def issort_list(list1):
  """
  Write a function to check whether a specified list is sorted or not.
  """
  for i in range(len(list1)-1):
    if list1[i] > list1[i+1]:
      return False
  return True

def issort_tuple(tuple1):
  """
  Write a function to check whether a specified tuple is sorted or not.
  """
  for