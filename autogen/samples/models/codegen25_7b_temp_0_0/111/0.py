def common_in_nested_lists(nestedlist):
  """
  Write a function to find the common elements in given nested lists.
  """
  common_elements = []
  for i in nestedlist:
    for j in i:
      if j not in common_elements:
        common_elements.append(j)
  return common_elements

print(common_in_nested_lists([[1, 2, 3], [4, 5