def unique_sublists(list1):
  """
  Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
  >>> unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
  """
  unique_sublists_dict = {}
  for sublist in list1:
    unique_sublists_dict[tuple(sublist)] = unique_sublists_dict.get(tuple(sublist), 0) + 1
  return unique_sublists_dict

def unique_sublists_2(list1):