def common_element(list1, list2):
  """
  Write a function that takes two lists and returns true if they have at least one common element.
  """
  for i in list1:
    for j in list2:
      if i == j:
        return True
  return False

def common_element_2(list1, list2):
  """
  Write a function that takes two lists and returns true if they have at least one common element.
  """
  return