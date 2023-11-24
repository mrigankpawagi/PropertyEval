def remove_odd(l):
  """
  Write a python function to remove odd numbers from a given list.
  >>> remove_odd([1,2,3]) == [2]
  """
  return [x for x in l if x % 2 == 0]

def remove_duplicates(l):
  """
  Write a python function to remove duplicates from a given list.
  >>> remove_duplicates([1,2,3,2,3,4]) == [1,2,3,4]