def sequential_search(dlist, item):
  """
  Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
  """
  pos = 0
  found = False
  while pos < len(dlist) and not found:
    if dlist[pos] == item:
      found = True
    else:
      pos += 1
  return (found, pos)

def ordered_sequential_search(dlist, item):
  """
