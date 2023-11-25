def unique_sublists(list1):
  """
  Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
  """
  unique_list = []
  for i in list1:
    if i not in unique_list:
      unique_list.append(i)
  unique_list = tuple(unique_list)
  return {unique_list: list1.count(unique_list)}

print(unique_sublists([[1,