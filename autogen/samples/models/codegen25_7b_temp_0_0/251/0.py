def insert_element(list,element):
  """
  Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
  """
  new_list = []
  for i in range(len(list)):
    new_list.append(element)
    new_list.append(list[i])
  return new_list

def remove_element(list,element):
  """
  Write a function that takes in a list and an element and removes