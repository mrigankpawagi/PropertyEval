def interleave_lists(list1,list2,list3):
  """
  Write a function to interleave 3 lists of the same length into a single flat list.
  """
  return [list1[i] for i in range(len(list1))] + [list2[i] for i in range(len(list2))] + [list3[i] for i in range(len(list3))]

def interleave_lists_2(list1,list2,list3):
