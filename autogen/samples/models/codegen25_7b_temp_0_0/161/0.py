def remove_elements(list1, list2):
  """
  Write a function to remove all elements from a given list present in another list.
  >>> remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
  """
  return [i for i in list1 if i not in list2]

def remove_duplicates(list1):
  """
  Write a function to remove all duplicates from a given list.
  >>> remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])