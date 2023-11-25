def count_element_in_list(list1, x): 
  """
  Write a function to count the number of sublists containing a particular element.
  """
  count = 0
  for i in list1:
    if x in i:
      count += 1
  return count

def count_element_in_list_recursive(list1, x):
  """
  Write a function to count the number of sublists containing a particular element.
  """
  count = 0