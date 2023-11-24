from itertools import groupby
def pack_consecutive_duplicates(list1):
  """
  Write a function to pack consecutive duplicates of a given list elements into sublists.
  >>> pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
  """
  return [list(g) for k, g in groupby(list1)]

def pack_consecutive_duplicates_2(list1):
  """
  Write a function to pack consecutive duplicates of a given list elements into sublists.
  >>> pack_consecutive_duplicates_2([0,