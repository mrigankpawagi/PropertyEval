def unique_sublists(list1):
  """
  Write a function to count the number of lists within a list. The function should return a dictionary, where every list is turned to a tuple, and the value of the tuple is the number of its occurrences.
  """
  unique_list = []
  for i in list1:
    if tuple(i) not in unique_list:
      unique_list.append(tuple(i))
  return {i: list1.count(list(i)) for i in unique_list}

print(unique_sublists([[1, 2