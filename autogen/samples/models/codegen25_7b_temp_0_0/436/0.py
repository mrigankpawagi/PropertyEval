def neg_nos(list1):
  """
  Write a python function to return the negative numbers in a list.
  """
  neg_nos = []
  for i in list1:
    if i < 0:
      neg_nos.append(i)
  return neg_nos

print(neg_nos([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))

def pos