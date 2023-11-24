def check_element(list,element):
  """
  Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
  >>> check_element(["green", "orange", "black", "white"],'blue')==False
  """
  for i in list:
    if i!=element:
      return False
  return True

def check_element_2(list,element):
  """
  Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
  >>> check_element_2(["