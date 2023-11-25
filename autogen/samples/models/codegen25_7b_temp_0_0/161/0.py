def remove_elements(list1, list2):
  """
  Write a function to remove all elements from a given list present in another list.
  """
  for i in list2:
    while i in list1:
      list1.remove(i)
  return list1

def remove_duplicates(list1):
  """
  Write a function to remove all duplicates from a given list.
  """
  list1 = list(set(list1))
