def pair_wise(l1):
  """
  Write a function to return a list of all pairs of consecutive items in a given list.
  >>> pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
  """
  return [(l1[i], l1[i+1]) for i in range(len(l1)-1)]

def pair_wise_2(l1):
  """
  Write a function to return a list of all pairs of consecutive items in a given list.
  >>> pair_wise([1,1,2,