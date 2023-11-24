def insert_element(list,element):
  """
  Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
  >>> insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
  """
  return [element] + list

def remove_element(list,element):
  """
  Write a function that takes in a list and an element and removes the first occurrence of the element from the list, and returns the resulting list.
  >>> remove_element(['Red', 'Green', 'Black'] ,'Red')==['Green