def extract_index_list(l1, l2, l3):
  """
  We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
  >>> extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
  """
  l = []
  for i in range(len(l1)):
    if l1[i] in l2 and l1[i] in l3:
      l.append(l1[i])
  return l

def extract_index_list_2(l1, l2, l3):
 