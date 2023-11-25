def count_integer(list1):
  """
  Write a python function that returns the number of integer elements in a given list.
  """
  count = 0
  for i in list1:
    if type(i) == int:
      count += 1
  return count

def count_string(list1):
  """
  Write a python function that returns the number of string elements in a given list.
  """
  count = 0
  for i in