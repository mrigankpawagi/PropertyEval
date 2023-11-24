def issort_list(list1):
  """
  Write a function to check whether a specified list is sorted or not.
  >>> issort_list([1,2,4,6,8,10,12,14,16,17])==True
  """
  for i in range(len(list1)-1):
    if list1[i]>list1[i+1]:
      return False
  return True

def issort_tuple(tuple1):
  """
  Write a function to check whether a specified tuple is sorted or not.
  >>> issort_