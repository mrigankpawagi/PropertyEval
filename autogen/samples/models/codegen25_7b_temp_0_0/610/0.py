def remove_kth_element(list1, L):
  """
  Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
  >>> remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
  """
  return list1[:L] + list1[L+1:]

def remove_duplicates(list1):
  """
  Write a python function which takes a list and returns a list with the same elements, but with no duplicates.
  >>> remove_duplicates([1,1,2,3,4,