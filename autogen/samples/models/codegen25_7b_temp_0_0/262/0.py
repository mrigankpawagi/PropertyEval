def split_two_parts(list1, L):
  """
  Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
  >>> split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
  """
  return (list1[:L], list1[L:])

def split_two_parts_2(list1, L):
  """
  Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in