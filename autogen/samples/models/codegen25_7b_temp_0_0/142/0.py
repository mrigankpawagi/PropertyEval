def count_samepair(list1,list2,list3):
  """
  Write a function to count number items that are identical in the same position of three given lists.
  >>> count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
  """
  count=0
  for i in range(len(list1)):
    if list1[i]==list2[i] and list2[i]==list3[i]:
      count+=1
  return count

def count_samepair_2(list1,list2,list3):
  """
