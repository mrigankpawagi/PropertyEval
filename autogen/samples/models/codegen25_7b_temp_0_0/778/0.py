from itertools import groupby
def pack_consecutive_duplicates(list1):
  """
  Write a function to pack consecutive duplicates of a given list elements into sublists.
  """
  return [list(g) for k, g in groupby(list1)]

def pack_consecutive_duplicates_2(list1):
  """
  Write a function to pack consecutive duplicates of a given list elements into sublists.
  """
  return [list(g) for k, g in group