def interleave_lists(list1,list2,list3):
  """
  Write a function to interleave 3 lists of the same length into a single flat list.
  >>> interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
  """
  return [list1[i] for i in range(len(list1))]+[list2[i] for i in range(len(list2))]+[list3[i] for i in range(len(list3))]

def flatten_list(list1):
  """
  Write a function to flatten