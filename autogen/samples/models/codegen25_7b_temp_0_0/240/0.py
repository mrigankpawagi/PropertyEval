def replace_list(list1,list2):
  """
  Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
  """
  list1[-1:] = list2
  return list1

print(replace_list([1,2,3,4,5], [6,7,8,9]))

def replace_list_2(list1,list2):
  """
  Write a function that takes in two lists and replaces the last