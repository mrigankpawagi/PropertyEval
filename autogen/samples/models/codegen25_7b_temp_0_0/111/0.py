def common_in_nested_lists(nestedlist):
  """
  Write a function to find the common elements in given nested lists.
  >>> set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
  """
  return set(nestedlist[0]).intersection(*nestedlist)

def common_in_nested_lists_2(nestedlist):
  """
  Write a function to find the common elements in given nested lists.
  >>> set(common_in_nested_lists_2([[12, 18, 23