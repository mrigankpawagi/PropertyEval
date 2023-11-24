def sort_sublists(list1):
  """
  Write a function to sort each sublist of strings in a given list of lists.
  >>> sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
  """
  for sublist in list1:
    sublist.sort()
  return list1

def sort_sublists_2(list1):
  """
  Write a function to sort each sublist of strings in a given list of lists.
  >>> sort_sublists_2([['green', 'orange'], ['black',