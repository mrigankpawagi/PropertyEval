def count_samepair(list1,list2,list3):
  """
  Write a function to count number items that are identical in the same position of three given lists.
  """
  count = 0
  for i in range(len(list1)):
    if list1[i] == list2[i] and list2[i] == list3[i]:
      count += 1
  return count

def count_samepair_2(list1,list2,list3):
  """
