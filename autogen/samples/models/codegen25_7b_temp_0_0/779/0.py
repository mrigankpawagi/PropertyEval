def unique_sublists(list1):
  """
  Write a function to count the number of lists within a list. The function should return a dictionary, where every list is turned to a tuple, and the value of the tuple is the number of its occurrences.
  >>> unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
  """
  dict1 = {}
  for i in list1:
    dict1[tuple(i)] = dict1.get(tuple(i), 0) + 1
  return dict1

def unique_sublists(list1):
  """
  Write a function to count the number of lists within a list. The function should