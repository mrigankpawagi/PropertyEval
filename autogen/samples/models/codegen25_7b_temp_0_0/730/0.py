from itertools import groupby
def consecutive_duplicates(nums):
  """
  Write a function to remove consecutive duplicates of a given list.
  >>> consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
  """
  return [k for k, g in groupby(nums)]

def remove_duplicates(nums):
  """
  Write a function to remove duplicates from a given list.
  >>> remove_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6,