def overlapping(list1,list2):  
  """
  Write a python function to check whether any value in a sequence exists in a sequence or not.
  >>> overlapping([1,2,3,4,5],[6,7,8,9]) == False
  """
  for i in list1:
    if i in list2:
      return True
  return False

def overlapping(list1,list2):  
  """
  Write a python function to check whether any value in a sequence exists in a sequence or not.
  >>> overlapping([1,2,3,4,5],[6