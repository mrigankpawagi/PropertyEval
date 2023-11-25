def check_element(list,element):
  """
  Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
  """
  for i in list:
    if i != element:
      return False
  return True

print(check_element([1,1,1,1],1))
print(check_element([1,2,3,4],1))

def check_element_2(list,element):
  """
  Write